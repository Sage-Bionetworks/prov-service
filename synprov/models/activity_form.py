# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov.models.agent import Agent
from synprov.models.reference import Reference
from synprov import util


class ActivityForm(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, used=None, generated=None, agents=None, name=None, description=None, _class=None):  # noqa: E501
        """ActivityForm - a model defined in OpenAPI

        :param used: The used of this ActivityForm.  # noqa: E501
        :type used: List[Reference]
        :param generated: The generated of this ActivityForm.  # noqa: E501
        :type generated: List[Reference]
        :param agents: The agents of this ActivityForm.  # noqa: E501
        :type agents: List[Agent]
        :param name: The name of this ActivityForm.  # noqa: E501
        :type name: str
        :param description: The description of this ActivityForm.  # noqa: E501
        :type description: str
        :param _class: The _class of this ActivityForm.  # noqa: E501
        :type _class: str
        """
        self.openapi_types = {
            'used': List[Reference],
            'generated': List[Reference],
            'agents': List[Agent],
            'name': str,
            'description': str,
            '_class': str
        }

        self.attribute_map = {
            'used': 'used',
            'generated': 'generated',
            'agents': 'agents',
            'name': 'name',
            'description': 'description',
            '_class': 'class'
        }

        self._used = used
        self._generated = generated
        self._agents = agents
        self._name = name
        self._description = description
        self.__class = _class

    @classmethod
    def from_dict(cls, dikt) -> 'ActivityForm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ActivityForm of this ActivityForm.  # noqa: E501
        :rtype: ActivityForm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def used(self):
        """Gets the used of this ActivityForm.


        :return: The used of this ActivityForm.
        :rtype: List[Reference]
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ActivityForm.


        :param used: The used of this ActivityForm.
        :type used: List[Reference]
        """

        self._used = used

    @property
    def generated(self):
        """Gets the generated of this ActivityForm.


        :return: The generated of this ActivityForm.
        :rtype: List[Reference]
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this ActivityForm.


        :param generated: The generated of this ActivityForm.
        :type generated: List[Reference]
        """

        self._generated = generated

    @property
    def agents(self):
        """Gets the agents of this ActivityForm.


        :return: The agents of this ActivityForm.
        :rtype: List[Agent]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this ActivityForm.


        :param agents: The agents of this ActivityForm.
        :type agents: List[Agent]
        """

        self._agents = agents

    @property
    def name(self):
        """Gets the name of this ActivityForm.


        :return: The name of this ActivityForm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActivityForm.


        :param name: The name of this ActivityForm.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ActivityForm.


        :return: The description of this ActivityForm.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ActivityForm.


        :param description: The description of this ActivityForm.
        :type description: str
        """

        self._description = description

    @property
    def _class(self):
        """Gets the _class of this ActivityForm.


        :return: The _class of this ActivityForm.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ActivityForm.


        :param _class: The _class of this ActivityForm.
        :type _class: str
        """

        self.__class = _class
