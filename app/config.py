class Config:
    """
    The class is used to configure application objects.
    Contains all the necessary variables to configure instances.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_SILENCE_UBER_WARNING = 1
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False}


class TestingConfig(Config):
    """
    The class is used to configure application objects for testing.
    Inherited from the main configuration class.
    Contains all the necessary variables to configure instances during unit testing.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    """
    The class is used to configure application objects for development.
    Inherited from the main configuration class.
    Contains all the necessary variables to configure instances during development.
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


class ProductionConfig(Config):
    """
    The class is used to configure application objects for production server.
    Inherited from the main configuration class.
    Contains all the necessary variables to configure instances during work in producyion server.
    """
    DEBUG = False



