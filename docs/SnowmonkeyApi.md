# openapi_client.SnowmonkeyApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config**](SnowmonkeyApi.md#otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config) | **GET** /api/snowmonkey/config | Get the snowmonkey config
[**otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages**](SnowmonkeyApi.md#otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages) | **GET** /api/snowmonkey/outages | Get the current snowmonkey outages
[**otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey**](SnowmonkeyApi.md#otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey) | **PATCH** /api/snowmonkey/config | Updates (using json-patch) the snowmonkey configuration
[**otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey**](SnowmonkeyApi.md#otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey) | **DELETE** /api/snowmonkey/outages | Reset the snowmonkey outages
[**otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey**](SnowmonkeyApi.md#otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey) | **POST** /api/snowmonkey/_start | Start the snowmonkey of all otoroshi instances
[**otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey**](SnowmonkeyApi.md#otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey) | **POST** /api/snowmonkey/_stop | Stop the snowmonkey of all otoroshi instances
[**otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey**](SnowmonkeyApi.md#otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey) | **PUT** /api/snowmonkey/config | Updates the snowmonkey configuration


# **otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config**
> OtoroshiModelsSnowMonkeyConfig otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config()

Get the snowmonkey config

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import snowmonkey_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
from pprint import pprint
# Defining the host is optional and defaults to http://otoroshi-api.oto.tools:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://otoroshi-api.oto.tools:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: otoroshi_auth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowmonkey_api.SnowmonkeyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the snowmonkey config
        api_response = api_instance.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnowmonkeyApi->otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsSnowMonkeyConfig**](OtoroshiModelsSnowMonkeyConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
**400** | Bad resource format. Take another look to the swagger, or open an issue |  -  |
**404** | Resource not found or does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages**
> OutagesList otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages()

Get the current snowmonkey outages

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import snowmonkey_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.outages_list import OutagesList
from pprint import pprint
# Defining the host is optional and defaults to http://otoroshi-api.oto.tools:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://otoroshi-api.oto.tools:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: otoroshi_auth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowmonkey_api.SnowmonkeyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current snowmonkey outages
        api_response = api_instance.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnowmonkeyApi->otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OutagesList**](OutagesList.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
**400** | Bad resource format. Take another look to the swagger, or open an issue |  -  |
**404** | Resource not found or does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey**
> OtoroshiModelsSnowMonkeyConfig otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(patch_body)

Updates (using json-patch) the snowmonkey configuration

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import snowmonkey_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
from openapi_client.model.patch_body import PatchBody
from pprint import pprint
# Defining the host is optional and defaults to http://otoroshi-api.oto.tools:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://otoroshi-api.oto.tools:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: otoroshi_auth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowmonkey_api.SnowmonkeyApi(api_client)
    patch_body = PatchBody([
        PatchDocument(
            op="add",
            path="path_example",
            value={},
            _from="_from_example",
        ),
    ]) # PatchBody | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) the snowmonkey configuration
        api_response = api_instance.otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(patch_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnowmonkeyApi->otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_body** | [**PatchBody**](PatchBody.md)| request body |

### Return type

[**OtoroshiModelsSnowMonkeyConfig**](OtoroshiModelsSnowMonkeyConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
**400** | Bad resource format. Take another look to the swagger, or open an issue |  -  |
**404** | Resource not found or does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey**
> Done otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey()

Reset the snowmonkey outages

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import snowmonkey_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.done import Done
from pprint import pprint
# Defining the host is optional and defaults to http://otoroshi-api.oto.tools:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://otoroshi-api.oto.tools:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: otoroshi_auth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowmonkey_api.SnowmonkeyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Reset the snowmonkey outages
        api_response = api_instance.otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnowmonkeyApi->otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
**400** | Bad resource format. Take another look to the swagger, or open an issue |  -  |
**404** | Resource not found or does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey**
> Done otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(body)

Start the snowmonkey of all otoroshi instances

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import snowmonkey_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.done import Done
from pprint import pprint
# Defining the host is optional and defaults to http://otoroshi-api.oto.tools:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://otoroshi-api.oto.tools:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: otoroshi_auth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowmonkey_api.SnowmonkeyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Start the snowmonkey of all otoroshi instances
        api_response = api_instance.otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnowmonkeyApi->otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
**400** | Bad resource format. Take another look to the swagger, or open an issue |  -  |
**404** | Resource not found or does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey**
> Done otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(body)

Stop the snowmonkey of all otoroshi instances

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import snowmonkey_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.done import Done
from pprint import pprint
# Defining the host is optional and defaults to http://otoroshi-api.oto.tools:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://otoroshi-api.oto.tools:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: otoroshi_auth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowmonkey_api.SnowmonkeyApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Stop the snowmonkey of all otoroshi instances
        api_response = api_instance.otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnowmonkeyApi->otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
**400** | Bad resource format. Take another look to the swagger, or open an issue |  -  |
**404** | Resource not found or does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey**
> OtoroshiModelsSnowMonkeyConfig otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(otoroshi_models_snow_monkey_config)

Updates the snowmonkey configuration

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import snowmonkey_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
from pprint import pprint
# Defining the host is optional and defaults to http://otoroshi-api.oto.tools:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://otoroshi-api.oto.tools:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: otoroshi_auth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowmonkey_api.SnowmonkeyApi(api_client)
    otoroshi_models_snow_monkey_config = OtoroshiModelsSnowMonkeyConfig(
        dry_run=True,
        outage_duration_to=3.14,
        chaos_config=OtoroshiModelsChaosConfig(
            bad_responses_fault_config=,
            large_request_fault_config=,
            large_response_fault_config=,
            latency_injection_fault_config=,
            enabled=True,
        ),
        times_per_day=1,
        outage_duration_from=3.14,
        start_time="start_time_example",
        include_user_facing_descriptors=True,
        target_groups=[
            "target_groups_example",
        ],
        enabled=True,
        stop_time="stop_time_example",
        outage_strategy=OtoroshiModelsOutageStrategy("AllServicesPerGroup"),
    ) # OtoroshiModelsSnowMonkeyConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates the snowmonkey configuration
        api_response = api_instance.otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(otoroshi_models_snow_monkey_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SnowmonkeyApi->otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_snow_monkey_config** | [**OtoroshiModelsSnowMonkeyConfig**](OtoroshiModelsSnowMonkeyConfig.md)| request body |

### Return type

[**OtoroshiModelsSnowMonkeyConfig**](OtoroshiModelsSnowMonkeyConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
**400** | Bad resource format. Take another look to the swagger, or open an issue |  -  |
**404** | Resource not found or does not exist |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

