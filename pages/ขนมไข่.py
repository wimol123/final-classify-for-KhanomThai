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
kanom_img_path = os.getenv("COMPONENT_59_PATH1")
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
st.title("ขนมไข่")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
st.image(image=kanom_img_path, width=850)

multi = """
ขนมไข่ ขนมไทยโบราณที่ขึ้นชื่อเรื่องความหอม หวานมัน ละมุนลิ้น  มีเอกลักษณ์เฉพาะตัวด้วยเนื้อสัมผัสที่นุ่มฟู  ทานคู่กับชา กาแฟ หรือเครื่องดื่มร้อนๆ  เข้ากันได้ดี
ขนมไข่มีถิ่นกำเนิดจาก ประเทศโปรตุเกส  เข้ามาเผยแพร่ในประเทศไทยสมัยกรุงศรีอยุธยา  โดยชาวโปรตุเกสที่เข้ามาค้าขาย  ขนมชนิดนี้จึงได้รับความนิยมในหมู่ชนชั้นสูง
ต่อมา  สูตรขนมไข่ได้ถูกดัดแปลงให้เข้ากับวัตถุดิบและความชอบของคนไทย  กลายเป็นขนมไทยโบราณที่ได้รับความนิยมจนถึงปัจจุบัน

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • ไข่ไก่ 3 ฟอง   
    • น้ำตาลทราย 100 กรัม  
    • เนยละลาย 50 กรัม  
    • แป้งสาลีอเนกประสงค์ 100 กรัม  
    • เกลือ 1/4 ช้อนชา  
    • กลิ่นวานิลลา 1 ช้อนชา  
      
    หมายเหตุ: ปริมาณส่วนผสมนี้สามารถทำขนมไข่ได้ประมาณ 10-12 ชิ้น
        

"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ตีไข่ไก่กับน้ำตาลจนขึ้นฟู  
    2. ใส่เนยละลาย เกลือ และกลิ่นวานิลลา ตีต่อจนเข้ากัน  
    3. ร่อนแป้งสาลีใส่ คนให้เข้ากัน  
    4. เทส่วนผสมลงพิมพ์  
    5. อบไฟ 180 องศาเซลเซียส ประมาณ 15-20 นาที หรือจนสุก  

    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
