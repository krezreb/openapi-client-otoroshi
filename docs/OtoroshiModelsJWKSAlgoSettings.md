# OtoroshiModelsJWKSAlgoSettings

Settings to use keypair from JWKS for verification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Key type | [optional] 
**proxy** | **dict** | Web proxy for http client | [optional] 
**headers** | **{str: (str,)}** | Http header when fetching JWKS | [optional] 
**mtls_config** | [**OtoroshiUtilsHttpMtlsConfig**](OtoroshiUtilsHttpMtlsConfig.md) |  | [optional] 
**type** | **str** | the kind of algosettings | [optional] 
**ttl** | **float** | Cache ttl | [optional] 
**url** | **str** | JWKS url | [optional] 
**timeout** | **float** | Timeout when fetching JWKS | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


