# OtoroshiEventsKafkaConfig

Settings for connection to a kafka cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **[str]** | URLs of the kafka servers | [optional] 
**key_pass** | **dict** | Optional keypass | [optional] 
**mtls_config** | [**OtoroshiUtilsHttpMtlsConfig**](OtoroshiUtilsHttpMtlsConfig.md) |  | [optional] 
**topic** | **str** | Optional kafka topic (otoroshi-events by default) | [optional] 
**truststore** | **dict** | Optional truststore | [optional] 
**keystore** | **dict** | Optional keystore | [optional] 
**send_events** | **bool** | Send events to it, or just connect | [optional] 
**type** | **str** | the kind of exporter | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


