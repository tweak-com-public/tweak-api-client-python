# TweakApi.PublicVTeamMemberApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_team_members_login_post**](PublicVTeamMemberApi.md#v1_team_members_login_post) | **POST** /v1/TeamMembers/login | Change portal
[**v1_team_members_logout_post**](PublicVTeamMemberApi.md#v1_team_members_logout_post) | **POST** /v1/TeamMembers/logout | Logout a TeamMember
[**v1_team_members_post**](PublicVTeamMemberApi.md#v1_team_members_post) | **POST** /v1/TeamMembers | Create a Member


# **v1_team_members_login_post**
> TeamMemberAccessToken v1_team_members_login_post(id, portal_id)

Change portal

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: teamKey
TweakApi.configuration.api_key['teamKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['teamKey'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PublicVTeamMemberApi()
id = 'id_example' # str | TeamMember id
portal_id = 'portal_id_example' # str | Portal id

try: 
    # Change portal
    api_response = api_instance.v1_team_members_login_post(id, portal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVTeamMemberApi->v1_team_members_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **portal_id** | **str**| Portal id | 

### Return type

[**TeamMemberAccessToken**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_team_members_logout_post**
> v1_team_members_logout_post()

Logout a TeamMember

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: teamKey
TweakApi.configuration.api_key['teamKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['teamKey'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PublicVTeamMemberApi()

try: 
    # Logout a TeamMember
    api_instance.v1_team_members_logout_post()
except ApiException as e:
    print("Exception when calling PublicVTeamMemberApi->v1_team_members_logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_team_members_post**
> object v1_team_members_post(data)

Create a Member

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: teamKey
TweakApi.configuration.api_key['teamKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['teamKey'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PublicVTeamMemberApi()
data = TweakApi.PublicV1TeamMember() # PublicV1TeamMember | Data to create Member

try: 
    # Create a Member
    api_response = api_instance.v1_team_members_post(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVTeamMemberApi->v1_team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PublicV1TeamMember**](PublicV1TeamMember.md)| Data to create Member | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

