import streamlit as st
import base64
import requests
import os
from git import Repo

class GalleryApp:
    def __init__(self, owner, repo, branch, personal_access_token):
        self.owner = owner
        self.repo = repo
        self.branch = branch
        self.personal_access_token = personal_access_token
        self.local_repo_path = "GeniusAadi/GeniusAadi"  # Replace with the local path of your repository

    def login(self):
        # Login form
        st.title("Login as Admin")
        name = st.text_input("Admin name")
        password = st.text_input("Password", type='password')
        if (name == "Rakes Rao") and (password == "R@kE$#M@th$&Mu$ic"):
            self.show_gallery()

    def show_gallery(self):
        st.title("Welcome to Gallery.")
        st.header("WELCOME Rao Sir.")
        gal = st.button("Gallery")
        if gal:
            self.display_files()
            self.upload_files()
            self.delete_files()

    def display_files(self):
        pho = st.checkbox("Photos")
        vdo = st.checkbox("Videos")
        if pho:
            photos_files = os.listdir("my_directory/photos")
            st.write("Photos:")
            for file in photos_files:
                st.write("- " + file)
        if vdo:
            videos_files = os.listdir("my_directory/videos")
            st.write("Videos:")
            for file in videos_files:
                st.write("- " + file)

    def upload_files(self):
        pho = st.checkbox("Photos")
        vdo = st.checkbox("Videos")
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

    def delete_files(self):
        pho = st.checkbox("Photos")
        vdo = st.checkbox("Videos")
        if pho or vdo:
            files = []
            if pho:
                files.extend(os.listdir("my_directory/photos"))
            if vdo:
                files.extend(os.listdir("my_directory/videos"))

            selected_files = st.multiselect("Select files to delete:", options=files)
            if st.button("Delete Selected Files"):
                if len(selected_files) == 0:
                    st.warning("No files selected.")
                else:
                    for file in selected_files:
                        file_dir = "photos" if file in files[:len(files)//2] else "videos"
                        file_path = f"my_directory/{file_dir}/{file}"
                        commit_message = "Delete file"

                        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{file_path}"
                        headers = {"Authorization": f"token {self.personal_access_token}"}
                        response = requests.get(url, headers=headers)

                        if response.status_code == 200:
                            file_data = response.json()
                            file_sha = file_data["sha"]

                            payload = {
                                "message": commit_message,
                                "sha": file_sha,
                                "branch": self.branch
                            }

                            delete_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{file_path}"
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

    app = GalleryApp(owner, repo, branch, personal_access_token)
    app.login()
