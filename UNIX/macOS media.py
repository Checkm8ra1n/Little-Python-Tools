import subprocess
import os

installer  = input("Enter the path to the .app macos installer: ")
os.chdir(installer)
drive = input("Enter the path to the USB drive (e.g. MyUSB): ")
subprocess.run("sudo resources/createinstallmedia --volume /Volumes/" + drive, shell=True)