import subprocess
import platform
import os

if platform.machine() == "AMD64":
    brew = "/usr/local/bin/brew"
else:
    brew = "/opt/homebrew/bin/brew"

macports = "/opt/local/bin/port"

def install_brew():
    print("Installing Homebrew...")
    subprocess.run(
        '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
        shell=True,
        check=True
    )
    print("Homebrew installation complete.")

macports_url = {
    26: "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-26-Tahoe.pkg",
    15: "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-15-Sequoia.pkg",
    14: "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-14-Sonoma.pkg",
    13: "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-13-Ventura.pkg",
    12: "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-12-Monterey.pkg",
    11 : "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-11-BigSur.pkg",
    10.15: "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-10.15-Catalina.pkg",
    10.14: "https://github.com/macports/macports-base/releases/download/v2.11.5/MacPorts-2.11.5-10.14-Mojave.pkg"

}

def install_macports():
    print("Installing MacPorts...")
    # Get macOS version
    mac_ver = platform.mac_ver()[0]
    major_ver = float(mac_ver.split('.')[0])
    minor_ver = float(mac_ver.split('.')[1]) if len(mac_ver.split('.')) > 1 else 0
    
    # Combine major and minor version if older than macOS 11
    version = major_ver if major_ver >= 11 else float(f"{major_ver}.{minor_ver}")
    
    # Get the correct URL from macports_url dictionary
    if version in macports_url:
        url = macports_url[version]
        print(f"Detected macOS version: {version}")
        print(f"Using MacPorts package for your system: {url}")
        
        # Download and install the package
        subprocess.run(
            f'curl -O "{url}" && sudo installer -pkg $(basename "{url}") -target /',
            shell=True,
            check=True
        )
        print("MacPorts installation complete.")
    else:
        print(f"No MacPorts package found for macOS version {version}")
        print("Please check https://www.macports.org/install.php for manual installation.")

def selector():
    print("Select a package manager:")
    print("1. Homebrew")
    print("2. MacPorts")
    pm = input("Enter your choice (1 or 2): ")
    pm = int(pm)
    if pm == 1:
        install_brew()
    elif pm == 2:
        install_macports()
    else:
        print("Invalid choice.")
        return

def checker():
    if os.path.exists(brew):
        print("Homebrew is installed.")
    elif os.path.exists(macports):
        print("MacPorts is installed.")
    else:
        print("No package manager found. Let's install one.")
        selector()



if  __name__ == "__main__":
    if platform.system() != "Darwin":
        print("This script is intended for macOS systems only.")
        exit(1)
    