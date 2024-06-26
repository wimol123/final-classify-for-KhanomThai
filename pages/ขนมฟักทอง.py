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
kanom_img_path = os.getenv("COMPONENT_167_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title and sections
st.title("ขนมฟักทอง")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมฟักทอง หรือเข้าหนมบ่าฟักแก้ว เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในงานมงคลต่างๆ เชื่อกันว่าฟักทองเป็นพืชที่ให้ความเย็น ช่วยคลายร้อน ขนมฟักทองจึงเป็นตัวแทนของความหวานเย็น
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
           - นึ่งฟักทองจนสุก
           - บดฟักทองให้ละเอียด

        2. **ผสมแป้ง:**
           - ผสมแป้งข้าวเจ้า, แป้งมัน, เกลือ และน้ำตาลทราย
           - ใส่น้ำกะทิทีละน้อย นวดจนแป้งเนียน

        3. **ผสมฟักทองและแป้ง:**
           - ใส่ฟักทองบดลงในแป้ง
           - นวดจนส่วนผสมเข้ากันดี

        4. **ตักใส่พิมพ์:**
           - ตักส่วนผสมใส่พิมพ์ที่เตรียมไว้
           - โรยหน้าด้วยมะพร้าวขูด

        5. **นึ่ง:**
           - นึ่งขนมฟักทองด้วยไฟปานกลางประมาณ 20-30 นาที หรือจนขนมสุก
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ส่วนผสม:**
        - ฟักทองนึ่ง 500 กรัม
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - แป้งมัน 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - น้ำกะทิ 1 ถ้วยตวง
        - มะพร้าวขูด สำหรับโรยหน้า
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณของส่วนผสมได้ตามชอบ
        - สามารถเพิ่มรสชาติให้กับขนมฟักทองได้ด้วยการใส่ใบเตย หรือ pandan leaves
        - ควรเลือกใช้ฟักทองแก่จัด เนื้อจะได้ไม่เละ
        - นึ่งฟักทองด้วยไฟปานกลาง จะได้เนื้อขนมที่เนียน
        - นึ่งขนมด้วยไฟปานกลาง จะได้ขนมที่สุกทั่ว
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
