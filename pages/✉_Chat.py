# import openai
import streamlit as st
import requests
import time
import base64
import json

st.set_page_config(
    page_title="OpenEyes",
    page_icon="👀",
)

st.title("OpenEyes")

# API_KEY = st.secrets["OPENAI_API_KEY"]


def makeRequest(prompt):
    url = "http://3.88.181.187:8080/v1/"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"  # setting up a session state model

if "messages" not in st.session_state:
    # st.session_state.messages = [] # setting up a session state messages to store the messages
    # set a default message hi to the bot before the user types anything
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi, I'm OpenEyes. I'm here to help you with your queries related to Animals. What do you want to know?",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):  # creating a chat message with the role
        st.markdown(message["content"])  # adding the content to the chat message


from transformers import pipeline
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
)


@st.cache_resource()
class CommandDetector:
    def __init__(self, model_path, tokenizer="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.classifier = pipeline(
            "text-classification", model=model_path, tokenizer=tokenizer
        )

    def command_filter(self, prompt):
        # Classify the input prompt
        result = self.classifier(prompt)
        command_id = int(result[0]["label"].split("_")[-1])
        command = {0: "vision", 1: "chat", 2: "goodbye", 3: "other", 4: "other", 5: "other"}[command_id]

        return command


# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # # Classify the input prompt as intent
    # get the model path from ../../models/checkpoint-760
    mycd = CommandDetector(model_path="./models/checkpoint-760")
    # st.write(intent)
    intent = mycd.command_filter(prompt)
    st.write(intent)
    if intent == "vision":
        # st.info("Head over to the camera page to take a picture 📷")
        st.session_state.messages = []
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Head over to the camera page to take a picture 📷",
            }
        )
        st.experimental_rerun()
    elif intent == "goodbye":
        st.session_state.messages = []
        # st.info("Bye 👋")
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Bye 👋, loved talking to you. See you soon!",
            }
        )
        st.experimental_rerun()
    else:
        # st.info("Head over to the chat page to ask questions and link to the page")
        pass

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response = makeRequest(prompt)
        for chunk in response["choices"][0]["message"]["content"].split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )


# 3 cols
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Export Chat History"):
        # Download the chat history as a json file
        # Convert JSON data to a string and encode as UTF-8
        json_data = json.dumps(st.session_state.messages).encode("utf-8")

        b64 = base64.b64encode(json_data).decode()
        href = f'<a href="data:application/json;base64,{b64}" download="example.json">Download JSON</a>'
        st.markdown(href, unsafe_allow_html=True)

with col3:
    # Clear chat button
    if st.button("Clear Chat"):
        # remove all the messages from the session state
        st.session_state.messages = []
        # add a default message to the session state
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Hi, I'm OpenEyes. I'm here to help you with your queries related to Animals. What do you want to know?",
            }
        )
        # rerun the app
        st.experimental_rerun()

# print(st.session_state.messages)
