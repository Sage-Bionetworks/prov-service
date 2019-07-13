import uuid
import json
import random as r

from synprov.models.prov_relationship import ProvRelationship
from synprov.mock.dict import (ActivityRoles,
                               NodeRelationships)
from synprov.util import get_datetime


class MockRelationship(ProvRelationship):

    def __init__(self, start_node, end_node, activity_class=None):
        super().__init__(start_node=start_node.id, end_node=end_node.id)
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
        self.start_id = start_node
        self.end_id = end_node

        start_end_nodes = (start_node.label, end_node.label)
        self.type = NodeRelationships[start_end_nodes]

        if start_end_nodes == ('Activity', 'Agent'):
            self.end_node_role = ActivityRoles[start_node._class][
                'in_subclass'
            ][self.type][end_node.label]['role']
        elif start_end_nodes == ('Activity', 'Reference'):
            self.end_node_role = ActivityRoles[start_node._class][
                'in_subclass'
            ][self.type][end_node.subclass]['role']
        elif start_end_nodes == ('Reference', 'Activity'):
            self.start_node_role = ActivityRoles[end_node._class][
                'out_subclass'
            ][self.type][start_node.subclass]['role']
        elif start_end_nodes == ('Reference', 'Agent'):
            self.end_node_role = ActivityRoles[activity_class][
                'out_subclass'
            ][self.type][end_node.label]['role']
            self.start_node_role = ActivityRoles[activity_class][
                'out_subclass'
            ][self.type][start_node.subclass]['role']


