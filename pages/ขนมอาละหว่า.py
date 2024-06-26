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
kanom_img_path = os.getenv("COMPONENT_231_PATH1")
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
st.title("ขนมอาละหว่า")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมอาละหว่า เป็นขนมพื้นเมืองไทยใหญ่ นิยมทานกันในจังหวัดแม่ฮ่องสอน มีลักษณ์เฉพาะตัวด้วยรสชาติหวานมัน หอมกะทิ ทานคู่กับน้ำกะทิ
        ในอดีต ขนมอาละหว่า นิยมทำทานในงานมงคลต่างๆ เชื่อกันว่าจะช่วยเสริมสิริมงคล โชคลาภ และความเจริญรุ่งเรือง
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ส่วนผสม:**

        **ตัวแป้ง:**
        - แป้งข้าวเจ้า 500 กรัม
        - น้ำเปล่า 500 มิลลิลิตร
        - เกลือ 1/2 ช้อนชา

        **ไส้:**
        - กะทิ 1 ถ้วยตวง
        - น้ำตาลปี๊บ 1 ถ้วยตวง
        - ไข่ไก่ 1 ฟอง
        - เกลือ 1/4 ช้อนชา

        **วิธีทำ:**

        **ตัวแป้ง:**
        1. ผสมแป้งข้าวเจ้า น้ำเปล่า และเกลือ นวดจนแป้งเนียน
        2. พักแป้งไว้ 30 นาที
        3. แบ่งแป้งเป็นก้อนกลมๆ ขนาดเท่าไข่ไก่
        4. กดแป้งให้แบน แล้วใส่ไส้

        **ไส้:**
        1. ผสมกะทิ น้ำตาลปี๊บ ไข่ไก่ และเกลือ คนให้เข้ากัน
        2. นำส่วนผสมไปกวนจนแห้ง

        **การประกอบร่าง:**
        1. นำแป้งที่ใส่ไส้แล้ว ไปนึ่งจนสุก
        2. ราดด้วยกะทิ

        **เคล็ดลับ:**
        - เลือกใช้แป้งข้าวเจ้าที่มีคุณภาพดี จะได้เนื้อสัมผัสที่เนียน
        - กวนไส้จนแห้งสนิท จะได้ไม่เละ
        - ปรับความหวานของกะทิตามชอบ
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
