# import streamlit as st

# picture = st.camera_input("Take a picture")

# # display the picture
# st.image(picture, caption="Your picture", use_column_width=True)

from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")
  