# OtoroshiModelsPrivateAppsUser

User session for private apps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm** | **str** | Session realm name | [optional] 
**token** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Session tokens (from OAuth) | [optional] 
**expired_at** | **float** | Session expiration date | [optional] 
**profile** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Session user profile | [optional] 
**last_refresh** | **float** | Session last refresh (if OAuth refresh_token supported) | [optional] 
**random_id** | **str** | Session random id | [optional] 
**email** | **str** | Session user email | [optional] 
**created_at** | **float** | Creation date of the session | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**auth_config_id** | **str** | Auth module id that created the session | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**name** | **str** | Entity name | [optional] 
**otoroshi_data** | **dict** | Otoroshi oriented metadata | [optional] 
**metadata** | **{str: (str,)}** | Entity metadata | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


