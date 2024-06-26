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
kanom_img_path = os.getenv("COMPONENT_185_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Display main image and title
st.image(image=header_img_path)
st.title("ขนมรังผึ้ง")
st.image(kanom_img_path)
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมรังผึ้งมีต้นกำเนิดมาจากประเทศจีน ในสมัยราชวงศ์ชิง มีชื่อเรียกว่า "หลอวเพา" นิยมทำกันในงานมงคลต่างๆ เชื่อกันว่าขนมรังผึ้งเป็นสิริมงคล ช่วยให้ชีวิตราบรื่น เหมือนนกที่ได้สร้างรังใหม่ ต่อมาได้มีการนำเข้ามายังประเทศไทย และได้รับการดัดแปลงสูตรให้เข้ากับความนิยมของคนไทย โดยใส่กะทิ ไข่ และน้ำตาล ทำให้ขนมมีรสชาติหวานหอม อร่อยยิ่งขึ้น
"""
st.markdown(multi)

col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • แป้งสาลีอเนกประสงค์
    • กะทิ
    • ไข่ไก่
    • น้ำตาลทราย
    • เกลือ
    • น้ำมันพืช
    • สีผสมอาหารสีเหลือง (เลือกใช้)
    """
    st.markdown(multi)

with col2:
    st.header("วิธีทำ")
    multi = """
    1. ผสมแป้ง: ร่อนแป้งสาลี เกลือ และผงฟู ลงในชาม ผสมให้เข้ากัน
    2. ตีไข่: ตีไข่ไก่กับน้ำตาลทรายจนฟู ใส่กะทิ ตีต่อจนเข้ากัน
    3. รวมส่วนผสม: เทส่วนผสมไข่ลงในชามแป้ง คนให้เข้ากันจนเนียน พักไว้ 30 นาที
    4. ทอดขนม: ตั้งกระทะ ทาน้ำมันพืชให้ร้อน ใส่พิมพ์ขนมรังผึ้งลงไป เทแป้งลงในพิมพ์ รอจนแป้งเริ่มสุก ใช้ตะเกียบแซะรอบๆ พิมพ์ พลิกกลับด้าน ทอดจนเหลืองกรอบ ตักขึ้นพักให้สะเด็ดน้ำมัน
    5. จัดเสิร์ฟ: ตักขนมรังผึ้งใส่จาน ราดด้วยน้ำกะทิหรือน้ำเชื่อม พร้อมเสิร์ฟ
    """
    st.markdown(multi)
