import uuid

from py2neo import Graph, Node, Relationship, NodeMatcher

from synprov.config import neomod
from synprov.models.reference import Reference
from synprov.models.agent import Agent
from synprov.util import get_datetime

graph = Graph(neomod.neo.db.url)
matcher = NodeMatcher(graph)


class GraphReference(Reference):

    def __init__(self,
                 name='',
                 target_id='',
                 target_version_id='1',
                 **kwargs):
        super().__init__(name=name,
                         target_id=target_id,
                         target_version_id=target_version_id)
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        self.label = 'Reference'
        self.openapi_types.update({'label': str})

    def create(self):
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()