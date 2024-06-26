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
kanom_img_path = os.getenv("COMPONENT_28_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวแดกงา: ขนมพื้นบ้านจากแป้งข้าวเหนียว",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวแดกงา: ขนมพื้นบ้านจากแป้งข้าวเหนียว")
st.image(kanom_img_path)
# ประวัติความเป็นมา
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
        เชื่อกันว่า ขนมข้าวแดกงามีมาช้านาน แต่ไม่มีหลักฐานแน่ชัดว่า起源มาจากไหน สันนิษฐานว่าน่าจะได้รับอิทธิพลมาจากอาหารของชาวลาว
        ในอดีต ขนมข้าวแดกงามักถูกทำขึ้นเพื่อเป็นเสบียงอาหารในยามทำนา เพราะสามารถเก็บไว้ทานได้นาน
        """
    )

# วิธีทำ
st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **เตรียมแป้งข้าวเหนียว:**
        1. นำแป้งข้าวเหนียวมาผสมกับน้ำเกลือ นวดจนแป้งเนียน
        2. รีดแป้งเป็นแผ่นบางๆ
        3. ตัดแป้งเป็นชิ้นสี่เหลี่ยมหรือตามชอบ

        **นำไปคั่ว:**
        4. ตั้งกระทะใส่น้ำมัน นำแป้งที่ตัดไว้ไปคั่วจนเหลืองกรอบ
        5. โรยงาขาวคั่วลงบนขนมข้าวแดกงา
        """
    )

# ส่วนผสม
st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - แป้งข้าวเหนียว
        - น้ำเกลือ
        - น้ำมัน
        - งาขาว
        """
    )

# หมายเหตุ
st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - สามารถใช้เตาแก๊ส หรือเตาถ่านในการคั่วขนมข้าวแดกงา
        - นิยมทานขนมข้าวแดกงาคู่กับน้ำชา
        """
    )

# Link back to Home
st.page_link("Home.py", label="Home", icon="↩️")
