# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov import util


class ProvRelationship(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, start_node=None, end_node=None, type=None, start_node_role=None, end_node_role=None):  # noqa: E501
        """ProvRelationship - a model defined in OpenAPI

        :param id: The id of this ProvRelationship.  # noqa: E501
        :type id: str
        :param start_node: The start_node of this ProvRelationship.  # noqa: E501
        :type start_node: str
        :param end_node: The end_node of this ProvRelationship.  # noqa: E501
        :type end_node: str
        :param type: The type of this ProvRelationship.  # noqa: E501
        :type type: str
        :param start_node_role: The start_node_role of this ProvRelationship.  # noqa: E501
        :type start_node_role: str
        :param end_node_role: The end_node_role of this ProvRelationship.  # noqa: E501
        :type end_node_role: str
        """
        self.openapi_types = {
            'id': str,
            'start_node': str,
            'end_node': str,
            'type': str,
            'start_node_role': str,
            'end_node_role': str
        }

        self.attribute_map = {
            'id': 'id',
            'start_node': 'startNode',
            'end_node': 'endNode',
            'type': 'type',
            'start_node_role': 'startNodeRole',
            'end_node_role': 'endNodeRole'
        }

        self._id = id
        self._start_node = start_node
        self._end_node = end_node
        self._type = type
        self._start_node_role = start_node_role
        self._end_node_role = end_node_role

    @classmethod
    def from_dict(cls, dikt) -> 'ProvRelationship':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProvRelationship of this ProvRelationship.  # noqa: E501
        :rtype: ProvRelationship
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ProvRelationship.


        :return: The id of this ProvRelationship.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProvRelationship.


        :param id: The id of this ProvRelationship.
        :type id: str
        """

        self._id = id

    @property
    def start_node(self):
        """Gets the start_node of this ProvRelationship.


        :return: The start_node of this ProvRelationship.
        :rtype: str
        """
        return self._start_node

    @start_node.setter
    def start_node(self, start_node):
        """Sets the start_node of this ProvRelationship.


        :param start_node: The start_node of this ProvRelationship.
        :type start_node: str
        """

        self._start_node = start_node

    @property
    def end_node(self):
        """Gets the end_node of this ProvRelationship.


        :return: The end_node of this ProvRelationship.
        :rtype: str
        """
        return self._end_node

    @end_node.setter
    def end_node(self, end_node):
        """Sets the end_node of this ProvRelationship.


        :param end_node: The end_node of this ProvRelationship.
        :type end_node: str
        """

        self._end_node = end_node

    @property
    def type(self):
        """Gets the type of this ProvRelationship.


        :return: The type of this ProvRelationship.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProvRelationship.


        :param type: The type of this ProvRelationship.
        :type type: str
        """
        allowed_values = ["WASASSOCIATEDWITH", "WASGENERATEDBY", "USED", "WASATTRIBUTEDTO"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def start_node_role(self):
        """Gets the start_node_role of this ProvRelationship.


        :return: The start_node_role of this ProvRelationship.
        :rtype: str
        """
        return self._start_node_role

    @start_node_role.setter
    def start_node_role(self, start_node_role):
        """Sets the start_node_role of this ProvRelationship.


        :param start_node_role: The start_node_role of this ProvRelationship.
        :type start_node_role: str
        """

        self._start_node_role = start_node_role

    @property
    def end_node_role(self):
        """Gets the end_node_role of this ProvRelationship.


        :return: The end_node_role of this ProvRelationship.
        :rtype: str
        """
        return self._end_node_role

    @end_node_role.setter
    def end_node_role(self, end_node_role):
        """Sets the end_node_role of this ProvRelationship.


        :param end_node_role: The end_node_role of this ProvRelationship.
        :type end_node_role: str
        """

        self._end_node_role = end_node_role