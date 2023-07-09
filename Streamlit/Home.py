import streamlit as st

st.set_page_config(
    page_title="OpenEyes",
    page_icon=":eyes:",
)

st.title("👀 OpenEyes")

# Welcome message
st.write("Welcome to the 👀 OpenEyes Homepage!")

# goto the chat section to talk to the bot
# st.write("Go to the chat section to talk to the bot!")
st.info(
    """👈 Go to the chat section to talk to the bot!
"""
)

with st.expander("💡 Idea"):
    st.markdown(
        """
        - The idea behind this project is to create a chatbot that can answer questions related to animals.
        - The chatbot is trained on the [AnimalQA dataset](
        https://www.kaggle.com/datasets/iamsouravbanerjee/animal-image-dataset-90-different-animals
        ) from Kaggle.
        We thought that this app will help the tourists who are visiting safari parks and zoos and want to know more about the animals they see.
        They can scan the animals from their phones and our Object Detection model will detect the animal and then the chatbot will answer the questions related to the animal.
        """
    )

with st.expander("🐍 Python Libraries Used"):
    st.markdown(
        """
        - `Streamlit` - For the frontend
        - `OpenAI` - For the chatbot
        - `Requests` - For making HTTP requests
        - `Time` - For adding delays
        - `Base64` - For encoding and decoding
        - `JSON` - For parsing JSON
        - `Pillow` - For image processing
        - `Numpy` - For numerical processing
        - `Pandas` - For data processing
        - `Matplotlib` - For data visualization
        - `YOLOv8` - For object detection
        - `PyTorch` - For deep learning
        - `Transformers` - For NLP
        - `HuggingFace` - For NLP
        - `Whisper` - For speech recognition
        - `PyAudio` - For audio processing
        
        """
    )
