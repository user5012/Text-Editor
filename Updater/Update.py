import os


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def search_for_req():
    requirements = 'req.txt'
    if os.path.exists(requirements):
        with open(requirements, 'r') as f:
            output = f.read()

    else:
        output = ''

    if output == '':
        os.system("pip install requests")
        with open(requirements, 'w') as f:
            print("Requirements Installed!")
            f.write("Installed requirements")
        Installer()

    else:
        Installer()

    
def Installer():
    import requests
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
        stored_version_file = 'stored_version.txt'

        if os.path.exists(stored_version_file):
            with open(stored_version_file, 'r') as f:
                stored_version = f.read().strip()
        else:
            stored_version = ''

        if latest_version != stored_version:
            print(RED, "UPDATE AVAILABLE", RESET)
            print("You will need to run Text-Editor.exe as administrator for update to be installed.")
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
            os.system("msiexec /f TextEditor.msi")
            os.system("exit")
        else:
            print("Already up to date.")
            os.system("exit")
    else:
        print("Failed to fetch release information from GitHub API.")
        os.system("pause")

search_for_req()