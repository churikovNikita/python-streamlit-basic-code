import streamlit as st


option = st.multiselect(
    'What are your favorite comp',['Tesla','bmw']
)

for x in option:
    if x == 'Tesla':
        st.markdown("# первое")
    if x == 'bmw':
        st.markdown("# второе")