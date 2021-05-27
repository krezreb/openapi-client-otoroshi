# openapi_client.CertificatesApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_certificates_controller_bulk_create_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_bulk_create_action) | **POST** /api/certificates/_bulk | Create multiple Certs at the same time
[**otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action) | **DELETE** /api/certificates/_bulk | Delete multiple Certs at the same time
[**otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action) | **PATCH** /api/certificates/_bulk | Update (using json-patch) multiple Certs at the same time
[**otoroshi_controllers_adminapi_certificates_controller_bulk_update_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_bulk_update_action) | **PUT** /api/certificates/_bulk | Update multiple Certs at the same time
[**otoroshi_controllers_adminapi_certificates_controller_create_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_create_action) | **POST** /api/certificates | Creates a Cert
[**otoroshi_controllers_adminapi_certificates_controller_delete_entity_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_delete_entity_action) | **DELETE** /api/certificates/{id} | Deletes a specific Cert using its id
[**otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action) | **GET** /api/certificates | Find all possible Certs entities
[**otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action) | **GET** /api/certificates/{id} | Find a specific Cert using its id
[**otoroshi_controllers_adminapi_certificates_controller_patch_entity_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_patch_entity_action) | **PATCH** /api/certificates/{id} | Updates (using json-patch) a specific Cert using its id
[**otoroshi_controllers_adminapi_certificates_controller_renew_cert**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_renew_cert) | **POST** /api/certificates/{certId}/_renew | Renew a certificates with the same attributes as the original one
[**otoroshi_controllers_adminapi_certificates_controller_update_entity_action**](CertificatesApi.md#otoroshi_controllers_adminapi_certificates_controller_update_entity_action) | **PUT** /api/certificates/{id} | Updates a specific Cert using its id
[**otoroshi_controllers_adminapi_templates_controller_initiate_certificate**](CertificatesApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_certificate) | **GET** /api/certificates/_template | Creates a new Certificate from a template


# **otoroshi_controllers_adminapi_certificates_controller_bulk_create_action**
> BulkResponseBody otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(body)

Create multiple Certs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
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
    api_instance = certificates_api.CertificatesApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Create multiple Certs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_bulk_create_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_bulk_create_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action**
> BulkResponseBody otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action()

Delete multiple Certs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
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
    api_instance = certificates_api.CertificatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete multiple Certs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_bulk_delete_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action**
> BulkResponseBody otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(body)

Update (using json-patch) multiple Certs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
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
    api_instance = certificates_api.CertificatesApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (using json-patch) multiple Certs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_bulk_patch_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_certificates_controller_bulk_update_action**
> BulkResponseBody otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(body)

Update multiple Certs at the same time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
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
    api_instance = certificates_api.CertificatesApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Update multiple Certs at the same time
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_bulk_update_action(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_bulk_update_action: %s\n" % e)
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

# **otoroshi_controllers_adminapi_certificates_controller_create_action**
> OtoroshiSslCert otoroshi_controllers_adminapi_certificates_controller_create_action(otoroshi_ssl_cert)

Creates a Cert

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)
    otoroshi_ssl_cert = OtoroshiSslCert(
        lets_encrypt=True,
        keypair=True,
        to=3.14,
        tags=[
            "tags_example",
        ],
        exposed=True,
        auto_renew=True,
        id="id_example",
        revoked=True,
        _from=3.14,
        client=True,
        ca=True,
        name="name_example",
        chain="chain_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        password=,
        sans=[
            "sans_example",
        ],
        self_signed=True,
        entity_metadata={
            "key": "key_example",
        },
        private_key="private_key_example",
        domain="domain_example",
        ca_ref=,
        description="description_example",
        subject="subject_example",
        valid=True,
    ) # OtoroshiSslCert | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a Cert
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_create_action(otoroshi_ssl_cert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_create_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_ssl_cert** | [**OtoroshiSslCert**](OtoroshiSslCert.md)| request body |

### Return type

[**OtoroshiSslCert**](OtoroshiSslCert.md)

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

# **otoroshi_controllers_adminapi_certificates_controller_delete_entity_action**
> OtoroshiSslCert otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(id)

Deletes a specific Cert using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific Cert using its id
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_delete_entity_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_delete_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiSslCert**](OtoroshiSslCert.md)

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

# **otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action**
> [OtoroshiSslCert] otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action()

Find all possible Certs entities

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Find all possible Certs entities
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_find_all_entities_action: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OtoroshiSslCert]**](OtoroshiSslCert.md)

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

