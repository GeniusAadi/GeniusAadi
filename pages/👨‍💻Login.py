import streamlit as st
import base64
import requests
import os
from git import Repo

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class GalleryApp:
    def __init__(self, owner, repo, branch, personal_access_token):
        self.owner = owner
        self.repo = repo
        self.branch = branch
        self.personal_access_token = personal_access_token
        self.local_repo_path = "path/to/local/repo"  # Replace with the local path of your repository

    def login(self):
        # Login form
        st.title("Login as Admin")
        name = st.text_input("Admin name", key="admin_name")
        password = st.text_input("Password", type='password', key="admin_password")
        lg = st.button("Login")
        
        # Initialize session state for login
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        
        # Check if already logged in
        if st.session_state.logged_in:
            self.show_gallery()
            return
        
        if lg:
            if (name == "Rakes Rao") and (password == "R@kE$#M@th$&Mu$ic"):
                st.session_state.logged_in = True
                self.show_gallery()
            else:
                st.header("You are not admin :angry:.")

    def show_gallery(self):
        # Display "Welcome to Gallery" only if logged in
        if st.session_state.logged_in:
            st.title("Welcome to Gallery.")
            st.header("WELCOME Rao Sir.")
        
        gallery_placeholder = st.empty()
        
        # Initialize session state for gallery button
        if "gallery_shown" not in st.session_state:
            st.session_state.gallery_shown = False
        
        if st.session_state.logged_in and (st.session_state.gallery_shown or gallery_placeholder.button("Gallery")):
            st.session_state.gallery_shown = True
            self.upload_files()
            self.delete_files()

    def upload_files(self):
        pho = st.checkbox("Photos", key="upload_photos_checkbox")
        vdo = st.checkbox("Videos", key="upload_videos_checkbox")
    
        if pho or vdo:
            upload = st.file_uploader("Upload Files", type=["png", "jpg", "pdf", "gif", "tiff", "psd", "eps", "ai", "indd", "raw", "webm", "mpg", "mp2", "mpeg", "mpe", "mpv", "ogg", "mp4", "m4p", "m4v", "avi", "wmv", "mov", "qt", "flv", "swf", "avchd"])
    
            if upload is not None:
                file_content = upload.getvalue()
                file_content_base64 = base64.b64encode(file_content).decode("utf-8")
                file_path = f"my_directory/{'photos' if pho else 'videos'}/{upload.name}"
                commit_message = "Upload file"
    
                payload = {
                    "message": commit_message,
                    "content": file_content_base64,
                    "branch": self.branch
                }
    
                url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{file_path}"
                headers = {"Authorization": f"token {self.personal_access_token}"}
                response = requests.put(url, json=payload, headers=headers)
    
                if response.status_code == 201:
                    st.success("File uploaded successfully.")
                    st.image(upload) if pho else st.video(upload)
                    self.commit_and_push_changes(commit_message)
                else:
                    st.error("Failed to upload file.")
                    st.error(f"Response: {response.text}")
                    # Print the full response for debugging purposes
                    # st.write(response.json())


    def delete_files(self):
        rm = st.button("Delete")
        
        # Initialize session state
        if "delete_shown" not in st.session_state:
            st.session_state.delete_shown = False
        
        if rm or st.session_state.delete_shown:
            st.session_state.delete_shown = True
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
                    self.delete_selected_files(selected_files)

    def delete_selected_files(self, selected_files):
        # Delete selected files from GitHub
        for file in selected_files:
            file_path = f"my_directory/photos/{file}" if os.listdir("my_directory/photos") else f"my_directory/videos/{file}"
            commit_message = "Delete file"
    
            # Get the file's current SHA
            url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{file_path}"
            headers = {"Authorization": f"token {self.personal_access_token}"}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                file_data = response.json()
                file_sha = file_data["sha"]
    
                # Create the deletion payload
                payload = {
                    "message": commit_message,
                    "sha": file_sha,
                    "branch": self.branch
                }
    
                # Delete the file on GitHub
                delete_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{file_path}"
                headers = {"Authorization": f"token {self.personal_access_token}"}
                delete_response = requests.delete(delete_url, json=payload, headers=headers)
    
                if delete_response.status_code == 200:
                    st.success(f"File '{file}' deleted successfully.")
                else:
                    st.error(f"Failed to delete file '{file}'.")
                    st.error(f"Response: {delete_response.text}")
            else:
                st.error(f"Failed to retrieve file data for '{file}'.")
                st.error(f"Response: {response.text}")

    def commit_and_push_changes(self, commit_message):
        repo = Repo(self.local_repo_path)
        repo.git.add(".")
        repo.index.commit(commit_message)
        origin = repo.remote("origin")
        origin.push()

if __name__ == "__main__":
    owner = "GeniusAadi"
    repo = "GeniusAadi"
    branch = "main"
    personal_access_token = "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"

    session_state = SessionState(logged_in=False)
    app = GalleryApp(owner, repo, branch, personal_access_token)
    app.login()
    #app.show_gallery()
