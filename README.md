<h1>IOT SECURITY SCANNER🔒</h1> 

The IoT Security Scanner is a Python-based tool to discover IoT devices, scan for vulnerabilities, and assess network security. Designed for administrators, researchers, and security enthusiasts, it provides real-time alerts, detailed reports, and automated monitoring of IoT networks.

<h2>📌 Project Focus</h2>
This project automates IoT security scanning to help administrators identify risks quickly. Manual scans are time-consuming; this tool is modular, extensible, and stores results for future analysis.

<h2>🛠 Technologies Used</h2>
> - Python 3 – Core language
>	- Flask & Flask-SocketIO – Web dashboard and real-time alerts
>	- MongoDB – Stores scan results
>	- ReportLab – Generates PDF reports
>	- SMTP/Email – Email notifications for high-risk vulnerabilities
>	- Socket Programming – Device discovery & port scanning

<h2>⚡ Key Features</h2>
•	Device Discovery: Detects connected devices automatically
•	Port Scanning: Identifies open & vulnerable ports
•	Vulnerability Analysis: Checks for insecure services & weak configs
•	Threat Assessment: Classifies risk as Low / Medium / High / Critical
•	Real-Time Alerts: Email & dashboard notifications
•	PDF Reporting: Professional scan reports for compliance
•	Database Storage: MongoDB storage for trend analysis
•	Modular & Extensible: Easy integration of new modules
Suitable for enterprises, home networks, and academic research.

</h2>🚀 Quick Start<h2>
<details> <summary>Click to expand</summary> 
**1️) Clone Repository**
git clone https://github.com/<your-username>/iot-security-scanner.git
cd iot-security-scanner
**2️) Install Dependencies**
pip install -r requirements.txt
**3️) Start MongoDB**
Ensure MongoDB is running locally:
mongodb://localhost:27017/
**4️) Run Application**
python main.py
**5️) Access Dashboard**
Open in browser:
http://127.0.0.1:5000
**6️) Reports**
•	PDF reports saved in project folder
•	Scan results stored in MongoDB
</details> 

<h2>📊 Example Output</h2>
•	Dashboard: Shows devices, open ports, and vulnerabilities
•	PDF Report: Summarizes IP, MAC, ports, vulnerabilities, and threat levels
•	Alerts: Critical issues trigger email & dashboard notifications

<h2>🔮 Future Improvements</h2>
<details> <summary>Click to expand</summary> 
•	Integrate with CVE/NVD database for live vulnerability mapping
•	Improved UI with charts, graphs, and filtering
•	Docker support for easier deployment
•	Support for additional protocols: UPnP, mDNS, SNMP
•	Multi-user authentication for secure dashboard access
</details> 

<h2>👨‍💻 Author</h2>
Jayasri Duraipandi
📧 Contact: jayasriduraipandi1415@gmail.com

<h2>📄 License</h2>
This project is licensed under the MIT License. See the LICENSE file for details.
