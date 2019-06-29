import connexion
import six
import uuid
import humps

from py2neo import Graph, Node, NodeMatcher

from synprov.config import neomod
from synprov.graphmodels import Activity, Reference, Agent


graph = Graph(neomod.neo.db.url)


def create_activity(body):  # noqa: E501
    """Create a new.

    Create a new Activity. If the passed Activity object contains a Used array, you must set the concreteType field of each Used subclass. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: Activity
    """
    act = Activity(**humps.decamelize(body))
    act.save()

    return act.node


def get_activities_graph():  # noqa: E501
    """Get provenance graph.

    Retrieve all nodes and relationships in the graph that pass filters. # noqa: E501


    :rtype: Graph
    """
    return 'Not Implemented', 501

