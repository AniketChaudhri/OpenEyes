import streamlit as st
from PIL import Image
from ultralytics import YOLO

# initialize the model
model = YOLO("yolov8n.pt")

# radio button to upload a picture or take a picture from webcam
st.sidebar.subheader("Select Input Source")
input_type = st.sidebar.radio(" ", ("Upload an Image", "Take a Picture"))

global picture

if input_type == "Upload an Image":
    picture = st.file_uploader("Select an image", type=["jpg", "jpeg", "png"])
else:
    # display the picture
    picture = st.camera_input("Take a picture")


if picture:
    st.image(picture, caption="Your picture", use_column_width=True)

    # save the picture
    with open("image.jpg", "wb") as f:
        f.write(picture.getvalue())  # write the picture to the disk

    st.info("Select the confidence threshold for the object detection model and press Detect Objects")

    # confidence slider
    st.sidebar.subheader("Confidence Threshold")
    confidence_threshold = st.sidebar.slider("Select a value", 0.0, 1.0, 0.5, 0.01)

    source_img = Image.open("image.jpg")

    if st.sidebar.button("Detect Objects"):
        # start the detection
        res = model.predict(source_img, conf=confidence_threshold)
        boxes = res[0].boxes
        res_plotted = res[0].plot()[:, :, ::-1]
        st.image(res_plotted, caption="Detected Image", use_column_width=True)

        st.balloons()

        st.success("Head over to the chat page to ask questions and link to the page")
