'''Write a program using smtplib and email.mime to send a plain-text email with a subject,
greeting, and short body to a given recipient using Gmail SMTP (or a local test server).'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'tarunnagpal192004@gmail.com'
msg['To'] = 'tarun.nagpal@simformsolutions.com'
msg['Subject'] = 'Greetings'
body = "Hello to you!!!"
msg.attach(MIMEText(body,'plain'))

try:
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login("tarunnagpal192004@gmail.com",'fcyn mzmd siha vswq')
        server.send_message(msg)
        print("Sended Succesfully")
except Exception as e:
    print(e)