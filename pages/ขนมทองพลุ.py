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
kanom_img_path = os.getenv("COMPONENT_123_PATH1")
# component_1_path = os.getenv("COMPONENT_KluaiChap_PATH2")
# component_2_path = os.getenv("COMPONENT_KluaiChap_PATH3")

# Set page configuration
st.set_page_config(
    page_title="ขนมทองพลุ: ขนมไทยโบราณ กรอบนอกนุ่มใน ไส้แน่น",
    page_icon="👜",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(header_img_path)
# Display title
st.title("ขนมทองพลุ")
st.image(kanom_img_path)
st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ขนมทองพลุ เป็นขนมไทยโบราณที่มีลักษณะคล้ายขนมเอแคลร์ของฝรั่งเศส แต่มีวิธีทำที่แตกต่างกัน โดยทองพลุนั้นจะใช้วิธีทอดแทนการอบ สันนิษฐานว่ามีที่มาจากการดัดแปลงสูตรขนมจากต่างประเทศ เข้ามาผสมผสานกับวัฒนธรรมการทำอาหารไทยจนกลายเป็นเอกลักษณ์เฉพาะตัว ขนมทองพลุได้รับความนิยมในอดีต มักถูกนำมาเสิร์ฟในงานมงคลต่างๆ หรือเป็นของว่างทานเล่น
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ขนมทองพลุ มีวิธีทำที่ค่อนข้างละเอียด:**

        1. **ทำแป้ง:** ผสมแป้งสาลีอเนกประสงค์, เนยจืด, เกลือ, และน้ำเปล่า ตั้งไฟจนแป้งสุกและเหนียว พักไว้ให้เย็น
        2. **ตีแป้ง:** ใส่ไข่ไก่ทีละฟอง ตีจนแป้งเนียน พักไว้
        3. **ทอดแป้ง:** ตั้งกระทะใส่น้ำมัน รอจนร้อน ใส่แป้งลงทอดเป็นก้อนกลม จนพองเหลือง ตักขึ้นพักไว้
        4. **ทำไส้:** ผัดไก่สับกับเครื่องปรุงรสต่างๆ จนสุก พักไว้
        5. **ประกอบขนม:** ผ่าครึ่งขนมทองพลุ ใส่ไส้ลงไป โรยด้วยน้ำตาลไอซิ่ง
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        - **แป้งสาลีอเนกประสงค์** 1 ถ้วยตวง
        - **เนยจืด** 80 กรัม
        - **เกลือ** 1/4 ช้อนชา
        - **น้ำเปล่า** 1 ถ้วยตวง
        - **ไข่ไก่** 3 ฟอง

        **ไส้:**
        - **เนื้อไก่สับ** 200 กรัม
        - **หอมใหญ่สับ** 1/2 ถ้วยตวง
        - **แครอทสับ** 1/2 ถ้วยตวง
        - **ข้าวโพดอ่อน** 1/2 ถ้วยตวง
        - **ซีอิ๊วขาว** 2 ช้อนโต๊ะ
        - **ซอสปรุงรส** 1 ช้อนโต๊ะ
        - **น้ำตาลทราย** 1 ช้อนโต๊ะ
        - **พริกไทยดำป่น** 1/4 ช้อนชา

        **เพิ่มเติม:**
        - **น้ำตาลไอซิ่ง** สำหรับโรยหน้า
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
