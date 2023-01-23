from app.dao.model.user import User


class UserDAO:
    """
    The UserDAO service class, which is Data Access Objects, is designed to perform
    all necessary operations with the database.
    """
    def __init__(self, session):
        """
        The function takes, as a parameter, a database access object during initialization.
        """
        self.session = session

    def get_one(self, uid: int):
        """
        The function defines the method of the class .get_one takes the row ID as a parameter
        and queries the "user" table entry of the database containing this parameter
        in the corresponding column and returns for further use.
        """
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        """
        The function defines the method of the class .get_by_username takes the username as a parameter
        and queries the "user" table entry of the database containing this parameter
        in the corresponding column and returns for further use.
        """
        return self.session.query(User).filter(User.email == email).first()

    def update(self, user: User):
        """
        The function defines the method of the class .update takes a database object as a parameter
        and writes and commits data to the "user" table of the database. Returns the accepted object.
        """
        self.session.add(user)
        self.session.commit()
        return user
