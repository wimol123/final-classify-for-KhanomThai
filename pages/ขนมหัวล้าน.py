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
kanom_img_path = os.getenv("COMPONENT_226_PATH1")
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
st.title("ขนมหัวล้าน")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมหัวล้าน เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัวด้วยรูปร่างกลมๆ นูนๆ คล้ายหัวล้าน มีทั้งแบบทอด แบบนึ่ง และแบบต้ม นิยมทานคู่กับกะทิ รสชาติหวานมัน กลมกล่อม ละมุนลิ้น
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ตัวแป้ง:**

        - แป้งข้าวเหนียว 300 กรัม
        - น้ำเปล่า 320 มิลลิลิตร
        - เกลือ 1/4 ช้อนชา

        **ไส้:**

        - มะพร้าวขูดขาว 200 กรัม
        - น้ำตาลปี๊บ 150 กรัม
        - น้ำเปล่า 100 มิลลิลิตร
        - เกลือ 1/4 ช้อนชา

        **กะทิ:**

        - หัวกะทิ 1 ถ้วย
        - น้ำตาลทราย 1-2 ช้อนโต๊ะ
        - เกลือ 1/4 ช้อนชา
        - แป้งข้าวเจ้าหรือแป้งข้าวโพด 1-2 ช้อนชา (ไม่ใส่ก็ได้ค่ะ แต่ใส่ให้กะทิข้นหน่อย)

        **วิธีทำตัวแป้ง:**

        1. ผสมแป้งข้าวเหนียว น้ำเปล่า และเกลือ นวดจนแป้งเนียน
        2. พักแป้งไว้ 30 นาที
        3. แบ่งแป้งเป็นก้อนกลมๆ ขนาดเท่าไข่ไก่
        4. กดแป้งให้แบน แล้วใส่ไส้

        **วิธีทำไส้:**

        1. ผสมมะพร้าวขูดขาว น้ำตาลปี๊บ น้ำเปล่า และเกลือ คนให้เข้ากัน
        2. นำส่วนผสมไปกวนจนแห้ง

        **วิธีทำกะทิ:**

        1. ตั้งกระทะใส่น้ำกะทิ น้ำตาลทราย เกลือ และแป้งข้าวเจ้าหรือแป้งข้าวโพด คนจนเข้ากัน
        2. เคี่ยวจนกะทิข้น

        **การประกอบร่าง:**

        1. นำแป้งที่ใส่ไส้แล้ว ไปนึ่งจนสุก
        2. ราดด้วยกะทิ

        **เคล็ดลับ:**

        - เลือกใช้แป้งข้าวเหนียวที่มีคุณภาพดี จะได้เนื้อสัมผัสที่นุ่ม
        - กวนไส้จนแห้งสนิท จะได้ไม่เละ
        - ปรับความหวานของกะทิตามชอบ
        """
    )

# Link back to Home.py
st.page_link("Home.py", label="Home", icon="↩️")
