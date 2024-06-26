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
kanom_img_path = os.getenv("COMPONENT_70_PATH1")
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
st.title("")

left_co, cent_co, last_co = st.columns(3)
st.title("ขนมค้างคาวเผือก")
with cent_co:
    st.image(image=kanom_img_path, width=500)

multi = """

ขนมค้างคาวเผือก เป็นของว่างไทยโบราณที่มีเอกลักษณ์โดดเด่นทั้งรูปลักษณ์และรสชาติ เรียกว่าเป็น "ของว่างที่หน้าตาไม่เหมือนใคร รสชาติอร่อยถูกปาก"  
  

**ที่มาของชื่อ**

- รูปร่างคล้ายค้างคาว: ขนมชนิดนี้มีรูปร่างคล้ายกับ "ค้างคาว" ที่กำลังกางปีกบิน แหลมตรงปลายทั้งสองข้าง    
- ส่วนผสมจากเผือก: แป้งของขนมค้างคาวเผือก มีส่วนผสมของเผือก ทำให้มีสีเหลืองอ่อน และเนื้อสัมผัสที่นุ่มละมุน  
  
**ประวัติ**  
- ตำราวัง: ขนมค้างคาวเผือกมี ต้นตำรับมาจากตำราอาหารไทยโบราณ  
- ความนิยม: ได้รับความนิยมใน สมัยรัตนโกสินทร์ เป็น ของว่างที่ชาววังนิยมรับประทาน  
- ผู้ริเริ่ม: มีการสันนิษฐานว่า "ท่านผู้หญิงเปลี่ยน ภาสกรวงศ์" เจ้าของตำรา "แม่ครัวหัวป่าก์" เป็นผู้ริเริ่มใส่เผือกในแป้งขนมค้างคาว จนกลายเป็น "ขนมค้างคาวเผือก" ที่เรารู้จักกันในปัจจุบัน  

**ลักษณะของขนม**  
- รูปร่าง: สามเหลี่ยม แหลมตรงปลายทั้งสองข้าง  
- สีสัน: เหลืองอ่อน  
- เนื้อสัมผัส: กรอบนอก นุ่มใน  
- รสชาติ: กลมกล่อม หอมมัน  
- ไส้: ไส้หมูสับ กุ้งสับ เห็ดหอม  
  
**วิธีการทาน**  
- ทานคู่กับ น้ำจิ้มอาจาด รสเปรี้ยวหวาน  
- ทานคู่กับ น้ำจิ้มไก่ รสหวานมัน  
  
ปัจจุบัน: ขนมค้างคาวเผือก หาทานได้ยากนิยมทำเฉพาะ งานพิเศษ หรือตาม ร้านขนมไทยบางร้าน

"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    ตัวแป้ง  
    • เผือกนึ่ง 500 กรัม
    • แป้งสาลีอเนกประสงค์ 100 กรัม  
    • แป้งข้าวเจ้า 50 กรัม
    • มะพร้าวขูดขาว 100 กรัม  
    • เกลือ 1/2 ช้อนชา  
    • น้ำตาลทราย 1 ช้อนโต๊ะ  
    • น้ำเปล่า 100 มิลลิลิตร  
  
    ตัวไส้  
    • เนื้อหมูสับ 200 กรัม  
    • กุ้งสับ 100 กรัม  
    • เห็ดหอม 5 ดอก  
    • แครอท 1/2 หัว  
    • หอมใหญ่ 1/4 หัว  
    • รากผักชี 1 ต้น  
    • กระเทียม 2 กลีบ  
    • พริกไทยขาวป่น 1/2 ช้อนชา  
    • ซีอิ๊วขาว 1 ช้อนโต๊ะ  
    • น้ำตาลทราย 1 ช้อนชา  
    • น้ำมันพืช 1 ช้อนโต๊ะ  
  
    น้ำจิ้มอาจาด  
    • น้ำส้มสายชู 3 ช้อนโต๊ะ  
    • น้ำตาลทราย 2 ช้อนโต๊ะ  
    • เกลือ 1/2 ช้อนชา  
    • พริกขี้หนูสวนซอย 5 เม็ด  
    • แครอทซอย 1/2 หัว  
    • หัวหอมซอย 1/4 หัว  
    • ผักชีซอย 1 ต้น  
    

"""
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    ตัวแป้ง  
1. นึ่งเผือกจนสุก นำมาบดให้ละเอียด  
2. ผสมแป้งสาลีอเนกประสงค์ แป้งข้าวเจ้า มะพร้าวขูดขาว เกลือ และน้ำตาลทรายลงในชาม  
3. ใส่เผือกบดลงไป นวดจนแป้งเนียนไม่ติดมือ  
4. ค่อยๆ เติมน้ำเปล่าลงไปทีละน้อย นวดจนแป้งไม่ติดชาม  
5. พักแป้งไว้ 30 นาที  
  
ตัวไส้
1. แช่เห็ดหอมในน้ำร้อนจนนิ่ม บีบน้ำออก สับละเอียด  
2. ตั้งกระทะ ใส่น้ำมันพืช 1 ช้อนโต๊ะ ใส่รากผักชี กระเทียม และพริกไทยขาวป่น ผัดจนหอม  
3. ใส่เนื้อหมูสับ กุ้งสับ และแครอทซอย ผัดจนสุก  
4. ใส่เห็ดหอมซอย หอมใหญ่สับ ซีอิ๊วขาว น้ำตาลทราย และเกลือ ผัดคลุกเคล้าจนเข้ากัน  
5. ปิดไฟ พักไว้ให้ไส้เย็น  
  
การประกอบขนม  
1. แบ่งแป้งออกเป็นก้อนเล็กๆ ปั้นเป็นก้อนกลม  
2. ใช้มือคลึงแป้งให้เป็นแผ่นบาง รีดแป้งด้วยไม้กลิ้ง  
3. ใส่ไส้ลงตรงกลาง พับแป้งเป็นรูปสามเหลี่ยม บีบปลายให้แหลม  
4. ตั้งกระทะใส่น้ำมันพืช จุ่มค้างคาวเผือกในน้ำเปล่า นำไปทอดในน้ำมันร้อนปานกลางจนเหลืองกรอบ  
5. ตักขึ้นพักให้สะเด็ดน้ำมัน  
  
น้ำจิ้มอาจาด
1. ผสมน้ำส้มสายชู น้ำตาลทราย เกลือ และพริกขี้หนูสวนซอยเข้าด้วยกัน  
2. ใส่แครอทซอย หัวหอมซอย และผักชีซอย คลุกเคล้าให้เข้ากัน  

    
    """
    st.markdown(multi)

st.page_link("Home.py", label="Home", icon="↩️")
