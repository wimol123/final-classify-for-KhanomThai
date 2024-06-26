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
kanom_img_path = os.getenv("COMPONENT_27_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ข้าวจี่: เสน่ห์ของข้าวเหนียวปิ้ง หอมมัน ทานคู่กับน้ำตาล",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวจี่: เสน่ห์ของข้าวเหนียวปิ้ง หอมมัน ทานคู่กับน้ำตาล")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
        ขนมข้าวจี่เป็นขนมพื้นบ้านของภาคอีสานที่นิยมทานกันทุกเพศทุกวัย
        มีเอกลักษณ์เฉพาะตัวที่โดดเด่นด้วยความหอมมันของข้าวเหนียวปิ้ง ทานคู่กับน้ำตาลหวานๆ
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **เตรียมข้าวเหนียว:**
        1. นำข้าวเหนียวไปแช่น้ำประมาณ 3-4 ชั่วโมง จากนั้นนำไปนึ่งจนสุก

        **เตรียมน้ำกะทิ:**
        2. ผสมกะทิ เกลือ และน้ำตาล คนให้เข้ากัน

        **ปั้นข้าวเหนียว:**
        3. ปั้นข้าวเหนียวที่นึ่งสุกแล้วเป็นแท่งกลม เสียบไม้

        **ย่างข้าวเหนียว:**
        4. นำข้าวเหนียวที่เสียบไม้ไปย่างไฟอ่อนจนเหลืองกรอบ

        **ชุบไข่ (ไม่จำเป็น):**
        5. ตีไข่ไก่กับน้ำมันพืช นำข้าวเหนียวที่ย่างแล้วไปชุบไข่ นำไปย่างต่อจนไข่สุก

        **ทานคู่กับน้ำตาล:**
        6. ทานข้าวจี่ร้อนๆ คู่กับน้ำตาลทราย หรือน้ำตาลปี๊บ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ข้าวเหนียว
        - กะทิ
        - เกลือ
        - น้ำตาล
        - ไข่ไก่ (สำหรับชุบ)
        - น้ำมันพืช (สำหรับชุบไข่)
        - น้ำตาลทราย หรือน้ำตาลปี๊บ
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - สามารถใช้เตาแก๊ส หรือเตาถ่านในการย่างข้าวเหนียว
        - นิยมทานข้าวจี่คู่กับกาแฟ หรือชา
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
