# OtoroshiModelsClientConfig

Settings for the http client when http request is forwarded

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_timeout** | **int** | Timeout at connection | [optional] 
**use_circuit_breaker** | **bool** | Use a circuit breaker to avoid cascading failure when calling chains of services. Highly recommended ! | [optional] 
**retry_initial_delay** | **int** | Specify the delay between two retries. Each retry, the delay is multiplied by the backoff factor | [optional] 
**proxy** | **dict** | Web proxy settings for http client | [optional] 
**call_timeout** | **int** | Specify how long each call should last at most in milliseconds (soft timeout as it&#39;s enforced by the circuit breaker) | [optional] 
**call_and_stream_timeout** | **int** | Specify how long each call should last at most in milliseconds (hard timeout, connection will be closed after that duration) | [optional] 
**global_timeout** | **int** | Specify how long the global call (with retries) should last at most in milliseconds | [optional] 
**max_errors** | **int** | Specify how many errors can pass before opening the circuit breaker | [optional] 
**retries** | **int** | Specify how many times the client will try to fetch the result of the request after an error before giving up. | [optional] 
**backoff_factor** | **int** | Specify the factor to multiply the delay for each retry | [optional] 
**custom_timeouts** | [**[OtoroshiModelsCustomTimeouts]**](OtoroshiModelsCustomTimeouts.md) | Custom timeouts per path | [optional] 
**idle_timeout** | **int** | Timeout on idle connection | [optional] 
**sample_interval** | **int** | Specify the sliding window time for the circuit breaker in milliseconds, after this time, error count will be reseted | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


