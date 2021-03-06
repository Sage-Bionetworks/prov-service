# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov.models.prov_node import ProvNode
from synprov.models.reference1 import Reference1
from synprov import util


class Reference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, description=None, created_at=None, created_by=None, target_version_id=None, target_id=None, _class=None, subclass=None):  # noqa: E501
        """Reference - a model defined in OpenAPI

        :param id: The id of this Reference.  # noqa: E501
        :type id: str
        :param name: The name of this Reference.  # noqa: E501
        :type name: str
        :param description: The description of this Reference.  # noqa: E501
        :type description: str
        :param created_at: The created_at of this Reference.  # noqa: E501
        :type created_at: date
        :param created_by: The created_by of this Reference.  # noqa: E501
        :type created_by: str
        :param target_version_id: The target_version_id of this Reference.  # noqa: E501
        :type target_version_id: str
        :param target_id: The target_id of this Reference.  # noqa: E501
        :type target_id: str
        :param _class: The _class of this Reference.  # noqa: E501
        :type _class: str
        :param subclass: The subclass of this Reference.  # noqa: E501
        :type subclass: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'description': str,
            'created_at': date,
            'created_by': str,
            'target_version_id': str,
            'target_id': str,
            '_class': str,
            'subclass': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'created_at': 'createdAt',
            'created_by': 'createdBy',
            'target_version_id': 'targetVersionId',
            'target_id': 'targetId',
            '_class': 'class',
            'subclass': 'subclass'
        }

        self._id = id
        self._name = name
        self._description = description
        self._created_at = created_at
        self._created_by = created_by
        self._target_version_id = target_version_id
        self._target_id = target_id
        self.__class = _class
        self._subclass = subclass

    @classmethod
    def from_dict(cls, dikt) -> 'Reference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Reference of this Reference.  # noqa: E501
        :rtype: Reference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Reference.


        :return: The id of this Reference.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Reference.


        :param id: The id of this Reference.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Reference.


        :return: The name of this Reference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Reference.


        :param name: The name of this Reference.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Reference.


        :return: The description of this Reference.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Reference.


        :param description: The description of this Reference.
        :type description: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Reference.


        :return: The created_at of this Reference.
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Reference.


        :param created_at: The created_at of this Reference.
        :type created_at: date
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Reference.


        :return: The created_by of this Reference.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Reference.


        :param created_by: The created_by of this Reference.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def target_version_id(self):
        """Gets the target_version_id of this Reference.


        :return: The target_version_id of this Reference.
        :rtype: str
        """
        return self._target_version_id

    @target_version_id.setter
    def target_version_id(self, target_version_id):
        """Sets the target_version_id of this Reference.


        :param target_version_id: The target_version_id of this Reference.
        :type target_version_id: str
        """
        if target_version_id is None:
            raise ValueError("Invalid value for `target_version_id`, must not be `None`")  # noqa: E501

        self._target_version_id = target_version_id

    @property
    def target_id(self):
        """Gets the target_id of this Reference.


        :return: The target_id of this Reference.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this Reference.


        :param target_id: The target_id of this Reference.
        :type target_id: str
        """
        if target_id is None:
            raise ValueError("Invalid value for `target_id`, must not be `None`")  # noqa: E501

        self._target_id = target_id

    @property
    def _class(self):
        """Gets the _class of this Reference.


        :return: The _class of this Reference.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Reference.


        :param _class: The _class of this Reference.
        :type _class: str
        """

        self.__class = _class

    @property
    def subclass(self):
        """Gets the subclass of this Reference.


        :return: The subclass of this Reference.
        :rtype: str
        """
        return self._subclass

    @subclass.setter
    def subclass(self, subclass):
        """Sets the subclass of this Reference.


        :param subclass: The subclass of this Reference.
        :type subclass: str
        """

        self._subclass = subclass
