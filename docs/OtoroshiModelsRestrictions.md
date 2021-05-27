# OtoroshiModelsRestrictions

Http requests restrictions for a service or an apikey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forbidden** | [**[OtoroshiModelsRestrictionPath]**](OtoroshiModelsRestrictionPath.md) | Forbidden paths (return 403) | [optional] 
**allowed** | [**[OtoroshiModelsRestrictionPath]**](OtoroshiModelsRestrictionPath.md) | Allowed paths | [optional] 
**not_found** | [**[OtoroshiModelsRestrictionPath]**](OtoroshiModelsRestrictionPath.md) | Not found paths (return 404) | [optional] 
**allow_last** | **bool** | Evalute allowed paths after everything else | [optional] 
**enabled** | **bool** | Restrictions enabled | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


