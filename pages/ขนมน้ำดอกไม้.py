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
kanom_img_path = os.getenv("COMPONENT_134_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมน้ำดอกไม้: เอกลักษณ์ความอร่อยจากภาคใต้ สูตรเด็ด ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมน้ำดอกไม้: เอกลักษณ์ความอร่อยจากภาคใต้ สูตรเด็ด ความเป็นมา วิธีทำ และส่วนผสม")

st.image(image=kanom_img_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมน้ำดอกไม้ หรือ ขนมชักหน้า เป็นขนมไทยพื้นบ้านจากภาคใต้ ขึ้นชื่อเรื่องความนุ่ม หนึบ หอม หวาน มัน ทานคู่กับชาหรือกาแฟ อร่อยลงตัว มีมานานหลายร้อยปี สันนิษฐานว่ามีต้นกำเนิดมาจากชาวพื้นเมืองภาคใต้ นิยมทำกันในงานมงคลต่างๆ เช่น งานแต่งงาน งานขึ้นบ้านใหม่
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - แป้งมันสำปะหลัง 2 ช้อนโต๊ะ
        - น้ำลอยดอกมะลิ 3/4 ถ้วยตวง (ใช้น้ำเปล่าผสมกลิ่นดอกมะลิแทนได้)
        - น้ำตาลทราย 1/4 ถ้วยตวง
        - สีผสมอาหารสีเขียวและสีชมพู
        - เกลือ 1/4 ช้อนชา
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. ร่อนแป้งข้าวเจ้า แป้งมันสำปะหลัง และเกลือเข้าด้วยกัน
        2. ใส่น้ำตาลทรายลงในน้ำลอยดอกมะลิ คนให้น้ำตาลละลายจนหมด
        3. เทน้ำเชื่อมลงในแป้งโดยแบ่งผสมทีละน้อยจนน้ำเชื่อมหมดและแป้งละลายดีไม่เป็นเม็ด
        4. แบ่งแป้งออกเป็น 2 ส่วน ส่วนหนึ่งหยดสีเขียวลงไป และอีกส่วนหนึ่งหยดสีชมพูลงไป คนให้สีเข้ากับแป้งดีแล้วพักไว้
        5. ตั้งหม้อน้ำ ใส่นึ่ง รอจนน้ำเดือด
        6. นำตะแกรงวางลงบนหม้อนึ่ง ใส่แป้งสีเขียวลงในพิมพ์ นึ่งประมาณ 10 นาที
        7. นำแป้งสีชมพูใส่ในพิมพ์ นึ่งต่อประมาณ 5 นาที
        8. นำขนมออกจากพิมพ์ พักไว้ให้เย็น
        9. ตัดขนมเป็นชิ้นพอดีคำ
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้แป้งข้าวเจ้าที่มีคุณภาพดี จะทำให้เนื้อขนมนุ่ม
        - น้ำลอยดอกมะลิสามารถใช้น้ำเปล่าผสมกลิ่นดอกมะลิแทนได้
        - สีผสมอาหารควรใช้ปริมาณน้อยๆ จะทำให้ขนมมีสีสันสวยงามโดยไม่ฉูดฉาด
        - นึ่งขนมด้วยไฟปานกลาง จะทำให้ขนมสุกทั่ว ไม่สุกดิบ
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
