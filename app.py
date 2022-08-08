import streamlit as st
from page_shuffler.utils import processPDF

uploaded_file = st.file_uploader('Choose a file',type='pdf')

processed_file = None

if uploaded_file:
    with st.spinner('Wait for it...'):
        processed_file = processPDF(uploaded_file)
    
if uploaded_file and processed_file is not None:
    st.download_button(label="Download scrambled PDF",
                    data=processed_file,
                    file_name=uploaded_file.name.split('.pdf')[0] + " - [Scrambled].pdf",
                    mime='application/octet-stream')