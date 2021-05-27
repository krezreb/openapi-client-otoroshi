# openapi_client.AdminsApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_templates_controller_create_from_template_simple**](AdminsApi.md#otoroshi_controllers_adminapi_templates_controller_create_from_template_simple) | **POST** /api/admins/simple/_template | Creates a new Template from a template
[**otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn**](AdminsApi.md#otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn) | **POST** /api/admins/webauthn/_template | Creates a new Template from a template
[**otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin**](AdminsApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin) | **GET** /api/admins/simple/_template | Creates a new SimpleAdmin from a template
[**otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin**](AdminsApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin) | **GET** /api/admins/webauthn/_template | Creates a new WebauthnAdmin from a template
[**otoroshi_controllers_adminapi_users_controller_delete_admin**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_delete_admin) | **DELETE** /api/admins/simple/{username} | Deletes an admin
[**otoroshi_controllers_adminapi_users_controller_register_simple_admin**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_register_simple_admin) | **POST** /api/admins/simple | Register an admin user
[**otoroshi_controllers_adminapi_users_controller_register_web_authn_admin**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_register_web_authn_admin) | **POST** /api/admins/webauthn | Register a webauthn admin user
[**otoroshi_controllers_adminapi_users_controller_simple_admins**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_simple_admins) | **GET** /api/admins/simple | Returns all admins
[**otoroshi_controllers_adminapi_users_controller_update_admin**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_update_admin) | **PUT** /api/admins/simple/{username} | Updates an admin
[**otoroshi_controllers_adminapi_users_controller_update_web_authn_admin**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_update_web_authn_admin) | **PUT** /api/admins/webauthn/{username} | Updates a webauthn admin
[**otoroshi_controllers_adminapi_users_controller_web_authn_admins**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_web_authn_admins) | **GET** /api/admins/webauthn | Returns all webauthn admin
[**otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin**](AdminsApi.md#otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin) | **DELETE** /api/admins/webauthn/{username}/{id} | Deletes a webauthn admin


# **otoroshi_controllers_adminapi_templates_controller_create_from_template_simple**
> OtoroshiModelsOtoroshiAdmin otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(body)

Creates a new Template from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.otoroshi_models_otoroshi_admin import OtoroshiModelsOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Template from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_create_from_template_simple(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_templates_controller_create_from_template_simple: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**OtoroshiModelsOtoroshiAdmin**](OtoroshiModelsOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn**
> OtoroshiModelsOtoroshiAdmin otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(body)

Creates a new Template from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.otoroshi_models_otoroshi_admin import OtoroshiModelsOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | request body

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Template from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_templates_controller_create_from_template_webauthn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| request body |

### Return type

[**OtoroshiModelsOtoroshiAdmin**](OtoroshiModelsOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin**
> OtoroshiModelsSimpleOtoroshiAdmin otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin()

Creates a new SimpleAdmin from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_simple_otoroshi_admin import OtoroshiModelsSimpleOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new SimpleAdmin from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_templates_controller_initiate_simple_admin: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsSimpleOtoroshiAdmin**](OtoroshiModelsSimpleOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin**
> OtoroshiModelsSimpleOtoroshiAdmin otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin()

Creates a new WebauthnAdmin from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_simple_otoroshi_admin import OtoroshiModelsSimpleOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new WebauthnAdmin from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_templates_controller_initiate_webauthn_admin: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsSimpleOtoroshiAdmin**](OtoroshiModelsSimpleOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_users_controller_delete_admin**
> Done otoroshi_controllers_adminapi_users_controller_delete_admin(username)

Deletes an admin

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
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
    api_instance = admins_api.AdminsApi(api_client)
    username = "username_example" # str | the username parameter

    # example passing only required values which don't have defaults set
    try:
        # Deletes an admin
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_delete_admin(username)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_delete_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username parameter |

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

# **otoroshi_controllers_adminapi_users_controller_register_simple_admin**
> OtoroshiModelsSimpleOtoroshiAdmin otoroshi_controllers_adminapi_users_controller_register_simple_admin(otoroshi_models_simple_otoroshi_admin)

Register an admin user

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_simple_otoroshi_admin import OtoroshiModelsSimpleOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)
    otoroshi_models_simple_otoroshi_admin = OtoroshiModelsSimpleOtoroshiAdmin(
        created_at=3.14,
        metadata={
            "key": "key_example",
        },
        password="password_example",
        rights=OtoroshiModelsUserRights(
            rights=[
                OtoroshiModelsUserRight(
                    tenant=OtoroshiModelsTenantAccess(
                        can_write=True,
                        value="value_example",
                        can_read=True,
                    ),
                    teams=[
                        OtoroshiModelsTeamAccess(
                            can_read=True,
                            value="value_example",
                            can_write=True,
                        ),
                    ],
                ),
            ],
        ),
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        typ=OtoroshiModelsOtoroshiAdminType("SIMPLE"),
        label="label_example",
        type="simple",
        username="username_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsSimpleOtoroshiAdmin | request body

    # example passing only required values which don't have defaults set
    try:
        # Register an admin user
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_register_simple_admin(otoroshi_models_simple_otoroshi_admin)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_register_simple_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_simple_otoroshi_admin** | [**OtoroshiModelsSimpleOtoroshiAdmin**](OtoroshiModelsSimpleOtoroshiAdmin.md)| request body |

### Return type

[**OtoroshiModelsSimpleOtoroshiAdmin**](OtoroshiModelsSimpleOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_users_controller_register_web_authn_admin**
> OtoroshiModelsWebAuthnOtoroshiAdmin otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(otoroshi_models_web_authn_otoroshi_admin)

Register a webauthn admin user

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.otoroshi_models_web_authn_otoroshi_admin import OtoroshiModelsWebAuthnOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)
    otoroshi_models_web_authn_otoroshi_admin = OtoroshiModelsWebAuthnOtoroshiAdmin(
        created_at=3.14,
        metadata={
            "key": "key_example",
        },
        password="password_example",
        credentials={
            "key": {},
        },
        rights=OtoroshiModelsUserRights(
            rights=[
                OtoroshiModelsUserRight(
                    tenant=OtoroshiModelsTenantAccess(
                        can_write=True,
                        value="value_example",
                        can_read=True,
                    ),
                    teams=[
                        OtoroshiModelsTeamAccess(
                            can_read=True,
                            value="value_example",
                            can_write=True,
                        ),
                    ],
                ),
            ],
        ),
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        typ=OtoroshiModelsOtoroshiAdminType("SIMPLE"),
        handle="handle_example",
        label="label_example",
        type="simple",
        username="username_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsWebAuthnOtoroshiAdmin | request body

    # example passing only required values which don't have defaults set
    try:
        # Register a webauthn admin user
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_register_web_authn_admin(otoroshi_models_web_authn_otoroshi_admin)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_register_web_authn_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_web_authn_otoroshi_admin** | [**OtoroshiModelsWebAuthnOtoroshiAdmin**](OtoroshiModelsWebAuthnOtoroshiAdmin.md)| request body |

### Return type

[**OtoroshiModelsWebAuthnOtoroshiAdmin**](OtoroshiModelsWebAuthnOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_users_controller_simple_admins**
> SimpleAdminList otoroshi_controllers_adminapi_users_controller_simple_admins()

Returns all admins

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.simple_admin_list import SimpleAdminList
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
    api_instance = admins_api.AdminsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all admins
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_simple_admins()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_simple_admins: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SimpleAdminList**](SimpleAdminList.md)

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

# **otoroshi_controllers_adminapi_users_controller_update_admin**
> OtoroshiModelsSimpleOtoroshiAdmin otoroshi_controllers_adminapi_users_controller_update_admin(username, otoroshi_models_simple_otoroshi_admin)

Updates an admin

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.otoroshi_models_simple_otoroshi_admin import OtoroshiModelsSimpleOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)
    username = "username_example" # str | the username parameter
    otoroshi_models_simple_otoroshi_admin = OtoroshiModelsSimpleOtoroshiAdmin(
        created_at=3.14,
        metadata={
            "key": "key_example",
        },
        password="password_example",
        rights=OtoroshiModelsUserRights(
            rights=[
                OtoroshiModelsUserRight(
                    tenant=OtoroshiModelsTenantAccess(
                        can_write=True,
                        value="value_example",
                        can_read=True,
                    ),
                    teams=[
                        OtoroshiModelsTeamAccess(
                            can_read=True,
                            value="value_example",
                            can_write=True,
                        ),
                    ],
                ),
            ],
        ),
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        typ=OtoroshiModelsOtoroshiAdminType("SIMPLE"),
        label="label_example",
        type="simple",
        username="username_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsSimpleOtoroshiAdmin | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates an admin
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_update_admin(username, otoroshi_models_simple_otoroshi_admin)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_update_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username parameter |
 **otoroshi_models_simple_otoroshi_admin** | [**OtoroshiModelsSimpleOtoroshiAdmin**](OtoroshiModelsSimpleOtoroshiAdmin.md)| request body |

### Return type

[**OtoroshiModelsSimpleOtoroshiAdmin**](OtoroshiModelsSimpleOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_users_controller_update_web_authn_admin**
> OtoroshiModelsWebAuthnOtoroshiAdmin otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(username, otoroshi_models_web_authn_otoroshi_admin)

Updates a webauthn admin

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.otoroshi_models_web_authn_otoroshi_admin import OtoroshiModelsWebAuthnOtoroshiAdmin
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
    api_instance = admins_api.AdminsApi(api_client)
    username = "username_example" # str | the username parameter
    otoroshi_models_web_authn_otoroshi_admin = OtoroshiModelsWebAuthnOtoroshiAdmin(
        created_at=3.14,
        metadata={
            "key": "key_example",
        },
        password="password_example",
        credentials={
            "key": {},
        },
        rights=OtoroshiModelsUserRights(
            rights=[
                OtoroshiModelsUserRight(
                    tenant=OtoroshiModelsTenantAccess(
                        can_write=True,
                        value="value_example",
                        can_read=True,
                    ),
                    teams=[
                        OtoroshiModelsTeamAccess(
                            can_read=True,
                            value="value_example",
                            can_write=True,
                        ),
                    ],
                ),
            ],
        ),
        location=OtoroshiModelsEntityLocation(
            tenant="tenant_example",
            teams=[
                "teams_example",
            ],
        ),
        typ=OtoroshiModelsOtoroshiAdminType("SIMPLE"),
        handle="handle_example",
        label="label_example",
        type="simple",
        username="username_example",
        tags=[
            "tags_example",
        ],
    ) # OtoroshiModelsWebAuthnOtoroshiAdmin | request body

    # example passing only required values which don't have defaults set
    try:
        # Updates a webauthn admin
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_update_web_authn_admin(username, otoroshi_models_web_authn_otoroshi_admin)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_update_web_authn_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username parameter |
 **otoroshi_models_web_authn_otoroshi_admin** | [**OtoroshiModelsWebAuthnOtoroshiAdmin**](OtoroshiModelsWebAuthnOtoroshiAdmin.md)| request body |

### Return type

[**OtoroshiModelsWebAuthnOtoroshiAdmin**](OtoroshiModelsWebAuthnOtoroshiAdmin.md)

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

# **otoroshi_controllers_adminapi_users_controller_web_authn_admins**
> WebauthnAdminList otoroshi_controllers_adminapi_users_controller_web_authn_admins()

Returns all webauthn admin

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.webauthn_admin_list import WebauthnAdminList
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
    api_instance = admins_api.AdminsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns all webauthn admin
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_web_authn_admins()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_web_authn_admins: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WebauthnAdminList**](WebauthnAdminList.md)

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

# **otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin**
> Done otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(username, id)

Deletes a webauthn admin

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import admins_api
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
    api_instance = admins_api.AdminsApi(api_client)
    username = "username_example" # str | the username parameter
    id = "id_example" # str | the id parameter

    # example passing only required values which don't have defaults set
    try:
        # Deletes a webauthn admin
        api_response = api_instance.otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin(username, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AdminsApi->otoroshi_controllers_adminapi_users_controller_web_authn_delete_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username parameter |
 **id** | **str**| the id parameter |

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

