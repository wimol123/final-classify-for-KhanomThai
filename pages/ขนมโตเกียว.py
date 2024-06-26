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
kanom_img_path = os.getenv("COMPONENT_107_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมโตเกียว: ขนมหน้าโรงเรียนสุดคลาสสิก",
    page_icon="🥞",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมโตเกียว")
st.image(kanom_img_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมโตเกียว เป็นขนมไทยชนิดหนึ่ง คล้ายกับโดรายากิของญี่ปุ่น แป้งแพนเค้กชิ้นบางๆ ทำให้ร้อนบนเตาขนาดเล็กที่มีหน้าเตาแบน 
        แล้วม้วนห่อไส้ซึ่งมีด้วยกันหลากหลายไส้ เช่น ไส้กรอก, ไข่นกกระทา, ไส้ครีมรสหวานต่าง ๆ รวมถึงอาจจะมีไส้พิเศษในบางร้าน เช่น ชีส, บิ๊กไบต์, ไก่ยอ หรือแซลมอน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมแป้ง: ผสมแป้งสาลีอเนกประสงค์ แป้งข้าวเจ้าหรือแป้งมันสำปะหลัง ผงฟู เกลือ น้ำตาล ไข่ นมสด และกลิ่นวานิลลา พักแป้งไว้
        2. เตรียมไส้: เตรียมไส้ตามชอบ เช่น ไส้ครีมหวาน ไส้กรอก ไข่นกกระทา ฯลฯ
        3. ทำขนมโตเกียว: ตั้งกระทะ ทาเนยบางๆ รอจนกระทะร้อน เทแป้งลงบนกระทะ รอจนแป้งเริ่มสุก ใส่ไส้ลงไป พับแป้งเป็นรูปครึ่งวงกลม
        4. จัดเสิร์ฟ: โรยหน้าด้วยน้ำตาลป่น ทานร้อนๆ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **แป้ง:**
        - แป้งสาลีอเนกประสงค์ 140 กรัม
        - แป้งข้าวเจ้าหรือแป้งมันสำปะหลัง 30 กรัม
        - ผงฟู 1 ช้อนชา
        - เกลือ 1/4 ช้อนชา
        - น้ำตาลทราย 50 กรัม
        - ไข่ไก่ 2 ฟอง
        - นมสด 120 กรัม
        - กลิ่นวานิลลา 1 ช้อนชา
        
        **ไส้:**
        - ไส้ครีมหวาน: ครีม Whipping cream, น้ำตาลทราย, กลิ่นวานิลลา
        - ไส้กรอก: ไส้กรอกหั่นเต๋า
        - ไข่นกกระทา: ไข่นกกระทาต้มสุก บด
        - ฯลฯ (ตามชอบ)
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
