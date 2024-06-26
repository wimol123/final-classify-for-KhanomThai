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
kanom_img_path = os.getenv("COMPONENT_krobkrem_PATH1")
component_1_path = os.getenv("COMPONENT_krobkrem_PATH2")
component_2_path = os.getenv("COMPONENT_krobkrem_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("กรอบเค็ม")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
กรอบเค็ม ขนมไทยโบราณที่หลายคนคุ้นเคย ลักษณะคล้ายครองแครง 
แต่เนื้อนุ่มกว่า โดยทั่วไปมีลักษณะเป็นแผ่นรูปสี่เหลี่ยมคล้ายขนมเปียกปูน 
แต่มีความแตกต่างกันไปขึ้นอยู่กับผู้ทำ 

ข้อมูลแน่ชัดเกี่ยวกับประวัติความเป็นมาของกรอบเค็มนั้นยังไม่ปรากฏชัด แต่สันนิษฐานว่าน่าจะมีมานานแล้ว
พบหลักฐานการทำขนมกรอบเค็มในตำราอาหารไทยโบราณหลายเล่ม เช่น ตำราแม่ครัวหลวง และตำราอาหารวัดสุวรรณาราม
ในอดีตกรอบเค็มเป็นขนมที่นิยมทำรับประทานกันในครัวเรือน
มักทำเพื่อเป็นของว่าง หรือทานคู่กับน้ำชา กาแฟ
ปัจจุบันกรอบเค็มหาซื้อทานได้ยากขึ้น แต่ยังมีบางร้านที่ยังคงทำขาย
       
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=component_1_path)

with col2:
    st.header("วิธีทำ")
    st.image(image=component_2_path)

st.page_link("Home.py", label="Home", icon="↩️")
