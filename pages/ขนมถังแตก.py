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
kanom_img_path = os.getenv("COMPONENT_111_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")
# Set page configuration
st.set_page_config(
    page_title="ขนมถังแตก: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมถังแตก")

st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมถังแตก เป็นขนมไทยโบราณที่มีมาช้านาน เชื่อกันว่ามีต้นกำเนิดมาจากภาคใต้ มักถูกนำมาใช้เป็นของว่างในงานมงคลต่างๆ ลักษณะของขนมถังแตกนั้น มีหน้าตาคล้ายกับขนมครก แต่มีขนาดใหญ่กว่า และมีรูพรุนกระจายอยู่ทั่วทั้งแผ่น แป้งของขนมถังแตกนั้น นุ่มฟู หอมหวานมัน ทานคู่กับไส้ต่างๆ เช่น มะพร้าวทึนทึกขูด ฝอยทอง เผือก มันม่วง ข้าวโพด
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. หมักแป้ง: ผสมแป้งข้าวเจ้า แป้งสาลีอเนกประสงค์ น้ำตาลทราย ยีสต์ เกลือ ผงฟู และน้ำเปล่า คนให้เข้ากันจนส่วนผสมละลายดี พักไว้ให้แป้งขึ้นฟู ประมาณ 1-2 ชั่วโมง
        2. เตรียมไส้: มะพร้าวทึนทึกขูด นำมาผสมกับน้ำตาลทราย เกลือ งาดำคั่ว และงาขาวคั่ว คนให้เข้ากัน
        3. ทอดขนม: ตั้งกระทะ ใส่น้ำมันพืชเล็กน้อย รอจนร้อน เทแป้งลงไปประมาณ 1 ช้อนโต๊ะ รอจนแป้งเริ่มสุก ใส่ไส้ลงไป พับครึ่ง ทอดต่อจนเหลืองกรอบ ตักขึ้นพักให้สะเด็ดน้ำมัน
        4. โรยหน้า: โรยหน้าขนมด้วยน้ำตาลทรายผสมงาขาวคั่ว และงาดำคั่ว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **แป้ง:**
        - แป้งข้าวเจ้า 500 กรัม
        - แป้งสาลีอเนกประสงค์ 200 กรัม
        - น้ำตาลทราย 200 กรัม
        - ยีสต์ 1 ช้อนชา
        - ผงฟู 1 ช้อนโต๊ะ
        - เกลือ 1 ช้อนชา
        - น้ำเปล่า 600 มิลลิลิตร
        - ไข่ไก่ 1 ฟอง
        - กลิ่นวานิลลา 1 ช้อนชา
        
        **ไส้:**
        - มะพร้าวทึนทึกขูด 200 กรัม
        - น้ำตาลทราย 50 กรัม
        - เกลือ 1/2 ช้อนชา
        - งาดำคั่ว 2 ช้อนโต๊ะ
        - งาขาวคั่ว 2 ช้อนโต๊ะ
        
        **โรยหน้า:**
        - น้ำตาลทราย 50 กรัม
        - งาดำคั่ว 1 ช้อนโต๊ะ
        - งาขาวคั่ว 1 ช้อนโต๊ะ
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
