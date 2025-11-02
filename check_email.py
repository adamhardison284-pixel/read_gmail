import smtplib
import dns.resolver

def check_email_exists(email):
    # Extract domain (e.g. gmail.com)
    domain = email.split('@')[-1]
    try:
        # Get MX records for the domain
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
    except Exception as e:
        return {"email": email, "exists": False, "error": f"DNS error: {e}"}

    # SMTP setup
    host = 'your-domain.com'  # replace with your domain or any hostname
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    try:
        server.connect(mx_record)
        server.helo(host)
        server.mail('test@' + host)
        code, message = server.rcpt(email)
        server.quit()

        if code == 250:
            return {"email": email, "exists": True, "status": message.decode()}
        else:
            return {"email": email, "exists": False, "status": message.decode()}
    except Exception as e:
        return {"email": email, "exists": False, "error": str(e)}

# Example usage
emails = ["kaamalennaaaji@yahoo.com"]
for email in emails:
    print(check_email_exists(email))
