def delete_files(self):
    pho = st.checkbox("Photos", key="delete_photos_checkbox")
    vdo = st.checkbox("Videos", key="delete_videos_checkbox")
    if pho or vdo:
        files = []
        if pho:
            files.extend(os.listdir("my_directory/photos"))
        if vdo:
            files.extend(os.listdir("my_directory/videos"))

        selected_files = st.multiselect("Select files to delete:", options=files, key="delete_files_multiselect")
        if st.button("Delete Selected Files", key="delete_files_button"):
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
