# openapi_client.TcpApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action) | **POST** /api/tcp/services/_bulk | Create multiple TcpServices at the same time
[**otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action) | **DELETE** /api/tcp/services/_bulk | Delete multiple TcpServices at the same time
[**otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action) | **PATCH** /api/tcp/services/_bulk | Update (using json-patch) multiple TcpServices at the same time
[**otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action) | **PUT** /api/tcp/services/_bulk | Update multiple TcpServices at the same time
[**otoroshi_controllers_adminapi_tcp_service_api_controller_create_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_create_action) | **POST** /api/tcp/services | Creates a TcpService
[**otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action) | **DELETE** /api/tcp/services/{id} | Deletes a specific TcpService using its id
[**otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action) | **GET** /api/tcp/services | Find all possible TcpServices entities
[**otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action) | **GET** /api/tcp/services/{id} | Find a specific TcpService using its id
[**otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action) | **PATCH** /api/tcp/services/{id} | Updates (using json-patch) a specific TcpService using its id
[**otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action**](TcpApi.md#otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action) | **PUT** /api/tcp/services/{id} | Updates a specific TcpService using its id
[**otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp**](TcpApi.md#otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp) | **POST** /api/tcp/services/_template | Creates a new Template from a template
[**otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp**](TcpApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp) | **GET** /api/tcp/_template | Creates a new TcpService from a template


# **otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(body)

Create multiple TcpServices at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.bulk_response_body import BulkResponseBody
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
    api_instance = tcp_api.TcpApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple TcpServices at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| request body |

### Return type

[**BulkResponseBody**](BulkResponseBody.md)

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action()

Delete multiple TcpServices at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.bulk_response_body import BulkResponseBody
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
    api_instance = tcp_api.TcpApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple TcpServices at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BulkResponseBody**](BulkResponseBody.md)

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(body)

Update (using json-patch) multiple TcpServices at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.bulk_response_body import BulkResponseBody
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
    api_instance = tcp_api.TcpApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple TcpServices at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| request body |

### Return type

[**BulkResponseBody**](BulkResponseBody.md)

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(body)

Update multiple TcpServices at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.bulk_response_body import BulkResponseBody
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
    api_instance = tcp_api.TcpApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple TcpServices at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| request body |

### Return type

[**BulkResponseBody**](BulkResponseBody.md)

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_create_action**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(otoroshi_tcp_tcp_service)

Creates a TcpService

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)
    otoroshi_tcp_tcp_service = OtoroshiTcpTcpService(
        enabled=True,
        description="description_example",
        metadata={
            "key": "key_example",
        },
        port=1,
        tags=[
            "tags_example",
        ],
        rules=[
            OtoroshiTcpTcpRule(
                domain="domain_example",
                targets=[
                    OtoroshiTcpTcpTarget(
                        host="host_example",
                        ip=,
                        port=1,
                        tls=True,
                    ),
                ],
            ),
        ],
        client_auth=OtoroshiSslClientAuth("Need"),
        interface="interface_example",
        sni=OtoroshiTcpSniSettings(
            enabled=True,
            forward_if_no_match=True,
            forwards_to=OtoroshiTcpTcpTarget(
                host="host_example",
                ip=,
                port=1,
                tls=True,
            ),
        ),
        id="id_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        name="name_example",
        tls=OtoroshiTcpTlsMode("Disabled"),
    ) # OtoroshiTcpTcpService | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a TcpService
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(otoroshi_tcp_tcp_service)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_tcp_tcp_service** | [**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)| request body |

### Return type

[**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)

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
**201** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(id)

Deletes a specific TcpService using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific TcpService using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action**
> [OtoroshiTcpTcpService] otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action()

Find all possible TcpServices entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible TcpServices entities
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiTcpTcpService]**](OtoroshiTcpTcpService.md)

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(id)

Find a specific TcpService using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific TcpService using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(id, otoroshi_tcp_tcp_service)

Updates (using json-patch) a specific TcpService using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_tcp_tcp_service = OtoroshiTcpTcpService(
        enabled=True,
        description="description_example",
        metadata={
            "key": "key_example",
        },
        port=1,
        tags=[
            "tags_example",
        ],
        rules=[
            OtoroshiTcpTcpRule(
                domain="domain_example",
                targets=[
                    OtoroshiTcpTcpTarget(
                        host="host_example",
                        ip=,
                        port=1,
                        tls=True,
                    ),
                ],
            ),
        ],
        client_auth=OtoroshiSslClientAuth("Need"),
        interface="interface_example",
        sni=OtoroshiTcpSniSettings(
            enabled=True,
            forward_if_no_match=True,
            forwards_to=OtoroshiTcpTcpTarget(
                host="host_example",
                ip=,
                port=1,
                tls=True,
            ),
        ),
        id="id_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        name="name_example",
        tls=OtoroshiTcpTlsMode("Disabled"),
    ) # OtoroshiTcpTcpService | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific TcpService using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(id, otoroshi_tcp_tcp_service)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_tcp_tcp_service** | [**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)| request body |

### Return type

[**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)

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

# **otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(id, otoroshi_tcp_tcp_service)

Updates a specific TcpService using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_tcp_tcp_service = OtoroshiTcpTcpService(
        enabled=True,
        description="description_example",
        metadata={
            "key": "key_example",
        },
        port=1,
        tags=[
            "tags_example",
        ],
        rules=[
            OtoroshiTcpTcpRule(
                domain="domain_example",
                targets=[
                    OtoroshiTcpTcpTarget(
                        host="host_example",
                        ip=,
                        port=1,
                        tls=True,
                    ),
                ],
            ),
        ],
        client_auth=OtoroshiSslClientAuth("Need"),
        interface="interface_example",
        sni=OtoroshiTcpSniSettings(
            enabled=True,
            forward_if_no_match=True,
            forwards_to=OtoroshiTcpTcpTarget(
                host="host_example",
                ip=,
                port=1,
                tls=True,
            ),
        ),
        id="id_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        name="name_example",
        tls=OtoroshiTcpTlsMode("Disabled"),
    ) # OtoroshiTcpTcpService | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific TcpService using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(id, otoroshi_tcp_tcp_service)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_tcp_tcp_service** | [**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)| request body |

### Return type

[**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)

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

# **otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(body)

Creates a new Template from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Template from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**OtoroshiTcpTcpService**](OtoroshiTcpTcpService.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp**
> OtoroshiTcpTcpService otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp()

Creates a new TcpService from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import tcp_api
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
    api_instance = tcp_api.TcpApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new TcpService from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TcpApi->otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp: %s\n" % e)
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

