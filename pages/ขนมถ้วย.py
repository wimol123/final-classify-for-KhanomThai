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
kanom_img_path = os.getenv("COMPONENT_108_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมถ้วย: ขนมไทยโบราณ หอมหวานมัน ทานง่าย",
    page_icon="🍮",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมถ้วย")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมถ้วย เป็นขนมไทยโบราณที่มีมานานหลายร้อยปี นิยมทำกันในทุกภาคของประเทศไทย แต่ละท้องถิ่นจะมีสูตรและวิธีทำที่แตกต่างกันบ้าง แต่วัตถุดิบหลักๆ จะคล้ายคลึงกัน
        ในสมัยโบราณ ขนมถ้วย มักถูกนำมาเสิร์ฟในงานมงคลต่างๆ เช่น งานแต่งงาน งานขึ้นบ้านใหม่ งานทำบุญ เพราะเชื่อกันว่า "ถ้วย" สื่อถึงความมั่นคง "แป้ง" สื่อถึงความเจริญรุ่งเรือง "กะทิ" สื่อถึงความอุดมสมบูรณ์
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมตัวขนมถ้วย: ผสมแป้งข้าวเจ้า แป้งมัน แป้งท้าวยายม่อม เกลือ น้ำตาลปี๊บ น้ำใบเตย และกะทิ คนจนส่วนผสมเข้ากันดี พักไว้
        2. เตรียมหน้ากะทิ: ผสมแป้งข้าวเจ้า น้ำตาลทราย เกลือ และหัวกะทิ คนจนเข้ากัน
        3. นึ่งขนมถ้วย: ใส่ตัวขนมถ้วยลงในถ้วยตะไล นึ่งด้วยไฟปานกลางประมาณ 10 นาที
        4. นึ่งหน้ากะทิ: นำหน้ากะทิมาเทลงบนตัวขนมถ้วย นึ่งต่อด้วยไฟแรงประมาณ 5 นาที หรือจนหน้ากะทิแตกมัน
        5. พักและเสิร์ฟ: รอให้ขนมถ้วยเย็นลง ทานคู่กับชา กาแฟ หรือน้ำอัญชัน
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ตัวขนมถ้วย:**
        - แป้งข้าวเจ้า 65 กรัม
        - แป้งมัน 15 กรัม
        - แป้งท้าวยายม่อม 15 กรัม
        - เกลือ 1/4 ช้อนชา
        - น้ำตาลปี๊บ 120 กรัม
        - น้ำใบเตย 200 กรัม
        - กะทิ 200 กรัม
        
        **หน้ากะทิ:**
        - แป้งข้าวเจ้า 20 กรัม
        - น้ำตาลทราย 30 กรัม
        - เกลือ 1/4 ช้อนชา
        - หัวกะทิ 400 กรัม
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
