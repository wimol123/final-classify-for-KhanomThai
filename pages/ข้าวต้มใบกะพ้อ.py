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
kanom_img_path = os.getenv("COMPONENT_32_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวต้มใบกะพ้อ: เอกลักษณ์ความอร่อยจากภูมิปัญญาไทยภาคใต้",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวต้มใบกะพ้อ: เอกลักษณ์ความอร่อยจากภูมิปัญญาไทยภาคใต้")
st.image(kanom_img_path)
st.title("ประวัติความเป็นมา")
with st.expander("ประวัติความเป็นมา"):
    st.markdown(
        """
        ขนมข้าวต้มใบกะพ้อเป็นขนมพื้นบ้านของชาวไทยภาคใต้ที่มีเอกลักษณ์เฉพาะตัว โดดเด่นด้วยกรรมวิธีการทำที่เรียบง่าย ผสมผสานวัตถุดิบท้องถิ่นเข้าด้วยกันจนกลายเป็นเมนูทานเล่นแสนอร่อยที่ได้รับความนิยมมาอย่างยาวนาน
        """
    )

st.title("เอกลักษณ์ของขนมข้าวต้มใบกะพ้อ")
with st.expander("เอกลักษณ์ของขนมข้าวต้มใบกะพ้อ"):
    st.markdown(
        """
        - **กลิ่นหอม:** ขนมข้าวต้มใบกะพ้อมีกลิ่นหอมเป็นเอกลักษณ์จากใบกะพ้อ
        - **รสชาติกลมกล่อม:** หวานมันเค็ม จากข้าวเหนียว กะทิ ถั่วดำ และน้ำตาล
        - **ความสวยงาม:** ขนมข้าวต้มใบกะพ้อมีสีสันสวยงาม จากใบกะพ้อสีเขียว ข้าวเหนียวสีขาว และถั่วดำสีดำ
        - **ความหมายดีงาม:** สื่อถึงความสามัคคี ความเจริญรุ่งเรือง และโชคลาภ
        """
    )

st.title("ส่วนผสมและวิธีทำ")
with st.expander("ส่วนผสมและวิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**
        - ข้าวเหนียวเขี้ยวงู 1 ถ้วย
        - กะทิ 1 กล่อง
        - ใบกะพ้อสำหรับห่อ
        - น้ำตาลทราย
        - เกลือ
        - น้ำเปล่า

        **วิธีทำ:**
        1. แช่ข้าวเหนียวเขี้ยวงูกับน้ำเปล่าประมาณ 3-4 ชั่วโมง
        2. เตรียมใบกะพ้อโดยคลี่ซ้อนกันเป็นเซ็ท ๆ แล้วพับเป็นรูปสามเหลี่ยม
        3. ผสมกะทิกับน้ำเปล่า เกลือ และน้ำตาลทราย ตั้งไฟเคี่ยวจนน้ำตาลทรายละลาย
        4. ตักข้าวเหนียวที่แช่ไว้ใส่ลงในใบกะพ้อ อัดให้แน่น
        5. ตั้งน้ำให้เดือด นำขนมข้าวต้มใบกะพ้อที่ห่อไว้ไปต้มประมาณ 45-60 นาที หรือจนกว่าข้าวเหนียวจะสุก
        6. ตักขนมข้าวต้มใบกะพ้อที่ต้มสุกแล้วออกมาพักให้สะเด็ดน้ำ
        7. แกะใบกะพ้อออก ราดด้วยน้ำเชื่อม ทานคู่กับน้ำแข็ง
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้ใบกะพ้ออ่อน จะทำให้ห่อขนมง่าย และขนมมีสีสวย
        - มัดใบกะพ้อให้แน่น เพื่อป้องกันไม่ให้น้ำไหลเข้าไปในตัวขนม
        - ปรับปริมาณน้ำตาลทรายได้ตามชอบ
        """
    )

st.title("การเก็บรักษา")
with st.expander("การเก็บรักษา"):
    st.markdown(
        """
        ขนมข้าวต้มใบกะพ้อสามารถเก็บไว้ทานได้นาน 1-2 วัน โดยใส่ในภาชนะปิดฝาสนิท เก็บไว้ในตู้เย็น
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
