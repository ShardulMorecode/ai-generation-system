import smtplib
from email.mime.text import MIMEText

def send_email_notification(to_email, user_id, content_url):
    sender_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEText(f"Your content is ready! View it here: {content_url}")
    msg['Subject'] = "Content Ready Notification"
    msg['From'] = sender_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, msg.as_string())