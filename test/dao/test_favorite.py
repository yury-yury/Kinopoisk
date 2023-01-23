from app.container import favorite_dao
from app.dao.model.favorite import Favorite


class TestFavoriteDAO:
    """
    The TestFavoriteDAO class is designed to test all methods of the FavoriteDAO class.
    """
    def test_get_user_by_email(self, user):
        """
        The function implements the test_get_user_by_email method of the TestFavoriteDAO class.
        Takes as an argument the user object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = favorite_dao.get_user_by_email(user.email)
        assert res is not None
        assert res == user

        res = favorite_dao.get_user_by_email("test")
        assert res is None

    def test_get_favorite(self, favorite):
        """
        The function implements the test_get_favorite method of the TestGenreDAO class.
        Takes as an argument the favorite object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = favorite_dao.get_favorite(1, 1)
        assert res is not None
        assert res == favorite

        res = favorite_dao.get_favorite(2, 2)
        assert res is None

    def test_create(self, db):
        """
        The function implements the test_update method of the TestFavoriteDAO class.
        Takes as an argument the db object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        favorite = Favorite(id=1, movie_id=1, user_id=1)
        favorite_2 = favorite_dao.create(favorite)
        favorite_1 = db.session.query(Favorite).first()
        assert favorite_1 is not None
        assert favorite == favorite_1
        assert favorite_1 == favorite_2

    def test_delete(self, db, favorite):
        """
        The function implements the test_delete method of the TestFavoriteDAO class.
        Takes as an argument the db and favorite objects prepared by the corresponding fixtures.
        Checks the correctness of the returned values when calling the method.
        """
        favorite_dao.delete(favorite)
        favorite_1 = db.session.query(Favorite).first()
        assert favorite_1 is None
