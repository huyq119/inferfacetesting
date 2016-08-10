#coding=utf-8
import ConfigParser,os,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_conf():
    conf_file = ConfigParser.ConfigParser()
    conf_file.read(os.path.join(os.getcwd(),'conf.ini'))
    conf = {}
    conf['sender'] = conf_file.get("email","sender")
    conf['receiver'] = conf_file.get("email","receiver")
    conf['smtpserver'] = conf_file.get("email","smtpserver")
    conf['username'] = conf_file.get("email","username")
    conf['password'] = conf_file.get("email","password")
    return conf

def sendMail(text):
    mail_info = get_conf()
    sender = mail_info['sender']
    receiver = mail_info['receiver']
    subject = '[AutomationTest]接口自动化测试报告通知'
    smtpserver = mail_info['smtpserver']
    username = mail_info['username']
    password = mail_info['password']

    msg = MIMEMultipart()

    att1 = MIMEText(text, 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename = "result.html"'
    msg.attach(att1)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ''.join(receiver)
    smtp = smtplib.SMTP("smtp-mail.outlook.com",25)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

html = '接口自动化扫描'
sendMail(html)