# openapi_client.PkiApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_pki_controller_certificate_data**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_certificate_data) | **POST** /api/pki/certs/_data | Extract data from a certificate
[**otoroshi_controllers_adminapi_pki_controller_certificate_is_valid**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_certificate_is_valid) | **POST** /api/pki/certs/_valid | Check if a certificate is valid (based on its own data)
[**otoroshi_controllers_adminapi_pki_controller_gen_cert**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_gen_cert) | **POST** /api/pki/cas/{ca}/certs | Generates a certificate
[**otoroshi_controllers_adminapi_pki_controller_gen_csr**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_gen_csr) | **POST** /api/pki/csrs | Generates a CSR
[**otoroshi_controllers_adminapi_pki_controller_gen_key_pair**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_gen_key_pair) | **POST** /api/pki/keys | Generates a keypair
[**otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert) | **POST** /api/pki/certs/_letencrypt | Generates a certificates using Let&#39;s Encrypt or any ACME compatible system
[**otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca) | **POST** /api/pki/cas | Generates a self signed CA
[**otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert) | **POST** /api/pki/certs | Generates a self signed certificates
[**otoroshi_controllers_adminapi_pki_controller_gen_sub_ca**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_gen_sub_ca) | **POST** /api/pki/cas/{ca}/cas | Generates a sub-CA
[**otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12) | **POST** /api/pki/certs/_p12 | Import de .p12 file as client certificates
[**otoroshi_controllers_adminapi_pki_controller_sign_cert**](PkiApi.md#otoroshi_controllers_adminapi_pki_controller_sign_cert) | **POST** /api/pki/cas/{ca}/certs/_sign | Sign a certificate based on a CSR


# **otoroshi_controllers_adminapi_pki_controller_certificate_data**
> Any otoroshi_controllers_adminapi_pki_controller_certificate_data(body)

Extract data from a certificate

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
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
    api_instance = pki_api.PkiApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Extract data from a certificate
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_certificate_data(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_certificate_data: %s\n" % e)
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

# **otoroshi_controllers_adminapi_pki_controller_certificate_is_valid**
> CertValidResponse otoroshi_controllers_adminapi_pki_controller_certificate_is_valid(otoroshi_ssl_cert)

Check if a certificate is valid (based on its own data)

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_cert import OtoroshiSslCert
from openapi_client.model.cert_valid_response import CertValidResponse
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
    api_instance = pki_api.PkiApi(api_client)
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
        # Check if a certificate is valid (based on its own data)
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_certificate_is_valid(otoroshi_ssl_cert)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_certificate_is_valid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_ssl_cert** | [**OtoroshiSslCert**](OtoroshiSslCert.md)| request body |

### Return type

[**CertValidResponse**](CertValidResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_gen_cert**
> OtoroshiSslPkiModelsGenCertResponse otoroshi_controllers_adminapi_pki_controller_gen_cert(ca, otoroshi_ssl_pki_models_gen_csr_query)

Generates a certificate

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_cert_response import OtoroshiSslPkiModelsGenCertResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_csr_query import OtoroshiSslPkiModelsGenCsrQuery
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
    api_instance = pki_api.PkiApi(api_client)
    ca = "ca_example" # str | the ca parameter
    otoroshi_ssl_pki_models_gen_csr_query = OtoroshiSslPkiModelsGenCsrQuery(
        client=True,
        hosts=[
            "hosts_example",
        ],
        key=OtoroshiSslPkiModelsGenKeyPairQuery(
            algo="algo_example",
            size=1,
        ),
        include_aia=True,
        signature_alg="signature_alg_example",
        existing_serial_number=,
        duration=3.14,
        digest_alg="digest_alg_example",
        ca=True,
        name={
            "key": "key_example",
        },
        subject=,
    ) # OtoroshiSslPkiModelsGenCsrQuery | request body

    # example passing only required values which don't have defaults set
    try:
        # Generates a certificate
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_gen_cert(ca, otoroshi_ssl_pki_models_gen_csr_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_gen_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca** | **str**| the ca parameter |
 **otoroshi_ssl_pki_models_gen_csr_query** | [**OtoroshiSslPkiModelsGenCsrQuery**](OtoroshiSslPkiModelsGenCsrQuery.md)| request body |

### Return type

[**OtoroshiSslPkiModelsGenCertResponse**](OtoroshiSslPkiModelsGenCertResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_gen_csr**
> OtoroshiSslPkiModelsGenCsrResponse otoroshi_controllers_adminapi_pki_controller_gen_csr(otoroshi_ssl_pki_models_gen_csr_query)

Generates a CSR

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.otoroshi_ssl_pki_models_gen_csr_response import OtoroshiSslPkiModelsGenCsrResponse
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_csr_query import OtoroshiSslPkiModelsGenCsrQuery
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
    api_instance = pki_api.PkiApi(api_client)
    otoroshi_ssl_pki_models_gen_csr_query = OtoroshiSslPkiModelsGenCsrQuery(
        client=True,
        hosts=[
            "hosts_example",
        ],
        key=OtoroshiSslPkiModelsGenKeyPairQuery(
            algo="algo_example",
            size=1,
        ),
        include_aia=True,
        signature_alg="signature_alg_example",
        existing_serial_number=,
        duration=3.14,
        digest_alg="digest_alg_example",
        ca=True,
        name={
            "key": "key_example",
        },
        subject=,
    ) # OtoroshiSslPkiModelsGenCsrQuery | request body

    # example passing only required values which don't have defaults set
    try:
        # Generates a CSR
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_gen_csr(otoroshi_ssl_pki_models_gen_csr_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_gen_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_ssl_pki_models_gen_csr_query** | [**OtoroshiSslPkiModelsGenCsrQuery**](OtoroshiSslPkiModelsGenCsrQuery.md)| request body |

### Return type

[**OtoroshiSslPkiModelsGenCsrResponse**](OtoroshiSslPkiModelsGenCsrResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_gen_key_pair**
> OtoroshiSslPkiModelsGenKeyPairResponse otoroshi_controllers_adminapi_pki_controller_gen_key_pair(otoroshi_ssl_pki_models_gen_key_pair_query)

Generates a keypair

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.otoroshi_ssl_pki_models_gen_key_pair_response import OtoroshiSslPkiModelsGenKeyPairResponse
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_key_pair_query import OtoroshiSslPkiModelsGenKeyPairQuery
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
    api_instance = pki_api.PkiApi(api_client)
    otoroshi_ssl_pki_models_gen_key_pair_query = OtoroshiSslPkiModelsGenKeyPairQuery(
        algo="algo_example",
        size=1,
    ) # OtoroshiSslPkiModelsGenKeyPairQuery | request body

    # example passing only required values which don't have defaults set
    try:
        # Generates a keypair
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_gen_key_pair(otoroshi_ssl_pki_models_gen_key_pair_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_gen_key_pair: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_ssl_pki_models_gen_key_pair_query** | [**OtoroshiSslPkiModelsGenKeyPairQuery**](OtoroshiSslPkiModelsGenKeyPairQuery.md)| request body |

### Return type

[**OtoroshiSslPkiModelsGenKeyPairResponse**](OtoroshiSslPkiModelsGenKeyPairResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert**
> OtoroshiSslPkiModelsGenCertResponse otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(body)

Generates a certificates using Let's Encrypt or any ACME compatible system

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_cert_response import OtoroshiSslPkiModelsGenCertResponse
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
    api_instance = pki_api.PkiApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Generates a certificates using Let's Encrypt or any ACME compatible system
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_gen_lets_encrypt_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**OtoroshiSslPkiModelsGenCertResponse**](OtoroshiSslPkiModelsGenCertResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca**
> OtoroshiSslPkiModelsGenCertResponse otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca(otoroshi_ssl_pki_models_gen_csr_query)

Generates a self signed CA

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_cert_response import OtoroshiSslPkiModelsGenCertResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_csr_query import OtoroshiSslPkiModelsGenCsrQuery
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
    api_instance = pki_api.PkiApi(api_client)
    otoroshi_ssl_pki_models_gen_csr_query = OtoroshiSslPkiModelsGenCsrQuery(
        client=True,
        hosts=[
            "hosts_example",
        ],
        key=OtoroshiSslPkiModelsGenKeyPairQuery(
            algo="algo_example",
            size=1,
        ),
        include_aia=True,
        signature_alg="signature_alg_example",
        existing_serial_number=,
        duration=3.14,
        digest_alg="digest_alg_example",
        ca=True,
        name={
            "key": "key_example",
        },
        subject=,
    ) # OtoroshiSslPkiModelsGenCsrQuery | request body

    # example passing only required values which don't have defaults set
    try:
        # Generates a self signed CA
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca(otoroshi_ssl_pki_models_gen_csr_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_gen_self_signed_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_ssl_pki_models_gen_csr_query** | [**OtoroshiSslPkiModelsGenCsrQuery**](OtoroshiSslPkiModelsGenCsrQuery.md)| request body |

### Return type

[**OtoroshiSslPkiModelsGenCertResponse**](OtoroshiSslPkiModelsGenCertResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert**
> OtoroshiSslPkiModelsGenCertResponse otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert(otoroshi_ssl_pki_models_gen_csr_query)

Generates a self signed certificates

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_cert_response import OtoroshiSslPkiModelsGenCertResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_csr_query import OtoroshiSslPkiModelsGenCsrQuery
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
    api_instance = pki_api.PkiApi(api_client)
    otoroshi_ssl_pki_models_gen_csr_query = OtoroshiSslPkiModelsGenCsrQuery(
        client=True,
        hosts=[
            "hosts_example",
        ],
        key=OtoroshiSslPkiModelsGenKeyPairQuery(
            algo="algo_example",
            size=1,
        ),
        include_aia=True,
        signature_alg="signature_alg_example",
        existing_serial_number=,
        duration=3.14,
        digest_alg="digest_alg_example",
        ca=True,
        name={
            "key": "key_example",
        },
        subject=,
    ) # OtoroshiSslPkiModelsGenCsrQuery | request body

    # example passing only required values which don't have defaults set
    try:
        # Generates a self signed certificates
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert(otoroshi_ssl_pki_models_gen_csr_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_gen_self_signed_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_ssl_pki_models_gen_csr_query** | [**OtoroshiSslPkiModelsGenCsrQuery**](OtoroshiSslPkiModelsGenCsrQuery.md)| request body |

### Return type

[**OtoroshiSslPkiModelsGenCertResponse**](OtoroshiSslPkiModelsGenCertResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_gen_sub_ca**
> OtoroshiSslPkiModelsGenCertResponse otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(ca, otoroshi_ssl_pki_models_gen_csr_query)

Generates a sub-CA

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_cert_response import OtoroshiSslPkiModelsGenCertResponse
from openapi_client.model.otoroshi_ssl_pki_models_gen_csr_query import OtoroshiSslPkiModelsGenCsrQuery
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
    api_instance = pki_api.PkiApi(api_client)
    ca = "ca_example" # str | the ca parameter
    otoroshi_ssl_pki_models_gen_csr_query = OtoroshiSslPkiModelsGenCsrQuery(
        client=True,
        hosts=[
            "hosts_example",
        ],
        key=OtoroshiSslPkiModelsGenKeyPairQuery(
            algo="algo_example",
            size=1,
        ),
        include_aia=True,
        signature_alg="signature_alg_example",
        existing_serial_number=,
        duration=3.14,
        digest_alg="digest_alg_example",
        ca=True,
        name={
            "key": "key_example",
        },
        subject=,
    ) # OtoroshiSslPkiModelsGenCsrQuery | request body

    # example passing only required values which don't have defaults set
    try:
        # Generates a sub-CA
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_gen_sub_ca(ca, otoroshi_ssl_pki_models_gen_csr_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_gen_sub_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca** | **str**| the ca parameter |
 **otoroshi_ssl_pki_models_gen_csr_query** | [**OtoroshiSslPkiModelsGenCsrQuery**](OtoroshiSslPkiModelsGenCsrQuery.md)| request body |

### Return type

[**OtoroshiSslPkiModelsGenCertResponse**](OtoroshiSslPkiModelsGenCertResponse.md)

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

# **otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12**
> Done otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(body)

Import de .p12 file as client certificates

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
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
    api_instance = pki_api.PkiApi(api_client)
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Import de .p12 file as client certificates
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_import_cert_from_p12: %s\n" % e)
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

# **otoroshi_controllers_adminapi_pki_controller_sign_cert**
> OtoroshiSslPkiModelsSignCertResponse otoroshi_controllers_adminapi_pki_controller_sign_cert(ca, body)

Sign a certificate based on a CSR

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import pki_api
from openapi_client.model.otoroshi_ssl_pki_models_sign_cert_response import OtoroshiSslPkiModelsSignCertResponse
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
    api_instance = pki_api.PkiApi(api_client)
    ca = "ca_example" # str | the ca parameter
    body = "body_example" # str | request body

    # example passing only required values which don't have defaults set
    try:
        # Sign a certificate based on a CSR
        api_response = api_instance.otoroshi_controllers_adminapi_pki_controller_sign_cert(ca, body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PkiApi->otoroshi_controllers_adminapi_pki_controller_sign_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca** | **str**| the ca parameter |
 **body** | **str**| request body |

### Return type

[**OtoroshiSslPkiModelsSignCertResponse**](OtoroshiSslPkiModelsSignCertResponse.md)

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

