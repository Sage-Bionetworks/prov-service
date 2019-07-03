import uuid
import json

from synprov.models.agent import Agent


class MockAgent(Agent):

    def __init__(self, name='', user_id=''):
        super().__init__(name=name, user_id=user_id)
        self.id = uuid.uuid1()
        self.label = 'Agent'
        self.openapi_types.update({'label': str})

    def get_data(self):
        x = self.to_dict()
        x.update({':LABEL': self.label})
        return x