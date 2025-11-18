import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from supabase import create_client, Client
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

bcl = True
def send_email(subject, sender_email, password, receiver_email, text, html, offer_id, smtp_id, smtp_host):
	try:
		msg = MIMEMultipart("alternative")
		msg["Subject"] = subject
		"""
		msg["From"] = 'amazon giveaways<deals@amazon.com>'
		msg["From"] = 'Das Überraschungsteam<deals@amazon.com>'
		msg["From"] = 'Das Uberraschungsteam <' + sender_email + '>'
		"""
		msg["From"] = 'Das Uberraschungsteam<surprise@amazon.com>'
		msg["To"] = receiver_email
		
		# Attach both versions
		msg.attach(MIMEText(text, "plain"))
		msg.attach(MIMEText(html, "html"))
		
		# --- Send the email ---
		with smtplib.SMTP(smtp_host, 587) as server:
			server.starttls()
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, msg.as_string())
			"""
			nb_send = nb_send + 1
			str_now = now.strftime("%Y-%m-%d %H:%M:%S")
			response_data_3 = supabase.table('sprint_host_smtps').update({"last_time": str_now, "nb_send": nb_send}).eq("id", smtp_id).execute()
			"""
			print('yes sent')
			print('sender: ', sender_email)
			
	except:
		offer_id = int(offer_id)
		bcl = False
		response_ = supabase.table("drops").delete().eq("email", receiver_email).eq("offer_id", offer_id).execute()
		response_data_ = supabase.table('sprint_host_smtps').update({"ready": 0}).eq("id", smtp_id).execute()
		print('not sent')
