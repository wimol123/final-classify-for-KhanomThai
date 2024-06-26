from ultralytics import YOLO
import streamlit as st
from PIL import Image
import numpy as np
import cv2
import random
from dotenv import load_dotenv
import os
from class_labels_name import class_labels_names

# Load variables from .env
load_dotenv()

# Get the path to the model from the environment
model_path = os.getenv("MODEL_PATH")
model = YOLO(model_path)
# Streamlit page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display the header image
HeadImg = os.getenv("HEADER_IMG_PATH")
# st.image(HeadImg)

# Page title
st.title("Classify for KhanomThai..")

# File uploader for the user to upload an image
image = st.file_uploader("Choose .jpg pic ...", type=["png", "jpg", "jpeg"])
if image:
    image = Image.open(image)
    st.image(image=image, use_column_width=True)

    st.write("")
    st.write("Detecting...")

    result = model(image)
    names = result[0].names
    probability = result[0].probs.data.numpy()
    prediction = np.argmax(probability)
    classNameinx = int(names[prediction])
    className = class_labels_names[classNameinx]
    st.title(className)
    pages = f"pages/{className}.py"
    label = f"คลิกเพื่อดูข้อมูลเพิ่มเติมเกี่ยวกับ {className}"
    st.page_link(pages, label=label, use_container_width=True, icon="🧁")
