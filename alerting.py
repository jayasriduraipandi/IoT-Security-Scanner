import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_socketio import SocketIO

# For Flask-SocketIO alerting
socketio = None  # This will be set from app.py after import

def set_socketio(sio):
    global socketio
    socketio = sio


def send_email_alert(subject, message, to_email):
    from_email = "jayasrd22mss015@skasc.ac.in"
    password = "jayasri1234567890"  # Use Gmail App Password or SMTP password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        print("[Alert] Email sent successfully")
    except Exception as e:
        print(f"[Alert] Failed to send email: {e}")

def set_socketio(sio):
    global socketio
    socketio = sio

def send_dashboard_alert(message):
    if socketio:
        socketio.emit('new_alert', {'message': message}, broadcast=True)
        print("[Alert] Dashboard alert sent")
    else:
        print("[Alert] SocketIO not initialized, cannot send dashboard alert")
