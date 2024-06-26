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
kanom_img_path = os.getenv("COMPONENT_54_PATH1")
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
st.title("ขนมขี้มอด")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
ขนมขี้มอด เป็นขนมหวานพื้นบ้านโบราณ นิยมทานกันในภาคใต้ โดยเฉพาะแถบจังหวัดพังงา ชุมพร ระนอง และปัตตานี

ลักษณะของขนมขี้มอด : มีลักษณะคล้ายทรายละเอียด สีเหลืองนวล
มีรสชาติหวานมัน กลมกล่อม
นิยมทานเล่น หรือทานคู่กับน้ำชา กาแฟ



"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ข้าวสาร

    มะพร้าวขูด

    น้ำตาลทราย

    เกลือ

"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. นำข้าวสารไปแช่น้ำ 10 นาที แล้วผึ่งให้แห้ง

    2. นำข้าวสารและมะพร้าวขูดไปคั่วไฟปานกลางจนเหลืองกรอบ

    3. โขลกข้าวสารคั่วให้ละเอียด

    4. บดมะพร้าวคั่วให้ละเอียด

    5. ผสมข้าวสารคั่ว มะพร้าวคั่ว น้ำตาลทราย และเกลือเข้าด้วยกัน

    6. บรรจุขนมขี้มอดใส่ภาชนะ

    
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
