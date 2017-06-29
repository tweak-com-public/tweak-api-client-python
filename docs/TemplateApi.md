# TweakApi.TemplateApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_change_stream_get**](TemplateApi.md#templates_change_stream_get) | **GET** /Templates/change-stream | Create a change stream.
[**templates_change_stream_post**](TemplateApi.md#templates_change_stream_post) | **POST** /Templates/change-stream | Create a change stream.
[**templates_count_get**](TemplateApi.md#templates_count_get) | **GET** /Templates/count | Count instances of the model matched by where from the data source.
[**templates_find_one_get**](TemplateApi.md#templates_find_one_get) | **GET** /Templates/findOne | Find first instance of the model matched by filter from the data source.
[**templates_get**](TemplateApi.md#templates_get) | **GET** /Templates | Find all instances of the model matched by filter from the data source.
[**templates_id_delete**](TemplateApi.md#templates_id_delete) | **DELETE** /Templates/{id} | Delete a model instance by {{id}} from the data source.
[**templates_id_designs_count_get**](TemplateApi.md#templates_id_designs_count_get) | **GET** /Templates/{id}/designs/count | Counts designs of Template.
[**templates_id_designs_delete**](TemplateApi.md#templates_id_designs_delete) | **DELETE** /Templates/{id}/designs | Deletes all designs of this model.
[**templates_id_designs_fk_delete**](TemplateApi.md#templates_id_designs_fk_delete) | **DELETE** /Templates/{id}/designs/{fk} | Delete a related item by id for designs.
[**templates_id_designs_fk_get**](TemplateApi.md#templates_id_designs_fk_get) | **GET** /Templates/{id}/designs/{fk} | Find a related item by id for designs.
[**templates_id_designs_fk_put**](TemplateApi.md#templates_id_designs_fk_put) | **PUT** /Templates/{id}/designs/{fk} | Update a related item by id for designs.
[**templates_id_designs_generate_post**](TemplateApi.md#templates_id_designs_generate_post) | **POST** /Templates/{id}/designs/generate | Generate design from template
[**templates_id_designs_get**](TemplateApi.md#templates_id_designs_get) | **GET** /Templates/{id}/designs | Queries designs of Template.
[**templates_id_designs_post**](TemplateApi.md#templates_id_designs_post) | **POST** /Templates/{id}/designs | Creates a new instance in designs of this model.
[**templates_id_exists_get**](TemplateApi.md#templates_id_exists_get) | **GET** /Templates/{id}/exists | Check whether a model instance exists in the data source.
[**templates_id_get**](TemplateApi.md#templates_id_get) | **GET** /Templates/{id} | Find a model instance by {{id}} from the data source.
[**templates_id_head**](TemplateApi.md#templates_id_head) | **HEAD** /Templates/{id} | Check whether a model instance exists in the data source.
[**templates_id_invitation_tickets_fk_delete**](TemplateApi.md#templates_id_invitation_tickets_fk_delete) | **DELETE** /Templates/{id}/invitationTickets/{fk} | Delete InvitationTickets for this Template
[**templates_id_invitation_tickets_fk_get**](TemplateApi.md#templates_id_invitation_tickets_fk_get) | **GET** /Templates/{id}/invitationTickets/{fk} | Get InvitationTicket by Id for this Template
[**templates_id_invitation_tickets_get**](TemplateApi.md#templates_id_invitation_tickets_get) | **GET** /Templates/{id}/invitationTickets | List InvitationTickets for this Template
[**templates_id_members_count_get**](TemplateApi.md#templates_id_members_count_get) | **GET** /Templates/{id}/members/count | Counts members of Template.
[**templates_id_members_delete**](TemplateApi.md#templates_id_members_delete) | **DELETE** /Templates/{id}/members | Deletes all members of this model.
[**templates_id_members_fk_delete**](TemplateApi.md#templates_id_members_fk_delete) | **DELETE** /Templates/{id}/members/{fk} | Delete a related item by id for members.
[**templates_id_members_fk_get**](TemplateApi.md#templates_id_members_fk_get) | **GET** /Templates/{id}/members/{fk} | Find a related item by id for members.
[**templates_id_members_fk_put**](TemplateApi.md#templates_id_members_fk_put) | **PUT** /Templates/{id}/members/{fk} | Update a related item by id for members.
[**templates_id_members_get**](TemplateApi.md#templates_id_members_get) | **GET** /Templates/{id}/members | Queries members of Template.
[**templates_id_members_post**](TemplateApi.md#templates_id_members_post) | **POST** /Templates/{id}/members | Creates a new instance in members of this model.
[**templates_id_members_rel_fk_delete**](TemplateApi.md#templates_id_members_rel_fk_delete) | **DELETE** /Templates/{id}/members/rel/{fk} | Remove the members relation to an item by id.
[**templates_id_members_rel_fk_head**](TemplateApi.md#templates_id_members_rel_fk_head) | **HEAD** /Templates/{id}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**templates_id_members_rel_fk_put**](TemplateApi.md#templates_id_members_rel_fk_put) | **PUT** /Templates/{id}/members/rel/{fk} | Add a related item by id for members.
[**templates_id_patch**](TemplateApi.md#templates_id_patch) | **PATCH** /Templates/{id} | Patch attributes for a model instance and persist it into the data source.
[**templates_id_permission_delete**](TemplateApi.md#templates_id_permission_delete) | **DELETE** /Templates/{id}/permission | Deletes permission of this model.
[**templates_id_permission_get**](TemplateApi.md#templates_id_permission_get) | **GET** /Templates/{id}/permission | Fetches hasOne relation permission.
[**templates_id_permission_post**](TemplateApi.md#templates_id_permission_post) | **POST** /Templates/{id}/permission | Creates a new instance in permission of this model.
[**templates_id_permission_put**](TemplateApi.md#templates_id_permission_put) | **PUT** /Templates/{id}/permission | Update permission of this model.
[**templates_id_portal_folders_count_get**](TemplateApi.md#templates_id_portal_folders_count_get) | **GET** /Templates/{id}/portalFolders/count | Counts portalFolders of Template.
[**templates_id_portal_folders_delete**](TemplateApi.md#templates_id_portal_folders_delete) | **DELETE** /Templates/{id}/portalFolders | Deletes all portalFolders of this model.
[**templates_id_portal_folders_fk_delete**](TemplateApi.md#templates_id_portal_folders_fk_delete) | **DELETE** /Templates/{id}/portalFolders/{fk} | Delete a related item by id for portalFolders.
[**templates_id_portal_folders_fk_get**](TemplateApi.md#templates_id_portal_folders_fk_get) | **GET** /Templates/{id}/portalFolders/{fk} | Find a related item by id for portalFolders.
[**templates_id_portal_folders_fk_put**](TemplateApi.md#templates_id_portal_folders_fk_put) | **PUT** /Templates/{id}/portalFolders/{fk} | Update a related item by id for portalFolders.
[**templates_id_portal_folders_get**](TemplateApi.md#templates_id_portal_folders_get) | **GET** /Templates/{id}/portalFolders | Queries portalFolders of Template.
[**templates_id_portal_folders_post**](TemplateApi.md#templates_id_portal_folders_post) | **POST** /Templates/{id}/portalFolders | Creates a new instance in portalFolders of this model.
[**templates_id_portal_folders_rel_fk_delete**](TemplateApi.md#templates_id_portal_folders_rel_fk_delete) | **DELETE** /Templates/{id}/portalFolders/rel/{fk} | Remove the portalFolders relation to an item by id.
[**templates_id_portal_folders_rel_fk_head**](TemplateApi.md#templates_id_portal_folders_rel_fk_head) | **HEAD** /Templates/{id}/portalFolders/rel/{fk} | Check the existence of portalFolders relation to an item by id.
[**templates_id_portal_folders_rel_fk_put**](TemplateApi.md#templates_id_portal_folders_rel_fk_put) | **PUT** /Templates/{id}/portalFolders/rel/{fk} | Add a related item by id for portalFolders.
[**templates_id_portals_count_get**](TemplateApi.md#templates_id_portals_count_get) | **GET** /Templates/{id}/portals/count | Counts portals of Template.
[**templates_id_portals_delete**](TemplateApi.md#templates_id_portals_delete) | **DELETE** /Templates/{id}/portals | Deletes all portals of this model.
[**templates_id_portals_fk_delete**](TemplateApi.md#templates_id_portals_fk_delete) | **DELETE** /Templates/{id}/portals/{fk} | Delete a related item by id for portals.
[**templates_id_portals_fk_get**](TemplateApi.md#templates_id_portals_fk_get) | **GET** /Templates/{id}/portals/{fk} | Find a related item by id for portals.
[**templates_id_portals_fk_put**](TemplateApi.md#templates_id_portals_fk_put) | **PUT** /Templates/{id}/portals/{fk} | Update a related item by id for portals.
[**templates_id_portals_get**](TemplateApi.md#templates_id_portals_get) | **GET** /Templates/{id}/portals | Queries portals of Template.
[**templates_id_portals_post**](TemplateApi.md#templates_id_portals_post) | **POST** /Templates/{id}/portals | Creates a new instance in portals of this model.
[**templates_id_portals_rel_fk_delete**](TemplateApi.md#templates_id_portals_rel_fk_delete) | **DELETE** /Templates/{id}/portals/rel/{fk} | Remove the portals relation to an item by id.
[**templates_id_portals_rel_fk_head**](TemplateApi.md#templates_id_portals_rel_fk_head) | **HEAD** /Templates/{id}/portals/rel/{fk} | Check the existence of portals relation to an item by id.
[**templates_id_portals_rel_fk_put**](TemplateApi.md#templates_id_portals_rel_fk_put) | **PUT** /Templates/{id}/portals/rel/{fk} | Add a related item by id for portals.
[**templates_id_put**](TemplateApi.md#templates_id_put) | **PUT** /Templates/{id} | Replace attributes for a model instance and persist it into the data source.
[**templates_id_replace_post**](TemplateApi.md#templates_id_replace_post) | **POST** /Templates/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**templates_id_tags_count_get**](TemplateApi.md#templates_id_tags_count_get) | **GET** /Templates/{id}/tags/count | Counts tags of Template.
[**templates_id_tags_delete**](TemplateApi.md#templates_id_tags_delete) | **DELETE** /Templates/{id}/tags | Deletes all tags of this model.
[**templates_id_tags_fk_delete**](TemplateApi.md#templates_id_tags_fk_delete) | **DELETE** /Templates/{id}/tags/{fk} | Delete a related item by id for tags.
[**templates_id_tags_fk_get**](TemplateApi.md#templates_id_tags_fk_get) | **GET** /Templates/{id}/tags/{fk} | Find a related item by id for tags.
[**templates_id_tags_fk_put**](TemplateApi.md#templates_id_tags_fk_put) | **PUT** /Templates/{id}/tags/{fk} | Update a related item by id for tags.
[**templates_id_tags_get**](TemplateApi.md#templates_id_tags_get) | **GET** /Templates/{id}/tags | Queries tags of Template.
[**templates_id_tags_post**](TemplateApi.md#templates_id_tags_post) | **POST** /Templates/{id}/tags | Creates a new instance in tags of this model.
[**templates_id_tags_rel_fk_delete**](TemplateApi.md#templates_id_tags_rel_fk_delete) | **DELETE** /Templates/{id}/tags/rel/{fk} | Remove the tags relation to an item by id.
[**templates_id_tags_rel_fk_head**](TemplateApi.md#templates_id_tags_rel_fk_head) | **HEAD** /Templates/{id}/tags/rel/{fk} | Check the existence of tags relation to an item by id.
[**templates_id_tags_rel_fk_put**](TemplateApi.md#templates_id_tags_rel_fk_put) | **PUT** /Templates/{id}/tags/rel/{fk} | Add a related item by id for tags.
[**templates_id_team_folder_get**](TemplateApi.md#templates_id_team_folder_get) | **GET** /Templates/{id}/teamFolder | Fetches belongsTo relation teamFolder.
[**templates_id_team_get**](TemplateApi.md#templates_id_team_get) | **GET** /Templates/{id}/team | Fetches belongsTo relation team.
[**templates_id_template_members_count_get**](TemplateApi.md#templates_id_template_members_count_get) | **GET** /Templates/{id}/templateMembers/count | Counts templateMembers of Template.
[**templates_id_template_members_delete**](TemplateApi.md#templates_id_template_members_delete) | **DELETE** /Templates/{id}/templateMembers | Deletes all templateMembers of this model.
[**templates_id_template_members_fk_delete**](TemplateApi.md#templates_id_template_members_fk_delete) | **DELETE** /Templates/{id}/templateMembers/{fk} | Delete a related item by id for templateMembers.
[**templates_id_template_members_fk_get**](TemplateApi.md#templates_id_template_members_fk_get) | **GET** /Templates/{id}/templateMembers/{fk} | Find a related item by id for templateMembers.
[**templates_id_template_members_fk_put**](TemplateApi.md#templates_id_template_members_fk_put) | **PUT** /Templates/{id}/templateMembers/{fk} | Update a related item by id for templateMembers.
[**templates_id_template_members_get**](TemplateApi.md#templates_id_template_members_get) | **GET** /Templates/{id}/templateMembers | Queries templateMembers of Template.
[**templates_id_template_members_post**](TemplateApi.md#templates_id_template_members_post) | **POST** /Templates/{id}/templateMembers | Creates a new instance in templateMembers of this model.
[**templates_id_uploader_get**](TemplateApi.md#templates_id_uploader_get) | **GET** /Templates/{id}/uploader | Fetches belongsTo relation uploader.
[**templates_id_workflow_get**](TemplateApi.md#templates_id_workflow_get) | **GET** /Templates/{id}/workflow | Fetches belongsTo relation workflow.
[**templates_patch**](TemplateApi.md#templates_patch) | **PATCH** /Templates | Patch an existing model instance or insert a new one into the data source.
[**templates_post**](TemplateApi.md#templates_post) | **POST** /Templates | Create a new instance of the model and persist it into the data source.
[**templates_put**](TemplateApi.md#templates_put) | **PUT** /Templates | Replace an existing model instance or insert a new one into the data source.
[**templates_replace_or_create_post**](TemplateApi.md#templates_replace_or_create_post) | **POST** /Templates/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**templates_update_post**](TemplateApi.md#templates_update_post) | **POST** /Templates/update | Update instances of the model matched by {{where}} from the data source.
[**templates_upsert_with_where_post**](TemplateApi.md#templates_upsert_with_where_post) | **POST** /Templates/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **templates_change_stream_get**
> file templates_change_stream_get(options=options)

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
api_instance = TweakApi.TemplateApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.templates_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_change_stream_get: %s\n" % e)
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

# **templates_change_stream_post**
> file templates_change_stream_post(options=options)

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
api_instance = TweakApi.TemplateApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.templates_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_change_stream_post: %s\n" % e)
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

# **templates_count_get**
> InlineResponse200 templates_count_get(where=where)

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
api_instance = TweakApi.TemplateApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.templates_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_find_one_get**
> Template templates_find_one_get(filter=filter)

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
api_instance = TweakApi.TemplateApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.templates_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_get**
> list[Template] templates_get(filter=filter)

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
api_instance = TweakApi.TemplateApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.templates_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_delete**
> object templates_id_delete(id)

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.templates_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_delete: %s\n" % e)
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

# **templates_id_designs_count_get**
> InlineResponse200 templates_id_designs_count_get(id, where=where)

Counts designs of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of Template.
    api_response = api_instance.templates_id_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_designs_delete**
> templates_id_designs_delete(id)

Deletes all designs of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id

try: 
    # Deletes all designs of this model.
    api_instance.templates_id_designs_delete(id)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_designs_fk_delete**
> templates_id_designs_fk_delete(id, fk)

Delete a related item by id for designs.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.templates_id_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_designs_fk_get**
> Design templates_id_designs_fk_get(id, fk)

Find a related item by id for designs.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.templates_id_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_designs_fk_put**
> Design templates_id_designs_fk_put(id, fk, data=data)

Update a related item by id for designs.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.templates_id_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_designs_generate_post**
> Design templates_id_designs_generate_post(id, id2, data=data)

Generate design from template

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
id2 = 'id_example' # str | 
data = TweakApi.Template() # Template |  (optional)

try: 
    # Generate design from template
    api_response = api_instance.templates_id_designs_generate_post(id, id2, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **id2** | **str**|  | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_designs_get**
> list[Design] templates_id_designs_get(id, filter=filter)

Queries designs of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of Template.
    api_response = api_instance.templates_id_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_designs_post**
> Design templates_id_designs_post(id, data=data)

Creates a new instance in designs of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.templates_id_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_exists_get**
> InlineResponse2002 templates_id_exists_get(id)

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.templates_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_exists_get: %s\n" % e)
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

# **templates_id_get**
> Template templates_id_get(id, filter=filter)

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.templates_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_head**
> InlineResponse2002 templates_id_head(id)

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.templates_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_head: %s\n" % e)
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

# **templates_id_invitation_tickets_fk_delete**
> object templates_id_invitation_tickets_fk_delete(id, id2, fk)

Delete InvitationTickets for this Template

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
id2 = 'id_example' # str | Template id
fk = 'fk_example' # str | InvitationTicket id

try: 
    # Delete InvitationTickets for this Template
    api_response = api_instance.templates_id_invitation_tickets_fk_delete(id, id2, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_invitation_tickets_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **id2** | **str**| Template id | 
 **fk** | **str**| InvitationTicket id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_invitation_tickets_fk_get**
> InvitationTicket templates_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)

Get InvitationTicket by Id for this Template

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
id2 = 'id_example' # str | Template id
fk = 'fk_example' # str | InvitationTicket id
filter = 'filter_example' # str | Only include changes that match this filter (optional)

try: 
    # Get InvitationTicket by Id for this Template
    api_response = api_instance.templates_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_invitation_tickets_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **id2** | **str**| Template id | 
 **fk** | **str**| InvitationTicket id | 
 **filter** | **str**| Only include changes that match this filter | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_invitation_tickets_get**
> list[InvitationTicket] templates_id_invitation_tickets_get(id, id2, filter=filter)

List InvitationTickets for this Template

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
id2 = 'id_example' # str | Template id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List InvitationTickets for this Template
    api_response = api_instance.templates_id_invitation_tickets_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_invitation_tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **id2** | **str**| Template id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_count_get**
> InlineResponse200 templates_id_members_count_get(id, where=where)

Counts members of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Template.
    api_response = api_instance.templates_id_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_delete**
> templates_id_members_delete(id)

Deletes all members of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id

try: 
    # Deletes all members of this model.
    api_instance.templates_id_members_delete(id)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_fk_delete**
> templates_id_members_fk_delete(id, fk)

Delete a related item by id for members.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.templates_id_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_fk_get**
> TeamMember templates_id_members_fk_get(id, fk)

Find a related item by id for members.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.templates_id_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_fk_put**
> TeamMember templates_id_members_fk_put(id, fk, data=data)

Update a related item by id for members.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.templates_id_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_get**
> list[TeamMember] templates_id_members_get(id, filter=filter)

Queries members of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Template.
    api_response = api_instance.templates_id_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_post**
> TeamMember templates_id_members_post(id, data=data)

Creates a new instance in members of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.templates_id_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_rel_fk_delete**
> templates_id_members_rel_fk_delete(id, fk)

Remove the members relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.templates_id_members_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_rel_fk_head**
> bool templates_id_members_rel_fk_head(id, fk)

Check the existence of members relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.templates_id_members_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_members_rel_fk_put**
> TemplateMember templates_id_members_rel_fk_put(id, fk, data=data)

Add a related item by id for members.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TemplateMember() # TemplateMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.templates_id_members_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TemplateMember**](TemplateMember.md)|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_patch**
> Template templates_id_patch(id, data=data)

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.Template() # Template | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.templates_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**Template**](Template.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_permission_delete**
> templates_id_permission_delete(id)

Deletes permission of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id

try: 
    # Deletes permission of this model.
    api_instance.templates_id_permission_delete(id)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_permission_get**
> TemplatePermissionSet templates_id_permission_get(id, refresh=refresh)

Fetches hasOne relation permission.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.templates_id_permission_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TemplatePermissionSet**](TemplatePermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_permission_post**
> TemplatePermissionSet templates_id_permission_post(id, data=data)

Creates a new instance in permission of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.TemplatePermissionSet() # TemplatePermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.templates_id_permission_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**TemplatePermissionSet**](TemplatePermissionSet.md)|  | [optional] 

### Return type

[**TemplatePermissionSet**](TemplatePermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_permission_put**
> TemplatePermissionSet templates_id_permission_put(id, data=data)

Update permission of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.TemplatePermissionSet() # TemplatePermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.templates_id_permission_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**TemplatePermissionSet**](TemplatePermissionSet.md)|  | [optional] 

### Return type

[**TemplatePermissionSet**](TemplatePermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_count_get**
> InlineResponse200 templates_id_portal_folders_count_get(id, where=where)

Counts portalFolders of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portalFolders of Template.
    api_response = api_instance.templates_id_portal_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_delete**
> templates_id_portal_folders_delete(id)

Deletes all portalFolders of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id

try: 
    # Deletes all portalFolders of this model.
    api_instance.templates_id_portal_folders_delete(id)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_fk_delete**
> templates_id_portal_folders_fk_delete(id, fk)

Delete a related item by id for portalFolders.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Delete a related item by id for portalFolders.
    api_instance.templates_id_portal_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_fk_get**
> PortalTemplateFolder templates_id_portal_folders_fk_get(id, fk)

Find a related item by id for portalFolders.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Find a related item by id for portalFolders.
    api_response = api_instance.templates_id_portal_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_fk_put**
> PortalTemplateFolder templates_id_portal_folders_fk_put(id, fk, data=data)

Update a related item by id for portalFolders.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portalFolders
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Update a related item by id for portalFolders.
    api_response = api_instance.templates_id_portal_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portalFolders | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_get**
> list[PortalTemplateFolder] templates_id_portal_folders_get(id, filter=filter)

Queries portalFolders of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portalFolders of Template.
    api_response = api_instance.templates_id_portal_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalTemplateFolder]**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_post**
> PortalTemplateFolder templates_id_portal_folders_post(id, data=data)

Creates a new instance in portalFolders of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Creates a new instance in portalFolders of this model.
    api_response = api_instance.templates_id_portal_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_rel_fk_delete**
> templates_id_portal_folders_rel_fk_delete(id, fk)

Remove the portalFolders relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Remove the portalFolders relation to an item by id.
    api_instance.templates_id_portal_folders_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_rel_fk_head**
> bool templates_id_portal_folders_rel_fk_head(id, fk)

Check the existence of portalFolders relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Check the existence of portalFolders relation to an item by id.
    api_response = api_instance.templates_id_portal_folders_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portal_folders_rel_fk_put**
> PortalTemplate templates_id_portal_folders_rel_fk_put(id, fk, data=data)

Add a related item by id for portalFolders.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portalFolders
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Add a related item by id for portalFolders.
    api_response = api_instance.templates_id_portal_folders_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portal_folders_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portalFolders | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_count_get**
> InlineResponse200 templates_id_portals_count_get(id, where=where)

Counts portals of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of Template.
    api_response = api_instance.templates_id_portals_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_delete**
> templates_id_portals_delete(id)

Deletes all portals of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id

try: 
    # Deletes all portals of this model.
    api_instance.templates_id_portals_delete(id)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_fk_delete**
> templates_id_portals_fk_delete(id, fk)

Delete a related item by id for portals.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.templates_id_portals_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_fk_get**
> Portal templates_id_portals_fk_get(id, fk)

Find a related item by id for portals.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.templates_id_portals_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_fk_put**
> Portal templates_id_portals_fk_put(id, fk, data=data)

Update a related item by id for portals.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.templates_id_portals_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_get**
> list[Portal] templates_id_portals_get(id, filter=filter)

Queries portals of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of Template.
    api_response = api_instance.templates_id_portals_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_post**
> Portal templates_id_portals_post(id, data=data)

Creates a new instance in portals of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.templates_id_portals_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_rel_fk_delete**
> templates_id_portals_rel_fk_delete(id, fk)

Remove the portals relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Remove the portals relation to an item by id.
    api_instance.templates_id_portals_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_rel_fk_head**
> bool templates_id_portals_rel_fk_head(id, fk)

Check the existence of portals relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Check the existence of portals relation to an item by id.
    api_response = api_instance.templates_id_portals_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_portals_rel_fk_put**
> PortalTemplate templates_id_portals_rel_fk_put(id, fk, data=data)

Add a related item by id for portals.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Add a related item by id for portals.
    api_response = api_instance.templates_id_portals_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_portals_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_put**
> Template templates_id_put(id, data=data)

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Model id
data = TweakApi.Template() # Template | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.templates_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Template**](Template.md)| Model instance data | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_replace_post**
> Template templates_id_replace_post(id, data=data)

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Model id
data = TweakApi.Template() # Template | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.templates_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Template**](Template.md)| Model instance data | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_count_get**
> InlineResponse200 templates_id_tags_count_get(id, where=where)

Counts tags of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts tags of Template.
    api_response = api_instance.templates_id_tags_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_delete**
> templates_id_tags_delete(id)

Deletes all tags of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id

try: 
    # Deletes all tags of this model.
    api_instance.templates_id_tags_delete(id)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_fk_delete**
> templates_id_tags_fk_delete(id, fk)

Delete a related item by id for tags.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Delete a related item by id for tags.
    api_instance.templates_id_tags_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_fk_get**
> Tag templates_id_tags_fk_get(id, fk)

Find a related item by id for tags.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Find a related item by id for tags.
    api_response = api_instance.templates_id_tags_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_fk_put**
> Tag templates_id_tags_fk_put(id, fk, data=data)

Update a related item by id for tags.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Update a related item by id for tags.
    api_response = api_instance.templates_id_tags_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for tags | 
 **data** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_get**
> list[Tag] templates_id_tags_get(id, filter=filter)

Queries tags of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries tags of Template.
    api_response = api_instance.templates_id_tags_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_post**
> Tag templates_id_tags_post(id, data=data)

Creates a new instance in tags of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Creates a new instance in tags of this model.
    api_response = api_instance.templates_id_tags_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_rel_fk_delete**
> templates_id_tags_rel_fk_delete(id, fk)

Remove the tags relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Remove the tags relation to an item by id.
    api_instance.templates_id_tags_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_rel_fk_head**
> bool templates_id_tags_rel_fk_head(id, fk)

Check the existence of tags relation to an item by id.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Check the existence of tags relation to an item by id.
    api_response = api_instance.templates_id_tags_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_tags_rel_fk_put**
> TemplateTag templates_id_tags_rel_fk_put(id, fk, data=data)

Add a related item by id for tags.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.TemplateTag() # TemplateTag |  (optional)

try: 
    # Add a related item by id for tags.
    api_response = api_instance.templates_id_tags_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_tags_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for tags | 
 **data** | [**TemplateTag**](TemplateTag.md)|  | [optional] 

### Return type

[**TemplateTag**](TemplateTag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_team_folder_get**
> TeamTemplateFolder templates_id_team_folder_get(id, refresh=refresh)

Fetches belongsTo relation teamFolder.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation teamFolder.
    api_response = api_instance.templates_id_team_folder_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_team_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_team_get**
> Team templates_id_team_get(id, refresh=refresh)

Fetches belongsTo relation team.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.templates_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_template_members_count_get**
> InlineResponse200 templates_id_template_members_count_get(id, where=where)

Counts templateMembers of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateMembers of Template.
    api_response = api_instance.templates_id_template_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_template_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_template_members_delete**
> templates_id_template_members_delete(id)

Deletes all templateMembers of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id

try: 
    # Deletes all templateMembers of this model.
    api_instance.templates_id_template_members_delete(id)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_template_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_template_members_fk_delete**
> templates_id_template_members_fk_delete(id, fk)

Delete a related item by id for templateMembers.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for templateMembers

try: 
    # Delete a related item by id for templateMembers.
    api_instance.templates_id_template_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_template_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for templateMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_template_members_fk_get**
> TemplateMember templates_id_template_members_fk_get(id, fk)

Find a related item by id for templateMembers.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for templateMembers

try: 
    # Find a related item by id for templateMembers.
    api_response = api_instance.templates_id_template_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_template_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for templateMembers | 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_template_members_fk_put**
> TemplateMember templates_id_template_members_fk_put(id, fk, data=data)

Update a related item by id for templateMembers.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
fk = 'fk_example' # str | Foreign key for templateMembers
data = TweakApi.TemplateMember() # TemplateMember |  (optional)

try: 
    # Update a related item by id for templateMembers.
    api_response = api_instance.templates_id_template_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_template_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **fk** | **str**| Foreign key for templateMembers | 
 **data** | [**TemplateMember**](TemplateMember.md)|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_template_members_get**
> list[TemplateMember] templates_id_template_members_get(id, filter=filter)

Queries templateMembers of Template.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateMembers of Template.
    api_response = api_instance.templates_id_template_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_template_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TemplateMember]**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_template_members_post**
> TemplateMember templates_id_template_members_post(id, data=data)

Creates a new instance in templateMembers of this model.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
data = TweakApi.TemplateMember() # TemplateMember |  (optional)

try: 
    # Creates a new instance in templateMembers of this model.
    api_response = api_instance.templates_id_template_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_template_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **data** | [**TemplateMember**](TemplateMember.md)|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_uploader_get**
> TeamMember templates_id_uploader_get(id, refresh=refresh)

Fetches belongsTo relation uploader.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation uploader.
    api_response = api_instance.templates_id_uploader_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_uploader_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_id_workflow_get**
> Workflow templates_id_workflow_get(id, refresh=refresh)

Fetches belongsTo relation workflow.

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
api_instance = TweakApi.TemplateApi()
id = 'id_example' # str | Template id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation workflow.
    api_response = api_instance.templates_id_workflow_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_id_workflow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_patch**
> Template templates_patch(data=data)

Patch an existing model instance or insert a new one into the data source.

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
api_instance = TweakApi.TemplateApi()
data = TweakApi.Template() # Template | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.templates_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Template**](Template.md)| Model instance data | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_post**
> Template templates_post(data=data)

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
api_instance = TweakApi.TemplateApi()
data = TweakApi.Template() # Template | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.templates_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Template**](Template.md)| Model instance data | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_put**
> Template templates_put(data=data)

Replace an existing model instance or insert a new one into the data source.

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
api_instance = TweakApi.TemplateApi()
data = TweakApi.Template() # Template | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.templates_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Template**](Template.md)| Model instance data | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_replace_or_create_post**
> Template templates_replace_or_create_post(data=data)

Replace an existing model instance or insert a new one into the data source.

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
api_instance = TweakApi.TemplateApi()
data = TweakApi.Template() # Template | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.templates_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Template**](Template.md)| Model instance data | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_update_post**
> InlineResponse2001 templates_update_post(where=where, data=data)

Update instances of the model matched by {{where}} from the data source.

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
api_instance = TweakApi.TemplateApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Template() # Template | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.templates_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Template**](Template.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_upsert_with_where_post**
> Template templates_upsert_with_where_post(where=where, data=data)

Update an existing model instance or insert a new one into the data source based on the where criteria.

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
api_instance = TweakApi.TemplateApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Template() # Template | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.templates_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->templates_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Template**](Template.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

