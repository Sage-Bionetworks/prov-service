import connexion
import six
import uuid
import humps
import json

from py2neo import Graph, Node, NodeMatcher

from synprov.config import neomod
from synprov.graphmodels import Activity, Reference, Agent
from synprov.util import neo4j_to_d3, neo4j_export


graph = Graph(neomod.neo.db.url)


def create_activity(body):  # noqa: E501
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


def get_activities_graph(limit=20, as_d3=True):  # noqa: E501
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
    if as_d3:
        return neo4j_to_d3(results.data())
    else:
        return neo4j_export(results.data())
