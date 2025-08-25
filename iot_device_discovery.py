from scapy.all import ARP, Ether, srp

def discover_devices(ip_range="192.168.1.1/24"):
    devices = []
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    result = srp(pkt, timeout=3, verbose=0)[0]
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices
