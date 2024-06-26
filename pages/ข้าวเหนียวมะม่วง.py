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
kanom_img_path = os.getenv("COMPONENT_49_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ข้าวเหนียวมะม่วง: เอกลักษณ์ความอร่อย หวานมัน ลงตัว",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวเหนียวมะม่วง: เอกลักษณ์ความอร่อย หวานมัน ลงตัว")
st.image(image=kanom_img_path, width=1000)
# Display introduction
st.markdown(
    """
    ข้าวเหนียวมะม่วง เป็นขนมไทยที่โด่งดังทั่วโลก มีต้นกำเนิดมาจากภูมิปัญญาไทยในอดีต นิยมทานคู่กับมะม่วงตามฤดูกาล โดยเฉพาะมะม่วงน้ำดอกไม้ หรือมะม่วงอกร่องในช่วงปลายฝนต้นหนาว
    """
)

st.title("เอกลักษณ์ของข้าวเหนียวมะม่วง")
st.markdown(
    """
    - **ความกลมกล่อม:** รสหวานมันของข้าวเหนียวมูนผสมผสานกับรสหวานอมเปรี้ยวของมะม่วงสุก ลงตัวอร่อย
    - **ความหอม:** ข้าวเหนียวมูนหอมกะทิ มะม่วงสุกหอมหวาน ทานคู่กันยิ่งเพิ่มความหอม
    - **ทานคู่กับมะม่วงตามฤดูกาล:** นิยมทานคู่กับมะม่วงน้ำดอกไม้ในช่วงฤดูร้อน หรือมะม่วงอกร่องในช่วงปลายฝนต้นหนาว
    """
)

st.title("วิธีทำข้าวเหนียวมะม่วง")

st.markdown(
    """
    **ส่วนผสมข้าวเหนียว:**
    - ข้าวเหนียวเขี้ยวงู 500 กรัม
    - กะทิ 400 มล.
    - เกลือ 1/2 ช้อนชา
    - น้ำตาลทราย 1/4 ถ้วยตวง
    - ใบเตย 2-3 ใบ

    **ส่วนผสมมะม่วง:**
    - มะม่วงสุก 2-3 ลูก (มะม่วงน้ำดอกไม้ หรือมะม่วงอกร่อง)

    **น้ำกะทิ (สำหรับราด):**
    - กะทิ 200 มล.
    - เกลือ 1/4 ช้อนชา
    - น้ำตาลทราย 1/4 ถ้วยตวง (หรือตามชอบ)
    - ใบเตย 1-2 ใบ
    """
)

st.title("ขั้นตอนการทำ")

st.markdown(
    """
    **ทำข้าวเหนียวมูน:**
    1. ล้างข้าวเหนียวเขี้ยวงูให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
    2. เทน้ำออก นำข้าวเหนียวไปนึ่งจนสุก
    3. ในระหว่างที่นึ่งข้าวเหนียว ให้นำกะทิ เกลือ น้ำตาลทราย ใบเตย ใส่หม้อตั้งไฟอ่อน คนจนน้ำตาลละลาย
    4. เมื่อข้าวเหนียวสุก ตักใส่หม้อกะทิ คนให้เข้ากัน ปิดไฟ พักไว้ 10 นาที

    **เตรียมมะม่วง:**
    - ปอกเปลือกมะม่วง หั่นเป็นชิ้นพอดีคำ

    **ทำน้ำกะทิราด:**
    - ให้นำกะทิ เกลือ น้ำตาลทราย ใบเตย ใส่หม้อตั้งไฟอ่อน คนจนน้ำตาลละลาย ปิดไฟ

    **จัดเสิร์ฟ:**
    - ตักข้าวเหนียวมูนใส่จาน วางมะม่วงสุก ราดด้วยน้ำกะทิ ทานคู่กับแตงโม หรือทานเปล่าก็อร่อย
    """
)

st.title("เคล็ดลับ")

st.markdown(
    """
    - เลือกใช้ข้าวเหนียวเขี้ยวงู จะทำให้เนื้อข้าวเหนียวมีกลิ่นหอมและมีความเหนียวนุ่ม
    - กะทิควรใช้กะทิสด จะทำให้ขนมมีรสชาติหอมมันอร่อย
    - น้ำตาลทรายและน้ำตาลปี๊บสามารถปรับเพิ่มหรือลดได้ตามชอบ
    - ใบเตยสามารถใส่หรือไม่ใส่ก็ได้
    """
)

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
