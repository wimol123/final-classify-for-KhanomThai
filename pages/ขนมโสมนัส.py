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
kanom_img_path = os.getenv("COMPONENT_217_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")


# Set page configuration
st.set_page_config(
    page_title="ขนมโสมนัส: ขนมไทยโบราณ หวานละมุน หอมมันมะพร้าว",
    page_icon="🥥",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display main image and title
# Display title
st.title("ขนมโสมนัส: ขนมไทยโบราณ หวานละมุน หอมมันมะพร้าว")
st.image(kanom_img_path)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมโสมนัส เชื่อกันว่ามีมาตั้งแต่สมัยกรุงศรีอยุธยา โดยมีเอกสารโบราณที่กล่าวถึงขนมชนิดนี้ไว้ว่า "โคมนัส" ซึ่งสันนิษฐานว่าเพี้ยนมาจากคำว่า "โคโคนัท" หมายถึงมะพร้าว ซึ่งเป็นส่วนผสมหลักของขนมชนิดนี้
        โสมนัสจัดเป็นขนมอบไทยยุคแรกๆ ที่ใช้ไข่ขาวเป็นส่วนผสม ต่างจากขนมไทยดั้งเดิมที่มักใช้ไข่แดง ขนมชนิดนี้ได้รับความนิยมในหมู่ชาววัง และยังเป็นที่โปรดปรานของสมเด็จพระนารายณ์มหาราช
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **วัตถุดิบ:**
        - ไข่ขาว 3 ฟอง
        - น้ำตาลทราย 150 กรัม
        - มะพร้าวขูดขาว 1 ½ ถ้วยตวง
        - เกลือ 1/8 ช้อนชา
        - น้ำมะนาว 1 ช้อนชา

        **วิธีทำ:**
        1. ตั้งกระทะเทฟล่อนไฟอ่อน ใส่ไข่ขาว เกลือ และน้ำมะนาว ตีจนตั้งยอดอ่อน
        2. ใส่น้ำตาลทรายค่อยๆ ทีละน้อย ตีต่อจนตั้งยอดแข็ง
        3. ใส่มะพร้าวขูดขาว คนเบาๆ ให้เข้ากัน
        4. ตักส่วนผสมใส่ถาดอบที่รองด้วยกระดาษอบ หรือเกลี่ยเป็นก้อนกลมๆ
        5. อบที่อุณหภูมิ 150 องศาเซลเซียส ประมาณ 5-10 นาที
        6. ลดไฟเหลือ 80 องศาเซลเซียส อบต่อจนขนมแห้งสนิท

        **หมายเหตุ:**
        - ระยะเวลาอบขึ้นอยู่กับเตาอบแต่ละชนิด ควรสังเกตสีของขนม ถ้าเริ่มเหลืองทองก็แสดงว่าขนมเสร็จ
        - สามารถปรับหวานของขนมได้ตามชอบ
        - มะพร้าวขูดขาวควรคั่วก่อนนำมาใช้ จะทำให้ขนมมีกลิ่นหอมและอร่อยยิ่งขึ้น
        """
    )
st.page_link("Home.py", label="Home", icon="↩️")
