from app.app import create_app
from app.config import DevelopmentConfig, TestingConfig


class TestConfig:
    """
    The TestConfig class is designed to check the correctness of the configuration
    of an application instance depending on the environment. Contains the necessary unit tests.
    """
    def test_development(self):
        """
        The test_development function is a method of the TestConfig class and is designed to verify
        the correctness of configuring an application instance used during the development
        and debugging of program code.
        """
        app_config = create_app(DevelopmentConfig).config
        assert app_config["TESTING"] is False
        assert app_config["DEBUG"] is True
        assert app_config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///test.db"
        assert app_config["SQLALCHEMY_ECHO"] is True

    def test_testing(self):
        """
        The test_testing function is a method of the TestConfig class and is designed to verify
        the correctness of configuring an application instance used during the testing of program code.
        """
        app_config = create_app(TestingConfig).config
        assert app_config["TESTING"] is True
        assert app_config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"
