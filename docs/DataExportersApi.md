# openapi_client.DataExportersApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action) | **POST** /api/data-exporter-configs/_bulk | Create multiple DataExporterConfigs at the same time
[**otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action) | **DELETE** /api/data-exporter-configs/_bulk | Delete multiple DataExporterConfigs at the same time
[**otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action) | **PATCH** /api/data-exporter-configs/_bulk | Update (using json-patch) multiple DataExporterConfigs at the same time
[**otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action) | **PUT** /api/data-exporter-configs/_bulk | Update multiple DataExporterConfigs at the same time
[**otoroshi_controllers_adminapi_data_exporter_config_controller_create_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_create_action) | **POST** /api/data-exporter-configs | Creates a DataExporterConfig
[**otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action) | **DELETE** /api/data-exporter-configs/{id} | Deletes a specific DataExporterConfig using its id
[**otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action) | **GET** /api/data-exporter-configs | Find all possible DataExporterConfigs entities
[**otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action) | **GET** /api/data-exporter-configs/{id} | Find a specific DataExporterConfig using its id
[**otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action) | **PATCH** /api/data-exporter-configs/{id} | Updates (using json-patch) a specific DataExporterConfig using its id
[**otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action**](DataExportersApi.md#otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action) | **PUT** /api/data-exporter-configs/{id} | Updates a specific DataExporterConfig using its id
[**otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config**](DataExportersApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config) | **GET** /api/data-exporter-configs/_template | Creates a new DataExporterConfig from a template


# **otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(body)

Create multiple DataExporterConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple DataExporterConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action()

Delete multiple DataExporterConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
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
    api_instance = data_exporters_api.DataExportersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple DataExporterConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(body)

Update (using json-patch) multiple DataExporterConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple DataExporterConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(body)

Update multiple DataExporterConfigs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple DataExporterConfigs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_create_action**
> OtoroshiModelsDataExporterConfig otoroshi_controllers_adminapi_data_exporter_config_controller_create_action(otoroshi_models_data_exporter_config)

Creates a DataExporterConfig

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    otoroshi_models_data_exporter_config = OtoroshiModelsDataExporterConfig(
        desc="desc_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        buffer_size=1,
        json_workers=1,
        group_duration=3.14,
        group_size=1,
        typ=OtoroshiModelsDataExporterConfigType("kafka"),
        tags=[
            "tags_example",
        ],
        send_workers=1,
        id="id_example",
        name="name_example",
        metadata={
            "key": "key_example",
        },
        config=OtoroshiModelsExporter(),
        projection={},
        enabled=True,
        filtering=OtoroshiModelsDataExporterConfigFiltering(
            include=[
                {},
            ],
            exclude=[
                {},
            ],
        ),
    ) # OtoroshiModelsDataExporterConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a DataExporterConfig
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_create_action(otoroshi_models_data_exporter_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_data_exporter_config** | [**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)| request body |

### Return type

[**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)

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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action**
> OtoroshiModelsDataExporterConfig otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(id)

Deletes a specific DataExporterConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific DataExporterConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)

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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action**
> [OtoroshiModelsDataExporterConfig] otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action()

Find all possible DataExporterConfigs entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
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
    api_instance = data_exporters_api.DataExportersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible DataExporterConfigs entities
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiModelsDataExporterConfig]**](OtoroshiModelsDataExporterConfig.md)

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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action**
> OtoroshiModelsDataExporterConfig otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(id)

Find a specific DataExporterConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific DataExporterConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)

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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action**
> OtoroshiModelsDataExporterConfig otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(id, otoroshi_models_data_exporter_config)

Updates (using json-patch) a specific DataExporterConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_data_exporter_config = OtoroshiModelsDataExporterConfig(
        desc="desc_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        buffer_size=1,
        json_workers=1,
        group_duration=3.14,
        group_size=1,
        typ=OtoroshiModelsDataExporterConfigType("kafka"),
        tags=[
            "tags_example",
        ],
        send_workers=1,
        id="id_example",
        name="name_example",
        metadata={
            "key": "key_example",
        },
        config=OtoroshiModelsExporter(),
        projection={},
        enabled=True,
        filtering=OtoroshiModelsDataExporterConfigFiltering(
            include=[
                {},
            ],
            exclude=[
                {},
            ],
        ),
    ) # OtoroshiModelsDataExporterConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific DataExporterConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(id, otoroshi_models_data_exporter_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_data_exporter_config** | [**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)| request body |

### Return type

[**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)

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

# **otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action**
> OtoroshiModelsDataExporterConfig otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(id, otoroshi_models_data_exporter_config)

Updates a specific DataExporterConfig using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
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
    api_instance = data_exporters_api.DataExportersApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_models_data_exporter_config = OtoroshiModelsDataExporterConfig(
        desc="desc_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        buffer_size=1,
        json_workers=1,
        group_duration=3.14,
        group_size=1,
        typ=OtoroshiModelsDataExporterConfigType("kafka"),
        tags=[
            "tags_example",
        ],
        send_workers=1,
        id="id_example",
        name="name_example",
        metadata={
            "key": "key_example",
        },
        config=OtoroshiModelsExporter(),
        projection={},
        enabled=True,
        filtering=OtoroshiModelsDataExporterConfigFiltering(
            include=[
                {},
            ],
            exclude=[
                {},
            ],
        ),
    ) # OtoroshiModelsDataExporterConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific DataExporterConfig using its id
        api_response = api_instance.otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(id, otoroshi_models_data_exporter_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_models_data_exporter_config** | [**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)| request body |

### Return type

[**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config**
> OtoroshiModelsDataExporterConfig otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config()

Creates a new DataExporterConfig from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import data_exporters_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
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
    api_instance = data_exporters_api.DataExportersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new DataExporterConfig from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DataExportersApi->otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsDataExporterConfig**](OtoroshiModelsDataExporterConfig.md)

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

