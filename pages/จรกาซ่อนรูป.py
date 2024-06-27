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
kanom_img_path = os.getenv("COMPONENT_73_PATH1")
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
st.title("จรกาซ่อนรูป")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
st.image(image=kanom_img_path, width=900)
multi = """
จรกาซ่อนรูป เป็นขนมไทยโบราณสมัยกรุงรัตนโกสินทร์ ซึ่งอาจจะไม่ค่อยเห็นกันบ่อยนัก. ซึ่งจรกา ในที่นี้ก็คือ ถั่วดำ ซ่อนรูปอยู่ในแป้งข้าวเหนียว แล้วเพิ่มการซ่อนรูปให้เป็นทรงเครื่อง โดยการใส่มะพร้าวอ่อน และ แปะก๊วย เข้าไปในส่วนผสมของน้ำกะทิสดสีขาวนวล 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
     ถั่วดำ 100 กรัม  
    แป้งข้าวเหนียว 180 กรัม  
    กะทิ 150 ml  
    กะทิ 850 ml  
    น้ำตาลมะพร้าว 260 กรัม  
    เกลือป่น 1 ช้อนชา  
    ใบเตย 3 ใบ  
    เกลือ 1/2 ช้อนชา  
    น้ำเปล่า 1 ถ้วยตวง  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
   
YouTube
expand_more
จรกาซ่อนรูป วิธีทำ
สูตรจากกวางเจาเข้าครัว

จรกาซ่อนรูป ขนมไทยทำง่าย หอม หวาน มัน อร่อย ซ่อนยังไงก็ไม่มิดติดใจกันทุกคน #kwangjaow เข้าครัว 👩🏼🍳

วัตถุดิบ

ถั่วดำ 100 กรัม
แป้งข้าวเหนียว 180 กรัม
กะทิ 150 ml
กะทิ 850 ml
น้ำตาลมะพร้าว 260 กรัม
เกลือป่น 1 ช้อนชา
ใบเตย 3 ใบ
เกลือ 1/2 ช้อนชา
น้ำเปล่า 1 ถ้วยตวง
วิธีทำ

1. ล้างถั่วดำให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
2. ต้มถั่วดำจนเปื่อยนำขึ้นพักไว้
3. ผสมแป้งข้าวเหนียว เกลือ และน้ำเปล่า นวดจนแป้งเนียน
4. แบ่งแป้งเป็นก้อนกลมๆ กดแป้งให้แบน
5. ใส่ถั่วดำต้มลงตรงกลาง ห่อแป้งให้มิด
6. ต้มน้ำกะทิ ใส่ใบเตย เกลือ และน้ำตาลมะพร้าว คนจนน้ำตาลละลาย
7. ใส่จรกาลงต้มจนลอยขึ้น
8. ตักจรกาขึ้นพักไว้ ทานคู่กับน้ำกะทิ
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
