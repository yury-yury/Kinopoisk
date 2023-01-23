from app.dao.director import DirectorDAO


class DirectorService:
    """
    The DirectorService service class is designed to link views and the database access object,
    and includes the necessary logic for working with received and transmitted data.
    """
    def __init__(self, dao: DirectorDAO):
        """
        The function takes, as a parameter, an object of the DirectorDAO class during initialization.
        """
        self.dao = dao

    def get_all(self):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all()

    def get_all_by_page(self, page: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_all_by_page(page)

    def get_one(self, did: int):
        """
        The function carries out the relationship between the representation and the object of receiving data.
        """
        return self.dao.get_one(did)
