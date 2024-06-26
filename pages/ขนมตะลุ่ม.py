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
kanom_img_path = os.getenv("COMPONENT_98_PATH1")
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
st.title("ขนมตะลุ่ม หรือขนมถ้วยสังขยา")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมตะลุ่มคือ ขนมพื้นบ้านทางภาคกลางของไทยที่มีมาตั้งแต่สมัยโบราณ ซึ่งจะประกอบด้วยตัวขนมและหน้าสังขยา ลักษณะคล้ายขนมถ้วย รสชาติจะออกหวานมัน โดยมีวัตถุดิบหลักอย่างแป้งชนิดต่าง ๆ กะทิและไข่เป็ด ถือเป็นหนึ่งใน ขนมไทยโบราณ ที่หาทานได้ค่อนข้างยาก จะมีเพียงบางพื้นที่เท่านั้นที่ทำขาย ถึงแม้ว่าวิธีการทำจะไม่ยากเท่าไหร่ก็ตาม แต่ด้วยปัจจัยหลายอย่างจึงทำให้ขนมชนิดนี้เริ่มถูกลืม ดังนั้นเราจึงอยากให้คนไทยช่วยกันอนุรักษ์ ขนม ตะลุ่ม ไว้ให้อยู่นาน ๆ
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    แป้งข้าวเจ้า 140 กรัม  
    แป้งมันสำปะหลัง 15 กรัม  
    แป้งเท้ายายม่อม 15 กรัม  
    เกลือ 1/2 ช้อนชา  
    หางกะทิ 170 มิลลิลิตร  
    น้ำปูนใส 15 มิลลิลิตร  
    น้ำลอยดอกมะลิ 335 มิลลิลิตร  
      
    หน้าสังขยา  
    ไข่เป็ด 3 ฟอง  
    น้ำตาลปี๊บ 180 กรัม  
    หัวกะทิ 130 มิลลิลิตร  
    ใบเตยหั่นท่อน 2 ใบ  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. เริ่มต้นด้วยการทำตัวขนม เตรียมภาชนะผสม ใส่แป้งข้าวเจ้าลงไป ตามด้วยแป้งมันสำปะหลัง แป้งเท้ายายม่อม เกลือและหางกะทิ นวดจนเนียนแล้วใส่น้ำปูนใสลงไป จากนั้นนวดต่ออีก 15 นาที  
    2. ใส่น้ำลอยดอกมะลิลงไป คนให้เข้ากันแล้วนำไปกรองใส่ถ้วย พักไว้ อุ่นถ้วยตะไลไว้เป็นเวลา 5 นาที หลังจากนั้นเปิดฝาออกแล้วตักส่วนผสมของตัวขนมที่ทำไว้ลงในถ้วยตะไลจนครบ เสร็จแล้วปิดฝานึ่งไว้ 3 นาที  
    3. ขั้นตอนต่อมาเตรียมทำหน้าสังขยา เริ่มจากตอกไข่เป็ดลงในภาชนะ ใส่น้ำตาลปี๊บและใบเตยลงไป จากนั้นใช้มือขยำให้ละเอียดเข้ากัน เสร็จแล้วใส่หัวกะทิลงไป ใช้มือขยำอีกครั้งและนำไปกรองให้ได้ส่วนผสมที่เนียนละเอียด  
    4. เมื่อนึ่งตัวขนมจนครบ 3 นาทีแล้ว ตักส่วนผสมหน้าสังขยาใส่ลงไปบนตัวขนมให้ครบทุกถ้วย หลังจากนั้นนึ่งต่ออีก 10 นาที เพียงเท่านี้ก็ถือเป็นอันเสร็จ  
        
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
