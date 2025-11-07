import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def send_email(subject, sender_email, password, receiver_email, text, html, offer_id, smtp_host):
  msg = MIMEMultipart("alternative")
  msg["Subject"] = subject
  msg["From"] = "newsletter@finya.de"
  msg["To"] = receiver_email
  
  # Attach both versions
  msg.attach(MIMEText(text, "plain"))
  msg.attach(MIMEText(html, "html"))
  
  # --- Send the email ---
  with smtplib.SMTP(smtp_host, 587) as server:
	  server.starttls()
	  server.login(sender_email, password)
	  server.sendmail(sender_email, receiver_email, msg.as_string())
	  print('sent')

subject = "🎁 Gratis-Produkte sichern – Uhren, Deko, Schuhe & mehr!"
table_name = "web_de"
of_id = "6";
txt_msg = ""
msg = """
    <p>Hallo,</p>
"""
"""
receiver_email = "bryan.pell@hotmail.com"
sender_email = 'let@a1186466.xsph.ru'
password = 'Arbinaji1987$'
smtp.a1185346.xsph.ru
"""
iddd = "a1189320"
receiver_email = "bryan.pell@hotmail.com"
receiver_email = "donaskarine13@gmx.fr"
#receiver_email = "arbi.naji@gmail.com"
sender_email = 'helena-jahn@'+iddd+'.xsph.ru'
password = 'Arbinaji1987$'
msg = msg.replace('[em]', receiver_email)
msg = msg.replace('[of_id]', of_id)
hhost = "smtp."+iddd+".xsph.ru"
send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, hhost)
		
