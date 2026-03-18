import unittest

from flask import json

from openapi_server.models.healthcheck200_response import Healthcheck200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHealthcheckController(BaseTestCase):
    """HealthcheckController integration test stubs"""

    def test_healthcheck(self):
        """Test case for healthcheck

        Health check
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/healthcheck',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
