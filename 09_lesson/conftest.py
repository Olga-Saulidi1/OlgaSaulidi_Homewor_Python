import pytest
from db_config import engine


@pytest.fixture(scope="session")
def db_engine():
    return engine


@pytest.fixture
def db_connection(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()
