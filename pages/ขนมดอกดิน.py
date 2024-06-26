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
kanom_img_path = os.getenv("COMPONENT_91_PATH1")
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
st.title("ขนมดอกดิน")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ดอกดิน เป็นขนมไทยโบราณพื้นบ้านนิยมทำกันปีละครั้ง เพราะดอกดินเกิดขึ้นเองตามธรรมชาติและหาได้ยากมักขึ้นในป่าเขาในระหว่างเดือนกันยายน – ตุลาคมของทุกปี ขนมชนิดนี้ทำจากดอกดิน กะทิ แป้งข้าวเหนียว แป้งมัน น้ำตาลทราย มะพร้าวทึนทึกขูด และเกลือป่นคนโบราณนิยมทานเป็นของว่าง
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • ดอกดิน500 กรัม  
    • กะทิ 1500 กรัม  
    • แป้งข้าวเหนียว 1 กิโลกรัม  
    • แป้งมัน 500 กรัม  
    • น้ำตาลทราย 1500 กรัม  
    • มะพร้าวทึนทึกขูด 400 กรัม  
    • เกลือป่น  1 ช้อนชา  


    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
1. นำดอกดินมาล้างทำความสะอาด แล้วหั่นเป็นชิ้นพอใส่เครื่องปั่นได้

2. ใส่ดอกดินลงในโถปั่นพร้อมเติมกะทิลงไปปั่นให้ละเอียดเทใส่หม้อพักไว้ก่อน

3. เทแป้งข้าวเหนียว แป้งมัน น้ำตาลทรายผสมให้เข้ากัน หลังจากนั้นให้เทน้ำดอกดินที่ปั่นเสร็จแล้วลงไปคนให้เข้ากัน

4. มะพร้าวทึนทึกขูด ผสมเกลือป่นเล็กน้อยเตรียมไว้ สำหรับโรยหน้าขนม

5. พับกระทงใบตอง แล้วเรียงใส่ในหม้อนึ่ง โดยตักแป้งที่ผสมเสร็จแล้วใส่ลงไปพร้อมโรยหน้าด้วยมะพร้าวขูด แล้วนำไปนึ่งจนขนมสุก เป็นอันเสร็จ
    
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
