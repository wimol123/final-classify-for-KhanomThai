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
kanom_img_path = os.getenv("COMPONENT_159_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมฝอยทอง: ขนมไทยโบราณ สีทองอร่าม หวานมัน หอมละมุน ทานเล่นหรือเป็นของมงคล",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมฝอยทอง: ขนมไทยโบราณ สีทองอร่าม หวานมัน หอมละมุน ทานเล่นหรือเป็นของมงคล")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมฝอยทอง เป็นขนมไทยโบราณที่มีมานานกว่า 200 ปี นิยมทำกันในงานมงคล งานประเพณี และงานสำคัญต่างๆ เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ชีวิตมั่งคั่ง ร่ำรวย เจริญก้าวหน้า
        เอกลักษณ์ของขนมฝอยทองคือ เส้นขนมสีเหลืองอร่าม เหนียวนุ่ม หวานมัน หอมกะทิ ทานคู่กับน้ำกะทิ หรือ ไอศกรีมกะทิ
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - ไข่แดง 5 ฟอง
    - น้ำตาลทราย 1 ถ้วยตวง
    - น้ำเปล่า 1/2 ถ้วยตวง
    - กะทิ 1 ถ้วยตวง
    - ใบเตย 2-3 ใบ
    - เกลือ 1/4 ช้อนชา
    - น้ำมันสำหรับทาพิมพ์
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. แยกไข่แดงและไข่ขาว
        2. ตีไข่แดงกับน้ำตาลทรายจนเข้ากัน
        3. ค่อยๆ ใส่น้ำเปล่า กะทิ ใบเตย เกลือ ตีจนเข้ากัน
        4. กรองส่วนผสม
        5. ตั้งกระทะ ใส่น้ำมัน เทส่วนผสมลงในกระทะ ใช้ตะแกรงตักส่วนผสม กรอกเป็นเส้นลงในกระทะ
        6. ต้มน้ำเชื่อม ใส่น้ำตาลทราย ใบเตย น้ำเปล่า ต้มจนน้ำตาลละลาย
        7. ตักเส้นฝอยทองใส่ในน้ำเชื่อม แช่ไว้จนเส้นฝอยทองนิ่ม
        8. ตักเส้นฝอยทองขึ้น จัดใส่จาน
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้ไข่แดงสดใหม่ จะได้เส้นฝอยทองที่มีสีสวย
        - สามารถปรับปริมาณน้ำตาลได้ตามชอบ
        - ควรต้มเส้นฝอยทองในน้ำเชื่อมจนนิ่ม จะได้เนื้อสัมผัสที่ดี
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
