import streamlit as st

# User selects background color
color = st.color_picker("Select background color", "#0008ff")

st.markdown(
    #CSS
    f"""
    <style>
        .stApp {{
            background-color: {color} !important;
        }}

        /* Force visible label text */
        label[for^="color"] {{
            color: #000 !important;
            font-weight: 600 !important;
        }}

        /* Color picker input field style */
        input[type="color"] {{
            border: 2px solid #000 !important;
            border-radius: 6px;
            background-color: #fff !important;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
