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
khanombanduk_path = os.getenv("COMPONENT_144_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมบันดุก: ขนมไทยโบราณ มงคลความเชื่อ และสูตรทำขนมบันดุกแบบดั้งเดิม",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("ขนมบันดุก: ขนมไทยโบราณ มงคลความเชื่อ และสูตรทำขนมบันดุกแบบดั้งเดิม")
st.image(image=khanombanduk_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมบันดุก หรือ มันดุก เป็นขนมไทยโบราณพื้นเมืองภาคใต้ โดดเด่นด้วยรูปลักษณ์ที่คล้ายปั้นดินสอ รสชาติหอม หวาน มัน กรอบ นิยมทานคู่กับชา กาแฟ หรือน้ำอัญชัน
        ขนมบันดุก มีต้นกำเนิดมาจากทางภาคใต้ของประเทศไทย สันนิษฐานว่าได้รับอิทธิพลมาจากวัฒนธรรมอาหารของชาวญวนที่อพยพเข้ามาอาศัยอยู่ในพื้นที่จังหวัดตราด ในอดีตนิยมทำและขายตามงานวัด งานประจำปี หรือตามท้องถนน ปัจจุบันหาซื้อได้ยากขึ้น แต่ยังพอมีบางร้านในจังหวัดตราดที่ทำและขายอยู่
        """
    )

st.title("ความเชื่อ")
with st.expander("ความเชื่อ"):
    st.markdown(
        """
        - รูปร่างของขนมบันดุก: เปรียบเสมือนแท่งทองคำ สื่อถึงโชคลาภ เงินทอง ความมั่งคั่ง
        - สีของขนมบันดุก:
            - สีเขียว: สื่อถึงธรรมชาติ ความเจริญงอกงาม
            - สีขาว: สื่อถึงความบริสุทธิ์ ความสะอาด
        - การทานขนมบันดุก: เชื่อกันว่าจะช่วยให้ชีวิตราบรื่น แคล้วคลาดปลอดภัย ประสบความสำเร็จในสิ่งที่มุ่งหวัง
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        ### ส่วนผสม:
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - แป้งมันสำปะหลัง 1/2 ถ้วยตวง
        - น้ำใบเตย 1 ถ้วยตวง
        - น้ำเปล่า 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - กะทิ 1 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - ถั่วลิสงคั่วบด 1/2 ถ้วยตวง
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        ### ตัวแป้งสีเขียว:
        1. ผสมแป้งข้าวเจ้า แป้งมันสำปะหลัง น้ำใบเตย น้ำเปล่า และเกลือ คนให้เข้ากัน พักไว้ 30 นาที
        2. เทแป้งที่ผสมไว้ ลงในพิมพ์ นึ่งด้วยไฟปานกลาง ประมาณ 10-15 นาที จนแป้งสุก

        ### ตัวแป้งสีขาว:
        1. ผสมแป้งข้าวเจ้า แป้งมันสำปะหลัง กะทิ น้ำเปล่า และเกลือ คนให้เข้ากัน พักไว้ 30 นาที
        2. เทแป้งที่ผสมไว้ ลงในพิมพ์ นึ่งด้วยไฟปานกลาง ประมาณ 10-15 นาที จนแป้งสุก

        ### การประกอบ:
        1. ตัดแป้งสีเขียวและสีขาว เป็นแท่งยาว
        2. โรยถั่วลิสงคั่วบด บนแป้งทั้งสองสี
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - แป้งข้าวเจ้าควรเป็นแป้งข้าวเจ้าใหม่
        - น้ำใบเตย ควรใช้ใบเตยสด หรือใบเตยอบแห้ง
        - กะทิควรเป็นกะทิสด
        - ถั่วลิสงคั่วบด ควรคั่วถั่วลิสงเอง จะได้ความหอม อร่อย
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
