from app.Errors.exceptions import InvalidCredentialsException, InvalidPasswordLengthException, InvalidPatentException, InvalidTokenException, NoTokenException, NotUniqueEmailException
import jwt
from flask import request, jsonify, session
from flask_restx import Resource
from passlib.hash import pbkdf2_sha256
from app.extensions import auth_ns
from app.Auth.models import Patent, User
from app.Auth.auth import token_required, create_token
from app.Auth.schemas import user_schema, user_registration_validation_schema
from flask_session import Session


def init_auth_services(app):
    server_session = Session(app)

    @auth_ns.route('/register', methods=['POST'])
    class RegisterResource(Resource):
        @auth_ns.doc(security=None, responses={200: 'Success', 409: 'Email already registered', 401: 'Invalid Credentials'})
        def post(self):
            email = request.json['email']
            pwd = request.json['password']
            patent = Patent.a93E33E251F414A32.name

            user = User.query.filter_by(email=email).first()

            if user is not None:
                raise NotUniqueEmailException("Email already registered")
            if len(pwd) < 6 or len(pwd) > 10:
                raise InvalidPasswordLengthException("At least 6 characters and at most 10")
            if patent not in Patent._member_names_:
                raise InvalidPatentException("Invalid patent")

            hashed=pbkdf2_sha256.hash(pwd)
            new_user = User(email=email, password=hashed, patent=patent)
            new_user.add_to_db()

            token = create_token(new_user)
            session['token'] = token

            return jsonify({
                'message': 'User created',
                'token': token
            })


    @auth_ns.route('/login', methods=['POST'])        
    class LoginResource(Resource):
        @auth_ns.doc(security=None, responses={200: 'Success', 401: 'Invalid Credentials'})
        def post(self):
            
            email = request.json['email']
            pwd = request.json['password']
            user = User.query.filter_by(email=email).first()
    
            if user is None or not pbkdf2_sha256.verify(pwd, user.password):
                raise InvalidCredentialsException("Invalid Credentials")

            existing_token = session.get('token')

            try:
                data = jwt.decode(existing_token, app.config['SECRET_KEY'], algorithms=["HS256"])
                if data['id'] == user.id:
                    return jsonify({
                        'token': existing_token
                    })
            except:
                pass

            token = create_token(user)

            session['token'] = token

            return jsonify({
                'token': token
            })



    @auth_ns.route('/refresh', methods=['GET'])
    class RefreshResource(Resource):
        @auth_ns.doc(security='Token Auth', responses={200: 'Success', 401: 'Invalid Token'})
        def get(self):
            token = session.get('token')
            if not token:
                raise NoTokenException("Invalid Token!")

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                user_id = data['id']
                user = User.query.filter_by(id = user_id).first()
                if user:
                    session.pop('token', None)
                    token = create_token(user)
                    session['token'] = token
                    return jsonify({
                        'token': token
                    }), 200
                else:
                    raise InvalidTokenException("Invalid Token!")
            except:
                return jsonify({'message': 'Token is invalid!'}), 403


    @auth_ns.route("/perfil", methods=['GET'])
    class ProfileResource(Resource):
        @auth_ns.marshal_with(user_schema)
        @auth_ns.doc(security='Token Auth', responses={200: 'Success', 401: 'Invalid Token'})
        def get(self):
            token = session.get('token')
            if not token:
                raise NoTokenException("Invalid Token!")
            
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                user_id = data['id']
                user = User.query.filter_by(id = user_id).first()
                if user:
                    response = {'email': user.email, 'patent': user.patent, 'token':token}
                    return response, 200
                else:
                    raise InvalidTokenException("Invalid Token!")
            except:
                return jsonify({'message': 'Token is invalid!'}), 403


    return auth_ns


