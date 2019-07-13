import connexion
import six

from synprov.models import D3Graph  # noqa: E501
from synprov import util
from synprov.graph.controllers import references_controller as controller


def get_reference_subgraph(id, limit=None, direction=None):  # noqa: E501
    """Get subgraph connected to an entity

    Retrieve the nodes and relationships in a neighborhood around a specified entity.  # noqa: E501

    :param id: entity ID
    :type id: str
    :param limit: maximum number of nodes to return
    :type limit: int
    :param direction: direction in which to collect nodes
    :type direction: str

    :rtype: D3Graph
    """
    return controller.get_reference_subgraph(
        id=id, limit=limit, direction=direction
    )
