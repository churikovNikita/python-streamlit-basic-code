import streamlit as st



checks = st.columns(2)
with checks[0]:
    images = st.checkbox('Photos to see?')
with checks[1]:
    codes = st.checkbox('Code to see?')

if images:
    with checks[0]:
        st.title("You see fotos")
if codes:
    with checks[1]:
        st.code('printf("%s",myBestCode)')
