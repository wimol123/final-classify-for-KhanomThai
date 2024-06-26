from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_196_PATH1")
# Set page configuration
st.set_page_config(
    page_title="ขนมลูกเดือยเปียก: ขนมไทยโบราณ หวาน มัน ชื่นใจ",
    page_icon="🍮",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมลูกเดือยเปียก: ขนมไทยโบราณ หวาน มัน ชื่นใจ")
st.image(kanom_img_path)
st.title("ที่มา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมลูกเดือยเปียก มีต้นกำเนิดมาจากทางภาคใต้ของไทย ในอดีต นิยมทำทานคู่กับน้ำชา หรือกาแฟ เป็นของว่างทานเล่น หรือมอบเป็นของฝาก
    """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ส่วนผสม**
        - ลูกเดือย 1 ถ้วยตวง
        - น้ำเปล่า 3 ถ้วยตวง
        - กะทิ 2 ถ้วยตวง
        - น้ำตาลปี๊บ 1 ถ้วยตวง
        - ใบเตย 2-3 ใบ
        - เกลือ 1/2 ช้อนชา
        
        **วิธีทำ**
        1. ล้างลูกเดือยให้สะอาด แช่น้ำไว้ข้ามคืน
        2. ต้มน้ำเปล่าให้เดือด ใส่ลูกเดือยที่แช่น้ำไว้ ต้มจนลูกเดือยนุ่ม
        3. เทกะทิ น้ำตาลปี๊บ ใบเตย เกลือ ลงในหม้อ คนให้เข้ากัน
        4. เคี่ยวจนน้ำกะทิข้น ใส่ลูกเดือยที่ต้มไว้ คนให้เข้ากัน
        5. ต้มต่อจนลูกเดือยดูดน้ำกะทิ ยกลงจากเตา
        6. พักให้เย็น ตักใส่ถ้วย ทานคู่กับน้ำแข็งไส หรือไอศกรีม
        
    """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้ลูกเดือยที่มีเม็ดใหญ่ จะได้เนื้อสัมผัสที่ดี
        - แช่น้ำลูกเดือยข้ามคืน จะได้ต้มสุกง่าย
        - ปรับความหวานของน้ำกะทิตามชอบ
        - โรยหน้าด้วยงาขาวคั่ว หรือเม็ดแมงลัก เพิ่มความอร่อย
    """
    )

st.page_link("Home.py", label="Home", icon="↩️")
