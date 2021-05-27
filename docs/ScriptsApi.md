# openapi_client.ScriptsApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_script_api_controller_bulk_create_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_bulk_create_action) | **POST** /api/scripts/_bulk | Create multiple otoroshi.script.Scripts at the same time
[**otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action) | **DELETE** /api/scripts/_bulk | Delete multiple otoroshi.script.Scripts at the same time
[**otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action) | **PATCH** /api/scripts/_bulk | Update (using json-patch) multiple otoroshi.script.Scripts at the same time
[**otoroshi_controllers_adminapi_script_api_controller_bulk_update_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_bulk_update_action) | **PUT** /api/scripts/_bulk | Update multiple otoroshi.script.Scripts at the same time
[**otoroshi_controllers_adminapi_script_api_controller_compile_script**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_compile_script) | **POST** /api/scripts/_compile | Trigger script compilation of the server
[**otoroshi_controllers_adminapi_script_api_controller_create_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_create_action) | **POST** /api/scripts | Creates a otoroshi.script.Script
[**otoroshi_controllers_adminapi_script_api_controller_delete_entity_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_delete_entity_action) | **DELETE** /api/scripts/{id} | Deletes a specific otoroshi.script.Script using its id
[**otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action) | **GET** /api/scripts | Find all possible otoroshi.script.Scripts entities
[**otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list) | **GET** /api/scripts/_list | Search plugins based on type of plugin
[**otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action) | **GET** /api/scripts/{id} | Find a specific otoroshi.script.Script using its id
[**otoroshi_controllers_adminapi_script_api_controller_patch_entity_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_patch_entity_action) | **PATCH** /api/scripts/{id} | Updates (using json-patch) a specific otoroshi.script.Script using its id
[**otoroshi_controllers_adminapi_script_api_controller_update_entity_action**](ScriptsApi.md#otoroshi_controllers_adminapi_script_api_controller_update_entity_action) | **PUT** /api/scripts/{id} | Updates a specific otoroshi.script.Script using its id
[**otoroshi_controllers_adminapi_templates_controller_initiate_script**](ScriptsApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_script) | **GET** /api/scripts/_template | Creates a new Script from a template


# **otoroshi_controllers_adminapi_script_api_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(body)

Create multiple otoroshi.script.Scripts at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
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
    api_instance = scripts_api.ScriptsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple otoroshi.script.Scripts at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action()

Delete multiple otoroshi.script.Scripts at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
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
    api_instance = scripts_api.ScriptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple otoroshi.script.Scripts at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(body)

Update (using json-patch) multiple otoroshi.script.Scripts at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
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
    api_instance = scripts_api.ScriptsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple otoroshi.script.Scripts at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_script_api_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(body)

Update multiple otoroshi.script.Scripts at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
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
    api_instance = scripts_api.ScriptsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple otoroshi.script.Scripts at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_script_api_controller_compile_script**
> Any otoroshi_controllers_adminapi_script_api_controller_compile_script(body)

Trigger script compilation of the server

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
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
    api_instance = scripts_api.ScriptsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Trigger script compilation of the server
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_compile_script(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_compile_script: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| request body |

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

# **otoroshi_controllers_adminapi_script_api_controller_create_action**
> OtoroshiScriptScript otoroshi_controllers_adminapi_script_api_controller_create_action(otoroshi_script_script)

Creates a otoroshi.script.Script

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_script_script import OtoroshiScriptScript
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
    api_instance = scripts_api.ScriptsApi(api_client)
    otoroshi_script_script = OtoroshiScriptScript(
        name="name_example",
        metadata={
            "key": "key_example",
        },
        tags=[
            "tags_example",
        ],
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        desc="desc_example",
        code="code_example",
        id="id_example",
        type=OtoroshiScriptPluginType("app"),
    ) # OtoroshiScriptScript | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a otoroshi.script.Script
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_create_action(otoroshi_script_script)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_script_script** | [**OtoroshiScriptScript**](OtoroshiScriptScript.md)| request body |

### Return type

[**OtoroshiScriptScript**](OtoroshiScriptScript.md)

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

# **otoroshi_controllers_adminapi_script_api_controller_delete_entity_action**
> OtoroshiScriptScript otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(id)

Deletes a specific otoroshi.script.Script using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_script_script import OtoroshiScriptScript
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
    api_instance = scripts_api.ScriptsApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific otoroshi.script.Script using its id
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiScriptScript**](OtoroshiScriptScript.md)

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

# **otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action**
> [OtoroshiScriptScript] otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action()

Find all possible otoroshi.script.Scripts entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_script_script import OtoroshiScriptScript
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
    api_instance = scripts_api.ScriptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible otoroshi.script.Scripts entities
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiScriptScript]**](OtoroshiScriptScript.md)

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

