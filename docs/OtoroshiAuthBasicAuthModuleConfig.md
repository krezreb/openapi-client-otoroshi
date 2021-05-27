# OtoroshiAuthBasicAuthModuleConfig

Authentication module that let you use otoroshi as the identity provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_max_age** | **int** | max age for the session cookie in seconds | [optional] 
**metadata** | **{str: (str,)}** | metadata of the module | [optional] 
**session_cookie_values** | [**OtoroshiAuthSessionCookieValues**](OtoroshiAuthSessionCookieValues.md) |  | [optional] 
**basic_auth** | **bool** | Use standard basic auth or web login form | [optional] 
**name** | **str** | name of the module | [optional] 
**webauthn** | **bool** | Use webauthn for login | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**id** | **str** | id of the module | [optional] 
**type** | **str** | the type of the module | [optional] 
**users** | [**[OtoroshiAuthBasicAuthUser]**](OtoroshiAuthBasicAuthUser.md) | Users attached to the module | [optional] 
**desc** | **str** | description of the module | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


