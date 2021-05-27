# OtoroshiModelsGlobalConfig

The global config (dynamic) for otoroshi

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geolocation_settings** | [**OtoroshiModelsGeolocationSettings**](OtoroshiModelsGeolocationSettings.md) |  | [optional] 
**alerts_emails** | **[str]** | Email addresses that will receive all Otoroshi alert events | [optional] 
**throttling_quota** | **int** | Authorized number of calls per second globally, measured on 10 seconds | [optional] 
**max_webhook_size** | **int** | Max number of items in webhooks | [optional] 
**max_concurrent_requests** | **int** | The number of authorized request processed at the same time | [optional] 
**clever_settings** | **dict** | Optional CleverCloud configuration | [optional] 
**endless_ip_addresses** | **[str]** | IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros | [optional] 
**plugins** | [**OtoroshiScriptPluginsPlugins**](OtoroshiScriptPluginsPlugins.md) |  | [optional] 
**kafka_config** | **dict** | Global kafka settings. deprecated | [optional] 
**max_logs_size** | **int** | Number of events kept locally | [optional] 
**proxies** | [**OtoroshiModelsProxies**](OtoroshiModelsProxies.md) |  | [optional] 
**enable_embedded_metrics** | **bool** | Enable embedded metrics | [optional] 
**elastic_reads_config** | **dict** | Config. for elastic reads | [optional] 
**tags** | **[str]** | Entity tags | [optional] 
**limit_concurrent_requests** | **bool** | If enabled, Otoroshi will reject new request if too much at the same time | [optional] 
**use_akka_http_client** | **bool** | Globally use akka http client for everything | [optional] 
**elastic_writes_configs** | [**[OtoroshiModelsElasticAnalyticsConfig]**](OtoroshiModelsElasticAnalyticsConfig.md) | Configs. for Elastic writes | [optional] 
**log_analytics_on_server** | **bool** | Log analytics event on the server | [optional] 
**metadata** | **{str: (str,)}** | Entity metadata | [optional] 
**api_read_only** | **bool** | If enabled, Admin API won&#39;t be able to write/update/delete entities | [optional] 
**back_office_auth_ref** | **dict** | Id of the auth module used for otoroshi-ui login | [optional] 
**stream_entity_only** | **bool** | HTTP will be streamed only. Doesn&#39;t work with old browsers | [optional] 
**otoroshi_id** | **str** | Unique id for this otoroshi instance | [optional] 
**mailer_settings** | **dict** | Optional mailer configuration | [optional] 
**lines** | **[str]** | Possibles lines for Otoroshi | [optional] 
**middle_fingers** | **bool** | Use middle finger emoji as a response character for endless HTTP responses | [optional] 
**analytics_webhooks** | [**[OtoroshiModelsWebhook]**](OtoroshiModelsWebhook.md) | Webhook that will receive all internal Otoroshi events | [optional] 
**auto_cert** | [**OtoroshiModelsAutoCert**](OtoroshiModelsAutoCert.md) |  | [optional] 
**maintenance_mode** | **bool** | Global maintenant mode | [optional] 
**lets_encrypt_settings** | [**OtoroshiUtilsLetsencryptLetsEncryptSettings**](OtoroshiUtilsLetsencryptLetsEncryptSettings.md) |  | [optional] 
**snow_monkey_config** | [**OtoroshiModelsSnowMonkeyConfig**](OtoroshiModelsSnowMonkeyConfig.md) |  | [optional] 
**scripts** | [**OtoroshiModelsGlobalScripts**](OtoroshiModelsGlobalScripts.md) |  | [optional] 
**per_ip_throttling_quota** | **int** | Authorized number of calls per second globally per IP address, measured on 10 seconds | [optional] 
**use_circuit_breakers** | **bool** | If enabled, services will be authorized to use circuit breakers | [optional] 
**max_http10_response_size** | **int** | The max size in bytes of an HTTP 1.0 response | [optional] 
**tls_settings** | [**OtoroshiModelsTlsSettings**](OtoroshiModelsTlsSettings.md) |  | [optional] 
**statsd_config** | **dict** | Statsd settings (agent connection) | [optional] 
**auto_link_to_default_group** | **bool** | If not defined, every new service descriptor will be added to the default group | [optional] 
**alerts_webhooks** | [**[OtoroshiModelsWebhook]**](OtoroshiModelsWebhook.md) | Webhook that will receive all Otoroshi alert events | [optional] 
**ip_filtering** | [**OtoroshiModelsIpFiltering**](OtoroshiModelsIpFiltering.md) |  | [optional] 
**u2f_login_only** | **bool** | If enabled, login to backoffice through Auth0 will be disabled | [optional] 
**user_agent_settings** | [**OtoroshiModelsUserAgentSettings**](OtoroshiModelsUserAgentSettings.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


