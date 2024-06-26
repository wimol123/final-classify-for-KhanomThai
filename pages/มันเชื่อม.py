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
kanom_img_path = os.getenv("COMPONENT_175_PATH1")
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
st.title("มันเชื่อม: เอกลักษณ์ไทยแท้ หวานละมุน กลมกล่อม")
st.image(kanom_img_path)
st.markdown(
    """
    ขนมมันเชื่อม เป็นขนมไทยโบราณที่มีมานาน นิยมทำกันในงานมงคลต่างๆ เชื่อกันว่ามันสำปะหลังเป็นพืชที่มีความเย็น ช่วยคลายร้อน ขนมมันเชื่อมจึงเป็นตัวแทนของความหวานเย็น
    มันสำปะหลังมีวิตามินซีสูง ช่วยเสริมสร้างภูมิคุ้มกัน ใยอาหารในมันสำปะหลังช่วยระบบขับถ่าย
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วิธีทำ:**

        **วัตถุดิบ:**
        - มันสำปะหลัง 1 กิโลกรัม
        - น้ำตาลทราย 500 กรัม
        - น้ำเปล่า 1 ลิตร
        - ใบเตย 2-3 ใบ
        - เกลือ 1/4 ช้อนชา

        **ขั้นตอนการทำ:**
        1. เตรียมมันสำปะหลัง: ปอกเปลือกมันสำปะหลัง ล้างให้สะอาด หั่นมันสำปะหลังเป็นชิ้นตามต้องการ
        2. ต้มมันสำปะหลัง: ตั้งหม้อใส่น้ำเปล่า ใบเตย ต้มจนเดือด ใส่ชิ้นมันสำปะหลังลงไปต้มจนสุก
        3. เตรียมน้ำเชื่อม: ตั้งกระทะใส่น้ำตาลทราย เกลือ เคี่ยวด้วยไฟอ่อนจนน้ำตาลละลาย และเหนียวข้น
        4. เชื่อมมัน: ใส่ชิ้นมันสำปะหลังที่ต้มสุกแล้วลงไปคลุกเคล้ากับน้ำเชื่อม จนทั่วดี
        5. พักและเสิร์ฟ: ตักมันเชื่อมใส่ถ้วย ราดด้วยน้ำเชื่อม เสิร์ฟเย็นๆ
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกมันสำปะหลังแก่จัด เนื้อแน่น จะได้ขนมมันเชื่อมที่มีรสชาติอร่อย
        - หั่นมันสำปะหลังให้มีความหนาเท่ากัน จะได้สุกพร้อมกัน
        - ต้มมันสำปะหลังด้วยไฟปานกลาง จะได้เนื้อขนมที่ใสและนิ่ม
        - แช่ชิ้นมันสำปะหลังในน้ำเกลือ 10 นาที ก่อนนำไปต้ม จะช่วยให้มันกรอบ
        - โรยเกลือเล็กน้อยบนขนมมันเชื่อม จะช่วยตัดรสหวาน
        """
    )

st.title("คุณค่าทางโภชนาการ")
with st.expander("คุณค่าทางโภชนาการ"):
    st.markdown(
        """
        - มันสำปะหลังมีวิตามินซีสูง ช่วยเสริมสร้างภูมิคุ้มกัน
        - ใยอาหารในมันสำปะหลังช่วยระบบขับถ่าย
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
