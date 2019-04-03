# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.json_activity import JsonActivity  # noqa: E501
from openapi_server.models.json_paginated_results_of_reference import JsonPaginatedResultsOfReference  # noqa: E501
from openapi_server.test import BaseTestCase


class TestActivityControllerController(BaseTestCase):
    """ActivityControllerController integration test stubs"""

    def test_create_activity(self):
        """Test case for create_activity

        Create a new.
        """
        body = (BytesIO(b'some file data'), 'file.txt')
        query_string = [('user_id', 3.4)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/rest/repo/v1/activity',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_activity(self):
        """Test case for delete_activity

        Delete an.
        """
        body = (BytesIO(b'some file data'), 'file.txt')
        query_string = [('user_id', 3.4)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/rest/repo/v1/activity/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_activity(self):
        """Test case for get_activity

        Get an existing.
        """
        body = (BytesIO(b'some file data'), 'file.txt')
        query_string = [('user_id', 3.4)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/rest/repo/v1/activity/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_entities_generated_by(self):
        """Test case for get_entities_generated_by

        .
        """
        query_string = [('limit', 10),
                        ('offset', 0),
                        ('user_id', 3.4)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rest/repo/v1/activity/{id}/generated'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_activity(self):
        """Test case for update_activity

        Update an.
        """
        body = (BytesIO(b'some file data'), 'file.txt')
        query_string = [('user_id', 3.4)]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/rest/repo/v1/activity/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
