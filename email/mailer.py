#!/usr/bin/env python3
# dpw@plaza.localdomain
# dpw@plaza.localdomain

# locally, setup env vars for EMAIL_SENDER and EMAIL_PW

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """Sends an email using the provided details."""
    try:
        # Create a multipart message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, 'plain'))

        host = os.environ.get("SMTP_HOST")
        port = os.environ.get("SMTP_PORT")

        # Connect to the SMTP server
        with smtplib.SMTP_SSL(host, port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    sender = os.environ.get('EMAIL_SENDER')
    password = os.environ.get('EMAIL_PW')
    receiver = "dw@raincitysoftware.com"
    subject_text = "network status"
    body_text = "ok"

    send_email(sender, password, receiver, subject_text, body_text)
