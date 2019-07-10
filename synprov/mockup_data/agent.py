import uuid
import json

from synprov.models.agent import Agent
from synprov.util import get_datetime


class MockAgent(Agent):

    def __init__(self, name='', user_id='', **kwargs):
        super().__init__(name=name, user_id=user_id)
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
        self.label = 'Agent'
        for kwa in kwargs:
            self.__setattr__(kwa, kwargs[kwa])
        self.openapi_types.update({'label': str})

    def get_data(self):
        return self.to_dict()
