import jwt
from flask import request
from flask_restx import Namespace, Resource

from app.constants import JWT_SECRET, JWT_ALGORITHM
from app.dao.model.user import UserSchema
from app.decorators import auth_required
from app.container import user_service


user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    """
    The UserView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/users/<int:uid>".
    """

    @auth_required
    def get(self):
        """
        The function takes as an argument the ID of the user in the form of an integer and is intended
        for processing a GET request to the address "/users/<in:uid>", implements a search for
        a user in the database,returns the found database object in the form of JSON.
        """
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        user_dict = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = user_dict.get("email", None)
        user = user_service.get_by_email(email)
        return user_schema.dump(user)

    @auth_required
    def patch(self):
        """
               The function takes as an argument the ID of the user in the form of an integer and is intended
               for processing the PUT request to the address "/users/<int:uid>", implements the search and updating
               of data about the user returns an updated database object in the form of JSON in the database.
               """
        req_json = request.json
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user_dict = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = user_dict.get("email", None)
        user = user_service.update(req_json, email)
        return user_schema.dump(user)


@user_ns.route('/password')
class UserPasswordView(Resource):
    """
    The UserPasswordView class inherits from the Resource class of the flask_restx library and
    is a Base View Class designed to process requests at the address "/users/password"
    """
    @auth_required
    def put(self):
        """
        The function takes as an argument the ID of the user in the form of an integer and is intended
        for processing the PUT request to the address "/users/<int:uid>", implements the search and updating
        of data about the user returns an updated database object in the form of JSON in the database.
        """
        req_json = request.json
        password_1, password_2 = req_json["password_1"], req_json["password_2"]
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user_dict = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = user_dict.get("email", None)
        user = user_service.change_password(password_1, password_2, email)
        
        return user_schema.dump(user)



