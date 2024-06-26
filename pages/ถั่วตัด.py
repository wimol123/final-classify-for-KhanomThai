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
kanom_img_path = os.getenv("COMPONENT_113_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ถั่วตัด: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ถั่วตัด")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ถั่วตัด เป็นขนมไทยโบราณที่มีมาช้านาน เชื่อกันว่ามีต้นกำเนิดมาจากภาคกลาง ลักษณะของขนมถั่วตัดนั้น เป็นแผ่นสี่เหลี่ยมสีเหลืองอ่อน ทำจากถั่วลิสงคั่วบด น้ำตาล และแบะแซ มีรสหวานมัน กรอบ ทานเล่นเพลิน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมถั่วลิสง: นำถั่วลิสงมาคั่วให้สุก แกะเปลือก พักไว้
        2. บดถั่ว: นำถั่วลิสงที่คั่วแล้วมาบดให้ละเอียด พักไว้
        3. เตรียมน้ำตาล: ตั้งกระทะ ใส่น้ำตาลปี๊บ น้ำเปล่า แบะแซ เกลือ คนจนน้ำตาลละลาย เคี่ยวจนเหนียว
        4. ผสมถั่ว: เทถั่วลิสงบดลงไปในกระทะ คนให้เข้ากัน จนส่วนผสมข้นหนืด
        5. เทใส่พิมพ์: เทส่วนผสมลงในพิมพ์ที่เตรียมไว้ เกลี่ยให้เรียบ รอให้เย็น
        6. ตัดเป็นชิ้น: ตัดขนมเป็นชิ้นสี่เหลี่ยมตามชอบ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ถั่วลิสง 500 กรัม
        - น้ำตาลปี๊บ 400 กรัม
        - น้ำเปล่า 200 มิลลิลิตร
        - แบะแซ 3 ช้อนโต๊ะ
        - เกลือ 1/2 ช้อนชา
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
