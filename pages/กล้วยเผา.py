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
kanom_img_path = os.getenv("COMPONENT_KluaiPao_PATH1")
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
st.title("กล้วยเผา")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
กล้วยเผา: ของกินยามเจ็บไข้แต่โบราณที่พระพุทธเจ้าหลวง-เจ้านายยังเสวย

กล้วยเผา อาหารง่ายๆ ที่ดูเหมือนจะธรรมดา แต่แฝงไว้ด้วยเรื่องราวและความหมายทางวัฒนธรรมมานานหลายยุคสมัย

ประวัติความเป็นมา:

กล้วยเผา นิยมรับประทานกันมานานแล้ว โดยเฉพาะในยามเจ็บป่วย เพราะมีคุณสมบัติในการช่วยย่อยอาหาร แก้ท้องเสีย และบำรุงร่างกาย
จากหลักฐานทางโบราณคดี พบภาพวาดเกี่ยวกับการเก็บเกี่ยวและบริโภคกล้วยบนผนังถ้ำโบราณในหลายแห่งของประเทศไทย
ในสมัยรัตนโกสินทร์ กล้วยเผาเป็นที่นิยมในหมู่พระภิกษุสามเณร และเหล่าเจ้านาย
มีบันทึกไว้ว่า พระบาทสมเด็จพระจุลจอมเกล้าเจ้าอยู่หัว รัชกาลที่ 5 โปรดเสวยกล้วยเผาเป็นประจำ และยังทรงมีพระราชดำริให้ปลูกต้นกล้วยไว้ในพระราชวัง
กล้วยเผายังปรากฏในวรรณคดีไทยหลายเรื่อง เช่น เรื่อง "พระอภัยมณี" ของสุนทรภู่ 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
        กล้วยหักมุกสุกงอม
"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
        1. ตัดแยกกล้วยเป็นลูก ๆ เอาไปล้างให้สะอาดและเช็ดให้แห้ง
     	
        2. ทำด้วยเตาถ่านหรือเตาแก๊สให้ใช้ไฟอ่อน เอากล้วยลงไปปิ้งบนตะแกรงหรือกระทะ ประมาณ 20 นาที หรือจนกว่าเปลือกสีดำและพองเกือบปริ ใช้มีดกรีดเปลือกตรงกลางออก ปิ้งต่ออีกสักพัก ประมาณ 10 นาที หรือจนกล้วยสีเหลืองและกลิ่นหอม
     	
        3. ทำด้วยหม้ออบลมร้อนโดยใช้ไฟ 200 องศาเซลเซียส ประมาณ 15 นาที พอครบเวลาเอาออกมาพลิกกลับด้าน และเอาไปอบต่ออีก 5 นาที หรือจนเปลือกกล้วยดำและพอกเกือบปริ นำออกมากรีดเปลือก เอาไปอบต่อ 10 นาที
     	
        4. ทำด้วยไมโครเวฟใช้ไฟ 800 วัตต์ เอาเข้าไปอบประมาณ 5 นาที เอาออกมากรีดเปลือกออก แล้วเข้าไปอบต่ออีก 1 นาทีหรือจนสุกเหลืองกลิ่นหอม
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
