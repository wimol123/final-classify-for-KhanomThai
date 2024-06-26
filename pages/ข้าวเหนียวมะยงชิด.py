import streamlit as st
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
# Get the paths from the environment (if any)
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_50_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ข้าวเหนียวมะยงชิด: เอกลักษณ์ความอร่อย หวานละมุน กลมกล่อม",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวเหนียวมะยงชิด: เอกลักษณ์ความอร่อย หวานละมุน กลมกล่อม")
st.image(kanom_img_path)
# Display header image if exists
if header_img_path and os.path.exists(header_img_path):
    st.image(header_img_path, use_column_width=True)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ข้าวเหนียวมะยงชิด เป็นขนมไทยโบราณที่ผสมผสานความหวานหอมของข้าวเหนียวมูน เข้ากับรสหวานอมเปรี้ยวของมะยงชิด ทานคู่กับกะทิหอมๆ
        มีต้นกำเนิดมาจากภูมิปัญญาไทยในอดีต นิยมทานคู่กับมะยงชิดตามฤดูกาล โดยเฉพาะในภาคตะวันออก
        """
    )

st.title("เอกลักษณ์")
with st.expander("เอกลักษณ์"):
    st.markdown(
        """
        - **ความกลมกล่อม:** รสหวานหอมของข้าวเหนียวมูน เข้ากับรสหวานอมเปรี้ยวของมะยงชิด ทานคู่กับกะทิหอมๆ ลงตัวอร่อย
        - **ความสดชื่น:** มะยงชิดมีเนื้อนุ่มฉ่ำ ทานคู่กับข้าวเหนียวมูน ช่วยคลายร้อน สดชื่น
        - **หาซื้อง่าย:** หาซื้อทานได้ง่ายในช่วงฤดูกาล ราคาไม่แพง
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        **ส่วนผสม**

        สำหรับข้าวเหนียว:
        - ข้าวเหนียวเขี้ยวงู 500 กรัม
        - กะทิ 400 มล.
        - เกลือ 1/2 ช้อนชา
        - น้ำตาลทราย 1/4 ถ้วยตวง
        - ใบเตย 2-3 ใบ

        สำหรับมะยงชิด:
        - มะยงชิดสุก 500 กรัม

        **วิธีทำ**

        1. **ทำข้าวเหนียวมูน:**
            - ล้างข้าวเหนียวเขี้ยวงูให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
            - เทน้ำออก นำข้าวเหนียวไปนึ่งจนสุก
            - ในระหว่างที่นึ่งข้าวเหนียว ให้นำกะทิ เกลือ น้ำตาลทราย ใบเตย ใส่หม้อตั้งไฟอ่อน คนจนน้ำตาลละลาย
            - เมื่อข้าวเหนียวสุก ตักใส่หม้อกะทิ คนให้เข้ากัน ปิดไฟ พักไว้ 10 นาที

        2. **เตรียมมะยงชิด:**
            - ปอกเปลือกมะยงชิด แกะเมล็ดออก หั่นเป็นชิ้นพอดีคำ

        3. **จัดเสิร์ฟ:**
            - ตักข้าวเหนียวมูนใส่จาน วางมะยงชิดสุก ราดด้วยน้ำกะทิ ทานคู่กับแตงโม หรือทานเปล่าก็อร่อย
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
