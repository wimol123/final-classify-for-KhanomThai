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
kanom_img_path = os.getenv("COMPONENT_67_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมครองแครงน้ำกะทิ: ขนมไทยโบราณ หอมมัน หวานมัน กรอบนอกนุ่มใน",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมครองแครงน้ำกะทิ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมครองแครงน้ำกะทิ เป็นขนมไทยโบราณที่มีมาช้านาน มีหลักฐานปรากฏในวรรณคดีไทยหลายเรื่อง 
        สันนิษฐานว่ามีต้นกำเนิดมาจากประเทศอินเดีย ซึ่งชาวไทยได้นำมารดัดแปลงสูตร ผสมผสานกับวัฒนธรรมการทำอาหารไทยจนกลายเป็นเอกลักษณ์เฉพาะตัว 
        ขนมครองแครงนิยมทำขึ้นเพื่อเป็นของว่าง ของหวาน หรือใช้ประกอบพิธีกรรมต่างๆ
        """
    )

st.title("ลักษณะของขนมครองแครงน้ำกะทิ")
with st.expander("ลักษณะของขนมครองแครงน้ำกะทิ"):
    st.markdown(
        """
        **ลักษณะของขนมครองแครงน้ำกะทิ:**
        - มีสีขาวนวล สื่อถึงความบริสุทธิ์
        - มีรสชาติหวานมัน กลมกล่อม
        - มีเนื้อสัมผัสกรอบนอกนุ่มใน
        - มีรูปร่างกลม คล้ายดอกไม้
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมครองแครงน้ำกะทิ มีวิธีทำดังนี้:**

        1. **ทำแป้ง:** ผสมแป้งมัน, น้ำเปล่า, ใบเตย, และเกลือ คนจนเข้ากัน พักไว้
        2. **ทำน้ำกะทิ:** ผสมหัวกะทิ, น้ำตาลทราย, และเกลือ ตั้งไฟจนน้ำตาลทรายละลาย
        3. **หยอดขนม:** ตักแป้งใส่กระบอกฉีด หยอดลงในน้ำกะทิเดือด ต้มจนขนมสุก
        4. **กะทิ:** ราดกะทิสดบนขนมครองแครง
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **แป้ง:**
        - แป้งมัน 1 ถ้วยตวง
        - น้ำเปล่า 1 ถ้วยตวง
        - ใบเตย 2-3 ใบ
        - เกลือ 1/4 ช้อนชา

        **น้ำกะทิ:**
        - หัวกะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
