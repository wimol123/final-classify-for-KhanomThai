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
kanom_img_path = os.getenv("COMPONENT_39_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวหลาม: ขนมไทยโบราณ หอมมัน กลมกล่อม ชวนลิ้มลอง",
    page_icon="🍙",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวหลาม: ขนมไทยโบราณ หอมมัน กลมกล่อม ชวนลิ้มลอง")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
        ข้าวหลามมีต้นกำเนิดมาจากภาคใต้ของไทย นิยมทำกันในงานบุญ งานมงคล หรือต้อนรับแขกผู้มาเยือน ในอดีตนั้น ข้าวเป็นอาหารหลักของคนไทย ข้าวหลามจึงเป็นการแปรรูปข้าวที่เหลือจากมื้ออาหารให้อร่อยและเก็บไว้ทานได้นาน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมข้าวเหนียว: แช่ข้าวเหนียวเขี้ยวงู 3-4 ชั่วโมง นึ่งจนสุก
        2. เตรียมกะทิ: ผสมกะทิ น้ำตาลปี๊บ เกลือ และใบเตย ต้มจนน้ำตาลละลาย
        3. คลุกข้าวเหนียว: ใส่ข้าวเหนียวที่นึ่งสุกลงในกะทิที่ต้มไว้ คลุกเคล้าให้เข้ากันดี
        4. ห่อข้าวหลาม: ใส่ข้าวเหนียวที่คลุกกะทิลงใน筒ไม้ไผ่ที่เตรียมไว้ ห่อด้วยใบตอง
        5. เผาข้าวหลาม: นำข้าวหลามไปเผาบนเตาถ่านจนสุก
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ข้าวเหนียวเขี้ยวงู 500 กรัม
        - กะทิ 200 มล.
        - น้ำตาลปี๊บ 100 กรัม
        - เกลือป่น 1/2 ช้อนชา
        - ใบเตย 2-3 ใบ
        - ใบตองสำหรับห่อ
        - ไม้ไผ่สำหรับใส่
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - สามารถเปลี่ยนกะทิเป็นน้ำเปล่าได้
        - ข้าวหลามสามารถเก็บไว้ทานได้นาน โดยใส่ในภาชนะปิดสนิท
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
