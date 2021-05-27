# OtoroshiModelsAlgoSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **dict** | Private key (for signing) | [optional] 
**size** | **int** | SHA function size | [optional] 
**public_key** | **str** | Public key (for verification) | [optional] 
**type** | **str** | the kind of algosettings | [optional] 
**cert_id** | **str** | Certificate id | [optional] 
**base64** | **bool** | The secret is base64 encoded | [optional] 
**secret** | **str** | HMAC secret | [optional] 
**kty** | **str** | Key type | [optional] 
**proxy** | **dict** | Web proxy for http client | [optional] 
**headers** | **{str: (str,)}** | Http header when fetching JWKS | [optional] 
**mtls_config** | [**OtoroshiUtilsHttpMtlsConfig**](OtoroshiUtilsHttpMtlsConfig.md) |  | [optional] 
**ttl** | **float** | Cache ttl | [optional] 
**url** | **str** | JWKS url | [optional] 
**timeout** | **float** | Timeout when fetching JWKS | [optional] 
**only_exposed_certs** | **bool** | Use only exposed certs | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


