from app.container import movie_dao


class TestMovieDAO:
    """
    The TestMovieDAO class is designed to test all methods of the MovieDAO class.
    """
    def test_get_all_by_director_and_genre(self, movie):
        """
        The function implements the test_get_all_by_director_and_genre method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_all_by_director_and_genre(1, 1)
        assert res is not None
        assert type(res) == list
        assert res == [movie]

        res = movie_dao.get_all_by_director_and_genre(2, 2)
        assert res is not None
        assert type(res) == list
        assert res == []

    def test_get_all_by_director(self, movie):
        """
        The function implements the test_get_all_by_director method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_all_by_director(1)
        assert res is not None
        assert type(res) == list
        assert res == [movie]

        res = movie_dao.get_all_by_director(2)
        assert res is not None
        assert type(res) == list
        assert res == []

    def test_get_all_by_genre(self, movie):
        """
        The function implements the test_get_all_by_genre method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_all_by_genre(1)
        assert res is not None
        assert type(res) == list
        assert res == [movie]

        res = movie_dao.get_all_by_genre(2)
        assert res is not None
        assert type(res) == list
        assert res == []

    def test_get_all_by_page(self, movie):
        """
        The function implements the test_get_all_by_page method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_all_by_page(1)
        assert res is not None
        assert type(res) == list
        assert res == [movie]

        res = movie_dao.get_all_by_page(2)
        assert res is not None
        assert type(res) == list
        assert res == []

    def test_get_all_by_page_new(self, movie):
        """
        The function implements the test_get_all_by_page_new method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_all_by_page_new(1)
        assert res is not None
        assert type(res) == list
        assert res == [movie]

        res = movie_dao.get_all_by_page_new(2)
        assert res is not None
        assert type(res) == list
        assert res == []

    def test_get_all(self, movie):
        """
        The function implements the test_get_all method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_all()
        assert res is not None
        assert type(res) == list
        assert res == [movie]

    def test_get_all_new(self, movie):
        """
        The function implements the test_get_all_new method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_all_new()
        assert res is not None
        assert type(res) == list
        assert res == [movie]

    def test_get_one(self, movie):
        """
        The function implements the test_get_one method of the TestUserDAO class.
        Takes as an argument the movie object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = movie_dao.get_one(1)
        assert res is not None
        assert res == movie

        res = movie_dao.get_one(2)
        assert res is None
        assert res == None
