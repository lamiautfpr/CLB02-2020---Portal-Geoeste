from flask import jsonify
from app.Errors.exceptions import InvalidCredentialsException, InvalidPasswordLengthException, InvalidPatentException, InvalidTokenException, NoTokenException, NotFoundException, NotUniqueEmailException
from sqlalchemy.exc import DataError, IntegrityError
from werkzeug.exceptions import BadRequest

def init_error_handlers(app):


    @app.errorhandler(NoTokenException)
    def handle_no_token_exception(e):
        return jsonify({"Error": "{}".format(e)}), 400


    @app.errorhandler(InvalidTokenException)
    def handle_invalid_token_exception(e):
        return jsonify({"Error": "{}".format(e)}), 400


    @app.errorhandler(InvalidCredentialsException)
    def handle_invalid_credentials_exception(e):
        return jsonify({"Error": "{}".format(e)}), 401

    
    @app.errorhandler(InvalidPatentException)
    def handle_invalid_patent_exception(e):
        return jsonify({"Error": "{}".format(e)}), 400


    @app.errorhandler(InvalidPasswordLengthException)
    def handle_invalid_password_length_exception(e):
        return jsonify({"Error": "{}".format(e)}), 400


    @app.errorhandler(NotUniqueEmailException)
    def handle_not_unique_email_exception(e):
        return jsonify({"Error": "{}".format(e)}), 409


    @app.errorhandler(NotFoundException)
    def handle_not_found_exception(e):
        return jsonify({"Error": "{}".format(e)}), 404


    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        return jsonify({"Error": "Bad Input Data", "Reason":"Parameters Integrity"}), 409


    @app.errorhandler(DataError)
    def handle_data_error(e):
        return jsonify({"Error": "Bad Input Type For ID"}), 400


    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        return jsonify({"Error": "Bad Request"}), 400

    return app