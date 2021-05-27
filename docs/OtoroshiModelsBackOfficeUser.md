# OtoroshiModelsBackOfficeUser

User session for otoroshi-ui admins

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**random_id** | **str** | Session user random id | [optional] 
**profile** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Session user profile | [optional] 
**auth_config_id** | **str** | Session created from auth module id | [optional] 
**rights** | [**OtoroshiModelsUserRights**](OtoroshiModelsUserRights.md) |  | [optional] 
**created_at** | **float** | Creation date for the session | [optional] 
**token** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Session tokens (only if OAuth/OIDC) | [optional] 
**name** | **str** | Session user name | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**metadata** | **{str: (str,)}** | Entity metadata | [optional] 
**email** | **str** | User email | [optional] 
**simple_login** | **bool** | Session generated from a simple login module (like basic or ldap) | [optional] 
**expired_at** | **float** | Expiration date for the session | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**last_refresh** | **float** | Last refresh of the session (OAuth with refresh tokens) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


