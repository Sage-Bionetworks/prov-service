import connexion
import six
import uuid
import humps

from py2neo import Node, NodeMatcher

from synprov.config import neo4j_connection as graph
from synprov.graph import GraphActivity, GraphReference, GraphAgent
from synprov.util import neo4j_to_d3


def get_agent_subgraph(id, limit=3, direction='down'):  # noqa: E501
    """Get subgraph connected to an agent.

    Retrieve all nodes and relationships in the graph that pass filters. # noqa: E501

    :param id: The ID of the agent to fetch.
    :type id: str

    :rtype: Graph
    """
    direction_rels = {
        'down': '<-[r:WASASSOCIATEDWITH]-'
    }
    query_base = (
        '''
        MATCH (t:Agent {{user_id: {{id}}}}){dir_rel}(s:Activity)
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
