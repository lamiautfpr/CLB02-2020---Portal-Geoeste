from flask_restx import Namespace
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
data_ns=Namespace('api/Data')
auth_ns=Namespace('api/Auth')
