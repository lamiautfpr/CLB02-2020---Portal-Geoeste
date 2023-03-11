from flask_restx import Namespace
from os import environ


class config(object):
    SECRET_KEY=environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_USER_IDENTITY_ATTRIBUTE = ('username','email')

    SESSION_TYPE = 'sqlalchemy'
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True

    data_ns=Namespace('Data')
    auth_ns=Namespace('Auth')



