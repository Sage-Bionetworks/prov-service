# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov import util


class Agent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, agent_id=None, role=None):  # noqa: E501
        """Agent - a model defined in OpenAPI

        :param agent_id: The agent_id of this Agent.  # noqa: E501
        :type agent_id: str
        :param role: The role of this Agent.  # noqa: E501
        :type role: str
        """
        self.openapi_types = {
            'agent_id': str,
            'role': str
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'role': 'role'
        }

        self._agent_id = agent_id
        self._role = role

    @classmethod
    def from_dict(cls, dikt) -> 'Agent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Agent of this Agent.  # noqa: E501
        :rtype: Agent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def agent_id(self):
        """Gets the agent_id of this Agent.


        :return: The agent_id of this Agent.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this Agent.


        :param agent_id: The agent_id of this Agent.
        :type agent_id: str
        """

        self._agent_id = agent_id

    @property
    def role(self):
        """Gets the role of this Agent.


        :return: The role of this Agent.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Agent.


        :param role: The role of this Agent.
        :type role: str
        """

        self._role = role