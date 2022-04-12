import pytest
from os import environ
from flask_migrate import upgrade
from api.app import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.app_context():
        yield app.test_client()
