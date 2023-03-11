from enum import Enum
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256
from ..extensions import db, login_manager


class Patent(Enum):
    a5FB374A934D584AF = 'ADMIN'
    aF6A29FB56F7AEEC8 = 'RESEARCHER'
    a93E33E251F414A32 = 'GUEST'
    


class User(UserMixin, db.Model):

    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(), unique=True, nullable=False)
    password=db.Column(db.String(), nullable=False)
    patent=db.Column(db.Enum(Patent), nullable=False)


    def __repr__(self):
        return str(self.email)


    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    

    def update_password(self, password, new_password):
        if pbkdf2_sha256.verify(password, self.password):
            self.password=pbkdf2_sha256.hash(new_password)
            db.session.commit()
            return True
        else:
            return False


    def check_permission(self, patent):
        return self.patent == patent
   

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    return user if user else None
