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
kanom_img_path = os.getenv("COMPONENT_121_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองชมพูนุท: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมทองชมพูนุท")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองชมพูนุท เป็นขนมมงคลไทยโบราณที่มีมาช้านาน เชื่อกันว่ามีต้นกำเนิดมาจากภาคกลาง ลักษณะของขนมทองชมพูนุทนั้น มีสีชมพูสวยสดใส หอมกลิ่นอบควันเทียน นิยมใช้ในงานมงคลหรือมอบให้เป็นของขวัญเพื่อแสดงถึงความเป็นสิริมงคล ความดีงาม และความเจริญรุ่งเรือง ปัจจุบันค่อนข้างหาทานยาก
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **แป้ง:**
        1. ผสมแป้งข้าวเจ้า แป้งข้าวเหนียว น้ำตาลทราย และเกลือ คนให้เข้ากัน
        2. ค่อย ๆ ใส่กะทิ โดยแบ่งเป็น 3 รอบ แล้วคนให้ส่วนผสมมีเนื้อเนียน
        3. กรองส่วนผสมผ่านกระชอน
        4. นำส่วนผสมขึ้นตั้งไฟ อ่อนกวนจนแป้งจับตัวเป็นก้อน จากนั้นปิดไฟ
        5. ใส่ไข่แดง คนให้เข้ากัน แล้วเปิดไฟอ่อนกวนต่อจนแป้งร่อนไม่ติดกะทะ
        6. ใส่สีผสมอาหารสีชมพู คนให้สีเข้ากันดี แล้วตักออกพึ่งให้เย็น

        **พิมพ์:**
        1. ทาพิมพ์ด้วยน้ำมันพืช
        2. ตักแป้งใส่พิมพ์ กดให้แน่น
        3. นำไปอบควันเทียน

        **อบควันเทียน:**
        1. เตรียมเตาอบควันเทียน โดยใส่ถ่านและขี้เลื่อย
        2. วางตะแกรงในเตาอบ
        3. วางขนมบนตะแกรง
        4. ปิดฝาเตาอบ รมควันประมาณ 15-20 นาที

        **พักขนม:**
        1. นำขนมออกจากเตาอบ พักให้เย็น
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - **แป้ง:**
          - แป้งข้าวเจ้า 60 กรัม
          - แป้งข้าวเหนียว 15 กรัม
          - กะทิ 115 กรัม
          - น้ำตาลทราย 85 กรัม
          - เกลือ ¼ ชัอนชา
          - ไข่แดง (ไข่ไก่) 2 ฟอง

        - **สีผสมอาหารสีชมพู:** สำหรับผสมเป็นสีชมพูสวยสดใส
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
