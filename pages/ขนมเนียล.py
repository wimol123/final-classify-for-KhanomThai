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
khanomneil = os.getenv("COMPONENT_137_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมเนียล: ขนมพื้นบ้านจากภูมิปัญญาท้องถิ่น",
    page_icon="🍡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมเนียล: ขนมพื้นบ้านจากภูมิปัญญาท้องถิ่น")
st.image(image=khanomneil)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเนียล เป็นขนมพื้นบ้านของชาวไทยเชื้อสายเขมรในภาคตะวันออกเฉียงเหนือตอนล่าง โดยเฉพาะในจังหวัดสุรินทร์ ขนมชนิดนี้มีความโดดเด่นทั้งรสชาติและหน้าตา มีลักษณะคล้ายพิซซ่า แต่ทำจากแป้งข้าวเหนียว
        ชื่อของขนมมาจากภาชนะที่ใช้ทำขนม ซึ่งเรียกว่า "เนียล" ในภาษาเขมร แปลว่า "ทะนาน" ในอดีตคนเขมรนิยมใช้กะลามะพร้าวผ่าครึ่งมาทำเป็นทะนาน จึงเรียกขนมนี้ว่า "ขนมเนียล"
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        การทำขนมเนียล:
        1. เตรียมแป้ง: นำแป้งข้าวเหนียวมาผสมกับน้ำตาลทรายแดง, น้ำตาลอ้อย, เกลือ และมะพร้าวขูด คลุกเคล้าให้เข้ากัน แล้วทิ้งไว้ 30 นาที
        2. นึ่งขนม: ตั้งหม้อน้ำ, ใส่ใบเตย, รอจนเดือด นำแป้งที่เตรียมไว้ใส่ลงในกะลามะพร้าวที่รองด้วยใบมะพร้าว วางบนหม้อนึ่ง, ปิดฝา นึ่งจนสุก
        3. พักขนม: เมื่อขนมสุก, นำออกมาพักบนใบตอง รอให้เย็น
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - แป้งข้าวเหนียว
        - น้ำตาลทรายแดง
        - น้ำตาลอ้อย
        - เกลือ
        - มะพร้าวขูด
        - ใบเตย
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - แป้งข้าวเหนียวควรเป็นแป้งข้าวเหนียวใหม่
        - น้ำตาลทรายแดงและน้ำตาลอ้อยสามารถปรับปริมาณได้ตามชอบ
        - มะพร้าวขูดควรเป็นมะพร้าวทึนทึก
        - ควรนึ่งขนมด้วยไฟอ่อนๆ
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
