# openapi_client.AuthModulesApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action) | **POST** /api/auths/_bulk | Create multiple AuthModuleConfigs at the same time
[**otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action) | **DELETE** /api/auths/_bulk | Delete multiple AuthModuleConfigs at the same time
[**otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action) | **PATCH** /api/auths/_bulk | Update (using json-patch) multiple AuthModuleConfigs at the same time
[**otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action) | **PUT** /api/auths/_bulk | Update multiple AuthModuleConfigs at the same time
[**otoroshi_controllers_adminapi_auth_modules_controller_create_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_create_action) | **POST** /api/auths | Creates a AuthModuleConfig
[**otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action) | **DELETE** /api/auths/{id} | Deletes a specific AuthModuleConfig using its id
[**otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action) | **GET** /api/auths | Find all possible AuthModuleConfigs entities
[**otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action) | **GET** /api/auths/{id} | Find a specific AuthModuleConfig using its id
[**otoroshi_controllers_adminapi_auth_modules_controller_finish_registration**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_finish_registration) | **POST** /api/auths/{id}/register/finish | Finishes the registration of a user
[**otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action) | **PATCH** /api/auths/{id} | Updates (using json-patch) a specific AuthModuleConfig using its id
[**otoroshi_controllers_adminapi_auth_modules_controller_start_registration**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_start_registration) | **POST** /api/auths/{id}/register/start | Stats the registration of a user
[**otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action**](AuthModulesApi.md#otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action) | **PUT** /api/auths/{id} | Updates a specific AuthModuleConfig using its id
[**otoroshi_controllers_adminapi_templates_controller_initiate_auth_module**](AuthModulesApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_auth_module) | **GET** /api/auths/_template | Creates a new AuthModule from a template


# **otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(body)

Create multiple AuthModuleConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple AuthModuleConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action()

Delete multiple AuthModuleConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple AuthModuleConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(body)

Update (using json-patch) multiple AuthModuleConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple AuthModuleConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(body)

Update multiple AuthModuleConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple AuthModuleConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_auth_modules_controller_create_action**
> OtoroshiAuthAuthModuleConfig otoroshi_controllers_adminapi_auth_modules_controller_create_action(otoroshi_auth_auth_module_config)

Creates a AuthModuleConfig

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    otoroshi_auth_auth_module_config = OtoroshiAuthAuthModuleConfig() # OtoroshiAuthAuthModuleConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a AuthModuleConfig
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_create_action(otoroshi_auth_auth_module_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_auth_auth_module_config** | [**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)| request body |

### Return type

[**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)

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

# **otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action**
> OtoroshiAuthAuthModuleConfig otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(id)

Deletes a specific AuthModuleConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific AuthModuleConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)

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

# **otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action**
> [OtoroshiAuthAuthModuleConfig] otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action()

Find all possible AuthModuleConfigs entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible AuthModuleConfigs entities
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiAuthAuthModuleConfig]**](OtoroshiAuthAuthModuleConfig.md)

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

# **otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action**
> OtoroshiAuthAuthModuleConfig otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(id)

Find a specific AuthModuleConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific AuthModuleConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)

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

# **otoroshi_controllers_adminapi_auth_modules_controller_finish_registration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(id, body)

Finishes the registration of a user

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    id = "id_example" # str | The id param of the target entity
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Finishes the registration of a user
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_finish_registration(id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_finish_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action**
> OtoroshiAuthAuthModuleConfig otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(id, otoroshi_auth_auth_module_config)

Updates (using json-patch) a specific AuthModuleConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_auth_auth_module_config = OtoroshiAuthAuthModuleConfig() # OtoroshiAuthAuthModuleConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific AuthModuleConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action(id, otoroshi_auth_auth_module_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_auth_auth_module_config** | [**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)| request body |

### Return type

[**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)

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

# **otoroshi_controllers_adminapi_auth_modules_controller_start_registration**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_auth_modules_controller_start_registration(id, body)

Stats the registration of a user

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    id = "id_example" # str | The id param of the target entity
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Stats the registration of a user
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_start_registration(id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_start_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action**
> OtoroshiAuthAuthModuleConfig otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(id, otoroshi_auth_auth_module_config)

Updates a specific AuthModuleConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_auth_auth_module_config = OtoroshiAuthAuthModuleConfig() # OtoroshiAuthAuthModuleConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific AuthModuleConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action(id, otoroshi_auth_auth_module_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_auth_modules_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_auth_auth_module_config** | [**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)| request body |

### Return type

[**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_auth_module**
> OtoroshiAuthAuthModuleConfig otoroshi_controllers_adminapi_templates_controller_initiate_auth_module()

Creates a new AuthModule from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import auth_modules_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_auth_auth_module_config import OtoroshiAuthAuthModuleConfig
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
    api_instance = auth_modules_api.AuthModulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new AuthModule from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_auth_module()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthModulesApi->otoroshi_controllers_adminapi_templates_controller_initiate_auth_module: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiAuthAuthModuleConfig**](OtoroshiAuthAuthModuleConfig.md)

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

