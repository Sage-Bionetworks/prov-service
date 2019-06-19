import connexion
import six
import uuid
import humps

from py2neo import Graph, Node, NodeMatcher

from synprov.config import neomod
from synprov.graphmodels import Activity, Reference, Agent


graph = Graph(neomod.neo.db.url)


def get_reference(id):  # noqa: E501
    """Get an existing.

    Get an existing Reference # noqa: E501

    :param id: The ID of the entity to fetch.
    :type id: str

    :rtype: Reference
    """
    return 'do some magic!'


def list_references():  # noqa: E501
    """.

    List References # noqa: E501


    :rtype: List[Reference]
    """
    return 'do some magic!'
