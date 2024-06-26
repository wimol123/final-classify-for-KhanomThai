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
kanom_img_path = os.getenv("COMPONENT_158_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมฝรั่งกุฎีจีนทิพย์: ขนมไทยโบราณ กรอบนอก นุ่มใน หอมหวาน ทานเล่นหรือทานคู่กับอาหารคาว",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมฝรั่งกุฎีจีนทิพย์: ขนมไทยโบราณ กรอบนอก นุ่มใน หอมหวาน ทานเล่นหรือทานคู่กับอาหารคาว")
st.image(kanom_img_path)
# Display ความเป็นมา
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมฝรั่งกุฎีจีนทิพย์ เป็นขนมไทยโบราณที่มีมานานกว่า 200 ปี สันนิษฐานว่ามีต้นกำเนิดมาจากชุมชนกุฎีจีนในกรุงธนบุรี นิยมทำกันในงานมงคล งานประเพณี และทานเล่นทั่วไป เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ชีวิตราบรื่น
        เอกลักษณ์ของขนมฝรั่งกุฎีจีนทิพย์คือ เนื้อขนมกรอบนอกนุ่มใน หวานมัน หอมกลิ่นไข่ โรยหน้าด้วยผลไม้อบแห้งเช่น ลูกเกด ฟักเชื่อม และพุทราแห้ง ทานคู่กับชาหรือกาแฟ
        """
    )

# Display ส่วนผสม
st.title("ส่วนผสม")
st.markdown(
    """
    - แป้งสาลีอเนกประสงค์ 180 กรัม
    - ไข่เป็ด 5 ฟอง
    - น้ำตาลทราย 180 กรัม
    - น้ำมะนาว 1 ช้อนชา
    - ผลไม้อบแห้งตามชอบ (ลูกเกด ฟักเชื่อม พุทราแห้ง)
    - เนยขาวสำหรับทาพิมพ์
    """
)

# Display วิธีทำ
st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. แยกไข่ขาวและไข่แดง
        2. ตีไข่ขาวจนตั้งยอดอ่อน
        3. ใส่ไข่แดง น้ำตาลทราย และน้ำมะนาว ตีจนเข้ากัน
        4. ค่อยๆ ใส่อแป้งสาลี ตะล่อมให้เข้ากัน
        5. เทส่วนผสมลงในชามที่มีไข่ขาว ตะล่อมให้เข้ากัน
        6. ทาพิมพ์ด้วยเนยขาว
        7. เทส่วนผสมลงในพิมพ์
        8. โรยหน้าด้วยผลไม้อบแห้ง
        9. นำเข้าอบที่ไฟ 170 ํ ไฟบน-ล่าง 20-25 นาที หรือสังเกตุจากสีขนม
        10. พักขนมจนเย็นสนิท
        """
    )

# Display หมายเหตุ
st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้ไข่เป็ดสดใหม่ จะได้เนื้อขนมที่นุ่มฟู
        - สามารถปรับปริมาณน้ำตาลได้ตามชอบ
        - ควรอบขนมจนสุกเหลือง จะได้เนื้อสัมผัสที่กรอบนอกนุ่มใน
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
