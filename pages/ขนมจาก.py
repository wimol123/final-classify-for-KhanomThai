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
kanom_img_path = os.getenv("COMPONENT_74_PATH1")
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
st.title("ขนมจาก")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
ที่มาของชื่อ ขนมจาก มาจาก ใบจาก ซึ่งเป็นใบไม้ที่เอาไว้ห่อแป้งขนมนั่นเอง 
โดย ต้นจาก ถือเป็นพืชท้องถิ่น ที่เติบโตได้ดีในป่าชายเลน 
ด้วยสภาพทางภูมิศาสตร์ ทำให้จังหวัดในปากแม่น้ำเจ้าพระยา 
ซึ่งติดกับป่าชายเลน เช่น สมุทรปราการ สมุทรสาคร สมุทรสงคราม 
นิยมนำ ใบจาก มาห่อขนม จนกลายเป็นขนมชื่อดังประจำจังหวัด 
ซึ่งปัจจัยสำคัญ ที่นิยมนำเอามาห่อขนมนั้นก็คือ เมื่อนำมาเผาด้วยไฟอ่อน ๆ 
แล้วจะส่งกลิ่นหอม นอกจากนี้ ก็ยังแข็ง ทนทาน ไม่แตกหักง่ายอีกด้วย

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    สูตรขนมจากแป้งข้าวเหนียวดำ  
    • ใบจาก ตัดเป็นท่อน ๆ ยาว 1 ฟุต  
    • แป้งข้าวเหนียวดำ 240 กรัม  
    • แป้งมัน 80 กรัม  
    • มะพร้าวอ่อนผสมมะพร้าวทึนทึกขูด 1 ถ้วย  
    • น้ำตาลปี๊บ 1/2 ถ้วย  
    • น้ำตาลทราย 2 ช้อนโต๊ะ  
    • เกลือป่น 2 ช้อนชา  
    • น้ำมะพร้าวอ่อน 1/2 – 1/3 ถ้วย (ไม่ต้องใส่หมด)  
    • ไม้กลัดก้านมะพร้าว (กลัดใบจาก)  
    • น้ำมันมะพร้าว (สำหรับเช็ดใบจาก)  
    
"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ขูดเนื้อมะพร้าวอ่อน และ มะพร้าวทึนทึกออกมา จนได้ 1 ถ้วย
    2. เตรียมชามผสม ใส่แป้งข้าวเหนียวดำ แป้งมัน คนให้เข้ากัน
    3. จากนั้น ใส่เนื้อมะพร้าวอ่อนผสมมะพร้าวขูดทึนทึก ลงไป คลุกเคล้าให้เข้ากัน
    4. ใส่น้ำตาลปี๊บ น้ำตาลทราย เกลือป่น นวดให้น้ำตาลปี๊บ น้ำตาลทรายละลายดี
    5. พอทุกอย่างเข้ากันดีแล้ว ให้ค่อย ๆ เติมน้ำมะพร้าวอ่อนลงไป แล้วนวดให้แป้งมีความข้นเหนียว
    6. ตัดใบจากเป็นท่อน ๆ ยาวท่อนละ 1 ฟุต จากนั้น นำใบจาก 2 แผ่น มาวางทับให้เสมอกัน แล้วใช้ไม้กลัดก้านมะพร้าวกลัดไว้ตรงกลาง
    7. ใช้พู่กัน หรือ กระดาษ จุ่มน้ำมันมะพร้าว เช็ดใบจาก เพื่อกำจัดสิ่งสกปรก และ เพิ่มกลิ่นหอม
    8. ตักแป้งขนมใส่ใบจาก ห่อให้เรียบร้อย แล้วใช้ไม้กลัดก้านมะพร้าว กลัดใบจาก หัว กลาง ท้าย ให้แน่น (ใครไม่สะดวก ใช้แม็กเย็บแทนก็ได้)
    9. นำไปย่างบนเตาถ่านให้สุก ใช้เวลา 3 – 5 นาที ถ้าแป้งแข็งตัวขึ้น และ มีกลิ่นหอม แสดงว่า แป้งสุกแล้ว ให้ยกลง เป็นอันเสร็จ (ถ้าไม่มีเตาถ่าน ให้วางตะแกรงลงบนเตาแก็ส แล้วเปิดไฟอ่อน ปิ้งขนมจากแทนก็ได้)

    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
