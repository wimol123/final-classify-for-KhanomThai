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
kanom_img_path = os.getenv("COMPONENT_96_PATH1")
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
st.title("ขนมดาวล้อมเดือน")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมดาวล้อมเดือน ขนมไทยโบราณที่หาทานได้ยากในปัจจุบัน  โดดเด่นด้วยเอกลักษณ์ของแป้งสีสันสดใส ห่อหุ้มไส้ถั่วรสเค็มมัน กลมกล่อมลงตัว  เมื่อทานคู่กับน้ำกะทิหอมมัน  โรยด้วยงาคั่วบด   ช่างเป็นเมนูของหวานที่ชวนให้นึกถึงอดีตและภูมิปัญญาไทยอันล้ำค่า  
  
ที่มาของชื่อขนม  
  
ยังไม่มีหลักฐานแน่ชัดที่ระบุถึงที่มาของชื่อ "ดาวล้อมเดือน"  แต่สันนิษฐานกันว่า  ลักษณะของขนมที่ปั้นเป็นก้อนกลมสีสันสดใส   คล้ายดวงดาวที่รายล้อมรอบดวงจันทร์   จึงเป็นที่มาของชื่อขนมอันไพเราะนี้  

เอกลักษณ์ของขนม  
  
แป้งขนม : ทำจากแป้งข้าวเหนียวผสมกับแป้งข้าวเจ้า นวดจนเนียน นำมาปั้นเป็นก้อนกลม แล้วนำไปนึ่งจนสุก แป้งจะมีสีสันสดใส โดยทั่วไปนิยมใช้สีเขียวจากใบเตย สีม่วงจากดอกอัญชัน และสีชมพูจากดอกกุหลาบ  
ไส้ขนม : ทำจากถั่วเขียวบด ผสมกับน้ำตาลทราย เกลือ และไข่แดง นำไปกวนจนเหนียวข้น  
น้ำกะทิ : นำกะทิสดมาเคี่ยวกับใบเตย เกลือ และน้ำตาลทราย จนได้น้ำกะทิหอมหวานมัน  
งาคั่ว : คั่วเมลดงาขาวจนเหลืองหอม  
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
   ไส้ถั่ว  
ถั่วเขียว 250 กรัม  
น้ำตาลทราย 100 กรัม  
กะทิ 100 กรัม  
เกลือ 1/2 ช้อนชา  
พริกไทยขาวบด 1/4 ช้อนชา  
น้ำมันพืช 2 ช้อนโต๊ะ  
  
แป้ง  
แป้งข้าวเหนียว 250 กรัม  
แป้งมัน 2 ช้อนโต๊ะ  
กะทิ 500 มิลลิลิตร  
น้ำเปล่า 100 มิลลิลิตร  
สีผสมอาหาร 2-3 หยด  
เกลือ 1/4 ช้อนชา  
งาขาวคั่ว  
  
น้ำกะทิ  
กะทิ 500 มิลลิลิตร  
ใบเตย 2-3 ใบ  
เกลือ 1/4 ช้อนชา  
น้ำตาลทราย 100 กรัม  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
ไส้ถั่ว  
1. ล้างถั่วเขียวให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง  
2. นำถั่วเขียวที่แช่น้ำไว้ไปนึ่งหรือต้มจนสุก  
3. นำถั่วเขียวที่สุกแล้วมาบดให้ละเอียด  
4. ตั้งกระทะใส่น้ำมันพืช 1 ช้อนโต๊ะ ใส่กระเทียมสับลงผัดจนหอม  
5. ใส่ถั่วเขียวบด น้ำตาลทราย เกลือ พริกไทยขาวบด กะทิ ลงผัดจนเข้ากันดี  
6. ใส่ใบเตยผูกปมลงไป โรยงาขาวคั่ว 1 ช้อนโต๊ะ ปิดไฟ ผักให้เย็น  
  
แป้ง  
1. ผสมแป้งข้าวเหนียว แป้งมัน เกลือ และน้ำเปล่าลงในอ่างผสม  
2. ค่อยๆ ใส่น้ำกะทิลงไป นวดจนแป้งเนียนไม่ติดมือ แบ่งแป้งออกเป็น 3 ส่วน  
3. ผสมสีผสมอาหารแต่ละสีกับแป้ง นวดจนเข้ากันดี  
4. ปั้นแป้งแต่ละสีเป็นก้อนกลมขนาดเท่ากัน  
  
ประกอบตัวขนม  
1. นำแป้งแต่ละสีมาวางสลับกันเป็นชั้น ๆ  
2. กดแป้งลงบนฝ่ามือ วางไส้ถั่วลงตรงกลาง ห่อแป้งให้มิด  
3. ตั้งน้ำในหม้อให้เดือด ใส่ขนมดาวล้อมเดือนลงไปต้มจนลอยขึ้น  
4. ตักขนมดาวล้อมเดือนขึ้น พักไว้ให้สะเด็ดน้ำ  
  
น้ำกะทิ  
1. ตั้งกะทิ ใบเตย เกลือ และน้ำตาลทรายลงในหม้อ เคี่ยวจนใบเตยหอม น้ำกะทิข้นขึ้น  
2. ตักขนมดาวล้อมเดือนใส่จาน ราดด้วยน้ำกะทิ โรยงาขาวคั่ว  
    
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
