import imaplib
import email
import re
import csv

"""
python gmail_collect.py
"""
gmail_accounts = [
    ["haitam.naji1994@gmail.com","rrbu grio amvk nwkf"],
    ["laurawinskey@gmail.com","koergusxgtrupirm"],
    ["ennajikarim707@gmail.com","ygnf ujtq wjdq mpmw"],
    ["axelklengel9@gmail.com","qoiq erot tnob kcld"],
    ["axelklengel@gmail.com","ydzd lkts ofpg zjbv"],
    ["klatifa820@gmail.com","plkn ccef sbio lill"],
    ["edwardtlaurel113@gmail.com","qykm rdpp jxgc cwdu"],
    ["onelifestunning@gmail.com","oigw szwx uami gofg"],
    ["stevewatauga@gmail.com","ouqj thgm ufgc qntz"],
    ["walidfahmi100@gmail.com","lejd lalw hyxc vnkh"],
    ["fleischmannflorentin@gmail.com","tbhc oiwb plzt o...
    ["hoflereiner628@gmail.com","duny kuhn uale bnzo"],
    ["jemmywatford769@gmail.com","wqdh kcfg knkp saax"],
    ["johnlrape@gmail.com","fpsq leox ixov lsuq"],
    ["magnuskringel@gmail.com","wjbu qvfo xvva axti"],
    ["ottoschaeffer82@gmail.com","oimu thfv ldpk ywqr"],
    ["ralfcurschmann@gmail.com","kddi tcow mhrn rwri"],
    ["willyhardison89@gmail.com","tkgw zhdr mjkr baip"],
    ["wilsonleonardo355@gmail.com","mqfl kynw cyzi ggwy"],
    ["adamhardison284@gmail.com","gpum xjlm atlb stjg"]
]
# === CONFIG ===
for acc in gmail_accounts:
    IMAP_SERVER = "imap.gmail.com"
    #EMAIL_ACCOUNT = "haitam.naji1994@gmail.com"
    #EMAIL_PASSWORD = "rrbugrioamvknwkf"  # 16-char app password
    EMAIL_ACCOUNT = acc[0]
    EMAIL_PASSWORD = acc[0].replace(" ","")
    
    # === CONNECT ===
    imap = imaplib.IMAP4_SSL(IMAP_SERVER)
    imap.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    
    # Search both inbox and spam if needed
    imap.select("INBOX")
    
    # Search common bounce indicators
    # mailer-daemon, postmaster, or common bounce subjects
    search_criterias = '(FROM "Mail Delivery Subsystem")'
    
    result, data = imap.search(None, search_criterias)
    if result != "OK":
        print("No messages found.")
        imap.logout()
        exit()
    
    msg_ids = data[0].split()
    print(f"Found {len(msg_ids)} possible bounces.")
    
    rows = []
    for msg_id in msg_ids:
        result, msg_data = imap.fetch(msg_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        mm = re.search(r"Final-Recipient:\s*[^;]+;\s*([^\s]+)", str(msg), re.I)
        aa = re.search(r"Message blocked", str(msg), re.I)
        if aa:
            aaa = str(aa.group())
            print("aaa: ", aaa)
        To = str(mm.group()).replace("Final-Recipient: rfc822;", "")
        print(To)
        subject = msg.get("Subject", "")
        date = msg.get("Date", "")
        from_addr = msg.get("From", "")
    
        failed = ""
        """
        # Parse message parts to find failed recipient
        for part in msg.walk():
            if part.get_content_type() == "message/delivery-status":
                try:
                    text = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                    m = re.search(r"Final-Recipient:\s*[^;]+;\s*([^\s]+)", text, re.I)
                    if m:
                        failed = m.group(1)
                except:
                    pass
    
            elif part.get_content_type() == "text/plain" and not failed:
                body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                m = re.search(r"Recipient:\s*([^\s]+@[^\s]+)", body)
                if m:
                    failed = m.group(1)
    
        rows.append({
            "to": To,
            "date": date,
            "from": from_addr,
            "subject": subject,
            "failed_recipient": failed
        })
        """
    """
    # Save to CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["to", "date", "from", "subject", "failed_recipient"])
        writer.writeheader()
        writer.writerows(rows)
    """
    imap.logout()
    print(f"[✓] Saved {len(rows)} bounce messages to {acc[0]}")
