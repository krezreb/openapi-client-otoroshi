# OtoroshiTcpTcpService

Model for a TCP proxy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Service enabled | [optional] 
**description** | **str** | Entity description | [optional] 
**metadata** | **{str: (str,)}** | Entity metadata | [optional] 
**port** | **int** | network port | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**rules** | [**[OtoroshiTcpTcpRule]**](OtoroshiTcpTcpRule.md) | Routing rules | [optional] 
**client_auth** | [**OtoroshiSslClientAuth**](OtoroshiSslClientAuth.md) |  | [optional] 
**interface** | **str** | Network interface | [optional] 
**sni** | [**OtoroshiTcpSniSettings**](OtoroshiTcpSniSettings.md) |  | [optional] 
**id** | **str** | Entity id | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**name** | **str** | Entity name | [optional] 
**tls** | [**OtoroshiTcpTlsMode**](OtoroshiTcpTlsMode.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


