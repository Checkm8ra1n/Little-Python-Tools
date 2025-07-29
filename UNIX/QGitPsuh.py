import subprocess
import sys
import os

if not os.path.exists(".git"):
    print("You haven't initialized a git repository in this directory, so I will do it for you.")
    input("Press enter to continue...")
    subprocess.run("git init", shell=True)
    print("Initialized a new git repository.")

print("Adding your files")
subprocess.run("git add .", shell=True)
print("Files added to the staging area.")
commit = input("Enter a commit message: ")
subprocess.run(f"git commit -m \"{commit}\"", shell=True)
print("Message committed.")
print("Pushing to the remote repository")
repository = input("Enter the remote repository URL (leave blank if you already set it up): ")
if repository:
    subprocess.run(f"git remote add origin {repository}", shell=True)
    print("Remote repository added.")
branch = input("Enter the branch name (default is 'master'): ") or "master"
subprocess.run(f"git branch -M {branch}", shell=True)
subprocess.run(f"git push -u origin {branch}", shell=True)