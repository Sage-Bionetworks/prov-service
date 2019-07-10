import uuid
import json

from synprov.models.reference import Reference
from synprov.mockup_data.dict import ReferenceClasses
from synprov.mockup_data.dict import ReferenceSubclasses
from synprov.util import get_datetime


class MockReference(Reference):

    reference_classes = ReferenceClasses
    reference_subclasses = ReferenceSubclasses

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
        return len(self.reference_classes)

    def get_subclass_count(self):
        return len(self.reference_subclasses[self._class])

    def get_data(self):
        return self.to_dict()
