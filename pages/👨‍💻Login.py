import streamlit as st
#from streamlit_extras.switch_page_button import switch_page
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
def file():
    global upload
    if pho:
        upload = st.file_uploader("Upload Photos",type=["png","jpg","pdf","gif","tiff","psd","eps","ai","indd","raw"])
        if upload is not None:
            return upload
    elif vdo:
        upload = st.file_uploader("Upload Videos",type=["webm","mpg","mp2","mpeg","mpe","mpv","ogg","mp4","m4p","m4v","avi","wmv","mov","qt","flv","swf","avchd"])
        if upload is not None:
            return upload
def store():
    global upload
    upload=file()
    upd=st.button("Upload")
    #initialize session state
    if "upd_state" not in st.session_state:
        st.session_state.upd_state = False
    if upd or st.session_state.upd_state:
        st.session_state.upd_state = True
        if upload is not None:
            if pho:
                with open(os.path.join("my_directory/photos",upload.name),"wb") as f:
                    f.write(upload.getbuffer())
                st.image(upload)
            elif vdo:
                with open(os.path.join("my_directory/videos",upload.name),"wb") as f:
                    f.write(upload.getbuffer())
                st.video(upload)
            st.success("File Uploaded Successfully.")
            #switch_page("Gallery")
# Function to delete selected files
def delete_selected_files(selected_files):
    # Delete selected files from the "photos" directory
    if os.listdir("my_directory/photos"):
        for file in selected_files:
            os.remove(os.path.join("my_directory/photos", file))
    # Delete selected files from the "videos" directory
    else:
        for file in selected_files:
            os.remove(os.path.join("my_directory/videos", file))
    st.success("Selected files have been deleted.")
st.title("Login as Admin")
name=st.text_input("Admin name")
password=st.text_input("Password",type='password')
if (name=="Rakes Rao") and (password=="R@kE$#M@th$&Mu$ic"):
    lg=st.button("Login")
    #initialize session state
    if "lg_state" not in st.session_state:
        st.session_state.lg_state = False
    if lg or st.session_state.lg_state:
        st.session_state.lg_state = True
        st.title("Welcome to Gallery.")
        st.header("WELCOME Rao Sir.")
        gal=st.button("Gallery")
        #initialize session state
        if "gal_state" not in st.session_state:
            st.session_state.gal_state = False
        if gal or st.session_state.gal_state:
            st.session_state.gal_state = True
            pho=st.checkbox("Photos")
            vdo=st.checkbox("Videos")
            store()
            rm=st.button("Delete")
            #initialize session state
            if "rm_state" not in st.session_state:
                st.session_state.rm_state = False
            if rm or st.session_state.lg_state:
                st.session_state.rm_state = True
                # Display checkboxes for all files in the "photos" directory
                photos_files = os.listdir("my_directory/photos")
                photos_files_selected = st.multiselect("Select photos to delete:", options=photos_files)

                # Display checkboxes for all files in the "videos" directory
                videos_files = os.listdir("my_directory/videos")
                videos_files_selected = st.multiselect("Select videos to delete:", options=videos_files)

                # Create a button to delete selected files
                if st.button("Delete Selected Files"):
                    if len(photos_files_selected) == 0 and len(videos_files_selected) == 0:
                        st.warning("No files selected.")
                    else:
                        selected_files = photos_files_selected + videos_files_selected
                        delete_selected_files(selected_files)
else:
    st.header("You are not admin :angry:.")
