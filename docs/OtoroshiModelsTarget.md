# OtoroshiModelsTarget

A target model for a service (destination for forwarded requests)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The host on which the HTTP call will be forwarded. Can be a domain name, or an IP address. Can also have a port | [optional] 
**weight** | **int** | The weight of the target when choosing | [optional] 
**protocol** | **str** | Protocol for the target | [optional] 
**predicate** | [**OtoroshiModelsTargetPredicate**](OtoroshiModelsTargetPredicate.md) |  | [optional] 
**ip_address** | **dict** | Target ip address. Usefull to make manual DNS resolution without breaking SNI | [optional] 
**mtls_config** | [**OtoroshiUtilsHttpMtlsConfig**](OtoroshiUtilsHttpMtlsConfig.md) |  | [optional] 
**scheme** | **str** | The protocol used for communication. Can be http or https | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


