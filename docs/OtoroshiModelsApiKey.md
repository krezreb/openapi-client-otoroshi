# OtoroshiModelsApiKey

An otoroshi apikey that can allow you to access some services

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_quota** | **int** | Authorized number of calls per day | [optional] 
**metadata** | **{str: (str,)}** | Bunch of metadata for the key | [optional] 
**throttling_quota** | **int** | Authorized number of calls per second, measured on 10 seconds | [optional] 
**constrained_services_only** | **bool** | This apikey can only be used on services that constrained their apikey routing | [optional] 
**allow_client_id_only** | **bool** | This apikey can be used juste with the client_id value | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**restrictions** | [**OtoroshiModelsRestrictions**](OtoroshiModelsRestrictions.md) |  | [optional] 
**tags** | **[str]** | Apikey tags | [optional] 
**enabled** | **bool** | Whether or not the key is enabled. If disabled, resources won&#39;t be available to calls using this key | [optional] 
**read_only** | **bool** | The apikey only allow access for GET, HEAD and OPTIONS verbs | [optional] 
**client_secret** | **str** | The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything | [optional] 
**valid_until** | **dict** | Date until when the apikey is valid | [optional] 
**client_name** | **str** | The name of the api key, for humans ;-) | [optional] 
**monthly_quota** | **int** | Authorized number of calls per month | [optional] 
**description** | **str** | Description of this apikey | [optional] 
**rotation** | [**OtoroshiModelsApiKeyRotation**](OtoroshiModelsApiKeyRotation.md) |  | [optional] 
**authorized_entities** | [**[OtoroshiModelsEntityIdentifier]**](OtoroshiModelsEntityIdentifier.md) | The group/service ids (prefixed by group_ or service_ on which the key is authorized | [optional] 
**client_id** | **str** | The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


