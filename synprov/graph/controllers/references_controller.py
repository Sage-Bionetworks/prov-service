import connexion
import six
import uuid
import humps

from py2neo import Node, NodeMatcher

from synprov.config import neo4j_connection as graph
from synprov.graph import GraphActivity, GraphReference, GraphAgent


def get_reference_subgraph(id):  # noqa: E501
    """Get subgraph connected to an entity.

    Retrieve the nodes and relationships in a neighborhood around a specified entity. # noqa: E501

    :param id: The ID of the entity to fetch.
    :type id: str

    :rtype: Graph
    """
    return 'Not Implemented', 501
