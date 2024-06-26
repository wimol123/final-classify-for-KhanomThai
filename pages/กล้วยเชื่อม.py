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
kanom_img_path = os.getenv("COMPONENT_KluaiChueam_PATH1")
component_1_path = os.getenv("COMPONENT_KluaiChueam_PATH2")
component_2_path = os.getenv("COMPONENT_KluaiChueam_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path, use_column_width=True)
st.title("กล้วยเชื่อม")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
    กล้วยเชื่อม ขนมไทยโบราณที่หลายคนคุ้นเคย ลักษณะคล้ายกล้วยต้ม แต่เนื้อจะนุ่มและหวานฉ่ำ 
    นิยมนำกล้วยน้ำว้ามาเชื่อมกับน้ำตาลจนเข้ากัน กลายเป็นขนมหวานทานเล่นที่อร่อยและเก็บไว้ได้นาน

    ประวัติความเป็นมา

    ข้อมูลแน่ชัดเกี่ยวกับประวัติความเป็นมาของกล้วยเชื่อมนั้นยังไม่ปรากฏชัด แต่สันนิษฐานว่าน่าจะมีมานานแล้ว
    พบหลักฐานการทำกล้วยเชื่อมในตำราอาหารไทยโบราณหลายเล่ม เช่น ตำราแม่ครัวหลวง และตำราอาหารวัดสุวรรณาราม
    ในอดีตกล้วยเชื่อมเป็นของหวานที่นิยมทำรับประทานกันในครัวเรือน มักทำเพื่อเป็นของหวานหลังอาหาร หรือทานคู่กับน้ำชา กาแฟ
    ปัจจุบันกล้วยเชื่อมหาซื้อทานได้ทั่วไป มีทั้งแบบดั้งเดิมและแบบประยุกต์
    
    เอกลักษณ์ของกล้วยเชื่อม

    กล้วยเนื้อนุ่ม หวานฉ่ำ รสชาติหวานมันกลมกล่อม มีกลิ่นหอมของน้ำตาลทานง่าย
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
