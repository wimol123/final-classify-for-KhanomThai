import streamlit as st
from PIL import Image
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
head_img = os.getenv("HEADER_IMG_PATH")
img1 = os.getenv("BACKGROUND_IMAGE_PATH")
img2 = os.getenv("COMPONENT_2-1_PATH")
img3 = os.getenv("COMPONENT_2-2_PATH")
# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=head_img)
st.title("ขนมกรวย")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=img1, width=500)


multi = """
        ขนมกรวยหรือ ขนมหางจิ้งจก นั้น เป็นขนมหวานชนิดหนึ่ง ที่ชาวไทยพุทธ และมุสลิม นิยมทํารับประทานกันมากในสมัยก่อน ปัจจุบันหาทานได้ยาก มีแป้งข้าวเจ้าเป็นส่วนผสม บรรจุกรวยใบตอง นำไปนึ่งให้สุก ทานง่าย ในอดีตนิยมป้อนเด็กทารก เนื่องจากเนื้อขนมนิ่ม รับประทานง่าย บรรจุอยู่ในกรวย จึงเรียกว่า ขนมกรวย
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    st.image(image=img2)

with col2:
    st.header("วิธีทำ")
    st.image(image=img3)

st.page_link("Home.py", label="Home", icon="↩️")
