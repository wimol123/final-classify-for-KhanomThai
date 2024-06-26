from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
header_img_path = os.getenv("HEADER_IMG_PATH")
khanomborapet_path = os.getenv("COMPONENT_139_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมบอระเพ็ด: ขนมพื้นเมืองภาคใต้",
    page_icon="🍘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมบอระเพ็ด: ขนมพื้นเมืองภาคใต้")
st.image(image=khanomborapet_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมบอระเพ็ด หรือ ขนมปะการัง เป็นขนมพื้นเมืองภาคใต้ที่มีเอกลักษณ์เฉพาะตัว โดดเด่นด้วยรูปลักษณ์ที่คล้ายปะการัง รสชาติหอม หวาน มัน กรอบ นิยมทานคู่กับชา กาแฟ หรือน้ำอัญชัน
        ขนมบอระเพ็ดมีต้นกำเนิดจากทางภาคใต้ของประเทศไทย โดยเฉพาะในจังหวัดนราธิวาส เชื่อกันว่าได้รับอิทธิพลมาจากวัฒนธรรมอาหารของชาวมลายู ในอดีตนิยมทำและขายตามงานวัด งานประจำปี หรือตามท้องถนน ปัจจุบันหาซื้อได้ยากขึ้น แต่ยังพอมีบางร้านที่ทำและขายอยู่
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        การทำขนมบอระเพ็ดนั้น ต้องอาศัยทั้งฝีมือและความประณีต โดยขั้นตอนคร่าวๆ ดังนี้:
        1. เตรียมแป้ง: นำแป้งข้าวเหนียว น้ำตาล เกลือ ไข่ไก่ และกะทิ มาผสมให้เข้ากัน นวดจนแป้งเนียนและไม่ติดมือ
        2. ปั้นขนม: แบ่งแป้งเป็นก้อนกลม นำไปคลุกกับงาดำ
        3. ทอดขนม: ตั้งกระทะใส่น้ำมัน รอจนร้อน นำแป้งที่คลุกงาดำลงทอดจนสุกเหลืองกรอบ
        4. พักขนม: เมื่อขนมสุก นำขึ้นจากกระทะ วางพักบนตะแกรง รอให้สะเด็ดน้ำมัน
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - แป้งข้าวเหนียว
        - น้ำตาล
        - เกลือ
        - ไข่ไก่
        - กะทิ
        - งาดำ
        - น้ำมัน
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - แป้งข้าวเหนียวควรเป็นแป้งข้าวเหนียวใหม่
        - น้ำตาลและเกลือสามารถปรับปริมาณได้ตามชอบ
        - กะทิควรเป็นกะทิสด
        - ควรทอดขนมด้วยไฟอ่อนๆ
        - งาดำสามารถคั่วก่อนนำมาคลุกกับแป้งก็ได้
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
