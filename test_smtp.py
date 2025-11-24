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
		msg["From"] = 'Das Uberraschungsteam <' + sender_email + '>'
		"""
		msg["From"] = 'Uberraschungsteam <surprise@amazon.com>'
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

#response = supabase.table("sprint_host_smtps").select("*").execute()
response = (
    supabase
        .table("sprint_host_smtps")
        .select("*")
        .order("id", desc=False)  # ASC
        .execute()
)
smtps = response.data

subject = "Deine Chance, etwas wirklich Großes zu gewinnen!"
table_name = "yahoo_de_duplicate"
of_id = "8";
txt_msg = ""
msg = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
			<html xmlns="http://www.w3.org/1999/xhtml">
			
			<head>
			  <title></title>
			
			  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
			  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
			  <meta name="format-detection" content="telephone=no"/>
			  <meta name="format-detection" content="date=no"/>
			  <meta name="format-detection" content="address=no"/>
			  <meta name="format-detection" content="email=no"/>
			  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
			
			  <style type="text/css">
				body	{Margin:0 auto; padding:0;}
				img		{max-width:100%;}
				table	{border-spacing:0!important; border:none; cellpadding:0px; }
				td		{cellpadding:0px; border-spacing:0px;}
				tr		{cellpadding:0px; border-spacing:0px;}
			/* GK: Client-specific Styles */
				#outlook a{padding:0;} /* GK: Force Outlook to provide a "view in browser" message */
				.ReadMsgBody{width:100%;} .ExternalClass{width:100%;} /* GK: Force Hotmail to display emails at full width */
				.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {line-height: 100%;} /* GK: Force Hotmail to display normal line spacing */
				body, table, td, a{-webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;} /* GK: Prevent WebKit and Windows mobile changing default text sizes */
				table, td{mso-table-lspace:0pt; mso-table-rspace:0pt;} /* GK: Remove spacing between tables in Outlook 2007 and up */
				img{-ms-interpolation-mode:bicubic;} /* GK: Allow smoother rendering of resized image in Internet Explorer */			
			  </style>
			</head>
			
			
			<body bgcolor="#f2f2f2">
			
			<!-- GK: container  -->
			  <table width="100%" border="0" cellpadding="0" cellspacing="0" id="wrappertable" style="table-layout: fixed;">
				<tr>
				  <td align="center" valign="top" >
					<table cellpadding="0" cellspacing="0" border="0">
					  <tr>
						<td width="600" align="center" valign="top" style="background-color: #ffffff; box-shadow: 1px 1px 10px 0px rgba(25, 25, 25, 0.15);">
							<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #151515;">
									  <tr>
										<td align="center" valign="middle" style="font-family:Arial, Helvetica, sans-serif; font-size:16px; font-weight:normal; line-height:22px; letter-spacing:0px; color:#ffffff;  min-height:20px; mso-line-height-rule: exactly; padding: 20px 25px;"><strong>Wir gratulieren Ihnen recht herzlich!</strong>
			
										</td>
									  </tr>
									</table>
			<!-- GK: image-->
						  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; padding:0px 0px 10px 0px;">
							<tr>
							  <td valign="middle" style=" line-height:1px;">
							  </td>
							</tr>
							<tr>
							  <td align="center" valign="top" style="padding: 0 0px;">
								<table cellpadding="0" cellspacing="0" border="0">
								  <tr>
									<td width="600" align="center" valign="middle" >
									  <a href="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/trk1_clk?em_ofid=[em]|[of_id]" style="outline:0;" target="_blank">
										<img src="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/img_op_gml?em_ofid=[em]|[of_id]" style="width: 100%; max-width: 100%; margin: 0px 0;" border="0" alt=""/>
									  </a>
							
									</td>
								  </tr>
								</table>
							  </td>
							</tr>
						  </table>
			<!-- GK: end image -->
					 <!-- GK: CTA (Button) -->
								  <table width="60%" cellpadding="0" cellspacing="0" border="0">
									<tr>
									  <td align="center" valign="top" style="padding: 0 20px;">
										<table cellpadding="0" cellspacing="0" border="0">
												 <tr>
											<td width="350" align="center" valign="top">
											  <table width="100%" cellpadding="0" cellspacing="0" border="0">
												<tr>
												  <td width="350" height="40" align="center" valign="middle" style="background-color:#ff9900; padding: 6px 12px; ">
													<a style="display: block; text-decoration: none; font-family: 'Arial', verdana, sans-serif; font-size: 18px; mso-line-height-rule: exactly; line-height: 32px;font-weight: bold; color: #ffffff;" href="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/trk1_clk?em_ofid=[em]|[of_id]" target="_blank"> 
														 Jetzt gewinnen!
													</a>
												  </td>
												</tr>
											  </table>
											</td>
										  </tr>
										</table>
									  </td>
									</tr>
								  </table>
			<!-- GK: end CTA (Button) -->
			<!-- GK: spacer -->
						  <table width="100%" cellpadding="0" cellspacing="0" border="0">
							<tr>
							  <td style="line-height: 0px;">
							  </td>
							</tr>
						  </table>
			<!-- GK: end spacer -->
			
			<!-- GK: text content -->
						  <table width="100%" cellpadding="0" cellspacing="0" border="0" >
							<tr>
							  <td align="center" valign="middle" style="font-family:Arial, Helvetica, sans-serif; font-size:16px; font-weight:normal; line-height:22px; letter-spacing:0px; color:#414141; padding-left:10px; padding-right:10px; min-height:20px; mso-line-height-rule: exactly; padding: 0px 25px;">
								  <br />
								  Nach einem speziellen Verfahren wurde Ihre E-Mail-Adresse ausgewählt:<br />
			
			( [em] )<br />
			<br />
			Sie haben es GESCHAFFT – Sie sind dabei!</strong><br />
			<br />
			
							  Wir freuen uns Ihnen mitzuteilen, dass Sie einer von 4 Teilnehmern in der Endauslosung sind. Sie haben jetzt die einmalige Chance, ein gratis &nbsp; <strong><br />
			 1.000€ AMAZON-Gutschein + iPhone 15 Pro Max</strong> zu gewinnen! <br />
			<br />
			Die anderen Teilnehmer in der Endauslosung sind: <br />
			1. Manuela Ö***<br />
			
			2. Dominik L***<br />
			
			3. Hermina T***<br />
			<br />
			
			 
			Jetzt schnell und einfach eintragen und qualifizieren Sie sich noch heute!<br />
			<br />
			
			 
			Wir wünschen viel Spaß und Erfolg!<br />
			
			Ihr Noah Müller vom Gutschein-Team
			 <br />
			<!-- GK: end text content -->
			
			<!-- GK: spacer -->
								  <table width="100%" cellpadding="0" cellspacing="0" border="0">
									<tr>
									  <td style="padding-top: 10px; line-height: 0px;">
									  </td>
									</tr>
								  </table>
			<!-- GK: end spacer -->
			
			<!-- GK: CTA (Button) -->
								  <table width="70%" cellpadding="0" cellspacing="0" border="0">
									<tr>
									  <td align="center" valign="top" style="padding: 0 20px;">
										<table cellpadding="0" cellspacing="0" border="0">
										  <tr>
											<td style="padding-top: 5px; line-height: 0px;">
											</td>
										  </tr>
										  <tr>
											<td width="350" align="center" valign="top">
											  <table width="100%" cellpadding="0" cellspacing="0" border="0">
												<tr>
												  <td width="350" height="40" align="center" valign="middle" style="background-color:#ff9900; padding: 6px 12px; ">
													<a style="display: block; text-decoration: none; font-family: 'Arial', verdana, sans-serif; font-size: 18px; mso-line-height-rule: exactly; line-height: 32px;font-weight: bold; color: #ffffff;" href="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/trk1_clk?em_ofid=[em]|[of_id]" target="_blank"> 
														 Jetzt mitmachen!
													</a>
												  </td>
												</tr>
											  </table>
											</td>
										  </tr>
										</table>
									  </td>
									</tr>
								  </table>
			<!-- GK: end CTA (Button) -->
			
								</td>
							  </tr>
							</table>
			
			<!-- GK: spacer -->
							<table width="100%" cellpadding="0" cellspacing="0" border="0">
							  <tr>
								<td style="padding-top: 40px; line-height: 0px;">
								</td>
							  </tr>
							</table>
			<!-- GK: end spacer -->
			
			<!-- GK: spacer -->
							<table width="100%" cellpadding="0" cellspacing="0" border="0" style=" background-color: #151515;">
							  <tr>
								<td style="padding-top: 60px; line-height: 0px;">
								</td>
							  </tr>
							</table>
			<!-- GK: end spacer -->
			
						</td>
					</tr>
				  </table></td>
			  </tr>
			</table>
			<!-- end container -->
			</body>
		</html>
"""

#for x in range(1):
for smtp in smtps:
	bcl = True
	nb_send = 0
	smtp = smtps[x]
	if smtp['ready'] == True:
		receiver_email = "kamlal.fahmi@yahoo.com"
		sender_email = smtp['username']
		password = smtp['pass']
		#for y in range(10):
		while bcl == True:
			user_bool = True
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
			
			print('receiver_email: ', receiver_email)
			msg = msg.replace('[em]', receiver_email)
			msg = msg.replace('[of_id]', of_id)
			send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, smtp['id'], smtp['host'])
		time.sleep(60)
		check_imap(smtp['id'], smtp['imap'], smtp['username'], smtp['pass'])






