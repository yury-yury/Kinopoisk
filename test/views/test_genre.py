import pytest

from app.dao.model.genre import Genre


class TestGenresView:
    """
    The TestGenresView class is designed for functional testing of views implemented by methods
    of the GenreView class.
    """
    def test_many(self, client, genre, header):
        """
        The test_many function implements a method of the TestGenreView class. Accepts client, genre,
        and header objects created by the corresponding fixtures as arguments. Checks the operability
        of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/genres/", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert response.json == [{"id": genre.id, "name": genre.name}]

    def test_genre_pages(self, client, genre, header):
        """
        The test_genre_page function implements a method of the TestGenreView class. Accepts client, genre,
        and header objects created by the corresponding fixtures as arguments. Checks the operability
        of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/genres/?page=1", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 1
        assert response.json == [{"id": genre.id, "name": genre.name}]

        response = client.get("/genres/?page=2", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 0

    def test_genre(self, client, genre, header):
        """
        The test_genre function implements a method of the TestGenreView class. Accepts client, genre,
        and header objects created by the corresponding fixtures as arguments. Checks the operability
        of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/genres/1", headers=header)
        assert response.status_code == 200
        assert response.json == {"id": genre.id, "name": genre.name, "movies": []}

    def test_genre_not_found(self, client, genre, header):
        """
        The test_genre_not_found function implements a method of the TestGenreView class. Accepts client, genre,
        and header objects created by the corresponding fixtures as arguments. Checks the operability
        of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/genres/2", headers=header)
        assert response.status_code == 404

    def test_genre_not_authorization(self, client, genre):
        """
        The test_genre_not_autorization function implements a method of the TestGenreView class. Accepts client, genre
        objects created by the corresponding fixtures as arguments. Checks the operability
        of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/genres/")
        assert response.status_code == 401
