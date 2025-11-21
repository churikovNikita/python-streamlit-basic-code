import streamlit as st

list = []
txt = st.text_area(
    "Text to analyze",placeholder="Write text", max_chars=100)

analyze_btn = st.button('Analyze')

if analyze_btn:
    text_split = txt.split(sep=" ") # create new list wh
    st.write(f'You wrote {len(txt)} characters. And {len(text_split)} words')