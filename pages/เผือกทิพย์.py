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
kanom_img_path = os.getenv("COMPONENT_157_PATH1")

# Set page configuration
st.set_page_config(
    page_title="เผือกทิพย์: ขนมไทยโบราณ เนื้อนุ่ม หอมมัน หวานละมุน ทานเล่นหรือทานคู่กับอาหารคาว",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("เผือกทิพย์: ขนมไทยโบราณ เนื้อนุ่ม หอมมัน หวานละมุน ทานเล่นหรือทานคู่กับอาหารคาว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเผือกทิพย์ หรือที่บางคนเรียกว่า ขนมมันทิพย์ เป็นขนมไทยโบราณที่มีมานานกว่า 100 ปี นิยมทำกันในงานมงคล งานประเพณี และทานเล่นทั่วไป เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ชีวิตราบรื่น
        เอกลักษณ์ของขนมเผือกทิพย์คือ เนื้อขนมนุ่มเนียน กลมกล่อม หวานมัน หอมกลิ่นเผือก ทานคู่กับชาหรือกาแฟร้อนๆ
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - เผือกนึ่ง 400 กรัม
    - ข้าวโพดต้ม 1 ฝัก
    - กะทิ 1/2 ถ้วย
    - น้ำตาลทราย 3 ช้อนโต๊ะ
    - น้ำตาลมะพร้าว 3 ช้อนโต๊ะ
    - เกลือป่น 1/4 ช้อนชา
    - ผงฟู 1 ช้อนชา
    - เนยสดรสจืด 1 ช้อนโต๊ะ
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. บดเผือกนึ่งจนเนียน
        2. ใส่ข้าวโพดต้ม บดให้เข้ากัน
        3. ใส่น้ำตาลทราย น้ำตาลมะพร้าว เกลือป่น ผงฟู เนยสด คนให้เข้ากัน
        4. ใส่กะทิ คลุกเคล้าจนส่วนผสมเข้ากันดี
        5. ปั้นเป็นก้อนกลมๆ
        6. นำไปปิ้งบนเตาถ่าน หรือ เตาไฟฟ้า หรือ ทอดในกระทะจนสุกเหลือง
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้เผือกนึ่งที่มีเนื้อแน่น จะได้ขนมที่มีเนื้อสัมผัสที่ดี
        - สามารถปรับปริมาณน้ำตาลได้ตามชอบ
        - ควรปิ้งขนมเผือกทิพย์จนสุกเหลือง จะได้เนื้อสัมผัสที่นุ่มละมุน
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
