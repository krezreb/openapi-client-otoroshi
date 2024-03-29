"""
    Otoroshi Admin API

    Admin API of the Otoroshi reverse proxy  # noqa: E501

    The version of the OpenAPI document: 1.5.0-alpha.14
    Contact: oss@maif.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.events_api import EventsApi  # noqa: E501


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_otoroshi_controllers_adminapi_events_controller_alert_events(self):
        """Test case for otoroshi_controllers_adminapi_events_controller_alert_events

        Get all events of type AlertEvent  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_events_controller_audit_events(self):
        """Test case for otoroshi_controllers_adminapi_events_controller_audit_events

        Get all events of type AuditEvent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
