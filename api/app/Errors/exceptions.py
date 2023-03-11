
class InvalidUserException(Exception):
    status_code: int = 401
    def __init__(self, message):
        self.message = message
        


class NoTokenException(Exception):
    status_code: int = 400
    def __init__(self, message):
        self.message = message
        


class InvalidTokenException(Exception):

    status_code: int = 400

    def __init__(self, message):
        self.message = message
        


class InvalidCredentialsException(Exception):

    status_code: int = 401

    def __init__(self, message):
        self.message = message
        


class InvalidPasswordLengthException(Exception):

    status_code: int = 400

    def __init__(self, message):
        self.message = message
        

class InvalidPatentException(Exception):

    status_code: int = 400
    
    def __init__(self, message):
        self.message = message
        


class NotUniqueEmailException(Exception):

    status_code: int = 409

    def __init__(self, message):
        self.message = message
        


class NotFoundException(Exception):

    status_code: int = 404

    def __init__(self, message):
        self.message = message
        