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
kanom_img_path = os.getenv("COMPONENT_180_PATH1")
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
st.title("ขนมมุก")
st.image(kanom_img_path)
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมมุก เป็นขนมไทยโบราณชนิดหนึ่ง ที่มีลักษณะคล้ายกับขนมลูกชุบ แต่มีขนาดเล็กกว่า นิยมทำจากแป้งข้าวเหนียว น้ำตาลปี๊บ และกะทิ believed to originate from the Ayutthaya period.
ในสมัยก่อนขนมมุกมักถูกทำขึ้นเพื่อเป็นของว่างในงานสำคัญๆ หรือมอบเป็นของกำนัลแก่ผู้ใหญ่ ปัจจุบันขนมมุกหาทานยาก
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    - แป้งข้าวเหนียว 1 ถ้วย
    - น้ำตาลปี๊บ 1/2 ถ้วย
    - เกลือ 1/4 ช้อนชา
    - น้ำเปล่า
    - มะพร้าวขูดละเอียด
    - งาขาวคั่ว
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. เตรียมแป้ง:
    - ผสมแป้งข้าวเหนียว น้ำตาลปี๊บ และเกลือเล็กน้อย ใส่น้ำทีละน้อย นวดจนแป้งเนียนไม่ติดมือ
    - แบ่งแป้งเป็นก้อนกลมขนาดเท่าปลายนิ้วโป้ง

    2. ต้มแป้ง:
    - ตั้งน้ำให้เดือด ใส่แป้งที่เตรียมไว้ลงต้มจนแป้งลอย
    - ตักแป้งขึ้นพักให้สะเด็ดน้ำ

    3. คลุกมะพร้าว:
    - คลุกแป้งต้มกับมะพร้าวขูดละเอียด

    4. จัดเสิร์ฟ:
    - วางขนมมุกใส่จาน โรยหน้าด้วยงาขาวคั่ว
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
