from app.container import genre_dao


class TestGenreDAO:
    """
    The TestGenreDAO class is designed to test all methods of the GenreDAO class.
    """
    def test_get_all(self, genre):
        """
        The function implements the test_get_all method of the TestGenreDAO class.
        Takes as an argument the genre object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = genre_dao.get_all()
        assert res is not None
        assert type(res) == list
        assert res == [genre]

    def test_get_all_by_page(self, genre):
        """
        The function implements the test_get_all_by_page method of the TestGenreDAO class.
        Takes as an argument the genre object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = genre_dao.get_all_by_page(1)
        assert res is not None
        assert type(res) == list
        assert res == [genre]

        res = genre_dao.get_all_by_page(2)
        assert res is not None
        assert type(res) == list
        assert res == []

    def test_get_one(self, genre):
        """
        The function implements the test_get_one method of the TestGenreDAO class.
        Takes as an argument the genre object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = genre_dao.get_one(1)
        assert res is not None
        assert res == genre

        res = genre_dao.get_one(2)
        assert res is None

    def test_get_list_movie_by_genre(self, movie):
        """
        The function implements the test_get_list_movie_by_genre method of the TestGenreDAO class.
        Takes as an argument the genre object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = genre_dao.get_list_movie_by_genre(1)
        assert res is not None
        assert type(res) == list
        assert res == [movie]
