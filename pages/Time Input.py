import streamlit as st


fs_team = st.text_input('First Team')
scd_team = st.text_input('Second Team')

time = st.time_input('Set an alarm for',value=None)

btn_show = st.button('Show')

if btn_show:
    st.write(f'The match the Liverpool and the Chelsea will start at {time}')