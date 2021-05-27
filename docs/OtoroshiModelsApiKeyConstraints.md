# OtoroshiModelsApiKeyConstraints

Settings used to extract apikeys from http requests and routing traffic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_headers_auth** | [**OtoroshiModelsCustomHeadersAuthConstraints**](OtoroshiModelsCustomHeadersAuthConstraints.md) |  | [optional] 
**routing** | [**OtoroshiModelsApiKeyRouteMatcher**](OtoroshiModelsApiKeyRouteMatcher.md) |  | [optional] 
**client_id_auth** | [**OtoroshiModelsClientIdAuthConstraints**](OtoroshiModelsClientIdAuthConstraints.md) |  | [optional] 
**jwt_auth** | [**OtoroshiModelsJwtAuthConstraints**](OtoroshiModelsJwtAuthConstraints.md) |  | [optional] 
**basic_auth** | [**OtoroshiModelsBasicAuthConstraints**](OtoroshiModelsBasicAuthConstraints.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


