import streamlit as st
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
# Get the paths from the environment (if any)
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_47_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ข้าวเหนียวปิ้ง: เอกลักษณ์ความอร่อย หอมกรุ่น กินเพลิน",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ข้าวเหนียวปิ้ง")
st.image(kanom_img_path)
# Display header image if exists
if header_img_path and os.path.exists(header_img_path):
    st.image(header_img_path, use_column_width=True)

st.title("เอกลักษณ์ของข้าวเหนียวปิ้ง")
with st.expander("เอกลักษณ์ของข้าวเหนียวปิ้ง"):
    st.markdown(
        """
        - ความหอม: ข้าวเหนียวมูนห่อใบตอง ปิ้งบนเตาถ่าน ส่งกลิ่นหอมกรุ่นชวนรับประทาน
        - ความอร่อย: ข้าวเหนียวมูนนุ่ม หอม หวานมัน ทานคู่กับไส้ต่างๆ อร่อยลงตัว
        - ความสะดวก: หาซื้อทานได้ง่าย ราคาไม่แพง
        """
    )

st.title("วิธีทำข้าวเหนียวปิ้ง")
with st.expander("วิธีทำข้าวเหนียวปิ้ง"):
    st.markdown(
        """
        **ส่วนผสม**

        - **ข้าวเหนียว:**
            - ข้าวเหนียวเขี้ยวงู 500 กรัม
            - กะทิ 400 มล.
            - เกลือ 1/2 ช้อนชา
            - น้ำตาลทราย 1/4 ถ้วยตวง
            - ใบเตย 2-3 ใบ

        - **ไส้:**
            - กล้วยนวล 3-4 ผล
            - เผือก 200 กรัม
            - มะพร้าวขูด 1/2 ถ้วยตวง
            - น้ำตาลทราย 2 ช้อนโต๊ะ (หรือตามชอบ)
            - เกลือ 1/4 ช้อนชา
            - ใบตองสำหรับห่อ

        **วิธีทำ**

        1. **ทำข้าวเหนียวมูน:**
            - ล้างข้าวเหนียวเขี้ยวงูให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
            - เทน้ำออก นำข้าวเหนียวไปนึ่งจนสุก
            - ในระหว่างที่นึ่งข้าวเหนียว ให้นำกะทิ เกลือ น้ำตาลทราย ใบเตย ใส่หม้อตั้งไฟอ่อน คนจนน้ำตาลละลาย
            - เมื่อข้าวเหนียวสุก ตักใส่หม้อกะทิ คนให้เข้ากัน ปิดไฟ พักไว้ 10 นาที

        2. **ทำไส้:**
            - ไส้กล้วย: กล้วยนวล ต้มจนสุก บดให้ละเอียด ผสมน้ำตาลทราย เกลือ พักไว้
            - ไส้เผือก: เผือกนึ่งจนสุก บดให้ละเอียด ผสมน้ำตาลทราย เกลือ มะพร้าวขูด พักไว้

        3. **ห่อข้าวเหนียว:**
            - ตัดใบตองเป็นสี่เหลี่ยม ตักข้าวเหนียวมูนใส่ลงไป ตามด้วยไส้ที่ชอบ ห่อให้มิดชิด

        4. **ปิ้งข้าวเหนียว:**
            - ตั้งเตาถ่าน รอจนถ่านร้อน นำข้าวเหนียวที่ห่อใบตองไปปิ้งจนสุกเหลือง หอมกรุ่น
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
