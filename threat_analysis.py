def analyze_threat(vulnerabilities):
    high_risk_ports = [21, 23, 80]
    risk_score = 0

    for port in vulnerabilities:
        if port in high_risk_ports:
            risk_score += 2
        else:
            risk_score += 1

    if risk_score >= 5:
        return "High"
    elif risk_score >= 3:
        return "Medium"
    else:
        return "Low"
