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
kanom_img_path = os.getenv("COMPONENT_183_PATH1")
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
st.title("ขนมรวมมิตร")
st.image(kanom_img_path)
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมรวมมิตร เป็นขนมหวานไทยโบราณที่มีเอกลักษณ์เฉพาะตัว ด้วยการรวมเอาเครื่องต่างๆ หลากหลายชนิดไว้ในถ้วยเดียว ทานคู่กับน้ำกะทิหรือน้ำเชื่อม รสชาติหวานมัน เย็นชื่นใจ เหมาะกับการทานในยามอากาศร้อน
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    - เครื่องรวมมิตร: ลอดช่อง ครองแครง ลูกชิด วุ้น ทับทิมกรอบ สาคู ขนุน เผือก ฟักทอง ลูกตาลอ่อน แปะก๊วย เม็ดแมงลัก ถั่วแดง ฯลฯ
    - น้ำกะทิ: กะทิสด น้ำตาลทราย เกลือ ใบเตย
    - น้ำเชื่อม: น้ำตาลทราย น้ำเปล่า ใบเตย
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. เตรียมเครื่องรวมมิตร:
    - ล้างและต้มเครื่องต่างๆ ให้สุก เตรียมไว้

    2. ทำน้ำกะทิ:
    - ตั้งหม้อใส่น้ำกะทิ น้ำตาลทราย เกลือ และใบเตย เคี่ยวจนน้ำกะทิเดือด ปิดไฟ พักไว้

    3. ทำน้ำเชื่อม:
    - ตั้งหม้อใส่น้ำตาลทราย น้ำเปล่า และใบเตย เคี่ยวจนน้ำตาลทรายละลาย ปิดไฟ พักไว้

    4. จัดเสิร์ฟ:
    - ตักเครื่องรวมมิตรใส่ถ้วย ราดด้วยน้ำกะทิและน้ำเชื่อม โรยน้ำแข็ง พร้อมเสิร์ฟ

    เคล็ดลับ:
    - เลือกใช้เครื่องรวมมิตรที่มีคุณภาพ สดใหม่
    - ปรับความหวานของน้ำกะทิและน้ำเชื่อมตามชอบ
    - เพิ่มเติมเครื่องต่างๆ ตามชอบ เช่น ขนมปังนึ่ง เฉาก๊วย ลอดช่องน้ำกะทิ
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
