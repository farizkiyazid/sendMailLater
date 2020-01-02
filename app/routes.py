from flask import render_template, request, current_app
from flask_mail import Message
from app import app, db, mail
from app.models import Emails
from threading import Thread
from app.emailScheduler import save_now

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kiki'}
    return render_template('index.html', title='Jublia', user=user)

@app.route('/email')
def saveEmailPage():
    return render_template('saveEmails.html', title='Jublia')

@app.route('/save_emails', methods=['GET', 'POST'])
def insertEmail():
    if request.method == 'POST':
        newEmailSubject = request.form['email_subject']
        newEmailContent = request.form['email_content']
        newTimestamp = request.form['timestamp']
        email = Emails(newEmailSubject, newEmailContent, newTimestamp)
        db.session.add(email)
        db.session.commit()
        # Default recipient use any email. I used a temporary email
        default_recipient = "digepo8061@email-9.com"
        save_now(newTimestamp, default_recipient, newEmailSubject, newEmailContent)
        return "<p>Inserted</p>"
    else:
        return "<p>you need to POST your request</p>"

