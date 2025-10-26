import os
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # use 465 if you prefer SSL
SMTP_USER = "haitam.naji1994@gmail.com"
SMTP_PASS = "rrbugrioamvknwkf"

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
        print(f"✅ Email sent to {to_email}")

if __name__ == "__main__":
    send_email("zhoridlono@web.de", "Hello from GitHub", "This email was sent using Gmail SMTP + GitHub Actions!")
