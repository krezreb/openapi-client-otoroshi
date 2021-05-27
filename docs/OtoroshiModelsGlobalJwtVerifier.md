# OtoroshiModelsGlobalJwtVerifier

Otoroshi model for JWT token verifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **{str: (str,)}** | Entity metadata | [optional] 
**algo_settings** | [**OtoroshiModelsAlgoSettings**](OtoroshiModelsAlgoSettings.md) |  | [optional] 
**name** | **str** | Verifier name | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**source** | [**OtoroshiModelsJwtTokenLocation**](OtoroshiModelsJwtTokenLocation.md) |  | [optional] 
**id** | **str** | Verifier id | [optional] 
**type** | **str** | the kind of verifier | [optional] 
**strict** | **bool** | Does it fail if JWT not found | [optional] 
**strategy** | [**OtoroshiModelsVerifierStrategy**](OtoroshiModelsVerifierStrategy.md) |  | [optional] 
**desc** | **str** | Verifier description | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


