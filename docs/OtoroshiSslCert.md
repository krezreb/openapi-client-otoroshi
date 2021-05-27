# OtoroshiSslCert

The otoroshi model for X509 certificates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lets_encrypt** | **bool** | Let&#39;s encrypt (ACME) generated | [optional] 
**keypair** | **bool** | Is cert used for its keypair only ? | [optional] 
**to** | **float** | Stop date | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**exposed** | **bool** | Is the cert exposed (public key exposed in jwks.json) | [optional] 
**auto_renew** | **bool** | Auto renew cert | [optional] 
**id** | **str** | Entity id | [optional] 
**revoked** | **bool** | Certificate is revoked | [optional] 
**_from** | **float** | Start date | [optional] 
**client** | **bool** | Is cert a client cert ? | [optional] 
**ca** | **bool** | Is cert a CA ? | [optional] 
**name** | **str** | Entity name | [optional] 
**chain** | **str** | Certicates chain (PEM encoded) | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**password** | **dict** | Certificate password | [optional] 
**sans** | **[str]** | Certificate SANs | [optional] 
**self_signed** | **bool** | Is cert self signed | [optional] 
**entity_metadata** | **{str: (str,)}** | Entity metadata | [optional] 
**private_key** | **str** | Certificate private key (PEM encoded) | [optional] 
**domain** | **str** | Certificate domain | [optional] 
**ca_ref** | **dict** | Reference to the CA (if any) | [optional] 
**description** | **str** | Entity description | [optional] 
**subject** | **str** | Certificate subject | [optional] 
**valid** | **bool** | Is cert valid | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


