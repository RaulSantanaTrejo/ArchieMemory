import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    pg_user = "postgres"
    pg_pwd = "postgres"
    pg_port = "5432"
    SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@localhost:{port}/archiememory_dev".format(username=pg_user, password=pg_pwd, port=pg_port)#is different in production

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
