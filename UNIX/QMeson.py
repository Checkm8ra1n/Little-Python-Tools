import os
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists("meson.build"):
    print("This is not a valid Meson project.")
    exit(1)
try:
    subprocess.run(["meson", "setup", "build"], check=True, shell=True)
except subprocess.CalledProcessError:
    print("Meson configuration failed")
    exit(1)
try:
    subprocess.run(["meson", "compile", "-C", "build"], check=True, shell=True)
except subprocess.CalledProcessError:
    print("Meson build failed")
    exit(1)
try:
    subprocess.run("ninja")
except subprocess.CalledProcessError:
    print("Ninja command failed")
    exit(1)