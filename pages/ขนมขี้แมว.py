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
kanom_img_path = os.getenv("COMPONENT_55_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมขี้แมว หรือ หนุมานคลุกฝุ่น")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
ขนมขี้แมว หรือ หนุมานคลุกฝุ่น เป็นขนมไทยโบราณที่มีมายาวนาน แต่ไม่มีหลักฐานที่แน่ชัดว่ามีที่มาจากไหน  บ้างก็ว่าตั้งชื่อตามลักษณะของขนมที่คล้ายก้อนขี้แมว  บ้างก็ว่าตั้งชื่อตามลักษณะการทำที่ต้องคลุกแป้งกับมะพร้าวจนสีคล้ายฝุ่น

อย่างไรก็ตาม ขนมชนิดนี้พบได้ทั่วไปในหลายภาคของประเทศไทย  โดยแต่ละท้องถิ่นอาจมีสูตรและวิธีการทำที่แตกต่างกันเล็กน้อย  แต่ส่วนผสมหลักๆ จะประกอบไปด้วย ข้าวเหนียว มะพร้าว น้ำตาล เกลือ  นำมาคลุกเคล้ากันจนเข้ากัน  จากนั้นปั้นเป็นก้อนกลมๆ  แล้วคลุกกับมะพร้าวขูดอีกครั้ง

ขนมขี้แมว นิยมทำในงานมงคลต่างๆ เช่น งานแต่งงาน งานบวช  หรือทำเพื่อแจกในงานบุญ  เพราะเป็นขนมที่ทำง่าย  ใช้วัตถุดิบน้อย  และเก็บไว้ได้นาน ปัจจุบัน ขนมขี้แมวหาทานได้ยากขึ้น  เพราะคนทำกันน้อยลง  แต่ยังมีบางร้านที่ยังคงสืบทอดสูตรดั้งเดิมเอาไว้  หากมีโอกาสลองหาทานดู  รับรองว่าจะไม่ผิดหวัง


"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    แป้งข้าวเจ้า 2 ถ้วย

    น้ำกะทิ 4 ถ้วย

    น้ำตาลปี๊บ 1 ถ้วย

    เกลือ 1/2 ช้อนชา
    
    มะพร้าวขูด 2 ถ้วย
    
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ผสมแป้งข้าวเจ้า น้ำกะทิ น้ำตาลปี๊บ และเกลือเข้าด้วยกัน ตั้งไฟปานกลาง กวนจนส่วนผสมข้นเหนียวและเริ่มจับตัวเป็นก้อน
    2. ยกลงจากเตา พักไว้ให้เย็น
    3. ปั้นแป้งเป็นก้อนกลมๆ ขนาดพอดีคำ
    4. คลุกแป้งกับมะพร้าวขูดให้ทั่ว
    5. วางขนมขี้แมวเรียงใส่จาน พักไว้ให้สะเด็ดน้ำมัน
    6. ทานเล่นหรือเก็บไว้ทานได้นาน

    
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
