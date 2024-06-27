from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
# Get the paths from the environment
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_233_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมอินทนิล")
st.image(kanom_img_path, width=850)
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")

multi = """
ส่วนผสม แป้งอินทนิล  
แป้งถั่วเขียว 20 กรัม  
แป้งมัน 80 กรัม  
น้ำใบเตย 500 กรัม (ปั่นใบเตย 3/4 ถ้วย + อัญชัญ 10 ดอก + น้ำ 500 กรัม)  
น้ำตาลทราย 100 กรัม  
"""
st.markdown(multi)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
     
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
   
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
