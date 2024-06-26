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
kanom_img_path = os.getenv("COMPONENT_131_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมเทียนสลัดงา: ขนมไทยโบราณ หอมมัน อร่อย หวานน้อย",
    page_icon="🍡",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมเทียนสลัดงา")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมเทียนสลัดงา เป็นขนมไทยโบราณที่หาทานได้ยาก มีเอกลักษณ์เฉพาะตัวที่โดดเด่นคือ มีแป้งบางใส ห่อไส้ถั่วกวน คลุกงาคั่ว ให้รสสัมผัสที่หอมมัน หวานน้อย กลมกล่อม นิยมทำขึ้นเพื่อเป็นของว่าง หรือใช้ประกอบพิธีกรรมต่างๆ
        ขนมเทียนสลัดงา สันนิษฐานว่ามีต้นกำเนิดมาจากขนมเทียนไส้ถั่วกวน ซึ่งชาวไทยได้นำมารดัดแปลงสูตร โดยเปลี่ยนแป้งจากแป้งข้าวเหนียว เป็นแป้งข้าวเจ้า ทำให้แป้งมีเนื้อสัมผัสที่บางใส และคลุกงาคั่วเพิ่มเติม เพื่อเพิ่มรสชาติและความหอม
        """
    )

st.title("ลักษณะของขนมเทียนสลัดงา")
with st.expander("ลักษณะของขนมเทียนสลัดงา"):
    st.markdown(
        """
        **ลักษณะของขนมเทียนสลัดงา:**
        - มีแป้งบางใส ห่อไส้ถั่วกวน
        - คลุกงาคั่ว ให้สีเหลืองอร่าม
        - มีรสชาติหวานน้อย กลมกล่อม
        - มีกลิ่นหอมงาคั่ว
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมเทียนสลัดงา มีวิธีทำดังนี้:**

        1. **ทำแป้ง:** ผสมแป้งข้าวเจ้า, กะทิ, น้ำตาลทราย, และเกลือ นวดจนแป้งเนียน พักไว้
        2. **ทำไส้:** ตำถั่วเขียวกวน, น้ำตาลทราย, และเกลือ เข้าด้วยกันจนเป็นเนื้อเหนียว
        3. **ห่อขนม:** ปั้นแป้งเป็นก้อนกลม กดแป้งให้แบน ตักไส้ถั่วกวนใส่ตรงกลาง ห่อแป้งให้เป็นรูปวงกลม
        4. **คลุกงา:** คลุกขนมที่ห่อไส้แล้ว กับงาคั่ว
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **แป้ง:**
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - กะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา

        **ไส้:**
        - ถั่วเขียวกวน 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา

        **เพิ่มเติม:**
        - งาคั่ว
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
