from yaspin import yaspin
from termcolor import colored
from keys import OPENAI_API_KEY


with yaspin(text="Waking agent...") as spinner:
    import os
    import time
    import requests
    import base64
    import threading
    import scipy.io.wavfile as wav
    from queue import Queue
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    from pygame import mixer

    from modules.Whisper import transcribe
    from modules.VoiceActivityDetection import VADDetector
    import openai
    from gtts import gTTS
    from modules.command import CommandDetector

    from modules.Yolo import Eyes
    # from modules.google import GoogleManager
    # from modules.github import create_repository

    openai.api_key = OPENAI_API_KEY
    mixer.init()


class GPTAssistant():

    def __init__(self, startListening=False, startTexting=False, voice=False, local=False):

        self.voice = voice
        self.listening = startListening
        self.texting = startTexting
        self.vad = VADDetector(self.onSpeechStart, self.onSpeechEnd)
        self.vad_data = Queue()
        self.context = [
            {"role": "system", "content": self.read_system_context("jvp.txt")}]

        self.cdet = CommandDetector(model_path="./models/checkpoint-760")
        # self.google = GoogleManager()
        self.eyes = Eyes()

        if startListening and not startTexting:
            self.startListening()

            t = threading.Thread(target=self.transcription_loop)
            t.start()

        else:
            self.writingMessage()

    def writingMessage(self):

        text = ''

        while True:

            text = input(colored("[👨]: ", "magenta"))

            self.build_context(role='user', content=text)

            command = self.cdet.command_filter(text)

            if (command != 'goodbye'):

                if command == "vision":

                    vision = self.eyes.see()

                    self.build_context(
                        role='system', content=f'The vision module detected {vision}. Respond to the last user promt using this information.')

                if command == "google":

                    self.google.get_query(text)

                    if (self.voice):
                        self.play_audio(response=self.google.notification,
                                        exit=exit, response_name="google_notification.mp3")

                    search = self.google.search()

                    self.build_context(
                        role='system', content=f'The google module found {search}. Respond to the last user promt using this information.')

                if command == "github":

                    repo = create_repository()

                    self.build_context(
                        role='system', content=f'The github module tried to create a repository and exited:\n {repo}. Tell the user what happened.')

                self.send_to_GPT(messages=self.context)

            else:

                self.send_to_GPT(messages=self.context)

                break

    def startListening(self):
        print(colored("Listening 👂", 'green'))
        t = threading.Thread(target=self.vad.startListening)
        t.start()

    def toggleListening(self):
        if not self.listening:
            print()
            print(colored("Listening 👂", 'green'))

        while not self.vad_data.empty():
            self.vad_data.get()
        self.listening = not self.listening

    def onSpeechStart(self):
        pass

    def onSpeechEnd(self, data):
        if data.any():
            self.vad_data.put(data)

    def transcription_loop(self):
        while True:
            if not self.vad_data.empty():
                data = self.vad_data.get()

                if self.listening:
                    self.toggleListening()

                text = transcribe(data)

                if len(text) > 4 and text != "Thank you.":

                    print(colored(f'[👨]:{text}', 'magenta'))

                    self.build_context(role='user', content=text)

                    command = self.cdet.command_filter(text)

                    if (command != 'goodbye'):

                        if command == "vision":

                            vision = self.eyes.see()

                            self.build_context(
                                role='system', content=f'The vision module detected {vision}. Respond to the last user promt using this information.')

                        if command == "google":

                            self.google.get_query(text)

                            if (self.voice):
                                self.play_audio(
                                    response=self.google.notification, exit=exit, response_name="google_notification.mp3")

                            search = self.google.search()

                            self.build_context(
                                role='system', content=f'The google module found {search}. Respond to the last user promt using this information.')

                        self.send_to_GPT(messages=self.context)

                    else:

                        self.send_to_GPT(messages=self.context, exit=True)

                        break

    def read_system_context(self, file):

        context = ''

        with open(file) as f:

            lines = f.readlines()

            for line in lines:

                context += line

        return context

    def build_context(self, role, content):

        self.context.append({"role": role, "content": content})

    def send_to_GPT(self, messages, exit=False):

        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages)

        response = completion['choices'][0]['message']['content']

        print(colored(f'[🤖]:{response}', 'green'))

        self.build_context(role='assistant', content=response)
        if (self.voice):
            self.play_audio(response=response, exit=exit)

    def play_audio(self, response, language="en", exit=False, response_name="GPT_response.mp3"):

        speech = gTTS(text=response, lang=language, slow=False)

        speech.save(response_name)

        # play audio
        mixer.music.load(response_name)
        mixer.music.play()

        # wait for audio to finish
        duration = mixer.Sound(response_name).get_length()
        time.sleep(duration + 1)

        # unload and delete audio
        mixer.music.unload()
        os.remove(response_name)

        # re-activate microphone
        if (self.listening and not exit):
            self.toggleListening()


if __name__ == '__main__':

    assistant = GPTAssistant(
        startListening=True, startTexting=True, voice=False, local=False)

    context = [{"role": "user", "content": "Testing GPT"}]
    assistant.send_to_GPT(messages=context)
