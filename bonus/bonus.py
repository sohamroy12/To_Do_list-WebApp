import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    #Started Camera
    camera_image = st.camera_input("Camera")
    if camera_image:
        # Create a pillow Image instance
        img = Image.open(camera_image)

        # Convert the pillow image to grayscale
        gray_img = img.convert("L")

        # Render the grayscale image on the web page
        st.image(gray_img)

with st.expander("Upload Image"):
    uploaded_image = st.file_uploader("Upload Image")
    if uploaded_image:
        img = Image.open(uploaded_image)
        gray_img = img.convert("L")
        st.image(gray_img)

