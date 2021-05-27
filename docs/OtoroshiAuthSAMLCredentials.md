# OtoroshiAuthSAMLCredentials

Used to sign, encrypt assertions and sign SAML documents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_key** | [**OtoroshiAuthCredential**](OtoroshiAuthCredential.md) |  | [optional] 
**encryption_key** | [**OtoroshiAuthCredential**](OtoroshiAuthCredential.md) |  | [optional] 
**signed_documents** | **bool** | Indicates if SAML documents have to be sign before sending to identity provider | [optional] 
**encrypted_assertions** | **bool** | Indicates if assertions have to be encrypt before sending to identity provider | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


