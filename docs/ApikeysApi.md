# openapi_client.ApikeysApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas) | **GET** /api/apikeys/{id}/quotas | Consumed quotas for a specific apikey
[**otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action) | **POST** /api/apikeys/_bulk | Create multiple ApiKeys at the same time
[**otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action) | **DELETE** /api/apikeys/_bulk | Delete multiple ApiKeys at the same time
[**otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action) | **PATCH** /api/apikeys/_bulk | Update (using json-patch) multiple ApiKeys at the same time
[**otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action) | **PUT** /api/apikeys/_bulk | Update multiple ApiKeys at the same time
[**otoroshi_controllers_adminapi_api_keys_controller_create_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_create_action) | **POST** /api/apikeys | Creates a ApiKey
[**otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action) | **DELETE** /api/apikeys/{id} | Deletes a specific ApiKey using its id
[**otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action) | **GET** /api/apikeys | Find all possible ApiKeys entities
[**otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action) | **GET** /api/apikeys/{id} | Find a specific ApiKey using its id
[**otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action) | **PATCH** /api/apikeys/{id} | Updates (using json-patch) a specific ApiKey using its id
[**otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas) | **DELETE** /api/apikeys/{id}/quotas | Reset quotas consumption for an apikey
[**otoroshi_controllers_adminapi_api_keys_controller_update_entity_action**](ApikeysApi.md#otoroshi_controllers_adminapi_api_keys_controller_update_entity_action) | **PUT** /api/apikeys/{id} | Updates a specific ApiKey using its id
[**otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys**](ApikeysApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys) | **GET** /api/apikeys/_template | Creates a new ApiKey from a template


# **otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas**
> OtoroshiModelsRemainingQuotas otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(id)

Consumed quotas for a specific apikey

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_remaining_quotas import OtoroshiModelsRemainingQuotas
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Consumed quotas for a specific apikey
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_api_key_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsRemainingQuotas**](OtoroshiModelsRemainingQuotas.md)

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

# **otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(body)

Create multiple ApiKeys at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple ApiKeys at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action()

Delete multiple ApiKeys at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple ApiKeys at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(body)

Update (using json-patch) multiple ApiKeys at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple ApiKeys at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(body)

Update multiple ApiKeys at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple ApiKeys at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_api_keys_controller_create_action**
> OtoroshiModelsApiKey otoroshi_controllers_adminapi_api_keys_controller_create_action(otoroshi_models_api_key)

Creates a ApiKey

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    otoroshi_models_api_key = OtoroshiModelsApiKey(
        daily_quota=1,
        metadata={
            "key": "key_example",
        },
        throttling_quota=1,
        constrained_services_only=True,
        allow_client_id_only=True,
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        restrictions=OtoroshiModelsRestrictions(
            forbidden=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            allowed=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            not_found=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            allow_last=True,
            enabled=True,
        ),
        tags=[
            "tags_example",
        ],
        enabled=True,
        read_only=True,
        client_secret="client_secret_example",
        valid_until=,
        client_name="client_name_example",
        monthly_quota=1,
        description="description_example",
        rotation=OtoroshiModelsApiKeyRotation(
            enabled=True,
            rotation_every=1,
            grace_period=1,
            next_secret=,
        ),
        authorized_entities=[
            OtoroshiModelsEntityIdentifier(),
        ],
        client_id="client_id_example",
    ) # OtoroshiModelsApiKey | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a ApiKey
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_create_action(otoroshi_models_api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_api_key** | [**OtoroshiModelsApiKey**](OtoroshiModelsApiKey.md)| request body |

### Return type

[**OtoroshiModelsApiKey**](OtoroshiModelsApiKey.md)

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

# **otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action**
> OtoroshiModelsApiKey otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(id)

Deletes a specific ApiKey using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific ApiKey using its id
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

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

# **otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action**
> [OtoroshiModelsApiKey] otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action()

Find all possible ApiKeys entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible ApiKeys entities
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiModelsApiKey]**](OtoroshiModelsApiKey.md)

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

