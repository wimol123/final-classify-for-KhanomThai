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
kanom_img_path = os.getenv("COMPONENT_64_PATH1")
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
st.title("ความเป็นมา")
st.image(image=kanom_img_path, width=850)

multi = """
ไข่แมงดาฉาบ (อาหารว่างไทย) สันนิษฐานว่าเป็นขนมทานเล่นหรือของว่างทานเล่นในวังสมัยโบราณช่วงรัตนโกสินทร์ตอนต้น 
ไว้สำหรับต้อนรับแขกที่มาเยี่ยมเยือนตามพระตำหนักมีรสชาติหวานนำ เค็มตาม มีความมันและหอมจากมะพร้าวและไข่แมงดาทะเล 
นับว่าเป็นของทานเล่นที่หาทานได้ยากยิ่งในปัจจุบัน  

ว่ากันว่าเป็นขนมพื้นบ้านเมืองเพชรต้นตำรับที่สืบทอดกันมานาน ชาวบ้านได้ทำถวายในรัชกาลที่ 5 
ครั้นเสด็จแปรพระราชฐาน ต้องใช้เวลากวนนานประมาณ 2 ชม. และต้องใช้ที่ขูดมะพร้าวแบบโบราณ ใช้เครื่องปั่นขูดเอาไม่ได้  

ในวรรณกรรมสี่แผ่นดิน ก็มีระบุด้วยว่า ขนมนี้แม่พลอยได้ชิมครั้งแรกตอนเข้าถวายตัวกับเสด็จ
บางข้อมูลก็ว่าขนมนี้กำเนิดที่ชุมชนอ่างศิลา และชาวบ้านทำไปถวาย เจ้าดารารัศมี ตอนท่านประชวร และมาพัก ท่านก็ทรงโปรด
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
     แมงดาจานต้มสุก 1 ตัว  
    น้ำตาลมะพร้าว 130 กรัม  
    หัวกะทิ 180 มิลลิลิตร   
    เนื้อมะพร้าวทึนทึกขูด 200 กรัม  
    เกลือ 1 ช้อนชา   
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
   **STEP 1 : ขูดไข่แมงดา**  
    นำแมงดาที่นึ่งสุกแล้ว มาดึงขาและเลาะเปลือกออก จากนั้นขูดนำแต่ไข่ออกมาพักไว้  
      
    **STEP 2 : เคี่ยวน้ำตาลและหัวกะทิ**  
    ตั้งกระทะใส่น้ำตาลลงไป ตามด้วยหัวกะทิ ทยอยเทหัวกะทิไปเรื่อยๆ ผัดจนน้ำตาลและหัวกะทิเข้ากันดี แล้วค่อยใส่เนื้อมะพร้าวขูด ตามด้วยเกลือ   

    **STEP 3 : ใส่ไข่แมงดา**  
    ใส่ไข่แมงดาลงไป จากนั้นผัดไปเรื่อยๆ จนมะพร้าวเริ่มเปลี่ยนเป็นสีเข้ม น้ำกะทิแห้งดี ค่อยตักขึ้น พร้อมรับประทาน
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
