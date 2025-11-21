import streamlit as st
import time

time_input = st.number_input("Enter a time")
btn = st.button('Start')


if btn:
    with st.empty():
        for seconds in range(int(time_input)):
            st.write(f"{seconds} seconds have passed")
            time.sleep(1)