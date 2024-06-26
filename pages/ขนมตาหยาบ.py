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
kanom_img_path = os.getenv("COMPONENT_101_PATH1")
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
st.title("ขนมตาหยาบ")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
มีความเป็นมาจากประเทศมาเลเซีย โดยจะเรียกว่าขนมตายับ ซึ่งมีบรรพบุรุษในสมัยอดีตได้สืบทอดกันนำเข้ามาสู่เมืองไทย จนกระทั่งเข้ามาสู่เมืองไทยเลยมีชื่อที่เพี้ยนออกไปว่าขนมตาหยาบ โดยไส้ของตัวขนมจะใช้มะพร้าวทึนทึก ส่วนแป้งก็จะเป็นแป้งสาลี ผสมกับแป้งข้าวเหนียวนิดหน่อย ใช่ไข่ไก่ผสมลงไป น้ำใบเตย และเกลือเท่านี้
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    มะพร้าวขูดขาว 200 กรัม  
    น้ำตาลมะพร้าว 50 กรัม   
    น้ำตาลทรายแดง 1 ช้อนโต๊ะ  
    น้ำตาลทรายขาว ½ ช้อนโต๊ะ  
    เกลือ ½ ช้อนชา  
    แป้งข้าวเจ้า ½ ถ้วยตวง  
    แป้งข้าวเหนียว 1 ถ้วยตวง  
    แป้งมันสำปะหลัง ¼ ถ้วยตวง    
    น้ำเปล่า 2 ถ้วยตวง  
    ไข่ไก่(เบอร์ 0) 1 ฟอง  
    น้ำใบเตยหรือสีผสมอาหารตามใจชอบ  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
STEP 1 : ผัดไส้กระฉีก  
- ตั้งกระทะ ใส่น้ำตาลมะพร้าว น้ำตาลทรายแดง และน้ำตาลทรายขาว คนจนน้ำตาลละลาย  
- ใส่มะพร้าวขูดขาวลงไป ปรุงรสด้วยเกลือ ผัดจนงวด พักไว้  
  
STEP 2 : ผสมแป้ง  
- ผสมแป้งข้าวเจ้า แป้งข้าวเหนียว แป้งมันสำปะหลัง เกลือ น้ำเปล่า และไข่ไก่ ลงไป  
- คนจนส่วนผสมเข้ากันดี แบ่งใส่สีตามใจชอบ  
  
STEP 3 : ทำขนมตาหยาบ  
- ตั้งกระทะ ทาน้ำมันบาง ๆ ใส่แป้งลงไป เกลี่ยแป้งเป็นแผ่นบาง ๆ รอจนแป้งสุก หยิบออกจากกระทะ  
- นำแป้งที่ได้มาห่อไส้กระฉีก พร้อมเสิร์ฟ   
    
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
