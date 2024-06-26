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
kanom_img_path = os.getenv("COMPONENT_KluaiBuatchi_PATH1")
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
st.title("กล้วยบวชชี")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
กล้วยบวชชี เป็นขนมหวานชนิดหนึ่งที่คนทั่วไปรู้จักเป็นอย่างดี ซึ่งเป็นขนมที่ดูเหมือน ธรรมดา 
แต่มีความเป็นเอกลักษณ์โดยเฉพาะกล้วยน้ำว้า มะพร้าวหรือน้ำกะทิเป็นวัตถุดิบที่คนไทยนำมาใช้ประกอบอาหาร 
ตั้งแต่สมัยโบราณจนปัจจุบัน หรือจะใช้กล้วยไข่ก็ได้

การทำกล้วยบวชชีในตำรับนี้ผู้เขียนจะใช้กะทิธัญพืชเป็นส่วนประกอบแทนกะทิทั่วไป เพื่อให้เป็นตำรับสุขภาพที่ทุกคนกินได้
       
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
        กล้วยน้ำว้าสุก ๑๒ ผล ขนาดกลาง
        
        กะทิธัญพืช ๖ ถ้วยตวง
        
        น้ำตาลทราย ๒๐๐ กรัม
        
        เกลือ ๕ กรัม
"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
        1. ปอกเปลือกกล้วยให้สะอาด หั่นให้เป็น ๔ ชิ้นต่อ ๑ ผล

        2. นำกล้วยไปต้มในน้ำเดือดให้พอสุกเพื่อเอายางออก ตักขึ้นให้สะเด็ดน้ำ
        
        3. นำกะทิตั้งไฟปานกลางให้เดือดใส่กล้วยลงไป หรี่ไฟอ่อน เพื่อให้ความหวานของกล้วยออกมา

        4. ปรุงรสด้วยน้ำตาลทราย ตามด้วยเกลือ ชิมรสให้ออกมัน หวาน เค็มเล็กน้อย รสกลมกล่อม
    """
    st.markdown(multi)
st.write(
    "หมายเหตุ การทำกล้วยบวชชีให้อร่อย กล้วยจะต้องเป็นกล้วยสวน ไม่ฝาด ไม่มีเมล็ด กะทิไม่ควรเคี่ยวจนแตกมัน เมื่อเวลากินจะติดลิ้น ปาก ไม่อร่อยชวนกิน"
)
st.page_link("Home.py", label="Home", icon="↩️")
