# OtoroshiModelsApiKeyRotation

Settings for automatic apikey rotation with grace period

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Rotation enabled | [optional] 
**rotation_every** | **int** | Rotate every n hours | [optional] 
**grace_period** | **int** | period (in hours) during which both secrets works | [optional] 
**next_secret** | **dict** | Next client_secret value | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


