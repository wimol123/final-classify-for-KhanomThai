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
kanom_img_path = os.getenv("COMPONENT_17_PATH1")
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
st.title("ขนมกวนขาว")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
เป็นขนมพื้นเมืองดั้งเดิมของชาวนครศรีธรรมราช คล้ายขนมเปียกปูนขาว นวดแป้งให้เข้ากับน้ำปูนใสแล้วนำไปเคี่ยวกับกะทิขนข้นเหนียว 
ราดหน้าด้วยกะทิเคี่ยวกับน้ำตาลและเกลือ แล้วโรยหน้าด้วยถั่วทองคั่ว

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    แป้งข้าวเจ้า 1/2 ถ้วยตวง

    น้ำปูนใส 3/4 ถ้วยตวง

    น้ำกะทิ  1  ถ้วยตวง

    เกลือป่น  นิดหน่อย

    น้ำตาลทราย  ปริมาณตามชอบ

    ถั่วเขียวเลาะเปลือกคั่วสุก   ปริมาณตามชอบ

    น้ำกะทิ  1 ถ้วยตวง
       
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """

    1. นำแป้งข้าวจ้าผสมผสมกับหางกะทิและน้ำปูนใสคนให้เข้ากัน นำกระทะทองเหลืองตั้งไฟอ่อน นำแป้งที่ผสมแล้วเทลงกระทะกวนไปทางเดียวกันให้ทั่วระวังอย่าให้แป้งจับกันเป็นลูก กวนจนเหนียวให้ได้ที่ สังเกตดูจะเห็นเนื้อขนมไม่ติดกระทะ เนื้อขนมสีขาวนวล ตักใส่ถาด เกลี่ยให้เรียบเสมอหน้า วางทิ้งไว้ให้เย็น เวลาจะรับประทานจึงตัดเป็นชิ้น ๆ
    
    2. นำกะทิใส่เกลือตั้งไฟอ่อน ๆ คนเรื่อย ๆ ร้อนจึงยกลง ให้คนต่อไปจนความร้อนลดลง เพราะถ้าไม่คนจะทำให้กะทิแตกมันได้ กะทิไม่ต้องข้นและมันจนเกินไป เพราะจะทำให้เลี่ยนมากไป
    
    3. ถั่วเขียวเอาเปลือกออก คั่วจนเหลือกรอบ ใส่ภาชนะปิดไว้
    
    4. ผสมขนมตักเนื้อขนมกวนขาวที่ตัดเป็นชิ้น ๆ แล้วใส่ถ้วย ตักกะทิราดขนมใส่น้ำตาลทรายทั้งเม็ด รสหวาน ตาม โรยถั่วเขียวที่คั่วไว้แล้ว
        
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
