from app.dao.model.movie import Movie
from app.dao.model.user import User
from app.dao.model.genre import Genre
from app.dao.model.director import Director
from app.dao.model.favorite import Favorite


class TestModels:
    """
    The TestModels class is designed to test models of database.
    """
    def test_users(self):
        """
        The function implements the test_user method of the TestModel class. Does not accept arguments.
        Checks the correctness of the values of the fields of the created objects of the User class.
        """
        user = User(name="oleg", email="oleg@oleg.ru", surname="user",
                          password="nePl4BfTTMW+TIHNef+bkLp5V8uGfsmtL7Zz1P5Ff5U=")

        assert user.name == "oleg"
        assert user.email == "oleg@oleg.ru"
        assert user.password == "nePl4BfTTMW+TIHNef+bkLp5V8uGfsmtL7Zz1P5Ff5U="
        assert user.favorit_genre_id is None

    def test_movie(self):
        """
        The function implements the test_movie method of the TestModel class. Does not accept arguments.
        Checks the correctness of the values of the fields of the created objects of the Movie class.
        """
        movie = Movie(title="Test_1", description="description_1", trailer="trailer_1",
                        year=2018, rating=8.6,	genre_id=1, director_id=1)

        assert movie is not None
        assert movie.title == "Test_1"
        assert movie.description == "description_1"
        assert movie.year == 2018

    def test_genre(self):
        """
        The function implements the test_genre method of the TestModel class. Does not accept arguments.
        Checks the correctness of the values of the fields of the created objects of the Genre class.
        """
        genre = Genre(name="Test")

        assert genre is not None
        assert genre.name == "Test"

    def test_favorite(self):
        """
        The function implements the test_favorite method of the TestModel class. Does not accept arguments.
        Checks the correctness of the values of the fields of the created objects of the Favorite class.
        """
        favorite = Favorite(user_id=1, movie_id=1)

        assert favorite is not None
        assert favorite.movie_id == 1
        assert favorite.user_id == 1

    def test_director(self):
        """
        The function implements the test_director method of the TestModel class. Does not accept arguments.
        Checks the correctness of the values of the fields of the created objects of the Director class.
        """
        director = Director(name="Test Director")

        assert director is not None
        assert director.name == "Test Director"