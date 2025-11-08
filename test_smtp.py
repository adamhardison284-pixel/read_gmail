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
	  print('sender_email: ', sender_email)
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
idss = [
	"a1189298",
	"a1189300",
	"a1189301",
	"a1189304",
	"a1189302",
	"a1189303",
	"a1189305",
	"a1189306",
	"a1189308",
	"a1189310",
	"a1189309",
	"a1189311",
	"a1189312",
	"a1189313",
	"a1189314",
	"a1189316",
	"a1189317",
	"a1189318",
	"a1189319",
	"a1189320"
]
for idq in idss:
	iddd = idq
	receiver_email = "bryan.pell@hotmail.com"
	receiver_email = "adamhardison284@gmail.com"
	receiver_email = "kamlal.fahmi@yahoo.com"
	receiver_email = "donaskarine13@gmx.fr"
	receiver_email = "nancycronin387cc@web.de"
	sender_email = 'helena-jahn@'+iddd+'.xsph.ru'
	password = 'Arbinaji1987$'
	msg = msg.replace('[em]', receiver_email)
	msg = msg.replace('[of_id]', of_id)
	hhost = "smtp."+iddd+".xsph.ru"
	send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, hhost)
		
