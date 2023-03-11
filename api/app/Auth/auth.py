import datetime
from functools import wraps
from app.Errors.exceptions import InvalidTokenException, NoTokenException
from flask import request, jsonify, current_app, Response
from .models import Patent, User
import jwt


def create_token(user: User, days=1):
    if user.patent is None:
        user.patent = Patent.a93E33E251F414A32
    payload = {
        'id': user.id,
        'email': user.email,
        'patent': user.patent.value,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=days)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'])
    return token


def decode_token(token: str):
    try:
        token_pure  = token.replace("Bearer ", "")
        data = jwt.decode(token_pure, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        return data
    except Exception as e:
        raise InvalidTokenException('Invalid on Expired Token')


def find_user_by_token(token: str):
    data = decode_token(token)
    user = User.query.filter_by(id=data['id']).first()
    return user, data


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'authorization' in request.headers:
            token = request.headers['authorization']
        if not token:
            raise NoTokenException("No Token Provided")

        try:
            current_user, data = find_user_by_token(token)
            assert current_user is not None
            assert current_user.patent == None or current_user.patent == Patent.a5FB374A934D584AF
            assert current_user.email == data['email']
        except:
            raise InvalidTokenException('Invalid on Expired Token')
        return f(current_user=current_user, *args, **kwargs)

    return decorated
