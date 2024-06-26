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
kanom_img_path = os.getenv("COMPONENT_179_PATH1")
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
# Display main image and title
st.image(image=header_img_path)
st.title("ขนมม้าฮ่อ")
st.image(kanom_img_path)
left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ม้าฮ่อ หรือ ม้าห้อ เป็นอาหารว่างโบราณของไทยชนิดหนึ่ง มีลักษณะเป็นไส้รสหวานเค็ม คล้ายไส้สาคู ทานคู่กับผลไม้รสเปรี้ยวจัด โดยนิยมใช้สับปะรด แต่สามารถใช้ผลไม้เปรี้ยวอื่นๆ เช่น ส้มเขียวหวาน มะยงชิด หรือ กีวี แทนได้

ม้าฮ่อมักนิยมทำในเทศกาลงานบุญ หรือพิธีกรรมสำคัญๆ โดยเฉพาะในชุมชนชาวไทยเชื้อสายมอญ เชื่อกันว่าชาวไทยสมัยก่อนเสียดายผลไม้รสเปรี้ยวที่ทานเปล่าๆ จึงคิดค้นไส้รสหวานเค็มขึ้นมาทานคู่กัน เพื่อเพิ่มรสชาติให้กลมกล่อม

ปัจจุบันม้าฮ่อหาทานได้ยาก
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ตัวผลไม้:
    - สับปะรด 1 ลูก
    - ส้มเขียวหวาน (กรณีไม่มีสับปะรด)
    - มะยงชิด หรือ กีวี (กรณีต้องการรสเปรี้ยวจัด)

    ตัวไส้:
    - หมูสับ 300 กรัม
    - ถั่วลิสงคั่วบด 3 ช้อนโต๊ะ
    - กระเทียมสับ 5 กลีบ
    - รากผักชี 4-5 ราก
    - น้ำมันพืช 40 มล.
    - น้ำตาลปี๊บ ½ ถ้วย
    - น้ำปลา 2 ช้อนโต๊ะ
    - พริกไทยดำเม็ด 1 ช้อนชา
    - ผักชี
    - พริกชี้ฟ้าแดง
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. เตรียมตัวผลไม้:
    - ปอกเปลือกสับปะรด หั่นเป็นชิ้นพอคำ
    - กรณีใช้ส้มเขียวหวาน แกะเปลือก แยกกลีบ ลอกใยส้มออก ผ่ากลีบส้มเป็นสองซีก
    - กรณีใช้มะยงชิด หรือ กีวี ปอกเปลือก หั่นเป็นชิ้นพอคำ

    2. เตรียมตัวไส้:
    - โขลกกระเทียม รากผักชี และพริกไทยดำเข้าด้วยกัน
    - ตั้งกระทะ ใส่น้ำมันพืช ผัดเครื่องแกงที่โขลกไว้จนหอม
    - ใส่หมูสับ ผัดจนหมูสุก
    - ใส่น้ำตาลปี๊บ น้ำปลา และถั่วลิสงคั่วบด ผัดจนส่วนผสมเข้ากันดีและเหนียวข้น
    - ปั้นไส้เป็นก้อนกลมๆ

    3. จัดเสิร์ฟ:
    - วางไส้ม้าฮ่อบนชิ้นสับปะรด ส้มเขียวหวาน มะยงชิด หรือ กีวี
    - ตกแต่งด้วยผักชี และพริกชี้ฟ้าแดงซอย

    เคล็ดลับ:
    - เลือกใช้สับปะรดสุกกำลังดี เนื้อจะกรอบและหวานฉ่ำ
    - ปรุงรสไส้ม้าฮ่อให้กลมกล่อมตามชอบ
    - สามารถเพิ่มกุ้งสับลงในไส้ม้าฮ่อเพื่อเพิ่มรสชาติ
    - หาทานม้าฮ่อสำเร็จรูปได้ยาก อาจลองทำทานเองตามสูตร
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
