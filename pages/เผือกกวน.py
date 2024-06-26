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
kanom_img_path = os.getenv("COMPONENT_155_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="เผือกกวน: ขนมไทยโบราณ หวานมัน หอมกะทิ ทานเล่นหรือทานคู่กับอาหารคาว",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("เผือกกวน: ขนมไทยโบราณ หวานมัน หอมกะทิ ทานเล่นหรือทานคู่กับอาหารคาว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเผือกกวน เป็นขนมไทยโบราณที่มีมานานกว่า 200 ปี นิยมทำกันในงานมงคล งานประเพณี และทานเล่นทั่วไป เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ผิวพรรณผ่องใส
        เอกลักษณ์ของขนมเผือกกวนคือ เนื้อขนมนุ่มหนึบ หวานมัน หอมกะทิ โรยหน้าด้วยเม็ดมุกน้ำตาล ทานคู่กับกะทิสด
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - เผือก 500 กรัม
    - น้ำตาลทราย 150 กรัม
    - กะทิ 250 กรัม
    - เกลือป่น 1/4 ช้อนชา
    - เม็ดมุกน้ำตาล (สำหรับโรยหน้า)
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. นึ่งเผือกจนสุก
        2. บดเผือกจนเนียน
        3. ใส่กะทิ น้ำตาลทราย เกลือป่น คนให้เข้ากัน
        4. ตั้งกระทะใส่น้ำมันพืช ใส่ส่วนผสมเผือก เคี่ยวจนเนื้อขนมข้นหนืด
        5. เทขนมใส่ถาด รอให้เย็น
        6. โรยหน้าด้วยเม็ดมุกน้ำตาล
        7. ตัดขนมเป็นชิ้นพอดีคำ
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้เผือกที่มีเนื้อแน่น จะได้ขนมที่มีเนื้อสัมผัสที่ดี
        - สามารถปรับปริมาณน้ำตาลทรายได้ตามชอบ
        - ควรโรยเม็ดมุกน้ำตาลหลังจากขนมเย็นแล้ว จะได้ไม่ละลาย
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
