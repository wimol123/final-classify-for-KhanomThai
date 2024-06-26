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
kanom_img_path = os.getenv("COMPONENT_224_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมหันตรา",
    page_icon="🍡",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมหันตรา")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมหันตรา เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัวด้วยรูปลักษณ์ที่สวยงาม ประณีต คล้ายกับลูกชุบ แต่มีการห่อด้วยไข่ที่ตีเป็นตารางลายสวยงาม นิยมนำมาทานคู่กับน้ำเชื่อม รสชาติหวานมัน กลมกล่อม ละมุนลิ้น

        ขนมหันตรามีต้นกำเนิดมาจากทางภาคกลางของไทย เชื่อกันว่ามีมานานกว่า 200 ปี ในอดีตนิยมทำในงานมงคลต่างๆ เพราะมีความหมายมงคล สื่อถึงความเจริญรุ่งเรือง โชคลาภ และความร่ำรวย
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**

        **ตัวหันตรา:**
        - ถั่วเขียวเลาะเปลือก 1 ถ้วยตวง
        - น้ำตาลทราย 1 ถ้วยตวง
        - หัวกะทิ 1 ถ้วยตวง
        - เกลือ 1/2 ช้อนชา

        **ไข่ตาราง:**
        - ไข่ไก่ 5 ฟอง
        - น้ำมันพืช 1 ช้อนโต๊ะ

        **น้ำเชื่อม:**
        - น้ำตาลทราย 2 ถ้วยตวง
        - น้ำเปล่า 2 ถ้วยตวง
        - ใบเตย 2-3 ใบ

        **การประกอบร่าง:**
        - นำตัวหันตราไปชุบไข่ตาราง
        - ต้มในน้ำเชื่อมจนสุก
        - ตักขึ้นพักให้สะเด็ดน้ำเชื่อม

        **เคล็ดลับ:**
        - เลือกใช้ถั่วเขียวที่มีคุณภาพดี เพื่อให้ได้เนื้อสัมผัสที่เนียน
        - กวนตัวหันตราจนแห้งสนิท จะได้ไม่เละ
        - ทอดไข่ให้บางๆ จะได้ห่อตัวหันตราได้ง่าย
        - ปรับความหวานของน้ำเชื่อมตามชอบ
        """
    )

# Link back to Home.py
st.page_link("Home.py", label="Home", icon="↩️")
