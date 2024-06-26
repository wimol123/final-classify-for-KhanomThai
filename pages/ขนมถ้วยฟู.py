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
kanom_img_path = os.getenv("COMPONENT_110_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมถ้วยฟู: ขนมไทยโบราณ ฟู นุ่ม หวานมัน",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมถ้วยฟู")

st.image(kanom_img_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมถ้วยฟู เป็นขนมไทยโบราณที่มีมานานหลายร้อยปี นิยมทำกันในทุกภาคของประเทศไทย แต่ละท้องถิ่นจะมีสูตรและวิธีทำที่แตกต่างกันบ้าง แต่วัตถุดิบหลักๆ จะคล้ายคลึงกัน
        ขนมถ้วยฟู เชื่อกันว่ามีต้นกำเนิดมาจากชาวมอญ แต่เดิมทำด้วยแป้งข้าวเจ้า กะทิ น้ำตาล เกลือ และยีสต์ นำมาผสมกันแล้วเทใส่พิมพ์ นึ่งจนสุก นิยมทานคู่กับชา กาแฟ หรือน้ำอัญชัน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมตัวขนมถ้วยฟู: ผสมแป้งข้าวเจ้า แป้งมัน แป้งท้าวยายม่อม เกลือ น้ำตาลปี๊บ น้ำใบเตย และกะทิ คนจนส่วนผสมเข้ากันดี พักไว้ 2 ชั่วโมง
        2. เตรียมหน้ากะทิ: ผสมแป้งข้าวเจ้า น้ำตาลทราย เกลือ และหัวกะทิ คนจนเข้ากัน
        3. นึ่งขนมถ้วยฟู: ใส่ตัวขนมถ้วยฟูลงในพิมพ์ตะไล นึ่งด้วยไฟปานกลางประมาณ 10 นาที
        4. นึ่งหน้ากะทิ: นำหน้ากะทิมาเทลงบนตัวขนมถ้วยฟู นึ่งต่อด้วยไฟแรงประมาณ 5 นาที หรือจนหน้ากะทิแตกมัน
        5. พักและเสิร์ฟ: รอให้ขนมถ้วยฟูเย็นลง ทานคู่กับชา กาแฟ หรือน้ำอัญชัน
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ตัวขนมถ้วยฟู:**
        - แป้งข้าวเจ้า 80 กรัม
        - แป้งมัน 15 กรัม
        - แป้งท้าวยายม่อม 15 กรัม
        - เกลือ 1/4 ช้อนชา
        - น้ำตาลปี๊บ 120 กรัม
        - น้ำใบเตย 200 กรัม
        - กะทิ 200 กรัม
        - ยีสต์ 1 ช้อนชา
        
        **หน้ากะทิ:**
        - แป้งข้าวเจ้า 20 กรัม
        - น้ำตาลทราย 30 กรัม
        - เกลือ 1/4 ช้อนชา
        - หัวกะทิ 400 กรัม
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
