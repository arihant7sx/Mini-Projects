import streamlit as st
from PIL import Image
from io import BytesIO

with st.expander("Start Camera"):
    #Starts the camera
    camera = st.camera_input("Camera")

if camera :
    #create a pillow image instance
    img = Image.open(camera)

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
