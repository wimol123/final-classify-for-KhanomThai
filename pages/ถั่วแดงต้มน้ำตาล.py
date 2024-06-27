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
kanom_img_path = os.getenv("COMPONENT_118_PATH1")
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
st.title("ถั่วแดงต้มน้ำตาล")
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
เป็นของหวานที่พบเห็นได้ทั่วไปในประเทศจีน ทําจากถั่วแดงและน้ำตาลและปรุงคล้ายถั่วเขียวต้มน้ำตาล มักเสิร์ฟเย็นในช่วงฤดูร้อนและเสิร์ฟร้อนในฤดูหนาวซึ่งมีผลหลากหลายเช่น บรรเทาความร้อนของร่างกาย เป็นประโยชน์ต่อกระเพาะอาหารขับปัสสาวะ เสริมธาตุเหล็กในการสร้างเลือด ถั่วแดงต้มน้ำตาลยังสามารถใช้ทําไอศกรีมหวานเย็นแบบแท่งและหงโต้วปิงซึ่งเป็นของหวานยอดนิยมตามร้านฉาชานทิงในฮ่องกง

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ถั่วแดงเม็ดเล็ก 300 g  
    น้ำเปล่า 2000ml (สามารถเพิ่ม ลด ได้)  
    น้ำตาลทรายแดง หรือขาว ความหวานตามชอบ  
    สาคู 1ถ้วยตวงข้าวสาร  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. นำถั่วแดงเม็ดเล็กมาล้างทำความสะอาด แล้วนำมาแช่น้ำข้ามคืน (จำเป็นต้องแช่นะคะ)  
    2. ตั้งน้ำ 2000ml แล้วนำถั่วใส่ลงไปเลยไม่ต้องรอให้น้ำเดือด จากนั้นก็ต้มถั่วจนสุกและเม็ดถั่วแตกดี ถ้าระหว่างที่ต้มถั่วแล้วน้ำมันลดลง ก็ให้เติมน้ำได้เรื่อยๆ ใช้ไฟปกติ (เราไม่อยากให้ดูที่เวลา อยากให้ดูที่เม็ดถั่วนะคะ ถ้าเม็ดถั่วสุกและแตกเม็ด ก็ถือว่า ok พอถั่วสุกได้ที่ถึงค่อยใส่น้ำตาลนะคะ)
    3. พอถั่วสุกแตกเม็ดดีแล้ว ก็มาต้มสาคูกันค่ะ ตั้งน้ำให้เดือดแล้วนำสาคูลงต้มให้สุก วิธีดูว่าใช้ได้หรือยัง ให้ดูที่เม็ดแป้งสีขาวๆ ต้มจนให้เห็นเม็ดแป้งสีขาวน้อยที่สุด ตามรูป จากนั้นก็กรองเอาแต่เม็ดสาคู แล้วนำไปล้างน้ำ จากนั้นนำเม็ดสาคูไปแช่น้ำอุณหภูมิห้อง 5 นาที
    4. จากนั้นก็นำเม็ดสาคูใส่ลงหม้อต้มถั่วแล้วคนให้เม็ดสาคูกับถั่วเข้ากันดี ไม่มีเม็ดสาคูจับตัวกันเป็นก้อนพร้อมเสิร์ฟ
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
