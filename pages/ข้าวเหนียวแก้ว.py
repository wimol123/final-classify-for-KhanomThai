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
kanom_img_path = os.getenv("COMPONENT_40_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวเหนียวแก้ว: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวเหนียวแก้ว: ความเป็นมา วิธีทำ และส่วนผสม")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมข้าวเหนียวแก้ว เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในงานมงคลต่างๆ เช่น งานแต่งงาน งานขึ้นบ้านใหม่ เชื่อว่าจะนำโชคลาภและความเจริญรุ่งเรืองให้กับผู้ที่รับประทาน
        ขนมชนิดนี้มีลักษณะคล้ายกับข้าวเหนียวมูน แต่มีกรรมวิธีการทำที่พิเศษกว่า ตรงที่มีการคลุกข้าวเหนียวกับน้ำกะทิเข้มข้นก่อนนำไปนึ่ง ทำให้เนื้อขนมมีความนุ่ม หอม หวานมัน และมีสีเหลืองสวย น่ารับประทาน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. ล้างข้าวเหนียวเขี้ยวงูให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
        2. ผสมกะทิ น้ำตาลทราย เกลือ และใบเตย ตั้งไฟปานกลาง กวนจนน้ำตาลละลายและกะทิเริ่มเดือด
        3. เทกะทิที่ผสมไว้ลงไปในข้าวเหนียวที่แช่น้ำไว้ คลุกเคล้าให้เข้ากันจนข้าวเหนียวดูดกะทิหมด
        4. เทข้าวเหนียวที่คลุกกะทิลงในตะกร้า นึ่งด้วยไฟปานกลางประมาณ 40-50 นาที หรือจนข้าวเหนียวสุก
        5. เมื่อข้าวเหนียวสุกแล้ว ยกออกจากเตานึ่ง พักไว้ให้เย็น
        6. จัดเสิร์ฟข้าวเหนียวแก้ว ทานคู่กับมะม่วงสุก หรือทุเรียนก็อร่อย
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ข้าวเหนียวเขี้ยวงู 1 ถ้วยตวง
        - กะทิ 2 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - ใบเตย 2-3 ใบ (สำหรับหอม)
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้ข้าวเหนียวเขี้ยวงู จะทำให้เนื้อข้าวเหนียวมีกลิ่นหอมและมีความเหนียวนุ่ม
        - กะทิควรใช้กะทิสด จะทำให้ขนมมีรสชาติหอมมันอร่อย
        - น้ำตาลทรายสามารถปรับเพิ่มหรือลดได้ตามชอบ
        - ใบเตยสามารถใส่หรือไม่ใส่ก็ได้
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
