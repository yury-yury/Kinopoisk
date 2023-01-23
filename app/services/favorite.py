from flask_restx import abort

from app.dao.favorite import FavoriteDAO
from app.dao.model.favorite import Favorite


class FavoriteService:
    """
    The FavoriteService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: FavoriteDAO):
        """
        The function takes, as a parameter, an object of the FavoriteDAO class during initialization.
        """
        self.dao = dao

    def create(self, mid: int, email: str):
        """
        The function implements the "create" method of the "FavoriteService" class, accepts the parameters
        of the movie ID and the user's Email. Creates a database object and passes it for saving.
        eturns the created object.
        """
        user = self.dao.get_user_by_email(email)
        favorite = Favorite(user_id=user.id, movie_id=mid)
        return self.dao.create(favorite)

    def delete(self,mid: int, email: str):
        """
        The function implements the "delete" method of the "FavoriteService" class, accepts the parameters
        of the movie ID and the user's Email. Makes a request to the DAO to search for a database object
        and passes it for deletion.
        """
        user = self.dao.get_user_by_email(email)
        favorite = self.dao.get_favorite(user.id, mid)
        if favorite is None:
            abort(404)
        self.dao.delete(favorite)