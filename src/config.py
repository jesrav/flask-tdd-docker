import os


def convert_db_uri(uri):
    """Fix to Heruku using postgres://"""
    if uri.startswith("postgres://"):
        return uri.replace("postgres://", "postgresql://", 1)
    else:
        return uri


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_precious"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = convert_db_uri(os.environ.get("DATABASE_URL"))