# **otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list**
> ScriptsList otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list()

Search plugins based on type of plugin

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.scripts_list import ScriptsList
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
    api_instance = scripts_api.ScriptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search plugins based on type of plugin
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_find_all_scripts_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ScriptsList**](ScriptsList.md)

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

# **otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action**
> OtoroshiScriptScript otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(id)

Find a specific otoroshi.script.Script using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_script_script import OtoroshiScriptScript
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
    api_instance = scripts_api.ScriptsApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific otoroshi.script.Script using its id
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiScriptScript**](OtoroshiScriptScript.md)

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

# **otoroshi_controllers_adminapi_script_api_controller_patch_entity_action**
> OtoroshiScriptScript otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(id, otoroshi_script_script)

Updates (using json-patch) a specific otoroshi.script.Script using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_script_script import OtoroshiScriptScript
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
    api_instance = scripts_api.ScriptsApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_script_script = OtoroshiScriptScript(
        name="name_example",
        metadata={
            "key": "key_example",
        },
        tags=[
            "tags_example",
        ],
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        desc="desc_example",
        code="code_example",
        id="id_example",
        type=OtoroshiScriptPluginType("app"),
    ) # OtoroshiScriptScript | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific otoroshi.script.Script using its id
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_patch_entity_action(id, otoroshi_script_script)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_script_script** | [**OtoroshiScriptScript**](OtoroshiScriptScript.md)| request body |

### Return type

[**OtoroshiScriptScript**](OtoroshiScriptScript.md)

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

# **otoroshi_controllers_adminapi_script_api_controller_update_entity_action**
> OtoroshiScriptScript otoroshi_controllers_adminapi_script_api_controller_update_entity_action(id, otoroshi_script_script)

Updates a specific otoroshi.script.Script using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_script_script import OtoroshiScriptScript
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
    api_instance = scripts_api.ScriptsApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_script_script = OtoroshiScriptScript(
        name="name_example",
        metadata={
            "key": "key_example",
        },
        tags=[
            "tags_example",
        ],
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        desc="desc_example",
        code="code_example",
        id="id_example",
        type=OtoroshiScriptPluginType("app"),
    ) # OtoroshiScriptScript | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific otoroshi.script.Script using its id
        api_response = api_instance.otoroshi_controllers_adminapi_script_api_controller_update_entity_action(id, otoroshi_script_script)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_script_api_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_script_script** | [**OtoroshiScriptScript**](OtoroshiScriptScript.md)| request body |

### Return type

[**OtoroshiScriptScript**](OtoroshiScriptScript.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_script**
> OtoroshiScriptScript otoroshi_controllers_adminapi_templates_controller_initiate_script()

Creates a new Script from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import scripts_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_script_script import OtoroshiScriptScript
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
    api_instance = scripts_api.ScriptsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new Script from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_script()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ScriptsApi->otoroshi_controllers_adminapi_templates_controller_initiate_script: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiScriptScript**](OtoroshiScriptScript.md)

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

