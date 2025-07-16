import requests
from bs4 import BeautifulSoup
import os
import platform

base_url = "https://mcversions.net/download"
version = input("Enter Minecraft version (e.g., 1.21.7): ").strip()
client = input("Type client or server (c/s): ").strip().lower()

# Set download directory based on OS
system = platform.system()
if system == "Windows":
    download_dir = os.path.join(os.environ["USERPROFILE"], "Downloads")
else:
    download_dir = os.path.expanduser("~/Downloads")

if not os.path.isdir(download_dir):
    os.makedirs(download_dir, exist_ok=True)
os.chdir(download_dir)

url = f"{base_url}/{version}"

try:
    resp = requests.get(url)
    resp.raise_for_status()
except Exception as e:
    print(f"Error fetching the page: {e}")
    exit(1)

soup = BeautifulSoup(resp.text, "html.parser")

if client == "s":
    btn = soup.find("a", string="Download Server Jar")
    filename = f"minecraft_server_{version}.jar"
elif client == "c":
    btn = soup.find("a", string="Download Client Jar")
    filename = f"minecraft_client_{version}.jar"
else:
    print("Invalid choice (use 'c' for client or 's' for server).")
    exit(1)

if not btn or not btn.get("href"):
    print("Download link not found for this version.")
    exit(1)

download_url = btn["href"]

print(f"Downloading from: {download_url}")
print(f"Saving to: {os.path.join(download_dir, filename)}")

try:
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"Download completed: {filename}")
except Exception as e:
    print(f"Error during download: {e}")