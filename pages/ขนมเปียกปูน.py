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
kanom_img_path = os.getenv("COMPONENT_152_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")
# Set page configuration
st.set_page_config(
    page_title="ขนมเปียกปูน: ขนมไทยโบราณ หวานมัน หอมกะทิ ทานเล่นหรือทานคู่กับอาหารคาว",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image(header_img_path)
# Display title
st.title("ขนมเปียกปูน: ขนมไทยโบราณ หวานมัน หอมกะทิ ทานเล่นหรือทานคู่กับอาหารคาว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเปียกปูนเป็นขนมไทยโบราณที่มีมานานกว่า 200 ปี นิยมทำกันในงานมงคล งานประเพณี และทานเล่นทั่วไป เชื่อกันว่าขนมชนิดนี้เป็นสิริมงคล ช่วยให้ผิวพรรณผ่องใส
        เอกลักษณ์ของขนมเปียกปูนคือ เนื้อขนมนุ่มหนึบ หวานมัน หอมกะทิ โรยหน้าด้วยงาขาวคั่ว ทานคู่กับกะทิสด
        """
    )

st.title("ส่วนผสม")
st.markdown(
    """
    - แป้งข้าวเจ้า 120 กรัม
    - แป้งท้าวยายม่อม 30 กรัม
    - แป้งมัน 30 กรัม
    - น้ำตาลทราย 50 กรัม
    - น้ำตาลมะพร้าว 200 กรัม
    - เกลือป่น 1/2 ช้อนชา
    - น้ำปูนใส 600 มล.
    - น้ำใบเตย 400 มล.
    - กะทิสด 300 มล.
    - แป้งข้าวเจ้า 20 กรัม
    - เกลือป่น 25 กรัม
    - งาขาวคั่ว
    """
)

st.title("วิธีทำตัวขนมเปียกปูน")
with st.expander("วิธีทำตัวขนมเปียกปูน"):
    st.markdown(
        """
        1. ผสมแป้งข้าวเจ้า แป้งท้าวยายม่อม แป้งมัน น้ำตาลทราย เกลือป่น และน้ำตาลมะพร้าวลงในชามผสม
        2. ใส่น้ำใบเตยลงไปทีละน้อย นวดคลึงให้เข้ากันจนแป้งเนียน
        3. เทส่วนผสมแป้งลงในกระทะทองเหลือง ตั้งไฟปานกลาง คนไปเรื่อยๆ จนแป้งสุกใส
        4. เทแป้งที่สุกแล้วลงบนถาด รอให้เย็น
        5. ตัดแป้งเป็นชิ้นพอดีคำ
        """
    )

st.title("วิธีทำกะทิราด")
with st.expander("วิธีทำกะทิราด"):
    st.markdown(
        """
        1. ผสมกะทิสด แป้งข้าวเจ้า เกลือป่น คนให้เข้ากันจนละลาย
        2. ตั้งกระทะใส่น้ำมันพืช ใส่ส่วนผสมกะทิ เคี่ยวจนกะทิข้น
        3. โรยงาขาวคั่วบนกะทิ
        """
    )

st.title("วิธีเสิร์ฟ")
with st.expander("วิธีเสิร์ฟ"):
    st.markdown(
        """
        1. ตักขนมเปียกปูนใส่จาน
        2. ราดด้วยกะทิสด
        3. ทานคู่กับน้ำชาหรือกาแฟ
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - ควรใช้แป้งข้าวเจ้าที่มีคุณภาพดี จะทำให้ขนมมีเนื้อเนียน
        - น้ำใบเตยควรคั้นจากใบเตยสด จะได้กลิ่นหอม
        - กะทิสดควรเป็นกะทิคั้นหัว จะได้กะทิที่หอมมัน
        - โรยงาขาวคั่วบนกะทิ จะช่วยเพิ่มรสชาติและความหอม
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
