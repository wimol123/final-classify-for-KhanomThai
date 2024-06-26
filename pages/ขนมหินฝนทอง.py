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
kanom_img_path = os.getenv("COMPONENT_227_PATH1")
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
st.title("ขนมหินฝนทอง: ขนมไทยโบราณ หายาก รสชาติอร่อย หวานมัน")
st.image(kanom_img_path)
st.markdown(
    """
    **ขนมหินฝนทอง** เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว ด้วยรูปลักษณ์ที่คล้ายหินฝนทอง สีเหลืองทองอร่าม ทำให้เป็นสัญลักษณ์ของความมั่งคั่งและร่ำรวย นิยมทำในงานมงคลต่างๆ เชื่อกันว่าจะช่วยเสริมสิริมงคล โชคลาภ และความเจริญรุ่งเรือง
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ส่วนผสม:**

        - แป้งข้าวเจ้า 2 ถ้วยตวง
        - กะทิ 1 ถ้วยตวง
        - ไข่แดง 2 ฟอง
        - น้ำตาลทราย 1 ถ้วยตวง
        - เกลือ 1/2 ช้อนชา
        - งาขาวคั่ว 1/2 ถ้วยตวง

        **วิธีทำ:**

        1. ผสมแป้งข้าวเจ้า กะทิ ไข่แดง น้ำตาลทราย เกลือ และงาขาวคั่ว คนให้เข้ากันจนเนียน
        2. เทส่วนผสมลงในพิมพ์ นำไปนึ่งจนสุก
        3. พักให้เย็น หั่นเป็นชิ้นพอดีคำ

        **เคล็ดลับ:**

        - เลือกใช้แป้งข้าวเจ้าที่มีคุณภาพดี จะได้เนื้อสัมผัสที่เนียน
        - กวนส่วนผสมจนเข้ากันดี ระวังไม่ให้เป็นก้อน
        - นึ่งด้วยไฟอ่อน ระวังไม่ให้น้ำตาลไหม้
        - ปรับความหวานของขนมตามชอบ
        """
    )

# Link back to Home.py
st.markdown("[Home](Home.py)")
