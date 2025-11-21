import streamlit as st

columns = st.columns(2)
with columns[0]:
    toggle_button1 = st.toggle('Enable Title/Foto/Video/Audio')
with columns[1]:    
    toggle_button2 = st.toggle('Enable Foto/Video/Audio')




if toggle_button1:
        st.write('My FIRST Title/Foto/Video/Audio')
if toggle_button2:
        st.write('My SECONDE Foto/Video/Audio')    