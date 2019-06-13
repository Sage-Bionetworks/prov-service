import logging

import pytest

from synprov import create_app

@pytest.fixture(scope='module')
def client():
    logging.getLogger('connexion.operation').setLevel('ERROR')
    app = create_app()
    with app.app.test_client() as c:
        yield c
