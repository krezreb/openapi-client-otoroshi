# OtoroshiSslPkiModelsGenCsrQuery

Settings for generating a certificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | **bool** | Is cert client ? | [optional] 
**hosts** | **[str]** | Certificate SANs | [optional] 
**key** | [**OtoroshiSslPkiModelsGenKeyPairQuery**](OtoroshiSslPkiModelsGenKeyPairQuery.md) |  | [optional] 
**include_aia** | **bool** | Include AIA extension (if generated from otoroshi CA) | [optional] 
**signature_alg** | **str** | Signature algorithm | [optional] 
**existing_serial_number** | **dict** |  | [optional] 
**duration** | **float** | Certificate lifespan | [optional] 
**digest_alg** | **str** | Digest algo | [optional] 
**ca** | **bool** | Is cert ca ? | [optional] 
**name** | **{str: (str,)}** | Certificate name | [optional] 
**subject** | **dict** | Certificate subject | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


