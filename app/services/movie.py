from flask_restx import abort

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO


class MovieService:
    """
    The MovieService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: MovieDAO):
        """
        The function takes, as a parameter, an object of the MovieDAO class during initialization.
        """
        self.dao = dao

    def get_all_by_director_and_genre(self, did: int, gid: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_director_and_genre(did, gid)

    def get_all_by_director(self, did: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_director(did)

    def get_all_by_genre(self, gid: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_genre(gid)

    def get_all_by_page(self, page: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_page(page)

    def get_all_by_page_new(self, page: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_page_new(page)

    def get_all(self):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all()

    def get_all_new(self):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_new()

    def get_one(self, mid: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        movie = self.dao.get_one(mid)
        if movie is None:
            abort(404)
        return movie




