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
kanom_img_path = os.getenv("COMPONENT_112_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมถั่วกวน: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมถั่วกวน")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมถั่วกวน เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในงานมงคลต่างๆ เชื่อกันว่ามีต้นกำเนิดมาจากภาคกลาง ลักษณะของขนมถั่วกวนนั้น มีเนื้อสัมผัสนุ่มละมุน หวานมัน มีกลิ่นหอมของมะพร้าวและใบเตย นิยมทานคู่กับชาหรือกาแฟ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมถั่ว: นำถั่วเขียวเลาะเปลือกมาล้างน้ำให้สะอาด แช่น้ำประมาณ 3-4 ชั่วโมง นำไปนึ่งหรือต้มจนสุก
        2. บดถั่ว: นำถั่วที่สุกแล้วมาบดให้ละเอียด พักไว้
        3. กวนถั่ว: ตั้งกระทะ ใส่น้ำตาลทราย น้ำเปล่า ใบเตย และเกลือ คนจนน้ำตาลทรายละลาย เทถั่วบดลงไป กวนจนเนื้อถั่วเนียน แห้ง และไม่ติดกระทะ
        4. ใส่กะทิ: ใส่น้ำกะทิ กวนต่อจนเนื้อขนมข้นหนืด ขึ้นเงา
        5. พักขนม: เทขนมใส่พิมพ์ รอให้เย็น ตัดเป็นชิ้นตามชอบ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ถั่วเขียวเลาะเปลือก 500 กรัม
        - น้ำตาลทราย 250 กรัม
        - น้ำเปล่า 250 มิลลิลิตร
        - ใบเตย 2-3 ใบ
        - เกลือ 1/2 ช้อนชา
        - น้ำกะทิ 200 มิลลิลิตร
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
