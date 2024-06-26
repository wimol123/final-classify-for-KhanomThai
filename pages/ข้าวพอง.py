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
kanom_img_path = os.getenv("COMPONENT_37_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวพอง: ขนมไทยโบราณ กรอบ อร่อย หอมมัน",
    page_icon="🍘",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวพอง: ขนมไทยโบราณ กรอบ อร่อย หอมมัน")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
        ข้าวพองมีต้นกำเนิดมาจากภาคเหนือของไทย นิยมทำกันในงานบุญ งานมงคล หรือต้อนรับแขกผู้มาเยือน ในอดีตนั้น ข้าวเหนียวเป็นอาหารหลักของคนไทย ข้าวพองจึงเป็นการแปรรูปข้าวที่เหลือจากมื้ออาหารให้อร่อยและเก็บไว้ทานได้นาน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมข้าวเหนียว: แช่ข้าวเหนียวเขี้ยวงู 3-4 ชั่วโมง นึ่งจนสุก
        2. ตำข้าวเหนียว: นำข้าวเหนียวที่นึ่งสุกมาตำจนละเอียด
        3. คลุกข้าวเหนียว: ใส่เกลือ น้ำตาลทราย และงาดำ คลุกเคล้ากับข้าวเหนียวที่ตำไว้
        4. นึ่งข้าวเหนียว: ใส่ข้าวเหนียวที่คลุกไว้ลงในพิมพ์ นึ่งจนสุก
        5. ตากแดด: นำข้าวเหนียวที่นึ่งสุกมาตากแดดจนแห้ง
        6. ทอดข้าวพอง: ตั้งน้ำมันให้ร้อน ทอดข้าวเหนียวที่ตากแดดจนพองกรอบ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ข้าวเหนียวเขี้ยวงู 500 กรัม
        - เกลือป่น 1/2 ช้อนชา
        - น้ำตาลทราย 50 กรัม
        - งาดำ 50 กรัม
        - น้ำมันพืชสำหรับทอด
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - สามารถเพิ่มรสชาติอื่นๆ ให้กับข้าวพอง เช่น รสเผ็ด รสหวาน
        - ข้าวพองสามารถเก็บไว้ทานได้นาน โดยใส่ในภาชนะปิดสนิท
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
