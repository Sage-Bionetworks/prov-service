# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from synprov.models import Activity  # noqa: E501
from synprov.test import BaseTestCase


class TestActivitiesController(BaseTestCase):
    """ActivitiesController integration test stubs"""

    def test_create_activity(self):
        """Test case for create_activity

        Create a new.
        """
        body = {
            'name': 'activity1', 
            'agents': [
                {'agent_id': 'agent1'}
            ], 
            'used': [
                {
                    'target_id': 'entity1', 
                    'target_version_number': 1}
            ], 
            'generated': [
                {
                    'target_id': 'entity2', 
                    'target_version_number': 1
                }
            ]
        }
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/rest/repo/v1/activity',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_get_activity(self):
        """Test case for get_activity

        Get an existing.
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/rest/repo/v1/activity/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if __name__ == '__main__':
    unittest.main()
