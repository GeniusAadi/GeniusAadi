import streamlit as st
import base64
#from streamlit_extras.switch_page_button import switch_page
import os
#To connect github and upload
import requests
# GitHub repository information
owner = "GeniusAadi"
repo = "GeniusAadi"
branch = "main" 
#file_path = "path/to/your/file.txt"  # path to the file you want to upload
commit_message = "Upload file"
#Setting page heading
st.set_page_config(page_title="Admin Login", page_icon=':page_with_curl:', layout="wide")
hide_st_style = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    '''
st.markdown(hide_st_style, unsafe_allow_html=True)
#function to upload photos and videos
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
#function to store photos and videos
def store():
    global upload
    upload = file()
    upd = st.button("Upload")

    # Initialize session state
    if "upd_state" not in st.session_state:
        st.session_state.upd_state = False

    if upd or st.session_state.upd_state:
        st.session_state.upd_state = True

        if upload is not None:
            file_content = upload.getvalue()
            file_content_base64 = base64.b64encode(file_content).decode("utf-8")
            file_path = f"my_directory/{'photos' if pho else 'videos'}/{upload.name}"
            commit_message = "Upload file"

            # Create the file payload
            payload = {
                "message": commit_message,
                "content": file_content_base64,
                "branch": branch
            }

            # Create the file on GitHub
            url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
            headers = {"Authorization": f"token {personal_access_token}"}
            response = requests.put(url, json=payload, headers=headers)

            if response.status_code == 201:
                st.success("File uploaded successfully.")
                st.image(upload) if pho else st.video(upload)
            else:
                st.error("Failed to upload file.")
                st.error(f"Response: {response.text}")

            #switch_page("Gallery")
# Function to delete selected files
def delete_selected_files(selected_files):
    if len(selected_files) == 0:
        st.warning("No files selected.")
        return

    # Delete selected files from GitHub
    for file in selected_files:
        file_path = f"my_directory/photos/{file}" if os.listdir("my_directory/photos") else f"my_directory/videos/{file}"
        commit_message = "Delete file"

        # Get the file's current SHA
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
        headers = {"Authorization": f"token {personal_access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            file_data = response.json()
            file_sha = file_data["sha"]

            # Create the deletion payload
            payload = {
                "message": commit_message,
                "sha": file_sha,
                "branch": branch
            }

            # Delete the file on GitHub
            delete_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
            delete_response = requests.delete(delete_url, json=payload, headers=headers)

            if delete_response.status_code == 200:
                st.success(f"File '{file}' deleted successfully.")
            else:
                st.error(f"Failed to delete file '{file}'.")
                st.error(f"Response: {delete_response.text}")
        else:
            st.error(f"Failed to retrieve file data for '{file}'.")
            st.error(f"Response: {response.text}")

    st.success("Selected files have been deleted.")

#Login form
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
