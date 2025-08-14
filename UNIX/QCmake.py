import subprocess
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists("CMakeLists.txt"):
    print("A CMakeLists.txt does not exist in the current directory.")
    exit(1)
if os.path.exists("build"):
    print("Build directory exists.")
    delete = input("Do you want to delete the build directory? (y/n): ")
    if delete.lower() == 'y':
        subprocess.run(["rm", "-rf", "build"])
        print("Build directory deleted.")
else:
    print("Build directory does not exist.")
    create = input("Do you want to create the build directory? (y/n): ")
    if create.lower() == 'y':
        subprocess.run(["mkdir", "build"])
        os.chdir("build")
        print("Build directory created.")

if os.path.exists("build"):
    os.chdir("build")
    print("Current directory:", os.getcwd())
    try:
        subprocess.run(["cmake", ".."], check=True)
    except subprocess.CalledProcessError:
        print("CMake configuration failed")
        exit(1)
    print("CMake configuration complete.")
    try:
        subprocess.run(["make"], check=True)
    except subprocess.CalledProcessError:
        print("Build process failed")
        exit(1)
    print("Build process complete.")
else:
    try:
        subprocess.run(["cmake", "."], check=True)
    except subprocess.CalledProcessError:
        print("CMake configuration failed")
        exit(1)

make = input("Do you want to run make or ninja? (m/n): ")
if make.lower() == 'm':
    try:
        subprocess.run(["make"], check=True)
    except subprocess.CalledProcessError:
        print("Make command failed")
        exit(1)
    print("Make command executed.")
elif make.lower() == 'n':
    try:
        subprocess.run(["ninja"], check=True)
    except subprocess.CalledProcessError:
        print("Ninja command failed")
        exit(1)
    print("Ninja command executed.")