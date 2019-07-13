import uuid
import json

from synprov.models.reference import Reference
from synprov.mock.dict import ReferenceClasses
from synprov.mock.dict import ReferenceSubclasses
from synprov.util import get_datetime


class MockReference(Reference):

    def __init__(self,
                 name='',
                 target_id='',
                 target_version_id='1',
                 **kwargs):
        super().__init__(name=name,
                         target_id=target_id,
                         target_version_id=target_version_id)
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
        self.label = 'Reference'
        for kwa in kwargs:
            self.__setattr__(kwa, kwargs[kwa])
        self.openapi_types.update({'label': str})

    def get_class_count(self):
        return len(ReferenceClasses)

    def get_subclass_count(self):
        return len(ReferenceSubclasses[self._class])

