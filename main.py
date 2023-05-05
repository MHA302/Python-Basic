# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st

from converter import convert_image

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")
# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_uploaded_image = convert_image(uploaded_image)
    st.image(gray_uploaded_image)

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    gray_camera_image = convert_image(camera_image)
    st.image(gray_camera_image)

