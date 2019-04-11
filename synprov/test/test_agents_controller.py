# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from synprov.models.agent import Agent  # noqa: E501
from synprov.test import BaseTestCase


class TestAgentsController(BaseTestCase):
    """AgentsController integration test stubs"""

    def test_get_agent(self):
        """Test case for get_agent

        Get an existing.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rest/prov/v1/agents/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_agents(self):
        """Test case for list_agents

        .
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rest/prov/v1/agents',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
