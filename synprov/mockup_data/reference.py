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
                 class_idx=0,
                 subclass_idx=0):
        super().__init__(name=name,
                         target_id=target_id,
                         target_version_id=target_version_id)
        self.id = str(uuid.uuid1())
        self.created_at = get_datetime()
        self.label = 'Reference'
        self.openapi_types.update({'label': str})

    def select_class(self, class_idx):
        self._class = self.reference_classes[class_idx]

    def select_subclass(self, subclass_idx):
        self.subclass = self.reference_subclasses[self._class][subclass_idx]

    def get_class_count(self):
        return len(self.reference_classes)

    def get_subclass_count(self):
        return len(self.reference_subclasses[self._class])

    def get_data(self):
        return self.to_dict()
