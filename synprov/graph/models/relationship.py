import uuid
import json
import random as r

from synprov.models.prov_relationship import ProvRelationship
from synprov.mock.dict import NodeRelationships
from synprov.util import get_datetime


class GraphRelationship(ProvRelationship):

    def __init__(self, start_node, end_node):
        super().__init__(start_node=start_node.id, end_node=end_node.id)
        self.start_id = start_node
        self.end_id = end_node

        start_end_nodes = (start_node.label, end_node.label)
        self.type = NodeRelationships[start_end_nodes]

    def create(self):
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
