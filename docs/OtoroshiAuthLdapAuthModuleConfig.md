# OtoroshiAuthLdapAuthModuleConfig

Authentication module that works with LDAP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_filters** | [**[OtoroshiAuthGroupFilter]**](OtoroshiAuthGroupFilter.md) | LDAP group filters | [optional] 
**metadata** | **{str: (str,)}** | Metadata of the module | [optional] 
**allow_empty_password** | **bool** | Allow empty password access | [optional] 
**basic_auth** | **bool** | Use standard basic auth or web login form | [optional] 
**search_base** | **str** | LDAP search base | [optional] 
**name_field** | **str** | Field name to get name from user profile | [optional] 
**email_field** | **str** | Field name to get email from user profile | [optional] 
**type** | **str** | the type of the module | [optional] 
**metadata_field** | **dict** | Field name to get metadata from user profile | [optional] 
**rights_override** | [**{str: (OtoroshiModelsUserRights,)}**](OtoroshiModelsUserRights.md) | Overrides user rights. Object with email as key | [optional] 
**group_rights** | [**{str: (OtoroshiAuthGroupRights,)}**](OtoroshiAuthGroupRights.md) | Rights associated with groups | [optional] 
**id** | **str** | Unique id of the config | [optional] 
**extra_metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Add metadata to user. Object with email as key | [optional] 
**search_filter** | **str** | Filter for users | [optional] 
**admin_password** | **dict** | The admin password | [optional] 
**session_cookie_values** | [**OtoroshiAuthSessionCookieValues**](OtoroshiAuthSessionCookieValues.md) |  | [optional] 
**data_override** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | Overiddes user data. Object with email as key | [optional] 
**super_admins** | **bool** | This module produces only super admins | [optional] 
**user_base** | **dict** | LDAP user base DN | [optional] 
**server_urls** | **[str]** | LDAP server list of url | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**session_max_age** | **int** | Max age of the session | [optional] 
**admin_username** | **dict** | The admin username | [optional] 
**name** | **str** | Name of the config | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**desc** | **str** | Description of the config | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


