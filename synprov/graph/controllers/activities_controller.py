import connexion
import six
import uuid
import humps
import json

from py2neo import Node, NodeMatcher

from synprov.config import neo4j_connection as graph
from synprov.graph import GraphActivity, GraphReference, GraphAgent
from synprov.util import neo4j_to_d3


def create_activity(body=None):  # noqa: E501
    """Create a new.

    Create a new Activity. If the passed Activity object contains a Used array, you must set the concreteType field of each Used subclass. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: Activity
    """
    # act = Activity(**humps.decamelize(body))
    # act.save()

    # return act.node
    return 'Not Implemented', 501


def get_activities_graph(limit=20):  # noqa: E501
    """Get provenance graph

    Retrieve all nodes and relationships in the graph that pass filters.  # noqa: E501

    :param limit: maximum number of nodes to return
    :type limit: int

    :rtype: D3Graph
    """
    # TODO: with the current query, the 'limit' parameter applies
    # to relationships, not really to nodes
    results = graph.run(
        '''
        MATCH (s)-[r]-(t)
        RETURN s as source, r as relationship, t as target
        LIMIT {limit}
        ''',
        limit=limit
    )
    return neo4j_to_d3(results.data())


def get_agent_subgraph(id, limit=3):  # noqa: E501
    """Get subgraph connected to an agent.

    Retrieve all nodes and relationships in the graph that pass filters. # noqa: E501

    :param id: The ID of the agent to fetch.
    :type id: str

    :rtype: Graph
    """
    query_base = (
        '''
        MATCH (t:Agent {{user_id: {{id}}}})<-[r:WASASSOCIATEDWITH]-(s:Activity)
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source,r as relationship,t as target
        '''
    ).format(
        lim=limit
    )

    results = graph.run(
        query_base,
        id=id
    )
    return neo4j_to_d3(results.data())


def get_reference_subgraph(id, limit=3, direction='down'):  # noqa: E501
    """Get subgraph connected to an entity.

    Retrieve the nodes and relationships in a neighborhood around a specified entity. # noqa: E501

    :param id: The ID of the entity to fetch.
    :type id: str

    :rtype: Graph
    """
    direction_rels = {
        'up': '-[r:WASGENERATEDBY]->',
        'down': '<-[r:USED]-'
    }
    query_base = (
        '''
        MATCH (t:Reference {{target_id: {{id}}}}){dir_rel}(s:Activity)
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source,r as relationship,t as target
        '''
    ).format(
        lim=limit,
        dir_rel=direction_rels[direction]
    )

    results = graph.run(
        query_base,
        id=id
    )
    return neo4j_to_d3(results.data())