# **otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action**
> OtoroshiModelsApiKey otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(id)

Find a specific ApiKey using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific ApiKey using its id
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

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

# **otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action**
> OtoroshiModelsApiKey otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(id, otoroshi_models_api_key)

Updates (using json-patch) a specific ApiKey using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_api_key = OtoroshiModelsApiKey(
        daily_quota=1,
        metadata={
            "key": "key_example",
        },
        throttling_quota=1,
        constrained_services_only=True,
        allow_client_id_only=True,
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        restrictions=OtoroshiModelsRestrictions(
            forbidden=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            allowed=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            not_found=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            allow_last=True,
            enabled=True,
        ),
        tags=[
            "tags_example",
        ],
        enabled=True,
        read_only=True,
        client_secret="client_secret_example",
        valid_until=,
        client_name="client_name_example",
        monthly_quota=1,
        description="description_example",
        rotation=OtoroshiModelsApiKeyRotation(
            enabled=True,
            rotation_every=1,
            grace_period=1,
            next_secret=,
        ),
        authorized_entities=[
            OtoroshiModelsEntityIdentifier(),
        ],
        client_id="client_id_example",
    ) # OtoroshiModelsApiKey | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific ApiKey using its id
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action(id, otoroshi_models_api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_api_key** | [**OtoroshiModelsApiKey**](OtoroshiModelsApiKey.md)| request body |

### Return type

[**OtoroshiModelsApiKey**](OtoroshiModelsApiKey.md)

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

# **otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas**
> OtoroshiModelsRemainingQuotas otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(id)

Reset quotas consumption for an apikey

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_remaining_quotas import OtoroshiModelsRemainingQuotas
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Reset quotas consumption for an apikey
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_reset_api_key_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsRemainingQuotas**](OtoroshiModelsRemainingQuotas.md)

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

# **otoroshi_controllers_adminapi_api_keys_controller_update_entity_action**
> OtoroshiModelsApiKey otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(id, otoroshi_models_api_key)

Updates a specific ApiKey using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_api_key = OtoroshiModelsApiKey(
        daily_quota=1,
        metadata={
            "key": "key_example",
        },
        throttling_quota=1,
        constrained_services_only=True,
        allow_client_id_only=True,
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        restrictions=OtoroshiModelsRestrictions(
            forbidden=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            allowed=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            not_found=[
                OtoroshiModelsRestrictionPath(
                    method="method_example",
                    path="path_example",
                ),
            ],
            allow_last=True,
            enabled=True,
        ),
        tags=[
            "tags_example",
        ],
        enabled=True,
        read_only=True,
        client_secret="client_secret_example",
        valid_until=,
        client_name="client_name_example",
        monthly_quota=1,
        description="description_example",
        rotation=OtoroshiModelsApiKeyRotation(
            enabled=True,
            rotation_every=1,
            grace_period=1,
            next_secret=,
        ),
        authorized_entities=[
            OtoroshiModelsEntityIdentifier(),
        ],
        client_id="client_id_example",
    ) # OtoroshiModelsApiKey | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific ApiKey using its id
        api_response = api_instance.otoroshi_controllers_adminapi_api_keys_controller_update_entity_action(id, otoroshi_models_api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_api_keys_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_api_key** | [**OtoroshiModelsApiKey**](OtoroshiModelsApiKey.md)| request body |

### Return type

[**OtoroshiModelsApiKey**](OtoroshiModelsApiKey.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys**
> OtoroshiModelsApiKey otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys()

Creates a new ApiKey from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import apikeys_api
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
    api_instance = apikeys_api.ApikeysApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new ApiKey from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApikeysApi->otoroshi_controllers_adminapi_templates_controller_initiate_api_key_apikeys: %s\n" % e)
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

