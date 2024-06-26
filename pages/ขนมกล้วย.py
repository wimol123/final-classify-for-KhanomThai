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
kanom_img_path = os.getenv("COMPONENT_KhanomKruai_PATH1")
component_1_path = os.getenv("COMPONENT_KhanomKruai_PATH2")
component_2_path = os.getenv("COMPONENT_KhanomKruai_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมกล้วย")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมกล้วย หรือเข้าหนมกล้วย เป็นขนมซึ่งชาวล้านนานิยมทำรับประทาน 
โดยใช้แป้งข้าวเจ้าและกล้วยน้ำว้าเป็นส่วนผสมหลัก

คุณค่าทางโภชนาการ

กล้วยน้ำว้าช่วยแก้โรคกระเพาะได้ดีเนื่องจากมีสารแทนนิน 
ซึ่งมีฤทธิ์ในการเคลือบรักษากระเพาะและลำไส้ป้องกันการติดเชื้อ 
และยังมีฤทธิ์ในการช่วยลดกรดในกระเพาะอาหารได้เป็นอย่างดี

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=component_1_path)
with col2:
    st.header("วิธีทำ")
    st.image(image=component_1_path)

st.page_link("Home.py", label="Home", icon="↩️")
