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
kanom_img_path = os.getenv("COMPONENT_18_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมไทยอะไรเอ่ย??",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display main image and title
st.image(image=header_img_path)
st.title("กะละแม")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
กะละแม ขนมไทยโบราณที่นิยมทำกันในช่วงเทศกาลสงกรานต์ มีลักษณะเป็นแท่งสีดำ เหนียวนุ่ม หอมหวานมัน 
กินคู่กับมะพร้าวขูด นิยมใช้เป็นของไหว้บรรพบุรุษ แบ่งปันเพื่อนบ้าน และใช้ในงานมงคลต่างๆ
ยังไม่มีหลักฐานแน่ชัดว่ากะละแมมีที่มาจากไหน แต่มีหลายทฤษฎีที่สันนิษฐานไว้ เช่น

ขนมจากมอญและพม่า: ราชาธิบายใน "สํานักงานราชบัณฑิตยสภา" สันนิษฐานว่า กะละแมมาจากขนมมอญและพม่า เรียกว่า "กฺวายฺนกลาแม" (อ่านว่า กฺวาน-กะ-ลา-แม)

ขนมจากตะวันตก: พุทธทาสภิกขุ สันนิษฐานว่า กะละแมมาจากขนมฮูละวะของอินเดียที่มีส่วนผสมเป็นนม แป้ง และน้ำตาล

ขนมพื้นเมืองภาคใต้: ทางภาคใต้มีขนมคล้ายกะละแมเรียกว่า "ขนมโดดอล" ใช้ในพิธีการต่างๆ


"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ข้าวเหนียว 1 กิโลกรัม
    
    กะทิ 1 กิโลกรัม
    
    น้ำตาลปี๊บ 1 กิโลกรัม

    เกลือ 1 ช้อนชา

"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ล้างข้าวเหนียวแล้วแช่น้ำไว้ 3-4 ชั่วโมง
    2. นำข้าวเหนียวที่แช่ไว้ไปนึ่งจนสุก
    3. ละลายน้ำตาลปี๊บกับน้ำเปล่า 1 ถ้วยตวง
    4. ตั้งกระทะ ใส่น้ำกะทิ เกลือ และน้ำตาลปี๊บที่ละลายไว้
    5. พอน้ำเดือด ใส่ข้าวเหนียวที่นึ่งสุกแล้วลงไปกวน
    6. กวนจนข้าวเหนียวเริ่มละลาย เติมน้ำกะทิลงไปทีละน้อย กวนต่อจนเนื้อเหนียวข้น
    7. เทกะละแมลงพิมพ์ที่รองด้วยใบตอง
    8. พักให้กะละแมเย็นและแข็งตัว
    9. ตัดกะละแมเป็นชิ้นพอดีคำ
    
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
