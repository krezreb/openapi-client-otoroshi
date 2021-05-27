# OtoroshiModelsJwtAuthConstraints

Settings to extract apikey from a jwt token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_pair_signed** | **bool** | The jwt token is signed by a keypair from a cert found from its id in apikey meta. &#39;jwt-sign-keypair&#39; | [optional] 
**cookie_name** | **dict** | Cookie name to extract jwt token | [optional] 
**query_name** | **dict** | Query param name to extract jwt token | [optional] 
**header_name** | **dict** | Header name to extract jwt token | [optional] 
**secret_signed** | **bool** | Jwt token signed with the client_secret | [optional] 
**max_jwt_lifespan_secs** | **dict** | Check if token does not have a long lifespan | [optional] 
**enabled** | **bool** | Constraint enabled | [optional] 
**include_request_attributes** | **bool** | Jwt token should include verb and path | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


