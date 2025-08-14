import os
import subprocess

os.chdir(os.path.dirname(__file__))
if not os.path.exists('configure'):
    print("This is not a valid C/C++ project to build")
    exit(1)

try:
    subprocess.run(['./configure'], check=True, shell=True)
except subprocess.CalledProcessError:
    print("Configuration failed")
    exit(1)
try:
    subprocess.run(['make'], check=True, shell=True)
except subprocess.CalledProcessError:
    print("Build failed")
    exit(1)
install = input("Do you want to install the project? (y/n): ")
if install.lower() == 'y':
    try:
        subprocess.run(['make', 'install'], check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Installation failed")
        exit(1)