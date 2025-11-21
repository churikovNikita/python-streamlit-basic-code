import streamlit as st


size = st.slider('Set image size', 100, 400,200 ) # name, min val, max val, default

st.image('image2.jpg', width=size)