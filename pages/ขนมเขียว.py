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
kanom_img_path = os.getenv("COMPONENT_57_PATH1")
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
st.title("ขนมเขียว")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
ขนมไทยพื้นบ้านจากจังหวัดปราจีนบุรี ขึ้นชื่อเรื่องความอร่อย 
หอมกลิ่นใบเตย ไส้หวานมัน ทานคู่กับชาหรือกาแฟยามเช้า 
เข้ากันได้ดี ขนมเขียวมีต้นกำเนิดที่อำเภอนาดี จังหวัดปราจีนบุรี 
เป็นการผสมผสานระหว่างข้าวเกรียบปากหม้อกับขนมถั่วแปบ 
สูตรดั้งเดิมสืบทอดมายาวนานกว่า 40 ปี โดย นางบุญส่ง บุดดา 
หรือ แม่ปุก เริ่มมีชื่อเสียงโด่งดังในปี พ.ศ. 2537 
จากงานเทศกาลล่องแก่งหินเพิง Amazing นาดีปัจจุบัน 
ขนมเขียว "แม่ปุก" ขยายกิจการมี 2 สาขา และมีวางขายในหลายจังหวัด


"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ส่วนแป้ง

    • แป้งข้าวเจ้า 200 กรัม

    • แป้งมันสำปะหลัง 90 กรัม

    • น้ำตาลทราย 120 กรัม

    • น้ำใบเตย 350 มล.

    • น้ำปูนใส 500 มล.

    • น้ำมันพืชสำหรับทาถาด

    ส่วนไส้
    
    • ถั่วเขียวเลาะเปลือกนึ่งสุก 400 กรัม

    • น้ำตาลทราย 200 กรัม

    • มะพร้าวอ่อนเส้น 300 กรัม

    • เกลือป่น 1/2 ช้อนชา
    
"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ทำแป้ง: ผสมแป้งข้าวเจ้า แป้งมัน น้ำตาลทราย และน้ำใบเตย คนจนเข้ากัน เติมน้ำปูนใส ทิ้งไว้ 30 นาที กรองแป้งอีกครั้ง
    2. ทำไส้: นำถั่วเขียวที่นึ่งสุกมาบดให้ละเอียด ผสมกับมะพร้าว น้ำตาลทราย และเกลือ
    3. เทแป้ง: ตั้งกระทะ ใส่น้ำมัน ทาบางๆ เทแปลงบางๆ รอจนสุก ตักขึ้น
    4. ใส่ไส้: วางแป้งบนใบตอง ตักไส้ใส่ตรงกลาง พับครึ่ง
    5. นึ่ง: นึ่งขนมเขียวประมาณ 10 นาที จากนั้นก็พร้อมรับประทาน

    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
