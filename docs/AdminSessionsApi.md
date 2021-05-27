# openapi_client.AdminSessionsApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_users_controller_discard_all_sessions**](AdminSessionsApi.md#otoroshi_controllers_adminapi_users_controller_discard_all_sessions) | **DELETE** /api/admin-sessions | Discard all admin sessions (otoroshi-ui)
[**otoroshi_controllers_adminapi_users_controller_discard_session**](AdminSessionsApi.md#otoroshi_controllers_adminapi_users_controller_discard_session) | **DELETE** /api/admin-sessions/{id} | Discard a specific admin session (otoroshi-ui)
[**otoroshi_controllers_adminapi_users_controller_sessions**](AdminSessionsApi.md#otoroshi_controllers_adminapi_users_controller_sessions) | **GET** /api/admin-sessions | Returns all admin sessions


# **otoroshi_controllers_adminapi_users_controller_discard_all_sessions**
> Done otoroshi_controllers_adminapi_users_controller_discard_all_sessions()

Discard all admin sessions (otoroshi-ui)

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admin_sessions_api
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
    api_instance = admin_sessions_api.AdminSessionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Discard all admin sessions (otoroshi-ui)
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_discard_all_sessions()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminSessionsApi->otoroshi_controllers_adminapi_users_controller_discard_all_sessions: %s\n" % e)
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

# **otoroshi_controllers_adminapi_users_controller_discard_session**
> Done otoroshi_controllers_adminapi_users_controller_discard_session(id)

Discard a specific admin session (otoroshi-ui)

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admin_sessions_api
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
    api_instance = admin_sessions_api.AdminSessionsApi(api_client)
    id = "id_example" # str | the id parameter

    # example passing only required values which don't have defaults set
    try:
        # Discard a specific admin session (otoroshi-ui)
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_discard_session(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminSessionsApi->otoroshi_controllers_adminapi_users_controller_discard_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the id parameter |

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

# **otoroshi_controllers_adminapi_users_controller_sessions**
> OtoroshiModelsBackOfficeUser otoroshi_controllers_adminapi_users_controller_sessions()

Returns all admin sessions

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admin_sessions_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_back_office_user import OtoroshiModelsBackOfficeUser
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
    api_instance = admin_sessions_api.AdminSessionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all admin sessions
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_sessions()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminSessionsApi->otoroshi_controllers_adminapi_users_controller_sessions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsBackOfficeUser**](OtoroshiModelsBackOfficeUser.md)

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

