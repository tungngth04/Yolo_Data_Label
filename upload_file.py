import streamlit as st
import os

st.title("Uploading files")
st.markdown("---")

#Upload multiple files
images = st.file_uploader("Please upload an image", type=['png','jpg','jpeg','gif','psd'], accept_multiple_files=True)

if images is not None:
    #path to connect
    destination_folder = "E:/python/private/imagesss"
    
    for image in images:
        st.image(image)
        st.write(image.name)
        
        #path, read and write open file
        with open(os.path.join(destination_folder,image.name),"wb") as file:
            
            file.write(image.getbuffer())
        st.success("File saved success")