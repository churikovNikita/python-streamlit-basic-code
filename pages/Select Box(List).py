import streamlit as st

st.header('Choose Your Car')

option = st.selectbox ('Which car',['bmw','audi', 'porsche'])

st.write(option)