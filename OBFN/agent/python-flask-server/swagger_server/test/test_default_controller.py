# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.obfn_parameters import ObfnParameters  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_configuration(self):
        """Test case for create_configuration

        Create configuration
        """
        obfn_params = ObfnParameters()
        response = self.client.open(
            '/api/obfn',
            method='POST',
            data=json.dumps(obfn_params),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_configuration(self):
        """Test case for delete_configuration

        Delete configuration
        """
        response = self.client.open(
            '/api/obfn',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_configuration(self):
        """Test case for retrieve_configuration

        Retrieve configuration
        """
        response = self.client.open(
            '/api/obfn',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_configuration(self):
        """Test case for update_configuration

        Update configuration
        """
        obfn_params = ObfnParameters()
        response = self.client.open(
            '/api/obfn',
            method='PUT',
            data=json.dumps(obfn_params),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
