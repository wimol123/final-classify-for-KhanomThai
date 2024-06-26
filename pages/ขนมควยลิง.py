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
kanom_img_path = os.getenv("COMPONENT_68_PATH1")
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
st.title("")

left_co, cent_co, last_co = st.columns(3)
st.title("ขนมควยลิง")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
ขนมควยลิง มีที่มาจาก เมื่อสมัยก่อนที่ชุมชนหนองบัวมีลิงแสมเป็นจำนวนมาก 
เวลาชาวบ้านทำขนมเจ้าลิงพวกนี้ก็จะมานั่งเฝ้า 
พร้อมกับโชว์ของดีให้ดูอยู่เป็นประจำ 
ชาวบ้านจึงตั้งชื่อขนมที่ทำว่า “ขนมควยลิง” นั่นเอง
  
ขนมควยลิงนั้นทำมาจากแป้งข้าวเหนียว นำมาปั้นเป็นแท่งเล็ก ๆ รี ๆ และนำไปต้มในน้ำเดือด จากนั้นคลุกกับมะพร้าวขูด 
ทานคู่กับน้ำตาล จะได้รสชาติหวาน ๆ มัน ๆ 

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • แป้งข้าวเหนียว 200 กรัม  
    • มันม่วงนึ่งสุก 100 กรัม  
    • น้ำมะพร้าว 200 มิลลิลิตร  
    • มะพร้าวขูดฝอย  
    • เกลือ  

"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    • เตรียมมะพร้าวขูด แล้วเอามะพร้าวขูดไปนึ่ง  
    • ผสมแป้งข้าวเหนียวและมันม่วงเข้าด้วยกัน จากนั้นใส่น้ำมะพร้าว แล้วนวดให้เป็นเนื้อเดียวกัน  
    • ปั้นแป้งให้เป็นรูปเรียวยาว  
    • เตรียมหม้อ แล้วต้มน้ำให้เดือด  
    • เมื่อน้ำเดือดแล้ว ใส่แป้งลงไปในหม้อ  
    • เมื่อแป้งลอยขึ้นมา แตะแล้วนิ่ม ก็ช้อนแป้งขึ้นมาพักไว้  
    • นำมะพร้าวขูดที่นึ่งเสร็จแล้ว และใส่เกลือลงไปนิดหน่อย จากนั้นเอาแป้งที่ต้มจนนิ่มแล้ว นำมาคลุกเคล้าให้ทั่วตัวแป้ง เป็นอันสิ้นสุดวิธีการทำขนมควยลิง พร้อมรับประทานได้  
    
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
