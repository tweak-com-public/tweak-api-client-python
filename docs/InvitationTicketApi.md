# TweakApi.InvitationTicketApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invitation_tickets_change_stream_get**](InvitationTicketApi.md#invitation_tickets_change_stream_get) | **GET** /InvitationTickets/change-stream | Create a change stream.
[**invitation_tickets_change_stream_post**](InvitationTicketApi.md#invitation_tickets_change_stream_post) | **POST** /InvitationTickets/change-stream | Create a change stream.
[**invitation_tickets_count_get**](InvitationTicketApi.md#invitation_tickets_count_get) | **GET** /InvitationTickets/count | Count instances of the model matched by where from the data source.
[**invitation_tickets_find_one_get**](InvitationTicketApi.md#invitation_tickets_find_one_get) | **GET** /InvitationTickets/findOne | Find first instance of the model matched by filter from the data source.
[**invitation_tickets_get**](InvitationTicketApi.md#invitation_tickets_get) | **GET** /InvitationTickets | Find all instances of the model matched by filter from the data source.
[**invitation_tickets_id_delete**](InvitationTicketApi.md#invitation_tickets_id_delete) | **DELETE** /InvitationTickets/{id} | Delete a model instance by {{id}} from the data source.
[**invitation_tickets_id_exists_get**](InvitationTicketApi.md#invitation_tickets_id_exists_get) | **GET** /InvitationTickets/{id}/exists | Check whether a model instance exists in the data source.
[**invitation_tickets_id_get**](InvitationTicketApi.md#invitation_tickets_id_get) | **GET** /InvitationTickets/{id} | Find a model instance by {{id}} from the data source.
[**invitation_tickets_id_head**](InvitationTicketApi.md#invitation_tickets_id_head) | **HEAD** /InvitationTickets/{id} | Check whether a model instance exists in the data source.
[**invitation_tickets_id_invitee_get**](InvitationTicketApi.md#invitation_tickets_id_invitee_get) | **GET** /InvitationTickets/{id}/invitee | Fetches belongsTo relation invitee.
[**invitation_tickets_id_inviter_get**](InvitationTicketApi.md#invitation_tickets_id_inviter_get) | **GET** /InvitationTickets/{id}/inviter | Fetches belongsTo relation inviter.
[**invitation_tickets_id_patch**](InvitationTicketApi.md#invitation_tickets_id_patch) | **PATCH** /InvitationTickets/{id} | Patch attributes for a model instance and persist it into the data source.
[**invitation_tickets_id_put**](InvitationTicketApi.md#invitation_tickets_id_put) | **PUT** /InvitationTickets/{id} | Replace attributes for a model instance and persist it into the data source.
[**invitation_tickets_id_replace_post**](InvitationTicketApi.md#invitation_tickets_id_replace_post) | **POST** /InvitationTickets/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**invitation_tickets_id_target_design_get**](InvitationTicketApi.md#invitation_tickets_id_target_design_get) | **GET** /InvitationTickets/{id}/targetDesign | Fetches belongsTo relation targetDesign.
[**invitation_tickets_id_target_design_member_get**](InvitationTicketApi.md#invitation_tickets_id_target_design_member_get) | **GET** /InvitationTickets/{id}/targetDesignMember | Fetches belongsTo relation targetDesignMember.
[**invitation_tickets_id_target_image_folder_get**](InvitationTicketApi.md#invitation_tickets_id_target_image_folder_get) | **GET** /InvitationTickets/{id}/targetImageFolder | Fetches belongsTo relation targetImageFolder.
[**invitation_tickets_id_target_image_folder_member_get**](InvitationTicketApi.md#invitation_tickets_id_target_image_folder_member_get) | **GET** /InvitationTickets/{id}/targetImageFolderMember | Fetches belongsTo relation targetImageFolderMember.
[**invitation_tickets_id_target_portal_get**](InvitationTicketApi.md#invitation_tickets_id_target_portal_get) | **GET** /InvitationTickets/{id}/targetPortal | Fetches belongsTo relation targetPortal.
[**invitation_tickets_id_target_portal_member_get**](InvitationTicketApi.md#invitation_tickets_id_target_portal_member_get) | **GET** /InvitationTickets/{id}/targetPortalMember | Fetches belongsTo relation targetPortalMember.
[**invitation_tickets_id_target_team_get**](InvitationTicketApi.md#invitation_tickets_id_target_team_get) | **GET** /InvitationTickets/{id}/targetTeam | Fetches belongsTo relation targetTeam.
[**invitation_tickets_id_target_team_member_get**](InvitationTicketApi.md#invitation_tickets_id_target_team_member_get) | **GET** /InvitationTickets/{id}/targetTeamMember | Fetches belongsTo relation targetTeamMember.
[**invitation_tickets_id_target_template_get**](InvitationTicketApi.md#invitation_tickets_id_target_template_get) | **GET** /InvitationTickets/{id}/targetTemplate | Fetches belongsTo relation targetTemplate.
[**invitation_tickets_id_target_template_member_get**](InvitationTicketApi.md#invitation_tickets_id_target_template_member_get) | **GET** /InvitationTickets/{id}/targetTemplateMember | Fetches belongsTo relation targetTemplateMember.
[**invitation_tickets_post**](InvitationTicketApi.md#invitation_tickets_post) | **POST** /InvitationTickets | Create a new instance of the model and persist it into the data source.


# **invitation_tickets_change_stream_get**
> file invitation_tickets_change_stream_get(options=options)

Create a change stream.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.invitation_tickets_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_change_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_change_stream_post**
> file invitation_tickets_change_stream_post(options=options)

Create a change stream.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.invitation_tickets_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_change_stream_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_count_get**
> InlineResponse2001 invitation_tickets_count_get(where=where)

Count instances of the model matched by where from the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.invitation_tickets_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_find_one_get**
> InvitationTicket invitation_tickets_find_one_get(filter=filter)

Find first instance of the model matched by filter from the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.invitation_tickets_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_get**
> list[InvitationTicket] invitation_tickets_get(filter=filter)

Find all instances of the model matched by filter from the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.invitation_tickets_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_delete**
> object invitation_tickets_id_delete(id)

Delete a model instance by {{id}} from the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.invitation_tickets_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_exists_get**
> InlineResponse2002 invitation_tickets_id_exists_get(id)

Check whether a model instance exists in the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.invitation_tickets_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_exists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_get**
> InvitationTicket invitation_tickets_id_get(id, filter=filter)

Find a model instance by {{id}} from the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.invitation_tickets_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_head**
> InlineResponse2002 invitation_tickets_id_head(id)

Check whether a model instance exists in the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.invitation_tickets_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_invitee_get**
> Customer invitation_tickets_id_invitee_get(id, refresh=refresh)

Fetches belongsTo relation invitee.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation invitee.
    api_response = api_instance.invitation_tickets_id_invitee_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_invitee_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_inviter_get**
> TeamMember invitation_tickets_id_inviter_get(id, refresh=refresh)

Fetches belongsTo relation inviter.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation inviter.
    api_response = api_instance.invitation_tickets_id_inviter_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_inviter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_patch**
> InvitationTicket invitation_tickets_id_patch(id, data=data)

Patch attributes for a model instance and persist it into the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
data = TweakApi.InvitationTicket() # InvitationTicket | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.invitation_tickets_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **data** | [**InvitationTicket**](InvitationTicket.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_put**
> InvitationTicket invitation_tickets_id_put(id, data=data)

Replace attributes for a model instance and persist it into the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | Model id
data = TweakApi.InvitationTicket() # InvitationTicket | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.invitation_tickets_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**InvitationTicket**](InvitationTicket.md)| Model instance data | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_replace_post**
> InvitationTicket invitation_tickets_id_replace_post(id, data=data)

Replace attributes for a model instance and persist it into the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | Model id
data = TweakApi.InvitationTicket() # InvitationTicket | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.invitation_tickets_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**InvitationTicket**](InvitationTicket.md)| Model instance data | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_design_get**
> Design invitation_tickets_id_target_design_get(id, refresh=refresh)

Fetches belongsTo relation targetDesign.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetDesign.
    api_response = api_instance.invitation_tickets_id_target_design_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_design_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_design_member_get**
> DesignMember invitation_tickets_id_target_design_member_get(id, refresh=refresh)

Fetches belongsTo relation targetDesignMember.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetDesignMember.
    api_response = api_instance.invitation_tickets_id_target_design_member_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_design_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_image_folder_get**
> ImageFolder invitation_tickets_id_target_image_folder_get(id, refresh=refresh)

Fetches belongsTo relation targetImageFolder.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetImageFolder.
    api_response = api_instance.invitation_tickets_id_target_image_folder_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_image_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_image_folder_member_get**
> ImageFolderMember invitation_tickets_id_target_image_folder_member_get(id, refresh=refresh)

Fetches belongsTo relation targetImageFolderMember.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetImageFolderMember.
    api_response = api_instance.invitation_tickets_id_target_image_folder_member_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_image_folder_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_portal_get**
> Portal invitation_tickets_id_target_portal_get(id, refresh=refresh)

Fetches belongsTo relation targetPortal.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetPortal.
    api_response = api_instance.invitation_tickets_id_target_portal_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_portal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_portal_member_get**
> PortalMember invitation_tickets_id_target_portal_member_get(id, refresh=refresh)

Fetches belongsTo relation targetPortalMember.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetPortalMember.
    api_response = api_instance.invitation_tickets_id_target_portal_member_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_portal_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_team_get**
> Team invitation_tickets_id_target_team_get(id, refresh=refresh)

Fetches belongsTo relation targetTeam.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetTeam.
    api_response = api_instance.invitation_tickets_id_target_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_team_member_get**
> TeamMember invitation_tickets_id_target_team_member_get(id, refresh=refresh)

Fetches belongsTo relation targetTeamMember.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetTeamMember.
    api_response = api_instance.invitation_tickets_id_target_team_member_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_team_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_template_get**
> Template invitation_tickets_id_target_template_get(id, refresh=refresh)

Fetches belongsTo relation targetTemplate.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetTemplate.
    api_response = api_instance.invitation_tickets_id_target_template_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_id_target_template_member_get**
> TemplateMember invitation_tickets_id_target_template_member_get(id, refresh=refresh)

Fetches belongsTo relation targetTemplateMember.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
id = 'id_example' # str | InvitationTicket id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation targetTemplateMember.
    api_response = api_instance.invitation_tickets_id_target_template_member_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_id_target_template_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| InvitationTicket id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitation_tickets_post**
> InvitationTicket invitation_tickets_post(data=data)

Create a new instance of the model and persist it into the data source.

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

# create an instance of the API class
api_instance = TweakApi.InvitationTicketApi()
data = TweakApi.InvitationTicket() # InvitationTicket | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.invitation_tickets_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitationTicketApi->invitation_tickets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InvitationTicket**](InvitationTicket.md)| Model instance data | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

