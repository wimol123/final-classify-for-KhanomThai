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
kanom_img_path = os.getenv("COMPONENT_178_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image(image=header_img_path)
st.title("ขนมมัศกอด")
st.image(kanom_img_path)
st.title("ความเป็นมา")


multi = """
มัศกอดเป็นขนมไทยโบราณที่มีลักษณะหน้าตาคล้ายคัพเค้ก รสชาติหวานหอม ทำจากแป้งสาลีผสมกับกะทิและไข่ นิยมใช้ในงานบุญหรืองานสำคัญต่าง ๆ สมัยก่อนการทำขนมมัศกอดจะใช้การอบด้วยถ่าน ทำให้มีรสชาติและกลิ่นหอมเป็นเอกลักษณ์
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    แป้งสาลี 1 ถ้วยตวง  
    น้ำตาลปี๊บ 1/2 ถ้วยตวง  
    กะทิ 1 ถ้วยตวง  
    ไข่ไก่ 3 ฟอง  
    น้ำมันพืช 1/4 ถ้วยตวง  
    เกลือ 1/4 ช้อนชา  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
STEP 1 : เตรียมส่วนผสม  
- ร่อนแป้งสาลีและเกลือเข้าด้วยกัน พักไว้  
- ตีไข่ไก่และน้ำตาลปี๊บจนขึ้นฟู เติมกะทิและน้ำมันพืช คนให้เข้ากัน  

STEP 2 : ผสมแป้ง  
- ใส่แป้งสาลีที่ร่อนไว้ลงในส่วนผสมไข่ คนให้เข้ากันดี เทลงในพิมพ์ที่เตรียมไว้  

STEP 3 : อบ  
- นำเข้าอบในเตาอบที่อุณหภูมิ 180 องศาเซลเซียส นาน 20-25 นาที หรือจนสุกเหลือง  
- นำออกจากเตา พักไว้ให้เย็น พร้อมเสิร์ฟ  
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
