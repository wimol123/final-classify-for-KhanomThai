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
kanom_img_path = os.getenv("COMPONENT_228_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมเหนียว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเหนียว เป็นขนมไทยโบราณที่มีมายาวนาน พบได้ทั่วทุกภาคของประเทศไทย นิยมทำทานคู่กับน้ำเชื่อม รสชาติหวานมัน กลมกล่อม ละมุนลิ้น มีหลายรูปแบบ หลายสูตร แตกต่างกันไปตามท้องถิ่น
        """
    )

st.title("ประเภทของขนมเหนียว")
with st.expander("ประเภทของขนมเหนียว"):
    st.markdown(
        """
        - ขนมเหนียวขาว: เป็นขนมเหนียวแบบดั้งเดิม ทำจากแป้งข้าวเหนียว กะทิ และน้ำตาลทราย
        - ขนมเหนียวดำ: คล้ายขนมเหนียวขาว แต่มีการใส่ใบเตยหรือใบอัญชัน ทำให้มีสีเขียวหรือสีม่วง
        - ขนมเหนียวไส้: มีไส้หลากหลายชนิด เช่น ไส้ถั่วกวน ไส้เผือก ไส้มันม่วง
        - ขนมเหนียวมะม่วง: ทานคู่กับมะม่วงสุก ราดด้วยกะทิ น้ำตาลทราย และน้ำปลาหวาน
        - ขนมเหนียวทอด: นำขนมเหนียวไปทอดจนเหลืองกรอบ ทานคู่กับน้ำเชื่อม
        """
    )

st.title("วิธีทำขนมเหนียว")
with st.expander("วิธีทำขนมเหนียว"):
    st.markdown(
        """
        **วัตถุดิบ:**

        - แป้งข้าวเหนียว 1 ถ้วยตวง
        - กะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - น้ำเปล่า 1/4 ถ้วยตวง (หรือตามความเหมาะสม)

        **วิธีทำ:**

        1. ผสมแป้งข้าวเหนียว กะทิ น้ำตาลทราย เกลือ และน้ำเปล่า คนให้เข้ากันจนเนียน
        2. นำส่วนผสมไปนึ่งจนสุก หรือต้มจนสุก
        3. ตักขึ้นพักให้เย็น ตัดเป็นชิ้นพอดีคำ
        """
    )

# Link back to Home.py
st.markdown("[Home](Home.py)")  # assuming Home.py is the file name for your home page
