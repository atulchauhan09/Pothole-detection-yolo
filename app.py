import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO

st.title("Pothole Detection System")


@st.cache_resource
def load_model():
    model = YOLO("best.pt")  # YOLOv8 native loader
    return model


model = load_model()

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image")

    if st.button("Detect Potholes"):
        with st.spinner("Detecting..."):
            results = model(np.array(image))
            result_img = results[0].plot()  # draws boxes on image
            st.image(result_img, caption="Detection Result")

            # Show detection summary
            boxes = results[0].boxes
            if boxes is not None and len(boxes) > 0:
                st.success(f"Found {len(boxes)} pothole(s) detected!")
            else:
                st.info("No potholes detected.")
