from unittest.mock import MagicMock
import pytest

from app.dao.model.director import Director
from app.dao.director import DirectorDAO
from app.services.director import DirectorService


@pytest.fixture()
def director_dao():
    """
    The utility function is designed to lock methods of the DirectorDAO class
    and prepare test data to check the functioning of methods of the DirectorService class.
    """
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="Тейлор Шеридан")
    director_2 = Director(id=2, name="Квентин Тарантино")
    director_3 = Director(id=3, name="Владимир Вайншток")

    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.get_one = MagicMock(return_value=director_2)

    return director_dao


class TestDirectorService():
    """
    The TestDirectorService service class is designed to check the functioning of methods
    of the DirectorService class and contains unit tests of all methods of the class being tested.
    """
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        """
        The service function - fixture of the TestDirectorService class creates a test instance
        of the class to check the functioning of the methods of the DirectorService class.
        """
        self.director_service = DirectorService(dao=director_dao)

    def test_get_all(self):
        """
        The function contains unit tests to check the operability of the "get_all" method
        of the DirectorService class.
        """
        directors = self.director_service.get_all()

        assert type(directors) == list
        assert len(directors) > 0
        assert directors[0] is not None

    def test_get_one(self):
        """
        The function contains unit tests to check the operability of the "get_one" method
        of the DirectorService class.
        """
        director = self.director_service.get_one(2)

        assert director is not None
        assert director.id is not None
