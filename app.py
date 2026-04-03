import streamlit as st
from PIL import Image
import numpy as np
import torch

st.title("Pothole Detection System")


# ✅ Load YOLOv5 model (stable)
@st.cache_resource
def load_model():
    model = torch.hub.load("ultralytics/yolov5", "custom", path="best.pt")
    return model


model = load_model()

uploaded_file = st.file_uploader("Upload Image")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Detect"):
        results = model(np.array(image))
        results.render()
        st.image(results.ims[0])
