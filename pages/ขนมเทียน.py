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
kanom_img_path = os.getenv("COMPONENT_130_PATH1")
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
st.title("ขนมเทียน")
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมเทียน หรือ ขนมนมสาว ทางภาคเหนือเรียกว่า ขนมจ็อก ซึ่งเป็นขนมที่นิยมใช้ในงานบุญของชาวเชียงใหม่โดยเฉพาะเทศกาลสงกรานต์ แต่เดิมมีไส้มะพร้าวและไส้ถั่วเขียว แต่ในปัจจุบันมีการดัดแปลงไส้ขนมจ็อกออกไปหลากหลายมาก
การทำขนมเทียนมีมาตั้งแต่สมัยโบราณ เป็นประเพณีของคนโบราณที่มักจะทำขนมเทียนไปทำบุญหรือทำ เพื่อประเพณีต่างๆ ซึ่งวิธีการทำขนมเป็นวิธีการดั้งเดิมและเป็นที่เลื่องลือทางรสชาติความอร่อย
ขนมเทียน ขนมของไหว้เจ้าที่ ขนมเข่ง ขนมไหว้เจ้าและบรรพบุรุษของชาวจีน

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    วัตถุดิบในการทำแป้ง  
    • แป้งข้าวเหนียว 300 กรัม  
    • น้ำตาลปี๊บ 100 กรัม  
    • กะทิ 200 มิลลิลิตร  
    • ใบตอง  
      
    วัตถุดิบในการทำไส้หวาน  
      
    • มะพร้าวทึนทึกขูดฝอย 2 ถ้วยตวง  
    • น้ำตาลปี๊บ หรือน้ำตาลมะพร้าว 150 กรัม  
    • เกลือป่น 1 ช้อนชา  
    • น้ำเปล่า 1/2 ถ้วยตวง  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
   
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
