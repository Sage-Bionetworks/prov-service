from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (BooleanField,
                                ListField,
                                EmbeddedDocumentField,
                                ReferenceField,
                                StringField,
                                IntField)


class Reference(Document):
    """Reference - a model defined in OpenAPI

    :param target_version_number: The target_version_number of this Reference.  # noqa: E501
    :type target_version_number: int
    :param target_id: The target_id of this Reference.  # noqa: E501
    :type target_id: str
    :param role: The role of this Reference.  # noqa: E501
    :type role: str
    """
    meta = {'collection': 'references'}
    target_id = StringField(required=True, 
                            unique_with=['target_version_number', 'role'])
    target_version_number = IntField(required=True,
                                     unique_with=['target_id', 'role'])
    role = StringField(unique_with=['target_id', 'target_version_number'],
                       default='')


class Agent(Document):
    """Agent - a model defined in OpenAPI

    :param agent_id: The agent_id of this Agent.  # noqa: E501
    :type agent_id: str
    :param role: The role of this Agent.  # noqa: E501
    :type role: str
    """
    meta = {'collection': 'agents'}
    agent_id = StringField(required=True, unique_with='role')
    role = StringField(unique_with='agent_id', default='')


class Activity(Document):
    """Activity - a model defined in OpenAPI

    :param id: The id of this Activity.  # noqa: E501
    :type id: str
    :param used: The used of this Activity.  # noqa: E501
    :type used: List[Reference]
    :param generated: The generated of this Activity.  # noqa: E501
    :type generated: List[Reference]
    :param agents: The agents of this Activity.  # noqa: E501
    :type agents: List[Agent]
    :param created_by: The created_by of this Activity.  # noqa: E501
    :type created_by: str
    :param etag: The etag of this Activity.  # noqa: E501
    :type etag: str
    :param modified_on: The modified_on of this Activity.  # noqa: E501
    :type modified_on: datetime
    :param modified_by: The modified_by of this Activity.  # noqa: E501
    :type modified_by: str
    :param created_on: The created_on of this Activity.  # noqa: E501
    :type created_on: datetime
    :param name: The name of this Activity.  # noqa: E501
    :type name: str
    :param description: The description of this Activity.  # noqa: E501
    :type description: str
    """
    meta = {'collection': 'activities'}
    activity_id = StringField(unique=True, default='')
    used = ListField(ReferenceField('Reference'), 
                     required=True,
                     default=[])
    generated = ListField(ReferenceField('Reference'), 
                          required=True,
                          default=[])
    agents = ListField(ReferenceField(Agent), required=False)
    name = StringField(default='')
    description = StringField(default='')
