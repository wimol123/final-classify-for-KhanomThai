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
kanom_img_path = os.getenv("COMPONENT_88_PATH1")
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
st.title("ขนมแชงม้า, ปลากริมไข่เต่า")

left_co, cent_co, last_co = st.columns(3)
st.title("ขนมแชงม้า: เอกลักษณ์ขนมไทยโบราณ")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมแชงม้า (หรือสะกดด้วย ซ เป็น แซงม้า) หรือ ขนมแซงมา เป็นขนมไทยโบราณที่มีเอกลักษณ์โดดเด่นด้วยรสชาติหวานมัน กลมกล่อม ผสมผสานความนุ่มหนึบของตัวแป้ง และความหอมมันของกะทิ ยังไม่มีหลักฐานแน่ชัดว่า ขนมแชงม้ามีต้นกำเนิดมาจากไหน แต่มีการสันนิษฐานว่า ขนมชนิดนี้อาจจะเป็นขนมที่ผสมผสานระหว่าง "ขนมปลากริม" และ "ขนมไข่เต่า" เข้าด้วยกัน ในอดีตนิยมทำขนมแชงม้าเพื่อเป็นของว่างในงานมงคลต่างๆ ปัจจุบัน ขนมแชงม้าหาทานได้ยากขึ้น แต่ยังมีบางร้านที่ยังคงทำขนมชนิดนี้ขายอยู่
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • แป้งข้าวเจ้า 1 ถ้วยตวง  
    • แป้งมัน 1/2 ถ้วยตวง  
    • แป้งข้าวเหนียว 1/4 ถ้วยตวง  
    • เกลือ 1/4 ช้อนชา  
    • น้ำเปล่า 1 ถ้วยตวง  
    • น้ำตาลปี๊บ 1 ถ้วยตวง  
    • กะทิ 2 ถ้วยตวง  
    • ใบเตย 2-3 ใบ  
    • เกลือ 1/4 ช้อนชา  

    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ผสมแป้งข้าวเจ้า แป้งมัน แป้งข้าวเหนียว เกลือ และน้ำเปล่า คนให้เข้ากันจนแป้งเนียน
    2. นำแป้งที่ผสมไว้มาปั้นเป็นรูปปลาและรูปไข่เต่า
    3. ต้มน้ำให้เดือด นำแป้งที่ปั้นไว้ลงต้มจนสุก
    4. ละลายน้ำตาลปี๊บกับน้ำเปล่า ใส่ใบเตย และเกลือ ลงในหม้อ
    5. เทกะทิลงในหม้อ คนให้เข้ากัน
    6. ใส่แป้งที่ต้มสุกแล้วลงในหม้อ เคี่ยวต่อจนแป้งสุกและข้น
    7. ตักใส่ถาด ตัดเป็นชิ้นพอดีคำ โรยหน้าด้วยมะพร้าวขูด
    
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
