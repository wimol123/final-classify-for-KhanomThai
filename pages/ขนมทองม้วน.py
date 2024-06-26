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
kanom_img_path = os.getenv("COMPONENT_125_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองม้วน: ขนมไทยโบราณ กรอบ หวาน มัน อร่อย",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมทองม้วน")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองม้วน เป็นขนมไทยโบราณที่มีมาช้านาน มีหลักฐานปรากฏในวรรณคดีไทยหลายเรื่อง สันนิษฐานว่ามีต้นกำเนิดมาจากแป้งโรตีของอินเดีย ซึ่งชาวไทยได้นำมารดัดแปลงสูตร ผสมผสานกับวัฒนธรรมการทำอาหารไทยจนกลายเป็นเอกลักษณ์เฉพาะตัว ขนมทองม้วนนิยมทำขึ้นเพื่อเป็นของว่าง ของฝาก หรือใช้ประกอบพิธีกรรมต่างๆ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมทองม้วน มีวิธีทำดังนี้:**

        1. **ทำแป้ง:** ผสมแป้งสาลีอเนกประสงค์, แป้งมัน, เกลือ, และน้ำเปล่า นวดจนแป้งเนียน พักไว้
        2. **ทำน้ำกะทิ:** ผสมกะทิ, น้ำตาลทราย, และเกลือ คนจนเข้ากัน
        3. **ทาแป้ง:** ตักแป้งมาทาบนพิมพ์ทองม้วน เกลี่ยให้บาง
        4. **อบแป้ง:** นำพิมพ์ทองม้วนไปอบในเตาอบที่อุณหภูมิ 180 องศาเซลเซียส ประมาณ 1 นาที หรือจนแป้งสุกเหลือง
        5. **ม้วนขนม:** ตักแป้งที่อบสุกแล้วออกมา รีบม้วนเป็นแท่ง พักไว้ให้เย็น
        6. **ตัดขนม:** ตัดทองม้วนเป็นท่อนสั้นๆ ตามต้องการ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - **แป้งสาลีอเนกประสงค์** 1 ถ้วยตวง
        - **แป้งมัน** 1/2 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา
        - **น้ำเปล่า** 1 ถ้วยตวง

        **น้ำกะทิ:**
        - **กะทิ** 1 ถ้วยตวง
        - **น้ำตาลทราย** 1/2 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา

        **เพิ่มเติม:**
        - **งาดำคั่ว** สำหรับโรยหน้า
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
