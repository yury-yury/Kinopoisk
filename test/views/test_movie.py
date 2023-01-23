import pytest

from app.dao.model.movie import Movie


class TestMovieView:
    """
    The TestMovieView class is designed for functional testing of views implemented by methods
    of the MovieView class.
    """
    def test_many(self, client, movie, header):
        """
        The test_many function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}]

    def test_many_pages(self, client, movie, header):
        """
        The test_many_page function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/?page=1", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 1
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}]

        response = client.get("/movies/?page=2", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 0

    def test_many_by_director_and_genre(self, client, movie, header):
        """
        The test_many_by_director_and_genre function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/?director_id=1&genre_id=1", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}]

    def test_many_by_director(self, client, movie, header):
        """
        The test_many_by_director function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/?director_id=1", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}]

    def test_many_by_genre(self, client, movie, header):
        """
        The test_many_by_genre function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/?genre_id=1", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}]

    def test_many_new(self, client, movie, header):
        """
        The test_many_new function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/?status=new", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}]

    def test_many_pages_new(self, client, movie, header):
        """
        The test_many_page_new function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/?page=1&status=new", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 1
        assert response.json == [{"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}]

        response = client.get("/movies/?page=2&status=new", headers=header)
        assert response.status_code == 200
        assert type(response.json) == list
        assert len(response.json) == 0

    def test_get_one(self, client, movie, header):
        """
        The test_get_one function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/1", headers=header)
        assert response.status_code == 200
        assert response.json == {"id": movie.id, "title": movie.title, "description": movie.description,
                                  "trailer": movie.trailer, "year": movie.year, "rating": movie.rating,
                                  "genre_id": movie.genre_id, "director_id": movie.director_id}

    def test_get_one_not_found(self, client, movie, header):
        """
        The test_get_one_not_found function implements a method of the TestMovieView class.
        Accepts client, movie, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/2", headers=header)
        assert response.status_code == 404


    def test_movie_not_authorization(self, client, movie):
        """
        The test_movie_not_authorization function implements a method of the TestMovieView class.
        Accepts client and movie objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get("/movies/")
        assert response.status_code == 401
