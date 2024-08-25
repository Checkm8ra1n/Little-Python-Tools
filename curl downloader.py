import os
import subprocess

def download():
    url = input("Type here URL: ").strip()
    try:
        subprocess.run(["curl", "-O", "-#", url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def yes():
    directory = input("Type here directory: ").strip()
    try:
        os.chdir(directory)
        download()
    except FileNotFoundError:
        print("Directory not found. Please provide a valid directory.")
    except PermissionError:
        print("Permission denied, try run as root.")

print("Curl downloader")
position = input("Do you want to set another download directory? (yes/no) ").strip().lower()

if position == "yes":
    yes()
else:
    download()
