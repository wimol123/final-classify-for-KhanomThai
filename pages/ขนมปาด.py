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
kanom_img_path = os.getenv("COMPONENT_150_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

st.set_page_config(
    page_title="ขนมปาด: ขนมพื้นบ้านล้านนา หวานมัน หอมกะทิ",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมปาด: ขนมพื้นบ้านล้านนา หวานมัน หอมกะทิ")
st.image(image=kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมปาด หรือ ข้าวหนมปาด เป็นขนมพื้นบ้านของชาวล้านนา นิยมทำกันในงานบุญ งานมงคล และทานเล่นทั่วไป เอกลักษณ์ของขนมชนิดนี้คือ เนื้อขนมเหนียวนุ่ม หวานมัน หอมกะทิ ทานคู่กับมะพร้าวขูด
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - แป้งข้าวเจ้า 1 กิโลกรัม
    - แป้งข้าวเหนียว 1/2 กิโลกรัม
    - น้ำอ้อย 2 1/2 กิโลกรัม
    - มะพร้าวขูด 1 กิโลกรัม
    - เกลือ 1/2 ช้อนชา
    - น้ำมันพืช (สำหรับทาถาดและใบตอง)
    """
)

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. ผสมแป้งข้าวเจ้า แป้งข้าวเหนียว เกลือ และน้ำอ้อย คนให้เข้ากันจนแป้งละลาย ไม่มีก้อน
        2. ตั้งกระทะทองเหลืองหรือกระทะก้นหนา ใช้ไฟปานกลาง
        3. เทส่วนผสมแป้งลงในกระทะ คนไปเรื่อยๆ จนแป้งเหนียวหนืด และมีเนื้อใส
        4. เทแป้งที่สุกแล้วลงบนถาดหรือภาชนะที่เตรียมไว้ ทาด้วยน้ำมันพืชบางๆ
        5. รอให้ขนมเย็น แล้วตัดเป็นชิ้นพอดีคำ
        6. โรยมะพร้าวขูด ทานคู่กับน้ำชาหรือกาแฟ
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ปริมาณน้ำอ้อยสามารถปรับได้ตามชอบ หากต้องการขนมหวานมาก ใส่น้ำอ้อยเพิ่ม
        - มะพร้าวขูดควรเป็นมะพร้าวทึนทึก จะได้เนื้อสัมผัสที่หยาบ อร่อย
        - ขนมปาดสามารถเก็บไว้ทานได้หลายวัน โดยใส่ในภาชนะที่ปิดมิดชิด เก็บไว้ในตู้เย็น
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
