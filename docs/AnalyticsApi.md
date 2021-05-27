# openapi_client.AnalyticsApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_analytics_controller_filterable_events**](AnalyticsApi.md#otoroshi_controllers_adminapi_analytics_controller_filterable_events) | **GET** /api/events | Events for a service, apikey or group
[**otoroshi_controllers_adminapi_analytics_controller_filterable_stats**](AnalyticsApi.md#otoroshi_controllers_adminapi_analytics_controller_filterable_stats) | **GET** /api/stats | Statistic for a service, apikey or group
[**otoroshi_controllers_adminapi_analytics_controller_global_stats**](AnalyticsApi.md#otoroshi_controllers_adminapi_analytics_controller_global_stats) | **GET** /api/stats/global | Global statistic for your services
[**otoroshi_controllers_adminapi_analytics_controller_global_status**](AnalyticsApi.md#otoroshi_controllers_adminapi_analytics_controller_global_status) | **GET** /api/status/global | Global status of your services
[**otoroshi_controllers_adminapi_analytics_controller_services_status**](AnalyticsApi.md#otoroshi_controllers_adminapi_analytics_controller_services_status) | **POST** /api/status | Status for some/all services over time
[**otoroshi_controllers_adminapi_templates_controller_template_spec**](AnalyticsApi.md#otoroshi_controllers_adminapi_templates_controller_template_spec) | **GET** /api/events/_template | Returns a template that extract possible fields out of a Gateway event


# **otoroshi_controllers_adminapi_analytics_controller_filterable_events**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_analytics_controller_filterable_events()

Events for a service, apikey or group

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Events for a service, apikey or group
        api_response = api_instance.otoroshi_controllers_adminapi_analytics_controller_filterable_events()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->otoroshi_controllers_adminapi_analytics_controller_filterable_events: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **otoroshi_controllers_adminapi_analytics_controller_filterable_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_analytics_controller_filterable_stats()

Statistic for a service, apikey or group

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Statistic for a service, apikey or group
        api_response = api_instance.otoroshi_controllers_adminapi_analytics_controller_filterable_stats()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->otoroshi_controllers_adminapi_analytics_controller_filterable_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **otoroshi_controllers_adminapi_analytics_controller_global_stats**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_analytics_controller_global_stats()

Global statistic for your services

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Global statistic for your services
        api_response = api_instance.otoroshi_controllers_adminapi_analytics_controller_global_stats()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->otoroshi_controllers_adminapi_analytics_controller_global_stats: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **otoroshi_controllers_adminapi_analytics_controller_global_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_analytics_controller_global_status()

Global status of your services

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Global status of your services
        api_response = api_instance.otoroshi_controllers_adminapi_analytics_controller_global_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->otoroshi_controllers_adminapi_analytics_controller_global_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **otoroshi_controllers_adminapi_analytics_controller_services_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} otoroshi_controllers_adminapi_analytics_controller_services_status(service_descriptor_list)

Status for some/all services over time

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
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
    api_instance = analytics_api.AnalyticsApi(api_client)
    service_descriptor_list = ServiceDescriptorList([
        OtoroshiModelsServiceDescriptor(
            build_mode=True,
            hosts=[
                "hosts_example",
            ],
            private_app=True,
            local_scheme="local_scheme_example",
            auth_config_ref=,
            issue_cert_ca=,
            root="root_example",
            name="name_example",
            additional_headers={
                "key": "key_example",
            },
            domain="domain_example",
            client_config=OtoroshiModelsClientConfig(
                connection_timeout=1,
                use_circuit_breaker=True,
                retry_initial_delay=1,
                proxy=,
                call_timeout=1,
                call_and_stream_timeout=1,
                global_timeout=1,
                max_errors=1,
                retries=1,
                backoff_factor=1,
                custom_timeouts=[
                    OtoroshiModelsCustomTimeouts(
                        path="path_example",
                        call_and_stream_timeout=1,
                        call_timeout=1,
                        idle_timeout=1,
                        global_timeout=1,
                        connection_timeout=1,
                    ),
                ],
                idle_timeout=1,
                sample_interval=1,
            ),
            matching_root=,
            force_https=True,
            local_host="local_host_example",
            send_otoroshi_headers_back=True,
            health_check=OtoroshiModelsHealthCheck(
                enabled=True,
                url="url_example",
            ),
            strictly_private=True,
            detect_api_key_sooner=True,
            allow_http10=True,
            subdomain="subdomain_example",
            paths=[
                "paths_example",
            ],
            strip_path=True,
            sec_com_algo_challenge_oto_to_back=OtoroshiModelsAlgoSettings(),
            api_key_constraints=OtoroshiModelsApiKeyConstraints(
                custom_headers_auth=OtoroshiModelsCustomHeadersAuthConstraints(
                    enabled=True,
                    client_id_header_name=,
                    client_secret_header_name=,
                ),
                routing=OtoroshiModelsApiKeyRouteMatcher(
                    one_tag_in=[
                        "one_tag_in_example",
                    ],
                    none_meta_keys_in=[
                        "none_meta_keys_in_example",
                    ],
                    one_meta_in={
                        "key": "key_example",
                    },
                    one_meta_key_in=[
                        "one_meta_key_in_example",
                    ],
                    all_meta_keys_in=[
                        "all_meta_keys_in_example",
                    ],
                    none_tag_in=[
                        "none_tag_in_example",
                    ],
                    all_tags_in=[
                        "all_tags_in_example",
                    ],
                    all_meta_in={
                        "key": "key_example",
                    },
                    none_meta_in={
                        "key": "key_example",
                    },
                ),
                client_id_auth=OtoroshiModelsClientIdAuthConstraints(
                    enabled=True,
                    header_name=,
                    query_name=,
                ),
                jwt_auth=OtoroshiModelsJwtAuthConstraints(
                    key_pair_signed=True,
                    cookie_name=,
                    query_name=,
                    header_name=,
                    secret_signed=True,
                    max_jwt_lifespan_secs=,
                    enabled=True,
                    include_request_attributes=True,
                ),
                basic_auth=OtoroshiModelsBasicAuthConstraints(
                    enabled=True,
                    header_name=,
                    query_name=,
                ),
            ),
            env="env_example",
            x_forwarded_headers=True,
            transformer_refs=[
                "transformer_refs_example",
            ],
            enabled=True,
            gzip=OtoroshiUtilsGzipGzipConfig(
                compression_level=1,
                black_list=[
                    "black_list_example",
                ],
                chunked_threshold=1,
                excluded_patterns=[
                    "excluded_patterns_example",
                ],
                buffer_size=1,
                white_list=[
                    "white_list_example",
                ],
                enabled=True,
            ),
            send_info_token=True,
            tcp_udp_tunneling=True,
            remove_headers_out=[
                "remove_headers_out_example",
            ],
            use_akka_http_client=True,
            maintenance_mode=True,
            id="id_example",
            remove_headers_in=[
                "remove_headers_in_example",
            ],
            log_analytics_on_server=True,
            sec_com_algo_info_token=OtoroshiModelsAlgoSettings(),
            user_facing=True,
            transformer_config={},
            client_validator_ref=,
            security_excluded_patterns=[
                "security_excluded_patterns_example",
            ],
            ip_filtering=OtoroshiModelsIpFiltering(
                whitelist=[
                    "whitelist_example",
                ],
                blacklist=[
                    "blacklist_example",
                ],
            ),
            targets=[
                OtoroshiModelsTarget(
                    host="host_example",
                    weight=1,
                    protocol="protocol_example",
                    predicate=OtoroshiModelsTargetPredicate(),
                    ip_address=,
                    mtls_config=OtoroshiUtilsHttpMtlsConfig(
                        mtls=True,
                        loose=True,
                        trust_all=True,
                        trusted_certs=[
                            "trusted_certs_example",
                        ],
                        certs=[
                            "certs_example",
                        ],
                    ),
                    scheme="scheme_example",
                ),
            ],
            redirection=OtoroshiModelsRedirectionSettings(
                enabled=True,
                code=1,
                to="to_example",
            ),
            tags=[
                "tags_example",
            ],
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
            override_host=True,
            access_validator=OtoroshiScriptAccessValidatorRef(
                enabled=True,
                excluded_patterns=[
                    "excluded_patterns_example",
                ],
                refs=[
                    "refs_example",
                ],
                config={},
            ),
            send_state_challenge=True,
            chaos_config=OtoroshiModelsChaosConfig(
                bad_responses_fault_config=,
                large_request_fault_config=,
                large_response_fault_config=,
                latency_injection_fault_config=,
                enabled=True,
            ),
            sec_com_info_token_version=OtoroshiModelsSecComInfoTokenVersion("Legacy"),
            additional_headers_out={
                "key": "key_example",
            },
            sec_com_headers=OtoroshiModelsSecComHeaders(
                claim_request_name=,
                state_request_name=,
                state_response_name=,
            ),
            matching_headers={
                "key": "key_example",
            },
            sec_com_algo_challenge_back_to_oto=OtoroshiModelsAlgoSettings(),
            sec_com_use_same_algo=True,
            use_new_ws_client=True,
            sec_com_excluded_patterns=[
                "sec_com_excluded_patterns_example",
            ],
            redirect_to_local=True,
            enforce_secure_communication=True,
            missing_only_headers_out={
                "key": "key_example",
            },
            sec_com_settings=OtoroshiModelsAlgoSettings(),
            handle_legacy_domain=True,
            canary=OtoroshiModelsCanary(
                enabled=True,
                traffic=3.14,
                targets=[
                    OtoroshiModelsTarget(
                        host="host_example",
                        weight=1,
                        protocol="protocol_example",
                        predicate=OtoroshiModelsTargetPredicate(),
                        ip_address=,
                        mtls_config=OtoroshiUtilsHttpMtlsConfig(
                            mtls=True,
                            loose=True,
                            trust_all=True,
                            trusted_certs=[
                                "trusted_certs_example",
                            ],
                            certs=[
                                "certs_example",
                            ],
                        ),
                        scheme="scheme_example",
                    ),
                ],
                root="root_example",
            ),
            location=OtoroshiModelsEntityLocation(
                tenant="tenant_example",
                teams=[
                    "teams_example",
                ],
            ),
            plugins=OtoroshiScriptPluginsPlugins(
                config={},
                enabled=True,
                excluded=[
                    "excluded_example",
                ],
                refs=[
                    "refs_example",
                ],
            ),
            sec_com_ttl=3.14,
            description="description_example",
            sec_com_version=OtoroshiModelsSecComVersion("V1"),
            pre_routing=OtoroshiScriptPreRoutingRef(
                enabled=True,
                excluded_patterns=[
                    "excluded_patterns_example",
                ],
                refs=[
                    "refs_example",
                ],
                config={},
            ),
            groups=[
                "groups_example",
            ],
            read_only=True,
            private_patterns=[
                "private_patterns_example",
            ],
            targets_load_balancing=OtoroshiModelsLoadBalancing(
                type="BestResponseTime",
                ratio=3.14,
            ),
            cors=OtoroshiModelsCorsSettings(
                enabled=True,
                allow_credentials=True,
                max_age=,
                allow_methods=[
                    "allow_methods_example",
                ],
                allow_headers=[
                    "allow_headers_example",
                ],
                excluded_patterns=[
                    "excluded_patterns_example",
                ],
                expose_headers=[
                    "expose_headers_example",
                ],
                allow_origin="allow_origin_example",
            ),
            metadata={
                "key": "key_example",
            },
            public_patterns=[
                "public_patterns_example",
            ],
            api=OtoroshiModelsApiDescriptor(
                expose_api=True,
                open_api_descriptor_url=,
            ),
            missing_only_headers_in={
                "key": "key_example",
            },
            issue_cert=True,
            headers_verification={
                "key": "key_example",
            },
            jwt_verifier=OtoroshiModelsJwtVerifier(),
            lets_encrypt=True,
        ),
    ]) # ServiceDescriptorList | request body

    # example passing only required values which don't have defaults set
    try:
        # Status for some/all services over time
        api_response = api_instance.otoroshi_controllers_adminapi_analytics_controller_services_status(service_descriptor_list)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->otoroshi_controllers_adminapi_analytics_controller_services_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_descriptor_list** | [**ServiceDescriptorList**](ServiceDescriptorList.md)| request body |

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

# **otoroshi_controllers_adminapi_templates_controller_template_spec**
> Any otoroshi_controllers_adminapi_templates_controller_template_spec()

Returns a template that extract possible fields out of a Gateway event

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import analytics_api
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
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a template that extract possible fields out of a Gateway event
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_template_spec()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnalyticsApi->otoroshi_controllers_adminapi_templates_controller_template_spec: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Any**](Any.md)

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

