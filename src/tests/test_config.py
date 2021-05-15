import os
from src.config import convert_db_uri


def test_convert_db_uri():
    uri = "postgres://postgres:postgres@api-db:5432/api_test"
    converted_uri = convert_db_uri(uri)
    assert converted_uri == "postgresql://postgres:postgres@api-db:5432/api_test"


def test_development_config(test_app):
    test_app.config.from_object("src.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")


def test_testing_config(test_app):
    test_app.config.from_object("src.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert test_app.config["TESTING"]
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )


def test_production_config(test_app):
    test_app.config.from_object("src.config.ProductionConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
