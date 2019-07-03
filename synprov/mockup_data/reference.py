import uuid
import json

from synprov.models.reference import Reference
from synprov.mockup_data.dict import ReferenceClasses
from synprov.mockup_data.dict import ReferenceSubclasses


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
        self.id = uuid.uuid1()
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
        x = self.to_dict()
        x.update({':LABEL': self.label})
        return x