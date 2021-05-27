# openapi_client.GroupsApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_analytics_controller_group_status**](GroupsApi.md#otoroshi_controllers_adminapi_analytics_controller_group_status) | **GET** /api/groups/{groupId}/status | Statis for a group of services over time
[**otoroshi_controllers_adminapi_service_group_controller_bulk_create_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_bulk_create_action) | **POST** /api/groups/_bulk | Create multiple ServiceGroups at the same time
[**otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action) | **DELETE** /api/groups/_bulk | Delete multiple ServiceGroups at the same time
[**otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action) | **PATCH** /api/groups/_bulk | Update (using json-patch) multiple ServiceGroups at the same time
[**otoroshi_controllers_adminapi_service_group_controller_bulk_update_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_bulk_update_action) | **PUT** /api/groups/_bulk | Update multiple ServiceGroups at the same time
[**otoroshi_controllers_adminapi_service_group_controller_create_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_create_action) | **POST** /api/groups | Creates a ServiceGroup
[**otoroshi_controllers_adminapi_service_group_controller_delete_entity_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_delete_entity_action) | **DELETE** /api/groups/{id} | Deletes a specific ServiceGroup using its id
[**otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action) | **GET** /api/groups | Find all possible ServiceGroups entities
[**otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action) | **GET** /api/groups/{id} | Find a specific ServiceGroup using its id
[**otoroshi_controllers_adminapi_service_group_controller_patch_entity_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_patch_entity_action) | **PATCH** /api/groups/{id} | Updates (using json-patch) a specific ServiceGroup using its id
[**otoroshi_controllers_adminapi_service_group_controller_service_group_services**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_service_group_services) | **GET** /api/groups/{id}/services | Get the services from a service group
[**otoroshi_controllers_adminapi_service_group_controller_update_entity_action**](GroupsApi.md#otoroshi_controllers_adminapi_service_group_controller_update_entity_action) | **PUT** /api/groups/{id} | Updates a specific ServiceGroup using its id
[**otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups**](GroupsApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups) | **GET** /api/groups/_template | Creates a new ServiceGroup from a template


# **otoroshi_controllers_adminapi_analytics_controller_group_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_analytics_controller_group_status(group_id)

Statis for a group of services over time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = "groupId_example" # str | the groupId parameter

    # example passing only required values which don't have defaults set
    try:
        # Statis for a group of services over time
        api_response = api_instance.otoroshi_controllers_adminapi_analytics_controller_group_status(group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_analytics_controller_group_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| the groupId parameter |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **otoroshi_controllers_adminapi_service_group_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(body)

Create multiple ServiceGroups at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple ServiceGroups at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action()

Delete multiple ServiceGroups at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple ServiceGroups at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(body)

Update (using json-patch) multiple ServiceGroups at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple ServiceGroups at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_service_group_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(body)

Update multiple ServiceGroups at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple ServiceGroups at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_service_group_controller_create_action**
> OtoroshiModelsServiceGroup otoroshi_controllers_adminapi_service_group_controller_create_action(otoroshi_models_service_group)

Creates a ServiceGroup

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    otoroshi_models_service_group = OtoroshiModelsServiceGroup(
        id="id_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        name="name_example",
        metadata={
            "key": "key_example",
        },
        description="description_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsServiceGroup | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a ServiceGroup
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_create_action(otoroshi_models_service_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_service_group** | [**OtoroshiModelsServiceGroup**](OtoroshiModelsServiceGroup.md)| request body |

### Return type

[**OtoroshiModelsServiceGroup**](OtoroshiModelsServiceGroup.md)

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

# **otoroshi_controllers_adminapi_service_group_controller_delete_entity_action**
> OtoroshiModelsServiceGroup otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(id)

Deletes a specific ServiceGroup using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific ServiceGroup using its id
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

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

# **otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action**
> [OtoroshiModelsServiceGroup] otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action()

Find all possible ServiceGroups entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible ServiceGroups entities
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiModelsServiceGroup]**](OtoroshiModelsServiceGroup.md)

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

# **otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action**
> OtoroshiModelsServiceGroup otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(id)

Find a specific ServiceGroup using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific ServiceGroup using its id
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

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

# **otoroshi_controllers_adminapi_service_group_controller_patch_entity_action**
> OtoroshiModelsServiceGroup otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(id, otoroshi_models_service_group)

Updates (using json-patch) a specific ServiceGroup using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_service_group = OtoroshiModelsServiceGroup(
        id="id_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        name="name_example",
        metadata={
            "key": "key_example",
        },
        description="description_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsServiceGroup | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific ServiceGroup using its id
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(id, otoroshi_models_service_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_service_group** | [**OtoroshiModelsServiceGroup**](OtoroshiModelsServiceGroup.md)| request body |

### Return type

[**OtoroshiModelsServiceGroup**](OtoroshiModelsServiceGroup.md)

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

# **otoroshi_controllers_adminapi_service_group_controller_service_group_services**
> ServiceDescriptorList otoroshi_controllers_adminapi_service_group_controller_service_group_services(id)

Get the services from a service group

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Get the services from a service group
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_service_group_services(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_service_group_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

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

# **otoroshi_controllers_adminapi_service_group_controller_update_entity_action**
> OtoroshiModelsServiceGroup otoroshi_controllers_adminapi_service_group_controller_update_entity_action(id, otoroshi_models_service_group)

Updates a specific ServiceGroup using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_service_group = OtoroshiModelsServiceGroup(
        id="id_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        name="name_example",
        metadata={
            "key": "key_example",
        },
        description="description_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsServiceGroup | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific ServiceGroup using its id
        api_response = api_instance.otoroshi_controllers_adminapi_service_group_controller_update_entity_action(id, otoroshi_models_service_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_service_group_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_service_group** | [**OtoroshiModelsServiceGroup**](OtoroshiModelsServiceGroup.md)| request body |

### Return type

[**OtoroshiModelsServiceGroup**](OtoroshiModelsServiceGroup.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups**
> OtoroshiModelsServiceGroup otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups()

Creates a new ServiceGroup from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new ServiceGroup from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GroupsApi->otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups: %s\n" % e)
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

