import pytest

from app.app import create_app, configur_app
from app.config import TestingConfig
from app.container import auth_service
from app.dao.model.director import Director
from app.dao.model.favorite import Favorite
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
from app.dao.model.user import User
from app.database import db as database


@pytest.fixture()
def app():
    """
    The app fixture is used to create and configure an instance of an application
    for testing using functional and unit tests. Returns the created test instance of the application.
    """
    config_test = TestingConfig()
    app = create_app(config_test)
    configur_app(app)
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    """
    The db fixture is used to initialize and configure the database access object for testing
    using functional and unit tests. Takes a test instance of the application as an argument.
    Returns the initialized test object.
    """
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()
    yield database
    database.session.close()


@pytest.fixture
def client(app, db):
    """
    The client fixture is used to create a test client object for testing using functional
    and unit tests. Accepts as arguments a test instance of the application and a database access object.
    Returns the created test client.
    """
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture()
def user(db):
    """
    The user fixture is used to create a test database object for testing using functional and unit tests.
    Accepts a database access object as an argument. Returns the created object.
    """
    user = User(id=1, name="oleg", email="oleg@oleg.ru", surname="user",
                password="S0gaYvvHJTMF/4+tTKN4kplnAMudGqHpDif8Ed/5FN0=")
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture()
def movie(db):
    """
    The movie fixture is used to create a test database object for testing using functional and unit tests.
    Accepts a database access object as an argument. Returns the created object.
    """
    obj = Movie(id=1, title="Test_1", description="description_1", trailer="trailer_1",
                year=2018, rating=8.6,	genre_id=1, director_id=1)
    db.session.add(obj)
    db.session.commit()
    return obj


@pytest.fixture()
def genre(db):
    """
    The genre fixture is used to create a test database object for testing using functional and unit tests.
    Accepts a database access object as an argument. Returns the created object.
    """
    obj = Genre(id=1, name="genre")
    db.session.add(obj)
    db.session.commit()
    return obj


@pytest.fixture()
def director(db):
    """
    The director fixture is used to create a test database object for testing using functional and unit tests.
    Accepts a database access object as an argument. Returns the created object.
    """
    obj = Director(id=1, name="director test")
    db.session.add(obj)
    db.session.commit()
    return obj


@pytest.fixture()
def favorite(db):
    """
    The favorite fixture is used to create a test database object for testing using functional and unit tests.
    Accepts a database access object as an argument. Returns the created object.
    """
    favorite = Favorite(id=1, user_id=1, movie_id=1)
    db.session.add(favorite)
    db.session.commit()
    return favorite


@pytest.fixture()
def header(user):
    """
    The header fixture is used to create a request header during authorization for testing using functional
    and unit tests of endpoints closed from unauthorized access. Takes the user object
    of the test user as an argument. Returns the created object.
    """
    token = auth_service.generate_tokens(user.email, "12345")
    return {'Authorization': "Bearer " + token['access_token']}