"""
    Otoroshi Admin API

    Admin API of the Otoroshi reverse proxy  # noqa: E501

    The version of the OpenAPI document: 1.5.0-alpha.14
    Contact: oss@maif.fr
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.scripts_api import ScriptsApi  # noqa: E501


class TestScriptsApi(unittest.TestCase):
    """ScriptsApi unit test stubs"""

    def setUp(self):
        self.api = ScriptsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_bulk_create_action

        Create multiple otoroshi.script.Scripts at the same time  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action

        Delete multiple otoroshi.script.Scripts at the same time  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action

        Update (using json-patch) multiple otoroshi.script.Scripts at the same time  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_bulk_update_action

        Update multiple otoroshi.script.Scripts at the same time  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_compile_script(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_compile_script

        Trigger script compilation of the server  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_create_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_create_action

        Creates a otoroshi.script.Script  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_delete_entity_action

        Deletes a specific otoroshi.script.Script using its id  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action

        Find all possible otoroshi.script.Scripts entities  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list

        Search plugins based on type of plugin  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action

        Find a specific otoroshi.script.Script using its id  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_patch_entity_action

        Updates (using json-patch) a specific otoroshi.script.Script using its id  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_script_api_controller_update_entity_action(self):
        """Test case for otoroshi_controllers_adminapi_script_api_controller_update_entity_action

        Updates a specific otoroshi.script.Script using its id  # noqa: E501
        """
        pass

    def test_otoroshi_controllers_adminapi_templates_controller_initiate_script(self):
        """Test case for otoroshi_controllers_adminapi_templates_controller_initiate_script

        Creates a new Script from a template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()