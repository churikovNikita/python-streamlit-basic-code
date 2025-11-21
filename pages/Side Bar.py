import streamlit as st




with st.sidebar:
    option = st.selectbox('How would you like to be contacted',['Email','Telefon'],)
    info = st.text_input('Info')
    btn_radio = st.radio('Choose shipping methode', ['Standard(5 - 15days)', 'Express 3-5days'])