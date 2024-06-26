import streamlit as st
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()
# Get the paths from the environment (if any)
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_44_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวเหนียวถั่วดำ: ขนมไทยโบราณ หอมหวาน",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวเหนียวถั่วดำ")
st.image(kanom_img_path)
# Display header image if exists
if header_img_path and os.path.exists(header_img_path):
    st.image(header_img_path, use_column_width=True)

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ข้าวเหนียวถั่วดำ เป็นขนมไทยโบราณที่มีมาช้านาน นิยมทำกันในงานมงคลต่างๆ เช่น 
        งานแต่งงาน งานขึ้นบ้านใหม่ ขนมชนิดนี้มีลักษณะเป็นข้าวเหนียวมูนสีขาว 
        ราดด้วยถั่วดำต้มกะทิสีดำสนิท รสชาติหวานมัน หอมกลิ่นกะทิ ทานคู่กับมะม่วงสุกหรือกล้วยน้ำว้าก็อร่อย
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมข้าวเหนียวมูน:
            1. ล้างข้าวเหนียวเขี้ยวงูให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
            2. ผสมกะทิ น้ำตาลทราย เกลือ และใบเตย ตั้งไฟปานกลาง กวนจนน้ำตาลละลายและกะทิเริ่มเดือด
            3. เทกะทิที่ผสมไว้ลงไปในข้าวเหนียวที่แช่น้ำไว้ คลุกเคล้าให้เข้ากันจนข้าวเหนียวดูดกะทิหมด
            4. เทข้าวเหนียวที่คลุกกะทิลงในตะกร้า นึ่งด้วยไฟปานกลางประมาณ 40-50 นาที หรือจนข้าวเหนียวสุก
            5. เมื่อข้าวเหนียวสุกแล้ว ยกออกจากเตานึ่ง พักไว้ให้เย็น
        
        2. เตรียมถั่วดำต้มกะทิ:
            1. ล้างถั่วดำให้สะอาด แช่น้ำไว้ 3-4 ชั่วโมง
            2. ต้มถั่วดำกับน้ำเปล่าจนเปื่อยนุ่ม
            3. เทกะทิ น้ำตาลปี๊บ เกลือ ลงในหม้อต้มถั่วดำ เคี่ยวต่อจนน้ำกะทิข้นหนืด
            4. ปิดไฟ พักไว้ให้เย็น
        
        3. จัดเสิร์ฟ:
            1. ตักข้าวเหนียวมูนใส่ถ้วย
            2. ราดด้วยถั่วดำต้มกะทิ
            3. ทานคู่กับมะม่วงสุกหรือกล้วยน้ำว้า
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        สำหรับข้าวเหนียวมูน:
        - ข้าวเหนียวเขี้ยวงู 1 ถ้วยตวง
        - กะทิ 1 ถ้วยตวง
        - น้ำตาลทราย 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        - ใบเตย 2-3 ใบ (สำหรับหอม)

        สำหรับถั่วดำต้มกะทิ:
        - ถั่วดำ 1 ถ้วยตวง
        - กะทิ 2 ถ้วยตวง
        - น้ำเปล่า 1 ถ้วยตวง
        - น้ำตาลปี๊บ 1/2 ถ้วยตวง
        - เกลือ 1/4 ช้อนชา
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - เลือกใช้ข้าวเหนียวเขี้ยวงู จะทำให้เนื้อข้าวเหนียวมีกลิ่นหอมและมีความเหนียวนุ่ม
        - กะทิควรใช้กะทิสด จะทำให้ขนมมีรสชาติหอมมันอร่อย
        - น้ำตาลทรายและน้ำตาลปี๊บสามารถปรับเพิ่มหรือลดได้ตามชอบ
        - ใบเตยสามารถใส่หรือไม่ใส่ก็ได้
        - ถั่วดำควรต้มจนเปื่อยนุ่ม จะได้เนื้อสัมผัสที่เนียนละมุน
        """
    )

# Link to home page or another page
st.page_link("Home.py", label="Home", icon="↩️")
