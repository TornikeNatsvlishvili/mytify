import os


class Config(object):
    SECRET_KEY = os.environ.get('MYTIFY_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True

    JWT_SECRET_KEY = 'CHANE ME'
    MONGO_DBNAME = 'mytify'
    DOWNLOAD_PATH = Config.APP_DIR + '/download'


class TestConfig(Config):
    TESTING = True
    DEBUG = True