#!/usr/bin/env python3
import os
import platform
import psutil
import subprocess
import sys

def get_os_info():
    if platform.system() == "Darwin":
        mac_ver = platform.mac_ver()[0]
        return f"macOS {mac_ver}"
    elif platform.system() == "Windows":
        return f"Windows {platform.release()}"
    else:
        return platform.system()

def get_cpu_info():
    if platform.system() == "Darwin":
        cmd = "sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(cmd, shell=True).strip().decode()
    elif platform.system() == "Windows":
        return platform.processor()
    return "CPU information not available"

def get_gpu_info():
    if platform.system() == "Darwin":
        cmd = "system_profiler SPDisplaysDataType | grep Chip"
        try:
            return subprocess.check_output(cmd, shell=True).strip().decode().split(": ")[1]
        except:
            return "GPU information not available"
    elif platform.system() == "Windows":
        try:
            cmd = "wmic path win32_VideoController get name"
            return subprocess.check_output(cmd, shell=True).strip().decode().split("\n")[1]
        except:
            return "GPU information not available"
    return "GPU information not available"

def get_ram_info():
    ram = psutil.virtual_memory()
    return f"{round(ram.total / (1024**3))} GB"

def get_disk_info():
    disk = psutil.disk_usage('/')
    total_gb = round(disk.total / (1024**3))
    free_gb = round(disk.free / (1024**3))
    return f"{total_gb} GB (Free: {free_gb} GB)"

def get_kernel_version():
    if platform.system() == "Darwin":
        return platform.release()
    elif platform.system() == "Windows":
        return platform.version()
    return platform.release()

def main():
    print(f"Operating System: {get_os_info()}")
    print(f"Kernel Version: {get_kernel_version()}")
    print(f"CPU Model: {get_cpu_info()}")
    print(f"GPU Model: {get_gpu_info()}")
    print(f"RAM: {get_ram_info()}")
    print(f"Disk Space: {get_disk_info()}")

if __name__ == "__main__":
    main()