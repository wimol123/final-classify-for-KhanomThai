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
kanom_img_path = os.getenv("COMPONENT_169_PATH1")
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
st.title("ฟักทองเชื่อม")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ฟักทองเชื่อม เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในงานมงคลต่างๆ เชื่อกันว่าฟักทองเป็นพืชที่ให้ความเย็น ช่วยคลายร้อน ฟักทองเชื่อมจึงเป็นตัวแทนของความหวานเย็น
        ฟักทองมีวิตามินเอสูง ช่วยบำรุงสายตา ใยอาหารในฟักทองช่วยระบบขับถ่าย
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วิธีทำ:**

        1. **เตรียมฟักทอง:**
           - เลือกฟักทองแก่จัด ล้างเปลือกให้สะอาด
           - ปอกเปลือกและคว้านเมล็ดออก
           - หั่นฟักทองเป็นชิ้นตามต้องการ

        2. **แช่น้ำปูนใส:**
           - ผสมน้ำปูนใสกับน้ำเปล่า
           - แช่ฟักทองที่หั่นไว้ในน้ำปูนใสประมาณ 30 นาที
           - ล้างฟักทองด้วยน้ำสะอาด

        3. **เชื่อมฟักทอง:**
           - ตั้งหม้อใส่น้ำเปล่า, น้ำตาลทราย, และใบเตย
           - ต้มจนน้ำตาลละลายและเดือด
           - ใส่ฟักทองลงไปเชื่อม
           - เคี่ยวด้วยไฟอ่อนจนฟักทองใส

        4. **พักและเสิร์ฟ:**
           - ตักฟักทองเชื่อมใส่ถ้วย
           - ราดด้วยน้ำเชื่อม
           - โรยหน้าด้วยเกลือเล็กน้อย
           - เสิร์ฟเย็นๆ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ส่วนผสม:**
        - ฟักทอง 500 กรัม
        - น้ำตาลทราย 2 ถ้วยตวง
        - น้ำเปล่า 4 ถ้วยตวง
        - ใบเตย 2-3 ใบ
        - เกลือ 1/4 ช้อนชา
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณของส่วนผสมได้ตามชอบ
        - สามารถเพิ่มรสชาติให้กับขนมฟักทองเชื่อมได้ด้วยการใส่น้ำมะนาว หรือ pandan leaves
        - ควรเลือกใช้ฟักทองแก่จัด เนื้อจะได้ไม่เละ
        - เคี่ยวฟักทองด้วยไฟอ่อน จะได้เนื้อขนมที่ใสและนิ่ม
        - แช่ฟักทองในน้ำปูนใสก่อน จะช่วยให้ฟักทองกรอบ
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
