import psutil
import socket

def get_network_info():
    interfaces = psutil.net_if_addrs()
    result = {}

    for name, addrs in interfaces.items():
        iface_info = {"ipv4": None, "ipv6": None, "mac": None}

        for addr in addrs:
            if addr.family == socket.AF_INET:
                iface_info["ipv4"] = addr.address
            elif addr.family == socket.AF_INET6:
                iface_info["ipv6"] = addr.address
            elif addr.family == psutil.AF_LINK:
                iface_info["mac"] = addr.address

        result[name] = iface_info

    return result