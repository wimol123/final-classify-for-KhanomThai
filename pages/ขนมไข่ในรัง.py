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
kanom_img_path = os.getenv("COMPONENT_62_PATH1")
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
st.title("ขนมไข่ในรัง, ฝอยเงิน")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """
**ขนมไข่ในรัง** ขนมไทยโบราณที่มีเอกลักษณ์โดดเด่นไม่เหมือนใคร ด้วยรูปลักษณ์ที่คล้ายรังนก วางไข่สีเหลืองอร่ามไว้ตรงกลาง รสชาติหอมหวานมันอร่อยเป็นที่นิยมทั้งในอดีตและปัจจุบัน  
  
**ที่มาของชื่อ**  
สันนิษฐานว่าได้ชื่อมาจากลักษณะของขนม โดยแป้งขนมไข่ที่อบจนฟูมีรูตรงกลางคล้ายกับรังนก และมีไข่สีเหลืองอร่ามอยู่ตรงกลาง เปรียบเสมือนไข่ที่นกวางไว้ในรัง  
  
**เอกลักษณ์ของขนมไข่ในรัง**  
รูปลักษณ์: ขนมไข่ในรังมีเอกลักษณ์เฉพาะตัว คือ แป้งขนมไข่ที่อบจนฟู มีรูตรงกลาง คล้ายกับรังนก และมีไข่สีเหลืองอร่ามอยู่ตรงกลาง  
รสชาติ: ขนมไข่ในรังมีรสชาติหอมหวาน มัน อร่อย ลงตัว  
ความพิเศษ: ขนมไข่ในรังเป็นขนมที่ต้องอาศัยความประณีตและความพิถีพิถันในการทำ โดยเฉพาะการบีบแป้งให้เป็นรูปรังนก และการตีไข่ให้ตั้งยอดอ่อน 



"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    • แป้งเค้ก 90 กรัม  
    • น้ำตาลทรายขาว 100 กรัม  
    • ผงฟู ½ ช้อนชา  
    • ไข่ไก่ขนาดใหญ่ 3 ฟอง  
    • กลิ่นวานิลลา ½ ช้อนชา  
    • น้ำมะนาว 1 ช้อนชา  
    • เนยสำหรับทาพิมพ์  

"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ตีไข่ไก่กับน้ำตาลทรายจนตั้งยอดอ่อน ใส่กลิ่นวานิลลาและน้ำมะนาว คนให้เข้ากัน  
    2. ร่อนแป้งเค้กและผงฟู ใส่ลงในส่วนผสมไข่ คนให้เข้ากันจนเนียน  
    3. เทส่วนผสมลงในถุงบีบ บีบแปลงเป็นรูปรังนกบนพิมพ์ที่ทาเนยไว้  
    4. อบในเตาอบที่อุณหภูมิ 180 องศาเซลเซียส ประมาณ 15-20 นาที หรือจนขนมสุกเหลือง  
    5. นำออกจากเตาอบ พักให้เย็นก่อนเสิร์ฟ  

    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
