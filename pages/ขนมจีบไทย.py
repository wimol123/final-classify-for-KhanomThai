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
kanom_img_path = os.getenv("COMPONENT_78_PATH1")
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
st.title("ขนมจีบไทย, ขนมจีบนก")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมจีบไทย หรือขนมจีบตัวนกมีรสชาติคล้ายกับช่อม่วง 
ต่างกันก็ตรงรูปร่างหน้าตาที่ดูคล้ายนก 
เหมาะสำหรับทำรับประทานเป็นอาหารว่างหรือทำเสิร์ฟในงานเลี้ยง 
เพราะมีหน้าตาที่น่าเอ็นดู
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ตัวแป้ง  
    • แป้งข้าวเจ้า180 กรัม  
    • แป้งท้าวยายม่อม160 กรัม  
    • กะทิ240 มิลลิลิตร  
    • น้ำ240 มิลลิลิตร  
    • น้ำมันรำข้าว1 ช้อนชา  

    ไส้หมู  
    • หมูสับ100 กรัม  
    • หอมแดง (สับ)100 กรัม  
    • ถั่วลิสงคั่วป่น10 กรัม  
    • น้ำตาลปี๊บ50 กรัม  
    • พริกไทยขาวเม็ด1⁄2 ช้อนชา  
    • กระเทียม (สับ)3 กลีบ  
    • เกลือ1 ช้อนชา  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. ผสมแป้งทั้งสองชนิดเข้าด้วยกัน หยดน้ำลงไปจนพอให้นวดแป้งได้ นวดประมาณ 4-5 นาที แล้วตามด้วยน้ำและกะทิที่เหลือ นวดแป้งจนแป้งไม่เป็นเม็ด ใส่น้ำมันรำข้าว แล้วเทใส่กระทะทองเหลือง หรือหม้อเคลือบ นำไปตั้งไฟ กวนจนแป้งสุกดี นำออกมาห่อด้วยพลาสติกถนอมอาหาร พักให้เย็นลง  
    2. ทำตัวไส้ โดยโขลกรากผักชี กระเทียมและพริกไทย นำไปผัดกับน้ำมันรำข้าวให้หอมดี ใส่หอมแดงสับลงไป ผัดให้สุก ตามด้วยหมูสับ พอสุกดี ก็ใส่น้ำตาลปี๊บและเกลือลงไป ผัดจนน้ำตาลข้นขึ้นเล็กน้อยประมาณ 10นาที ยกออกจากความร้อน ใส่ถั่วลงไป เคล้าให้เข้ากัน พักให้เย็น  
    3. แบ่งแป้งเป็นก้อนๆ ละ 15 กรัม ขึ้นเบ้าให้แป้งมีรูปทรงเป็นแอ่งเหมือนชาม ใส่ไส้ หุ้มให้มิด จับแป้งให้นูนขึ้นมาเป็นส่วนหัว ใช้ที่จับจีบจีบให้รอบตัว เสียบแครอทจุ่มน้ำบางๆ เป็นปาก และงาเป็นตา วางเรียงในลังถึงรองใบตองทาน้ำมัน  
    4. นำไปนึ่งในลังถึงที่ร้อนดีเป็นเวลา 10นาที  
    5. ทาน้ำมันบางๆ เสิร์ฟกับผักกาดหอม ผักชี และพริกขี้หนูสวน  
    
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
