# OtoroshiAuthSamlAuthModuleConfig

Configuration of SAML Authentication module

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validate_signature** | **bool** | Indicates if SAML response signature has to be validate when otoroshi got SAML responses from identity provider | [optional] 
**metadata** | **{str: (str,)}** | Metadata of the SAML module | [optional] 
**sso_protocol_binding** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Protocol binding used during SAML requests | [optional] 
**session_cookie_values** | [**OtoroshiAuthSessionCookieValues**](OtoroshiAuthSessionCookieValues.md) |  | [optional] 
**validating_certificates** | **[str]** | Certificates used to validate SAML response signature | [optional] 
**signature** | [**OtoroshiAuthSAMLSignature**](OtoroshiAuthSAMLSignature.md) |  | [optional] 
**credentials** | [**OtoroshiAuthSAMLCredentials**](OtoroshiAuthSAMLCredentials.md) |  | [optional] 
**validate_assertions** | **bool** | Indicates if assertions have to be validate when otoroshi got SAML responses from identity provider | [optional] 
**type** | **str** | the type of the module | [optional] 
**issuer** | **str** | Issuer of the SAML requests | [optional] 
**tags** | **[str]** | SAML module tags | [optional] 
**session_max_age** | **int** | Max age of the session | [optional] 
**used_name_idas_email** | **bool** | Is name ID used as email ? | [optional] 
**single_logout_url** | **str** | URL used by otoroshi to disconnect users from identity provider | [optional] 
**name** | **str** | Name of the SAML module | [optional] 
**email_attribute_name** | **dict** | Field name to find email in user profile returned by identity provider | [optional] 
**single_sign_on_url** | **str** | URL used by otoroshi to redirect users to identity provider login page | [optional] 
**name_id_format** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The name ID Format to use for the subject | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**single_logout_protocol_binding** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Protocol binding used during SAML requests | [optional] 
**id** | **str** | Id of the SAML Auth module | [optional] 
**desc** | **str** | Description of the SAML Auth module | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


