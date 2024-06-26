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
kanom_img_path = os.getenv("COMPONENT_207_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมสะบ้า: ขนมไทยพื้นบ้าน ภาคใต้ หวานมัน กลมกล่อม",
    page_icon="🍘",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมสะบ้า: ขนมไทยพื้นบ้าน ภาคใต้ หวานมัน กลมกล่อม")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมาของขนมสะบ้า"):
    st.markdown(
        """
        **ขนมสะบ้า** หรือ **ขนมบ้า** เป็นขนมไทยพื้นบ้านภาคใต้ ที่มีลักษณะคล้ายขนมตาล แต่มีขนาดเล็กกว่า ทำจากแป้งข้าวเหนียว มันเทศ น้ำตาล และงาขาว นิยมทำทานในงานบุญสารทเดือนสิบ

        เชื่อกันว่าขนมสะบ้ามีต้นกำเนิดมาจากภาคใต้ของไทย สูตรดั้งเดิมทำจากแป้งข้าวเหนียว มันเทศ น้ำตาล และงาขาว ต่อมาได้มีการดัดแปลงสูตร โดยใส่ไข่ไก่ เกลือ และน้ำเปล่าเพิ่มเติม ทำให้เนื้อขนมมีความนุ่ม และรสชาติกลมกล่อมมากขึ้น
    """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสมของขนมสะบ้า"):
    st.markdown(
        """
        - แป้งข้าวเหนียว 200 กรัม
        - มันเทศต้มสุก 300 กรัม
        - น้ำตาลทราย 100 กรัม
        - งาขาว 50 กรัม
        - ไข่ไก่ 1 ฟอง
        - เกลือ 1/2 ช้อนชา
        - น้ำเปล่า 50 มล.
    """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำขนมสะบ้า"):
    st.markdown(
        """
        **ส่วนผสม:**
        1. นำมันเทศต้มสุกมาบดให้ละเอียด
        2. ผสมแป้งข้าวเหนียว, น้ำตาลทราย, งาขาว, ไข่ไก่, เกลือ และน้ำเปล่า นวดจนแป้งเนียน
        3. ใส่มันเทศบดลงในแป้ง นวดจนเข้ากันดี
        4. ปั้นแป้งเป็นก้อนกลมๆ
        5. นำขนมไปนึ่งในลังถึง ประมาณ 30-40 นาที หรือจนขนมสุก
    """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุสำหรับขนมสะบ้า"):
    st.markdown(
        """
        - สามารถปรับปริมาณน้ำตาลทรายได้ตามชอบ
        - ใส่ใบเตยลงในแป้ง จะทำให้ขนมมีกลิ่นหอม
        - ทานคู่กับมะพร้าวขูดคั่ว หรือถั่วลิสงคั่วบด
    """
    )

st.page_link("Home.py", label="Home", icon="↩️")
