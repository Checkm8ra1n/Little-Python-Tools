import socket
import psutil

def get_interface_ip(interface_names):
    for iface in interface_names:
        addrs = psutil.net_if_addrs().get(iface)
        if addrs:
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    return addr.address
    return None

def get_ips():
    # Possibili nomi delle interfacce su macOS/Linux/Windows
    wifi_names = ["en0", "wlan0", "Wi-Fi", "wl0", "wlp2s0"]
    eth_names = ["en1", "eth0", "Ethernet", "enp3s0"]

    wifi_ip = get_interface_ip(wifi_names)
    eth_ip = get_interface_ip(eth_names)

    print(f"Wifi IP: {wifi_ip if wifi_ip else 'not connected'}")
    print(f"Ethernet IP: {eth_ip if eth_ip else 'not connected'}")

if __name__ == "__main__":
    get_ips()