from flask import request
from flask_restx import Namespace, Resource

from app.views.user import user_schema
from app.container import auth_service, user_service


auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegView(Resource):
    """
    The AuthRegView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/auth/register".
    """
    def post(self):
        """
        The function does not accept arguments and is designed to process a POST request
        to the address "/auth/register", implements the creation of a new user and writing
        it to the database, returns the created database object in the form of JSON.
        """
        req_json = request.json
        new_user = user_service.create(req_json)
        return user_schema.dump(new_user)


@auth_ns.route('/login')
class AuthView(Resource):
    """
    The AuthView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/auth/login".
    """
    def post(self):
        """
        The function does not accept arguments and is designed to process a POST request at the address "/auth/login",
        checks the user registration data in the database and implements the creation of short-term
        and long-term tokens necessary to access the endpoints of the application returns the created
        objects in the form of JSON.
        """
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)
        if None in [email, password]:
            return "", 400
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        """
        The function does not accept arguments and is designed to process a PUT request at the address "/auth/login",
        checks a long-term token and implements the creation of short-term and long-term tokens necessary
        to access the endpoints of the application returns the created objects in the form of JSON.
        """
        data = request.json
        token = data.get("refresh_token")
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201