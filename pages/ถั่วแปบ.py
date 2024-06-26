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
kanom_img_path = os.getenv("COMPONENT_115_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมถั่วแปบ: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🍴",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมถั่วแปบ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมถั่วแปบ เป็นขนมไทยโบราณที่มีมาช้านาน เชื่อกันว่ามีต้นกำเนิดมาจากภาคกลาง ลักษณะของขนมถั่วแปบนั้น ทำเลียนแบบฝักถั่วของต้นถั่วแปบ มีสีสันสวยงาม ทำจากแป้งข้าวเหนียว ไส้ถั่วเขียว มะพร้าวขูด งาคั่ว ทานคู่กับน้ำตาลทรายโรยงาคั่ว
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **แป้ง:**
        1. ผสมแป้งข้าวเหนียว น้ำ ใบเตย เกลือ คนจนส่วนผสมละลายดี พักไว้
        2. ตั้งกระทะ ใส่น้ำมันพืชเล็กน้อย เทแปลงลงไป เกลี่ยให้บาง รอจนแป้งเริ่มสุก ตักขึ้นพัก
        
        **ไส้:**
        1. นำถั่วเขียวมาล้างน้ำ แช่น้ำประมาณ 3-4 ชั่วโมง นำไปนึ่งหรือต้มจนสุก
        2. บดถั่วเขียวที่สุกแล้ว พักไว้
        3. ใส่มะพร้าวขูด เกลือ น้ำตาลทราย งาคั่ว คลุกให้เข้ากัน
        
        **ประกอบร่าง:**
        1. ทาแป้งบางๆ บนใบตอง
        2. ตักไส้ถั่วเขียววางบนแป้ง
        3. พับใบตองห่อไส้เป็นรูปสามเหลี่ยม
        4. นึ่งประมาณ 10-15 นาที
        
        **โรยหน้า:**
        1. ผสมน้ำตาลทราย งาขาวคั่ว งาดำคั่ว คลุกให้เข้ากัน
        2. โรยหน้าขนมถั่วแปบที่นึ่งเสร็จแล้ว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **แป้ง:**
        - แป้งข้าวเหนียว 200 กรัม
        - น้ำ 100 มล.
        - ใบเตย 2-3 ใบ
        - เกลือ 1/4 ช้อนชา
        
        **ไส้:**
        - ถั่วเขียว 100 กรัม
        - มะพร้าวขูด 100 กรัม
        - น้ำตาลทราย 50 กรัม
        - เกลือ 1/4 ช้อนชา
        - งาคั่ว 2 ช้อนโต๊ะ
        
        **โรยหน้า:**
        - น้ำตาลทราย 2 ช้อนโต๊ะ
        - งาขาวคั่ว 1 ช้อนโต๊ะ
        - งาดำคั่ว 1 ช้อนโต๊ะ
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
