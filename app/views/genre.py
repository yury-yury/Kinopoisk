from flask import request, jsonify
from flask_restx import Namespace, Resource

from app.dao.model.genre import GenreSchema
from app.container import genre_service
from app.decorators import auth_required


genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    """
    The GenresView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/genres/".
    """
    @auth_required
    def get(self):
        """
        The function does not accept arguments and is designed to process GET requests at the address "/genres/",
        implements a search for all genres in the database, returns the found data in the form of JSON.
        """
        if request.args.get("page"):
            page = int(request.args.get("page"))
            genres = genre_service.get_all_by_page(page)
            return genres_schema.dump(genres)

        else:
            genres = genre_service.get_all()
            return genres_schema.dump(genres)


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    The GenreView class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at "/genres/<int:gid>".
    """
    @auth_required
    def get(self, gid: int):
        """
        The function takes as an argument the genre identifier in the form of an integer and is intended
        for processing a GET request at the address "/genres/<in:gid>", implements a genre search
        in the database, returns the found database object in the form of JSON.
        """
        res = genre_service.get_one_with_movie(gid)
        return jsonify(res)

