import streamlit as st


name = st.text_input('What is your name?')
surname = st.text_input('What is your surname?')

btn = st.button('Show')

if btn == True:
    st.write('Hallo my freind. I don\'t forget, your name is ' + name +' '+ surname )
    #st.write(f'Welcome {name} {surname}')