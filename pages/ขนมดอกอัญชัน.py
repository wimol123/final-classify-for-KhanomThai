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
kanom_img_path = os.getenv("COMPONENT_94_PATH1")
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
st.title("ขนมดอกอัญชัน")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมดอกอัญชัน เป็นขนมไทยโบราณที่คล้ายขนมน้ำดอกไม้ แต่มีเอกลักษณ์โดดเด่นโดยเฉพาะที่เป็นสีม่วงอมน้ำเงินที่มาจากดอกอัญชัน ลักษณะเป็นถ้วยทรงกลมเนื้อแป้งนุ่มเด้ง มีกลิ่นหอมน้ำลอยดอกมะลิ รสชาติหวานตัดเค็ม แป้งเนื้อนุ่มหนึบ สีสันสวยงาม และตกแต่งจานด้วยใบตอง ประดับด้วยดอกอัญชันสดเพื่อเพิ่มความสวยงามและความเป็นธรรมชาติ

 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
ส่วนผสมขนมดอกอัญชัน  
• แป้งข้าวเจ้า 100 กรัม  
• แป้งเท้ายายม่อม 16 กรัม  
• น้ำตาลทราย 120 กรัม  
• น้ำปูนใส  20 กรัม  
• น้ำดอกอัญชันคั้น 160 กรัม  
• น้ำเปล่า  250 กรัม  
  
ส่วนผสมหน้ากะทิ  
• แป้งข้าวเจ้า 25 กรัม  
• กะทิ  250 กรัม  
• น้ำตาลทราย 12 กรัม  
• เกลือป่น  4 กรัม  
• แป้งถั่วเขียว 4 กรัม  
  
ส่วนผสมไข่แมงดา  
• ไข่เป็ด  10 ฟอง  
• แป้งทองหยอด 25 กรัม  
  
ส่วนผสมน้ำเชื่อม  
• น้ำตาลทราย 1 กิโลกรัม  
• น้ำลอยดอกมะลิ  750 กรัม  
• ใบเตย  4-5 ใบ  
• เปลือกไข่เป็ด 3 ฟอง  
  
ส่วนผสมน้ำเชื่อมใส  
• น้ำตาลทราย  500 กรัม    
• น้ำลอยดอกมะลิ 500 กรัม    
• ใบเตย  4-5 ใบ  
• เปลือกไข่เป็ด 2 ฟอง  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    วิธีทำน้ำเชื่อม  
1. นำน้ำตาลทรายใส่กระทงทอง พร้อมเปลือกไข่  
2. เติมน้ำลอยดอกมะลิและใบเตย  
3. ยกขึ้นตั้งไฟพอเดือด เคี่ยวประมาณ 10 นาที  
4. ยกลงกรองด้วยผ้าขาวบาง เทลงในกระทะทองยกขึ้นตั้งไฟเคี่ยวต่อให้เดือด  
  
ทำไข่แมงดา  
1. ตอกไข่เป็ดใส่ภาชนะแยกไข่แดง  
2. กรองผ่านกระชอน  
3. ใส่แป้งทองหยอด ผสมให้เข้ากัน  
4. เมื่อน้ำเชื่อมได้ที่เดือดปุดๆ ตรงกลาง ตักส่วนผสมใส่ในกรวยใบตองหรือกรวยทองเหลือง หยดลงในน้ำเชื่อม  
5. จนเต็มกระทะ เพิ่มเป็นไฟกลาง  
6. พอสุกตักขึ้น  
7. ใส่ในน้ำเชื่อมใส ทิ้งไว้สักครู่ ตักขึ้นพักไว้ให้สะเด็ดน้ำเชื่อม  
  
ทำขนมดอกอัญชัน   
1. ใส่น้ำตาลทราย น้ำเปล่าลงในหม้อ ตั้งไฟพอเดือด ยกลงกรอง พักไว้ให้เย็น  
2. ผสมแป้งข้าวเจ้า แป้งเท้ายายม่อม เข้าด้วยกัน ใส่น้ำเชื่อมที่เตรียมไว้ ให้พอนวดได้   
3. นวดประมาณ 15 นาที  
4. ใส่น้ำเชื่อมที่เหลือ น้ำปูนใส น้ำดอกอัญชัน ผสมให้เข้ากัน  
5. ใส่น้ำเปล่าลงในลังถึง ประมาณ 3/4 ของลังถึง ตั้งไฟให้เดือด นึ่งถ้วยให้ร้อน หยอดส่วนผสมใส่ให้เต็มถ้วย  
6. ปิดฝานึ่ง ประมาณ 20 นาที ยกลงพักไว้ให้เย็น แคะออกจากถ้วย พักไว้  

ทำหน้ากะทิ  
1. ผสมกะทิ แป้งข้าวเจ้า แป้งถั่วเขียว น้ำตาลทราย เกลือป่น ลงในกระทะทอง  
2. ยกขึ้นตั้งไฟ คนจนข้น แป้งสุก ยกลงพักไว้ให้เย็น ใส่กระชอนกรอง แล้วตักใส่กรวยกระดาษใช้หัวบีบเบอร์ 102  
3. บีบหน้ากะทิลงบนขนมให้สวยงาม  
4. ตกแต่งด้วยไข่แมงดา  
    
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
