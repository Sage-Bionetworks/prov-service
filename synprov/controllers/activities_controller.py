import connexion
import six

from synprov.models import ActivityForm  # noqa: E501
from synprov.models import Neo4jGraph  # noqa: E501
from synprov.models import Node  # noqa: E501
from synprov import util
from synprov.graph.controllers import activities_controller as controller


def create_activity(
    body
):  # noqa: E501
    """Create a new activity

    Create a new Activity. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Node
    """
    if connexion.request.is_json:
        body = ActivityForm.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.create_activity(
        body=body
    )


def create_activity_batch(
    body
):  # noqa: E501
    """Create multiple new activities

    Create multiple new Activities. # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: Node
    """
    if connexion.request.is_json:
        body = [ActivityForm.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return controller.create_activity_batch(
        body=body
    )


def delete_activity_used(
    id,
    reference_id
):  # noqa: E501
    """Delete &#39;used&#39; reference

    Remove a reference from the list of &#39;used&#39; entities in an Activity.  # noqa: E501

    :param id: activity ID
    :type id: str
    :param reference_id: entity ID
    :type reference_id: str

    :rtype: None
    """
    return controller.delete_activity_used(
        id=id,
        reference_id=reference_id
    )


def get_activities_graph(
    sort_by='created_at',
    order='desc',
    limit=3
):  # noqa: E501
    """Get provenance graph

    Retrieve all nodes and relationships in the graph that pass filters.  # noqa: E501

    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int

    :rtype: Neo4jGraph
    """
    return controller.get_activities_graph(
        sort_by=sort_by,
        order=order,
        limit=limit
    )


def get_agent_subgraph(
    id,
    sort_by='created_at',
    order='desc',
    limit=3
):  # noqa: E501
    """Get subgraph connected to an agent

    Retrieve the nodes and relationships in a neighborhood around a specified user.  # noqa: E501

    :param id: user ID
    :type id: str
    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int

    :rtype: Neo4jGraph
    """
    return controller.get_agent_subgraph(
        id=id,
        sort_by=sort_by,
        order=order,
        limit=limit
    )


def get_reference_subgraph(
    id,
    direction='down',
    sort_by='created_at',
    order='desc',
    limit=3
):  # noqa: E501
    """Get subgraph connected to an entity

    Retrieve the nodes and relationships in a neighborhood around a specified entity.  # noqa: E501

    :param id: entity ID
    :type id: str
    :param direction: direction in which to collect connected activities
    :type direction: str
    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int

    :rtype: Neo4jGraph
    """
    return controller.get_reference_subgraph(
        id=id,
        direction=direction,
        sort_by=sort_by,
        order=order,
        limit=limit
    )
