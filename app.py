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
import streamlit as st
from PIL import Image
import numpy as np
import os
import gdown

# st.title("Pothole Detection System")

model_path = "best.pt"

# ✅ Download model if not present
if os.path.exists(model_path):
    os.remove(model_path)
    url = "https://drive.google.com/uc?id=1Xclx_BRdkR32q2wdlHaT9adbuyIllrqr"
    gdown.download(url, model_path, quiet=False)


# ✅ Load model safely (fix cv2 crash)
@st.cache_resource
def load_model():
    import os

    os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"  # safety fix
    from ultralytics import YOLO

    return YOLO(model_path)
    # from ultralytics import YOLO

    # return YOLO(model_path)


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
