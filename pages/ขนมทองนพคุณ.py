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
kanom_img_path = os.getenv("COMPONENT_122_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองนพคุณ: ขนมมงคลสูตรโบราณ",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมทองนพคุณ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองนพคุณ เป็นขนมไทยโบราณ จัดอยู่ในกลุ่มขนมตระกูล "ทอง" นิยมทำขึ้นในงานมงคลต่างๆ ชื่อ "ทองนพคุณ" นั้น มีความหมายมงคล "ทอง" หมายถึง เงินทอง "นพ" หมายถึง เก้า "คุณ" หมายถึง คุณสมบัติที่ดี รวมความหมายว่า ขนมชนิดนี้ เปรียบเสมือนตัวแทนของเงินทอง เกียรติยศ ชื่อเสียง และคุณสมบัติที่ดีงาม เหมาะแก่การมอบเป็นของขวัญ ของฝาก หรือใช้ประกอบพิธีกรรมมงคลต่างๆ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมทองนพคุณ มีวิธีทำที่ค่อนข้างพิถีพิถัน:**

        1. **นำถั่วทองคั่วสุกมาบดจนเป็นเนื้อแป้งละเอียด**
        2. **ผสมแป้งถั่วทอง, ไข่แดง, น้ำตาลทราย, และเกลือ นวดจนแป้งเนียน**
        3. **นำแป้งมาตีด้วยมือจนขึ้นฟู พักแป้งไว้ประมาณ 30 นาที**
        4. **นำแป้งที่พักไว้มาปั้นเป็นรูปดอกไม้ หรือรูปทรงต่างๆ ตามต้องการ**
        5. **ทาไข่แดงบางๆ บนตัวขนม**
        6. **นำขนมไปอบในเตาอบที่อุณหภูมิ 180 องศาเซลเซียส ประมาณ 20 นาที หรือจนขนมสุกเหลือง**
        7. **นำขนมออกจากเตาอบ พักให้เย็นสนิท**
        8. **ตกแต่งขนมด้วยทองคำเปลว**
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - **ถั่วทองคั่วสุก** 2 ถ้วยตวง
        - **ไข่แดง** 2 ฟอง
        - **น้ำตาลทราย** 1 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา
        - **น้ำมันพืช** 1 ช้อนโต๊ะ
        - **ทองคำเปลว** สำหรับตกแต่ง
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
