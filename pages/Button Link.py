import streamlit as st


col = st.columns(3)
with col[0]:
    btn_JS = st.link_button("JS Course",url='https://google.com')
with col[1]:
    btn_PY = st.link_button("PY Course",url='https://google.com')
with col[2]:
    btn_J = st.link_button("Java Course",url='https://google.com')