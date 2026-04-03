import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO

st.title("Pothole Detection System")

# ✅ Load model directly from repo
model = YOLO("best.pt")

uploaded_file = st.file_uploader("Upload Image")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Detect"):
        results = model(np.array(image), conf=0.2)
        st.image(results[0].plot())
