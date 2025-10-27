#!/usr/bin/env python3

import socket
import subprocess
import argparse
import sys

def run_cmd(cmd):
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
        return out.strip()
    except Exception:
        return None

def device_for_hardware_port(port_name):
    # usa networksetup per mappare "Wi-Fi" / "Ethernet" a device (en0, en1, ...)
    out = run_cmd(["networksetup", "-listallhardwareports"])
    if not out:
        return None
    lines = out.splitlines()
    dev = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("Hardware Port:"):
            hw = line.split("Hardware Port:")[1].strip()
            # next lines may contain Device:
            j = i + 1
            device = None
            while j < len(lines) and lines[j].strip() != "":
                if lines[j].strip().startswith("Device:"):
                    device = lines[j].split("Device:")[1].strip()
                j += 1
            if hw.lower() == port_name.lower():
                return device
            # also allow some common synonyms
            if port_name.lower() == "wifi" and hw.lower() in ("wi-fi", "wifi", "airport"):
                return device
        i += 1
    return None

def ip_for_device(device):
    if not device:
        return None
    ip = run_cmd(["ipconfig", "getifaddr", device])
    return ip

def get_wifi_ip():
    # prova a trovare il device per Wi‑Fi e prendere l'IP
    dev = device_for_hardware_port("Wi-Fi")
    if not dev:
        dev = device_for_hardware_port("WiFi")
    if not dev:
        dev = device_for_hardware_port("AirPort")
    return ip_for_device(dev)

def get_ethernet_ip():
    dev = device_for_hardware_port("Ethernet")
    return ip_for_device(dev)

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-e", action="store_true", dest="ethernet")
    parser.add_argument("-w", action="store_true", dest="wifi")
    parser.add_argument("-h", action="store_true", dest="hostname_only")
    args, extra = parser.parse_known_args()
    if extra:
        print("Usage: python3 myip.py [-e] [-w] [-h]")
        sys.exit(1)

    hostname = socket.gethostname()

    wifi_ip = get_wifi_ip()
    eth_ip = get_ethernet_ip()

    # comportamenti delle opzioni
    if args.hostname_only:
        print("Host name: " + hostname)
        return

    if args.wifi and not args.ethernet:
        print("Wi-Fi IP Address: " + (wifi_ip if wifi_ip else "Not Connected"))
        return

    if args.ethernet and not args.wifi:
        print("Ethernet IP Address: " + (eth_ip if eth_ip else "Not Connected"))
        return

    # nessuna opzione o entrambe: stampa tutto
    print("Host name: " + hostname)
    print("Wi-Fi IP Address: " + (wifi_ip if wifi_ip else "Not Connected"))
    print("Ethernet IP Address: " + (eth_ip if eth_ip else "Not Connected"))

if __name__ == "__main__":
    main()
# ...existing code...