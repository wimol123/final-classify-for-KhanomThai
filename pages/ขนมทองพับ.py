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
kanom_img_path = os.getenv("COMPONENT_124_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองพับ: ขนมไทยโบราณ กรอบ หวาน มัน อร่อย",
    page_icon="🔺",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมทองพับ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองพับ เป็นขนมไทยโบราณที่มีมาช้านาน สันนิษฐานว่ามีต้นกำเนิดมาจากแป้งจี่ของจีน ซึ่งชาวไทยได้นำมารดัดแปลงสูตร ผสมผสานกับวัฒนธรรมการทำอาหารไทยจนกลายเป็นเอกลักษณ์เฉพาะตัว ขนมทองพับนิยมทำขึ้นเพื่อเป็นของว่าง ของฝาก หรือใช้ประกอบพิธีกรรมต่างๆ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมทองพับ มีวิธีทำดังนี้:**

        1. **ทำแป้ง:** ผสมแป้งสาลีอเนกประสงค์, แป้งข้าวเจ้า, เกลือ, และน้ำเปล่า นวดจนแป้งเนียน พักไว้
        2. **ทำไส้:** ผสมกะทิ, น้ำตาลทราย, เกลือ, และไข่ไก่ คนจนเข้ากัน นำไปตั้งไฟจนส่วนผสมข้นเหนียว พักไว้
        3. **ปั้นขนม:** แบ่งแป้งเป็นก้อนกลมๆ รีดแป้งเป็นแผ่นบาง ตักไส้ใส่ตรงกลาง พับแป้งเป็นรูปสามเหลี่ยม ทาไข่แดงบางๆ
        4. **อบขนม:** นำขนมไปอบในเตาอบที่อุณหภูมิ 180 องศาเซลเซียส ประมาณ 20 นาที หรือจนขนมสุกเหลือง
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - **แป้งสาลีอเนกประสงค์** 1 ถ้วยตวง
        - **แป้งข้าวเจ้า** 1/2 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา
        - **น้ำเปล่า** 1 ถ้วยตวง

        **ไส้:**
        - **กะทิ** 1 ถ้วยตวง
        - **น้ำตาลทราย** 1/2 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา
        - **ไข่ไก่** 1 ฟอง

        **เพิ่มเติม:**
        - **ไข่แดง** สำหรับทาหน้าขนม
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
