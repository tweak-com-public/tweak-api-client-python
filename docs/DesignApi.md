# TweakApi.DesignApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**designs_change_stream_get**](DesignApi.md#designs_change_stream_get) | **GET** /Designs/change-stream | Create a change stream.
[**designs_change_stream_post**](DesignApi.md#designs_change_stream_post) | **POST** /Designs/change-stream | Create a change stream.
[**designs_count_get**](DesignApi.md#designs_count_get) | **GET** /Designs/count | Count instances of the model matched by where from the data source.
[**designs_find_one_get**](DesignApi.md#designs_find_one_get) | **GET** /Designs/findOne | Find first instance of the model matched by filter from the data source.
[**designs_get**](DesignApi.md#designs_get) | **GET** /Designs | Find all instances of the model matched by filter from the data source.
[**designs_id_approve_post**](DesignApi.md#designs_id_approve_post) | **POST** /Designs/{id}/approve | Approve design
[**designs_id_assignee_get**](DesignApi.md#designs_id_assignee_get) | **GET** /Designs/{id}/assignee | Fetches belongsTo relation assignee.
[**designs_id_commenters_count_get**](DesignApi.md#designs_id_commenters_count_get) | **GET** /Designs/{id}/commenters/count | Counts commenters of Design.
[**designs_id_commenters_delete**](DesignApi.md#designs_id_commenters_delete) | **DELETE** /Designs/{id}/commenters | Deletes all commenters of this model.
[**designs_id_commenters_fk_delete**](DesignApi.md#designs_id_commenters_fk_delete) | **DELETE** /Designs/{id}/commenters/{fk} | Delete a related item by id for commenters.
[**designs_id_commenters_fk_get**](DesignApi.md#designs_id_commenters_fk_get) | **GET** /Designs/{id}/commenters/{fk} | Find a related item by id for commenters.
[**designs_id_commenters_fk_put**](DesignApi.md#designs_id_commenters_fk_put) | **PUT** /Designs/{id}/commenters/{fk} | Update a related item by id for commenters.
[**designs_id_commenters_get**](DesignApi.md#designs_id_commenters_get) | **GET** /Designs/{id}/commenters | Queries commenters of Design.
[**designs_id_commenters_post**](DesignApi.md#designs_id_commenters_post) | **POST** /Designs/{id}/commenters | Creates a new instance in commenters of this model.
[**designs_id_commenters_rel_fk_delete**](DesignApi.md#designs_id_commenters_rel_fk_delete) | **DELETE** /Designs/{id}/commenters/rel/{fk} | Remove the commenters relation to an item by id.
[**designs_id_commenters_rel_fk_head**](DesignApi.md#designs_id_commenters_rel_fk_head) | **HEAD** /Designs/{id}/commenters/rel/{fk} | Check the existence of commenters relation to an item by id.
[**designs_id_commenters_rel_fk_put**](DesignApi.md#designs_id_commenters_rel_fk_put) | **PUT** /Designs/{id}/commenters/rel/{fk} | Add a related item by id for commenters.
[**designs_id_comments_count_get**](DesignApi.md#designs_id_comments_count_get) | **GET** /Designs/{id}/comments/count | Counts comments of Design.
[**designs_id_comments_delete**](DesignApi.md#designs_id_comments_delete) | **DELETE** /Designs/{id}/comments | Deletes all comments of this model.
[**designs_id_comments_fk_delete**](DesignApi.md#designs_id_comments_fk_delete) | **DELETE** /Designs/{id}/comments/{fk} | Delete a related item by id for comments.
[**designs_id_comments_fk_get**](DesignApi.md#designs_id_comments_fk_get) | **GET** /Designs/{id}/comments/{fk} | Find a related item by id for comments.
[**designs_id_comments_fk_put**](DesignApi.md#designs_id_comments_fk_put) | **PUT** /Designs/{id}/comments/{fk} | Update a related item by id for comments.
[**designs_id_comments_get**](DesignApi.md#designs_id_comments_get) | **GET** /Designs/{id}/comments | Queries comments of Design.
[**designs_id_comments_nk_commenter_get**](DesignApi.md#designs_id_comments_nk_commenter_get) | **GET** /Designs/{id}/comments/{nk}/commenter | Fetches belongsTo relation commenter.
[**designs_id_comments_nk_design_get**](DesignApi.md#designs_id_comments_nk_design_get) | **GET** /Designs/{id}/comments/{nk}/design | Fetches belongsTo relation design.
[**designs_id_comments_nk_replies_count_get**](DesignApi.md#designs_id_comments_nk_replies_count_get) | **GET** /Designs/{id}/comments/{nk}/replies/count | Counts replies of DesignComment.
[**designs_id_comments_nk_replies_delete**](DesignApi.md#designs_id_comments_nk_replies_delete) | **DELETE** /Designs/{id}/comments/{nk}/replies | Deletes all replies of this model.
[**designs_id_comments_nk_replies_fk_delete**](DesignApi.md#designs_id_comments_nk_replies_fk_delete) | **DELETE** /Designs/{id}/comments/{nk}/replies/{fk} | Delete a related item by id for replies.
[**designs_id_comments_nk_replies_fk_get**](DesignApi.md#designs_id_comments_nk_replies_fk_get) | **GET** /Designs/{id}/comments/{nk}/replies/{fk} | Find a related item by id for replies.
[**designs_id_comments_nk_replies_fk_put**](DesignApi.md#designs_id_comments_nk_replies_fk_put) | **PUT** /Designs/{id}/comments/{nk}/replies/{fk} | Update a related item by id for replies.
[**designs_id_comments_nk_replies_get**](DesignApi.md#designs_id_comments_nk_replies_get) | **GET** /Designs/{id}/comments/{nk}/replies | Queries replies of DesignComment.
[**designs_id_comments_nk_replies_post**](DesignApi.md#designs_id_comments_nk_replies_post) | **POST** /Designs/{id}/comments/{nk}/replies | Creates a new instance in replies of this model.
[**designs_id_comments_nk_reply_of_get**](DesignApi.md#designs_id_comments_nk_reply_of_get) | **GET** /Designs/{id}/comments/{nk}/replyOf | Fetches belongsTo relation replyOf.
[**designs_id_comments_post**](DesignApi.md#designs_id_comments_post) | **POST** /Designs/{id}/comments | Creates a new instance in comments of this model.
[**designs_id_delete**](DesignApi.md#designs_id_delete) | **DELETE** /Designs/{id} | Delete a model instance by {{id}} from the data source.
[**designs_id_design_members_count_get**](DesignApi.md#designs_id_design_members_count_get) | **GET** /Designs/{id}/designMembers/count | Counts designMembers of Design.
[**designs_id_design_members_delete**](DesignApi.md#designs_id_design_members_delete) | **DELETE** /Designs/{id}/designMembers | Deletes all designMembers of this model.
[**designs_id_design_members_fk_delete**](DesignApi.md#designs_id_design_members_fk_delete) | **DELETE** /Designs/{id}/designMembers/{fk} | Delete a related item by id for designMembers.
[**designs_id_design_members_fk_get**](DesignApi.md#designs_id_design_members_fk_get) | **GET** /Designs/{id}/designMembers/{fk} | Find a related item by id for designMembers.
[**designs_id_design_members_fk_put**](DesignApi.md#designs_id_design_members_fk_put) | **PUT** /Designs/{id}/designMembers/{fk} | Update a related item by id for designMembers.
[**designs_id_design_members_get**](DesignApi.md#designs_id_design_members_get) | **GET** /Designs/{id}/designMembers | Queries designMembers of Design.
[**designs_id_design_members_post**](DesignApi.md#designs_id_design_members_post) | **POST** /Designs/{id}/designMembers | Creates a new instance in designMembers of this model.
[**designs_id_dynamic_data_get**](DesignApi.md#designs_id_dynamic_data_get) | **GET** /Designs/{id}/dynamicData | Fetches belongsTo relation dynamicData.
[**designs_id_exists_get**](DesignApi.md#designs_id_exists_get) | **GET** /Designs/{id}/exists | Check whether a model instance exists in the data source.
[**designs_id_exports_count_get**](DesignApi.md#designs_id_exports_count_get) | **GET** /Designs/{id}/exports/count | Counts exports of Design.
[**designs_id_exports_delete**](DesignApi.md#designs_id_exports_delete) | **DELETE** /Designs/{id}/exports | Deletes all exports of this model.
[**designs_id_exports_fk_delete**](DesignApi.md#designs_id_exports_fk_delete) | **DELETE** /Designs/{id}/exports/{fk} | Delete a related item by id for exports.
[**designs_id_exports_fk_get**](DesignApi.md#designs_id_exports_fk_get) | **GET** /Designs/{id}/exports/{fk} | Find a related item by id for exports.
[**designs_id_exports_fk_put**](DesignApi.md#designs_id_exports_fk_put) | **PUT** /Designs/{id}/exports/{fk} | Update a related item by id for exports.
[**designs_id_exports_get**](DesignApi.md#designs_id_exports_get) | **GET** /Designs/{id}/exports | Queries exports of Design.
[**designs_id_exports_post**](DesignApi.md#designs_id_exports_post) | **POST** /Designs/{id}/exports | Creates a new instance in exports of this model.
[**designs_id_folder_get**](DesignApi.md#designs_id_folder_get) | **GET** /Designs/{id}/folder | Fetches belongsTo relation folder.
[**designs_id_get**](DesignApi.md#designs_id_get) | **GET** /Designs/{id} | Find a model instance by {{id}} from the data source.
[**designs_id_head**](DesignApi.md#designs_id_head) | **HEAD** /Designs/{id} | Check whether a model instance exists in the data source.
[**designs_id_members_count_get**](DesignApi.md#designs_id_members_count_get) | **GET** /Designs/{id}/members/count | Counts members of Design.
[**designs_id_members_delete**](DesignApi.md#designs_id_members_delete) | **DELETE** /Designs/{id}/members | Deletes all members of this model.
[**designs_id_members_fk_delete**](DesignApi.md#designs_id_members_fk_delete) | **DELETE** /Designs/{id}/members/{fk} | Delete a related item by id for members.
[**designs_id_members_fk_get**](DesignApi.md#designs_id_members_fk_get) | **GET** /Designs/{id}/members/{fk} | Find a related item by id for members.
[**designs_id_members_fk_put**](DesignApi.md#designs_id_members_fk_put) | **PUT** /Designs/{id}/members/{fk} | Update a related item by id for members.
[**designs_id_members_get**](DesignApi.md#designs_id_members_get) | **GET** /Designs/{id}/members | Queries members of Design.
[**designs_id_members_post**](DesignApi.md#designs_id_members_post) | **POST** /Designs/{id}/members | Creates a new instance in members of this model.
[**designs_id_members_rel_fk_delete**](DesignApi.md#designs_id_members_rel_fk_delete) | **DELETE** /Designs/{id}/members/rel/{fk} | Remove the members relation to an item by id.
[**designs_id_members_rel_fk_head**](DesignApi.md#designs_id_members_rel_fk_head) | **HEAD** /Designs/{id}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**designs_id_members_rel_fk_put**](DesignApi.md#designs_id_members_rel_fk_put) | **PUT** /Designs/{id}/members/rel/{fk} | Add a related item by id for members.
[**designs_id_patch**](DesignApi.md#designs_id_patch) | **PATCH** /Designs/{id} | Patch attributes for a model instance and persist it into the data source.
[**designs_id_permission_delete**](DesignApi.md#designs_id_permission_delete) | **DELETE** /Designs/{id}/permission | Deletes permission of this model.
[**designs_id_permission_get**](DesignApi.md#designs_id_permission_get) | **GET** /Designs/{id}/permission | Fetches hasOne relation permission.
[**designs_id_permission_post**](DesignApi.md#designs_id_permission_post) | **POST** /Designs/{id}/permission | Creates a new instance in permission of this model.
[**designs_id_permission_put**](DesignApi.md#designs_id_permission_put) | **PUT** /Designs/{id}/permission | Update permission of this model.
[**designs_id_portal_get**](DesignApi.md#designs_id_portal_get) | **GET** /Designs/{id}/portal | Fetches belongsTo relation portal.
[**designs_id_put**](DesignApi.md#designs_id_put) | **PUT** /Designs/{id} | Replace attributes for a model instance and persist it into the data source.
[**designs_id_reject_post**](DesignApi.md#designs_id_reject_post) | **POST** /Designs/{id}/reject | Reject design
[**designs_id_rejection_comment_get**](DesignApi.md#designs_id_rejection_comment_get) | **GET** /Designs/{id}/rejectionComment | Fetches belongsTo relation rejectionComment.
[**designs_id_replace_post**](DesignApi.md#designs_id_replace_post) | **POST** /Designs/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**designs_id_requester_get**](DesignApi.md#designs_id_requester_get) | **GET** /Designs/{id}/requester | Fetches belongsTo relation requester.
[**designs_id_reviewer_get**](DesignApi.md#designs_id_reviewer_get) | **GET** /Designs/{id}/reviewer | Fetches belongsTo relation reviewer.
[**designs_id_submit_post**](DesignApi.md#designs_id_submit_post) | **POST** /Designs/{id}/submit | Submit design for approval
[**designs_id_tags_count_get**](DesignApi.md#designs_id_tags_count_get) | **GET** /Designs/{id}/tags/count | Counts tags of Design.
[**designs_id_tags_delete**](DesignApi.md#designs_id_tags_delete) | **DELETE** /Designs/{id}/tags | Deletes all tags of this model.
[**designs_id_tags_fk_delete**](DesignApi.md#designs_id_tags_fk_delete) | **DELETE** /Designs/{id}/tags/{fk} | Delete a related item by id for tags.
[**designs_id_tags_fk_get**](DesignApi.md#designs_id_tags_fk_get) | **GET** /Designs/{id}/tags/{fk} | Find a related item by id for tags.
[**designs_id_tags_fk_put**](DesignApi.md#designs_id_tags_fk_put) | **PUT** /Designs/{id}/tags/{fk} | Update a related item by id for tags.
[**designs_id_tags_get**](DesignApi.md#designs_id_tags_get) | **GET** /Designs/{id}/tags | Queries tags of Design.
[**designs_id_tags_post**](DesignApi.md#designs_id_tags_post) | **POST** /Designs/{id}/tags | Creates a new instance in tags of this model.
[**designs_id_tags_rel_fk_delete**](DesignApi.md#designs_id_tags_rel_fk_delete) | **DELETE** /Designs/{id}/tags/rel/{fk} | Remove the tags relation to an item by id.
[**designs_id_tags_rel_fk_head**](DesignApi.md#designs_id_tags_rel_fk_head) | **HEAD** /Designs/{id}/tags/rel/{fk} | Check the existence of tags relation to an item by id.
[**designs_id_tags_rel_fk_put**](DesignApi.md#designs_id_tags_rel_fk_put) | **PUT** /Designs/{id}/tags/rel/{fk} | Add a related item by id for tags.
[**designs_id_team_get**](DesignApi.md#designs_id_team_get) | **GET** /Designs/{id}/team | Fetches belongsTo relation team.
[**designs_id_template_get**](DesignApi.md#designs_id_template_get) | **GET** /Designs/{id}/template | Fetches belongsTo relation template.
[**designs_patch**](DesignApi.md#designs_patch) | **PATCH** /Designs | Patch an existing model instance or insert a new one into the data source.
[**designs_post**](DesignApi.md#designs_post) | **POST** /Designs | Create a new instance of the model and persist it into the data source.
[**designs_put**](DesignApi.md#designs_put) | **PUT** /Designs | Replace an existing model instance or insert a new one into the data source.
[**designs_replace_or_create_post**](DesignApi.md#designs_replace_or_create_post) | **POST** /Designs/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**designs_update_post**](DesignApi.md#designs_update_post) | **POST** /Designs/update | Update instances of the model matched by {{where}} from the data source.
[**designs_upsert_with_where_post**](DesignApi.md#designs_upsert_with_where_post) | **POST** /Designs/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **designs_change_stream_get**
> file designs_change_stream_get(options=options)

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
api_instance = TweakApi.DesignApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.designs_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_change_stream_get: %s\n" % e)
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

# **designs_change_stream_post**
> file designs_change_stream_post(options=options)

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
api_instance = TweakApi.DesignApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.designs_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_change_stream_post: %s\n" % e)
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

# **designs_count_get**
> InlineResponse2001 designs_count_get(where=where)

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
api_instance = TweakApi.DesignApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.designs_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_count_get: %s\n" % e)
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

# **designs_find_one_get**
> Design designs_find_one_get(filter=filter)

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
api_instance = TweakApi.DesignApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.designs_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_get**
> list[Design] designs_get(filter=filter)

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
api_instance = TweakApi.DesignApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.designs_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_approve_post**
> Design designs_id_approve_post(id, id2)

Approve design

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
id2 = 'id_example' # str | Customer id

try: 
    # Approve design
    api_response = api_instance.designs_id_approve_post(id, id2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_approve_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **id2** | **str**| Customer id | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_assignee_get**
> TeamMember designs_id_assignee_get(id, refresh=refresh)

Fetches belongsTo relation assignee.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation assignee.
    api_response = api_instance.designs_id_assignee_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_assignee_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_count_get**
> InlineResponse2001 designs_id_commenters_count_get(id, where=where)

Counts commenters of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts commenters of Design.
    api_response = api_instance.designs_id_commenters_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_delete**
> designs_id_commenters_delete(id)

Deletes all commenters of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id

try: 
    # Deletes all commenters of this model.
    api_instance.designs_id_commenters_delete(id)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_fk_delete**
> designs_id_commenters_fk_delete(id, fk)

Delete a related item by id for commenters.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Delete a related item by id for commenters.
    api_instance.designs_id_commenters_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_fk_get**
> TeamMember designs_id_commenters_fk_get(id, fk)

Find a related item by id for commenters.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Find a related item by id for commenters.
    api_response = api_instance.designs_id_commenters_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_fk_put**
> TeamMember designs_id_commenters_fk_put(id, fk, data=data)

Update a related item by id for commenters.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for commenters
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for commenters.
    api_response = api_instance.designs_id_commenters_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for commenters | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_get**
> list[TeamMember] designs_id_commenters_get(id, filter=filter)

Queries commenters of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries commenters of Design.
    api_response = api_instance.designs_id_commenters_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_post**
> TeamMember designs_id_commenters_post(id, data=data)

Creates a new instance in commenters of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in commenters of this model.
    api_response = api_instance.designs_id_commenters_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_rel_fk_delete**
> designs_id_commenters_rel_fk_delete(id, fk)

Remove the commenters relation to an item by id.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Remove the commenters relation to an item by id.
    api_instance.designs_id_commenters_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_rel_fk_head**
> bool designs_id_commenters_rel_fk_head(id, fk)

Check the existence of commenters relation to an item by id.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Check the existence of commenters relation to an item by id.
    api_response = api_instance.designs_id_commenters_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_commenters_rel_fk_put**
> DesignComment designs_id_commenters_rel_fk_put(id, fk, data=data)

Add a related item by id for commenters.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for commenters
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Add a related item by id for commenters.
    api_response = api_instance.designs_id_commenters_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_commenters_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for commenters | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_count_get**
> InlineResponse2001 designs_id_comments_count_get(id, where=where)

Counts comments of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts comments of Design.
    api_response = api_instance.designs_id_comments_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_delete**
> designs_id_comments_delete(id)

Deletes all comments of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id

try: 
    # Deletes all comments of this model.
    api_instance.designs_id_comments_delete(id)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_fk_delete**
> designs_id_comments_fk_delete(id, fk)

Delete a related item by id for comments.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for comments

try: 
    # Delete a related item by id for comments.
    api_instance.designs_id_comments_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for comments | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_fk_get**
> DesignComment designs_id_comments_fk_get(id, fk)

Find a related item by id for comments.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for comments

try: 
    # Find a related item by id for comments.
    api_response = api_instance.designs_id_comments_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for comments | 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_fk_put**
> DesignComment designs_id_comments_fk_put(id, fk, data=data)

Update a related item by id for comments.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for comments
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Update a related item by id for comments.
    api_response = api_instance.designs_id_comments_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for comments | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_get**
> list[DesignComment] designs_id_comments_get(id, filter=filter)

Queries comments of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries comments of Design.
    api_response = api_instance.designs_id_comments_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignComment]**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_commenter_get**
> TeamMember designs_id_comments_nk_commenter_get(id, nk, refresh=refresh)

Fetches belongsTo relation commenter.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation commenter.
    api_response = api_instance.designs_id_comments_nk_commenter_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_commenter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_design_get**
> Design designs_id_comments_nk_design_get(id, nk, refresh=refresh)

Fetches belongsTo relation design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation design.
    api_response = api_instance.designs_id_comments_nk_design_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_design_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_replies_count_get**
> InlineResponse2001 designs_id_comments_nk_replies_count_get(id, nk, where=where)

Counts replies of DesignComment.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts replies of DesignComment.
    api_response = api_instance.designs_id_comments_nk_replies_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_replies_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_replies_delete**
> designs_id_comments_nk_replies_delete(id, nk)

Deletes all replies of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.

try: 
    # Deletes all replies of this model.
    api_instance.designs_id_comments_nk_replies_delete(id, nk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_replies_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_replies_fk_delete**
> designs_id_comments_nk_replies_fk_delete(id, nk, fk)

Delete a related item by id for replies.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
fk = 'fk_example' # str | Foreign key for replies

try: 
    # Delete a related item by id for replies.
    api_instance.designs_id_comments_nk_replies_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_replies_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **fk** | **str**| Foreign key for replies | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_replies_fk_get**
> DesignComment designs_id_comments_nk_replies_fk_get(id, nk, fk)

Find a related item by id for replies.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
fk = 'fk_example' # str | Foreign key for replies

try: 
    # Find a related item by id for replies.
    api_response = api_instance.designs_id_comments_nk_replies_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_replies_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **fk** | **str**| Foreign key for replies | 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_replies_fk_put**
> DesignComment designs_id_comments_nk_replies_fk_put(id, nk, fk, data=data)

Update a related item by id for replies.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
fk = 'fk_example' # str | Foreign key for replies
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Update a related item by id for replies.
    api_response = api_instance.designs_id_comments_nk_replies_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_replies_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **fk** | **str**| Foreign key for replies | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_replies_get**
> list[DesignComment] designs_id_comments_nk_replies_get(id, nk, filter=filter)

Queries replies of DesignComment.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries replies of DesignComment.
    api_response = api_instance.designs_id_comments_nk_replies_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_replies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignComment]**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_replies_post**
> DesignComment designs_id_comments_nk_replies_post(id, nk, data=data)

Creates a new instance in replies of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Creates a new instance in replies of this model.
    api_response = api_instance.designs_id_comments_nk_replies_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_replies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_nk_reply_of_get**
> DesignComment designs_id_comments_nk_reply_of_get(id, nk, refresh=refresh)

Fetches belongsTo relation replyOf.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
nk = 'nk_example' # str | Foreign key for comments.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation replyOf.
    api_response = api_instance.designs_id_comments_nk_reply_of_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_nk_reply_of_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **nk** | **str**| Foreign key for comments. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_comments_post**
> DesignComment designs_id_comments_post(id, data=data)

Creates a new instance in comments of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Creates a new instance in comments of this model.
    api_response = api_instance.designs_id_comments_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_delete**
> object designs_id_delete(id)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.designs_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_delete: %s\n" % e)
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

# **designs_id_design_members_count_get**
> InlineResponse2001 designs_id_design_members_count_get(id, where=where)

Counts designMembers of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designMembers of Design.
    api_response = api_instance.designs_id_design_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_design_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_design_members_delete**
> designs_id_design_members_delete(id)

Deletes all designMembers of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id

try: 
    # Deletes all designMembers of this model.
    api_instance.designs_id_design_members_delete(id)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_design_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_design_members_fk_delete**
> designs_id_design_members_fk_delete(id, fk)

Delete a related item by id for designMembers.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for designMembers

try: 
    # Delete a related item by id for designMembers.
    api_instance.designs_id_design_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_design_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for designMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_design_members_fk_get**
> DesignMember designs_id_design_members_fk_get(id, fk)

Find a related item by id for designMembers.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for designMembers

try: 
    # Find a related item by id for designMembers.
    api_response = api_instance.designs_id_design_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_design_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for designMembers | 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_design_members_fk_put**
> DesignMember designs_id_design_members_fk_put(id, fk, data=data)

Update a related item by id for designMembers.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for designMembers
data = TweakApi.DesignMember() # DesignMember |  (optional)

try: 
    # Update a related item by id for designMembers.
    api_response = api_instance.designs_id_design_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_design_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for designMembers | 
 **data** | [**DesignMember**](DesignMember.md)|  | [optional] 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_design_members_get**
> list[DesignMember] designs_id_design_members_get(id, filter=filter)

Queries designMembers of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designMembers of Design.
    api_response = api_instance.designs_id_design_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_design_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignMember]**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_design_members_post**
> DesignMember designs_id_design_members_post(id, data=data)

Creates a new instance in designMembers of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.DesignMember() # DesignMember |  (optional)

try: 
    # Creates a new instance in designMembers of this model.
    api_response = api_instance.designs_id_design_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_design_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**DesignMember**](DesignMember.md)|  | [optional] 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_dynamic_data_get**
> DynamicData designs_id_dynamic_data_get(id, refresh=refresh)

Fetches belongsTo relation dynamicData.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dynamicData.
    api_response = api_instance.designs_id_dynamic_data_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_dynamic_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_exists_get**
> InlineResponse2002 designs_id_exists_get(id)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.designs_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exists_get: %s\n" % e)
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

# **designs_id_exports_count_get**
> InlineResponse2001 designs_id_exports_count_get(id, where=where)

Counts exports of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts exports of Design.
    api_response = api_instance.designs_id_exports_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exports_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_exports_delete**
> designs_id_exports_delete(id)

Deletes all exports of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id

try: 
    # Deletes all exports of this model.
    api_instance.designs_id_exports_delete(id)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_exports_fk_delete**
> designs_id_exports_fk_delete(id, fk)

Delete a related item by id for exports.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for exports

try: 
    # Delete a related item by id for exports.
    api_instance.designs_id_exports_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exports_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for exports | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_exports_fk_get**
> DesignExport designs_id_exports_fk_get(id, fk)

Find a related item by id for exports.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for exports

try: 
    # Find a related item by id for exports.
    api_response = api_instance.designs_id_exports_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exports_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for exports | 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_exports_fk_put**
> DesignExport designs_id_exports_fk_put(id, fk, data=data)

Update a related item by id for exports.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for exports
data = TweakApi.DesignExport() # DesignExport |  (optional)

try: 
    # Update a related item by id for exports.
    api_response = api_instance.designs_id_exports_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exports_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for exports | 
 **data** | [**DesignExport**](DesignExport.md)|  | [optional] 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_exports_get**
> list[DesignExport] designs_id_exports_get(id, filter=filter)

Queries exports of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries exports of Design.
    api_response = api_instance.designs_id_exports_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignExport]**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_exports_post**
> DesignExport designs_id_exports_post(id, data=data)

Creates a new instance in exports of this model.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.DesignExport() # DesignExport |  (optional)

try: 
    # Creates a new instance in exports of this model.
    api_response = api_instance.designs_id_exports_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_exports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**DesignExport**](DesignExport.md)|  | [optional] 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_folder_get**
> DesignFolder designs_id_folder_get(id, refresh=refresh)

Fetches belongsTo relation folder.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation folder.
    api_response = api_instance.designs_id_folder_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_get**
> Design designs_id_get(id, filter=filter)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.designs_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_head**
> InlineResponse2002 designs_id_head(id)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.designs_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_head: %s\n" % e)
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

# **designs_id_members_count_get**
> InlineResponse2001 designs_id_members_count_get(id, where=where)

Counts members of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Design.
    api_response = api_instance.designs_id_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_delete**
> designs_id_members_delete(id)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id

try: 
    # Deletes all members of this model.
    api_instance.designs_id_members_delete(id)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_fk_delete**
> designs_id_members_fk_delete(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.designs_id_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_fk_get**
> TeamMember designs_id_members_fk_get(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.designs_id_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_fk_put**
> TeamMember designs_id_members_fk_put(id, fk, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.designs_id_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
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

# **designs_id_members_get**
> list[TeamMember] designs_id_members_get(id, filter=filter)

Queries members of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Design.
    api_response = api_instance.designs_id_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_post**
> TeamMember designs_id_members_post(id, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.designs_id_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_rel_fk_delete**
> designs_id_members_rel_fk_delete(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.designs_id_members_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_rel_fk_head**
> bool designs_id_members_rel_fk_head(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.designs_id_members_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_members_rel_fk_put**
> DesignMember designs_id_members_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.DesignMember() # DesignMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.designs_id_members_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**DesignMember**](DesignMember.md)|  | [optional] 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_patch**
> Design designs_id_patch(id, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.Design() # Design | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.designs_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**Design**](Design.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_permission_delete**
> designs_id_permission_delete(id)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id

try: 
    # Deletes permission of this model.
    api_instance.designs_id_permission_delete(id)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_permission_get**
> DesignPermissionSet designs_id_permission_get(id, refresh=refresh)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.designs_id_permission_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_permission_post**
> DesignPermissionSet designs_id_permission_post(id, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.DesignPermissionSet() # DesignPermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.designs_id_permission_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)|  | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_permission_put**
> DesignPermissionSet designs_id_permission_put(id, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.DesignPermissionSet() # DesignPermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.designs_id_permission_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)|  | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_portal_get**
> Portal designs_id_portal_get(id, refresh=refresh)

Fetches belongsTo relation portal.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation portal.
    api_response = api_instance.designs_id_portal_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_portal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_put**
> Design designs_id_put(id, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Model id
data = TweakApi.Design() # Design | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.designs_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Design**](Design.md)| Model instance data | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_reject_post**
> Design designs_id_reject_post(id, id2, data=data)

Reject design

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
id2 = 'id_example' # str | Customer id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Reject design
    api_response = api_instance.designs_id_reject_post(id, id2, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_reject_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **id2** | **str**| Customer id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_rejection_comment_get**
> DesignComment designs_id_rejection_comment_get(id, refresh=refresh)

Fetches belongsTo relation rejectionComment.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation rejectionComment.
    api_response = api_instance.designs_id_rejection_comment_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_rejection_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_replace_post**
> Design designs_id_replace_post(id, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Model id
data = TweakApi.Design() # Design | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.designs_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Design**](Design.md)| Model instance data | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_requester_get**
> TeamMember designs_id_requester_get(id, refresh=refresh)

Fetches belongsTo relation requester.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation requester.
    api_response = api_instance.designs_id_requester_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_requester_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_reviewer_get**
> TeamMember designs_id_reviewer_get(id, refresh=refresh)

Fetches belongsTo relation reviewer.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation reviewer.
    api_response = api_instance.designs_id_reviewer_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_reviewer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_submit_post**
> Design designs_id_submit_post(id, id2)

Submit design for approval

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
id2 = 'id_example' # str | Customer id

try: 
    # Submit design for approval
    api_response = api_instance.designs_id_submit_post(id, id2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_submit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **id2** | **str**| Customer id | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_count_get**
> InlineResponse2001 designs_id_tags_count_get(id, where=where)

Counts tags of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts tags of Design.
    api_response = api_instance.designs_id_tags_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_delete**
> designs_id_tags_delete(id)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id

try: 
    # Deletes all tags of this model.
    api_instance.designs_id_tags_delete(id)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_fk_delete**
> designs_id_tags_fk_delete(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Delete a related item by id for tags.
    api_instance.designs_id_tags_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_fk_get**
> Tag designs_id_tags_fk_get(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Find a related item by id for tags.
    api_response = api_instance.designs_id_tags_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_fk_put**
> Tag designs_id_tags_fk_put(id, fk, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Update a related item by id for tags.
    api_response = api_instance.designs_id_tags_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
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

# **designs_id_tags_get**
> list[Tag] designs_id_tags_get(id, filter=filter)

Queries tags of Design.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries tags of Design.
    api_response = api_instance.designs_id_tags_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_post**
> Tag designs_id_tags_post(id, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Creates a new instance in tags of this model.
    api_response = api_instance.designs_id_tags_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **data** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_rel_fk_delete**
> designs_id_tags_rel_fk_delete(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Remove the tags relation to an item by id.
    api_instance.designs_id_tags_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_rel_fk_head**
> bool designs_id_tags_rel_fk_head(id, fk)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Check the existence of tags relation to an item by id.
    api_response = api_instance.designs_id_tags_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for tags | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_tags_rel_fk_put**
> DesignTag designs_id_tags_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.DesignTag() # DesignTag |  (optional)

try: 
    # Add a related item by id for tags.
    api_response = api_instance.designs_id_tags_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_tags_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **fk** | **str**| Foreign key for tags | 
 **data** | [**DesignTag**](DesignTag.md)|  | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_team_get**
> Team designs_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.designs_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_id_template_get**
> Template designs_id_template_get(id, refresh=refresh)

Fetches belongsTo relation template.

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
api_instance = TweakApi.DesignApi()
id = 'id_example' # str | Design id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation template.
    api_response = api_instance.designs_id_template_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_id_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_patch**
> Design designs_patch(data=data)

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
api_instance = TweakApi.DesignApi()
data = TweakApi.Design() # Design | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.designs_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Design**](Design.md)| Model instance data | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_post**
> Design designs_post(data=data)

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
api_instance = TweakApi.DesignApi()
data = TweakApi.Design() # Design | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.designs_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Design**](Design.md)| Model instance data | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_put**
> Design designs_put(data=data)

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
api_instance = TweakApi.DesignApi()
data = TweakApi.Design() # Design | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.designs_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Design**](Design.md)| Model instance data | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_replace_or_create_post**
> Design designs_replace_or_create_post(data=data)

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
api_instance = TweakApi.DesignApi()
data = TweakApi.Design() # Design | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.designs_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Design**](Design.md)| Model instance data | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_update_post**
> InlineResponse2003 designs_update_post(where=where, data=data)

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
api_instance = TweakApi.DesignApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Design() # Design | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.designs_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Design**](Design.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **designs_upsert_with_where_post**
> Design designs_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.DesignApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Design() # Design | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.designs_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignApi->designs_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Design**](Design.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

