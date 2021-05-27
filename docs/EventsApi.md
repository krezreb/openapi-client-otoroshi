# openapi_client.EventsApi

All URIs are relative to *http://otoroshi-api.oto.tools:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**otoroshi_controllers_adminapi_events_controller_alert_events**](EventsApi.md#otoroshi_controllers_adminapi_events_controller_alert_events) | **GET** /api/alert/events | Get all events of type AlertEvent
[**otoroshi_controllers_adminapi_events_controller_audit_events**](EventsApi.md#otoroshi_controllers_adminapi_events_controller_audit_events) | **GET** /api/audit/events | Get all events of type AuditEvent


# **otoroshi_controllers_adminapi_events_controller_alert_events**
> AlertEventList otoroshi_controllers_adminapi_events_controller_alert_events()

Get all events of type AlertEvent

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alert_event_list import AlertEventList
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
    api_instance = events_api.EventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all events of type AlertEvent
        api_response = api_instance.otoroshi_controllers_adminapi_events_controller_alert_events()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->otoroshi_controllers_adminapi_events_controller_alert_events: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertEventList**](AlertEventList.md)

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

# **otoroshi_controllers_adminapi_events_controller_audit_events**
> AuditEventList otoroshi_controllers_adminapi_events_controller_audit_events()

Get all events of type AuditEvent

### Example

* Basic Authentication (otoroshi_auth):
```python
import time
import openapi_client
from openapi_client.api import events_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.audit_event_list import AuditEventList
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
    api_instance = events_api.EventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all events of type AuditEvent
        api_response = api_instance.otoroshi_controllers_adminapi_events_controller_audit_events()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EventsApi->otoroshi_controllers_adminapi_events_controller_audit_events: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditEventList**](AuditEventList.md)

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

