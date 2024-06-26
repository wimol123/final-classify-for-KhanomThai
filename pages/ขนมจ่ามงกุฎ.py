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
kanom_img_path = os.getenv("COMPONENT_75_PATH1")
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
st.title("ขนมจ่ามงกุฏ")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
เป็นชื่อขนมไทยชนิดหนึ่ง มีลักษณะคล้ายกะละแมสีขาว ไม่ใส่สี 
ทำจากแป้งข้าวเจ้าหรือแป้งข้าวเหนียวนวดผสมกับแป้งถั่วเขียว 
นำไปกวนกับกะทิและน้ำตาลทรายขาวจนเหนียว 
โรยเมล็ดถั่วลิสงคั่วซอยหรือเมล็ดแตงโมกะเทาะเปลือกเป็นไส้ในตัวขนม 
(สูตรโบราณจะโรยแป้งทอดตัดเป็นชิ้นเล็ก ๆ เท่าเมล็ดข้าวสุก 
ซึ่งใช้เวลาทำนานกว่า) จากนั้นตัดขนมเป็นก้อนพอคำ 
ห่อด้วยตองกล้วยเพสลาด ที่นาบไว้แล้ว

จ่ามงกุฎเป็นขนมชนิดหนึ่งที่ได้รับการกล่าวถึงในกาพย์เห่เรือชมเครื่องคาวหวาน
และงานนักขัตฤกษ์ซึ่งเป็นพระราชนิพนธ์ในพระบาทสมเด็จพระพุทธเลิศหล้านภาลัย 
โดยเป็นตำรับดั้งเดิมในสมเด็จพระศรีสุริเยนทราบรมราชินี
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    แป้งข้าวเหนียว 100 กรัม

    หัวกะทิ 300 กรัม

    น้ำตาลทราย 300 กรัม

    เมล็ดแตงโมคั่ว

    ใบตองกล้วยตานีสำหรับห่อ

    เทียนอบขนม
    
    ไม้กลัด
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. นำใบตองกล้วยตานีไปตากแดดสองแดดให้แห้ง แล้วนำมารีดด้วยเตารีดให้เรียบเงาและมีกลิ่นหอม นำมาตัดให้ได้ขนาดที่ต้องการห่อเนื้อขนม
    2. นำแป้งข้าวเหนียวมาอบควันเทียนทิ้งไว้หนึ่งคืน
    3. นำแป้งข้าวเหนียวที่อบควันเทียนแล้วมาผสมกับกะทิแล้วนำไปกรองด้วยผ้าขาวบางใส่ลงในกระทะสำหรับกวน ใส่น้ำตาลทรายลงไปผสมแล้วกวนด้วยการใช้ไฟกลางๆค่อนไปทางอ่อน กวนผสมจนส่วนผสมสุกใสข้นไม่ติดกระทะ พักขนมจนอุ่น
    4. นำขนมที่ได้มาห่อด้วยใบตองที่เตรียมไว้โรยหน้าด้วยเมล็ดแตงโมคั่ว กลัดด้วยไม้กลัดแล้วนำไปตากแดดอีกหนึ่งแดดก็นำมากินได้แล้ว
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
