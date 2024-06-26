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
kanom_img_path = os.getenv("COMPONENT_156_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="เผือกฉาบ: ขนมไทยโบราณ กรอบ หวานมัน หอมกะทิ ทานเล่นหรือทานคู่กับอาหารคาว",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("เผือกฉาบ: ขนมไทยโบราณ กรอบ หวานมัน หอมกะทิ ทานเล่นหรือทานคู่กับอาหารคาว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเผือกฉาบ เป็นขนมไทยโบราณที่มีมานานกว่า 200 ปี นิยมทำกันในงานมงคล งานประเพณี และทานเล่นทั่วไป เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ชีวิตเฟื่องฟู
        เอกลักษณ์ของขนมเผือกฉาบคือ เนื้อขนมกรอบ หวานมัน หอมกะทิ ทานคู่กับชาหรือกาแฟ
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - เผือก 1 กิโลกรัม
    - น้ำตาล 800 กรัม
    - น้ำเปล่า 300 มิลลิลิตร
    - ใบเตย 1 กำ
    - เนยเค็ม 300 กรัม
    - เกลือ 1 ช้อนโต๊ะ
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. ปอกเปลือกเผือก ล้างน้ำให้สะอาด หั่นเป็นชิ้นพอดีคำ
        2. นึ่งเผือกจนสุก
        3. เทเผือกนึ่งใส่กระทะ ใส่น้ำตาล เคี่ยวจนน้ำตาลละลาย
        4. ใส่ใบเตย เนยเค็ม เกลือ เคี่ยวต่อจนส่วนผสมเข้ากันดี
        5. เทส่วนผสมลงบนถาด รอให้เย็น
        6. ตัดขนมเป็นชิ้นพอดีคำ
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้เผือกที่มีเนื้อแน่น จะได้ขนมที่มีเนื้อสัมผัสที่ดี
        - สามารถปรับปริมาณน้ำตาลได้ตามชอบ
        - ควรทอดขนมเผือกฉาบจนสุกเหลือง จะได้เนื้อสัมผัสที่กรอบอร่อย
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
