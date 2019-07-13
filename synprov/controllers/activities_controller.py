import connexion
import six

from synprov.models import Activity  # noqa: E501
from synprov.models import ActivityForm  # noqa: E501
from synprov.models import D3Graph  # noqa: E501
from synprov import util
from synprov.graph.controllers import activities_controller as controller


def create_activity(body):  # noqa: E501
    """Create a new activity

    Create a new Activity. If the passed Activity object contains a Used array, you must set the concreteType field of each Used subclass. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: Activity
    """
    if connexion.request.is_json:
        body = ActivityForm.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.create_activity(
        body=body
    )


def get_activities_graph(limit=None):  # noqa: E501
    """Get provenance graph

    Retrieve all nodes and relationships in the graph that pass filters.  # noqa: E501

    :param limit: maximum number of nodes to return
    :type limit: int

    :rtype: D3Graph
    """
    return controller.get_activities_graph(
        limit=limit
    )
