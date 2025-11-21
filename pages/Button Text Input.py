import streamlit as st

car_types = ['toyota','fiat', 'ford', 'bmw']

car = st.text_input('Type an car') 

button = st.button('Check Avaliability')
 
if button == True:
    have_it = car.lower() in car_types
    if have_it:
        st.write('We have it')
    else:
        st.write('Not listed')