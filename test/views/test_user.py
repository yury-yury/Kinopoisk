class TestUserView:
    """
    The TestUserView class is designed for functional testing of views implemented by methods
    of the UserView class.
    """
    def test_get(self, client, user, header):
        """
        The test_get function implements a method of the TestUserView class.
        Accepts client, user, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get('/users/', headers = header)
        assert response.status_code == 200
        assert response.json["name"] == user.name
        assert  response.json["favorit_genre_id"] == None

    def test_get_not_authorization(self, client, user):
        """
        The test_get_not_authorization function implements a method of the TestUserView class.
        Accepts client and user objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.get('/users/')
        assert response.status_code == 401

    def test_patch(self, client, user, header):
        """
        The test_patch function implements a method of the TestUserView class.
        Accepts client, user, and header objects created by the corresponding fixtures as arguments.
        Checks the operability of the corresponding representation and the correctness of the returned values.
        """
        response = client.patch('/users/', headers=header, json={"favorit_genre_id": 1})
        assert response.status_code == 200
        assert response.json["favorit_genre_id"] == 1
