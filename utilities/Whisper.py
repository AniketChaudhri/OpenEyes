import whisper
import numpy as np
model = whisper.load_model("base")

def transcribe(audio, language="en"):
    audio = audio.flatten().astype(np.float32) / 32768.0
    audio = whisper.pad_or_trim(audio)


    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # decode the audio, remove language if you want a different language``
    options = whisper.DecodingOptions(language=language, fp16 = False)

    result = whisper.decode(model, mel, options)

    return result.text
