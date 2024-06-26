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
kanom_img_path = os.getenv("COMPONENT_128_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองเอก: ขนมไทยมงคล อร่อย หวานมัน",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมทองเอก")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองเอก เป็นขนมไทยโบราณที่มีมาช้านาน จัดอยู่ในกลุ่ม "ขนมทอง" นิยมทำขึ้นเพื่อเป็นของว่าง ของมงคล หรือใช้ประกอบพิธีกรรมต่างๆ ชื่อ "ทองเอก" นั้น หมายถึง การเป็นที่หนึ่ง สื่อถึงความเจริญรุ่งเรือง เงินทอง และความสำเร็จ ขนมทองเอกมีเอกลักษณ์เฉพาะตัวที่โดดเด่นคือ มีสีเหลืองอร่าม รูปร่างคล้ายดอกไม้ตูม และประดับด้วยทองคำเปลว
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมทองเอก มีวิธีทำดังนี้:**

        1. **ทำแป้ง:** ผสมไข่แดง, แป้งสาลีอเนกประสงค์, แป้งมัน, เกลือ, และกะทิ คนจนแป้งเนียน พักไว้
        2. **ทำน้ำกะทิ:** ผสมกะทิ, น้ำตาลทราย, และเกลือ คนจนเข้ากัน นำไปตั้งไฟจนส่วนผสมข้นเหนียว พักไว้
        3. **ปั้นขนม:** แบ่งแป้งเป็นก้อนกลมๆ รีดแป้งเป็นแผ่นบาง ตักไส้ใส่ตรงกลาง พับแป้งเป็นรูปสามเหลี่ยม ทาไข่แดงบางๆ
        4. **อบขนม:** นำขนมไปอบในเตาอบที่อุณหภูมิ 180 องศาเซลเซียส ประมาณ 20 นาที หรือจนขนมสุกเหลือง
        5. **ตกแต่ง:** ประดับขนมด้วยทองคำเปลว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - **ไข่แดง** 3 ฟอง
        - **แป้งสาลีอเนกประสงค์** 1 ถ้วยตวง
        - **แป้งมัน** 1/2 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา
        - **กะทิ** 1 ถ้วยตวง

        **ไส้:**
        - **กะทิ** 1 ถ้วยตวง
        - **น้ำตาลทราย** 1/2 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา

        **เพิ่มเติม:**
        - **ไข่แดง** สำหรับทาหน้าขนม
        - **ทองคำเปลว** สำหรับตกแต่ง
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
