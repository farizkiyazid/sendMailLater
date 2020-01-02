import datetime, calendar, time
from dateutil.parser import parse
from threading import Thread
from app import mail, app
from flask_mail import Message
from flask import current_app

# my current way of doing it in this example is by using the time we input at the POST request.
# what I think would be better is by constantly checking the database.
# That way if we change the time data manually, the schedule will change too.
# Where in this code, it still follows the initial date.
# I'm choosing this way at the moment for convinience and if I had more time, I'd definitely choose the better approach above.

def save_now(specifiedTime, recipient, email_subject, email_content):
    x = datetime.datetime.strptime(specifiedTime, '%Y-%m-%d %H:%M:%S')
    Thread(target=scheduling, args=(app, x, recipient, email_subject, email_content)).start()

def scheduling(currApp, specifiedTime, recipient, email_subject, email_content):
    now = datetime.datetime.now()
    if specifiedTime>now :
        time.sleep(5)
        save_now(currApp, specifiedTime, recipient, email_subject, email_content)
    else :
        print("done")
        print(specifiedTime, recipient, "| Subject:", email_subject, "| Content:", email_content)
        msg = Message(email_subject, sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[recipient])
        msg.body = email_content
        send_async_email(currApp, msg)    

def send_async_email(currApp, msg):
    with currApp.app_context():
        mail.send(msg)
