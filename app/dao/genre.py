from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


class GenreDAO:
    """
    The GenreDAO service class, which is Data Access Objects, is designed to perform
    all necessary operations with the database.
    """
    def __init__(self, session):
        """
        The function takes, as a parameter, a database access object during initialization.
        """
        self.session = session

    def get_all(self):
        """
        The function defines the method of the class .get_all and queries all records
        of the "genre" table of the database and returns it for further use.
        """
        return self.session.query(Genre).all()

    def get_all_by_page(self, page: int):
        """
        The function defines the method of the class .get_all takes the page number
        as a parameterand queries all recordsof the "genre" table of the database
        and performs its page-by-page returns for further use.
        """
        return self.session.query(Genre).limit(12).offset((page - 1) * 12).all()

    def get_one(self, gid: int):
        """
        The function defines the method of the class .get_one takes the row ID as a parameter
        and queries the "movie" table entry of the database containing this parameter
        in the corresponding column and returns for further use.
        """
        return self.session.query(Genre).get(gid)

    def get_list_movie_by_genre(self, gid: int):
        """
         The function defines the method of the class .get_list_by_genre takes the genre ID as a parameter
        and queries all records of the "movie" table of the database containing this parameter
        in the corresponding column and returns for further use.
        If there are no such records, returns an empty list.
        """
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()
