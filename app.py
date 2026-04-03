import streamlit as st
from PIL import Image
import numpy as np
import os
import requests

st.title("Pothole Detection System")

MODEL_PATH = "best.pt"
URL = "https://github.com/atulchauhan09/Pothole-detection-yolo/releases/download/v1.0/best.pt"


def download_model():
    # 🚨 Always delete old file
    if os.path.exists(MODEL_PATH):
        os.remove(MODEL_PATH)

    st.write("Downloading model...")

    response = requests.get(URL, stream=True)

    # ✅ Check if request successful
    if response.status_code != 200:
        st.error("Failed to download model")
        st.stop()

    with open(MODEL_PATH, "wb") as f:
        for chunk in response.iter_content(8192):
            if chunk:
                f.write(chunk)

    # ✅ Debug file size
    size = os.path.getsize(MODEL_PATH)
    st.write(f"Downloaded file size: {size}")

    # 🚨 Critical check
    if size < 5_000_000:
        st.error("Downloaded file is corrupted")
        st.stop()


def load_model():
    from ultralytics import YOLO

    return YOLO(MODEL_PATH)


# 🚨 FORCE fresh download every run (for debugging)
download_model()

model = load_model()

uploaded_file = st.file_uploader("Upload Image")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Detect"):
        results = model(np.array(image), conf=0.2)
        st.image(results[0].plot())
