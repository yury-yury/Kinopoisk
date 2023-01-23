from unittest.mock import MagicMock
import pytest

from app.dao.model.user import User
from app.dao.user import UserDAO
from app.services.user import UserService


@pytest.fixture()
def user_dao():
    """
    The utility function is designed to lock methods of the UserDAO class
    and prepare test data to check the functioning of methods of the UserService class.
    """
    user_dao = UserDAO(None)

    user_1 = User(id=2, name="oleg", email="oleg@oleg.ru", surname="user",
                  password="nePl4BfTTMW+TIHNef+bkLp5V8uGfsmtL7Zz1P5Ff5U=")
    user_2 = User(id=3, name="john", email="john@john.ru", surname="admin",
                  password="Cl63UZctBNY5nscyTHO9gQnAdN0mEyJ7toia6qSp454=")
    user_3 = User(id=4, name="alice", email="alice@alice.ru", surname="user",
                  password="rnS9BDglDZXPg1ZqfiAFL5bJOrmymOi7H5adjbNrnGU=")

    user_dao.get_by_email = MagicMock(return_value=user_3)
    user_dao.update = MagicMock(return_value=user_1)

    return user_dao


class TestUserService():
    """
    The TestUserService service class is designed to check the functioning of methods
    of the UserService class and contains unit tests of all methods of the class being tested.
    """
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        """
        The service function - fixture of the TestUserService class creates a test instance
        of the class to check the functioning of the methods of the UserService class.
        """
        self.user_service = UserService(dao=user_dao)

    def test_get_by_email(self):
        """
        The function contains unit tests to check the operability of the "get_by_username" method
        of the UserService class.
        """
        user = self.user_service.get_by_email("alice@alice.ru")

        assert user is not None
        assert user.id is not None
        assert user.name == "alice"

    def test_update(self):
        """
        The function contains unit tests to check the operability of the "update" method
        of the UserService class.
        """
        data = {"id": 2, "name": "oleg", "email": "oleg@oleg.ru", "password": "12345", "surname": "user"}
        user = self.user_service.update(data, "oleg@oleg.ru")

        assert user.id is not None
        assert user.name == "oleg"

    def test_change_password(self):
        """
        The function contains unit tests to check the operability of the "change_password" method
        of the UserService class.
        """
        result = self.user_service.change_password("Alice", "Alice", "alice@alice.ru")

        assert result is not None
        assert result != 400

    def test_generate_password(self):
        """
        The function contains unit tests to check the operability of the "generate_password" method
        of the UserService class.
        """
        password_hash = self.user_service.generate_password("12345")

        assert password_hash is not None
        assert password_hash == b"S0gaYvvHJTMF/4+tTKN4kplnAMudGqHpDif8Ed/5FN0="

    def test_compare_password(self):
        """
        The function contains unit tests to check the operability of the "compare_password" method
        of the UserService class.
        """
        res = self.user_service.compare_password("S0gaYvvHJTMF/4+tTKN4kplnAMudGqHpDif8Ed/5FN0=", "12345")

        assert res is not None
        assert res == True
