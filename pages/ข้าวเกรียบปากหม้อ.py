from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_23_PATH1")
# component_1_path = os.getenv("COMPONENT_109_PATH2")
# component_2_path = os.getenv("COMPONENT_109_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ข้าวเกรียบปากหม้อ",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวเกรียบปากหม้อ")
st.image(kanom_img_path, width=900)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมฝักบัว หรือที่บางคนเรียกว่า ขนมดอกบัว เป็นขนมไทยโบราณที่มีมานานกว่า 100 ปี นิยมทำกันในงานมงคล งานประเพณี และทานเล่นทั่วไป เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ชีวิตเจริญรุ่งเรือง
        เอกลักษณ์ของขนมฝักบัวคือ ลักษณะคล้ายดอกบัว กลม ฟู นุ่ม หอมใบเตย หวานมัน ทานคู่กับชาหรือกาแฟร้อนๆ
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - แป้งข้าวเจ้า 1 ถ้วยตวง
    - แป้งข้าวเหนียว 1/2 ถ้วยตวง
    - แป้งมัน 1/4 ถ้วยตวง
    - น้ำใบเตย 1 ถ้วยตวง
    - น้ำเปล่า 1/4 ถ้วยตวง
    - เกลือ 1/4 ช้อนชา
    - น้ำตาลทราย 1/2 ถ้วยตวง
    - น้ำมันพืชสำหรับทอด
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. ผสมแป้งข้าวเจ้า แป้งข้าวเหนียว แป้งมัน เกลือ น้ำใบเตย น้ำเปล่า คนให้เข้ากัน
        2. ใส่น้ำตาลทราย คนให้ละลาย
        3. พักแป้งไว้ 30 นาที
        4. ตั้งกระทะ ใส่น้ำมัน รอจนร้อน
        5. ตักแป้ง 1 ช้อนโต๊ะ เทลงในกระทะ
        6. ทอดจนขนมสุกเหลือง พอง
        7. ตักขนมขึ้น พักให้สะเด็ดน้ำมัน
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้แป้งข้าวเจ้าที่มีคุณภาพดี จะได้เนื้อขนมที่นุ่มฟู
        - สามารถปรับปริมาณน้ำตาลได้ตามชอบ
        - ควรทอดขนมในน้ำมันที่ร้อนพอดี จะได้ขนมที่กรอบนอกนุ่มใน
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
