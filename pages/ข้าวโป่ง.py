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
kanom_img_path = os.getenv("COMPONENT_36_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวโป่ง: ขนมไทยโบราณ หอม อร่อย น่ารับประทาน",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมข้าวโป่ง: ขนมไทยโบราณ หอม อร่อย น่ารับประทาน")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
       ข้าวโป่ง ขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว ทำจากแป้งข้าวเหนียว นึ่งสุก ตำจนเหนียว นำมาห่อไส้ถั่วลิสงคั่วบด คลุกงาดำ คั่วจนกรอบ ทานคู่กับน้ำชาหรือกาแฟยามเช้า
ประวัติความเป็นมา
ข้าวโป่งมีต้นกำเนิดมาจากภาคอีสานของไทย นิยมทำกันในงานบุญ งานมงคล หรือต้อนรับแขกผู้มาเยือน ในอดีตนั้น ข้าวเป็นอาหารหลักของคนไทย ข้าวโป่งจึงเป็นการแปรรูปข้าวที่เหลือจากมื้ออาหารให้อร่อยและเก็บไว้ทานได้นาน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1.	เตรียมแป้งข้าวเหนียว: แช่ข้าวเหนียวเขี้ยวงู 3-4 ชั่วโมง นึ่งจนสุก
        2.	ตำแป้ง: นำข้าวเหนียวที่นึ่งสุกมาตำจนเหนียว
        3.	เตรียมไส้: คั่วถั่วลิสงจนสุก นำมาตำรวมกับงาดำ เกลือ และน้ำตาลทราย
        4.	ห่อไส้: นำแป้งข้าวเหนียวมาปั้นเป็นแผ่นบางๆ ใส่ไส้ถั่วลิสง คลึงม้วนจนเป็นแท่ง
        5.	หั่นข้าวโป่ง: หั่นข้าวโป่งเป็นชิ้นพอดีคำ
        6.	ทอดข้าวโป่ง: ตั้งน้ำมันให้ร้อน ทอดข้าวโป่งจนเหลืองกรอบ
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
    •   ข้าวเหนียวเขี้ยวงู 500 กรัม
	•	ถั่วลิสงคั่ว 200 กรัม
	•	งาดำ 50 กรัม
	•	เกลือป่น 1/2 ช้อนชา
	•	น้ำตาลทราย 50 กรัม
	•	น้ำมันพืชสำหรับทอด
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        •	สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        •	สามารถเปลี่ยนไส้ถั่วลิสงเป็นไส้หวานอื่นๆ เช่น ไส้เผือก ไส้มันม่วง
        •	ข้าวโป่งสามารถเก็บไว้ทานได้นาน โดยใส่ในภาชนะปิดสนิท
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
