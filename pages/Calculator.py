import streamlit as st


f_number = st.number_input('First number')
s_number = st.number_input('Second number')


column = st.columns(4)

with column[0]:
    btn_add = st.button('Addition (+)')
with column[1]:
    btn_sub = st.button('Subtraction (-)')
with column[2]:
    btn_mul = st.button('Multiplication (*)')
with column[3]:
    btn_div = st.button('Division (/)')


if btn_add:
    st.write(f'{f_number+s_number}')
if btn_sub:
    st.write(f'{f_number-s_number}')
if btn_mul:
    st.write(f'{f_number*s_number}')
if btn_div:
    st.write(f'{f_number/s_number}')
