
def check_vulnerabilities(open_ports):
    # Example logic
    vulnerabilities = {}
    for port, info in open_ports.items():
        if port in [21, 23, 80]:  # Insecure common ports
            vulnerabilities[port] = "Potential vulnerability detected"
        else:
            vulnerabilities[port] = "No known vulnerability"
    return vulnerabilities
