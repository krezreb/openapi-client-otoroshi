# OtoroshiModelsCanary

Settings for canary routing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Use canary mode for this service | [optional] 
**traffic** | **float** | Ratio of traffic that will be sent to canary targets. | [optional] 
**targets** | [**[OtoroshiModelsTarget]**](OtoroshiModelsTarget.md) | The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures | [optional] 
**root** | **str** | Otoroshi will append this root to any target choosen. If the specified root is &#39;/api/foo&#39;, then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


