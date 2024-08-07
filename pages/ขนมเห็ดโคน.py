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
kanom_img_path = os.getenv("COMPONENT_229_PATH1")
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
st.title("ขนมเห็ดโคน")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเห็ดโคน หรือที่หลายๆคนน่าจะรู้จักกันในชื่อ เมอแรงค์เห็ด เป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัวด้วยรูปร่างที่คล้ายเห็ดโคน สีขาวนวล รสชาติหวานมัน ละมุนลิ้น นิยมทำทานคู่กับน้ำชา หรือกาแฟ
        ขนมเห็ดโคน มีต้นกำเนิดมาจากทางภาคใต้ของไทย เชื่อกันว่าได้รับอิทธิพลมาจากอาหารฝรั่งเศส ในอดีต นิยมทำในงานมงคลต่างๆ เพราะมีความหมายมงคล สื่อถึงความเจริญรุ่งเรือง โชคลาภ และความร่ำรวย
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ส่วนผสม:**

        - ไข่ขาว 3 ฟอง
        - น้ำตาลทราย 90 กรัม
        - น้ำมะนาว 1/2 ช้อนชา
        - แป้งท้าวยายม่อม 1 ช้อนโต๊ะ
        - แป้งสาลี 1 ช้อนโต๊ะ (ตราบัวแดง)
        - ผงโกโก้ สำหรับโรย
        - แป้งสาลีบัวแดงคั่วสำหรับโรย
        - น้ำเชื่อม

        **วิธีทำ:**

        1. ตีไข่ขาวจนตั้งยอดอ่อน ใส่น้ำมะนาวลงไปตีต่อจนตั้งยอด
        2. ทยอยใส่น้ำตาลทรายลงตีจนตั้งยอดแข็ง
        3. แบ่งส่วนผสมที่ได้เป็น 2 ส่วน
        4. ส่วนที่ 1 นำมาทำก้านเห็ด ให้นำแป้งท้าวยายม่อมมาคนผสมให้เข้ากัน ตักใส่ถุงแล้วบีบใส่ถาด ให้มีลักษณะเป็นแท่งสูงเหมือนก้านเห็ด
        5. ส่วนที่ 2 ใส่แป้งสาลี คนให้เข้ากัน ตักส่วนผสมใส่ถุงบีบ บีบเป็นรูปดอกเห็ด พักไว้
        6. อบไฟ 100 องศา 1 ชั่วโมง หรือจนสุก
        7. พักให้เย็น โรยผงโกโก้ และแป้งสาลีคั่ว
        8. ราดด้วยน้ำเชื่อม

        **เคล็ดลับ:**

        - เลือกใช้ไข่ขาวสดใหม่ จะได้ตีฟูง่าย
        - ตีไข่ขาวด้วยความเร็วปานกลาง ระวังไม่ให้ไข่ขาวแตก
        - อบไฟด้วยอุณหภูมิที่ต่ำ จะได้เนื้อขนมที่กรอบนอกนุ่มใน
        - ปรับความหวานของน้ำเชื่อมตามชอบ
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
