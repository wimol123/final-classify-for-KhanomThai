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
kanom_img_path = os.getenv("COMPONENT_126_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองหยอด: ขนมไทยมงคล สีเหลืองทอง หวานมันฉ่ำปาก!",
    page_icon="🍘",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมทองหยอด")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองหยอด เป็นขนมไทยโบราณที่มีมาช้านาน มีหลักฐานปรากฏในวรรณคดีไทยหลายเรื่อง สันนิษฐานว่ามีต้นกำเนิดมาจากประเทศจีน ซึ่งชาวไทยได้นำมารดัดแปลงสูตร ผสมผสานกับวัฒนธรรมการทำอาหารไทยจนกลายเป็นเอกลักษณ์เฉพาะตัว ขนมทองหยอดนิยมทำขึ้นเพื่อเป็นของว่าง ของมงคล หรือใช้ประกอบพิธีกรรมต่างๆ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมทองหยอด มีวิธีทำดังนี้:**

        1. **ทำแป้ง:** ผสมไข่แดง, แป้งข้าวเจ้า, แป้งมัน, เกลือ, และน้ำเปล่า ตีจนแป้งเนียน พักไว้
        2. **ทำน้ำเชื่อม:** ผสมน้ำตาลทรายกับน้ำเปล่า ตั้งไฟจนน้ำตาลทรายละลาย เคี่ยวต่อจนน้ำเชื่อมข้น
        3. **หยอดขนม:** ตักแป้งใส่กระบอกฉีด หยอดลงในน้ำเชื่อมเดือด ต้มจนขนมสุก ตักขึ้นพักไว้
        4. **คลุกงา:** คลุกทองหยอดกับงาคั่ว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - **ไข่แดง** 3 ฟอง
        - **แป้งข้าวเจ้า** 1/2 ถ้วยตวง
        - **แป้งมัน** 1/4 ถ้วยตวง
        - **เกลือ** 1/4 ช้อนชา
        - **น้ำเปล่า** 1/4 ถ้วยตวง

        **น้ำเชื่อม:**
        - **น้ำตาลทราย** 1 ถ้วยตวง
        - **น้ำเปล่า** 1 ถ้วยตวง

        **เพิ่มเติม:**
        - **งาคั่ว** สำหรับคลุก
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
