import winreg
import os

def disable_smartscreen():
    # Define the registry key path and value name for SmartScreen
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer"
    value_name = "SmartScreenEnabled"

    try:
        # Open the registry key with write access
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, "Off", winreg.KEY_SET_VALUE) as reg_key:
            # Set the value to disable SmartScreen (1 = disable, 0 = enable)
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_DWORD, 1)
        print("SmartScreen has been disabled.")
    except Exception as e:
        print(f"Failed to disable SmartScreen: {e}")