import streamlit as st
import os
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
            with open("pages/📷Gallery.py") as f:
                st.image(upload)
            st.success("File Uploaded Successfully.")
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
else:
    st.header("You are not admin :angry:.")