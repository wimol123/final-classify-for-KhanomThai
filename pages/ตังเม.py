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
kanom_img_path = os.getenv("COMPONENT_99_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมตังเม: ขนมไทยโบราณ มงคล หวานมัน หนึบหนับ",
    page_icon="🍡",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมตังเม")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมตังเม เป็นขนมไทยโบราณที่มีมาช้านาน มีหลักฐานปรากฏในวรรณคดีไทยหลายเรื่อง สันนิษฐานว่ามีต้นกำเนิดมาจากประเทศจีน ซึ่งชาวไทยได้นำมารดัดแปลงสูตร ผสมผสานกับวัฒนธรรมการทำอาหารไทยจนกลายเป็นเอกลักษณ์เฉพาะตัว 
        ขนมตังเมนิยมทำขึ้นเพื่อเป็นของว่าง ของมงคล หรือใช้ประกอบพิธีกรรมต่างๆ
        """
    )

st.title("ลักษณะของขนมตังเม")
with st.expander("ลักษณะของขนมตังเม"):
    st.markdown(
        """
        **ลักษณะของขนมตังเม:**
        - มีสีสันสดใส หลากหลายสี สื่อถึงความรื่นเริง
        - มีรสชาติหวานมัน หนึบหนับ
        - มีรูปร่างที่หลากหลาย ขึ้นอยู่กับความคิดสร้างสรรค์ของผู้ทำ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมตังเม มีวิธีทำดังนี้:**

        1. **เตรียมน้ำเชื่อม:** ผสมน้ำตาลทราย, น้ำเปล่า, และใบเตย ตั้งไฟจนน้ำตาลทรายละลาย เคี่ยวต่อจนน้ำเชื่อมข้น
        2. **เตรียมแป้ง:** ผสมแป้งข้าวเจ้า, แป้งข้าวเหนียว, กะทิ, น้ำตาลทราย, เกลือ, และสีผสมอาหาร คนจนเข้ากัน
        3. **ใส่แป้งลงพิมพ์:** เทแป้งลงพิมพ์ นำไปนึ่งจนสุก
        4. **ตัดขนมตังเม:** ตัดขนมตังเมเป็นชิ้นตามต้องการ
        5. **คลุกงา:** คลุกขนมตังเมกับงาคั่ว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **น้ำเชื่อม:**
        - น้ำตาลทราย 1 ถ้วยตวง
        - น้ำเปล่า 1/2 ถ้วยตวง
        - ใบเตย 2-3 ใบ

        **แป้ง:**
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - แป้งข้าวเหนียว 1/2 ถ้วยตวง
        - กะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - สีผสมอาหาร ตามต้องการ

        **เพิ่มเติม:**
        - งาคั่ว
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
