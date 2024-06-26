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
kanom_img_path = os.getenv("COMPONENT_KluaiThap_PATH1")
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
st.title("กล้วยทับ")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
กล้วยทับ ขนมไทยโบราณที่หลายคนคุ้นเคย ลักษณะคล้ายกล้วยปิ้ง แต่เนื้อนุ่มกว่า โดยทั่วไปมีลักษณะเป็นชิ้นหนาๆ 
นำมาปิ้งบนเตาถ่าน ราดด้วยกะทิ น้ำตาลทราย และเกลือ นิยมรับประทานกันทั้งเด็กและผู้ใหญ่


ประวัติความเป็นมา
ข้อมูลแน่ชัดเกี่ยวกับประวัติความเป็นมาของกล้วยทับนั้นยังไม่ปรากฏชัด แต่สันนิษฐานว่าน่าจะมีมานานแล้ว
พบหลักฐานการทำกล้วยทับในตำราอาหารไทยโบราณหลายเล่ม เช่น ตำราแม่ครัวหลวง และตำราอาหารวัดสุวรรณาราม
ในอดีตกล้วยทับเป็นอาหารว่างที่นิยมทำรับประทานกันในครัวเรือน มักทำเพื่อเป็นของว่าง หรือทานคู่กับน้ำชา กาแฟ
ปัจจุบันกล้วยทับหาซื้อทานได้ทั่วไป มีทั้งแบบดั้งเดิมและแบบประยุกต์
       
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
        กล้วยน้ำว้าห่าม 2 หวี

        หัวกะทิ 1 ½ ถ้วยตวง

        น้ำตาลปี๊บ 200 กรัม

        น้ำตาลทรายขาว 100 กรัม

        เกลือป่น ½ ช้อนชา

        เนยจืด 1 ช้อนโต๊ะ

        ใบเตยมัด 3 ใบ

        เนื้อมะพร้าว(ซอยเส้น) 1 ถ้วยตวง
"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
        1. ตั้งหม้อใส่น้ำตาลปี๊บ น้ำตาลทราย เกลือ กะทิ และใบเตย จากนั้นเปิดไฟกลาง เคี่ยวจนน้ำตาลละลาย

        2. เมื่อละลายและเดือดให้หรี่เป็นไฟอ่อน จากนั้นเคี่ยวต่อประมาณ 15 – 20 นาที (เคี่ยวจนข้นเล็กน้อย) ตักใบเตยออกแล้วใส่เนยลงไปคนให้ละลายเข้ากัน จากนั้นพักให้เย็น

        3. ทำกล้วยมาปอกเปลือก ตัดส่วนหัวและท้ายออกจากนั้นหั่นเป็นท่อน ท่อนประมาณ 1.5 เซน

        4. เรียงใส่หม้อทอดไร้น้ำมัน อบที่ไฟ 180 องศา 15 – 20 นาที (อบ 10 นาทีแล้วกลับอีกด้านขึ้น แล้วอบต่ออีก 5 - 10 นาที)

        5. นำกล้วยมากดให้แบน (ให้กดตอนที่กล้วยยังร้อนอยู่เพื่อความกดง่าย)

        6. เรียงใส่จานราดน้ำกะทิ แล้วโรยหน้าด้วยมะพร้าว พร้อมรับประทาน
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
