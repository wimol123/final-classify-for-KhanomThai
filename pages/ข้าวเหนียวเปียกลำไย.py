import streamlit as st
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
# Get the paths from the environment (if any)
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_48_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ข้าวเหนียวเปียกลำไย: เอกลักษณ์ความอร่อย หอมหวาน ชื่นใจ",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวเหนียวเปียกลำไย")
st.image(kanom_img_path, width=900)
# Display header image if exists

st.title("เอกลักษณ์ของข้าวเหนียวเปียกลำไย")
with st.expander("เอกลักษณ์ของข้าวเหนียวเปียกลำไย"):
    st.markdown(
        """
        - ความหอมหวาน: ข้าวเหนียวมูนหอมมัน กะทิหอมกลมกล่อม ผสมผสานกับความหวานฉ่ำของลำไย อร่อยลงตัว
        - ความชื่นใจ: ทานคู่กับน้ำกะทิเย็นๆ ชื่นใจ คลายร้อน
        - หาซื้อง่าย: หาซื้อทานได้ง่าย ราคาไม่แพง
        """
    )

st.title("วิธีทำข้าวเหนียวเปียกลำไย")
with st.expander("วิธีทำข้าวเหนียวเปียกลำไย"):
    st.markdown(
        """
        **ส่วนผสม**

        - **ข้าวเหนียว:**
            - ข้าวเหนียวเขี้ยวงู 500 กรัม
            - กะทิ 400 มล.
            - เกลือ 1/2 ช้อนชา
            - น้ำตาลทราย 1/4 ถ้วยตวง
            - ใบเตย 2-3 ใบ

        - **ลำไย:**
            - ลำไยแกะเปลือก 500 กรัม
            - น้ำเปล่า 1 ถ้วยตวง
            - น้ำตาลทราย 1/4 ถ้วยตวง (หรือตามชอบ)

        - **น้ำกะทิ:**
            - กะทิ 400 มล.
            - เกลือ 1/4 ช้อนชา
            - น้ำตาลทราย 1/4 ถ้วยตวง (หรือตามชอบ)
            - ใบเตย 2-3 ใบ

        **วิธีทำ**

        1. **ทำข้าวเหนียวมูน:**
            - ล้างข้าวเหนียวเขี้ยวงูให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
            - เทน้ำออก นำข้าวเหนียวไปนึ่งจนสุก
            - ในระหว่างที่นึ่งข้าวเหนียว ให้นำกะทิ เกลือ น้ำตาลทราย ใบเตย ใส่หม้อตั้งไฟอ่อน คนจนน้ำตาลละลาย
            - เมื่อข้าวเหนียวสุก ตักใส่หม้อกะทิ คนให้เข้ากัน ปิดไฟ พักไว้ 10 นาที

        2. **ต้มลำไย:**
            - ลำไยแกะเปลือก แช่น้ำเกลือไว้ 10 นาที ล้างน้ำสะอาด พักไว้
            - ตั้งหม้อใส่น้ำเปล่า น้ำตาลทราย ใบเตย ต้มจนน้ำตาลละลาย เดือด
            - ใส่ลำไย ต้มต่อจนลำไยใส ปิดไฟ พักไว้

        3. **ทำน้ำกะทิ:**
            - ให้นำกะทิ เกลือ น้ำตาลทราย ใบเตย ใส่หม้อตั้งไฟอ่อน คนจนน้ำตาลละลาย ปิดไฟ

        4. **จัดเสิร์ฟ:**
            - ตักข้าวเหนียวมูนใส่ถ้วย ราดด้วยน้ำกะทิ และลำไย ทานร้อนๆ หรือเย็นๆ ก็อร่อย
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
