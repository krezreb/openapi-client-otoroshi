# OtoroshiModelsCustomTimeouts

Settings for custom timeouts for a specific path

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | path on which this configuration works | [optional] 
**call_and_stream_timeout** | **int** | Specify how long each call should last at most in milliseconds (hard timeout, connection will be closed after that duration) | [optional] 
**call_timeout** | **int** | Specify how long each call should last at most in milliseconds (soft timeout as it&#39;s enforced by the circuit breaker) | [optional] 
**idle_timeout** | **int** | Timeout on idle connection | [optional] 
**global_timeout** | **int** | Specify how long the global call (with retries) should last at most in milliseconds | [optional] 
**connection_timeout** | **int** | Timeout at connection | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


