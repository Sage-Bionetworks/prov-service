import uuid

from synprov.models.agent import Agent
from synprov.util import get_datetime


class GraphAgent(Agent):

    def __init__(self,
                 name='',
                 user_id='',
                 **kwargs):
        super().__init__(name=name, user_id=user_id)
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        self.label = 'Agent'
        self.openapi_types.update({'label': str})

    def create(self):
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
