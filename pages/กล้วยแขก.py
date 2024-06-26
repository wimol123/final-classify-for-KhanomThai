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
kanom_img_path = os.getenv("COMPONENT_Kluaikhaek_PATH1")
component_1_path = os.getenv("COMPONENT_Kluaikhaek_PATH2")
component_2_path = os.getenv("COMPONENT_Kluaikhaek_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path, use_column_width=True)
st.title("กล้วยแขก")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
    กล้วยทอด หรือกล้วยแขก เกิดขึ้นในสยามประเทศครั้งแรก ในสมัยกรุงศรีอยุธยาศรีรามเทพนคร เป็นราชธานี 
    ซึ่งชาวอิสลาม หรือที่บ้านเราเรียกเขาว่าแขก เป็นศาสตราจารย์เกี่ยวกับอาหารประเภททอดทุกชนิด 
    และในช่วงนั้นสยามประเทศยังไม่เคยทำอาหารชนิดใดให้สุก 
    และสามารถกินได้จากการทอดมาก่อนเลย พอมีคนทำสูตรเอาแป้งมาผสมกับน้ำ 
    และใส่เครื่องเทศลงไป และนำกล้วยของไทยไปชุบและนำไปทอด 
    จึงเรียกว่า กล้วยแขก เพราะการทำอาหารให้สุกจากการทอด 
    มาจากคนอิสลาม หรือบ้านเราเรียกเขาว่า แขก นั่นเอง
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=component_1_path)

with col2:
    st.header("วิธีทำ")
    st.image(image=component_2_path)

st.page_link("Home.py", label="Home", icon="↩️")
