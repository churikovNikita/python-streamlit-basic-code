import streamlit as st

tab1, tab2, tab3 = st.tabs(["Football", "Tennis", "Box"])

with tab1:
    
    st.header("Football")
    with st.expander("See description"):
        st.write('Is not very interested')
with tab2:
    st.header("Tennis")

with tab3:
    st.header("Box")

