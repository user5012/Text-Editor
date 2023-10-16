import os
def Installer():
    # GitHub repository information
    owner = 'user5012'
    repo = 'Text-Editor'

    # GitHub API URL to get the latest release
    api_url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'

    # Send a GET request to the GitHub API
    response = requests.get(api_url)

    if response.status_code == 200:
        release_data = response.json()
        latest_version = release_data['tag_name']

        # Check if the latest release version is different from the currently stored version

        if latest_version != "v1.3":
            print(RED,"Update available! ", RESET,"You can download it from here https://github.com/user5012/Text-Editor/releases")
            """
            print(RED, "UPDATE AVAILABLE", RESET)
            # Download the release assets here
            assets = release_data['assets']

            for asset in assets:
                asset_url = asset['browser_download_url']  # Get the download URL
                asset_name = asset['name']  # Get the asset name

                # Download the asset
                response = requests.get(asset_url)
                if response.status_code == 200:
                    with open(asset_name, 'wb') as f:
                        f.write(response.content)

            # Save the latest release version to the stored_version.txt file
            with open(stored_version_file, 'w') as f:
                f.write(latest_version)

            print(YELLOW,"Downloaded the latest release.",RESET)
            
        else:
            print("Already up to date.")
            os.system("exit")
    else:
        print("Failed to fetch release information from GitHub API.")
        os.system("pause")

search_for_req()