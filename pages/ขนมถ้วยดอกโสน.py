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
kanom_img_path = os.getenv("COMPONENT_134_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมถ้วยดอกโสน: ขนมไทยโบราณ หอมกรุ่น กินเพลิน",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมถ้วยดอกโสน")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมถ้วยดอกโสน เป็นขนมไทยโบราณอีกชนิดหนึ่งที่หาทานได้ยาก มีเอกลักษณ์เฉพาะตัวที่ไม่เหมือนใคร ทั้งความหอมกรุ่นของดอกโสน รสชาติหวานมัน กลมกล่อม เนื้อสัมผัสที่นุ่มละมุน ทานคู่กับกะทิหอมๆ ช่างเป็นของหวานที่ลงตัวสุดๆ
        ในอดีต ดอกโสนเป็นพืชผักพื้นบ้านที่หาได้ง่าย นิยมนำมาประกอบอาหารคาวหวาน ขนมถ้วยดอกโสนจึงเป็นอีกหนึ่งภูมิปัญญาไทยที่ดัดแปลงดอกโสนมาเป็นวัตถุดิบหลัก
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมดอกโสน: เด็ดดอกโสนสด ล้างน้ำให้สะอาด พักไว้ให้สะเด็ดน้ำ
        2. เตรียมแป้ง: ผสมแป้งข้าวเจ้า แป้งมัน แป้งท้าวยายม่อม เกลือ น้ำตาลปี๊บ และน้ำใบเตย คนจนเข้ากัน พักไว้
        3. คลุกแป้งกับดอกโสน: ใส่ดอกโสนลงในแป้ง คลุกเคล้าให้ดอกโสนเคลือบแป้งทั่วดี
        4. เทใส่พิมพ์: ตักส่วนผสมใส่พิมพ์ขนมถ้วย
        5. นึ่งขนม: นำไปนึ่งด้วยไฟปานกลางประมาณ 10-15 นาที หรือจนขนมสุก
        6. เตรียมหน้ากะทิ: ผสมแป้งข้าวเจ้า น้ำตาลทราย เกลือ และหัวกะทิ คนจนเข้ากัน
        7. ราดหน้ากะทิ: นำหน้ากะทิมาเทราดบนขนมถ้วยดอกโสนที่นึ่งสุกแล้ว
        8. นึ่งต่อ: นำไปนึ่งต่อด้วยไฟแรงประมาณ 5 นาที หรือจนหน้ากะทิแตกมัน
        9. พักและเสิร์ฟ: รอให้ขนมถ้วยดอกโสนเย็นลง ทานคู่กับชา กาแฟ หรือน้ำอัญชัน
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ตัวขนมถ้วย:**
        - ดอกโสนสด 1 ถ้วย
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - แป้งมัน 1/2 ถ้วยตวง
        - แป้งท้าวยายม่อม 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - น้ำตาลปี๊บ 1 ถ้วยตวง
        - น้ำใบเตย 1 ถ้วยตวง
        
        **หน้ากะทิ:**
        - แป้งข้าวเจ้า 1/4 ถ้วยตวง
        - น้ำตาลทราย 1/4 ถ้วยตวง
        - เกลือ 1/8 ช้อนชา
        - หัวกะทิ 1 ถ้วยตวง
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
