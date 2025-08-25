from flask import Flask, render_template
from flask_socketio import SocketIO
import os, socket

from iot_port_scanner import scan_ports
from vuln_checker import check_vulnerabilities
from threat_analysis import analyze_threat
from report_generator import generate_report
from alerting import send_email_alert, send_dashboard_alert, set_socketio
from pymongo import MongoClient
from datetime import datetime


client = MongoClient('mongodb://localhost:27017/')  # for local MongoDB
db = client['iot_scanner']
collection = db['scan_results']

test_doc = {"message": "Hello MongoDB!", "time": datetime.now()}
result = collection.insert_one(test_doc)
print(f"Inserted document ID: {result.inserted_id}")

# Flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
set_socketio(socketio)

print("[*] Current Working Directory:", os.getcwd())

@app.route('/')
def index():
    return render_template('index.html')

# Fallback device discovery
def fallback_discovery():
    print("[*] Using fallback IP discovery (localhost only)")
    local_ip = socket.gethostbyname(socket.gethostname())
    return [{"ip": local_ip, "mac": "A8:3B:76:7C:E0:85"}]

def run_scan():
    print("\n[*] Starting IoT Security Scan...\n")
    devices = fallback_discovery()  # Replace with discover_devices() if available
    full_report = []

    for device in devices:
        ip = device['ip']
        mac = device.get('mac', 'N/A')
        print(f"\n[*] Scanning Device: {ip} ({mac})")

        try:
            ports = scan_ports(ip)
            print(f"Open Ports: {list(ports.keys())}")

            vulnerabilities = check_vulnerabilities(ports)
            print(f"Vulnerabilities: {vulnerabilities}")

            risk = analyze_threat(vulnerabilities)
            print(f"Risk Level: {risk}")

            alert_message = f"Device IP: {ip}\nMAC: {mac}\nRisk Level: {risk}\nVulnerabilities:\n"
            for vname, vdetail in vulnerabilities.items():
                alert_message += f"- {vname}: {vdetail}\n"

            # Terminal output
            print(alert_message)

            # Emit structured data to browser
            socketio.emit('scan_update', {
                'ip': ip,
                'mac': mac,
                'ports': list(ports.keys()),
                'vulnerabilities': vulnerabilities,
                'risk': risk
            })

            # Save to MongoDB
            collection.insert_one({
                "ip": ip,
                "mac": mac,
                "ports": list(ports.keys()),
                "vulnerabilities": vulnerabilities,
                "risk": risk,
                "scan_time": datetime.now()
            })

            # Send alerts
            if risk in ['High', 'Critical']:
                subject = f"Alert: {risk} Risk Detected on {ip}"
                send_email_alert(subject, alert_message, "jayasrid22mss015@skasc.ac.in")
                send_dashboard_alert(alert_message)

            # Prepare for PDF
            full_report.append({
                "IP Address": ip,
                "MAC Address": mac,
                "Open Ports": ', '.join(str(p) for p in ports),
                "Vulnerabilities": ', '.join(f"{k}: {v}" for k, v in vulnerabilities.items()),
                "Threat Level": risk  # ✅ Now included
            })
            if not full_report:  # fallback for testing
               full_report = [
        {
            "IP Address": "192.168.1.10",
            "MAC Address": "00:1A:2B:3C:4D:5E",
            "Open Ports": "22, 80",
            "Vulnerabilities": "Weak SSH password, HTTP not secure",
            "Threat Level": "High"
        }
    ]

        except Exception as e:
            print(f"[!] Error scanning {ip}: {e}")

    # Single PDF generation
    generate_report(full_report)
    print("[*] PDF Report generated successfully.")

@socketio.on('connect')
def handle_connect():
    print("[*] Dashboard connected.")
    run_scan()

if __name__ == '__main__':
    socketio.run(app, debug=True)
