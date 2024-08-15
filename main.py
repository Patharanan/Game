import streamlit as st
import os
from datetime import datetime

# กำหนดรายการของป้ายแต่ละด้าน
rewards = {
    "กล่อง 1": {"front": "images/2.png", "back": "images/1.png"},
    "กล่อง 2": {"front": "images/3.png", "back": "images/1.png"},
    "กล่อง 3": {"front": "images/4.png", "back": "images/1.png"},
}

def main():
    st.set_page_config(page_title="เกมเปิดป้ายสุ่ม", page_icon="🎲")

    # หน้าต้อนรับสำหรับกรอกข้อมูล
    if 'started' not in st.session_state:
        st.session_state.started = False

    if not st.session_state.started:
        st.title("Welcome random gift  for you ")
        st.write("Fill in your details to get started.")

        name = st.text_input("Name:")
        gf_name = st.text_input("Name Girlfriend:")
        date = st.date_input("Date:", min_value=datetime.today())
        
        if st.button("Start"):
            if name and date:
                st.session_state.name = name
                st.session_state.date = date
                st.session_state.started = True
            else:
                st.error("กรุณากรอกข้อมูลให้ครบ")
    else:
        # หน้าหลักของเกม
        st.title(f"CarePhat - will give you what you can open {st.session_state.name}!")
        st.write(f"วันที่: {st.session_state.date}")
        
        # สร้างสถานะสำหรับเก็บสถานะการเปิดของแต่ละกล่อง
        if 'flipped' not in st.session_state:
            st.session_state.flipped = {key: False for key in rewards.keys()}

        # ฟังก์ชันเพื่อจัดการการพลิกป้าย
        def flip_box(box_name):
            # รีเซ็ตสถานะการเปิดของทุกกล่องให้เป็น False ก่อน
            for key in st.session_state.flipped.keys():
                st.session_state.flipped[key] = False
            # เปิดกล่องที่ถูกคลิก
            st.session_state.flipped[box_name] = True
            st.balloons()  # เพิ่มลูกเล่นบอลลูน

        # ขนาดที่ต้องการสำหรับรูปภาพ
        image_width = 700  # ปรับความกว้างของรูปภาพ

        # สร้างแถวสำหรับปุ่มและรูปภาพ
        for i, (box_name, images) in enumerate(rewards.items()):
            # จัดกลุ่มปุ่มและรูปภาพใน container
            with st.container():
                # ตรวจสอบสถานะการพลิกและแสดงภาพ
                image_path = images["front"] if st.session_state.flipped[box_name] else images["back"]

                # ตรวจสอบว่าไฟล์ภาพมีอยู่
                if os.path.exists(image_path):
                    st.image(image_path, use_column_width=False, width=image_width)
                    
                    # ปุ่มพลิกที่อยู่ใต้ภาพ
                    if st.button(f"Open Box", key=f"flip_{box_name}"):
                        flip_box(box_name)
                        st.success(f"Open {box_name} and found this!")
                else:
                    st.error(f"ไม่สามารถหาไฟล์: {image_path}")

            # เพิ่มช่องว่างระหว่างแถว
            st.write("")

if __name__ == "__main__":
    main()
