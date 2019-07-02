import connexion
import six
import uuid
import humps

from py2neo import Graph, Node, NodeMatcher

from synprov.config import neomod
from synprov.graphmodels import Activity, Reference, Agent


graph = Graph(neomod.neo.db.url)


def get_reference_subgraph(id):  # noqa: E501
    """Get subgraph connected to an entity.

    Retrieve the nodes and relationships in a neighborhood around a specified entity. # noqa: E501

    :param id: The ID of the entity to fetch.
    :type id: str

    :rtype: Graph
    """
    return 'Not Implemented', 501
