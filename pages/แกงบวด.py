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
kanom_img_path = os.getenv("COMPONENT_Kaengbuat_PATH1")
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
st.title("แกงบวด")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
 แกงบวด(เผือก, มัน, ฝักทอง) เป็นขนมไทยพื้นบ้านของชาวไทย ที่บ่งบอกถึงความเป็นไทยเนื่องจากชาวบ้านส่วนใหญ่มีอาชีพเกษตรกรรม 
 ปลูกผักผลไม้ ไว้รับประทานเอง จึงนำอาหารที่มีอยู่ในท้องถิ่นมาทำขนมรับประทานเองภายในครอบครัว 
 หรือนำไปทำบุญที่วัด และใช้รับรองแขก ปัจจุบันหลายครอบครัวเริ่มเลิกราห่างหายกันไปเนื่องจากเห็นว่ามีขั้นตอนที่ยุ่งยาก 
 เสียเวลา และสามารถซื้อหาได้ง่ายตามตลาดทั่ว ๆ แต่ก็ยังคงเหลือเป็นบางครอบครัวที่สานต่อ 
 รักษาสืบทอดการทำขนมแกงบวดฟักทอง คงไว้ให้ลูกหลานได้เรียนรู้ อนุรักษ์สืบสานต่อไป

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
        1. ฟักทอง เผือก หรือมัน หั่นเป็นชิ้นพอดีคำ 

        2. น้ำเปล่า 2 1/2 ถ้วยตวง

        3. หัวกะทิ 1 ถ้วยตวง

        4. หางกะทิ 1 ถ้วยตวง

        5. ใบเตย 2 ใบ

        6. น้ำตาลทราย 40 กรัม

        7. น้ำตาลปี๊บ 40 กรัม

        8. เกลือป่น 1/4 ช้อนชา
       
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
        1. ทำความสะอาดและหั่นฟักทอง มันหรือเผือก เป็นชิ้นพอดีคำ

        2. นำหางกะทิ, ใบเตย, น้ำตาลทรายและน้ำตาลปี๊บใส่ลงไปในหม้อ และนำไปตั้งบนไฟร้อนปานกลางจนเดือด
        
        3. ใส่ฟักทองที่หั่นไว้แล้วลงไป ต้มต่อไปจนฟักทองสุกและนุ่ม (ใช้เวลาประมาณ 10 นาที)
        
        4. ใส่หัวกะทิและเกลือลงไป ต้มต่อจนเืดือดอีกครั้งจึงปิดไฟ
        
        5. ตักใส่ถ้วย สามารถเสริฟทันทีขณะร้อน หรือปล่อยไว้ให้เย็นแล้วค่อยเสริฟเป็นอาหารว่างก็ได้เช่นกัน
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
