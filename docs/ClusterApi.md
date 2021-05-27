# openapi_client.ClusterApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members) | **DELETE** /api/cluster/members | Clear cluster members from members statistics
[**otoroshi_controllers_adminapi_cluster_controller_create_login_token**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_create_login_token) | **POST** /api/cluster/login-tokens/{id} | Api to create a distributed login token between worker and leader
[**otoroshi_controllers_adminapi_cluster_controller_create_session**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_create_session) | **POST** /api/cluster/sessions | Api to create a distributed private apps session between worker and leader
[**otoroshi_controllers_adminapi_cluster_controller_get_cluster_members**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_get_cluster_members) | **GET** /api/cluster/members | Get cluster members statistics
[**otoroshi_controllers_adminapi_cluster_controller_get_user_token**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_get_user_token) | **GET** /api/cluster/user-tokens/{id} | Api to get a distributed login token between worker and leader
[**otoroshi_controllers_adminapi_cluster_controller_internal_state**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_internal_state) | **GET** /api/cluster/state | Api to get internal state from a leader
[**otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid) | **GET** /api/cluster/login-tokens/{id} | Api to check a distributed login token between worker and leader
[**otoroshi_controllers_adminapi_cluster_controller_is_session_valid**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_is_session_valid) | **GET** /api/cluster/sessions/{id} | Api to create a distributed private apps session between worker and leader
[**otoroshi_controllers_adminapi_cluster_controller_live_cluster**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_live_cluster) | **GET** /api/cluster/live | Api to get cluster statistics
[**otoroshi_controllers_adminapi_cluster_controller_set_user_token**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_set_user_token) | **POST** /api/cluster/user-tokens | Api to set a distributed login token between worker and leader
[**otoroshi_controllers_adminapi_cluster_controller_update_quotas**](ClusterApi.md#otoroshi_controllers_adminapi_cluster_controller_update_quotas) | **PUT** /api/cluster/quotas | Api to push quotas usage from a worker to a leader


# **otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members**
> Done otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members()

Clear cluster members from members statistics

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
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
    api_instance = cluster_api.ClusterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear cluster members from members statistics
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_clear_cluster_members: %s\n" % e)
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

# **otoroshi_controllers_adminapi_cluster_controller_create_login_token**
> TokenResponse otoroshi_controllers_adminapi_cluster_controller_create_login_token(id, body)

Api to create a distributed login token between worker and leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.token_response import TokenResponse
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
    api_instance = cluster_api.ClusterApi(api_client)
    id = "id_example" # str | the id parameter
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Api to create a distributed login token between worker and leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_create_login_token(id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_create_login_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the id parameter |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_create_session**
> OtoroshiModelsPrivateAppsUser otoroshi_controllers_adminapi_cluster_controller_create_session(otoroshi_models_private_apps_user)

Api to create a distributed private apps session between worker and leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_private_apps_user import OtoroshiModelsPrivateAppsUser
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
    api_instance = cluster_api.ClusterApi(api_client)
    otoroshi_models_private_apps_user = OtoroshiModelsPrivateAppsUser(
        realm="realm_example",
        token={},
        expired_at=3.14,
        profile={},
        last_refresh=3.14,
        random_id="random_id_example",
        email="email_example",
        created_at=3.14,
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        auth_config_id="auth_config_id_example",
        tags=[
            "tags_example",
        ],
        name="name_example",
        otoroshi_data=,
        metadata={
            "key": "key_example",
        },
    ) # OtoroshiModelsPrivateAppsUser | request body

    # example passing only required values which don't have defaults set
    try:
        # Api to create a distributed private apps session between worker and leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_create_session(otoroshi_models_private_apps_user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_create_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_private_apps_user** | [**OtoroshiModelsPrivateAppsUser**](OtoroshiModelsPrivateAppsUser.md)| request body |

### Return type

[**OtoroshiModelsPrivateAppsUser**](OtoroshiModelsPrivateAppsUser.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_get_cluster_members**
> Any otoroshi_controllers_adminapi_cluster_controller_get_cluster_members()

Get cluster members statistics

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
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
    api_instance = cluster_api.ClusterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster members statistics
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_get_cluster_members()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_get_cluster_members: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Any**](Any.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_get_user_token**
> TokenResponse otoroshi_controllers_adminapi_cluster_controller_get_user_token(id)

Api to get a distributed login token between worker and leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.token_response import TokenResponse
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
    api_instance = cluster_api.ClusterApi(api_client)
    id = "id_example" # str | the id parameter

    # example passing only required values which don't have defaults set
    try:
        # Api to get a distributed login token between worker and leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_get_user_token(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_get_user_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the id parameter |

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_internal_state**
> Any otoroshi_controllers_adminapi_cluster_controller_internal_state()

Api to get internal state from a leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
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
    api_instance = cluster_api.ClusterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Api to get internal state from a leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_internal_state()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_internal_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Any**](Any.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid**
> TokenResponse otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(id)

Api to check a distributed login token between worker and leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.token_response import TokenResponse
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
    api_instance = cluster_api.ClusterApi(api_client)
    id = "id_example" # str | the id parameter

    # example passing only required values which don't have defaults set
    try:
        # Api to check a distributed login token between worker and leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_is_login_token_valid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the id parameter |

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_is_session_valid**
> OtoroshiModelsPrivateAppsUser otoroshi_controllers_adminapi_cluster_controller_is_session_valid(id)

Api to create a distributed private apps session between worker and leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_private_apps_user import OtoroshiModelsPrivateAppsUser
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
    api_instance = cluster_api.ClusterApi(api_client)
    id = "id_example" # str | the id parameter

    # example passing only required values which don't have defaults set
    try:
        # Api to create a distributed private apps session between worker and leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_is_session_valid(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_is_session_valid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the id parameter |

### Return type

[**OtoroshiModelsPrivateAppsUser**](OtoroshiModelsPrivateAppsUser.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_live_cluster**
> Any otoroshi_controllers_adminapi_cluster_controller_live_cluster()

Api to get cluster statistics

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
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
    api_instance = cluster_api.ClusterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Api to get cluster statistics
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_live_cluster()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_live_cluster: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Any**](Any.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_set_user_token**
> TokenResponse otoroshi_controllers_adminapi_cluster_controller_set_user_token(user_token_body)

Api to set a distributed login token between worker and leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.user_token_body import UserTokenBody
from openapi_client.model.token_response import TokenResponse
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
    api_instance = cluster_api.ClusterApi(api_client)
    user_token_body = UserTokenBody(
        token="token_example",
    ) # UserTokenBody | request body

    # example passing only required values which don't have defaults set
    try:
        # Api to set a distributed login token between worker and leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_set_user_token(user_token_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_set_user_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token_body** | [**UserTokenBody**](UserTokenBody.md)| request body |

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **otoroshi_controllers_adminapi_cluster_controller_update_quotas**
> Done otoroshi_controllers_adminapi_cluster_controller_update_quotas(body)

Api to push quotas usage from a worker to a leader

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import cluster_api
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
    api_instance = cluster_api.ClusterApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Api to push quotas usage from a worker to a leader
        api_response = api_instance.otoroshi_controllers_adminapi_cluster_controller_update_quotas(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterApi->otoroshi_controllers_adminapi_cluster_controller_update_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| request body |

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

