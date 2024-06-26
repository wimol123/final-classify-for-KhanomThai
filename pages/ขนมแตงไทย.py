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
kanom_img_path = os.getenv("COMPONENT_105_PATH1")
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
st.title("ขนมแตงไทย")

left_co, cent_co, last_co = st.columns(3)
st.title("ความเป็นมา")
with cent_co:
    st.image(image=kanom_img_path, width=600)

multi = """
ขนมแตงไทยเป็นขนมพื้นเมืองของคนภาคเหนือและถือเป็นญาติคนนึงของขนมกล้วย เนื้อขนมจะมีสีเหลืองนวล เนื้อนุ่ม หอมหวานกลิ่นแตงไทยโรยหน้าด้วยมะพร้าวทึนทึกขูด ขนมแตงไทยทำคล้ายกับขนมกล้วย คือใช้แตงไทยสุกงอมบดละเอียดหรือว่าขูดเป็นเส้นผสมกับแป้งข้าวเจ้า กะทิ น้ำตาลทราย มะพร้าวขูด บางตำราใส่แป้งมันสำปะหลังให้ส่วนผสมเหนียวขึ้น จะเทใส่ถาดใส่กระทงใบตอง หรือใส่กรวยใบตองก็ได้แล้วแต่จะชอบรูปทรงแบบไหน 
 
"""
st.markdown(multi)
col1, col2 = st.columns(2)

with col1:
    st.header("ส่วนประกอบ")
    multi = """
    เนื้อแตงไทยสุกขูดเป็นเส้น 2 ถ้วย  
    น้ำตาลทราย 2 ถ้วย  
    แป้งข้าวเจ้า 2 ถ้วย  
    กะทิ 3 ถ้วย  
    เกลือ 1 ช้อนชา  
    แป้งท้าวยายม่อม ¾ ถ้วย  
    มะพร้าวขูดขาว ½ ถ้วย  
    """
    st.markdown(multi)
with col2:
    st.header("วิธีทำ")
    multi = """
    1. นำมะพร้าวขูดขาวใส่ในชามเล็กแล้วผสมเกลือประมาณ 1/4 ช้อนชา แล้วคลุกเคล้าให้เข้ากัน เตรียมพักไว้  
    2. จากนั้นนำแตงไทยมาผ่าครึ่งลูกตามยาว ขูดส่วนของเมล็ดออกให้หมด และใช้ที่ขูดขูดแตงไทยให้เป็นเส้นๆ แล้วบีบน้ำออกบางส่วน  
    3. ใส่แป้งข้าวเจ้าและแป้งท้าวยายม่อมลงไป เติมกะทิ น้ำตาลทรายและเกลืออีกส่วนนึงที่เหลือเข้าด้วยกันแล้วนวดให้เป็นเนื้อเดียวกัน  
    4. นำส่วนผสมทั้งหมดใส่ในกระทะทองยกตั้งไฟอ่อนเคี่ยวแค่พอข้นแล้วยกลง  
    5. ตักส่วนผสมใส่ในกรวยใบตอง แล้วโรยหน้าด้วยมะพร้าวขูด นำไปเสียบรูรังถึงนึ่งน้ำเดือดไฟแรง 15 นาทีแล้วยกลงพักให้เย็น  
        
    """
    st.markdown(multi)
st.page_link("Home.py", label="Home", icon="↩️")
