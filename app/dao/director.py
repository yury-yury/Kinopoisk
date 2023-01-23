from app.dao.model.director import Director


class DirectorDAO:
    """
    The DirectorDAO service class, which is Data Access Objects, is designed to perform
    all necessary operations with the database.
    """
    def __init__(self, session):
        """
        The function takes, as a parameter, a database access object during initialization.
        """
        self.session = session

    def get_all(self):
        """
        The function defines the method of the class .get_all and queries all records
        of the "director" table of the database and returns it for further use.
        """
        return self.session.query(Director).all()

    def get_all_by_page(self, page: int):
        """
        The function defines the method of the class .get_all and queries all records
        of the "director" table of the database and performs its page-by-page return for further use.
        """
        return self.session.query(Director).limit(12).offset((page - 1) * 12).all()

    def get_one(self, did: int):
        """
        The function defines the method of the class .get_one takes the row ID as a parameter
        and queries the "director" table entry of the database containing this parameter
        in the corresponding column and returns for further use.
        """
        return self.session.query(Director).get(did)
