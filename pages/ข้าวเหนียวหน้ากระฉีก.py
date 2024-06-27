import streamlit as st
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get the paths from the environment (if any)
header_img_path = os.getenv("HEADER_IMG_PATH")
kanom_img_path = os.getenv("COMPONENT_52_PATH1")

# Set page configuration
st.set_page_config(
    page_title="ขนมข้าวเหนียวหน้ากระฉีก: ความเป็นมา วิธีทำ และส่วนผสม",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image(image=header_img_path)
# Display title
st.title("ขนมข้าวเหนียวหน้ากระฉีก: ความเป็นมา วิธีทำ และส่วนผสม")
st.image(kanom_img_path, width=900)
# Display header image if exists

st.title("ความเป็นมา")
with st.expander("ความเป็นมา"):
    st.markdown(
        """
        ข้าวเหนียวหน้ากระฉีก เป็นขนมไทยโบราณที่มีมายาวนาน นิยมทานคู่กับข้าวเหนียวมูน โดยเฉพาะข้าวเหนียวแดง
        นิยมทำกันในงานมงคลต่างๆ เช่น งานทำบุญ งานแต่งงาน ขนมชนิดนี้มีเอกลักษณ์ที่หน้าขนมมีลักษณะคล้ายกับรอยฉีกขาด
        มาจากการเคี่ยวน้ำตาลปี๊บกับมะพร้าวทึนทึกจนเหนียวข้น เมื่อเทใส่ถาดแล้วจะแตกเป็นรอยคล้ายฉีก
        """
    )

st.title("วิธีทำ")
with st.expander("วิธีทำ"):
    st.markdown(
        """
        1. เตรียมข้าวเหนียว:
            - แช่ข้าวเหนียวเขี้ยวงูกับข้าวเหนียวดำรวมกัน ประมาณ 3 ชั่วโมง นำไปนึ่งจนสุก
        
        2. เตรียมน้ำกะทิ:
            - นำกะทิใส่หม้อ ใส่น้ำตาลทราย เกลือป่น คนให้เข้ากัน ตั้งไฟคนจนละลายและเดือด ยกออกจากเตา
        
        3. มูนข้าวเหนียว:
            - เทข้าวเหนียวที่นึ่งสุกใส่กะทิ คนให้เข้ากัน ปิดฝาอบไว้ 10 นาที คนข้าวเหนียวอีกครั้ง ปิดฝาทิ้งไว้ 10 นาที
        
        4. ทำหน้ากระฉีก:
            - ตั้งกระทะใส่น้ำตาลปี๊บ น้ำตาลทรายแดง เกลือ และใบเตย เคี่ยวจนน้ำตาลละลายและเริ่มเหนียว
            - ใส่เนื้อมะพร้าวทึนทึกขูดฝอย เคี่ยวต่อจนส่วนผสมข้นเหนียว เทใส่ถาด รอให้เย็น
        
        5. เสิร์ฟ:
            - ตักข้าวเหนียวมูนใส่จาน ราดด้วยหน้ากระฉีก ทานคู่กับมะม่วงสุกหรือกล้วยน้ำว้า
        """
    )

st.title("ส่วนผสม")
with st.expander("ส่วนผสม"):
    st.markdown(
        """
        ข้าวเหนียวมูน:
        - ข้าวเหนียวเขี้ยวงู 1 ถ้วย
        - ข้าวเหนียวดำ 1/2 ถ้วย
        - กะทิ 400 มิลลิลิตร
        - น้ำตาลทราย 2 ช้อนโต๊ะ
        - เกลือป่น 1/4 ช้อนชา
        - ใบเตย 2-3 ใบ

        หน้ากระฉีก:
        - น้ำตาลปี๊บ 1 ถ้วย
        - น้ำตาลทรายแดง 1/2 ถ้วย
        - เกลือป่น 1/4 ช้อนชา
        - มะพร้าวทึนทึกขูดฝอย 2 ถ้วย
        - ใบเตย 2-3 ใบ
        
        หมายเหตุ:
        - สูตรนี้สามารถปรับปริมาณส่วนผสมได้ตามชอบ
        - ควรใช้มะพร้าวทึนทึกแก่จัด เนื้อจะได้กรอบ
        - น้ำตาลปี๊บสามารถเปลี่ยนเป็นน้ำตาลมะพร้าวได้
        - หน้ากระฉีกสามารถเก็บไว้ในตู้เย็นได้ประมาณ 1 อาทิตย์
        """
    )

st.title("เคล็ดลับ")
with st.expander("เคล็ดลับ"):
    st.markdown(
        """
        - ควรเลือกใช้ข้าวเหนียวเขี้ยวงู และข้าวเหนียวดำที่มีคุณภาพ
        - การเคี่ยวน้ำตาลและมะพร้าวควรเคี่ยวจนเหนียวข้น เพื่อให้ได้หน้ากระฉีกที่มีรสชาติกลมกล่อม
        - ถ้าไม่ชอบใบเตยสามารถไม่ใช้ได้
        """
    )

st.page_link("Home.py", label="Home", icon="↩️")
