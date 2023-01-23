from flask import request, jsonify
from flask_restx import Namespace, Resource

from app.dao.model.movie import MovieSchema
from app.decorators import auth_required
from app.container import movie_service


movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    The MovieView class inherits from the Resource class of the flask_restx library
    and is the base viewer class designed to handle all requests to the address "/movies/".
    """
    @auth_required
    def get(self):
        """
        The function defines a class method and is designed to process GET requests at "/movies/",
        tracks and organizes various types of movie searches: all movies, movies of a certain genre,
        movies of a certain director and movies of a certain director and genre.
        """
        if request.args.get("director_id") and request.args.get("genre_id"):
            did = int(request.args.get("director_id"))
            gid = int(request.args.get("genre_id"))
            movies = movie_service.get_all_by_director_and_genre(did, gid)
            return movies_schema.dump(movies)

        elif request.args.get("director_id"):
            did = int(request.args.get("director_id"))
            movies = movie_service.get_all_by_director(did)
            return movies_schema.dump(movies)

        elif request.args.get("genre_id"):
            gid = int(request.args.get("genre_id"))
            movies = movie_service.get_all_by_genre(gid)
            return movies_schema.dump(movies)

        elif request.args.get("status") == "new":
            if request.args.get("page"):
                page = request.args.get("page", type=int)
                all_movies = movie_service.get_all_by_page_new(page)
                return movies_schema.dump(all_movies)
            else:
                all_movies = movie_service.get_all_new()
                return movies_schema.dump(all_movies)

        elif request.args.get("page"):
            page = request.args.get("page", type=int)
            all_movies = movie_service.get_all_by_page(page)
            return movies_schema.dump(all_movies)

        else:
            all_movies = movie_service.get_all()
            return movies_schema.dump(all_movies)


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    he MovieView class inherits from the Resource class of the flask_rectx library and
    is a Base View class designed to process requests at the address "/movies/<int:mid>".
    """
    @auth_required
    def get(self, mid: int):
        """
        The function takes as an argument the id of the movie as an integer and is designed to process
        a GET request at the address "/movies/<int:mid>", implements a search for the movie in the database,
        returns the found database object in the form of JSON.
        """
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie)

