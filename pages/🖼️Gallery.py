import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Gallery", page_icon=":smile:", layout="wide")

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
    #st.progress(100)
    #st.snow()
    #st.balloons()

# display the list of files
st.write("Files in selected folder:")
for file in files:
    #st.image(file) or st.video(file)
    #st.download_button("Download File",file)
    #fbr=st.file_browser("Select a file")
    st.write("- " + file.name)
