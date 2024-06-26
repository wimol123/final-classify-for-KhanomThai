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
kanom_img_path = os.getenv("COMPONENT_230_PATH1")
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
st.title("ขนมอาเกาะ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมอาเกาะ หรือ เม็ดมะม่วงหิมพานต์ผัดน้ำตาลโตนด เป็นขนมพื้นบ้านจากภาคใต้ โดยเฉพาะจังหวัดพัทลุง มีเอกลักษณ์เฉพาะตัวด้วยเม็ดมะม่วงหิมพานต์เคลือบด้วยน้ำตาลโตนด รสชาติหวานมัน กรอบ อร่อย
        ในอดีต ขนมอาเกาะ นิยมทำทานคู่กับน้ำชา หรือกาแฟ เป็นของว่างทานเล่น หรือมอบเป็นของฝาก ด้วยความที่หาซื้อได้ยาก จึงกลายเป็นขนมที่มีเอกลักษณ์ และเป็นที่นิยมของนักท่องเที่ยว
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ส่วนผสม:**

        - เม็ดมะม่วงหิมพานต์ 1 ถ้วยตวง
        - น้ำตาลโตนด 1 ถ้วยตวง
        - เกลือ 1/2 ช้อนชา

        **วิธีทำ:**

        1. ตั้งกระทะใส่น้ำตาลโตนด เคี่ยวจนละลายและเหนียวข้น
        2. ใส่เม็ดมะม่วงหิมพานต์ เกลือ คนให้เข้ากัน
        3. เทส่วนผสมลงบนถาด เกลี่ยให้เรียบ
        4. พักให้เย็น ตัดเป็นชิ้นพอดีคำ

        **เคล็ดลับ:**

        - เลือกใช้เม็ดมะม่วงหิมพานต์ใหม่ จะได้รสชาติอร่อย
        - เคี่ยวน้ำตาลโตนดด้วยไฟอ่อน ระวังไม่ให้น้ำตาลไหม้
        - ปรับความหวานของขนมตามชอบ
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
