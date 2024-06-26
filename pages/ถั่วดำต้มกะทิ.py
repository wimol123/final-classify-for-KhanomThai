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
kanom_img_path = os.getenv("COMPONENT_117_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ถั่วดำต้มกะทิ: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ถั่วดำต้มกะทิ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ถั่วดำต้มกะทิ เป็นขนมไทยโบราณที่มีมาช้านาน เชื่อกันว่ามีต้นกำเนิดมาจากภาคกลาง ลักษณะของขนมถั่วดำต้มกะทิ นั้น มีเนื้อสัมผัสนุ่มละมุน หวานมัน มีกลิ่นหอมของมะพร้าวและใบเตย นิยมทานคู่กับชาหรือกาแฟ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมถั่วดำ: ล้างถั่วดำให้สะอาด แช่น้ำประมาณ 3-4 ชั่วโมง หรือค้างคืน
        2. ต้มถั่วดำ: นำถั่วดำที่แช่น้ำไว้ ใส่หม้อใส่น้ำ ต้มจนถั่วดำสุกเปื่อย
        3. เตรียมน้ำกะทิ: ตั้งกระทะ ใส่กะทิ น้ำตาลทราย ใบเตย เกลือ คนจนน้ำตาลทรายละลาย เคี่ยวจนน้ำกะทิเดือด
        4. ผสมถั่วดำ: เทถั่วดำที่ต้มสุกแล้วลงไปในกระทะน้ำกะทิ คนให้เข้ากัน
        5. ต้มต่อ: ต้มต่อจนถั่วดำดูใส น้ำกะทิซึมเข้าเนื้อถั่ว
        6. พักขนม: ตักขนมถั่วดำต้มกะทิใส่ถ้วย พักให้เย็น
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ถั่วดำ 200 กรัม
        - กะทิ 400 มิลลิลิตร
        - น้ำตาลทราย 150 กรัม
        - น้ำเปล่า 100 มิลลิลิตร
        - ใบเตย 2-3 ใบ
        - เกลือ 1/4 ช้อนชา
        
        **หมายเหตุ:**
        - สามารถปรับปริมาณน้ำตาลทรายได้ตามชอบ
        - ใบเตยสามารถอบควันเทียนเพื่อเพิ่มความหอม
        - ขนมถั่วดำต้มกะทิสามารถเก็บไว้ได้นานโดยใส่ในภาชนะที่ปิดสนิทและเก็บในตู้เย็น
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
