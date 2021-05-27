# openapi_client.LinesApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_services_controller_all_lines**](LinesApi.md#otoroshi_controllers_adminapi_services_controller_all_lines) | **GET** /api/lines | Get all lines of work (prod, preprod, etc)
[**otoroshi_controllers_adminapi_services_controller_services_for_a_line**](LinesApi.md#otoroshi_controllers_adminapi_services_controller_services_for_a_line) | **GET** /api/lines/{line}/services | Get all service for a line of work


# **otoroshi_controllers_adminapi_services_controller_all_lines**
> StringList otoroshi_controllers_adminapi_services_controller_all_lines()

Get all lines of work (prod, preprod, etc)

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import lines_api
from openapi_client.model.string_list import StringList
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
    api_instance = lines_api.LinesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all lines of work (prod, preprod, etc)
        api_response = api_instance.otoroshi_controllers_adminapi_services_controller_all_lines()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LinesApi->otoroshi_controllers_adminapi_services_controller_all_lines: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StringList**](StringList.md)

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

# **otoroshi_controllers_adminapi_services_controller_services_for_a_line**
> ServiceDescriptorList otoroshi_controllers_adminapi_services_controller_services_for_a_line(line)

Get all service for a line of work

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import lines_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.service_descriptor_list import ServiceDescriptorList
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
    api_instance = lines_api.LinesApi(api_client)
    line = "line_example" # str | The line param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Get all service for a line of work
        api_response = api_instance.otoroshi_controllers_adminapi_services_controller_services_for_a_line(line)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LinesApi->otoroshi_controllers_adminapi_services_controller_services_for_a_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line** | **str**| The line param of the target entity |

### Return type

[**ServiceDescriptorList**](ServiceDescriptorList.md)

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

