import streamlit as st
import os
from datetime import datetime


rewards = {
    "กล่อง 1": {"front": "images/2.png", "back": "images/1.png"},
    "กล่อง 2": {"front": "images/3.png", "back": "images/1.png"},
    "กล่อง 3": {"front": "images/4.png", "back": "images/1.png"},
}

def main():
    st.set_page_config(page_title="Game for baby", page_icon="🎲")
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
        st.title(f"CarePhat - will give you what you can open {st.session_state.name}!")
        st.write(f"วันที่: {st.session_state.date}")
        if 'flipped' not in st.session_state:
            st.session_state.flipped = {key: False for key in rewards.keys()}

        def flip_box(box_name):
            for key in st.session_state.flipped.keys():
                st.session_state.flipped[key] = False
            st.session_state.flipped[box_name] = True
            st.balloons()  
        image_width = 700 

        for i, (box_name, images) in enumerate(rewards.items()):
            with st.container():
                image_path = images["front"] if st.session_state.flipped[box_name] else images["back"]
                if os.path.exists(image_path):
                    st.image(image_path, use_column_width=False, width=image_width)
                    if st.button(f"Open Box", key=f"flip_{box_name}"):
                        flip_box(box_name)
                        st.success(f"Open {box_name} and found this!")
                else:
                    st.error(f"ไม่สามารถหาไฟล์: {image_path}")
            st.write("")

if __name__ == "__main__":
    main()
