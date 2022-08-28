"""
    Swagger Petstore

    A sample API that uses a petstore as an example to demonstrate features in the OpenAPI 3.0 specification  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_pet(self):
        """Test case for add_pet

        """
        pass

    def test_delete_pet(self):
        """Test case for delete_pet

        """
        pass

    def test_find_pet_by_id(self):
        """Test case for find_pet_by_id

        """
        pass

    def test_find_pets(self):
        """Test case for find_pets

        """
        pass


if __name__ == '__main__':
    unittest.main()