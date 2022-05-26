import pytest

from metro import create_app


@pytest.fixture()
def myapp():
    myapp = create_app()
    myapp.config.update(
        {
            "TESTING": True,
        }
    )

    yield myapp


@pytest.fixture()
def client(myapp):
    return myapp.test_client()
