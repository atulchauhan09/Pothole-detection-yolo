# import streamlit as st
# from ultralytics import YOLO
# from PIL import Image
# import numpy as np

# st.title("Pothole Detection System")

# model = YOLO("runs/detect/train/weights/best.pt")  # replace with best.pt later

# uploaded_file = st.file_uploader("Upload Image")

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image")

#     if st.button("Detect"):
#         results = model(image, conf=0.2)
#         result_img = results[0].plot()
#         st.image(result_img, caption="Detection Result")
# import streamlit as st
# from ultralytics import YOLO
# from PIL import Image
# import numpy as np
# import os

# st.title("Pothole Detection System")

# model_path = "runs/detect/train/weights/best.pt"

# if not os.path.exists(model_path):
#     st.error("Model not found! Please train first.")
#     st.stop()

# model = YOLO(model_path)

# uploaded_file = st.file_uploader("Upload Image")

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image")

#     if st.button("Detect"):
#         image_np = np.array(image)
#         results = model(image_np, conf=0.2)

#         result_img = results[0].plot()
#         st.image(result_img, caption="Detection Result")
# import streamlit as st

# from ultralytics import YOLO
# from PIL import Image
# import numpy as np
# import os

# st.title("Pothole Detection System")

# model_path = "best.pt"  # ✅ FIXED

# if not os.path.exists(model_path):
#     st.error("Model not found! Please check path.")
#     st.stop()

# model = load_model()

# uploaded_file = st.file_uploader("Upload Image")

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image")

#     if st.button("Detect"):
#         image_np = np.array(image)
#         results = model(image_np, conf=0.2)

#         result_img = results[0].plot()
#         st.image(result_img, caption="Detection Result")


# import streamlit as st
# from PIL import Image
# import numpy as np
# import os

# st.title("Pothole Detection System")

# model_path = "best.pt"


# # ✅ DEFINE FUNCTION FIRST
# @st.cache_resource
# def load_model():
#     from ultralytics import YOLO

#     return YOLO(model_path)


# # ✅ THEN USE IT
# if not os.path.exists(model_path):
#     st.error("Model not found! Please check path.")
#     st.stop()

# model = load_model()

# uploaded_file = st.file_uploader("Upload Image")

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image")

#     if st.button("Detect"):
#         image_np = np.array(image)
#         results = model(image_np, conf=0.2)

#         result_img = results[0].plot()
#         st.image(result_img, caption="Detection Result")
# import streamlit as st
# from PIL import Image
# import numpy as np
# import os
# import gdown

# # st.title("Pothole Detection System")

# model_path = "best.pt"

# # ✅ Download model if not present
# if os.path.exists(model_path):
#     os.remove(model_path)
#     url = "https://drive.google.com/uc?id=1Xclx_BRdkR32q2wdlHaT9adbuyIllrqr"
#     gdown.download(url, model_path, quiet=False)


# # ✅ Load model safely (fix cv2 crash)
# @st.cache_resource
# def load_model():
#     import os

#     os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"  # safety fix
#     from ultralytics import YOLO

#     return YOLO(model_path)
#     # from ultralytics import YOLO

#     # return YOLO(model_path)


# model = load_model()

# uploaded_file = st.file_uploader("Upload Image")

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image")

#     if st.button("Detect"):
#         image_np = np.array(image)
#         results = model(image_np, conf=0.2)

#         result_img = results[0].plot()
#         st.image(result_img, caption="Detection Result")
# import streamlit as st
# from PIL import Image
# import numpy as np
# import os
# import requests

# st.title("Pothole Detection System")

# MODEL_PATH = "best.pt"


# @st.cache_resource
# def load_model():
#     # ✅ Download ONLY if not exists
#     if not os.path.exists(MODEL_PATH):
#         url = "https://drive.google.com/uc?export=download&id=1Xclx_BRdkR32q2wdlHaT9adbuyIllrqr"

#         with st.spinner("Downloading model..."):
#             response = requests.get(url, stream=True)

#             with open(MODEL_PATH, "wb") as f:
#                 for chunk in response.iter_content(chunk_size=8192):
#                     if chunk:
#                         f.write(chunk)

#     from ultralytics import YOLO

#     return YOLO(MODEL_PATH)


# model = load_model()

# uploaded_file = st.file_uploader("Upload Image")

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image")

#     if st.button("Detect"):
#         image_np = np.array(image)
#         results = model(image_np, conf=0.2)

#         result_img = results[0].plot()
#         st.image(result_img, caption="Detection Result")
import streamlit as st
from PIL import Image
import numpy as np
import os
import requests

st.title("Pothole Detection System")

MODEL_PATH = "best.pt"
FILE_ID = "1Xclx_BRdkR32q2wdlHaT9adbuyIllrqr"


@st.cache_resource
def load_model():

    def download_file_from_google_drive(file_id, destination):
        URL = "https://drive.google.com/uc?export=download"

        session = requests.Session()
        response = session.get(URL, params={"id": file_id}, stream=True)

        # ✅ Handle large file confirmation (IMPORTANT)
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                response = session.get(
                    URL,
                    params={"id": file_id, "confirm": value},
                    stream=True,
                )
                break

        with open(destination, "wb") as f:
            for chunk in response.iter_content(32768):
                if chunk:
                    f.write(chunk)

    # ✅ Download if file missing OR corrupted
    if (not os.path.exists(MODEL_PATH)) or os.path.getsize(MODEL_PATH) < 1_000_000:
        with st.spinner("Downloading model..."):
            download_file_from_google_drive(FILE_ID, MODEL_PATH)

    from ultralytics import YOLO

    return YOLO(MODEL_PATH)


model = load_model()

uploaded_file = st.file_uploader("Upload Image")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    if st.button("Detect"):
        image_np = np.array(image)
        results = model(image_np, conf=0.2)

        result_img = results[0].plot()
        st.image(result_img, caption="Detection Result")
