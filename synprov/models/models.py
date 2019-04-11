from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (BooleanField,
                                ListField,
                                EmbeddedDocumentField,
                                ReferenceField, 
                                StringField,
                                IntField)


class Reference(EmbeddedDocument):

  meta = {'collection': 'reference'}
  target_id = StringField(required=True)
  target_version_number = IntField(required=True)


class Used(EmbeddedDocument):

  meta = {'collection': 'used'}
  reference = EmbeddedDocumentField('Reference', required=True)
  executed = BooleanField(default=False)


class Activity(Document):

  meta = {'collection': 'activity'}
  activity_id = StringField(unique=True)
  used = ListField(EmbeddedDocumentField('Used'), required=True)
  name = StringField(default='')
  description = StringField(default='')