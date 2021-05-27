# OtoroshiAuthAuthModuleConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_max_age** | **int** | Max age of the session | [optional] 
**metadata** | **{str: (str,)}** | Metadata of the SAML module | [optional] 
**session_cookie_values** | [**OtoroshiAuthSessionCookieValues**](OtoroshiAuthSessionCookieValues.md) |  | [optional] 
**basic_auth** | **bool** | Use standard basic auth or web login form | [optional] 
**name** | **str** | Name of the SAML module | [optional] 
**webauthn** | **bool** | Use webauthn for login | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**id** | **str** | Id of the SAML Auth module | [optional] 
**type** | **str** | the type of the module | [optional] 
**users** | [**[OtoroshiAuthBasicAuthUser]**](OtoroshiAuthBasicAuthUser.md) | Users attached to the module | [optional] 
**desc** | **str** | Description of the SAML Auth module | [optional] 
**tags** | **[str]** | SAML module tags | [optional] 
**refresh_tokens** | **bool** | Refresh token support | [optional] 
**token_url** | **str** | OAuth token URL | [optional] 
**mtls_config** | [**OtoroshiUtilsHttpMtlsConfig**](OtoroshiUtilsHttpMtlsConfig.md) |  | [optional] 
**name_field** | **str** | Field name to get name from user profile | [optional] 
**email_field** | **str** | Field name to get email from user profile | [optional] 
**introspection_url** | **str** | URL to introspect access_token | [optional] 
**login_url** | **str** | OAuth login URL | [optional] 
**scope** | **str** | The scope of the token | [optional] 
**rights_override** | [**{str: (OtoroshiModelsUserRights,)}**](OtoroshiModelsUserRights.md) | Overrides user rights of users connected by OAuth1 module | [optional] 
**callback_url** | **str** | Otoroshi callback URL | [optional] 
**client_secret** | **str** | OAuth Client secret | [optional] 
**extra_metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Add metadata to user. Object with email as key | [optional] 
**access_token_field** | **str** | Field name to get access token | [optional] 
**user_info_url** | **str** | OAuth userinfo to get user profile | [optional] 
**client_id** | **str** | OAuth Client id | [optional] 
**use_cookie** | **bool** | Use cookies for redirection | [optional] 
**authorize_url** | **str** | OAuth authorize URL | [optional] 
**data_override** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | Overiddes user data. Object with email as key | [optional] 
**super_admins** | **bool** | This module produces only super admins | [optional] 
**api_key_meta_field** | **str** | Field name to extract apikey metadata | [optional] 
**use_json** | **bool** | Use JSON or URL Form Encoded as payload with the OAuth provider | [optional] 
**api_key_tags_field** | **str** | Field name to extract apikey tags | [optional] 
**otoroshi_data_field** | **str** | Field name to get otoroshi metadata from. You can specify sub fields using | as separator | [optional] 
**jwt_verifier** | **dict** | Algo. settings to verify JWT token | [optional] 
**proxy** | **dict** | Web proxy configuration for the module&#39;s http client | [optional] 
**logout_url** | **str** | OAuth logout URL | [optional] 
**oid_config** | **dict** | URL of the OIDC config. file | [optional] 
**read_profile_from_token** | **bool** | The user profile will be read from the JWT token in id_token | [optional] 
**claims** | **str** | The claims of the token | [optional] 
**group_filters** | [**[OtoroshiAuthGroupFilter]**](OtoroshiAuthGroupFilter.md) | LDAP group filters | [optional] 
**allow_empty_password** | **bool** | Allow empty password access | [optional] 
**search_base** | **str** | LDAP search base | [optional] 
**metadata_field** | **dict** | Field name to get metadata from user profile | [optional] 
**group_rights** | [**{str: (OtoroshiAuthGroupRights,)}**](OtoroshiAuthGroupRights.md) | Rights associated with groups | [optional] 
**search_filter** | **str** | Filter for users | [optional] 
**admin_password** | **dict** | The admin password | [optional] 
**user_base** | **dict** | LDAP user base DN | [optional] 
**server_urls** | **[str]** | LDAP server list of url | [optional] 
**admin_username** | **dict** | The admin username | [optional] 
**profile_url** | **str** | URL fetch by otoroshi to get user information from identity provider | [optional] 
**authorize_url** | **str** | The authorize URL used to initiates the authorization flow that authenticates the user with the Identity Provider | [optional] 
**request_token_url** | **str** | URL fetch to get a request token during the first step of the authorization OAuth 1 flow | [optional] 
**http_method** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Method used to get request and access token | [optional] 
**consumer_secret** | **str** | Client secret obtained from identity provider configuration | [optional] 
**access_token_url** | **str** | Endpoint requested by otoroshi to get access token during the authorization OAuth1 flow | [optional] 
**callback_url** | **str** | The location where the identity provider returns a browser after the user finishes authenticating with their IDP | [optional] 
**consumer_key** | **str** | Client ID obtained on identity provider | [optional] 
**validate_signature** | **bool** | Indicates if SAML response signature has to be validate when otoroshi got SAML responses from identity provider | [optional] 
**sso_protocol_binding** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Protocol binding used during SAML requests | [optional] 
**validating_certificates** | **[str]** | Certificates used to validate SAML response signature | [optional] 
**signature** | [**OtoroshiAuthSAMLSignature**](OtoroshiAuthSAMLSignature.md) |  | [optional] 
**credentials** | [**OtoroshiAuthSAMLCredentials**](OtoroshiAuthSAMLCredentials.md) |  | [optional] 
**validate_assertions** | **bool** | Indicates if assertions have to be validate when otoroshi got SAML responses from identity provider | [optional] 
**issuer** | **str** | Issuer of the SAML requests | [optional] 
**used_name_idas_email** | **bool** | Is name ID used as email ? | [optional] 
**single_logout_url** | **str** | URL used by otoroshi to disconnect users from identity provider | [optional] 
**email_attribute_name** | **dict** | Field name to find email in user profile returned by identity provider | [optional] 
**single_sign_on_url** | **str** | URL used by otoroshi to redirect users to identity provider login page | [optional] 
**name_id_format** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The name ID Format to use for the subject | [optional] 
**single_logout_protocol_binding** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Protocol binding used during SAML requests | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

