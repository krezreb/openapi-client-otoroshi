"""
    Otoroshi Admin API

    Admin API of the Otoroshi reverse proxy  # noqa: E501

    The version of the OpenAPI document: 1.5.0-alpha.14
    Contact: oss@maif.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.templates_api import TemplatesApi  # noqa: E501


class TestTemplatesApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""

    def setUp(self):
        self.api = TemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(self):
        """Test case for otoroshi_controllers_adminapi_templates_controller_create_from_template_templates

        Creates a new Template from a template  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates(self):
        """Test case for otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates

        Creates a new ApiKey from a template  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates(self):
        """Test case for otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates

        Creates a new ServiceGroup from a template  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_templates_controller_initiate_service_templates(self):
        """Test case for otoroshi_controllers_adminapi_templates_controller_initiate_service_templates

        Creates a new Service from a template  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates(self):
        """Test case for otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates

        Creates a new TcpService from a template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
