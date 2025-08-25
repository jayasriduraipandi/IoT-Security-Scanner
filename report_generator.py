# report_generator.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_report(data):
    filename = f"IoT_Scan_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y = height - 50

    # Report Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "IoT Security Scanner Report")
    y -= 40

    c.setFont("Helvetica", 12)

    if not data:
        c.drawString(50, y, "No devices found or no scan data available.")
    else:
        for device in data:
            c.drawString(50, y, f"IP Address: {device.get('IP Address', 'N/A')}")
            y -= 20
            c.drawString(50, y, f"MAC Address: {device.get('MAC Address', 'N/A')}")
            y -= 20
            c.drawString(50, y, f"Open Ports: {device.get('Open Ports', 'None')}")
            y -= 20
            c.drawString(50, y, f"Vulnerabilities: {device.get('Vulnerabilities', 'None')}")
            y -= 20
            c.drawString(50, y, f"Threat Level: {device.get('Threat Level', 'Unknown')}")
            y -= 40

            # If page is full, create new page
            if y < 100:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 50

    c.save()
    return filename
