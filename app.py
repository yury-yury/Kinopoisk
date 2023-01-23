from app.app import create_app, configur_app
from app.config import DevelopmentConfig

if __name__ == '__main__':

    app_config = DevelopmentConfig()
    app = create_app(app_config)
    configur_app(app)
    app.run()
