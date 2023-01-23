from flask import request
from flask_restx import Namespace, Resource

from app.dao.model.director import DirectorSchema
from app.decorators import auth_required
from app.container import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    """
    The Directory view class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/directors/".
    """
    @auth_required
    def get(self):
        """
        The function does not accept arguments and is designed to process GET requests at the address "/directors/",
        implements a search for all directors in the database, returns the found data in the form of JSON.
        """
        if request.args.get("page"):
            page = int(request.args.get("page"))
            directors = director_service.get_all_by_page(page)
            return directors_schema.dump(directors)

        else:
            directors = director_service.get_all()
            return directors_schema.dump(directors)


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """
    The Directory View class inherits from the Resource class of the flask_restx library and
    is a Base View class designed to process requests at the address "/directors/<int:did>".
    """
    @auth_required
    def get(self, did: int):
        """
        The function takes as an argument the ID of the director in the form of an integer and is intended
        for processing a GET request to the address "/directors/<in:did>", implements a search for
        a director in the database,returns the found database object in the form of JSON.
        """
        director = director_service.get_one(did)
        return director_schema.dump(director)

