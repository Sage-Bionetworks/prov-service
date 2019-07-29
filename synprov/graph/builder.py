import logging

from py2neo import Graph

from synprov.config import neo4j_connection as graph
from synprov.models.activity_form import ActivityForm
from synprov.graph.client import GraphClient
from synprov.graph.models.activity import GraphActivity
from synprov.graph.models.reference import GraphReference
from synprov.graph.models.agent import GraphAgent
from synprov.graph.models.relationship import GraphRelationship


logger = logging.getLogger(__name__)


class ActivityBuilder(ActivityForm):

    gdb = GraphClient(graph)

    def __init__(self,
                 name,
                 used,
                 generated,
                 agents,
                 **kwargs):

        super().__init__(name=name)

        self.activity = GraphActivity(name=name, **kwargs)
        self.used = [GraphReference(**u) for u in used]
        self.generated = [GraphReference(**g) for g in generated]
        self.agents = [GraphAgent(**a) for a in agents]
        self.openapi_types.update({'activity': object})

    def _find_activity(self):
        activities = graph.run(
            '''
            WITH {e_ids} as refs
            MATCH (r:Reference)-[:WASGENERATEDBY]->(act:Activity)
            WHERE r.target_id in refs
            WITH act, size(refs) as inputCnt, count(DISTINCT r) as cnt
            WHERE cnt = inputCnt
            RETURN act
            ''',
            e_ids=[e.target_id for e in self.generated]
        ).data()

        if len(activities) > 1:
            raise ValueError
        elif len(activities):
            return activities[0]['act']

    def connect_used(self):
        logger.debug("Creating :USED relationships")
        used_rels = [GraphRelationship(self.activity, ref)
                     for ref in self.used]
        return used_rels

    def connect_associated(self):
        logger.debug("Creating :WASASSOCIATEDWITH relationships")
        associated_rels = [GraphRelationship(self.activity, agt)
                           for agt in self.agents]
        return associated_rels

    def connect_generated(self):
        logger.debug("Creating :WASGENERATEDBY relationships")
        generated_rels = [GraphRelationship(gen, self.activity)
                          for gen in self.generated]
        return generated_rels

    def connect_attributed(self):
        logger.debug("Creating :WASATTRIBUTEDTO relationships")
        attributed_rels = [GraphRelationship(gen, agt)
                          for gen in self.generated
                          for agt in self.agents]
        return attributed_rels

    def save(self):
        if not self._find_activity():
            logger.info("Creating new activity")
            self.activity.create()
            self.gdb.create_node(self.activity)
            for u in self.used:
                u.create()
                self.gdb.create_node(u)
            for g in self.generated:
                g.create()
                self.gdb.create_node(g)
            for a in self.agents:
                a.create()
                self.gdb.create_node(a)
            for rel in self.connect_used():
                rel.create()
                self.gdb.create_relationship(rel)
            for rel in self.connect_associated():
                rel.create()
                self.gdb.create_relationship(rel)
            for rel in self.connect_generated():
                rel.create()
                self.gdb.create_relationship(rel)
            for rel in self.connect_attributed():
                rel.create()
                self.gdb.create_relationship(rel)

        return self._find_activity()