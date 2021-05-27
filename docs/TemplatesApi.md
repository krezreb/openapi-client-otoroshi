# openapi_client.TemplatesApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_templates_controller_create_from_template_templates**](TemplatesApi.md#otoroshi_controllers_adminapi_templates_controller_create_from_template_templates) | **POST** /api/{entity}/_template | Creates a new Template from a template
[**otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates**](TemplatesApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates) | **GET** /api/new/apikey | Creates a new ApiKey from a template
[**otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates**](TemplatesApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates) | **GET** /api/new/group | Creates a new ServiceGroup from a template
[**otoroshi_controllers_adminapi_templates_controller_initiate_service_templates**](TemplatesApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_service_templates) | **GET** /api/new/service | Creates a new Service from a template
[**otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates**](TemplatesApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates) | **GET** /api/new/tcp/service | Creates a new TcpService from a template


# **otoroshi_controllers_adminapi_templates_controller_create_from_template_templates**
> Any otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(entity, body)

Creates a new Template from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import templates_api
from openapi_client.model.any import Any
from openapi_client.model.error_response import ErrorResponse
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
    api_instance = templates_api.TemplatesApi(api_client)
    entity = "entity_example" # str | the entity parameter
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Template from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_create_from_template_templates(entity, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemplatesApi->otoroshi_controllers_adminapi_templates_controller_create_from_template_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| the entity parameter |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**Any**](Any.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates**
> OtoroshiModelsApiKey otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates()

Creates a new ApiKey from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import templates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_api_key import OtoroshiModelsApiKey
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new ApiKey from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemplatesApi->otoroshi_controllers_adminapi_templates_controller_initiate_api_key_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsApiKey**](OtoroshiModelsApiKey.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates**
> OtoroshiModelsServiceGroup otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates()

Creates a new ServiceGroup from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import templates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_service_group import OtoroshiModelsServiceGroup
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new ServiceGroup from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemplatesApi->otoroshi_controllers_adminapi_templates_controller_initiate_service_group_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsServiceGroup**](OtoroshiModelsServiceGroup.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_service_templates**
> OtoroshiModelsServiceDescriptor otoroshi_controllers_adminapi_templates_controller_initiate_service_templates()

Creates a new Service from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import templates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_service_descriptor import OtoroshiModelsServiceDescriptor
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new Service from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_service_templates()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemplatesApi->otoroshi_controllers_adminapi_templates_controller_initiate_service_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsServiceDescriptor**](OtoroshiModelsServiceDescriptor.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates()

Creates a new TcpService from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import templates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_tcp_tcp_service import OtoroshiTcpTcpService
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
    api_instance = templates_api.TemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new TcpService from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TemplatesApi->otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)

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

