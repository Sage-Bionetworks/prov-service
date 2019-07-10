# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov.models.prov_node import ProvNode
from synprov import util

from synprov.models.prov_node import ProvNode  # noqa: E501

class Activity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, description=None, created_at=None, created_by=None, _class=None):  # noqa: E501
        """Activity - a model defined in OpenAPI

        :param id: The id of this Activity.  # noqa: E501
        :type id: str
        :param name: The name of this Activity.  # noqa: E501
        :type name: str
        :param description: The description of this Activity.  # noqa: E501
        :type description: str
        :param created_at: The created_at of this Activity.  # noqa: E501
        :type created_at: date
        :param created_by: The created_by of this Activity.  # noqa: E501
        :type created_by: str
        :param _class: The _class of this Activity.  # noqa: E501
        :type _class: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'description': str,
            'created_at': date,
            'created_by': str,
            '_class': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'created_at': 'createdAt',
            'created_by': 'createdBy',
            '_class': 'class'
        }

        self._id = id
        self._name = name
        self._description = description
        self._created_at = created_at
        self._created_by = created_by
        self.__class = _class

    @classmethod
    def from_dict(cls, dikt) -> 'Activity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Activity of this Activity.  # noqa: E501
        :rtype: Activity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Activity.


        :return: The id of this Activity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Activity.


        :param id: The id of this Activity.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Activity.


        :return: The name of this Activity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Activity.


        :param name: The name of this Activity.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Activity.


        :return: The description of this Activity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Activity.


        :param description: The description of this Activity.
        :type description: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Activity.


        :return: The created_at of this Activity.
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Activity.


        :param created_at: The created_at of this Activity.
        :type created_at: date
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Activity.


        :return: The created_by of this Activity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Activity.


        :param created_by: The created_by of this Activity.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def _class(self):
        """Gets the _class of this Activity.


        :return: The _class of this Activity.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Activity.


        :param _class: The _class of this Activity.
        :type _class: str
        """

        self.__class = _class