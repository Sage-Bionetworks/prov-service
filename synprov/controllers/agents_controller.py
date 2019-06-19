import connexion
import six
import uuid
import humps

from py2neo import Graph, Node, NodeMatcher

from synprov.config import neomod
from synprov.graphmodels import Activity, Reference, Agent


graph = Graph(neomod.neo.db.url)


def get_agent(id):  # noqa: E501
    """Get an existing.

    Get an existing Agent # noqa: E501

    :param id: The ID of the agent to fetch.
    :type id: str

    :rtype: Agent
    """
    return 'do some magic!'


def list_agents():  # noqa: E501
    """.

    List Agents # noqa: E501


    :rtype: List[Agent]
    """
    return 'do some magic!'
