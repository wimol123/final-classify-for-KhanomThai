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
kanom_img_path = os.getenv("COMPONENT_195_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมลูกเดือยน้ำกะทิ: ความหวานละมุน หอมก รุ่นเก่าแก่",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
st.title("ขนมลูกเดือยน้ำกะทิ: ความหวานละมุน หอมก รุ่นเก่าแก่")
st.image(kanom_img_path)
st.title("ที่มา")
with st.expander("ที่มา"):
    st.markdown(
        """
        ขนมลูกเดือยน้ำกะทิ ขนมหวานไทยโบราณที่ขึ้นชื่อเรื่องความหอม หวาน ละมุน กลมกล่อม ทานคู่กับน้ำกะทิเย็นชื่นใจ เป็นที่นิยมมาอย่างยาวนาน
    """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ลูกเดือยแห้ง 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - กะทิสด 4 ถ้วยตวง
        - ใบเตย 2-3 ใบ (มัดรวมกัน)
        - น้ำเปล่า 4 ถ้วยตวง
    """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. ล้างลูกเดือยให้สะอาด แช่น้ำทิ้งไว้ 4-6 ชั่วโมง หรือข้ามคืน
        2. ต้มน้ำเปล่าใส่น้ำตาลทราย เกลือ และใบเตย มัดรวมกัน ตั้งไฟจนน้ำตาลละลาย
        3. เทลูกเดือยที่แช่น้ำไว้ลงในหม้อน้ำตาล ต้มจนลูกเดือยนิ่ม
        4. เทกะทิสดลงในหม้อ คนเรื่อยๆจนกะทิละลายเข้ากัน
        5. ต้มต่อจนน้ำกะทิเริ่มข้น เกลี่ยฟองบนผิวหน้าออก
        6. ปิดไฟ ตักใส่ถ้วย เสิร์ฟพร้อมน้ำแข็ง
    """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สามารถเพิ่มเครื่องเทศอื่นๆ เช่น อบเชย รากฝรั่ง ลงในหม้อน้ำตาลเพื่อเพิ่มกลิ่นหอม
        - เลือกใช้ใบเตยหอมๆ จะช่วยเพิ่มรสชาติให้กับขนม
        - ปรับความหวานของน้ำกะทิได้ตามชอบ
        - ทานร้อนๆ หรือทานเย็นก็อร่อย
    """
    )

st.page_link("Home.py", label="Home", icon="↩️")
