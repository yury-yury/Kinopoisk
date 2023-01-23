from app.dao.model.user import User
from app.database import db


class TestAuthView:
    """
    The TestAuthView class is designed for functional testing of views implemented by methods of the AuthView class.
    """
    def test_create_user(self, client):
        """
        The test_create_user function implements a method of the TestAuthView class. Takes as an argument
        the client object created by the corresponding fixture. Checks the operability of the corresponding
        representation and the correctness of the returned values.
        """
        data = {"email": "oleg@oleg.ru", "password": "12345"}
        responce = client.post('/auth/register', json=data)
        assert responce.status_code == 200
        assert db.session.query(User).first() is not None

    def test_login(self, client, user):
        """
        The test_login function implements a method of the TestAuthView class. Takes as an argument
        the client and user objects created by the corresponding fixtures. Checks the operability
        of the corresponding representation and the correctness of the returned values.
        """
        data = {"email": "oleg@oleg.ru", "password": "12345"}
        responce = client.post('/auth/login', json=data)
        assert responce.status_code == 201
        assert type(responce.json) == dict
        assert "access_token" in responce.json.keys()
        assert "reresh_token" in responce.json.keys()

        data = {"email": "oleg@oleg.ru", "password": "1234"}
        responce = client.post('/auth/login', json=data)
        assert responce.status_code == 400
