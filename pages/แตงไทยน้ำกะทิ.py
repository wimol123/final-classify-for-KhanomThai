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
kanom_img_path = os.getenv("COMPONENT_106_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมแตงไทยน้ำกะทิ: ของหวานไทยโบราณ หอมหวาน ชื่นใจ",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมแตงไทยน้ำกะทิ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมแตงไทยน้ำกะทิ เป็นขนมหวานไทยโบราณที่มีมานานหลายร้อยปี นิยมทานกันในทุกภาคของประเทศไทย 
        แต่ละท้องถิ่นจะมีสูตรและวิธีทำที่แตกต่างกันบ้าง แต่วัตถุดิบหลักๆ จะคล้ายคลึงกัน
        ในสมัยโบราณ ขนมแตงไทยน้ำกะทิ มักถูกนำมาเสิร์ฟในงานมงคลต่างๆ เช่น งานแต่งงาน งานขึ้นบ้านใหม่ เพราะเชื่อกันว่า 
        "แตงไทย" มีสีแดง สื่อถึงความเป็นสิริมงคล "กะทิ" สื่อถึงความอุดมสมบูรณ์
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมแตงไทย: ล้างแตงไทยให้สะอาด ปอกเปลือก คว้านเอาไส้และเมล็ดออก หั่นแตงไทยเป็นชิ้นพอดีคำ 
           นำไปแช่เย็นให้แตงไทยกรอบ
        2. เตรียมน้ำกะทิ: นำกะทิใส่หม้อ เติมน้ำตาลมะพร้าว เกลือป่น ใบเตย ตั้งไฟอ่อนๆ คนจนน้ำตาลมะพร้าวละลาย 
           พอเดือดแล้วปิดไฟ พักไว้ให้เย็น
        3. ประกอบเสิร์ฟ: ใส่แตงไทยลงในชาม ราดด้วยน้ำกะทิที่เย็นแล้ว โรยหน้าด้วยเมล็ดถั่วลิสงคั่ว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - แตงไทย 1 ลูก
        - กะทิ 500 กรัม
        - น้ำตาลมะพร้าว 180 กรัม
        - เกลือป่น 1/2 ช้อนชา
        - ใบเตย 4-5 ใบ
        - เมล็ดถั่วลิสงคั่ว สำหรับโรยหน้า (ไม่จำเป็น)
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - สามารถปรับความหวานมันของน้ำกะทิได้ตามชอบ
        - สามารถเพิ่มเนื้อมะพร้าวอ่อน ถั่วดำ ถั่วลิสงต้ม หรือผลไม้สดอื่นๆ ลงในขนมแตงไทยได้ตามชอบ
        - ควรใช้แตงไทยสุกงอม เนื้อจะหวานฉ่ำ ทานคู่กับน้ำกะทิเย็นๆ ชื่นใจ
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
