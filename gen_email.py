import smtplib, ssl, email
import os
import sys


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email():
    
    
    message = ""
    f = open("dat.txt", "r")
    lines = f.readlines()
    for line in lines:
        
        message += line
    print("content: "+message)
    subject = "Email Notifier"
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "jtemailnotifier@gmail.com"  # Enter your address
    receiver_email = "jtmt15@hotmail.com"  # Enter receiver address
    password = "UwUCumS0x69!"

    

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
    print("sent email!")

send_email()


