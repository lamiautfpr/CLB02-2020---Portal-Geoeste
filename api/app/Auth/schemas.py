from app.Auth.models import Patent
from app.extensions import auth_ns
from flask_restx import fields

class PatentField(fields.Raw):
    def format(self, value: Patent):
        return value._name_

user_schema = auth_ns.model('User', {
    'email': fields.String(required=True, description='User email'),
    'patent': PatentField(required=True, description='User patent'),
    'token': fields.String(required=True, description='User token')
})

user_registration_validation_schema = auth_ns.model('UserRegistrationValidation', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
    'patent': PatentField(required=True, description='User patent')
})
