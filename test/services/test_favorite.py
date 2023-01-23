from unittest.mock import MagicMock

import pytest

from app.dao.favorite import FavoriteDAO
from app.dao.model.favorite import Favorite
from app.dao.model.user import User
from app.services.favorite import FavoriteService


@pytest.fixture()
def favorite_dao():
    """
    The utility function is designed to lock methods of the FavoriteDAO class
    and prepare test data to check the functioning of methods of the FavoriteService class.
    """
    favorite_dao = FavoriteDAO(None)

    favorite_1 = Favorite(id=1, user_id=1, movie_id=1)
    favorite_2 = Favorite(id=2, user_id=2, movie_id=2)
    user_1 = User(id=1, name="john", email="john@john.ru", surname="admin",
                  password="Cl63UZctBNY5nscyTHO9gQnAdN0mEyJ7toia6qSp454=")


    favorite_dao.create = MagicMock(return_value=favorite_1)
    favorite_dao.delete = MagicMock(return_value="")
    favorite_dao.get_favorite = MagicMock(return_value=favorite_1)
    favorite_dao.get_user_by_email = MagicMock(return_value=user_1)

    return favorite_dao


class TestFavoriteService():
    """
    The TestFavoriteService service class is designed to check the functioning of methods
    of the FavoriteService class and contains unit tests of all methods of the class being tested.
    """
    @pytest.fixture(autouse=True)
    def favorite_service(self, favorite_dao):
        """
        The service function - fixture of the TestFavoriteService class creates a test instance
        of the class to check the functioning of the methods of the FavoriteService class.
        """
        self.favorite_service = FavoriteService(dao=favorite_dao)

    def test_create(self):
        """
        The function contains unit tests to check the operability of the "create" method
        of the FavoriteService class.
        """
        favorite = self.favorite_service.create(1, "john@john.ru")

        assert favorite is not None
        assert favorite.id is not None

    def test_delete(self):
        """
        The function contains unit tests to check the operability of the "delete" method
        of the FavoriteService class.
        """
        favorite = self.favorite_service.delete(1, "john@john.ru")

        assert favorite is None

