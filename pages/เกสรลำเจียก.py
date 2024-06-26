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
kanom_img_path = os.getenv("COMPONENT_21_PATH1")
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
st.title("เกสรลำเจียก")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
ขนมเกสรลำเจียก ขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว 
ขึ้นชื่อเรื่องความหอม หวานมัน และรูปลักษณ์ที่สวยงาม 
คล้ายดอกลำเจียกบาน นิยมทำกันในจังหวัดอ่างทอง
โดยเฉพาะที่ตำบลไผ่จำศีล อำเภอวิเศษชัยชาญ

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    แป้งข้าวเหนียว 2 ถ้วยตวง

    กะทิ 4 ถ้วยตวง

    น้ำตาลทราย 1 ถ้วยตวง

    เกลือ 1/2 ช้อนชา

    ใบเตย 3-4 ใบ

    ฟักทอง 100 กรัม

    น้ำดอกกุหลาบ 1 ช้อนโต๊ะ

    มะพร้าวอ่อนขูด 2 ถ้วยตวง

"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ผสมแป้งข้าวเหนียวกับกะทิ 1 ถ้วยตวง คนให้ละลายเข้ากัน
    2. ละลายน้ำตาลทรายกับน้ำเปล่า 1 ถ้วยตวง
    3. ตั้งกระทะ ใส่น้ำกะทิ 1 ถ้วยตวง เกลือ และน้ำตาลปี๊บที่ละลายไว้
    4. พอน้ำเดือด ใส่แป้งข้าวเหนียวที่ผสมไว้ลงไปกวน
    5. กวนจนแป้งสุกและข้น
    6. แบ่งแป้งออกเป็น 3 ส่วน
    7. ผสมแป้งส่วนแรกกับใบเตยบดละเอียด
    8. ผสมแป้งส่วนที่สองกับฟักทองบดละเอียด
    9. ผสมแป้งส่วนที่สามกับน้ำดอกกุหลาบ
    10. เทแป้งแต่ละสีลงพิมพ์ที่รองด้วยใบตอง
    11. นึ่งจนขนมสุก
    12. พักให้ขนมเย็นและแข็งตัว
    13. ตัดขนมเป็นชิ้นพอดีคำ
    14. โรยมะพร้าวอ่อนขูด
    
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
