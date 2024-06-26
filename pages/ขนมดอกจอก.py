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
kanom_img_path = os.getenv("COMPONENT_90_PATH1")
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
st.title("ขนมดอกจอก")

left_co, cent_co, last_co = st.columns(3)
st.title("ขนมดอกจอก ที่ความเป็นมาไม่กระจอกเหมือนชื่อ")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมดอกจอกในปัจจุบัน อาจเป็นขนมราคาย่อมเยาที่หาได้ยากในกรุงเทพมหานครในปัจจุบัน แต่ในความเป็นจริงแล้ว ขนมดอกจอกมีความเชื่อมโยงกับวัฒนธรรมตั้งแต่มาเลเซียไปจนถึงนอร์เวย์  
  
ขนมดอกจอกเป็นขนมท้องถิ่นทางภาคใต้ มีลักษณะคล้ายจอกแหน ทำจากแป้งข้าวเจ้า แป้งมัน กะทิ และงาดำ นำแม่พิมพ์ชุบแป้งแล้วนำไปทอด นิยมรับประทานในช่วงเทศกาลสารทเดือนสิบ
  
ขนมดอกจอกนี้ สันนิษฐานว่า มีที่มาจากขนมอัศศุ มุรุกุ (Achu Murukku) เป็นขนมของชาวเปอรานากันที่ได้รับจากอินเดียตอนใต้และศรีลังกา โดยคำว่า อัศศุ หมายถึง แม่พิมพ์ ส่วน มุรุกุ หมายถึง บิดหรือขดเป็นเกลียว โดยขนมชนิดนี้รับประทานในช่วงเทศกาลดิวาลี ซึ่งเป็นช่วงระยะเวลาใกล้เคียงกับเทศกาลสารทเดือนสิบ
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    แป้งข้าวเจ้า 1 ถ้วยตวง
    แป้งสาลี 1 ถ้วยตวง
    น้ําตาลทราย ¾ ถ้วย
    ไข่ไก่ 1 ฟอง
    กะทิ ½ ถ้วยตวง
    เกลือ 1 ช้อนชา
    น้ำปูนใส 1 ถ้วยตวง
    งาดำ 2 ช้อนโต๊ะ
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    STEP 1 : ผสม  
    - ผสมส่วนผสมทุกอย่างรวมกัน ใช้ตะกร้อตีให้เนียนเป็นเนื้อเดียวกัน  
  
    STEP 2 : ทอด  
    - นําพิมพ์ แช่น้ํามันให้พิมพ์ร้อน ใช้ไฟปานกลางจากนั้นนําพิมพ์มาจุ่มในแป้ง นําไปทอด พอสุกเป็นสีน้ำตาล ตักขึ้นวางบนถ้วยตะไลคว่ำ ให้สะเด็ดน้ํามัน  
    - รอให้เย็น พร้อมรับประทาน!  
    
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
