import streamlit as st


if "disabled" not in st.session_state:  # ← проверяете "disabled"
    st.session_state.disabled = False   # ← устанавливаете "disabled"


radio_button = st.radio('Choose somethink',["HTML", "JS", "Zero Code"], index=None,
                        key="visible", 
                        disabled=st.session_state.disabled) # то что проверяю я строка 4 и 5



if radio_button == "JS":
    st.code('println("Hello JAVAscript")')
    st.session_state.disabled = True
if radio_button == "HTML":
        st.code('<h1>HEY Html</h1>')
if radio_button == "Zero Code":
        st.code('No cOde just chill')
