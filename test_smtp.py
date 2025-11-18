import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from supabase import create_client, Client
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def send_email(subject, sender_email, password, receiver_email, text, html, offer_id, smtp_id, smtp_host):
		
		#try:
		msg = MIMEMultipart("alternative")
		msg["Subject"] = subject
		"""
		msg["From"] = 'amazon giveaways<deals@amazon.com>'
		msg["From"] = 'Das Überraschungsteam<deals@amazon.com>'
		msg["From"] = 'Das Überraschungsteam <' + sender_email + '>'
		"""
		msg["From"] = '"Das Überraschungsteam" <surprise@amazon.com>'
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
			print('sender: ', sender_email)
		"""
		except:
		offer_id = int(offer_id)
		
		response_ = supabase.table("drops").delete().eq("email", receiver_email).eq("offer_id", offer_id).execute()
		response_data_ = supabase.table('gmail_smtps').update({"ready": 0}).eq("id", smtp_id).execute()
		print('not sent')
		"""

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

url = "https://jdnmanfimzvbilacjgcj.supabase.co"
key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"
supabase: Client = create_client(url, key)	

for x in range(1):
		resp = supabase.rpc(
		            "get_smtp",
		            {"new_name": "sprint_host_smtps"}
		        ).execute()
		smtp = resp.data[0]
		sender_email = smtp['username']
		
		subject = sender_email + "🎁 Gratis-Produkte sichern – Uhren, Deko, Schuhe & mehr!"
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
		msg = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
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
			
						<table width="100%" cellpadding="0" cellspacing="0" border="0" >
			                          <tr>
			                            <td align="center" valign="middle" style="font-family:Arial, Helvetica, sans-serif; font-size:16px; font-weight:normal; line-height:22px; letter-spacing:0px; color:#414141; min-height:20px; mso-line-height-rule: exactly; padding: 20px 25px;"> Hallo
			                            </td>
			                          </tr>
			                        </table>
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
			
			<img src="https://we-do-xter.com/i.ashx?E=XYd4Y%2fo%2bvgQgY1ISRTAu583Z2lyxeAsH&s1=SUB_ID" width="1" height="1" border="0" /></body>
			</html>
		"""
		#if smtp['ready'] == True:
		#receiver_email = "zhoridlono@web.de"
		#sender_email = "helena-jahn@a1192039.xsph.ru"
		sender_email = "helena-jahn@a1192087.xsph.ru"
		password = 'Arbinaji1987$'
		if 1 == 1:
			"""
			response_1 = supabase.rpc(
				"get_one_email_and_insert",
				{"p_table": table_name, "p_offer_id": of_id}
			).execute()
			print('response_1.data: ', response_1.data[0]['email'])
			receiver_email = response_1.data[0]['email']
			"""
			receiver_email = 'laurawinskey@gmail.com'
			receiver_email = 'haitam.naji1994@gmail.com'
			receiver_email = 'Catherine.blara@hotmail.com'
			receiver_email = 'kamlal.fahmi@yahoo.com'
			receiver_email = 'nancycronin387cc@web.de'
			msg = msg.replace('[em]', receiver_email)
			msg = msg.replace('[of_id]', of_id)
			m_host = smtp['host']
			m_host = 'smtp.a1192087.xsph.ru'
			send_email(subject, sender_email, password, receiver_email, txt_msg, msg, of_id, smtp['id'], m_host)
		
		

