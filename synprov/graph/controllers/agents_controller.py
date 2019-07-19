import connexion
import six
import uuid
import humps

from py2neo import Node, NodeMatcher

from synprov.config import neo4j_connection as graph
from synprov.graph import GraphActivity, GraphReference, GraphAgent


def get_agent_subgraph(id, limit=None):  # noqa: E501
    """Get subgraph connected to an agent.

    Retrieve all nodes and relationships in the graph that pass filters. # noqa: E501

    :param id: The ID of the agent to fetch.
    :type id: str

    :rtype: Graph
    """
    return 'Not Implemented', 501
