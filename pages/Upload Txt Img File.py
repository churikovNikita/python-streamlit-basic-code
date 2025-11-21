import streamlit as st

uploaded_img = st.file_uploader("Choose an Image", accept_multiple_files=True)
uploaded_txt = st.file_uploader("Choose an Text", accept_multiple_files=True)

for images in uploaded_img:
    st.write("filename",images.name)
    st.image(images)



    
for txt in uploaded_txt:
    bytes_data = txt.read()
    st.write(bytes_data)
