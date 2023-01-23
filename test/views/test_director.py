import pytest

from app.dao.model.director import Director


class TestDirectorView:
    """
    The TestDirectorView class is designed for functional testing of views implemented by methods
    of the DirectorView class.
    """
    def test_many(self, client, director, header):
        """
        The test_many function implements a method of the TestDirectorView class. Accepts client,
        director, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/directors/", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert response.json == [{"id": director.id, "name": director.name}]

    def test_genre_pages(self, client, director, header):
        """
        The test_genre_page function implements a method of the TestDirectorView class. Accepts client,
        director, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/directors/?page=1", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 1
        assert response.json == [{"id": director.id, "name": director.name}]

        response = client.get("/directors/?page=2", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 0

    def test_director_get_one(self, client, director, header):
        """
        The test_director_get_one function implements a method of the TestDirectorView class. Accepts client,
        director, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/directors/1", headers=header)
        assert response.status_code == 200
        assert response.json == {"id": director.id, "name": director.name}

    def test_director_not_found(self, client, director, header):
        """
        The test_director_not_found function implements a method of the TestDirectorView class. Accepts client,
        director, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/director/2", headers=header)
        assert response.status_code == 404

    def test_director_not_authorization(self, client):
        """
        The test_director_not_authorization function implements a method of the TestDirectorView class. Accepts client,
        objects created by the corresponding fixture as argument.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/directors/")
        assert response.status_code == 401
