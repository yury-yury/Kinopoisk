import jwt
from flask import request
from flask_restx import Namespace, Resource

from app.constants import JWT_SECRET, JWT_ALGORITHM
from app.dao.model.favorite import FavoriteSchema
from app.decorators import auth_required
from app.container import favorite_service


favorite_ns = Namespace('/favorites/movies')

favorite_schema = FavoriteSchema()
favorites_schema = FavoriteSchema(many=True)


@favorite_ns.route('/<int:mid>')
class FavoriteView(Resource):
    """
    The FavoriteView class inherits from the Resource class of the flask_restx library and
    is a Base View Class designed to process requests at the address "/favorites/movies/<int:mid>".
    """
    @auth_required
    def post(self, mid: int):
        """
        The function takes the movie ID as an argument and is designed to process POST requests
        at the address "/favorites/movies/<int:mid>", implements the creation and addition of
        a new object to the favorite database table, returns the created object as JSON.
        """
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user_dict = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = user_dict.get("email", None)
        favorite = favorite_service.create(mid, email)
        return favorite_schema.dump(favorite)

    @auth_required
    def delete(self, mid: int):
        """
        The function takes the movie ID as an argument and is designed to process DELETE requests
        at the address "/favorites/movies/<int:mid>", implements search and deletion from
        the favorite table of the object database.
        """
        token = request.headers['Authorization'].split('Bearer ')[-1]
        user_dict = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = user_dict.get("email", None)
        favorite_service.delete(mid, email)
        return ""