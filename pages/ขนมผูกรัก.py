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
kanom_img_path = os.getenv("COMPONENT_154_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมผูกรัก: ขนมไทยโบราณจากเมืองสตูล หอม อร่อย ทานเล่นหรือทานคู่กับอาหารคาว",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมผูกรัก: ขนมไทยโบราณจากเมืองสตูล หอม อร่อย ทานเล่นหรือทานคู่กับอาหารคาว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมผูกรัก เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว นิยมทำกันในจังหวัดสตูล เชื่อกันว่าขนมชนิดนี้มีมานานกว่า 100 ปี
        เอกลักษณ์ของขนมผูกรักคือ แป้งบางกรอบ ไส้แน่นเต็มคำ มีรสชาติหวานมัน หอมเครื่องเทศ ทานคู่กับน้ำชาหรือกาแฟร้อนๆ
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - แป้งข้าวเหนียว 200 กรัม
    - แป้งข้าวเจ้า 100 กรัม
    - เกลือ 1/2 ช้อนชา
    - น้ำเปล่า 1 ถ้วยตวง
    - น้ำมันพืช สำหรับทอด
"""
)

st.title("ไส้")
st.markdown(
    """
    - ปลาทูนึ่งแกะเอาแต่เนื้อ 2 ถ้วยตวง
    - หอมแดงซอย 1/2 ถ้วยตวง
    - ตะไคร้ซอย 1/2 ช้อนโต๊ะ
    - พริกแกงเผ็ด 2 ช้อนโต๊ะ
    - น้ำตาลปี๊บ 1/4 ถ้วยตวง
    - เกลือ 1/2 ช้อนชา
    - น้ำมันพืช 2 ช้อนโต๊ะ
"""
)

st.title("วิธีทำตัวขนม")
with st.expander("วิธีทำตัวขนม"):
    st.markdown(
        """
        1. ผสมแป้งข้าวเหนียว แป้งข้าวเจ้า เกลือ และน้ำเปล่า นวดจนแป้งเนียน พักไว้
        2. แบ่งแป้งเป็นก้อนกลมๆ รีดให้เป็นแผ่นบางๆ
        3. ใส่ไส้ตรงกลาง พับแป้งแล้วผูกรักให้แน่น
        4. ตั้งกระทะใส่น้ำมัน รอจนร้อน นำขนมผูกรักลงทอดจนสุกเหลือง ตักขึ้นพักไว้
        """
    )

st.title("วิธีทำไส้")
with st.expander("วิธีทำไส้"):
    st.markdown(
        """
        1. ตั้งกระทะใส่น้ำมัน ใส่หอมแดงซอย ตะไคร้ซอย ผัดจนหอม
        2. ใส่พริกแกงเผ็ด ผัดจนหอม
        3. ใส่เนื้อปลาทูนึ่ง ผัดจนเข้ากัน
        4. ปรุงรสด้วยน้ำตาลปี๊บ เกลือ ผัดจนไส้แห้ง
        """
    )

st.title("วิธีเสิร์ฟ")
with st.expander("วิธีเสิร์ฟ"):
    st.markdown(
        """
        1. ตักขนมผูกรักใส่จาน
        2. ทานคู่กับน้ำชาหรือกาแฟร้อนๆ
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้ปลาทูนึ่งสด จะได้ไส้ที่มีรสชาติอร่อย
        - สามารถปรับปริมาณพริกแกงเผ็ดได้ตามชอบ
        - ควรทอดขนมผูกรักจนสุกเหลือง จะได้เนื้อสัมผัสที่กรอบอร่อย
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
