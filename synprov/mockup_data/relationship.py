import uuid
import json
import random as r

from synprov.models.prov_relationship import ProvRelationship
from synprov.mockup_data.dict import (ActivityRoles,
                                      NodeRelationships)


class MockRelationship(ProvRelationship):

    node_relationships = NodeRelationships

    def __init__(self, start_node, end_node, activity_class=None):
        super().__init__(start_node=start_node.id, end_node=end_node.id)

        self.start_id = start_node
        self.end_id = end_node

        start_end_nodes = (start_node.label, end_node.label)
        self.type = self.node_relationships[start_end_nodes]

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

    def get_data(self):
        x = self.to_dict()
        x.update({
            ':START_ID': str(self.start_id),
            ':END_ID': str(self.end_id),
            ':TYPE': self.type
        })
        return x
