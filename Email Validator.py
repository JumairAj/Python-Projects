import os
import random
import math
import smtplib


digits = '0123456789'

OTP = ''
for _ in range(6):
    OTP += digits[math.floor(random.random()*10)]

msg = f"""This is an automated message..
{OTP}  is your OTP
      """

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('jumair1111@gmail.com', 'pjmwxmeqexmcvhxj')
email_id = input('Enter your email: ')
s.sendmail('&&&&&&&&&&&',email_id,msg)
wrong= 0
while True and wrong < 3:
    a = input('Enter your Otp>: ')
    if a == OTP:
        print('Verified')
        break
    else:
        print('please check the OTP again')
    wrong +=1
clear()