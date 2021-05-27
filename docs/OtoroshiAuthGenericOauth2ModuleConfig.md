# OtoroshiAuthGenericOauth2ModuleConfig

Authentication module that works with OAuth2/OIDC

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_tokens** | **bool** | Refresh token support | [optional] 
**metadata** | **{str: (str,)}** | Metadata of the module | [optional] 
**token_url** | **str** | OAuth token URL | [optional] 
**mtls_config** | [**OtoroshiUtilsHttpMtlsConfig**](OtoroshiUtilsHttpMtlsConfig.md) |  | [optional] 
**name_field** | **str** | Field name to get name from user profile | [optional] 
**email_field** | **str** | Field name to get email from user profile | [optional] 
**type** | **str** | the type of the module | [optional] 
**introspection_url** | **str** | URL to introspect access_token | [optional] 
**login_url** | **str** | OAuth login URL | [optional] 
**scope** | **str** | The scope of the token | [optional] 
**rights_override** | [**{str: (OtoroshiModelsUserRights,)}**](OtoroshiModelsUserRights.md) | Overrides user rights. Object with email as key | [optional] 
**callback_url** | **str** | Otoroshi callback URL | [optional] 
**client_secret** | **str** | OAuth Client secret | [optional] 
**id** | **str** | Unique id of the config | [optional] 
**extra_metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Add metadata to user. Object with email as key | [optional] 
**access_token_field** | **str** | Field name to get access token | [optional] 
**user_info_url** | **str** | OAuth userinfo to get user profile | [optional] 
**client_id** | **str** | OAuth Client id | [optional] 
**use_cookie** | **bool** | Use cookies for redirection | [optional] 
**authorize_url** | **str** | OAuth authorize URL | [optional] 
**session_cookie_values** | [**OtoroshiAuthSessionCookieValues**](OtoroshiAuthSessionCookieValues.md) |  | [optional] 
**data_override** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | Overiddes user data. Object with email as key | [optional] 
**super_admins** | **bool** | This module produces only super admins | [optional] 
**api_key_meta_field** | **str** | Field name to extract apikey metadata | [optional] 
**use_json** | **bool** | Use JSON or URL Form Encoded as payload with the OAuth provider | [optional] 
**api_key_tags_field** | **str** | Field name to extract apikey tags | [optional] 
**otoroshi_data_field** | **str** | Field name to get otoroshi metadata from. You can specify sub fields using | as separator | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**jwt_verifier** | **dict** | Algo. settings to verify JWT token | [optional] 
**session_max_age** | **int** | max age for the session cookie in seconds | [optional] 
**proxy** | **dict** | Web proxy configuration for the module&#39;s http client | [optional] 
**logout_url** | **str** | OAuth logout URL | [optional] 
**oid_config** | **dict** | URL of the OIDC config. file | [optional] 
**read_profile_from_token** | **bool** | The user profile will be read from the JWT token in id_token | [optional] 
**name** | **str** | Name of the config | [optional] 
**claims** | **str** | The claims of the token | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**desc** | **str** | Description of the config | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


