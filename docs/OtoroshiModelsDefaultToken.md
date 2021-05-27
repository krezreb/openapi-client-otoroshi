# OtoroshiModelsDefaultToken

Default jwt token when no other token validated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_settings** | [**OtoroshiModelsVerificationSettings**](OtoroshiModelsVerificationSettings.md) |  | [optional] 
**type** | **str** | the kind of strategy | [optional] 
**strict** | **bool** | If the token already exists in the request, then fail | [optional] 
**token** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The default token | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


