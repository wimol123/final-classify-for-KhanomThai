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
kanom_img_path = os.getenv("COMPONENT_38_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวหมาก: เอกลักษณ์ความอร่อย หอมมัน กลมกล่อม",
    page_icon="🍡",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวหมาก: เอกลักษณ์ความอร่อย หอมมัน กลมกล่อม")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
        ข้าวหมากมีต้นกำเนิดมาจากภาคใต้ของไทย นิยมทำกันในงานบุญ งานมงคล หรือต้อนรับแขกผู้มาเยือน ในอดีตนั้น ข้าวเป็นอาหารหลักของคนไทย ข้าวหมากจึงเป็นการแปรรูปข้าวที่เหลือจากมื้ออาหารให้อร่อยและเก็บไว้ทานได้นาน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมข้าวเหนียว: แช่ข้าวเหนียวเขี้ยวงู 3-4 ชั่วโมง นึ่งจนสุก
        2. เตรียมลูกแป้งข้าวหมาก: นำลูกแป้งข้าวหมากมาละลายน้ำ
        3. คลุกข้าวเหนียว: ใส่ลูกแป้งข้าวหมากที่ละลายน้ำลงในข้าวเหนียวที่นึ่งสุก คลุกเคล้าให้เข้ากันดี
        4. หมักข้าวเหนียว: ใส่ข้าวเหนียวที่คลุกแป้งลงในภาชนะ ปิดฝาหมักไว้ 2-3 วัน
        5. นึ่งข้าวหมาก: นำข้าวหมากที่หมักไว้ไปนึ่งจนสุก
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ข้าวเหนียวเขี้ยวงู 500 กรัม
        - ลูกแป้งข้าวหมาก 2-3 ลูก
        - น้ำเปล่า
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - ควรเลือกใช้ลูกแป้งข้าวหมากที่มีคุณภาพดี
        - ข้าวหมากสามารถเก็บไว้ทานได้นาน โดยใส่ในภาชนะปิดสนิท
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
