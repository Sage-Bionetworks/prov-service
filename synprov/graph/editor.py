import logging

from py2neo import Graph

from synprov.config import neo4j_connection as graph
from synprov.models.activity import Activity
from synprov.graph.client import GraphClient
from synprov.graph.models.activity import GraphActivity
from synprov.graph.models.reference import GraphReference
from synprov.graph.models.agent import GraphAgent
from synprov.graph.models.relationship import GraphRelationship


logger = logging.getLogger(__name__)


class ActivityEditor(Activity):

    gdb = GraphClient(graph)

    def __init__(self,
                 id,
                 **kwargs):

        # super().__init__(name=name)
        self.id = id
        activity_node = self._find_activity()
        self.activity = GraphActivity(**activity_node)
        self.openapi_types.update({'activity': object})

    def _find_activity(self):
        return graph.nodes.match('Activity', id=self.id).first()

    def _find_used_rel(self):
        activity_node = self._find_activity()
        used_node = graph.nodes.match('Reference', id=self.used.id).first()
        return graph.match((activity_node, used_node), r_type='USED').first()

    def connect_used(self):
        logger.debug("Creating :USED relationships")
        used_rel = GraphRelationship(self.activity, self.used)

        return used_rel

    def append_used(self, used_form):
        self.used = GraphReference(**used_form)
        self.used.create(self.gdb.graph)
        self.gdb.create_node(self.used)

        if not self._find_used_rel():
            rel = self.connect_used()
            rel.create()
            self.gdb.create_relationship(rel)

        return self._find_activity()