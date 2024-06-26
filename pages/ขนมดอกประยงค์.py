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
kanom_img_path = os.getenv("COMPONENT_92_PATH1")
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
st.title("ขนมดอกประยงค์, ขนมไข่แมงดา, ขนมทองหยอดจิ๋ว")

left_co, cent_co, last_co = st.columns(3)
st.title("ขนมไข่แมงดา: ของหวานโบราณ หายาก น่าค้นหา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมไข่แมงดา เป็นขนมไทยโบราณชนิดหนึ่งที่มีลักษณะคล้ายไข่แมงดาตัวเมีย ลอยตัวอยู่ในน้ำเชื่อมสีเหลืองใส รสชาติหวานละมุน หอมกลิ่นใบเตย หาทานได้ยากในปัจจุบัน  
  
ประวัติของขนมไข่แมงดายังไม่แน่ชัด มีการสันนิษฐานว่าขนมชนิดนี้ได้รับอิทธิพลมาจากขนมทองหยอด ซึ่งเป็นขนมไทยโบราณอีกชนิดหนึ่ง  บ้างก็ว่าขนมไข่แมงดานั้นทำเลียนแบบมาจากไข่แมงดาตัวเมีย นำมาทำเป็นอาหารทานเล่น  
  
หลักฐานทางประวัติศาสตร์ที่ชัดเจนที่สุดคือ ขนมไข่แมงดาปรากฏใน "ตำราอาหารคาวหวาน" ฉบับพิมพ์ครั้งแรกในสมัยกรุงรัตนโกสินทร์ตอนต้น แสดงว่าเป็นขนมที่มีมานานพอสมควร  
  
ในบทละครเรื่องสังข์ทองยังมีการกล่าวถึงขนมไข่แมงดา แสดงว่าขนมชนิดนี้เป็นที่รู้จักในหมู่คนทั่วไปในสมัยนั้น  
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • น้ำตาลทรายขาว 500  กรัม  
    • น้ำสะอาด 500  กรัม  
    • ใบเตยหอม 5  ใบ  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    - ผสมน้ำตาลกับน้ำ คนให้น้ำตาลละลาย   
    - นำไปตั้งไฟให้เดือดแล้วใส่ใบเตยหอมลง แล้วเคี่ยวน้ำเชื่อมต่อสักครู่ ปิดไฟ  กรองด้วยผ้าขาว พักไว้ให้เย็น
    หมายเหตุ: เตรียมไว้สำหรับแช่ขนม
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
