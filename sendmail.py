# -*- coding: utf-8 -*-
#确认邮箱开启了smtp，password是客户端授权密码
__author__ = 'lk'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(fromEmail, username, password, serverAddress, subject, htmlContent, toEmail):
    '''
    fromEmail: 使用哪个邮箱地址发送
    username: 登陆邮箱服务器的用户名，一般与fromEmail相同
    password: 登陆的密码 邮箱客户端授权码
    serverAddress: 邮箱服务的地址（包含端口）
    subject: 邮件主题
    htmlContent: 邮件正文，使用html格式编写
    toEmail: 要发送到的邮箱地址，可以写多个
    '''
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = ', '.join(toEmail)
    msg["Accept-Language"] = "zh-CN"  # 指定语言环境是中文
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"  # 指定使用特定的编码，防止乱码
    part = MIMEText(htmlContent, 'html', 'UTF-8')
    msg.attach(part)

    s = smtplib.SMTP(serverAddress)
    print "Try to login"
    s.login(username, password)
    print "login successfully, try to send"
    s.sendmail(fromEmail, toEmail, msg.as_string())
    print "send successfully"
    s.quit()


sendMail(fromEmail='发送方',
         username="",
         password="",
         serverAddress='smtp.163.com:25',
         subject='Python邮件代码测试',
         htmlContent="宝贝你好呀.(By Osero)",
         toEmail=['XXXX@XX.com'])
