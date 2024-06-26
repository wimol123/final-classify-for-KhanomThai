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
kanom_img_path = os.getenv("COMPONENT_192_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมลิ้นจี่: ขนมไทยโบราณ สูตรลับจากคุณยาย",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมลิ้นจี่: ขนมไทยโบราณ สูตรลับจากคุณยาย")
st.image(kanom_img_path)
st.title("ที่มา")
with st.expander("ที่มา"):
    st.markdown(
        """
        ขนมลิ้นจี่ มีมาช้านาน ไม่มีหลักฐานแน่ชัดว่ามีต้นกำเนิดมาจากที่ใด แต่สันนิษฐานว่า น่าจะมีมาตั้งแต่สมัยกรุงศรีอยุธยา โดยปรากฏชื่ออยู่ในกาพย์เห่ชมเครื่องคาวหวาน
    """
    )

st.title("สูตร")
with st.expander("สูตร"):
    st.markdown(
        """
        **ส่วนผสม**
        - แป้งข้าวเจ้า 2 ถ้วยตวง
        - แป้งมันสำปะหลัง 1 ถ้วยตวง
        - เกลือ 1/2 ช้อนชา
        - น้ำตาลปี๊บ 1 ถ้วยตวง
        - น้ำเปล่า 1 ถ้วยตวง
        - ไข่ไก่ 1 ฟอง
        - น้ำมันพืช 1/2 ถ้วยตวง
        - งาขาวคั่ว 1/4 ถ้วยตวง

        **วิธีทำ**
        1. ผสมแป้งข้าวเจ้า แป้งมันสำปะหลัง เกลือ ร่อนจนเข้ากัน
        2. ละลายน้ำตาลปี๊บกับน้ำเปล่า ใส่ลงในแป้ง คนจนเข้ากันดี
        3. ตีไข่ไก่ ใส่ลงในแป้ง คนต่อจนแป้งเนียน
        4. ตั้งกระทะ ใส่น้ำมัน รอจนร้อน
        5. หยอดแป้งลงในกระทะ ตักเป็นวงกลมเล็กๆ
        6. ทอดจนขนมเหลืองกรอบ ตักขึ้นพักให้สะเด็ดน้ำมัน
        7. คลุกขนมกับงาขาวคั่ว เสร็จสิ้น
    """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - แป้งที่ใช้ควรมีอุณหภูมิห้อง จะทำให้เนื้อแป้งเนียน นุ่ม
        - การหยอดแป้งลงในกระทะ ควรใช้ช้อนโต๊ะ จะได้ขนาดขนมที่พอดีคำ
        - น้ำมันที่ใช้ทอดควรมีอุณหภูมิที่ร้อนพอดี จะได้ขนมที่กรอบไม่อมน้ำมัน
        - งาขาวคั่วควรคั่วจนหอม จะได้ขนมที่มีรสชาติอร่อยยิ่งขึ้น
    """
    )

st.title("คุณค่าทางโภชนาการ")
with st.expander("คุณค่าทางโภชนาการ"):
    st.markdown(
        """
        ขนมลิ้นจี่ ให้พลังงานจากคาร์โบไฮเดรต ไขมัน และโปรตีน
    """
    )

st.title("การเก็บรักษา")
with st.expander("การเก็บรักษา"):
    st.markdown(
        """
        ขนมลิ้นจี่ควรเก็บไว้ในภาชนะที่ปิดสนิท ห่างความชื้น อุณหภูมิห้อง เก็บได้ประมาณ 1-2 วัน
    """
    )

st.page_link("Home.py", label="Home", icon="↩️")
