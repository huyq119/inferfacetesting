#!/usr/bin/python
#  -*- coding: utf-8 -*-

from email.mime.text import MIMEText
msg = MIMEText("this is test for email","plain","utf-8")

# 输入Email地址和口令:
from_addr = "huyuqi@chinau.cc"
password = "huyuqi119+1"
# 输入SMTP服务器地址:
smtp_server = "smtp.ym.163.com"
# 输入收件人地址:
to_addr = "54234133@qq.com"

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()