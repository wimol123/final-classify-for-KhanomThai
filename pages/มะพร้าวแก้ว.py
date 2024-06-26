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
kanom_img_path = os.getenv("COMPONENT_171_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("มะพร้าวแก้ว")
st.image(kanom_img_path)
st.title("ที่มา")
with st.expander("ที่มา"):
    st.markdown(
        """
        มะพร้าวแก้วเป็นขนมที่มีต้นกำเนิดจากภูมิปัญญาชาวบ้านไทย โดยเฉพาะในภาคใต้ ซึ่งมีการปลูกมะพร้าวมากมาย ชาวบ้านได้นำมะพร้าวมาแปรรูปเป็นขนมหวานเพื่อเก็บไว้รับประทานในครัวเรือนและจำหน่ายเป็นสินค้าท้องถิ่น
        """
    )

st.title("ส่วนประกอบ")
with st.expander("ส่วนประกอบ"):
    st.markdown(
        """
        **ส่วนประกอบ:**
        1. มะพร้าวขูดเส้น 500 กรัม
        2. น้ำตาลทราย 300 กรัม
        3. น้ำลอยดอกมะลิ 1/2 ถ้วยตวง
        4. สีผสมอาหาร (ตามชอบ)
        5. เกลือป่น 1/4 ช้อนชา
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วิธีทำ:**

        1. ล้างมะพร้าวขูดเส้นในน้ำเปล่าให้สะอาด พักให้สะเด็ดน้ำ
        2. ในหม้อขนาดกลาง ใส่น้ำลอยดอกมะลิ, น้ำตาลทราย, และเกลือป่น ตั้งไฟกลางๆ คนให้ส่วนผสมละลายเข้ากันดี
        3. เมื่อส่วนผสมน้ำตาลเริ่มเดือด ใส่มะพร้าวขูดเส้นลงไป คนให้เข้ากัน ลดไฟลงเล็กน้อย
        4. เคี่ยวน้ำตาลกับมะพร้าวขูดเส้นจนมะพร้าวมีลักษณะเหนียวและน้ำตาลเกาะตัวที่มะพร้าว ปิดไฟ
        5. หากต้องการสีสัน สามารถใส่สีผสมอาหารลงไปคนให้เข้ากันตอนนี้
        6. ตักมะพร้าวแก้วขึ้นมาวางบนถาดที่ปูกระดาษไขหรือถาดที่ทาด้วยน้ำมันเล็กน้อย เพื่อไม่ให้ติดถาด
        7. รอให้มะพร้าวแก้วเย็นตัวและแห้งเกาะตัวเข้ากันดี แล้วจึงเก็บในภาชนะที่มีฝาปิดเพื่อรักษาความกรอบ
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
