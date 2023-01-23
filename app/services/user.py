import base64
import hashlib
import hmac

from flask import abort

from app.constants import PWD_SALT, PWD_ITERATIONS
from app.dao.user import UserDAO
from app.dao.model.user import User


class UserService:
    """
    The UserService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: UserDAO):
        """
        The function takes, as a parameter, an object of the UserDAO class during initialization.
        """
        self.dao = dao

    def get_by_email(self, email: str):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_by_email(email)

    def create(self, data: dict):
        """
        The function defines the method of the class .create takes data for creating a database object
        as a parameter, creates it and passes it for saving. Returns the created entity.
        """
        data["password"] = self.generate_password(data.get("password"))
        user = User(**data)
        return self.dao.update(user)

    def update(self, data: dict, email: str):
        """
        The function defines the method of the class .update accepts data for updating a database object
        as a parameter updates it and passes it for saving. Returns the updated entity
        """
        user = self.get_by_email(email)
        if "name" in data.keys():
            user.name = data.get("name")
        if "surname" in data.keys():
            user.surname = data.get("surname")
        if "password" in data.keys():
            user.password = self.generate_password(data.get("password"))
        if "favorit_genre_id" in data.keys():
            user.favorit_genre_id = data.get("favorit_genre_id")
        if "email" in data.keys():
            user.email = data.get("email")

        return self.dao.update(user)

    def change_password(self, password_1: str, password_2: str, email: str):
        """

        """
        user = self.get_by_email(email)
        if self.compare_password(user.password, password_1):
            user.password = self.generate_password(password_2)
            return self.dao.update(user)
        abort(400)

    def generate_password(self, password):
        """
        The function takes the user's password as an argument in the form of a string and is designed
        to hash the password in order to protect the stored information. Returns the password hash.
        """
        hash_digest = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), PWD_SALT, PWD_ITERATIONS)
        return base64.b64encode(hash_digest)

    def compare_password(self, password_hash, other_password):
        """
        The function takes as arguments the hash of the user's password stored in the database
        and the entered password in the form of a string and is designed to verify the entered data.
        Returns True if the correct data is entered, otherwise False.
        """
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac('sha256', other_password.encode('utf-8'), PWD_SALT, PWD_ITERATIONS)
        return hmac.compare_digest(decoded_digest, hash_digest)
