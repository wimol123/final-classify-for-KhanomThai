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
kanom_img_path = os.getenv("COMPONENT_76_PATH1")
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
st.title("ขนมจี้")

left_co, cent_co, last_co = st.columns(3)
st.title("ขนมจี้: ขนมไทยโบราณ หอมหวาน มัน อร่อย")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมจี้เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว 
โดยมีลักษณะเป็นแป้งนุ่มสีขาว ห่อไส้หวานมัน 
ทานคู่กับน้ำตาลทรายและงาคั่ว นิยมทำทานกันในช่วงเทศกาลต่างๆ 
หรือทำแจกในงานมงคล  
  
ขนมจี้มีมานานแล้ว แต่ไม่ทราบแน่ชัดว่ามีต้นกำเนิดมาจากไหน  
บ้างก็ว่ามีมาตั้งแต่สมัยกรุงศรีอยุธยา  บ้างก็ว่าเป็นขนมที่ชาวจีนนำเข้ามา 
แต่ขนมจี้ที่เราทานกันทั่วไปในปัจจุบัน  น่าจะได้รับอิทธิพลมาจากขนมกะลอจี๊ของจีน  
แต่มีการเปลี่ยนแปลงวิธีทำ โดยเฉพาะวิธีการทำแป้ง
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • แป้งข้าวเหนียว 1 ถ้วยตวง  
    • แป้งข้าวเจ้า 1/2 ถ้วยตวง  
    • เกลือป่น 1/2 ช้อนชา  
    • น้ำเปล่า 1 ถ้วยตวง  
    • น้ำตาลทราย 1/2 ถ้วยตวง  
    • งาดำคั่ว 1/4 ถ้วยตวง  
    • แป้งข้าวเจ้าคั่วสำหรับคลุก 1/4 ถ้วยตวง  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ร่อนแป้งข้าวเหนียว แป้งข้าวเจ้า และเกลือป่น ใส่ลงในชามผสม  
    2. ค่อยๆ เติมน้ำเปล่าลงไปทีละน้อย นวดจนแป้งเนียน ไม่ติดมือ  
    3. นำแป้งไปนึ่งในลังถึงไฟปานกลาง ประมาณ 20-30 นาที หรือจนแป้งสุก  
    4. เทแป้งที่นึ่งสุก ลงบนผ้าขาวบาง พักให้เย็น  
    5. แบ่งแป้งออกเป็นก้อนกลมๆ ขนาดเส้นผ่านศูนย์กลางประมาณ 1 นิ้ว  
    6. ผสมน้ำตาลทรายกับงาดำคั่ว คลุกเคล้าให้เข้ากัน  
    7. ตักไส้ใส่ลงบนแป้ง ห่อให้มิด  
    8. คลุกแป้งที่ห่อไส้ กับแป้งข้าวเจ้าคั่ว จนทั่ว  
    9. จัดเสิร์ฟ ทานคู่กับน้ำตาลทรายและงาคั่ว  
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
