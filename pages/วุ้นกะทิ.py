from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_200_PATH1")

# Set page configuration
st.set_page_config(
    page_title="วุ้นกะทิ: ขนมไทยโบราณ หวานละมุน ทานเย็นสดชื่น",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("วุ้นกะทิ: ขนมไทยโบราณ หวานละมุน ทานเย็นสดชื่น")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        วุ้นกะทิ เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว หอมหวานจากกะทิ รสชาติละมุน ทานเย็นสดชื่น ที่นิยมทานคู่กับขนมชั้น หรือหมี่เล็กน้ำแข็ง
    """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ส่วนผสม**
        - กะทิ 400 มล.
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - ผงวุ้น 1 ช้อนชา
        - เกลือป่น 1/4 ช้อนชา
        - น้ำเปล่า 1 ถ้วยตวง
        - น้ำมะพร้าว 1/2 ถ้วยตวง
        - เอ็นเอ็ม หรือแป้งมัน 1 ช้อนชา
        
        **วิธีทำ**
        1. ต้มกะทิ: ตั้งหม้อ ตั้งไฟกลาง ใส่กะทิ ตามด้วยน้ำตาลทราย คนให้น้ำตาลละลาย
        2. ผสมวุ้น: ผสมผงวุ้นกับน้ำเปล่า คนให้ละลาย พักไว้ 10 นาที
        3. เทน้ำวุ้น: เทน้ำวุ้นลงในกะทิ คนให้เข้ากัน
        4. ตั้งไฟเบา: ตั้งไฟเบา ต้มจนกะทิเดือดพอเหมาะ พักไว้ 5 นาที
        5. เทน้ำมะพร้าว: เทน้ำมะพร้าวลงในหม้อ คนให้เข้ากัน
        6. ตั้งไฟกลาง: ตั้งไฟกลาง คนเอ็นเอ็มลงไป คนให้เข้ากัน
        7. ตั้งไฟเบา: ตั้งไฟเบา พักไว้ 3-5 นาที
        8. พัก: พักให้เย็น นำไปพักเย็นในตู้เย็น 2 ชั่วโมง
        
    """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - ใช้กะทิที่หอม
        - ใส่น้ำมะพร้าวเพิ่มความหอมหวาน
        - คนให้เข้ากันในขั้นตอนการผสมวุ้น
        - พักเย็นในตู้เย็นก่อนทาน
    """
    )

st.page_link("Home.py", label="Home", icon="↩️")
