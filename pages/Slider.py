import streamlit as st
st.header("Consumer Loan calc tool")

loan = st.select_slider('Amount',
                   options=[0,10000,20000,30000,40000,50000]
        )
month = st.select_slider('Month', options=[6,12,18,24,30,36,42,48,54,60]
                  )

st.write(loan * month)


 