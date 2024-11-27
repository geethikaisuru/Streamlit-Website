import os
from dotenv import load_dotenv
import smtplib, ssl

def send_email(message, user_email, topic):
    load_dotenv()
    username = os.getenv('email')
    PASS = os.getenv('PASSWORD')

    host = "smtp.gmail.com"
    port = 587  # Using port 587 with starttls()

    receiver_email = user_email
    context = ssl.create_default_context()
    message_Full = f"""\
Subject: Contact Form Website: {user_email}

Topic: {topic}

{message}

From: {user_email}
"""

    try:
        with smtplib.SMTP(host, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(username, PASS)
            server.sendmail(username, receiver_email, message_Full)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
