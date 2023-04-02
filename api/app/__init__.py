from app.Auth.Services.auth_services import init_auth_services
from app.Errors.exceptions import NoTokenException
from app.Errors.handlers import init_error_handlers
from flask import Flask, jsonify, session
from flask_restx import Api
from flask_compress import Compress
from flask_cors import CORS
from flask_session import Session
from .extensions import db, login_manager, data_ns
from .Data.modules.Map.Services.MapModuleService import MapModuleService
from .Data.modules.Member.Services.MemberModuleService import MemberModuleService


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def create_app(config):
    app=Flask(__name__, static_url_path='/', template_folder='templates')
    Compress(app) 
    app.config.from_object(config)
    server_session = Session(app)

    @app.route('/api')
    def index():
        return  "200"


    @app.route("/api/logout", methods=['POST'])
    def logout():
        session_token = session.get('token')
        if session_token:
            session.pop('token')
            return jsonify({"message": "Successful Logout"}), 200
        else:
            raise NoTokenException("Invalid or Expired Token")


    @app.errorhandler(401)
    def handle_401(e):
        return jsonify({"Error": "No Token Provided"}), 401


    CORS_ALLOW_ORIGIN="*,*"
    CORS_EXPOSE_HEADERS="*,*"
    CORS_ALLOW_HEADERS="content-type,*"
    cors = CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , expose_headers= CORS_EXPOSE_HEADERS.split(","),   supports_credentials = True)
    register_extensions(app)
    api=Api(app, doc="/docs")
    service = MapModuleService()
    member_service = MemberModuleService()
    namespace = service.services(data_ns)
    namespace = member_service.services(namespace)
    auth_namespace = init_auth_services(app)
    api.add_namespace(namespace)
    api.add_namespace(auth_namespace)

    app = init_error_handlers(app)

    return app
    
    
