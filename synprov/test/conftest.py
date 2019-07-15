import logging

import pytest
import random

from py2neo import Graph

from synprov import create_app
from synprov.config import neo4j_connection as graph
from synprov.graph.client import GraphClient
from synprov.mock.main import create_mock_graph


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def client():
    logging.getLogger('connexion.operation').setLevel('ERROR')
    app = create_app()
    with app.app.test_client() as c:
        yield c


@pytest.fixture(scope='function')
def mock_graph():
    logger.info("setup: initializing graph database")
    yield graph

    logger.info("teardown: deleting graph database records")
    graph.delete_all()


@pytest.fixture(scope='function')
def mock_graph_data(mock_graph):
    logger.info("setup: populating graph database")
    graph = mock_graph
    random.seed(0)
    gc = GraphClient(graph)
    create_mock_graph(gc, 5)
    yield graph


@pytest.fixture(scope='function')
def mock_activity_form():
    used = [
        {
            'name': 'Reference_5',
            'target_id': 'TargetID_5',
            'target_version_id': '1.0',
            '_class': 'Resource',
            'subclass': 'File'
        }
        # {
        #     'name': 'Reference_5',
        #     'target_id': 'TargetID_5',
        #     'target_version_id': '1.0',
        #     '_class': 'Tool',
        #     'subclass': 'Tool'
        # }
    ]
    generated = [
        {
            'name': 'Reference_6',
            'target_id': 'TargetID_6',
            'target_version_id': '1.0',
            '_class': 'Resource',
            'subclass': 'State'
        }
    ]
    agents = [
        {
            'name': 'User_2',
            'user_id': 'UserID_2'
        }
    ]
    form = {
        'name': 'Activity_3',
        '_class': 'Tool session',
        'agents': agents,
        'description': '',
        'used': used,
        'generated': generated

    }
    yield form

