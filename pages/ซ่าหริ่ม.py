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
kanom_img_path = os.getenv("COMPONENT_89_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมซ่าหริ่ม: ขนมไทยโบราณ หอมมัน หวานมัน กรอบนอกนุ่มใน",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมซ่าหริ่ม")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมซ่าหริ่มหรือซาหริ่ม เป็นขนมไทยโบราณที่มีมาช้านาน มีหลักฐานปรากฏในวรรณคดีไทยหลายเรื่อง 
        สันนิษฐานว่ามีต้นกำเนิดมาจากประเทศจีน ซึ่งชาวไทยได้นำมารดัดแปลงสูตร ผสมผสานกับวัฒนธรรมการทำอาหารไทยจนกลายเป็นเอกลักษณ์เฉพาะตัว 
        ขนมซ่าหริ่มนิยมทำขึ้นเพื่อเป็นของว่าง ของหวาน หรือใช้ประกอบพิธีกรรมต่างๆ
        """
    )

st.title("ลักษณะของขนมซ่าหริ่ม")
with st.expander("ลักษณะของขนมซ่าหริ่ม"):
    st.markdown(
        """
        **ลักษณะของขนมซ่าหริ่ม:**
        - มีเส้นสีขาว คล้ายเส้นขนมจีน
        - มีรสชาติหวานมัน กลมกล่อม
        - มีเนื้อสัมผัสกรอบนอกนุ่มใน
        - ราดด้วยกะทิ น้ำเชื่อม และมะพร้าวอ่อน
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมซ่าหริ่ม มีวิธีทำดังนี้:**

        1. **ทำแป้ง:** ผสมแป้งข้าวเจ้า, น้ำเปล่า, เกลือ, และสีผสมอาหาร นวดจนแป้งเนียน พักไว้
        2. **ต้มเส้น:** ต้มน้ำให้เดือด ใส่แป้งที่เตรียมไว้ ต้มจนเส้นสุก โรยน้ำสะอาดพักไว้
        3. **เตรียมน้ำกะทิ:** ผสมหัวกะทิ, น้ำตาลทราย, เกลือ, และใบเตย ตั้งไฟจนน้ำตาลทรายละลาย
        4. **เตรียมมะพร้าวอ่อน:** หั่นมะพร้าวอ่อนเป็นชิ้นพอคำ
        5. **เสิร์ฟ:** ใส่เส้นซ่าหริ่มลงในถ้วย ราดด้วยน้ำกะทิ โรยมะพร้าวอ่อน และน้ำแข็ง
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        **แป้ง:**
        - แป้งข้าวเจ้า 1 ถ้วยตวง
        - น้ำเปล่า 1 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - สีผสมอาหาร ตามต้องการ

        **น้ำกะทิ:**
        - หัวกะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - ใบเตย 2-3 ใบ

        **เพิ่มเติม:**
        - มะพร้าวอ่อน
        - น้ำแข็ง
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
