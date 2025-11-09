import imaplib
import email
import re
import csv
import os
from supabase import create_client, Client
"""
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
"""
url = "https://jdnmanfimzvbilacjgcj.supabase.co"
key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"
supabase: Client = create_client(url, key)
response = supabase.table("gmail_smtps").select("*").execute()
smtps = response.data

def insert_email_to_supabase(p_email):
    result = supabase.rpc(
        "insert_bounced_email",
        {"p_email": p_email}
    ).execute()

"""
python gmail_collect.py
"""

# === CONFIG ===
for smtp in smtps:
    IMAP_SERVER = smtp['imap']
    EMAIL_ACCOUNT = smtp['username']
    EMAIL_PASSWORD = smtp['pass'].replace(" ","")
    
    try:
        # === CONNECT ===
        imap = imaplib.IMAP4_SSL(IMAP_SERVER)
        imap.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        
        # Search both inbox and spam if needed
        imap.select("INBOX")
        
        # Search common bounce indicators
        # mailer-daemon, postmaster, or common bounce subjects
        search_criterias = '(FROM "Mail Delivery System")'
        if '@gmail' in smtp['username']:
            search_criterias = '(FROM "Mail Delivery Subsystem")'
        elif '@yandex.com' in smtp['username']:
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
            aa = re.search(r"Message blocked", str(msg), re.I)
            bb = re.search(r"Message bloqué", str(msg), re.I)
            if aa or bb:
                aaa = str(aa.group())
                print("aaa: ", aaa)
                imap.store(msg_id, '+FLAGS', '\\Deleted')
            else:
                To = str(mm.group()).replace("Final-Recipient: rfc822;", "")
                To = To.replace(" ", "")
                print("To: ", To)
                reason_code_1 = "550 Requested action not taken: mailbox unavailable"
                reason_code_2 = "554-IP address is block listed"
                reason_code_3 = "all hosts for 'web.de' have been failing for a long time (and retry time not reached)"
                rc_1 = re.search(reason_code_1, str(msg), re.I)
                rc_2 = re.search(reason_code_2, str(msg), re.I)
                rc_3 = re.search(reason_code_3, str(msg), re.I)
                if rc_1:
                    insert_email_to_supabase(To)
                elif rc_2 or rc_3:
                    """
                    result_1 = supabase.rpc(
                        "update_reason",
                        {"uid": smtp['id']}
                    ).execute()
                    """
                    response_data_ = supabase.table('gmail_smtps').update({"ready": 0, "reason": "blacklisted"}).eq("id", smtp['id']).execute()
                imap.store(msg_id, '+FLAGS', '\\Deleted')
        imap.expunge()
        imap.logout()
    except:
        pass

