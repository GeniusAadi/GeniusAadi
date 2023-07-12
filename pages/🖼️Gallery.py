import streamlit as st
from PIL import Image
from io import BytesIO
from pathlib import Path

st.set_page_config(page_title="Gallery", page_icon=":smile:", layout="wide")
hide_st_style = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    '''
st.markdown(hide_st_style, unsafe_allow_html=True)

# Function for downloading images
def download_image(file_path):
    with open(file_path, "rb") as f:
        image_bytes = f.read()
    return image_bytes

# Get the website root directory
root_dir = Path("my_directory")

# Check if the root directory exists
if not root_dir.exists():
    st.error("Website root directory not found.")
else:
    # Get the list of subdirectories within the root directory
    subdirs = [x for x in root_dir.iterdir() if x.is_dir()]

    # Create a selectbox for the subdirectories
    selected_dir = st.selectbox("Select a folder:", subdirs)

    if selected_dir:
        # Get the list of files within the selected subdirectory
        files = [x for x in selected_dir.iterdir() if x.is_file()]

        # Display the list of files
        st.write("Files in selected folder:")
        for file in files:
            st.write("- " + file.name)

            if selected_dir == subdirs[1]:
                # Display and download images
                image = Image.open(file)
                st.image(image, width=250, caption=file.name)

                if st.download_button("Download Image", file.name, file.name, "image/png"):
                    image_bytes = download_image(file)
                    st.success("Image downloaded successfully")

            elif selected_dir == subdirs[0]:
                # Display and download videos
                video_file = open(file, 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)

                if st.download_button("Download Video", file.name, file.name, "video/mp4"):
                    video_bytes = download_image(file)
                    st.success("Video downloaded successfully")
