from app.container import user_dao
from app.dao.model.user import User
from app.database import db


class TestUserDAO:
    """
    The TestUserDAO class is designed to test all methods of the UserDAO class.
    """
    def test_get_one(self, user):
        """
        The function implements the test_get_one method of the TestUserDAO class.
        Takes as an argument the user object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        user_1 = user_dao.get_one(1)
        assert user_1 is not None
        assert user_1 == user

    def test_get_by_email(self, user):
        """
        The function implements the test_get_by_email method of the TestUserDAO class.
        Takes as an argument the user object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        user_1 = user_dao.get_by_email("oleg@oleg.ru")
        assert user_1 is not None
        assert user_1 == user

    def test_update(self, db):
        """
        The function implements the test_update method of the TestUserDAO class.
        Takes as an argument the db object prepared by the corresponding fixture.
        Checks the correctness of the returned values when calling the method.
        """
        user = User(id=1, name="oleg", email="oleg@oleg.ru", surname="user",
                password="S0gaYvvHJTMF/4+tTKN4kplnAMudGqHpDif8Ed/5FN0=")
        user_2 = user_dao.update(user)
        user_1 = db.session.query(User).first()
        assert user_1 is not None
        assert user == user_1
        assert user_1 == user_2