# **otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action**
> OtoroshiSslCert otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(id)

Find a specific Cert using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)
    id = "id_example" # str | The id param of the target entity

    # example passing only required values which don't have defaults set
    try:
        # Find a specific Cert using its id
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_find_entity_by_id_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |

### Return type

[**OtoroshiSslCert**](OtoroshiSslCert.md)

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

# **otoroshi_controllers_adminapi_certificates_controller_patch_entity_action**
> OtoroshiSslCert otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(id, otoroshi_ssl_cert)

Updates (using json-patch) a specific Cert using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_ssl_cert = OtoroshiSslCert(
        lets_encrypt=True,
        keypair=True,
        to=3.14,
        tags=[
            "tags_example",
        ],
        exposed=True,
        auto_renew=True,
        id="id_example",
        revoked=True,
        _from=3.14,
        client=True,
        ca=True,
        name="name_example",
        chain="chain_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        password=,
        sans=[
            "sans_example",
        ],
        self_signed=True,
        entity_metadata={
            "key": "key_example",
        },
        private_key="private_key_example",
        domain="domain_example",
        ca_ref=,
        description="description_example",
        subject="subject_example",
        valid=True,
    ) # OtoroshiSslCert | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates (using json-patch) a specific Cert using its id
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_patch_entity_action(id, otoroshi_ssl_cert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_patch_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_ssl_cert** | [**OtoroshiSslCert**](OtoroshiSslCert.md)| request body |

### Return type

[**OtoroshiSslCert**](OtoroshiSslCert.md)

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

# **otoroshi_controllers_adminapi_certificates_controller_renew_cert**
> OtoroshiSslCert otoroshi_controllers_adminapi_certificates_controller_renew_cert(cert_id, body)

Renew a certificates with the same attributes as the original one

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)
    cert_id = "certId_example" # str | The certId param of the target entity
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Renew a certificates with the same attributes as the original one
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_renew_cert(cert_id, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_renew_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **str**| The certId param of the target entity |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**OtoroshiSslCert**](OtoroshiSslCert.md)

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

# **otoroshi_controllers_adminapi_certificates_controller_update_entity_action**
> OtoroshiSslCert otoroshi_controllers_adminapi_certificates_controller_update_entity_action(id, otoroshi_ssl_cert)

Updates a specific Cert using its id

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)
    id = "id_example" # str | The id param of the target entity
    otoroshi_ssl_cert = OtoroshiSslCert(
        lets_encrypt=True,
        keypair=True,
        to=3.14,
        tags=[
            "tags_example",
        ],
        exposed=True,
        auto_renew=True,
        id="id_example",
        revoked=True,
        _from=3.14,
        client=True,
        ca=True,
        name="name_example",
        chain="chain_example",
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        password=,
        sans=[
            "sans_example",
        ],
        self_signed=True,
        entity_metadata={
            "key": "key_example",
        },
        private_key="private_key_example",
        domain="domain_example",
        ca_ref=,
        description="description_example",
        subject="subject_example",
        valid=True,
    ) # OtoroshiSslCert | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a specific Cert using its id
        api_response = api_instance.otoroshi_controllers_adminapi_certificates_controller_update_entity_action(id, otoroshi_ssl_cert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_certificates_controller_update_entity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id param of the target entity |
 **otoroshi_ssl_cert** | [**OtoroshiSslCert**](OtoroshiSslCert.md)| request body |

### Return type

[**OtoroshiSslCert**](OtoroshiSslCert.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_certificate**
> OtoroshiSslCert otoroshi_controllers_adminapi_templates_controller_initiate_certificate()

Creates a new Certificate from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import certificates_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
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
    api_instance = certificates_api.CertificatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new Certificate from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_certificate()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificatesApi->otoroshi_controllers_adminapi_templates_controller_initiate_certificate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiSslCert**](OtoroshiSslCert.md)

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

