# OtoroshiModelsWebAuthnOtoroshiAdmin

An otoroshi admin user that uses webauthn at login

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **float** | User creation date | [optional] 
**metadata** | **{str: (str,)}** | Entity metadata | [optional] 
**password** | **str** | User password | [optional] 
**credentials** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | User webauthn credentials | [optional] 
**rights** | [**OtoroshiModelsUserRights**](OtoroshiModelsUserRights.md) |  | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**typ** | [**OtoroshiModelsOtoroshiAdminType**](OtoroshiModelsOtoroshiAdminType.md) |  | [optional] 
**handle** | **str** | User webauthn handle | [optional] 
**label** | **str** | User label | [optional] 
**type** | **str** | the kind of admin | [optional] 
**username** | **str** | User username | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


