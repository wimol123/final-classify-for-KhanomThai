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
kanom_img_path = os.getenv("COMPONENT_80_PATH1")
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
st.title("ขนมเจิมมาศ")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
เจิม แปลว่า เพิ่มหรือเสริมเพื่อความเป็นมงคล  
มาศ แปลว่า ทอง  
เจิมด้วยทองเพื่อความเป็นมงคล และเป็นของมีค่า 
ควรค่าแก่การบริโภคเพื่อมงคลชีวิต ตัวขนมด้านนอกทำมาจากทองเอก 
ไส้ขนมทำมาจากถั่วกวนสีเหลืองทองสอดไส้ด้วยไข่เค็ม 
และติดทองคำเปลวด้านบนเพื่อความเป็นมงคลหากใช้มอบเป็นของขวัญ 
เปรียบเสมือนได้มอบสิ่งมีค่าเป็นสิริมงคลแก่ผู้รับ

"""
st.markdown(multi)

# col1, col2 = st.columns(2)

# with col1:
#     st.header("ส่วนประกอบ")
#     multi = """


#     """
#     st.markdown(multi)
# with col2:
#     st.header("วิธีทำ")
#     multi = """


#     """
#     st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
