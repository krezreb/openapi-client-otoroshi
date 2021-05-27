# openapi_client.OrganizationsApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_templates_controller_initiate_tenant**](OrganizationsApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_tenant) | **GET** /api/tenants/_template | Creates a new Tenant from a template
[**otoroshi_controllers_adminapi_tenants_controller_bulk_create_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_bulk_create_action) | **POST** /api/tenants/_bulk | Create multiple Tenants at the same time
[**otoroshi_controllers_adminapi_tenants_controller_bulk_delete_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_bulk_delete_action) | **DELETE** /api/tenants/_bulk | Delete multiple Tenants at the same time
[**otoroshi_controllers_adminapi_tenants_controller_bulk_patch_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_bulk_patch_action) | **PATCH** /api/tenants/_bulk | Update (using json-patch) multiple Tenants at the same time
[**otoroshi_controllers_adminapi_tenants_controller_bulk_update_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_bulk_update_action) | **PUT** /api/tenants/_bulk | Update multiple Tenants at the same time
[**otoroshi_controllers_adminapi_tenants_controller_create_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_create_action) | **POST** /api/tenants | Creates a Tenant
[**otoroshi_controllers_adminapi_tenants_controller_delete_entity_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_delete_entity_action) | **DELETE** /api/tenants/{id} | Deletes a specific Tenant using its id
[**otoroshi_controllers_adminapi_tenants_controller_find_all_entities_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_find_all_entities_action) | **GET** /api/tenants | Find all possible Tenants entities
[**otoroshi_controllers_adminapi_tenants_controller_find_entity_by_id_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_find_entity_by_id_action) | **GET** /api/tenants/{id} | Find a specific Tenant using its id
[**otoroshi_controllers_adminapi_tenants_controller_patch_entity_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_patch_entity_action) | **PATCH** /api/tenants/{id} | Updates (using json-patch) a specific Tenant using its id
[**otoroshi_controllers_adminapi_tenants_controller_update_entity_action**](OrganizationsApi.md#otoroshi_controllers_adminapi_tenants_controller_update_entity_action) | **PUT** /api/tenants/{id} | Updates a specific Tenant using its id


# **otoroshi_controllers_adminapi_templates_controller_initiate_tenant**
> OtoroshiModelsTenant otoroshi_controllers_adminapi_templates_controller_initiate_tenant()

Creates a new Tenant from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_tenant import OtoroshiModelsTenant
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new Tenant from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_tenant()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_templates_controller_initiate_tenant: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)

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

# **otoroshi_controllers_adminapi_tenants_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_tenants_controller_bulk_create_action(body)

Create multiple Tenants at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple Tenants at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_tenants_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_tenants_controller_bulk_delete_action()

Delete multiple Tenants at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple Tenants at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_tenants_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_tenants_controller_bulk_patch_action(body)

Update (using json-patch) multiple Tenants at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple Tenants at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_tenants_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_tenants_controller_bulk_update_action(body)

Update multiple Tenants at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple Tenants at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_tenants_controller_create_action**
> OtoroshiModelsTenant otoroshi_controllers_adminapi_tenants_controller_create_action(otoroshi_models_tenant)

Creates a Tenant

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_tenant import OtoroshiModelsTenant
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    otoroshi_models_tenant = OtoroshiModelsTenant(
        description="description_example",
        metadata={
            "key": "key_example",
        },
        name="name_example",
        tags=[
            "tags_example",
        ],
        id="id_example",
    ) # OtoroshiModelsTenant | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a Tenant
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_create_action(otoroshi_models_tenant)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_tenant** | [**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)| request body |

### Return type

[**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)

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

# **otoroshi_controllers_adminapi_tenants_controller_delete_entity_action**
> OtoroshiModelsTenant otoroshi_controllers_adminapi_tenants_controller_delete_entity_action(id)

Deletes a specific Tenant using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_tenant import OtoroshiModelsTenant
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific Tenant using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)

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

# **otoroshi_controllers_adminapi_tenants_controller_find_all_entities_action**
> [OtoroshiModelsTenant] otoroshi_controllers_adminapi_tenants_controller_find_all_entities_action()

Find all possible Tenants entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_tenant import OtoroshiModelsTenant
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible Tenants entities
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiModelsTenant]**](OtoroshiModelsTenant.md)

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

# **otoroshi_controllers_adminapi_tenants_controller_find_entity_by_id_action**
> OtoroshiModelsTenant otoroshi_controllers_adminapi_tenants_controller_find_entity_by_id_action(id)

Find a specific Tenant using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_tenant import OtoroshiModelsTenant
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific Tenant using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)

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

# **otoroshi_controllers_adminapi_tenants_controller_patch_entity_action**
> OtoroshiModelsTenant otoroshi_controllers_adminapi_tenants_controller_patch_entity_action(id, otoroshi_models_tenant)

Updates (using json-patch) a specific Tenant using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_tenant import OtoroshiModelsTenant
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_tenant = OtoroshiModelsTenant(
        description="description_example",
        metadata={
            "key": "key_example",
        },
        name="name_example",
        tags=[
            "tags_example",
        ],
        id="id_example",
    ) # OtoroshiModelsTenant | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific Tenant using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_patch_entity_action(id, otoroshi_models_tenant)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_tenant** | [**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)| request body |

### Return type

[**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)

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

# **otoroshi_controllers_adminapi_tenants_controller_update_entity_action**
> OtoroshiModelsTenant otoroshi_controllers_adminapi_tenants_controller_update_entity_action(id, otoroshi_models_tenant)

Updates a specific Tenant using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_tenant import OtoroshiModelsTenant
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
    api_instance = organizations_api.OrganizationsApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_tenant = OtoroshiModelsTenant(
        description="description_example",
        metadata={
            "key": "key_example",
        },
        name="name_example",
        tags=[
            "tags_example",
        ],
        id="id_example",
    ) # OtoroshiModelsTenant | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific Tenant using its id
        api_response = api_instance.otoroshi_controllers_adminapi_tenants_controller_update_entity_action(id, otoroshi_models_tenant)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->otoroshi_controllers_adminapi_tenants_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_tenant** | [**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)| request body |

### Return type

[**OtoroshiModelsTenant**](OtoroshiModelsTenant.md)

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

