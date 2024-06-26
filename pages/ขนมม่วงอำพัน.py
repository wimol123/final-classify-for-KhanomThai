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
kanom_img_path = os.getenv("COMPONENT_170_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title and sections
st.title("ขนมม่วงอำพัน")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมม่วงอำพัน เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในงานมงคลต่างๆ โดยมีลักษณะคล้ายดอกไม้สีม่วงอ่อนๆ เชื่อกันว่าขนมม่วงอำพันนั้น สื่อถึงความเจริญรุ่งเรือง
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วิธีทำ:**

        1. **เตรียมไส้มันม่วง:**
           - นำมันม่วงมาต้มหรือนึ่งจนสุก
           - บดมันม่วงให้ละเอียด
           - ใส่กะทิ, น้ำตาลทราย, เกลือ, และใบเตยลงไปผสม
           - ตั้งไฟอ่อน คนเรื่อยๆ จนข้นเหนียว
           - เทส่วนผสมที่ข้นเหนียวลงพิมพ์ พักไว้ให้เย็นและแข็งตัว

        2. **เตรียมตัวแป้ง:**
           - ผสมแป้งข้าวเจ้า, แป้งมัน, เกลือ, และน้ำ
           - นวดจนแป้งเนียน

        3. **ห่อไส้:**
           - แบ่งแป้งเป็นก้อนกลมๆ
           - กดแป้งให้แบนบาง
           - ตักไส้มันม่วงที่เตรียมไว้ใส่ตรงกลาง
           - ห่อแป้งให้มิดชิด

        4. **นึ่ง:**
           - ตั้งน้ำในหม้อให้น้ำเดือด
           - นำขนมม่วงอำพันที่ห่อไว้ไปนึ่งจนสุกหรือจนแป้งใส

        5. **เสิร์ฟ:**
           - ตักขนมม่วงอำพันใส่จาน
           - ราดด้วยกะทิ
           - โรยหน้าด้วยเกลือเล็กน้อย
           - เสิร์ฟร้อนๆ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **ส่วนผสมสำหรับไส้มันม่วง:**
        - มันม่วง 500 กรัม
        - กะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - ใบเตย 2-3 ใบ

        **ส่วนผสมสำหรับตัวแป้ง:**
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - แป้งมัน 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - น้ำเปล่า
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณของส่วนผสมได้ตามชอบ
        - สามารถเพิ่มรสชาติให้กับไส้มันม่วงได้ด้วยการใส่กลิ่นมะลิ หรือ pandan leaves
        - แป้งควรนวดจนเนียน จะได้ไม่ติดมือ
        - นึ่งขนมด้วยไฟปานกลาง จะได้แป้งที่สุกทั่ว
        - ราดกะทิบนขนมม่วงอำพันตอนร้อนๆ จะได้กะทิซึมเข้าเนื้อ
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
