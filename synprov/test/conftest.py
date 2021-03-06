import logging

import pytest
import random

from py2neo import Graph

from synprov import create_app
from synprov.config import neo4j_connection as graph
from synprov.graph.client import GraphClient
from synprov.mock.main import create_mock_graph


logging.basicConfig(level=logging.DEBUG)
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
    random.seed(1)
    gc = GraphClient(graph)
    create_mock_graph(gc, 5)
    yield graph


@pytest.fixture(scope='function')
def mock_activity_id(mock_graph_data):
    activity_node = graph.nodes.match('Activity').first()
    yield activity_node['id']


@pytest.fixture(scope='function')
def mock_activity_form():
    used = [
        {
            'name': 'Reference_3',
            'target_id': 'TargetID_3',
            'target_version_id': '1.0',
            '_class': 'Resource',
            'subclass': 'File'
        },
        {
            'name': 'Reference_4',
            'target_id': 'TargetID_4',
            'target_version_id': '1.0',
            '_class': 'Tool',
            'subclass': 'Tool'
        }
    ]
    generated = [
        {
            'name': 'Reference_5',
            'target_id': 'TargetID_5',
            'target_version_id': '1.0',
            '_class': 'Resource',
            'subclass': 'State'
        }
    ]
    agents = [
        {
            'name': 'User_1',
            'user_id': 'UserID_1'
        }
    ]
    form = {
        'name': 'Activity_2',
        '_class': 'Tool session',
        'agents': agents,
        'description': '',
        'used': used,
        'generated': generated

    }
    yield form

@pytest.fixture(scope='function')
def mock_activity_request():
    used = [
        {
            'name': 'Reference_3',
            'targetId': 'TargetID_3',
            'targetVersionId': '1.0',
            'class': 'Resource',
            'subclass': 'File'
        },
        {
            'name': 'Reference_4',
            'target_id': 'TargetID_4',
            'target_version_id': '1.0',
            '_class': 'Tool',
            'subclass': 'Tool'
        }
    ]
    generated = [
        {
            'name': 'Reference_5',
            'targetId': 'TargetID_5',
            'targetVersionId': '1.0',
            'class': 'Resource',
            'subclass': 'State'
        }
    ]
    agents = [
        {
            'name': 'User_1',
            'userId': 'UserID_1'
        }
    ]
    form = {
        'name': 'Activity_3',
        'class': 'Tool session',
        'agents': agents,
        'description': '',
        'used': used,
        'generated': generated

    }
    yield form
