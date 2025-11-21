import streamlit as st


tab1, tab2, tab3 = st.tabs(["Football", "Tennis", "Basket"])

with tab1:
    st.header("Football")
with tab2:
    st.header("Tennis")
with tab3:
    st.header("Basket")