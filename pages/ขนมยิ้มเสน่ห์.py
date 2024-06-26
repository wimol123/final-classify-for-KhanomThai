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
kanom_img_path = os.getenv("COMPONENT_182_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display main image and title
st.image(image=header_img_path)
st.title("ขนมยิ้มเสน่ห์")

st.image(kanom_img_path)
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมยิ้มเสน่ห์ หรือ ขนมหัวเราะ เป็นขนมไทยโบราณชนิดหนึ่ง มีลักษณะเป็นลูกกลมๆ เวลาทอดหน้าขนมจะต้องแตกออกคล้ายรอยยิ้มของหน้าคนเรา เนื้อขนมที่ได้มีความกรอบนอกนุ่มใน เนื้อขนมฟู่นุ่ม ร่วน
ในปัจจุบัน ขนมยิ้มเสน่ห์หาทานยาก ขนมชนิดนี้มักทำขายในช่วงเทศกาลงานบุญ หรืองานประเพณีท้องถิ่น
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    - แป้งสาลีเอนกประสงค์ 420 กรัม
    - ผงฟู 2 ช้อนชา
    - ไข่ไก่ 2 ฟอง
    - น้ำตาลทรายขาว 170 กรัม
    - เกลือ 1/2 ช้อนชา
    - กลิ่นวนิลา 3 หยด (ใส่หรือไม่ใส่ก็ได้)
    - เนยเค็มละลาย 30 กรัม
    - นมจืด 30 กรัม
    - งาขาว 1 ถ้วยตวง
    - น้ำมันพืช (สำหรับทอด)
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. เตรียมแป้ง:
    - ผสมแป้งสาลี ผงฟู เกลือ และน้ำตาลทรายเข้าด้วยกัน
    - ใส่ไข่ไก่ เนยละลาย นมจืด และกลิ่นวนิลา ตีจนส่วนผสมเข้ากันดี
    - นวดแป้งจนเนียน ไม่ติดมือ
    - พักแป้งไว้ 30 นาที

    2. ปั้นแป้ง:
    - แบ่งแป้งเป็นก้อนกลมๆ ขนาดเท่าไข่ไก่
    - คลุกแป้งกับงาขาว

    3. ทอดขนม:
    - ตั้งน้ำมันให้ร้อนปานกลาง
    - ทอดขนมจนเหลืองกรอบ พักไว้ให้สะเด็ดน้ำมัน

    4. จัดเสิร์ฟ:
    - วางขนมยิ้มเสน่ห์ใส่จาน

    เคล็ดลับ:
    - เลือกใช้แป้งสาลีที่มีโปรตีนปานกลาง
    - นวดแป้งจนเนียน ไม่ติดมือ
    - พักแป้งก่อนปั้น จะทำให้เนื้อขนมฟู
    - ทอดขนมด้วยไฟปานกลาง จะทำให้ขนมสุกทั่ว ไม่ไหม้
    - พักขนมให้สะเด็ดน้ำมันก่อนเสิร์ฟ
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
