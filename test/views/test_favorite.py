import pytest

from app.dao.model.favorite import Favorite
from app.database import db


class TestFavoriteView:
    """
    The TestFavoriteView class is designed for functional testing of views implemented by methods
    of the FavoriteView class.
    """
    def test_create(self, client, header, movie):
        """
         The test_create function implements a method of the TestFavoriteView class. Accepts as arguments
         the client, movie, and header objects created by the corresponding fixtures.
         Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        responce = client.post('/favorites/movies/1', headers=header)
        assert responce.status_code == 200
        assert type(responce.json) == dict
        assert responce.json == {"id": 1, "user_id": 1, "movie_id": 1}
        assert db.session.query(Favorite).get(1) is not None


    def test_delete(self, client, header, movie, favorite):
        """
         The test_delete function implements a method of the TestFavoriteView class. Accepts as arguments
         the client, movie, and header objects created by the corresponding fixtures.
         Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        responce = client.delete('/favorites/movies/1', headers=header)
        assert responce.status_code == 200
        assert db.session.query(Favorite).get(1) is None


    def test_delete_none(self, client, header, movie):
        """
         The test_delete_none function implements a method of the TestFavoriteView class. Accepts as arguments
         the client, movie, and header objects created by the corresponding fixtures.
         Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        responce = client.delete('/favorites/movies/2', headers=header)
        assert responce.status_code == 404

    def test_favorite_not_authorization(self, client, movie):
        """
         The test_favorite_not_autorization function implements a method of the TestFavoriteView class.
         Accepts as arguments the client and movie objects created by the corresponding fixtures.
         Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.post("/favorites/movies/1")
        assert response.status_code == 401