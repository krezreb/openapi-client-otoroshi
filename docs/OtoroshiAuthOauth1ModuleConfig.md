# OtoroshiAuthOauth1ModuleConfig

Configuration of OAuth 1.0 module

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_url** | **str** | URL fetch by otoroshi to get user information from identity provider | [optional] 
**metadata** | **{str: (str,)}** | The metadata of the OAuth 1 module | [optional] 
**authorize_url** | **str** | The authorize URL used to initiates the authorization flow that authenticates the user with the Identity Provider | [optional] 
**request_token_url** | **str** | URL fetch to get a request token during the first step of the authorization OAuth 1 flow | [optional] 
**session_cookie_values** | [**OtoroshiAuthSessionCookieValues**](OtoroshiAuthSessionCookieValues.md) |  | [optional] 
**type** | **str** | the type of the module | [optional] 
**http_method** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Method used to get request and access token | [optional] 
**tags** | **[str]** | OAuth module tags | [optional] 
**session_max_age** | **int** | Max age of the session | [optional] 
**consumer_secret** | **str** | Client secret obtained from identity provider configuration | [optional] 
**access_token_url** | **str** | Endpoint requested by otoroshi to get access token during the authorization OAuth1 flow | [optional] 
**name** | **str** | The name of the OAuth 1 module | [optional] 
**rights_override** | [**{str: (OtoroshiModelsUserRights,)}**](OtoroshiModelsUserRights.md) | Overrides user rights of users connected by OAuth1 module | [optional] 
**callback_url** | **str** | The location where the identity provider returns a browser after the user finishes authenticating with their IDP | [optional] 
**location** | [**OtoroshiModelsEntityLocation**](OtoroshiModelsEntityLocation.md) |  | [optional] 
**id** | **str** | Id of the module | [optional] 
**consumer_key** | **str** | Client ID obtained on identity provider | [optional] 
**desc** | **str** | Description of the oauth 1 module | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


