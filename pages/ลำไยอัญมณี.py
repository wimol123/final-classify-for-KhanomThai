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
kanom_img_path = os.getenv("COMPONENT_191_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมลำไยอัญมณี: ของหวานเย็นชื่นใจ สูตรลับจากคุณยาย",
    page_icon="🍧",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display main image and title
st.image(image=header_img_path)
st.title("ขนมลำไยอัญมณี: ของหวานเย็นชื่นใจ สูตรลับจากคุณยาย")
st.image(kanom_img_path)
st.title("ที่มา")
with st.expander("ที่มา"):
    st.markdown(
        """
        ขนมลำไยอัญมณี ไม่มีหลักฐานแน่ชัดว่ามีต้นกำเนิดมาจากที่ใด สันนิษฐานว่า น่าจะได้รับอิทธิพลจากวัฒนธรรมตะวันตก ผสมผสานกับวัตถุดิบท้องถิ่นอย่างลำไย กลายเป็นขนมหวานเย็นที่ได้รับความนิยมในประเทศไทย
    """
    )

st.title("สูตร")
with st.expander("สูตร"):
    st.markdown(
        """
        **ส่วนผสม**
        - ลำไยแกะเปลือก 300 กรัม
        - น้ำเปล่า 500 มิลลิลิตร
        - น้ำตาลทราย 100 กรัม
        - วุ้นผง 1 ช้อนชา
        - สีผสมอาหารหลากสี

        **วิธีทำ**
        1. ต้มน้ำเปล่ากับน้ำตาลทรายจนเดือด
        2. ละลายวุ้นผงกับน้ำเปล่าเล็กน้อย เทลงในน้ำเชื่อม คนจนวุ้นละลาย
        3. แบ่งน้ำวุ้นเป็น 4 ถ้วย ใส่สีผสมอาหารลงในแต่ละถ้วย คนให้เข้ากัน
        4. นำลำไยแกะเปลือก ใส่ลงในพิมพ์ เทน้ำวุ้นหลากสีลงในพิมพ์ รอจนวุ้นเซ็ตตัว
        5. นำขนมลำไยอัญมณี ออกจากพิมพ์ ตัดเป็นชิ้นพอดีคำ ทานคู่กับน้ำแข็งไส
    """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้ลำไยสด เนื้อแน่น จะได้รสชาติอร่อย
        - น้ำตาลทรายสามารถปรับเพิ่มหรือลดได้ตามชอบ
        - วุ้นผงควรละลายกับน้ำเปล่าให้สนิทก่อน จะได้ไม่มีเม็ดวุ้น
        - สีผสมอาหารควรเลือกใช้สีที่ปลอดภัย
        - เก็บขนมในตู้เย็น จะได้ทานได้นานขึ้น
    """
    )

st.title("คุณค่าทางโภชนาการ")
with st.expander("คุณค่าทางโภชนาการ"):
    st.markdown(
        """
        ขนมลำไยอัญมณี ให้พลังงานจากคาร์โบไฮเดรต และวิตามินจากลำไย
    """
    )

st.title("การเก็บรักษา")
with st.expander("การเก็บรักษา"):
    st.markdown(
        """
        ขนมลำไยอัญมณีควรเก็บไว้ในตู้เย็น เพื่อความสดใหม่และสามารถทานได้นานขึ้น
    """
    )

st.page_link("Home.py", label="Home", icon="↩️")
