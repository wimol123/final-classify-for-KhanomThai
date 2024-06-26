# This is a placeholder for ขนมหน่อไม้.py
from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_218_PATH1")
# Set page configuration
st.set_page_config(
    page_title="ขนมหน่อไม้",
    page_icon="🎋",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมหน่อไม้")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมหน่อไม้ เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในช่วงฤดูฝนที่หน่อไม้มีหน่ออ่อนๆ สดใหม่ ขนมชนิดนี้มีเอกลักษณ์เฉพาะตัวคือใช้หน่อไม้เป็นวัตถุดิบหลัก ผสมผสานกับแป้ง น้ำตาล กะทิ และมะพร้าวขูด
        ในอดีต ขนมหน่อไม้มักทำกันในหมู่บ้านชนบท นิยมทานกันในครอบครัว เพื่อนฝูง หรือใช้เป็นของว่างในงานต่างๆ ปัจจุบัน ขนมหน่อไม้เริ่มหาทานได้ยากขึ้น แต่ยังมีบางร้านที่ยังคงทำขนมชนิดนี้ขายอยู่
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**
        - หน่อไม้ไผ่ตง 1 กิโลกรัม
        - แป้งมัน 400 กรัม
        - แป้งข้าวเจ้า 100 กรัม
        - น้ำตาลทราย 400 กรัม
        - หัวกะทิ 150 กรัม
        - มะพร้าวขาวขูด 200 กรัม
        - เกลือป่น 1/2 ช้อนโต๊ะ
        - มะพร้าวขาวขูด (โรยหน้า)
        - ใบตอง

        **วิธีทำ:**
        1. นำหน่อไม้ไปต้มจนสุก ประมาณ 30 นาที
        2. ล้างหน่อไม้ให้สะอาด คั้นน้ำออกให้มากที่สุด
        3. สับหน่อไม้เป็นชิ้นเล็กๆ
        4. ผสมแป้งมัน แป้งข้าวเจ้า น้ำตาลทราย หัวกะทิ มะพร้าวขูด เกลือป่น และหน่อไม้สับ เข้าด้วยกัน
        5. แช่ส่วนผสมในตู้เย็น ประมาณ 30 นาที - 1 ชั่วโมง
        6. ตักส่วนผสมใส่ใบตอง พับปลายทั้งสองข้าง
        7. นึ่งขนมหน่อไม้ประมาณ 30 นาที
        8. โรยมะพร้าวขูดที่คั่วแล้วบนหน้าขนม
        """
    )

# Link back to Home.py
st.page_link("Home.py", label="Home", icon="↩️")
