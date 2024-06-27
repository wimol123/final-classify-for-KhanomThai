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
kanom_img_path = os.getenv("COMPONENT_93_PATH1")
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
st.title("ขนมดอกโสน")

left_co, cent_co, last_co = st.columns(3)
st.title("ขนมดอกโสน: ขนมไทยโบราณที่มาจากภูมิปัญญาพื้นบ้าน")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมดอกโสน เป็นขนมไทยโบราณที่หาทานได้ยากในปัจจุบัน  เอกลักษณ์ของขนมชนิดนี้คือการใช้ "ดอกโสน"  พืชท้องถิ่นที่มักขึ้นอยู่ตามริมน้ำ มาเป็นส่วนผสมหลัก  ซึ่งนอกจากจะนำมาทำเป็นขนมแล้ว ดอกโสนยังนิยมนำมาประกอบอาหารคาว เช่น แกงส้ม ยำ หรือลวกจิ้มน้ำพริกอีกด้วย
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • ดอกโสน              1         ก.ก  
    • มะพร้าวทึนทึก      1         ก.ก  
    • แป้งข้าวเจ้า          1/2      ก.ก  
    • น้ำตาลทราย         3         ถ้วย  
    • เกลือป่น               1/2      ช้อนชา  
    • น้ำดอกไม้สด        1          ถ้วย  

    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
เอาแป้งข้าวเจ้าใส่ภาชนะ ผสมกับดอกโสน คลุกเคล้าให้เข้ากัน พรมน้ำดอกไม้สดที่เราเตรียมไว้ให้ทั่วๆ เสร็จแล้วนำไปนึ่งให้สุข เวลารับประทานผสมมะพร้าว เกลือป่น น้ำตาลทราย ให้เข้ากัน แล้วพร้อมเสิร์ฟ
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
