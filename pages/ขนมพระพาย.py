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
kanom_img_path = os.getenv("COMPONENT_161_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมพระพาย: ขนมไทยโบราณ หอมหวานมัน ทานเล่นหรือทานคู่กับอาหารคาว",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมพระพาย: ขนมไทยโบราณ หอมหวานมัน ทานเล่นหรือทานคู่กับอาหารคาว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมพระพายเป็นขนมไทยโบราณที่มีมานานกว่า 200 ปี นิยมทำกันในงานมงคล งานประเพณี และทานเล่นทั่วไป เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ชีวิตกลมเกลียว รักกันแน่นแฟ้น
        เอกลักษณ์ของขนมพระพายคือ แป้งเหนียวนุ่ม ห่อไส้ถั่วกวนหวานมัน ราดด้วยน้ำกะทิหอมๆ ทานคู่กับกล้วยไข่เชื่อม
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - แป้งข้าวเหนียว 2 ถ้วยตวง
    - น้ำเปล่า 1 ถ้วยตวง
    - เกลือ 1/4 ช้อนชา
    """
)

st.markdown(
    """
    **ไส้:**
    - ถั่วเขียวกวน 1 ถ้วยตวง
    - กะทิ 1/2 ถ้วยตวง
    - น้ำตาลทราย 1/2 ถ้วยตวง
    - เกลือ 1/4 ช้อนชา
    """
)

st.markdown(
    """
    **น้ำกะทิ:**
    - กะทิ 2 ถ้วยตวง
    - น้ำตาลปี๊บ 1 ถ้วยตวง
    - เกลือ 1/4 ช้อนชา
    - ใบเตย 2-3 ใบ
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **แป้ง:**
        1. ผสมแป้งข้าวเหนียว น้ำเปล่า เกลือ นวดจนแป้งเนียน
        2. แบ่งแป้งเป็นก้อนกลมๆ
        3. กดแป้งให้เป็นแผ่นบางๆ

        **ไส้:**
        1. ผสมถั่วเขียวกวน กะทิ น้ำตาลทราย เกลือ คนให้เข้ากัน
        2. ปั้นไส้ถั่วเป็นก้อนกลมๆ

        **น้ำกะทิ:**
        1. ผสมกะทิ น้ำตาลปี๊บ เกลือ ใบเตย คนจนน้ำตาลละลาย
        2. ตั้งไฟ เคี่ยวจนน้ำกะทิข้น

        **การประกอบ:**
        1. ห่อไส้ถั่วด้วยแป้ง มัดให้แน่น
        2. ต้มน้ำให้เดือด ใส่ขนมพระพายลงต้มจนสุก
        3. ตักขนมพระพายขึ้น ราดด้วยน้ำกะทิ
        4. ทานคู่กับกล้วยไข่เชื่อม และน้ำแข็ง
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้แป้งข้าวเหนียวที่มีคุณภาพดี จะได้เนื้อแป้งที่เหนียวนุ่ม
        - สามารถปรับปริมาณน้ำตาลได้ตามชอบ
        - ควรเคี่ยวน้ำกะทิด้วยไฟอ่อน จะได้น้ำกะทิที่หอมมัน
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
