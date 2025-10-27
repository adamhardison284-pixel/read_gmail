import imaplib
import email
import re
import csv
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
response = supabase.table("gmail_smtps").select("*").execute()
smtps = response.data

def insert_email_to_supabase(p_email):
    result = supabase.rpc(
        "insert_bounced_email_github",
        {"p_email": p_email}
    ).execute()

"""
python gmail_collect.py
"""

# === CONFIG ===
for smtp in smtps:
    IMAP_SERVER = "imap.gmail.com"
    EMAIL_ACCOUNT = smtp['username']
    EMAIL_PASSWORD = smtp['pass'].replace(" ","")
    
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
    print(f"Found {len(msg_ids)} possible bounces to {acc[0]}.")
    
    rows = []
    for msg_id in msg_ids:
        result, msg_data = imap.fetch(msg_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        mm = re.search(r"Final-Recipient:\s*[^;]+;\s*([^\s]+)", str(msg), re.I)
        aa = re.search(r"Message blocked", str(msg), re.I)
        bb = re.search(r"Message bloqué", str(msg), re.I)
        if aa or bb:
            aaa = str(aa.group())
            print("aaa: ", aaa)
            imap.store(msg_id, '+FLAGS', '\\Deleted')
        else:
            To = str(mm.group()).replace("Final-Recipient: rfc822; ", "")
            insert_email_to_supabase(To)
            imap.store(msg_id, '+FLAGS', '\\Deleted')
    imap.expunge()
    imap.logout()

