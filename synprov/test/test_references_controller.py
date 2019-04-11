# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from synprov.models.reference import Reference  # noqa: E501
from synprov.test import BaseTestCase


class TestReferencesController(BaseTestCase):
    """ReferencesController integration test stubs"""

    def test_get_reference(self):
        """Test case for get_reference

        Get an existing.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/rest/prov/v1/references/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
