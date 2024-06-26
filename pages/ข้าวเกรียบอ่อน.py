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
kanom_img_path = os.getenv("COMPONENT_25_PATH1")
# component_1_path = os.getenv("COMPONENT_109_PATH2")
# component_2_path = os.getenv("COMPONENT_109_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ข้าวเกรียบอ่อน: ความเป็นเอกลักษณ์ของขนมพื้นบ้านไทย",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวเกรียบอ่อน: ความเป็นเอกลักษณ์ของขนมพื้นบ้านไทย")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ข้าวเกรียบอ่อนเป็นขนมพื้นบ้านของไทยที่มีมานานแล้ว สันนิษฐานว่าน่าจะได้รับอิทธิพลมาจากอาหารของชาวญวนที่อพยพมาตั้งถิ่นฐานในจันทบุรีตั้งแต่สมัยอยุธยาตอนปลาย
        เอกลักษณ์ของข้าวเกรียบอ่อนอยู่ที่แป้งที่นุ่มบาง ไส้ที่หอมหวาน และน้ำจิ้มรสเด็ด
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมแป้ง: ผสมแป้งข้าวเจ้า แป้งมัน แป้งท้าวยายม่อม และน้ำตาลปี๊บกับน้ำเปล่า นวดจนแป้งเนียน พักไว้
        2. เตรียมไส้:
           - ไส้หวาน: มะพร้าวขูด น้ำตาลทราย เกลือ และงาคั่ว
           - ไส้เค็ม: มะพร้าวอ่อน อบเกลือ
        3. นึ่งแป้ง:
           - ตั้งหม้อนึ่งน้ำให้เดือด
           - ทาแป้งบางๆ บนผ้าขาวบางที่ขึงบนปากหม้อ
           - นึ่งจนแป้งสุกใส
        4. ใส่ไส้:
           - วางแป้งที่นึ่งสุกบนใบตอง
           - ใส่ไส้ตามชอบ
           - ม้วนแป้งให้เป็นรูปแท่ง
        5. ห่อใบตอง:
           - ห่อข้าวเกรียบอ่อนด้วยใบตอง
           - มัดด้วยเชือก
        6. นึ่งต่อ:
           - นึ่งข้าวเกรียบอ่อนที่ห่อใบตองอีกครั้งประมาณ 5 นาที
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        แป้ง:
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - แป้งมัน 1 ช้อนโต๊ะ
        - แป้งท้าวยายม่อม 1 ช้อนโต๊ะ
        - น้ำตาลปี๊บ 1/3 ถ้วยตวง
        - น้ำเปล่า 3/4 ถ้วยตวง

        ไส้หวาน:
        - มะพร้าวขูด 2 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - งาคั่ว 1/4 ถ้วยตวง

        ไส้เค็ม:
        - มะพร้าวอ่อน อบเกลือ 2 ถ้วยตวง
        - หอมแดงซอย 1/4 ถ้วยตวง
        - ต้นหอมซอย 1/4 ถ้วยตวง
        - พริกไทยป่น 1/4 ช้อนชา
        - เกลือ 1/4 ช้อนชา

        น้ำจิ้ม:
        - น้ำตาลปี๊บ 1/2 ถ้วยตวง
        - น้ำมะขามเปียก 1/4 ถ้วยตวง
        - น้ำปลา 2 ช้อนโต๊ะ
        - พริกขี้หนูสวนซอย 1/4 ถ้วยตวง
        - ถั่วลิสงคั่วบด 2 ช้อนโต๊ะ
        """
    )

st.title("หมายเหตุ")
with st.expander("หมายเหตุ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - ไส้ข้าวเกรียบอ่อนสามารถดัดแปลงได้หลากหลาย เช่น ไส้เผือก ไส้ถั่วเขียว ฯลฯ
        - น้ำจิ้มข้าวเกรียบอ่อนสามารถปรับรสชาติได้ตามชอบ
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
