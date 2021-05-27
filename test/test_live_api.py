"""
    Otoroshi Admin API

    Admin API of the Otoroshi reverse proxy  # noqa: E501

    The version of the OpenAPI document: 1.5.0-alpha.14
    Contact: oss@maif.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.live_api import LiveApi  # noqa: E501


class TestLiveApi(unittest.TestCase):
    """LiveApi unit test stubs"""

    def setUp(self):
        self.api = LiveApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_otoroshi_controllers_adminapi_stats_controller_global_live_stats(self):
        """Test case for otoroshi_controllers_adminapi_stats_controller_global_live_stats

        Get global live statis  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_stats_controller_host_metrics(self):
        """Test case for otoroshi_controllers_adminapi_stats_controller_host_metrics

        Get local host metrics  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_stats_controller_service_live_stats_live(self):
        """Test case for otoroshi_controllers_adminapi_stats_controller_service_live_stats_live

        Get live stats for a specific service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
