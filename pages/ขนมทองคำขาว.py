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
kanom_img_path = os.getenv("COMPONENT_120_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองคำขาว: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🍰",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image(header_img_path)

# Display title
st.title("ขนมทองคำขาว")

st.image(kanom_img_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองคำขาว เป็นขนมไทยโบราณที่นิยมทำในงานมงคลต่างๆ มีลักษณะคล้ายทองคำแท่ง เชื่อกันว่าจะนำโชคลาภและความรุ่งเรืองมาสู่ผู้ทาน ทำจากไข่ขาว น้ำตาลทราย แป้ง อบจนสุก โรยหน้าด้วยทองคำเปลว
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **แป้ง:**
        1. ผสมแป้งข้าวเจ้า แป้งข้าวโพด แป้งท้าวยายม่อม เกลือ น้ำเปล่า คนจนส่วนผสมเข้ากัน พักไว้

        **ไส้:**
        1. ตีไข่ขาวจนตั้งยอดอ่อน
        2. ใส่ครีมออฟทาร์ทาร์ ตีต่อจนตั้งยอดแข็ง
        3. ใส่น้ำตาลทรายค่อยๆ ตีต่อจนตั้งยอด
        4. ค่อยๆ เทแป้งลงในไข่ขาว ตะล่อมให้เข้ากัน

        **อบขนม:**
        1. เทส่วนผสมลงพิมพ์ อบในเตาอบที่อุณหภูมิ 180 องศาเซลเซียส ประมาณ 20-25 นาที หรือจนสุก
        2. โรยหน้าด้วยทองคำเปลว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **แป้ง:**
        - แป้งข้าวเจ้า 100 กรัม
        - แป้งข้าวโพด 50 กรัม
        - แป้งท้าวยายม่อม 30 กรัม
        - เกลือ 1/4 ช้อนชา
        - น้ำเปล่า 100 มิลลิลิตร

        **ไส้:**
        - ไข่ขาว 3 ฟอง
        - ครีมออฟทาร์ทาร์ 1/4 ช้อนชา
        - น้ำตาลทราย 150 กรัม

        **ทองคำเปลว:** สำหรับโรยหน้า
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
