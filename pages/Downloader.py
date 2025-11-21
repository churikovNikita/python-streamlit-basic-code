import streamlit as st

st.image('IMG_0285.JPG')

file_name = st.text_input('Enter File Name')

with open ('IMG_0285.JPG',"rb") as file:
    btn = st.download_button(
        label="Download Image",
        data=file,
        file_name=file_name,
        mime="image/png"
    )