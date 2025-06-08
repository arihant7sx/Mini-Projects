import streamlit as st
from PIL import Image
from io import BytesIO


uploaded_image = st.file_uploader("Upload Image")


with st.expander("Start Camera"):
    #Starts the camera
    camera = st.camera_input("Camera")

if camera or uploaded_image :
    #create a pillow image instance
    source = uploaded_image if uploaded_image else camera
    img = Image.open(source)

    #Convert the pillow image to greyscale
    grey_img = img.convert("L")

    # Render the greyscale image on the webapp
    st.image(grey_img)

    # Convert the image to BytesIO
    buffer = BytesIO()
    grey_img.save(buffer, format="PNG")
    byte_data = buffer.getvalue()

    # Adds a download button
    st.download_button(
        label="Download Grayscale Image",
        data=byte_data,
        file_name="grayscale_image.png",
        mime="image/png"
    )
