# OtoroshiAuthBasicAuthUser

A user model for the BasicAuthModuleConfig module

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | User metadata | [optional] 
**password** | **str** | User password (bcrypt hashed) | [optional] 
**email** | **str** | User email | [optional] 
**webauthn** | **dict** | Webauthn details | [optional] 
**rights** | [**OtoroshiModelsUserRights**](OtoroshiModelsUserRights.md) |  | [optional] 
**name** | **str** | User name | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


