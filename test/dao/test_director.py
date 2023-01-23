from app.container import director_dao


class TestDirectorDAO:
    """
    The TestDirectorDAO class is designed to test all methods of the DirectorDAO class.
    """
    def test_get_all(self, director):
        """
        The function implements the test_get_all method of the TestDirectorDAO class.
        Takes as an argument the director object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = director_dao.get_all()
        assert res is not None
        assert type(res) == list
        assert res == [director]

    def test_get_all_by_page(self, director):
        """
        The function implements the test_get_all_by_page method of the TestDirectorDAO class.
        Takes as an argument the director object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = director_dao.get_all_by_page(1)
        assert res is not None
        assert type(res) == list
        assert res == [director]

        res = director_dao.get_all_by_page(2)
        assert res is not None
        assert type(res) == list
        assert res == []

    def test_get_one(self, director):
        """
        The function implements the test_get_one method of the TestDirectorDAO class.
        Takes as an argument the director object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        res = director_dao.get_one(1)
        assert res is not None
        assert res == director

        res = director_dao.get_one(2)
        assert res is None
