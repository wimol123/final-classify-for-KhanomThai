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
khanomninews = os.getenv("COMPONENT_136_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมนิ่มนวล: ขนมไทยโบราณ หอม หวาน มัน ละมุนลิ้น",
    page_icon="🍡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมนิ่มนวล: ขนมไทยโบราณ หอม หวาน มัน ละมุนลิ้น")
st.image(image=khanomninews)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมนิ่มนวล เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว หากินได้ยาก แต่มีเสน่ห์ดึงดูดผู้คนด้วยรสชาติที่หอม หวาน มัน และเนื้อสัมผัสที่นุ่มละมุนละลายในปาก
        ขนมนิ่มนวลมีต้นกำเนิดจากทางภาคตะวันออกของประเทศไทย โดยเฉพาะจังหวัดระยอง สูตรดั้งเดิมสืบทอดมายาวนานกว่า 100 ปี ปัจจุบันหาซื้อได้ยาก แต่ยังพอมีบางร้านที่ทำและขายอยู่
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        การทำขนมนิ่มนวลนั้น ต้องอาศัยความประณีตและความพิถีพิถัน โดยขั้นตอนคร่าวๆ ดังนี้
        1. เตรียมแป้ง: นำข้าวเจ้าและข้าวเหนียวมา voorgekookt ให้สุก จากนั้นนำมาตำหรือโม่ให้ละเอียด
        2. เตรียมน้ำเชื่อม: นำน้ำตาลทราย น้ำเปล่า และใบเตยมาเคี่ยวจนน้ำเชื่อมข้น
        3. คลุกแป้งกับน้ำเชื่อม: นำแป้งที่เตรียมไว้มาคลุกกับน้ำเชื่อมร้อน นวดจนแป้งเนียนและไม่ติดมือ
        4. นึ่งขนม: ปั้นแป้งเป็นก้อนกลม นำไปนึ่งจนสุก
        5. คลุกมะพร้าว: นำมะพร้าวขูดที่นึ่งสุกมาคลุกกับขนมนิ่มนวล
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - แป้งข้าวเจ้า
        - แป้งข้าวเหนียว
        - น้ำตาลทราย
        - น้ำเปล่า
        - ใบเตย
        - มะพร้าวขูด
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - แป้งที่ใช้ควรเป็นแป้งข้าวเจ้าและแป้งข้าวเหนียวอย่างดี
        - น้ำเชื่อมควรมีอุณหภูมิที่ร้อนพอประมาณ
        - ควรนึ่งขนมด้วยไฟอ่อนๆ
        - มะพร้าวขูดควรเป็นมะพร้าวทึนทึก
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
