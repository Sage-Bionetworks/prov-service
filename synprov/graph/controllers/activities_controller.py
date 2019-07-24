import connexion
import six
import uuid
import humps
import json

from py2neo import Node, NodeMatcher

from synprov.config import neo4j_connection as graph
from synprov.graph import ActivityBuilder
from synprov.util import neo4j_to_d3


def create_activity(body=None):  # noqa: E501
    """Create a new.

    Create a new Activity. If the passed Activity object contains a Used array, you must set the concreteType field of each Used subclass. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: Activity
    """
    builder = ActivityBuilder(
        **body.to_dict()
    )
    act_node = builder.save()
    print(act_node)
    return humps.camelize({
        'id': str(act_node.identity),
        'labels': list(act_node.labels),
        'properties': dict(act_node)
    })


def get_activities_graph(sort_by=None, order=None, limit=None):  # noqa: E501
    """Get provenance graph

    Retrieve all nodes and relationships in the graph that pass filters.  # noqa: E501

    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int

    :rtype: D3Graph
    """
    query_base = (
        '''
        MATCH (s:Activity)
        WITH s
        ORDER BY s.{key}{dir}
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source, r as relationship, t as target
        '''
    ).format(
        key=sort_by,
        dir=(' ' + order.upper()) if order == 'desc' else '',
        lim=limit
    )

    results = graph.run(
        query_base,
    )
    return humps.camelize(neo4j_to_d3(results.data()))


def get_agent_subgraph(id, sort_by=None, order=None, limit=None):  # noqa: E501
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

    :rtype: D3Graph
    """
    query_base = (
        '''
        MATCH (t:Agent {{user_id: {{id}}}})<-[r:WASASSOCIATEDWITH]-(s:Activity)
        WITH s
        ORDER BY s.{key}{dir}
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source, r as relationship, t as target
        '''
    ).format(
        key=sort_by,
        dir=(' ' + order.upper()) if order == 'desc' else '',
        lim=limit
    )

    results = graph.run(
        query_base,
        id=id
    )
    return humps.camelize(neo4j_to_d3(results.data()))


def get_reference_subgraph(id,
                           direction='down',
                           sort_by='created_at',
                           order='desc',
                           limit=3):  # noqa: E501
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

    :rtype: D3Graph
    """
    direction_rels = {
        'up': '-[r:WASGENERATEDBY]->',
        'down': '<-[r:USED]-'
    }
    query_base = (
        '''
        MATCH (t:Reference {{target_id: {{id}}}}){dir_rel}(s:Activity)
        WITH s
        ORDER BY s.{key}{dir}
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source, r as relationship, t as target
        '''
    ).format(
        dir_rel=direction_rels[direction],
        key=sort_by,
        dir=(' ' + order.upper()) if order == 'desc' else '',
        lim=limit
    )

    results = graph.run(
        query_base,
        id=id
    )
    return humps.camelize(neo4j_to_d3(results.data()))