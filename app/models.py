from app import db
import datetime

class Emails(db.Model):
    __tablename__ = 'emails'

    event_id = db.Column(db.Integer, primary_key=True)
    email_subject = db.Column(db.String())
    email_content = db.Column(db.String())
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, email_subject, email_content, timestamp):
        self.email_subject = email_subject
        self.email_content = email_content
        self.timestamp = timestamp

    def __repr__(self):
        return '<event_id {}>'.format(self.id)
