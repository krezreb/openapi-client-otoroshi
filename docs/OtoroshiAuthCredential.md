# OtoroshiAuthCredential

Pair of raw certificate, private key and certId for SAML protocol

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **dict** | PEM certificate used to sign SAML requests send to identity provider | [optional] 
**private_key** | **dict** | Private key of the certificate used to sign SAML requests send to identity provider | [optional] 
**cert_id** | **dict** | Id of the certificate used to sign SAML requests send to identity provider | [optional] 
**use_otoroshi_certificate** | **bool** | Indicates if SAML requests are signed with otoroshi certificate or a PEM certificate | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


