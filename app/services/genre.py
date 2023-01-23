from flask_restx import abort

from app.dao.genre import GenreDAO


class GenreService:
    """
    The GenreService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: GenreDAO):
        """
        The function takes, as a parameter, an object of the GenreDAO class during initialization.
        """
        self.dao = dao

    def get_all_by_page(self, page: int):
        """
         The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_page(page)

    def get_all(self):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all()

    def get_one_with_movie(self, gid: int):
        """
        The function defines the method of the class .get_one_with_movie takes the genre ID as a parameter,
        makes requests from the database object data acquisition object with the corresponding parameter
        and a list of related objects from the "movie" table, generates response data in the form
        of a dictionary and returns them.
        """
        genre = self.dao.get_one(gid)
        if genre is None:
            abort(404)
        movies = self.dao.get_list_movie_by_genre(gid)
        movies_list = list()
        for item in movies:
            movies_list.append(item.title)
        return {"id": genre.id, "name": genre.name, "movies": movies_list}
