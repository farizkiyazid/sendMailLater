import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgres://hccwclzwgseygw:6b0825488e4175031a47a7917be4b51393a908cc5afa72fae7c7886b5faa6445@ec2-174-129-33-186.compute-1.amazonaws.com:5432/d2bhvua8dpvqda'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = False
    # For default email sender I used my personal email, but for safety reasons, I removed it to be filled locally
    MAIL_SERVER = ''
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    # MAIL_DEBUG = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = None
    # MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATACHMENTS = False
