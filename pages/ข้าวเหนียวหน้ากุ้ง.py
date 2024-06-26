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
kanom_img_path = os.getenv("COMPONENT_53_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ข้าวเหนียวหน้ากุ้ง: ขนมไทยโบราณ สูตรเด็ด",
    page_icon="🍤",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวเหนียวหน้ากุ้ง: ขนมไทยโบราณ")
st.image(kanom_img_path)
# Ingredients
st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ข้าวเหนียวมูน:**
        - ข้าวเหนียวเขี้ยวงู 500 กรัม
        - กะทิ 400 มิลลิลิตร
        - น้ำตาลทราย 200 กรัม
        - เกลือ 1/2 ช้อนชา
        - ใบเตย 3-4 ใบ
        - ผงขมิ้น 1/4 ช้อนชา

        **หน้ากุ้ง:**
        - กุ้งสด 200 กรัม
        - มะพร้าวขูดขาว 100 กรัม
        - หอมแดง 5 หัว
        - กระเทียม 3 กลีบ
        - รากผักชี 1 ต้น
        - พริกไทยขาว 1/2 ช้อนชา
        - น้ำมันพืช 2 ช้อนโต๊ะ
        - น้ำตาลทราย 2 ช้อนโต๊ะ
        - เกลือ 1/4 ช้อนชา
        - ใบมะกรูดซอย 1 ช้อนโต๊ะ
        """
    )

# Method
st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ข้าวเหนียวมูน:**
        1. ล้างข้าวเหนียวเขี้ยวงูให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
        2. ผสมกะทิ น้ำตาลทราย เกลือ ใบเตย และผงขมิ้น นำไปตั้งไฟจนเดือด
        3. เทน้ำกะทิเดือดลงบนข้าวเหนียวที่แช่ไว้ คลุกเคล้าให้เข้ากัน
        4. นำข้าวเหนียวที่คลุกกะทิแล้วไปนึ่งจนสุก ประมาณ 30-40 นาที

        **หน้ากุ้ง:**
        1. ตำกุ้ง หอมแดง กระเทียม รากผักชี และพริกไทยขาวให้ละเอียด
        2. ตั้งกระทะ ใส่น้ำมันพืช ใส่เครื่องที่ตำไว้ลงไปผัดจนหอม
        3. ปรุงรสด้วยน้ำตาลทราย เกลือ และใบมะกรูดซอย ผัดต่อจนเข้ากัน
        4. ตักหน้ากุ้งที่ผัดไว้ ราดบนข้าวเหนียวมูนที่นึ่งสุกแล้ว
        """
    )

# Tips
st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้ข้าวเหนียวเขี้ยวงู จะทำให้ข้าวเหนียวมีกลิ่นหอมและนุ่ม
        - แช่ข้าวเหนียวเขี้ยวงูไว้หลายๆ ชั่วโมง จะทำให้ข้าวเหนียวมูนสุกเร็วและนุ่มขึ้น
        - กะทิควรเป็นกะทิสด จะทำให้ข้าวเหนียวมูนหอมมัน
        - ปรุงรสหน้ากุ้งให้พอดีตามชอบ
        - โรยหน้าข้าวเหนียวหน้ากุ้งด้วยงาขาวคั่ว จะช่วยเพิ่มความหอมและอร่อย
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
