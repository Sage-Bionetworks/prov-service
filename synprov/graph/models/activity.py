import uuid

from synprov.models.activity import Activity
from synprov.util import get_datetime


class GraphActivity(Activity):

    def __init__(self,
                 name='',
                 **kwargs):
        super().__init__(name=name)
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        self.label = 'Activity'
        self.openapi_types.update({'label': str})


    def create(self):
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
