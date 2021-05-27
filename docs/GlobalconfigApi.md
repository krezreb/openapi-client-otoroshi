# openapi_client.GlobalconfigApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_global_config_controller_global_config**](GlobalconfigApi.md#otoroshi_controllers_adminapi_global_config_controller_global_config) | **GET** /api/globalconfig | Get the global config
[**otoroshi_controllers_adminapi_global_config_controller_patch_global_config**](GlobalconfigApi.md#otoroshi_controllers_adminapi_global_config_controller_patch_global_config) | **PATCH** /api/globalconfig | Update (with json-patch) the global config
[**otoroshi_controllers_adminapi_global_config_controller_update_global_config**](GlobalconfigApi.md#otoroshi_controllers_adminapi_global_config_controller_update_global_config) | **PUT** /api/globalconfig | Update the global config
[**otoroshi_controllers_adminapi_templates_controller_initiate_global_config**](GlobalconfigApi.md#otoroshi_controllers_adminapi_templates_controller_initiate_global_config) | **GET** /api/globalconfig/_template | Creates a new GlobalConfig from a template


# **otoroshi_controllers_adminapi_global_config_controller_global_config**
> OtoroshiModelsGlobalConfig otoroshi_controllers_adminapi_global_config_controller_global_config()

Get the global config

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import globalconfig_api
from openapi_client.model.otoroshi_models_global_config import OtoroshiModelsGlobalConfig
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
    api_instance = globalconfig_api.GlobalconfigApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the global config
        api_response = api_instance.otoroshi_controllers_adminapi_global_config_controller_global_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalconfigApi->otoroshi_controllers_adminapi_global_config_controller_global_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsGlobalConfig**](OtoroshiModelsGlobalConfig.md)

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

# **otoroshi_controllers_adminapi_global_config_controller_patch_global_config**
> OtoroshiModelsGlobalConfig otoroshi_controllers_adminapi_global_config_controller_patch_global_config(patch_body)

Update (with json-patch) the global config

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import globalconfig_api
from openapi_client.model.otoroshi_models_global_config import OtoroshiModelsGlobalConfig
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.patch_body import PatchBody
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
    api_instance = globalconfig_api.GlobalconfigApi(api_client)
    patch_body = PatchBody([
        PatchDocument(
            op="add",
            path="path_example",
            value={},
            _from="_from_example",
        ),
    ]) # PatchBody | request body

    # example passing only required values which don't have defaults set
    try:
        # Update (with json-patch) the global config
        api_response = api_instance.otoroshi_controllers_adminapi_global_config_controller_patch_global_config(patch_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalconfigApi->otoroshi_controllers_adminapi_global_config_controller_patch_global_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_body** | [**PatchBody**](PatchBody.md)| request body |

### Return type

[**OtoroshiModelsGlobalConfig**](OtoroshiModelsGlobalConfig.md)

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

# **otoroshi_controllers_adminapi_global_config_controller_update_global_config**
> OtoroshiModelsGlobalConfig otoroshi_controllers_adminapi_global_config_controller_update_global_config(otoroshi_models_global_config)

Update the global config

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import globalconfig_api
from openapi_client.model.otoroshi_models_global_config import OtoroshiModelsGlobalConfig
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
    api_instance = globalconfig_api.GlobalconfigApi(api_client)
    otoroshi_models_global_config = OtoroshiModelsGlobalConfig(
        geolocation_settings=OtoroshiModelsGeolocationSettings(),
        alerts_emails=[
            "alerts_emails_example",
        ],
        throttling_quota=1,
        max_webhook_size=1,
        max_concurrent_requests=1,
        clever_settings=,
        endless_ip_addresses=[
            "endless_ip_addresses_example",
        ],
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
        kafka_config=,
        max_logs_size=1,
        proxies=OtoroshiModelsProxies(
            elastic=,
            events_webhooks=,
            jwk=,
            auth=,
            clevercloud=,
            alert_emails=,
            authority=,
            services=,
        ),
        enable_embedded_metrics=True,
        elastic_reads_config=,
        tags=[
            "tags_example",
        ],
        limit_concurrent_requests=True,
        use_akka_http_client=True,
        elastic_writes_configs=[
            OtoroshiModelsElasticAnalyticsConfig(
                cluster_uri="cluster_uri_example",
                headers={
                    "key": "key_example",
                },
                password=,
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
                index=,
                type="type_example",
                user=,
            ),
        ],
        log_analytics_on_server=True,
        metadata={
            "key": "key_example",
        },
        api_read_only=True,
        back_office_auth_ref=,
        stream_entity_only=True,
        otoroshi_id="otoroshi_id_example",
        mailer_settings=,
        lines=[
            "lines_example",
        ],
        middle_fingers=True,
        analytics_webhooks=[
            OtoroshiModelsWebhook(
                headers={
                    "key": "key_example",
                },
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
                type="elastic",
                url="url_example",
            ),
        ],
        auto_cert=OtoroshiModelsAutoCert(
            allowed=[
                "allowed_example",
            ],
            enabled=True,
            reply_nicely=True,
            not_allowed=[
                "not_allowed_example",
            ],
            ca_ref=,
        ),
        maintenance_mode=True,
        lets_encrypt_settings=OtoroshiUtilsLetsencryptLetsEncryptSettings(
            private_key="private_key_example",
            contacts=[
                "contacts_example",
            ],
            emails=[
                "emails_example",
            ],
            enabled=True,
            public_key="public_key_example",
            server="server_example",
        ),
        snow_monkey_config=OtoroshiModelsSnowMonkeyConfig(
            dry_run=True,
            outage_duration_to=3.14,
            chaos_config=OtoroshiModelsChaosConfig(
                bad_responses_fault_config=,
                large_request_fault_config=,
                large_response_fault_config=,
                latency_injection_fault_config=,
                enabled=True,
            ),
            times_per_day=1,
            outage_duration_from=3.14,
            start_time="start_time_example",
            include_user_facing_descriptors=True,
            target_groups=[
                "target_groups_example",
            ],
            enabled=True,
            stop_time="stop_time_example",
            outage_strategy=OtoroshiModelsOutageStrategy("AllServicesPerGroup"),
        ),
        scripts=OtoroshiModelsGlobalScripts(
            job_config={},
            enabled=True,
            transformers_config={},
            transformers_refs=[
                "transformers_refs_example",
            ],
            pre_route_refs=[
                "pre_route_refs_example",
            ],
            sink_config={},
            job_refs=[
                "job_refs_example",
            ],
            validator_refs=[
                "validator_refs_example",
            ],
            sink_refs=[
                "sink_refs_example",
            ],
            pre_route_config={},
            validator_config={},
        ),
        per_ip_throttling_quota=1,
        use_circuit_breakers=True,
        max_http10_response_size=1,
        tls_settings=OtoroshiModelsTlsSettings(
            default_domain=,
            random_if_not_found=True,
        ),
        statsd_config=,
        auto_link_to_default_group=True,
        alerts_webhooks=[
            OtoroshiModelsWebhook(
                headers={
                    "key": "key_example",
                },
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
                type="elastic",
                url="url_example",
            ),
        ],
        ip_filtering=OtoroshiModelsIpFiltering(
            whitelist=[
                "whitelist_example",
            ],
            blacklist=[
                "blacklist_example",
            ],
        ),
        u2f_login_only=True,
        user_agent_settings=OtoroshiModelsUserAgentSettings(
            enabled=True,
        ),
    ) # OtoroshiModelsGlobalConfig | request body

    # example passing only required values which don't have defaults set
    try:
        # Update the global config
        api_response = api_instance.otoroshi_controllers_adminapi_global_config_controller_update_global_config(otoroshi_models_global_config)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalconfigApi->otoroshi_controllers_adminapi_global_config_controller_update_global_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otoroshi_models_global_config** | [**OtoroshiModelsGlobalConfig**](OtoroshiModelsGlobalConfig.md)| request body |

### Return type

[**OtoroshiModelsGlobalConfig**](OtoroshiModelsGlobalConfig.md)

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

# **otoroshi_controllers_adminapi_templates_controller_initiate_global_config**
> OtoroshiModelsGlobalConfig otoroshi_controllers_adminapi_templates_controller_initiate_global_config()

Creates a new GlobalConfig from a template

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import globalconfig_api
from openapi_client.model.otoroshi_models_global_config import OtoroshiModelsGlobalConfig
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
    api_instance = globalconfig_api.GlobalconfigApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Creates a new GlobalConfig from a template
        api_response = api_instance.otoroshi_controllers_adminapi_templates_controller_initiate_global_config()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalconfigApi->otoroshi_controllers_adminapi_templates_controller_initiate_global_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OtoroshiModelsGlobalConfig**](OtoroshiModelsGlobalConfig.md)

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

