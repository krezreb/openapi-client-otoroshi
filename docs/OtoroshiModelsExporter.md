# OtoroshiModelsExporter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **[str]** | URLs of the kafka servers | [optional] 
**key_pass** | **dict** | Optional keypass | [optional] 
**mtls_config** | [**OtoroshiUtilsHttpMtlsConfig**](OtoroshiUtilsHttpMtlsConfig.md) |  | [optional] 
**topic** | **str** | Pulsar topic | [optional] 
**truststore** | **dict** | Optional truststore | [optional] 
**keystore** | **dict** | Optional keystore | [optional] 
**send_events** | **bool** | Send events to it, or just connect | [optional] 
**type** | **str** | the kind of mailer | [optional] 
**tls_trust_certs_file_path** | **dict** | Trusted cert path | [optional] 
**namespace** | **str** | Pulsar namespace | [optional] 
**uri** | **str** | Pulsar cluster url | [optional] 
**tenant** | **str** | Pulsar tenant | [optional] 
**cluster_uri** | **str** | Cluster URL | [optional] 
**headers** | **{str: (str,)}** | Sender headers | [optional] 
**password** | **dict** | Elastic password | [optional] 
**index** | **dict** | Index name | [optional] 
**user** | **dict** | Elastic user | [optional] 
**ref** | **str** | Script id | [optional] 
**config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Script config | [optional] 
**path** | **str** | File path | [optional] 
**max_file_size** | **int** | Max file size in bytes | [optional] 
**labels** | **{str: (str,)}** | Exposed labels | [optional] 
**url** | **str** | Sender URL | [optional] 
**to** | [**[OtoroshiUtilsMailerEmailLocation]**](OtoroshiUtilsMailerEmailLocation.md) | Destination email address | [optional] 
**eu** | **bool** | European tenant | [optional] 
**api_key** | **str** | Sendgrid apikey | [optional] 
**domain** | **str** | Mailgun domain | [optional] 
**api_key_private** | **str** | Private key | [optional] 
**api_key_public** | **str** | Public key | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


