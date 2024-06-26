# This is a placeholder for ขนมหยกมณี.py
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
kanom_img_path = os.getenv("COMPONENT_222_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมหยกมณี",
    page_icon="🍡",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title and sections
st.title("ขนมหยกมณี")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมหยกมณี เป็นขนมไทยโบราณชนิดหนึ่งที่มีเอกลักษณ์เฉพาะตัวด้วยสีเขียวใสจากใบเตย คล้ายกับหยกมณีมีสีเขียวและเปล่งประกายเมื่อส่องแสง ขนมชนิดนี้มักนิยมนำมาทานคู่กับมะพร้าวขูดฝอย หวานมัน กลมกล่อม ละมุนลิ้น

        ในอดีต หยกมณีถือเป็นขนมที่นิยมเสิร์ฟในงานมงคลต่างๆ โดยเฉพาะในหมู่ชนชั้นสูง เชื่อกันว่าขนมชนิดนี้สื่อถึงความเจริญรุ่งเรือง โชคลาภ และความร่ำรวย ด้วยรูปลักษณ์ที่สวยงาม สีสันสดใส และรสชาติที่อร่อย หยกมณีจึงกลายเป็นหนึ่งในขนมไทยที่ได้รับความนิยมมาอย่างยาวนาน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**

        **ส่วนผสม:**
        - สาคูเม็ดเล็ก 1 ถ้วยตวง
        - น้ำใบเตย 1 ถ้วยตวง
        - น้ำเปล่า (สำหรับต้มสาคู) 1 ½ ถ้วยตวง
        - น้ำตาลทราย 1 ถ้วยตวง
        - มะพร้าวทึนทึกขูดฝอย 1 ถ้วยตวง
        - เกลือป่น ½ ช้อนชา

        **วิธีทำ:**
        1. ล้างสาคูให้สะอาด และพักไว้ให้สะเด็ดน้ำ
        2. นำมะพร้าวขูดฝอยไปคลุกกับเกลือ และนึ่งจนสุก พักไว้
        3. ต้มน้ำเปล่าใส่น้ำใบเตย และเมื่อเดือด ใส่สาคูลงไป คนเรื่อยๆ จนสาคูใส
        4. ใส่น้ำตาลทรายลงไป คนจนละลาย
        5. ตักหยกมณีใส่พิมพ์ และรอให้เย็น
        6. โรยมะพร้าวขูดฝอยทันทีหลังจากหยกมณีเย็น จะได้เกาะติดกันดี

        **เคล็ดลับ:**
        - เลือกใช้ใบเตยใบอ่อน เพื่อให้ได้สีเขียวที่สวยงาม
        - ต้มสาคูด้วยไฟอ่อน และคนเรื่อยๆ เพื่อไม่ให้สาคูก้นกระทะ
        - ปรับความหวานตามชอบ
        - โรยมะพร้าวขูดฝอยทันทีหลังจากหยกมณีเย็น เพื่อให้เกาะติดกันได้ดีขึ้น
        """
    )

# Link back to Home.py
st.page_link("Home.py", label="Home", icon="↩️")
