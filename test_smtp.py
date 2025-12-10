import imaplib
import email
import re
import csv
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from supabase import create_client, Client
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def insert_email_to_supabase(p_email):
    result = supabase.rpc(
        "insert_bounced_email",
        {"p_email": p_email}
    ).execute()
	
def has_special_char(username):
    return bool(re.search(r"[^A-Za-z0-9]", username))
	
def check_imap(smtp_id, imap_, username_, pass_):
	smtp_id = imap_
	IMAP_SERVER = imap_
	EMAIL_ACCOUNT = username_
	EMAIL_PASSWORD = pass_
	
	try:
		# === CONNECT ===
		imap = imaplib.IMAP4_SSL(IMAP_SERVER)
		imap.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
		
		# Search both inbox and spam if needed
		imap.select("INBOX")
		
		# Search common bounce indicators
		# mailer-daemon, postmaster, or common bounce subjects
		search_criterias = '(FROM "Mail Delivery System")'
		if '@gmail' in username_:
			search_criterias = '(FROM "Mail Delivery Subsystem")'
		elif '@yandex.com' in username_:
			search_criterias = '(FROM "mailer-daemon@yandex.ru")'
		
		result, data = imap.search(None, search_criterias)
		if result != "OK":
			print("No messages found.")
			imap.logout()
			exit()
		
		msg_ids = data[0].split()
		print(f"Found {len(msg_ids)} possible bounces to {EMAIL_ACCOUNT}.")
		
		rows = []
		for msg_id in msg_ids:
			result, msg_data = imap.fetch(msg_id, "(RFC822)")
			raw_email = msg_data[0][1]
			msg = email.message_from_bytes(raw_email)
			mm = re.search(r"Final-Recipient:\s*[^;]+;\s*([^\s]+)", str(msg), re.I)
			To = str(mm.group()).replace("Final-Recipient: rfc822;", "")
			To = To.replace(" ", "")
			reason_code_1 = "action not taken: mailbox unavailable"
			reason_code_4 = "mailbox not found"
			reason_code_2 = "554-IP address is block listed"
			reason_code_3 = "all hosts for 'web.de' have been failing for a long time (and retry time not reached)"
			rc_1 = re.search(reason_code_1, str(msg), re.I)
			rc_4 = re.search(reason_code_4, str(msg), re.I)
			rc_2 = re.search(reason_code_2, str(msg), re.I)
			rc_3 = re.search(reason_code_3, str(msg), re.I)
			print("rc_1: ", rc_1)
			print("rc_4: ", rc_4)
			if rc_1 is not None or rc_4 is not None:
				insert_email_to_supabase(To)
				print("bounced To: ", To)
			elif rc_2 is not None or rc_3 is not None:
				"""
				result_1 = supabase.rpc(
					"update_reason",
					{"uid": smtp['id']}
				).execute()
				"""
				print("blacklisted To: ", To)
				response_data_ = supabase.table('sprint_host_smtps').update({"ready": 0, "reason": "blacklisted"}).eq("id", smtp_id).execute()
			imap.store(msg_id, '+FLAGS', '\\Deleted')
		imap.expunge()
		imap.logout()
	except:
		pass

bcl = True
nb_send = 0
def send_email(subject, sender_email, password, receiver_email, text, html, offer_id, smtp_id, smtp_host):
	try:
		msg = MIMEMultipart("alternative")
		msg["Subject"] = subject
		"""
		msg["From"] = 'amazon giveaways<deals@amazon.com>'
		msg["From"] = 'Das Überraschungsteam<deals@amazon.com>'
		msg["From"] = 'Uberraschungsteam <surprise@amazon.com>'
		"""
		msg["From"] = 'Das Uberraschungsteam <' + sender_email + '>'
		msg["To"] = receiver_email
		
		# Attach both versions
		msg.attach(MIMEText(text, "plain"))
		msg.attach(MIMEText(html, "html"))
		
		# --- Send the email ---
		with smtplib.SMTP(smtp_host, 587) as server:
			server.starttls()
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, msg.as_string())
			global nb_send
			nb_send = nb_send + 1
			response_data_3 = supabase.table('sprint_host_smtps').update({"nb_send": nb_send}).eq("id", smtp_id).execute()
			"""
			str_now = now.strftime("%Y-%m-%d %H:%M:%S")
			"""
			print('yes sent')
			print('sender: ', sender_email)
			
	except:
		offer_id = int(offer_id)
		global bcl
		bcl = False
		response_ = supabase.table("drops").delete().eq("email", receiver_email).eq("offer_id", offer_id).execute()
		response_data_ = supabase.table('sprint_host_smtps').update({"ready": 0}).eq("id", smtp_id).execute()
		print('not sent')

url = "https://jdnmanfimzvbilacjgcj.supabase.co"
key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"
supabase: Client = create_client(url, key)

#response = supabase.table("sprint_host_smtps").select("*").eq("ready", 1).execute()
response = (
    supabase
        .table("sprint_host_smtps")
        .select("*")
		.eq("ready", 1)
        .order("id", desc=False)  # ASC
        .execute()
)
smtps = response.data

of_id = "7";
response_offer = supabase.table("offers").select("*").eq("id", int(of_id)).execute()
subject = response_offer.data[0]['subject']
#subject = "Deine Chance, etwas wirklich Großes zu gewinnen!"
table_name = "yahoo_de_duplicate"
txt_msg = ""

msg = response_offer.data[0]['letter']
for x in range(1):
	#for smtp in smtps:
	bcl = True
	nb_send = 0
	smtp = smtps[x]
	if smtp['ready'] == True:
		receiver_email = "adamoyler2705cc@web.de"
		receiver_email = "kamlal.fahmi@yahoo.com"
		receiver_email = "sophie.blarbi44@hotmail.com"
		receiver_email = "adamhardison284@gmail.com"
		
		sender_email = smtp['username']
		password = smtp['pass']
		for y in range(1):
			#while bcl == True:
			user_bool = True
			"""
			while user_bool == True:
				response_1 = supabase.rpc(
					"get_one_email_and_insert",
					{"p_table": table_name, "p_offer_id": of_id}
				).execute()
				if response_1.data[0]['email'].count("@") == 1:
					emqq = response_1.data[0]['email'].split('@')[0]
					if not has_special_char(emqq):
						print('response_1.data: ', response_1.data[0]['email'])
						receiver_email = response_1.data[0]['email']
						user_bool = False
					else:
						#response_ = supabase.table("drops").delete().eq("email", response_1.data[0]['email']).eq("offer_id", of_id).execute()
						pass
				else:
					#response_ = supabase.table("drops").delete().eq("email", response_1.data[0]['email']).eq("offer_id", of_id).execute()
					pass
			"""
			print('receiver_email: ', receiver_email)
			msg = msg.replace('[em]', receiver_email)
			msg = msg.replace('[of_id]', of_id)
			send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, smtp['id'], smtp['host'])
		time.sleep(60)
		check_imap(smtp['id'], smtp['imap'], smtp['username'], smtp['pass'])






