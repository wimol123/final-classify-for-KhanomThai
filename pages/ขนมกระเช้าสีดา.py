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
kanom_img_path = os.getenv("COMPONENT_KhanomKrachaoSida_PATH1")
component_1_path = os.getenv("COMPONENT_KhanomKrachaoSida_PATH2")
component_2_path = os.getenv("COMPONENT_KhanomKrachaoSida_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมกระเช้าสีดา")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมกระเช้าสีดา เป็นขนมไทยชาววังชนิดนี้มีที่มาจากต้นกระเช้าสีดาในวรรณคดีรามเกียรติ์ ทำมาจากแป้ง 
รูปทรงคล้ายกับกระเช้า และส่วนที่เป็นไส้ขนมทำจากมะพร้าวสีสันสวยงาม 
ปัจจุบันหารับประทานได้ค่อนข้างยาก เนื่องจากต้องใช้ความประณีตและละเอียดอ่อนในการทำ 
สมัยโบราณนิยมใช้ในงานทำบุญ งานแต่ง เทศกาลสำคัญต่าง ๆ
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
