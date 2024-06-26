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
kanom_img_path = os.getenv("COMPONENT_184_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมรังนก")
st.image(kanom_img_path)
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมรังนกมีต้นกำเนิดมาจากภาคใต้ของประเทศไทย นิยมทำกันในงานมงคลต่างๆ เช่น งานแต่งงาน งานขึ้นบ้านใหม่ งานบวช เชื่อกันว่าขนมรังนกเป็นสิริมงคล ช่วยให้ชีวิตราบรื่น เหมือนนกที่ได้สร้างรังใหม่
"""
st.markdown(multi)

col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • มันเทศ
    • น้ำตาลปี๊บ
    • เกลือ
    • น้ำมันสำหรับทอด
    """
    st.markdown(multi)

with col2:
    st.header("วิธีทำ")
    multi = """
    1. เตรียมมันเทศ: ปอกเปลือกมันเทศ ล้างน้ำให้สะอาด หั่นเป็นชิ้นบางๆ หรือขูดเส้น
    2. ทอดมันเทศ: ตั้งกระทะใส่น้ำมัน รอจนร้อน ใส่มันเทศลงไปทอดจนเหลืองกรอบ ตักขึ้นพักให้สะเด็ดน้ำมัน
    3. เตรียมน้ำเชื่อม: ตั้งหม้อใส่น้ำตาลปี๊บ น้ำเปล่า เกลือ เคี่ยวจนน้ำตาลละลาย ปิดไฟ พักไว้
    4. คลุกมันเทศกับน้ำเชื่อม: ใส่มันเทศทอดลงในชาม ราดด้วยน้ำเชื่อม คลุกเคล้าให้เข้ากัน
    5. จัดเสิร์ฟ: ตักขนมรังนกใส่จาน พร้อมเสิร์ฟ
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
