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
kanom_img_path = os.getenv("COMPONENT_232_PATH1")
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
st.title("ขนมอาลัว")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมอาลัว เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว ด้วยรูปลักษณ์ที่ด้านนอกจะแข็ง ด้านในจะนุ่ม มีหลากหลายสีสัน ชวนน่ารับประทาน รสชาติหวานมัน กลมกล่อม นิยมทำทานคู่กับน้ำชา หรือกาแฟ
        ในอดีต ขนมอาลัว มีต้นกำเนิดมาจากโปรตุเกส เข้ามาในไทยในสมัยกรุงศรีอยุธยา โดยฝรั่งที่เข้ามาค้าขาย นิยมทำในงานมงคลต่างๆ เพราะมีความหมายมงคล สื่อถึงความเจริญรุ่งเรือง โชคลาภ และความร่ำรวย
        """
    )

st.title("ประเภทของขนมอาลัว")
with st.expander("ประเภทของขนมอาลัว"):
    st.markdown(
        """
        **ขนมอาลัว สามารถจำแนกประเภทได้ดังนี้**

        - **อาลัวชาววัง:** มีขนาดใหญ่ สีเหลือง เนื้อนุ่ม หอมมัน นิยมทำในงานสำคัญๆ ของราชสำนัก
        - **อาลัวจิ๋ว:** มีขนาดเล็ก หลากหลายสีสัน เนื้อสัมผัสนุ่ม หนึบ หาซื้อได้ทั่วไป
        - **อาลัวทอด:** นำอาลัวไปทอดจนเหลืองกรอบ ทานคู่กับน้ำเชื่อม
        """
    )

st.title("วิธีทำขนมอาลัว")
with st.expander("วิธีทำขนมอาลัว"):
    st.markdown(
        """
        **วัตถุดิบ:**

        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - กะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1 ถ้วยตวง
        - น้ำเปล่า 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - สีผสมอาหาร (ตามชอบ)

        **วิธีทำ:**

        1. ผสมแป้งข้าวเจ้า กะทิ น้ำตาลทราย น้ำเปล่า เกลือ และสีผสมอาหาร คนให้เข้ากันจนเนียน
        2. เทส่วนผสมลงในพิมพ์ นำไปนึ่งจนสุก
        3. พักให้เย็น หั่นเป็นชิ้นพอดีคำ

        **เคล็ดลับ:**
        - เลือกใช้แป้งข้าวเจ้าที่มีคุณภาพดี จะได้เนื้อสัมผัสที่เนียน
        - ปรับความหวานของขนมตามชอบ
        - ทานคู่กับน้ำชา หรือกาแฟ
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
