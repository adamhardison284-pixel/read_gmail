import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from supabase import create_client, Client
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def send_email(subject, sender_email, password, receiver_email, text, html, offer_id, smtp_id, smtp_host):
	try:
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
			"""
			nb_send = nb_send + 1
			str_now = now.strftime("%Y-%m-%d %H:%M:%S")
			response_data_3 = supabase.table('gmail_smtps').update({"last_time": str_now, "nb_send": nb_send}).eq("id", smtp_id).execute()
			"""
			print('yes sent')
	except:
		offer_id = int(offer_id)
		"""
		response_ = supabase.table("drops").delete().eq("email", receiver_email).eq("offer_id", offer_id).execute()
		response_data_ = supabase.table('gmail_smtps').update({"ready": 0}).eq("id", smtp_id).execute()
		"""
		print('not sent')

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

url = "https://jdnmanfimzvbilacjgcj.supabase.co"
key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"
supabase: Client = create_client(url, key)	

resp = supabase.rpc(
            "get_smtp",
            {"new_name": "sprint_host_smtps"}
        ).execute()
smtp = response.data[0]

subject = "🎁 Gratis-Produkte sichern – Uhren, Deko, Schuhe & mehr!"
table_name = "web_de"
of_id = "6";
txt_msg = ""
msg = """
    <p>Hallo,</p>
	<p><span zeum4c2="PR_1_0" data-ddnwab="PR_1_0" aria-invalid="grammar" class="Lm ng">wir</span> haben etwas ganz Besonderes nur für dich! <img data-emoji="🎉" class="an1" alt="🎉" aria-label="🎉" draggable="false" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f389/32.png" loading="lazy"></p>
	<p>Für kurze Zeit verschenken wir <strong>exklusive Produkte</strong> – völlig kostenlos. Wähle einfach deine Favoriten aus und wir kümmern uns um den Rest. Egal ob <strong>stilvolle Uhren</strong>, <strong>moderne Wohn- &amp; Dekoartikel</strong>, <strong>praktische Küchenhelfer</strong>, <strong>trendige <span zeum4c2="PR_2_0" data-ddnwab="PR_2_0" aria-invalid="spelling" class="LI ng">Herrenaccessoires</span></strong> oder <strong>bequeme Schuhe</strong> – hier ist für jeden etwas dabei.</p>
	<p><img data-emoji="💥" class="an1" alt="💥" aria-label="💥" draggable="false" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f4a5/32.png" loading="lazy"> <strong>Warum wir das tun:</strong><br>
	Wir möchten unsere Community erweitern und suchen ehrliches Feedback von echten Testern. Du bekommst die Produkte gratis, probierst sie aus und teilst deine Meinung – ganz einfach!</p>
	<p><img data-emoji="👉" class="an1" alt="👉" aria-label="👉" draggable="false" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f449/32.png" loading="lazy"> <strong>So bekommst du deine Gratis-Produkte:</strong></p>
	<ol>
	<li>
	<p>Besuche unsere exklusive Angebotsseite.</p>
	</li>
	<li>
	<p>Wähle deine Lieblingsartikel aus.</p>
	</li>
	<li>
	<p>Gib deine Versanddaten ein – und schon ist dein Paket unterwegs!</p>
	</li>
	</ol>
	<p>Aber beeil dich – die Stückzahlen sind begrenzt und die Aktion läuft nur für kurze Zeit!</p>
	<p><img data-emoji="✨" class="an1" alt="✨" aria-label="✨" draggable="false" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/2728/32.png" loading="lazy"> <strong>Jetzt kostenlose Produkte sichern und Neues entdecken!</strong></p>
	<p><a style="text-decoration:none" href="https://www.watana-design.com/en/website-design/redirect.php?url=https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/trk1_clk?em_ofid=[em]|[of_id]"><b><font color="#0000ff">Jetzt gratis sichern</font></b></a>&nbsp;<img data-emoji="🔥" class="an1" alt="🔥" aria-label="🔥" draggable="false" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f525/32.png" loading="lazy"></p>
	<p>Liebe Grüße<br><img style="width:1px; height:1px;" src="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/img_op_gml?em_ofid=[em]|[of_id]"/>
	<strong>Dein Rewards-Team</strong></p>
"""
for x in range(1):
		#if smtp['ready'] == True:
		#receiver_email = "zhoridlono@web.de"
		sender_email = smtp['username']
		password = 'ArbiNaji1987$'
		"""
		# Parse the string into a datetime object (includes UTC offset)
		previous_str = smtp['last_time']
		last_time_send = datetime.fromisoformat(previous_str)
		# Current UTC time
		now = datetime.now(timezone.utc)
		# Difference in minutes
		diff_minutes = (now - last_time_send).total_seconds() / 60
		time_between_emails = 24*60 / smtp['max_send']
		if diff_minutes >= time_between_emails:
		"""
		if 1 == 1:
			"""
			response_1 = supabase.rpc(
				"get_one_email_and_insert",
				{"p_table": table_name, "p_offer_id": of_id}
			).execute()
			print('response_1.data: ', response_1.data[0]['email'])
			receiver_email = response_1.data[0]['email']
			"""
			receiver_email = 'kamlal.fahmi@yahoo.com'
			msg = msg.replace('[em]', receiver_email)
			msg = msg.replace('[of_id]', of_id)
			send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, smtp['id'], smtp['host'])
		"""
		if smtp['ready'] == False:
			sender_email = smtp['username']
			password = smtp['pass']
			# Parse the string into a datetime object (includes UTC offset)
			previous_str = smtp['last_time']
			last_time_send = datetime.fromisoformat(previous_str)
			# Current UTC time
			now = datetime.now(timezone.utc)
			# Difference in minutes
			diff_minutes = (now - last_time_send).total_seconds() / 60
			if diff_minutes >= 30:
				response_data_ = supabase.table('gmail_smtps').update({"ready": 1}).eq("id", smtp['id']).execute()
				response_1 = supabase.rpc(
					"get_one_email_and_insert",
					{"p_table": table_name, "p_offer_id": of_id}
				).execute()
				print('response_1.data: ', response_1.data[0]['email'])
				receiver_email = response_1.data[0]['email']
				msg = msg.replace('[em]', receiver_email)
				msg = msg.replace('[of_id]', of_id)
				send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, smtp['id'], smtp['host'], smtp['nb_send'])
		"""
		
		

