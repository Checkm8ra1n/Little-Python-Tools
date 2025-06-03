import os
import subprocess
import platform

def efi_windows():
    input("Please ensure you are running this script as Administrator.")
    choice = input("Do you want to mount the EFI partition of your already installed Windows? (y/n): ")
    if choice == "yes" or "YES":
        drive = input("Enter the drive letter for the EFI partition (ex. Z:): ")
        print("Mounting the EFI partition...")
        subprocess.run("mountvol " + drive + " /s", shell=True)
        print("EFI partition mounted at " + drive)
    else:
        print("Follow the instructions to mount EFI partition of the drive you wish to install:")
        print("1. As you can see there's diskpart now, first type (list disk).")
        print("2. Find the disk you want to use and type (sel disk X) where X is the disk number.")
        print("3. Type (list par) to see the partition of the disk.")
        print("4. Find the EFI partition and type (sel par Y) where Y is the partition number; (usually is the first one).")
        print("5. Type (ass letter=Z (or whatever drive letter you want)) to assign a drive letter to the EFI partition.")
        print("Done! You can simply write (exit)")
        subprocess.run("diskpart", shell=True)

def efi_linux():
    print("Here you can mount the efi partition on your linux machine")
    disk = input("Type the disk letter of the partition you wish to mount (usually the main disk is the A): ")
    print("Mounting EFI partion, you will asked the sudo password")
    subprocess.run("sudo mount /dev/sd" + disk + "1 /mnt", shell=True)
    print("EFI partition mounted")

def efi_macos():
    print("Here you can mount the efi partition on your mac, useful for Hackintosh and OCLP")
    disk = input("Type the disk number of the partition you wish to mount (usually the main disk is the 0): ")
    print("Mounting EFI partion, you will asked the sudo password")
    subprocess.run("sudo diskutil mount /dev/disk" + disk + "s1", shell=True)
    print("EFI partition mounted")

if __name__ == "__main__":
    if platform.system() == "Darwin":
        efi_macos()
    elif platform.system() == "Linux":
        efi_linux()
    elif platform.system() == "Windows":
        efi_windows