import streamlit as st
import os

st.set_page_config(page_title="Admin Login", page_icon=':page_with_curl:', layout="wide")
hide_st_style = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    '''
st.markdown(hide_st_style, unsafe_allow_html=True)

def file(pho, vdo):
    upload = None
    if pho:
        upload = st.file_uploader("Upload Photos", type=["png", "jpg", "pdf", "gif", "tiff", "psd", "eps", "ai", "indd", "raw"])
    elif vdo:
        upload = st.file_uploader("Upload Videos", type=["webm", "mpg", "mp2", "mpeg", "mpe", "mpv", "ogg", "mp4", "m4p", "m4v", "avi", "wmv", "mov", "qt", "flv", "swf", "avchd"])
    return upload

def store(upload, pho, vdo):
    if upload is not None:
        if pho:
            with open(os.path.join("my_directory/photos", upload.name), "wb") as f:
                f.write(upload.getbuffer())
            st.image(upload)
        elif vdo:
            with open(os.path.join("my_directory/videos", upload.name), "wb") as f:
                f.write(upload.getbuffer())
            st.video(upload)
        st.success("File Uploaded Successfully.")

def delete_selected_files(selected_files):
    # Delete selected files from the "photos" directory
    for file in selected_files:
        os.remove(os.path.join("my_directory/photos", file))
    
    # Delete selected files from the "videos" directory
    for file in selected_files:
        os.remove(os.path.join("my_directory/videos", file))
    
    st.success("Selected files have been deleted.")

st.title("Login as Admin")
name = st.text_input("Admin name")
password = st.text_input("Password", type='password')

logged_in = False

if (name == "Rakes Rao") and (password == "R@kE$#M@th$&Mu$ic"):
    logged_in = True

if logged_in:
    st.title("Welcome to Gallery.")
    st.header("WELCOME Rao Sir.")
    gal = st.button("Gallery")
    
    if gal:
        pho = st.checkbox("Photos")
        vdo = st.checkbox("Videos")
        upload = file(pho, vdo)
        store(upload, pho, vdo)
        
        rm = st.button("Delete")
        
        if rm:
            photos_files = os.listdir("my_directory/photos")
            videos_files = os.listdir("my_directory/videos")
            
            # Display checkboxes for all files in the "photos" directory
            photos_files_selected = st.multiselect("Select photos to delete:", options=photos_files)

            # Display checkboxes for all files in the "videos" directory
            videos_files_selected = st.multiselect("Select videos to delete:", options=videos_files)

            if st.button("Delete Selected Files"):
                selected_files = photos_files_selected + videos_files_selected
                if len(selected_files) == 0:
                    st.warning("No files selected.")
                else:
                    delete_selected_files(selected_files)

if not logged_in:
    st.header("You are not admin :angry:.")
