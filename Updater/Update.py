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
        stored_version_file = 'stored_version.txt'

        if os.path.exists(stored_version_file):
            with open(stored_version_file, 'r') as f:
                stored_version = f.read().strip()
        else:
            stored_version = ''

        if latest_version != stored_version:
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
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(RED,"IF THERE IS ANY PROBLEM WITH UPDATE. RUN Text-Editor.exe AS ADMINISTRATOR",RESET)
try:
    import requests
    import tkinter as tk
    from tkinter import filedialog
    import re
    from tkinter import messagebox
    import os
    import sys
    import subprocess

except ModuleNotFoundError as e:
    print(e)
    choice = ""
    print("You don't have requirements install. Do you want to install them? (Y/N)")
    input(choice)
    while choice != 'Y' or choice != 'y' or choice != 'N' or choice != 'n':
        print("answer only with Y/y or N/n")
        choice = ""
        input(choice)
    if choice == 'Y' or choice == 'y':
        os.system("pip install -r requirements.txt")
        Installer()
    else:
        print("Okay but you cant run the app")
        os.system("pause")
        sys.exit()

Installer()