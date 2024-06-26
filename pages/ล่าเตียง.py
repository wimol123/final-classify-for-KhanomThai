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
khanomla_img_path = os.getenv("COMPONENT_190_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมล่าเตียง: มรดกความอร่อยจากรัชกาลที่ 2",
    page_icon="🍮",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display main image and title
st.title("ล่าเตียง")

st.title(image=khanomla_img_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมล่าเตียงเป็นขนมไทยโบราณที่มีเอกลักษณ์เฉพาะตัว ขึ้นชื่อเรื่องความประณีต รสชาติกลมกล่อม หอมหวาน และหน้าตาที่สวยงาม สันนิษฐานว่ามีต้นกำเนิดมาตั้งแต่สมัยรัชกาลที่ 2 โดยปรากฏชื่ออยู่ในกาพย์เห่ชมเครื่องคาวหวาน ล่าเตียงเป็นอาหารว่างที่นิยมเสิร์ฟในงานมงคลต่างๆ เช่น งานแต่งงาน งานขึ้นบ้านใหม่ หรือแม้กระทั่งงานศพ โดยเชื่อกันว่าล่าเตียงมีลักษณะคล้ายกับ "ข่าย" ที่ใช้ดักวิญญาณ สื่อถึงการส่งวิญญาณของผู้ล่วงลับไปสู่สุคติ
    """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - แป้งข้าวเจ้า
        - แป้งข้าวเหนียว
        - ไข่ไก่
        - กุ้งสับ
        - หมูสับ
        - ถั่วลิสงคั่วบด
        - หอมใหญ่สับ
        - ผักชี
        - พริกชี้ฟ้าแดง
        - น้ำปลา
        - น้ำตาลปี๊บ
        - เกลือ
        - น้ำมันพืช
    """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. ผสมแป้งข้าวเจ้า แป้งข้าวเหนียว เกลือ และน้ำเปล่า นวดจนเนื้อเนียน
        2. ตั้งกระทะ ใส่น้ำมัน นำแป้งที่นวดไว้ ตักใส่กะลามะพร้าวเจาะรู หยอดลงบนกระทะที่มีน้ำมันร้อน
        3. แกว่งกระทะเป็นวงกลม จนแป้งกลายเป็นแผ่นบางกรอบ
        4. เตรียมไส้ โดยผัดกุ้งสับ หมูสับ หอมใหญ่สับ ปรุงรสด้วยน้ำปลา น้ำตาลปี๊บ และเกลือ ใส่ถั่วลิสงคั่วบด ผัดจนเข้ากันดี
        5. นำแผ่นแป้งที่ทอดไว้ ตักไส้ใส่ตรงกลาง พับครึ่ง มัดด้วยต้นหอม
        6. ตั้งกระทะ ใส่น้ำมัน นำล่าเตียงลงทอดจนเหลืองกรอบ
        7. โรยหน้าด้วยผักชีและพริกชี้ฟ้าแดงสับ
    """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - แป้งที่ใช้ควรมีอุณหภูมิห้อง จะทำให้เนื้อแป้งเนียน นุ่ม
        - การแกว่งกระทะควรทำอย่างสม่ำเสมอ จะทำให้เส้นขนมล่าเตียงบางกรอบสวยงาม
        - ไส้ของล่าเตียงสามารถปรับเปลี่ยนได้ตามชอบ เช่น ใส่เห็ด ใส่กะหล่ำปลี หรือใส่ผักอื่นๆ
    """
    )

st.title("คุณค่าทางโภชนาการ")
with st.expander("คุณค่าทางโภชนาการ"):
    st.markdown(
        """
        ล่าเตียงเป็นแหล่งคาร์โบไฮเดรต โปรตีน ไขมัน และใยอาหาร
    """
    )

st.title("การเก็บรักษา")
with st.expander("การเก็บรักษา"):
    st.markdown(
        """
        ล่าเตียงควรเก็บไว้ในภาชนะที่ปิดสนิท ห่างความชื้น อุณหภูมิห้อง เก็บได้ประมาณ 1-2 วัน
    """
    )

st.page_link("Home.py", label="Home", icon="↩️")
