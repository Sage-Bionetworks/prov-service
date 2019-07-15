import uuid

from synprov.models.reference import Reference
from synprov.util import get_datetime


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