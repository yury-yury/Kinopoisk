from app.dao.model.favorite import Favorite
from app.dao.model.user import User


class FavoriteDAO:
    """
    The FavoriteDAO service class, which is Data Access Objects, is designed to perform
    all necessary operations with the database.
    """
    def __init__(self, session):
        """
        The function takes, as a parameter, a database access object during initialization.
        """
        self.session = session

    def create(self, favorite: Favorite):
        """
        The function represents the create method of the FavoriteDAO class and adds the object received
        as an argument to the database and saves it. Returns the received object.
        """
        self.session.add(favorite)
        self.session.commit()
        return favorite

    def delete(self, favorite: Favorite):
        """
        The function represents the delete method of the FavoriteDAO class and deletes the object received
        as an argument from the database and saves it.
        """
        self.session.delete(favorite)
        self.session.commit()

    def get_user_by_email(self, email):
        """
        The function represents the get_user_by_email method of the FavoriteDAO class and fetches
        an object from the 'user' table of the database, based on the email value received as an argument.
        """
        return self.session.query(User).filter(User.email == email).first()

    def get_favorite(self, user_id, movie_id):
        """
        The function represents the get_favorite method of the Favoriteday class and selects an object from
        the 'favorite' table of the database, based on the user_id and movie_id values received as arguments.
        """
        return self.session.query(Favorite).filter(Favorite.user_id == user_id, Favorite.movie_id == movie_id).first()