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
kanom_img_path = os.getenv("COMPONENT_220_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมหม้อแกง",
    page_icon="🍮",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมหม้อแกง")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมหม้อแกง หรือ ขนมกุมภมาศ เป็นขนมไทยชนิดหนึ่งที่มีมาตั้งแต่สมัยกรุงศรีอยุธยา โดยมีเอกสารโบราณที่กล่าวถึงขนมชนิดนี้ไว้ว่า "โคมนัส" ซึ่งสันนิษฐานว่าเพี้ยนมาจากคำว่า "โคโคนัท" หมายถึงมะพร้าว ซึ่งเป็นส่วนผสมหลักของขนมชนิดนี้

        ขนมหม้อแกงจัดเป็นขนมอบไทยยุคแรกๆ ที่ใช้ไข่ขาวเป็นส่วนผสม ต่างจากขนมไทยดั้งเดิมที่มักใช้ไข่แดง ขนมชนิดนี้ได้รับความนิยมในหมู่ชาววัง และยังเป็นที่โปรดปรานของสมเด็จพระนารายณ์มหาราช
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**
        - ไข่ไก่ 4 ฟอง
        - น้ำตาลทราย 1 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - กะทิ 2 ถ้วยตวง
        - แป้งข้าวเจ้า 1/2 ถ้วยตวง
        - มะพร้าวขูด 1 ถ้วยตวง
        - ใบเตย 3-4 ใบ (สำหรับหอม)

        **วิธีทำ:**
        1. ตีไข่ไก่กับน้ำตาลทราย เกลือ และใบเตยจนตั้งยอด
        2. ค่อยๆ ใส่กะทิ คนให้เข้ากัน
        3. ใส่แป้งข้าวเจ้า คนให้เข้ากันจนเนียน
        4. เทส่วนผสมใส่ในพิมพ์ที่ทาเนยไว้
        5. โรยมะพร้าวขูด
        6. นึ่งไฟปานกลาง ประมาณ 30-40 นาที
        7. พักให้เย็นก่อนเสิร์ฟ
        """
    )

# Link back to Home.py
st.page_link("Home.py", label="Home", icon="↩️")
