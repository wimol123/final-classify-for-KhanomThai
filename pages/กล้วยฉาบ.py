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
kanom_img_path = os.getenv("COMPONENT_KluaiChap_PATH1")
component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("กล้วยฉาบ")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
กล้วยฉาบ เป็นการนำผลไม้มาทำการแปรรูปให้มีมูลค่าเพิ่มขึ้น เช่น การนำกล้วยน้ำว้านำมาแปรรูปเป็นขนมที่ขึ้นชื่อของหมู่บ้านคลองสี่เสียด 
และได้มีการจำหน่ายไปตามจังหวัดต่างๆ รวมถึงการสั่งซื้อจากต่างประเทศ จนกระทั้งได้มีการจัดตั้งกลุ่มผู้ผลิตชื่อกลุ่มสตรีบ้านคลองสี่เสียด 
ซึ่งถือเป็นสินค้าotopอันดับต้นๆของจังหวัดนครนายก เป็นที่รู้จักกันในชื่อ กล้วยทอด “ผู้ใหญ่หนู”

เริ่มจากการที่สมาชิกในกลุ่มปลูกกล้วยกันทุกบ้าน ผลผลิตกล้วยที่ได้เมื่อนำไปขายก็ไม่ได้เงินมากนัก จึงได้ทดลองนำกล้วย ที่หาได้ในหมู่บ้านมาลองทำกล้วยทอด หรือ ที่เรียกกันว่ากล้วยฉาบขาย เริ่มจากการทำขายเล็กๆ น้อยๆ ส่งขายตามร้านขายของฝากในจังหวัดนครนายก ต่อมาได้มีการทดลองนำวัตถุดิบตัวอื่นๆ ที่สามารถหาได้ในหมู่บ้านใกล้เคียงในจังหวัดนครนายก อย่าง เผือก และมันมาทดลองทอดดูบ้างในลักษณะเช่นเดียวกับกล้วย 
ปรากฎว่าเมื่อนำออกขายผลตอบรับออกมาดีจึงได้ทำเผือก และมันทอดขายร่วมกับกล้วยทอดมาตลอด
       
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=component_1_path)

with col2:
    st.header("วิธีทำ")
    st.image(image=component_2_path)

st.page_link("Home.py", label="Home", icon="↩️")
