# openapi_client.JwtVerifiersApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action) | **POST** /api/verifiers/_bulk | Create multiple GlobalJwtVerifiers at the same time
[**otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action) | **DELETE** /api/verifiers/_bulk | Delete multiple GlobalJwtVerifiers at the same time
[**otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action) | **PATCH** /api/verifiers/_bulk | Update (using json-patch) multiple GlobalJwtVerifiers at the same time
[**otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action) | **PUT** /api/verifiers/_bulk | Update multiple GlobalJwtVerifiers at the same time
[**otoroshi_controllers_adminapi_jwt_verifier_controller_create_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_create_action) | **POST** /api/verifiers | Creates a GlobalJwtVerifier
[**otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action) | **DELETE** /api/verifiers/{id} | Deletes a specific GlobalJwtVerifier using its id
[**otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action) | **GET** /api/verifiers | Find all possible GlobalJwtVerifiers entities
[**otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action) | **GET** /api/verifiers/{id} | Find a specific GlobalJwtVerifier using its id
[**otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action) | **PATCH** /api/verifiers/{id} | Updates (using json-patch) a specific GlobalJwtVerifier using its id
[**otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action) | **PUT** /api/verifiers/{id} | Updates a specific GlobalJwtVerifier using its id
[**otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier**](JwtVerifiersApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier) | **GET** /api/verifiers/_template | Creates a new JwtVerifier from a template


# **otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(body)

Create multiple GlobalJwtVerifiers at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple GlobalJwtVerifiers at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action()

Delete multiple GlobalJwtVerifiers at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple GlobalJwtVerifiers at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(body)

Update (using json-patch) multiple GlobalJwtVerifiers at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple GlobalJwtVerifiers at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(body)

Update multiple GlobalJwtVerifiers at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple GlobalJwtVerifiers at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_create_action**
> OtoroshiModelsGlobalJwtVerifier otoroshi_controllers_adminapi_jwt_verifier_controller_create_action(otoroshi_models_global_jwt_verifier)

Creates a GlobalJwtVerifier

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    otoroshi_models_global_jwt_verifier = OtoroshiModelsGlobalJwtVerifier(
        metadata={
            "key": "key_example",
        },
        algo_settings=OtoroshiModelsAlgoSettings(),
        name="name_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        source=OtoroshiModelsJwtTokenLocation(),
        id="id_example",
        type="global",
        strict=True,
        strategy=OtoroshiModelsVerifierStrategy(),
        desc="desc_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsGlobalJwtVerifier | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a GlobalJwtVerifier
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_create_action(otoroshi_models_global_jwt_verifier)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_global_jwt_verifier** | [**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)| request body |

### Return type

[**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)

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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action**
> OtoroshiModelsGlobalJwtVerifier otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(id)

Deletes a specific GlobalJwtVerifier using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific GlobalJwtVerifier using its id
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)

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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action**
> [OtoroshiModelsGlobalJwtVerifier] otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action()

Find all possible GlobalJwtVerifiers entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible GlobalJwtVerifiers entities
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiModelsGlobalJwtVerifier]**](OtoroshiModelsGlobalJwtVerifier.md)

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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action**
> OtoroshiModelsGlobalJwtVerifier otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(id)

Find a specific GlobalJwtVerifier using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific GlobalJwtVerifier using its id
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)

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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action**
> OtoroshiModelsGlobalJwtVerifier otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(id, otoroshi_models_global_jwt_verifier)

Updates (using json-patch) a specific GlobalJwtVerifier using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_global_jwt_verifier = OtoroshiModelsGlobalJwtVerifier(
        metadata={
            "key": "key_example",
        },
        algo_settings=OtoroshiModelsAlgoSettings(),
        name="name_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        source=OtoroshiModelsJwtTokenLocation(),
        id="id_example",
        type="global",
        strict=True,
        strategy=OtoroshiModelsVerifierStrategy(),
        desc="desc_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsGlobalJwtVerifier | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific GlobalJwtVerifier using its id
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action(id, otoroshi_models_global_jwt_verifier)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_global_jwt_verifier** | [**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)| request body |

### Return type

[**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)

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

# **otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action**
> OtoroshiModelsGlobalJwtVerifier otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(id, otoroshi_models_global_jwt_verifier)

Updates a specific GlobalJwtVerifier using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_global_jwt_verifier = OtoroshiModelsGlobalJwtVerifier(
        metadata={
            "key": "key_example",
        },
        algo_settings=OtoroshiModelsAlgoSettings(),
        name="name_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        source=OtoroshiModelsJwtTokenLocation(),
        id="id_example",
        type="global",
        strict=True,
        strategy=OtoroshiModelsVerifierStrategy(),
        desc="desc_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsGlobalJwtVerifier | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific GlobalJwtVerifier using its id
        api_response = api_instance.otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action(id, otoroshi_models_global_jwt_verifier)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_jwt_verifier_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_global_jwt_verifier** | [**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)| request body |

### Return type

[**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier**
> OtoroshiModelsGlobalJwtVerifier otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier()

Creates a new JwtVerifier from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import jwt_verifiers_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_global_jwt_verifier import OtoroshiModelsGlobalJwtVerifier
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
    api_instance = jwt_verifiers_api.JwtVerifiersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new JwtVerifier from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling JwtVerifiersApi->otoroshi_controllers_adminapi_templates_controller_initiate_jwt_verifier: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsGlobalJwtVerifier**](OtoroshiModelsGlobalJwtVerifier.md)

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

