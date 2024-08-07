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
kanom_img_path = os.getenv("COMPONENT_83_PATH1")
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
st.title("ขนมช่อผกากรอง")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมผกากรอง เป็นขนมไทยที่มาจากความคิดสร้างสรรค์ของ อ.สำเร็จ วรรณพิรุณ ซึ่งท่านได้พัฒนาสูตรจาก ขนมช่อแก้ว ให้มีความสวยงามมากยิ่งขึ้น ด้วยการทำกลีบขนมให้มีกลีบบาง ซ้อนกันหลาย ๆ ชั้น จนเหมือนกับดอกผกากรอง ทำให้ขนมชนิดนี้ถูกเรียกว่า ขนมผกากรอง มาจนถึงปัจจุบัน
โดยส่วนผสมหลักของแป้งขนมนั้น ประกอบด้วย แป้งเค้ก หัวกะทิ น้ำตาลทราย แต่ถ้าหากอยากเพิ่มสีสันให้สวยงาม เหมือนกับดอกไม้ที่มีหลายสี ก็สามารถใส่สีผสมอาหารต่าง ๆ ลงไปผสมกับตัวแป้งได้ ไม่ว่าจะเป็น สีม่วง สีส้ม สีชมพู หรือ สีเขียว สำหรับในส่วนไส้นั้น นิยมใส่ไส้ถั่วกวน เผือกกวน มันหวาน มันม่วงกวน หรือ ทองหยอด ก็ได้ ตามชอบ
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ส่วนผสมไส้ถั่วกวน  
    • ถั่วเขียวซี่กระเทาะเปลือก 250 กรัม  
    • กะทิ 250 มิลลิลิตร  
    • น้ำตาลทราย 200 กรัม  
    • เกลือ 1/2 ช้อนชา  

    ส่วนผสมแป้งขนม  
    • แป้งเค้ก 210 กรัม  
    • หัวกะทิ 400 มิลลิลิตร  
    • น้ำตาลทรายขาว 60 กรัม  
    • กลิ่นมะลิ 1/4 ช้อนชา  
    • สีผสมอาหารสีม่วง ส้ม ชมพู เขียว อย่างละ 1 – 2 หยด  
    • เกล็ดน้ำตาลกลมเคลือบสี สำหรับตกแต่ง  

    อุปกรณ์อื่น ๆ  
    • แหนบจีบหัวใบไม้  
    • ถ้วยพิมพ์วุ้นใส เบอร์ 8  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    ไส้  
    1. นำถั่วเขียวไปล้างน้ำให้สะอาด 3 – 4 รอบ จนกว่าน้ำจะใส จากนั้น แช่น้ำเปล่า 4 – 5 ชั่วโมง จนกว่าถั่วเขียวจะนิ่ม  
    2. พอครบเวลา ให้นำถั่วเขียวไปล้างน้ำให้สะอาดอีก 3 – 4 รอบ พักให้สะเด็ดน้ำ แล้วห่อด้วยผ้าขาวบาง นำไปนึ่งในซึ้ง ด้วยไฟแรง เป็นเวลา 25 – 30 นาที จนกว่าถั่วเขียวจะสุกนิ่ม เสร็จแล้ว ใส่ถั่วเขียวลงในชามผสม แล้วใช้สากตำให้ละเอียด  
    3. ตั้งกระทะ ใส่กะทิลงไป ตามด้วยเกลือป่น น้ำตาลทราย เปิดไฟกลางค่อนไฟอ่อน คนให้น้ำตาลทรายละลายดี  
    4. พอน้ำตาลละลายดีแล้ว ใส่ถั่วเขียวบดลงไป คนให้เข้ากัน และ กวนไปเรื่อย ๆ จนกว่าเนื้อถั่วเขียวจะเริ่มข้นขึ้น  
    5. พอข้นขึ้นดีแล้ว ให้ลดเป็นไฟอ่อน กวนต่อไปเรื่อย ๆ จนกว่าถั่วเขียวจะเริ่มแห้ง ใช้เวลา 15 – 20 นาที พอไส้ได้ที่แล้ว ให้ตักขึ้นใส่ชามผสม พักทิ้งไว้ให้เย็น  
    6. ใช้มือนวดถั่วเขียวให้นิ่ม เป็นเนื้อเดียวกัน เสร็จแล้ว แบ่งออกมาเป็นก้อนเล็ก ๆ แล้วปั้นให้เป็นก้อนกลม เตรียมไว้  
        
    ตัวขนม  
    1. เตรียมชามผสม ใส่แป้งเค้ก น้ำตาลทราย คนให้เข้ากัน จากนั้น ค่อย ๆ ใส่น้ำกะทิและกลิ่นมะลิลงไป พร้อมกับคนแป้งไปด้วย จนกว่าแป้งจะละลายเข้ากันกับกะทิ จนเป็นเนื้อเดียวกัน
    2. ตั้งกระทะ ใส่แป้งที่ผสมไว้ลงไป แล้วเปิดไฟอ่อน ใช้ไม้พายกวนแป้งไปเรื่อย ๆ จนกว่าแป้งจะจับตัวเป็นก้อน และ ร่อนออกจากกระทะ
    3. พอแป้งสุกดีแล้ว ให้เอาออกจากกระทะ ตัดแป้งออกเป็น 5 ส่วนเท่า ๆ กัน แล้วใส่สีผสมอาหารในแป้งแต่ละก้อน ตามชอบ นวดให้เข้ากันจนได้แป้ง 5 สีตามที่ต้องการ
    4. เริ่มห่อไส้ถั่วกวน โดยแบ่งแป้งมาส่วนหนึ่ง ปั้นให้เป็นก้อนกลม แล้วแผ่เป็นแผ่นบาง นำถั่วกวนที่ปั้นเป็นก้อนกลมไว้แล้ว มาวางตรงกลาง หุ้มและปั้นให้เป็นก้อนกลม ใส่ถ้วยวุ้นเล็ก ๆ ไว้
    5. ใช้แหนบจีบใบไม้ จับจีบแป้งจากล่างขึ้นบน เป็นชั้น ๆ ให้สวยงาม แล้วตกแต่งด้านบนด้วยเกล็ดน้ำตาลกลมเคลือบสี เป็นอันเสร็จ
        
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
