import streamlit as st
from PIL import Image
from io import BytesIO
from pathlib import Path

st.set_page_config(page_title="Gallery", page_icon=":smile:", layout="wide")
#function for downloading both videos and photos
def download_image(url):
    with open(url, "r+", encoding="latin1") as f:
        url_bytes=f.read()
        f.write(url_bytes)

# get the website root directory
root_dir = Path("my_directory")

# check if the root directory exists
if not root_dir.exists():
    st.error("Website root directory not found.")
if root_dir is not None:
    # get the list of subdirectories within the root directory
    subdirs = [x for x in root_dir.iterdir() if x.is_dir()]

    # create a selectbox for the subdirectories
    selected_dir = st.selectbox("Select a folder:", subdirs)

    # get the list of files within the selected subdirectory
    files = [x for x in selected_dir.iterdir() if x.is_file()]

# display the list of files
st.write("Files in selected folder:")
for file in files:
    st.write("- " + file.name)
    if selected_dir == subdirs[0]:
        image_paths= Image.open(file)
        with BytesIO() as output:
            image_paths.save(output, format='PNG')
            image_bytes = output.getvalue()
        if st.download_button("Download Image",image_bytes,file_name=file.name,mime="png/jpg/pdf/gif/tiff/psd/eps/ai/indd/raw"):
            download_image(file)
            st.success("Image downloaded successfully")
        st.image(image_paths, width=250, caption=image_paths)
    elif selected_dir == subdirs[1]:
        video_file = open(file, 'rb')
        video_bytes = video_file.read()
        if st.download_button("Download Video",video_bytes,file_name=file.name,mime="video/webm/mpg/mp2/mpeg/mpe/mpv/ogg/mp4/m4p/m4v/avi/wmv/mov/qt/flv/swf/avchd"):
            download_image(file)
            st.success("Video downloaded successfully")
        st.video(video_bytes)
