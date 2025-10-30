import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def send_email(subject, sender_email, password, receiver_email, text, html, offer_id, smtp_host):
  msg = MIMEMultipart("alternative")
  msg["Subject"] = subject
  msg["From"] = sender_email
  msg["To"] = receiver_email
  
  # Attach both versions
  msg.attach(MIMEText(text, "plain"))
  msg.attach(MIMEText(html, "html"))
  
  # --- Send the email ---
  with smtplib.SMTP(smtp_host, 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

subject = "🎁 Gratis-Produkte sichern – Uhren, Deko, Schuhe & mehr!"
table_name = "web_de"
of_id = "6";
txt_msg = ""
msg = """
    <p>Hallo,</p>
"""
"""
receiver_email = "nancycronhykiin387cc@web.de"
sender_email = 'let@a1185346.xsph.ru'
password = 'Arbinaji1987$'
smtp.a1185346.xsph.ru
"""
receiver_email = "nancycronin387cc@web.de"
sender_email = 'patriziapauli@yandex.com'
password = 'okydmgbhqoyavnkk'
msg = msg.replace('[em]', receiver_email)
msg = msg.replace('[of_id]', of_id)
send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, "smtp.yandex.com")
		
