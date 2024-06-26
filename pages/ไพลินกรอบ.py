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
kanom_img_path = os.getenv("COMPONENT_165_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมไพลินกรอบ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมไพลินกรอบ เป็นขนมไทยโบราณที่มีมาช้านาน เชื่อกันว่ามีต้นกำเนิดมาจากในวัง คำว่า "ไพลิน" นั้นหมายถึง อัญมณีสีน้ำเงินเข้ม ขนมชนิดนี้จึงได้ชื่อมาจากสีสันของดอกอัญชันที่นำมาใช้ทำเป็นไส้ขนม
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วิธีทำ:**

        1. **เตรียมไส้ไพลิน:**
           - นำดอกอัญชันมาต้มน้ำจนได้น้ำสีน้ำเงินเข้ม
           - ใส่แป้งมันสำปะหลัง, น้ำตาลทราย, เกลือ, และใบเตยลงในน้ำอัญชัน คนจนส่วนผสมละลายเข้ากันดี
           - นำส่วนผสมไปตั้งไฟอ่อน คนเรื่อยๆ จนข้นเหนียว
           - เทส่วนผสมที่ข้นเหนียวลงพิมพ์ พักไว้ให้เย็นและแข็งตัว

        2. **เตรียมตัวไพลิน:**
           - ปอกแห้ว, หั่นเป็นชิ้นลูกเต๋า แช่น้ำเกลือเพื่อป้องกันไม่ให้แห้วดำ
           - ล้างแห้วให้สะอาดและพักไว้
           - นำแห้วไปคลุกกับแป้งมันสำปะหลัง
           - ต้มน้ำให้เดือด นำแห้วที่คลุกแป้งแล้วลงไปต้มจนลอยขึ้น
           - ตักแห้วขึ้นสะเด็ดน้ำ

        3. **ประกอบขนม:**
           - นำไส้ไพลินที่เย็นและแข็งตัวแล้ว ตัดเป็นชิ้นพอดีคำ
           - นำไส้ไพลินมาวางบนตัวไพลิน
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **สำหรับไส้ไพลิน:**
        - ดอกอัญชัน 10 ดอก
        - แป้งมันสำปะหลัง 1/2 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - ใบเตย 2 ใบ

        **สำหรับตัวไพลิน:**
        - แห้ว 500 กรัม
        - แป้งมันสำปะหลัง 1 ถ้วยตวง
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณของส่วนผสมได้ตามชอบ
        - สามารถเพิ่มรสชาติให้กับไส้ไพลินได้ด้วยการใส่กลิ่นมะลิ หรือ pandan leaves
        - ตัวไพลินสามารถเปลี่ยนจากแห้วเป็นมันแกว หรือเผือกได้
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
