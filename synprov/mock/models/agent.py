import uuid

from synprov.models.agent import Agent
from synprov.util import get_datetime


class MockAgent(Agent):

    def __init__(self, name='', user_id='', **kwargs):
        super().__init__(name=name, user_id=user_id)
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        self.label = 'Agent'
        self.openapi_types.update({'label': str})

