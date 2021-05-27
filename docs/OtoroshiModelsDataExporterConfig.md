# OtoroshiModelsDataExporterConfig

Module to export otoroshi specific events to whatever destination you want

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** | Description | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**buffer_size** | **int** | buffer size | [optional] 
**json_workers** | **int** | nb workers | [optional] 
**group_duration** | **float** | duration | [optional] 
**group_size** | **int** | Group size | [optional] 
**typ** | [**OtoroshiModelsDataExporterConfigType**](OtoroshiModelsDataExporterConfigType.md) |  | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**send_workers** | **int** | send workers | [optional] 
**id** | **str** | Id | [optional] 
**name** | **str** | Name | [optional] 
**metadata** | **{str: (str,)}** | Metadata | [optional] 
**config** | [**OtoroshiModelsExporter**](OtoroshiModelsExporter.md) |  | [optional] 
**projection** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | projection | [optional] 
**enabled** | **bool** | Boolean | [optional] 
**filtering** | [**OtoroshiModelsDataExporterConfigFiltering**](OtoroshiModelsDataExporterConfigFiltering.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


