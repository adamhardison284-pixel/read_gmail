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
		
