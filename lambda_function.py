import smtplib
from email.mime.text import MIMEText
import ast

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

def lambda_handler(event, context):
    message = ast.literal_eval(event['Records'][0]['Sns']['Message'])
    if message['eventType'] == "BookclubCreate":
        subject = "Book Club Created!"
        body = "Book club created."
    elif message['eventType'] == "BookclubUpdate":
        subject = "Book Club Updated!"
        body = "You have updated " + message["bookclub_name"] + "."
    elif message['eventType'] == "BookclubDelete":
        subject = "Book Club Deleted"
        body = "You have deleted " + message["bookclub_name"] + "."
    elif message['eventType'] == "addMembers":
        subject = "Welcome to " + message["bookclub_name"]
        body = "You have been added to " + message["bookclub_name"] + "!"
        
    sender = "sahil.mahendrakar@gmail.com"
    recipients = message['recipient_emails']
    password = "nzqc qdpb bcpm sqex"
    
    send_email(subject, body, sender, recipients, password)


