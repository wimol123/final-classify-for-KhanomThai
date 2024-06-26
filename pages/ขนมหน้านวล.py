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
kanom_img_path = os.getenv("COMPONENT_219_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมหน้านวล",
    page_icon="🎋",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมหน้านวล")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมหน้านวล หรือ ขนมทองโปร่ง เป็นขนมไทยโบราณที่มีมาตั้งแต่สมัยกรุงศรีอยุธยา เชื่อกันว่าได้รับอิทธิพลมาจากขนมโปรตุเกสที่มีชื่อว่า "โอวอส โมเลส" (Ovos Moles)

        ขนมหน้านวล นิยมทำกันในหมู่ชาววัง และเป็นที่โปรดปรานของสมเด็จพระนารายณ์มหาราช ขนมชนิดนี้มักทำในงานมงคลต่างๆ เช่น งานฉลองวันเกิด งานขึ้นบ้านใหม่

        ปัจจุบัน ขนมหน้านวลหาทานได้ยากขึ้น แต่ยังมีบางร้านที่ยังคงทำขนมชนิดนี้ขายอยู่ และด้วยความอร่อย หวานมัน กรอบนอก นุ่มใน ขนมหน้านวลจึงยังคงเป็นที่ชื่นชอบของคนไทยมาจนถึงปัจจุบัน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**
        - ไข่แดง 5 ฟอง
        - แป้งเค้ก 25 กรัม
        - น้ำตาลทรายป่น 120 กรัม
        - น้ำมันพืชสำหรับทาพิมพ์

        **วิธีทำ:**
        1. ตีไข่แดงกับน้ำตาลทรายป่นจนตั้งยอด
        2. ร่อนแป้งเค้กใส่ลงในไข่แดง ตะล่อมให้เข้ากัน
        3. ใส่ส่วนผสมลงในถุงบีบ
        4. บีบส่วนผสมลงในพิมพ์รูปเรือที่ทาด้วยน้ำมันพืช ประมาณ ¾ ของพิมพ์
        5. อบไฟ 150 องศาเซลเซียส ประมาณ 15-20 นาที
        6. พักให้ขนมเย็นลงก่อนนำออกจากพิมพ์
        """
    )

# Link back to Home.py
st.page_link("Home.py", label="Home", icon="↩️")
