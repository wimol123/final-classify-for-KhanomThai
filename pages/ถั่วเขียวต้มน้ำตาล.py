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
kanom_img_path = os.getenv("COMPONENT_116_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมถั่วเขียวต้มน้ำตาล: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมถั่วเขียวต้มน้ำตาล")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมถั่วเขียวต้มน้ำตาล เป็นขนมหวานที่ได้รับความนิยมมายาวนาน มีต้นกำเนิดจากประเทศจีน นิยมทานในฤดูร้อนเพื่อดับกระหาย เชื่อกันว่าช่วยคลายร้อน 
        บำรุงร่างกายในประเทศไทย ขนมถั่วเขียวต้มน้ำตาลเป็นของหวานที่หาทานได้ง่าย มีสูตรและวิธีทำที่หลากหลาย นิยมทานคู่กับน้ำแข็งไส ลอดช่อง
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมถั่วเขียว: ล้างถั่วเขียวให้สะอาด แช่น้ำประมาณ 3-4 ชั่วโมง หรือค้างคืน
        2. ต้มถั่วเขียว: นำถั่วเขียวที่แช่น้ำไว้ ใส่หม้อใส่น้ำ ต้มจนถั่วเขียวสุกเปื่อย
        3. ปรุงน้ำตาล: ตั้งกระทะใส่น้ำเปล่า น้ำตาลทราย ใบเตย เกลือ คนจนน้ำตาลทรายละลาย เคี่ยวจนน้ำตาลเหนียว
        4. ผสมถั่วเขียว: เทถั่วเขียวที่ต้มสุกแล้วลงไปในกระทะน้ำตาล คนให้เข้ากัน
        5. ต้มต่อ: ต้มต่อจนถั่วเขียวดูใส น้ำตาลซึมเข้าเนื้อถั่ว
        6. พักขนม: ตักขนมถั่วเขียวต้มน้ำตาลใส่ถ้วย พักให้เย็น
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ถั่วเขียว 200 กรัม
        - น้ำตาลทราย 150 กรัม
        - น้ำเปล่า 1.5 ลิตร
        - ใบเตย 2-3 ใบ
        - เกลือ 1/4 ช้อนชา
        
        **หมายเหตุ:**
        - สามารถปรับปริมาณน้ำตาลทรายได้ตามชอบ
        - ใบเตยสามารถอบควันเทียนเพื่อเพิ่มความหอม
        - ขนมถั่วเขียวต้มน้ำตาลสามารถเก็บไว้ได้นานโดยใส่ในภาชนะที่ปิดสนิทและเก็บในตู้เย็น
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
