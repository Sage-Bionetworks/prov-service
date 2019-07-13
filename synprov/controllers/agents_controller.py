import connexion
import six

from synprov.models import D3Graph  # noqa: E501
from synprov import util
from synprov.graph.controllers import agents_controller as controller


def get_agent_subgraph(id, limit=None):  # noqa: E501
    """Get subgraph connected to an agent

    Retrieve the nodes and relationships in a neighborhood around a specified user.  # noqa: E501

    :param id: user ID
    :type id: str
    :param limit: maximum number of nodes to return
    :type limit: int

    :rtype: D3Graph
    """
    return controller.get_agent_subgraph(
        id=id, limit=limit
    )
