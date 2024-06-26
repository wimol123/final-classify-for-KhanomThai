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
kanom_img_path = os.getenv("COMPONENT_166_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมฟักเขียวกวน")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมฟักเขียวกวน เป็นขนมไทยโบราณที่ขึ้นชื่อเรื่องความหอม หวาน มัน กลมกล่อม ทานคู่กับอะไรก็อร่อย ขนมชนิดนี้มีมานานหลายร้อยปี สันนิษฐานว่ามีต้นกำเนิดมาจากชาววัง ในสมัยก่อนนั้นนิยมทำในงานมงคลต่างๆ เช่น งานแต่งงาน งานขึ้นบ้านใหม่
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วิธีทำ:**

        1. **เตรียมฟักเขียว:**
           - ปอกฟักเขียว หั่นตามยาวและคว้านเอาเม็ดออก ขูดเนื้อฟักให้เป็นเส้นฝอย
           - บีบน้ำฟักออกให้พอหมาดๆ

        2. **ผสมส่วนผสม:**
           - ผสมฟักเขียวขูด, น้ำตาลปี๊บ, เกลือ และกะทิ คลุกเคล้าให้เข้ากัน

        3. **ทำขนมฟักเขียวกวน:**
           - ตั้งกระทะ ใส่ส่วนผสมที่เตรียมไว้ลงไป กวนด้วยไฟอ่อนจนเนื้อฟักข้นเหนียว
           - ใส่เนื้อมะพร้าวขูด กวนต่อจนเข้ากัน

        4. **การตัดและพัก:**
           - ตักขนมฟักเขียวกวนใส่ถาด พักไว้ให้เย็น
           - ตัดขนมฟักเขียวกวนเป็นชิ้นพอดีคำ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ส่วนผสม:**
        - ฟักเขียวแก่ 2 กิโลกรัม
        - น้ำตาลปี๊บ 1 กิโลกรัม
        - กะทิ 400 มิลลิลิตร
        - เกลือ 1/2 ช้อนชา
        - มะพร้าวขูด 100 กรัม
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้ฟักเขียวแก่ จะทำให้เนื้อขนมฟักเขียวกวนมีสีเข้มและรสชาติหอมหวาน
        - บีบน้ำฟักออกให้พอหมาดๆ จะทำให้ขนมฟักเขียวกวนไม่แฉะ
        - กวนด้วยไฟอ่อน จะทำให้เนื้อขนมฟักเขียวกวนเนียน ไม่กระด้าง
        - ใส่เนื้อมะพร้าวขูด จะทำให้ขนมฟักเขียวกวนมีรสชาติหอมมัน
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
