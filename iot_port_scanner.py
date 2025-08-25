import nmap

def scan_ports(ip):
    try:
        scanner = nmap.PortScanner()
        scanner.scan(ip, '1-1024')
        return scanner[ip]['tcp'] if 'tcp' in scanner[ip] else {}
    except Exception as e:
        print(f"[!] Port scanning failed for {ip}: {e}")
        return {}
