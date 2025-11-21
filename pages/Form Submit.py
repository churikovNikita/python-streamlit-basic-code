import streamlit as st


with st.form("My form"):
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    age = st.slider('Age',1,100,20)
    start_day = st.date_input('Start Day')
    submitted = st.form_submit_button("Submit")