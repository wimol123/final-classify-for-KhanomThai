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
kanom_img_path = os.getenv("COMPONENT_221_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="ขนมหม้อตาล",
    page_icon="🍮",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมหม้อตาล")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมหม้อตาล เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในช่วงฤดูฝนที่มะพร้าวอ่อนมีขายมาก ขนมชนิดนี้มีเอกลักษณ์เฉพาะตัวคือแป้งด้านนอกจะแข็ง คล้ายกับแป้งพาย ส่วนด้านในจะเป็นน้ำตาลก้อนสีเหลืองทอง หอมหวานมัน

        ในอดีต ขนมหม้อตาลมักทำกันในหมู่บ้านชนบท นิยมทานกันในครอบครัว เพื่อนฝูง หรือใช้เป็นของว่างในงานต่างๆ ปัจจุบัน ขนมหม้อตาลเริ่มหาทานได้ยากขึ้น แต่ยังมีบางร้านที่ยังคงทำขนมชนิดนี้ขายอยู่
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**

        **ตัวแป้ง:**
        - แป้งสาลีอเนกประสงค์ 90 กรัม
        - ไข่แดง 1 ฟอง
        - กะทิ 1 ช้อนโต๊ะ
        - น้ำเย็น 1-2 ช้อนโต๊ะ

        **ไส้น้ำตาล:**
        - น้ำตาลทราย 150 กรัม
        - น้ำเปล่า 30 กรัม
        - กลิ่นมะลิ 1 ช้อนชา
        - สีผสมอาหาร (สีตามชอบ)

        **วิธีทำ:**

        **ตัวแป้ง:**
        1. ผสมแป้งสาลีอเนกประสงค์ เกลือ ไข่แดง กะทิ และน้ำเย็น นวดให้เข้ากันจนแป้งเนียนไม่ติดมือ
        2. พักแป้งไว้ 30 นาที
        3. แบ่งแป้งเป็นก้อนกลมๆ ประมาณ 20 กรัม
        4. คลึงแป้งเป็นแผ่นกลมบางๆ

        **ไส้น้ำตาล:**
        1. ผสมน้ำตาลทราย น้ำเปล่า และกลิ่นมะลิ นำไปเคี่ยวจนน้ำตาลละลายและเหนียวข้น
        2. แบ่งน้ำตาลเป็นก้อนกลมๆ ขนาดเท่ากับแป้ง
        3. ใส่ไส้น้ำตาลลงบนแผ่นแป้ง ห่อแป้งให้มิดชิด

        **การประกอบ:**
        1. วางขนมหม้อตาลลงบนพิมพ์ที่รองด้วยกระดาษไข
        2. อบไฟ 170 องศาเซลเซียส ประมาณ 20 นาที
        3. พักให้ขนมเย็นก่อนทาน
        """
    )

# Link back to Home.py
st.page_link("Home.py", label="Home", icon="↩️")
