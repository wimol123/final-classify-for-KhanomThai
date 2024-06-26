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
kanom_img_path = os.getenv("COMPONENT_35_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวตู: เอกลักษณ์ความอร่อย หอมหวาน ชวนลิ้มลอง",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวตู: เอกลักษณ์ความอร่อย หอมหวาน ชวนลิ้มลอง")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
        ข้าวตูมีต้นกำเนิดมาจากภาคกลางของไทย นิยมทำกันในงานมงคลหรือต้อนรับแขกผู้มาเยือน ในอดีตนั้นข้าวเป็นอาหารหลักของคนไทย ข้าวตูจึงเป็นการแปรรูปข้าวที่เหลือจากมื้ออาหารให้อร่อยและเก็บไว้ทานได้นาน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมข้าวเหนียว: แช่ข้าวเหนียวเขี้ยวงู 3-4 ชั่วโมง นึ่งจนสุก
        2. คั่วข้าวเหนียว: นำข้าวเหนียวที่นึ่งสุกไปคั่วไฟอ่อนจนเหลืองหอม
        3. ตำข้าวเหนียว: นำข้าวเหนียวคั่วที่เย็นแล้วมาตำจนละเอียด
        4. ผสมกะทิ: ผสมกะทิ น้ำตาลปี๊บ เกลือ และใบเตย ต้มจนน้ำตาลละลาย
        5. คลุกข้าวเหนียว: ใส่ข้าวเหนียวตำลงในกะทิที่ต้มไว้ คลุกเคล้าจนเข้ากันดี
        6. ปั้นข้าวตู: ปั้นข้าวเหนียวที่คลุกกะทิเป็นก้อนกลมๆ
        7. อบควันเทียน: เรียงข้าวตูในหม้อ นำเทียนหอมมาวางไว้จุดไฟ อบควันเทียนจนหอม
        8. พักและพร้อมทาน: นำข้าวตูออกจากหม้อ พักให้เย็น
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - ข้าวเหนียวเขี้ยวงู 500 กรัม
        - กะทิ 200 มล.
        - น้ำตาลปี๊บ 100 กรัม
        - เกลือป่น 1/2 ช้อนชา
        - ใบเตย 2-3 ใบ
        - เทียนหอม 1 แท่ง
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - สามารถเปลี่ยนกะทิเป็นน้ำเปล่าได้
        - ข้าวตูสามารถเก็บไว้ทานได้นาน โดยใส่ในภาชนะปิดสนิท
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
