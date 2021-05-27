# OtoroshiModelsSnowMonkeyConfig

Settings for the snow monkey (chaos engineering)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Whether or not outages will actualy impact requests | [optional] 
**outage_duration_to** | **float** | End of outage duration range | [optional] 
**chaos_config** | [**OtoroshiModelsChaosConfig**](OtoroshiModelsChaosConfig.md) |  | [optional] 
**times_per_day** | **int** | Number of time per day each service will be outage | [optional] 
**outage_duration_from** | **float** | Start of outage duration range | [optional] 
**start_time** | **str** | Start time of Snow Monkey each day | [optional] 
**include_user_facing_descriptors** | **bool** | Whether or not user facing apps. will be impacted by Snow Monkey | [optional] 
**target_groups** | **[str]** | Groups impacted by Snow Monkey. If empty, all groups will be impacted | [optional] 
**enabled** | **bool** | Whether or not this config is enabled | [optional] 
**stop_time** | **str** | Stop time of Snow Monkey each day | [optional] 
**outage_strategy** | [**OtoroshiModelsOutageStrategy**](OtoroshiModelsOutageStrategy.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


