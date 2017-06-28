# TweakApi.ImageFolderApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_folders_change_stream_get**](ImageFolderApi.md#image_folders_change_stream_get) | **GET** /ImageFolders/change-stream | Create a change stream.
[**image_folders_change_stream_post**](ImageFolderApi.md#image_folders_change_stream_post) | **POST** /ImageFolders/change-stream | Create a change stream.
[**image_folders_count_get**](ImageFolderApi.md#image_folders_count_get) | **GET** /ImageFolders/count | Count instances of the model matched by where from the data source.
[**image_folders_find_one_get**](ImageFolderApi.md#image_folders_find_one_get) | **GET** /ImageFolders/findOne | Find first instance of the model matched by filter from the data source.
[**image_folders_get**](ImageFolderApi.md#image_folders_get) | **GET** /ImageFolders | Find all instances of the model matched by filter from the data source.
[**image_folders_id_children_count_get**](ImageFolderApi.md#image_folders_id_children_count_get) | **GET** /ImageFolders/{id}/children/count | Counts children of ImageFolder.
[**image_folders_id_children_delete**](ImageFolderApi.md#image_folders_id_children_delete) | **DELETE** /ImageFolders/{id}/children | Deletes all children of this model.
[**image_folders_id_children_fk_delete**](ImageFolderApi.md#image_folders_id_children_fk_delete) | **DELETE** /ImageFolders/{id}/children/{fk} | Delete a related item by id for children.
[**image_folders_id_children_fk_get**](ImageFolderApi.md#image_folders_id_children_fk_get) | **GET** /ImageFolders/{id}/children/{fk} | Find a related item by id for children.
[**image_folders_id_children_fk_put**](ImageFolderApi.md#image_folders_id_children_fk_put) | **PUT** /ImageFolders/{id}/children/{fk} | Update a related item by id for children.
[**image_folders_id_children_get**](ImageFolderApi.md#image_folders_id_children_get) | **GET** /ImageFolders/{id}/children | Queries children of ImageFolder.
[**image_folders_id_children_post**](ImageFolderApi.md#image_folders_id_children_post) | **POST** /ImageFolders/{id}/children | Creates a new instance in children of this model.
[**image_folders_id_delete**](ImageFolderApi.md#image_folders_id_delete) | **DELETE** /ImageFolders/{id} | Delete a model instance by {{id}} from the data source.
[**image_folders_id_exists_get**](ImageFolderApi.md#image_folders_id_exists_get) | **GET** /ImageFolders/{id}/exists | Check whether a model instance exists in the data source.
[**image_folders_id_folder_members_count_get**](ImageFolderApi.md#image_folders_id_folder_members_count_get) | **GET** /ImageFolders/{id}/folderMembers/count | Counts folderMembers of ImageFolder.
[**image_folders_id_folder_members_delete**](ImageFolderApi.md#image_folders_id_folder_members_delete) | **DELETE** /ImageFolders/{id}/folderMembers | Deletes all folderMembers of this model.
[**image_folders_id_folder_members_fk_delete**](ImageFolderApi.md#image_folders_id_folder_members_fk_delete) | **DELETE** /ImageFolders/{id}/folderMembers/{fk} | Delete a related item by id for folderMembers.
[**image_folders_id_folder_members_fk_get**](ImageFolderApi.md#image_folders_id_folder_members_fk_get) | **GET** /ImageFolders/{id}/folderMembers/{fk} | Find a related item by id for folderMembers.
[**image_folders_id_folder_members_fk_put**](ImageFolderApi.md#image_folders_id_folder_members_fk_put) | **PUT** /ImageFolders/{id}/folderMembers/{fk} | Update a related item by id for folderMembers.
[**image_folders_id_folder_members_get**](ImageFolderApi.md#image_folders_id_folder_members_get) | **GET** /ImageFolders/{id}/folderMembers | Queries folderMembers of ImageFolder.
[**image_folders_id_folder_members_post**](ImageFolderApi.md#image_folders_id_folder_members_post) | **POST** /ImageFolders/{id}/folderMembers | Creates a new instance in folderMembers of this model.
[**image_folders_id_get**](ImageFolderApi.md#image_folders_id_get) | **GET** /ImageFolders/{id} | Find a model instance by {{id}} from the data source.
[**image_folders_id_head**](ImageFolderApi.md#image_folders_id_head) | **HEAD** /ImageFolders/{id} | Check whether a model instance exists in the data source.
[**image_folders_id_images_count_get**](ImageFolderApi.md#image_folders_id_images_count_get) | **GET** /ImageFolders/{id}/images/count | Counts images of ImageFolder.
[**image_folders_id_images_delete**](ImageFolderApi.md#image_folders_id_images_delete) | **DELETE** /ImageFolders/{id}/images | Deletes all images of this model.
[**image_folders_id_images_fk_delete**](ImageFolderApi.md#image_folders_id_images_fk_delete) | **DELETE** /ImageFolders/{id}/images/{fk} | Delete a related item by id for images.
[**image_folders_id_images_fk_get**](ImageFolderApi.md#image_folders_id_images_fk_get) | **GET** /ImageFolders/{id}/images/{fk} | Find a related item by id for images.
[**image_folders_id_images_fk_put**](ImageFolderApi.md#image_folders_id_images_fk_put) | **PUT** /ImageFolders/{id}/images/{fk} | Update a related item by id for images.
[**image_folders_id_images_get**](ImageFolderApi.md#image_folders_id_images_get) | **GET** /ImageFolders/{id}/images | Queries images of ImageFolder.
[**image_folders_id_images_post**](ImageFolderApi.md#image_folders_id_images_post) | **POST** /ImageFolders/{id}/images | Creates a new instance in images of this model.
[**image_folders_id_invitation_tickets_fk_delete**](ImageFolderApi.md#image_folders_id_invitation_tickets_fk_delete) | **DELETE** /ImageFolders/{id}/invitationTickets/{fk} | Delete InvitationTickets for this ImageFolder
[**image_folders_id_invitation_tickets_fk_get**](ImageFolderApi.md#image_folders_id_invitation_tickets_fk_get) | **GET** /ImageFolders/{id}/invitationTickets/{fk} | Get InvitationTicket by Id for this ImageFolder
[**image_folders_id_invitation_tickets_get**](ImageFolderApi.md#image_folders_id_invitation_tickets_get) | **GET** /ImageFolders/{id}/invitationTickets | List InvitationTickets for this ImageFolder
[**image_folders_id_members_count_get**](ImageFolderApi.md#image_folders_id_members_count_get) | **GET** /ImageFolders/{id}/members/count | Counts members of ImageFolder.
[**image_folders_id_members_delete**](ImageFolderApi.md#image_folders_id_members_delete) | **DELETE** /ImageFolders/{id}/members | Deletes all members of this model.
[**image_folders_id_members_fk_delete**](ImageFolderApi.md#image_folders_id_members_fk_delete) | **DELETE** /ImageFolders/{id}/members/{fk} | Delete a related item by id for members.
[**image_folders_id_members_fk_get**](ImageFolderApi.md#image_folders_id_members_fk_get) | **GET** /ImageFolders/{id}/members/{fk} | Find a related item by id for members.
[**image_folders_id_members_fk_put**](ImageFolderApi.md#image_folders_id_members_fk_put) | **PUT** /ImageFolders/{id}/members/{fk} | Update a related item by id for members.
[**image_folders_id_members_get**](ImageFolderApi.md#image_folders_id_members_get) | **GET** /ImageFolders/{id}/members | Queries members of ImageFolder.
[**image_folders_id_members_post**](ImageFolderApi.md#image_folders_id_members_post) | **POST** /ImageFolders/{id}/members | Creates a new instance in members of this model.
[**image_folders_id_members_rel_fk_delete**](ImageFolderApi.md#image_folders_id_members_rel_fk_delete) | **DELETE** /ImageFolders/{id}/members/rel/{fk} | Remove the members relation to an item by id.
[**image_folders_id_members_rel_fk_head**](ImageFolderApi.md#image_folders_id_members_rel_fk_head) | **HEAD** /ImageFolders/{id}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**image_folders_id_members_rel_fk_put**](ImageFolderApi.md#image_folders_id_members_rel_fk_put) | **PUT** /ImageFolders/{id}/members/rel/{fk} | Add a related item by id for members.
[**image_folders_id_parent_get**](ImageFolderApi.md#image_folders_id_parent_get) | **GET** /ImageFolders/{id}/parent | Fetches belongsTo relation parent.
[**image_folders_id_patch**](ImageFolderApi.md#image_folders_id_patch) | **PATCH** /ImageFolders/{id} | Patch attributes for a model instance and persist it into the data source.
[**image_folders_id_portals_count_get**](ImageFolderApi.md#image_folders_id_portals_count_get) | **GET** /ImageFolders/{id}/portals/count | Counts portals of ImageFolder.
[**image_folders_id_portals_delete**](ImageFolderApi.md#image_folders_id_portals_delete) | **DELETE** /ImageFolders/{id}/portals | Deletes all portals of this model.
[**image_folders_id_portals_fk_delete**](ImageFolderApi.md#image_folders_id_portals_fk_delete) | **DELETE** /ImageFolders/{id}/portals/{fk} | Delete a related item by id for portals.
[**image_folders_id_portals_fk_get**](ImageFolderApi.md#image_folders_id_portals_fk_get) | **GET** /ImageFolders/{id}/portals/{fk} | Find a related item by id for portals.
[**image_folders_id_portals_fk_put**](ImageFolderApi.md#image_folders_id_portals_fk_put) | **PUT** /ImageFolders/{id}/portals/{fk} | Update a related item by id for portals.
[**image_folders_id_portals_get**](ImageFolderApi.md#image_folders_id_portals_get) | **GET** /ImageFolders/{id}/portals | Queries portals of ImageFolder.
[**image_folders_id_portals_post**](ImageFolderApi.md#image_folders_id_portals_post) | **POST** /ImageFolders/{id}/portals | Creates a new instance in portals of this model.
[**image_folders_id_portals_rel_fk_delete**](ImageFolderApi.md#image_folders_id_portals_rel_fk_delete) | **DELETE** /ImageFolders/{id}/portals/rel/{fk} | Remove the portals relation to an item by id.
[**image_folders_id_portals_rel_fk_head**](ImageFolderApi.md#image_folders_id_portals_rel_fk_head) | **HEAD** /ImageFolders/{id}/portals/rel/{fk} | Check the existence of portals relation to an item by id.
[**image_folders_id_portals_rel_fk_put**](ImageFolderApi.md#image_folders_id_portals_rel_fk_put) | **PUT** /ImageFolders/{id}/portals/rel/{fk} | Add a related item by id for portals.
[**image_folders_id_put**](ImageFolderApi.md#image_folders_id_put) | **PUT** /ImageFolders/{id} | Replace attributes for a model instance and persist it into the data source.
[**image_folders_id_replace_post**](ImageFolderApi.md#image_folders_id_replace_post) | **POST** /ImageFolders/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**image_folders_id_team_get**](ImageFolderApi.md#image_folders_id_team_get) | **GET** /ImageFolders/{id}/team | Fetches belongsTo relation team.
[**image_folders_patch**](ImageFolderApi.md#image_folders_patch) | **PATCH** /ImageFolders | Patch an existing model instance or insert a new one into the data source.
[**image_folders_post**](ImageFolderApi.md#image_folders_post) | **POST** /ImageFolders | Create a new instance of the model and persist it into the data source.
[**image_folders_put**](ImageFolderApi.md#image_folders_put) | **PUT** /ImageFolders | Replace an existing model instance or insert a new one into the data source.
[**image_folders_replace_or_create_post**](ImageFolderApi.md#image_folders_replace_or_create_post) | **POST** /ImageFolders/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**image_folders_update_post**](ImageFolderApi.md#image_folders_update_post) | **POST** /ImageFolders/update | Update instances of the model matched by {{where}} from the data source.
[**image_folders_upsert_with_where_post**](ImageFolderApi.md#image_folders_upsert_with_where_post) | **POST** /ImageFolders/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **image_folders_change_stream_get**
> file image_folders_change_stream_get(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.image_folders_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_change_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_change_stream_post**
> file image_folders_change_stream_post(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.image_folders_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_change_stream_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_count_get**
> InlineResponse200 image_folders_count_get(where=where)

Count instances of the model matched by where from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.image_folders_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_find_one_get**
> ImageFolder image_folders_find_one_get(filter=filter)

Find first instance of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.image_folders_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_get**
> list[ImageFolder] image_folders_get(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.image_folders_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_children_count_get**
> InlineResponse200 image_folders_id_children_count_get(id, where=where)

Counts children of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts children of ImageFolder.
    api_response = api_instance.image_folders_id_children_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_children_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_children_delete**
> image_folders_id_children_delete(id)

Deletes all children of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id

try: 
    # Deletes all children of this model.
    api_instance.image_folders_id_children_delete(id)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_children_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_children_fk_delete**
> image_folders_id_children_fk_delete(id, fk)

Delete a related item by id for children.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Delete a related item by id for children.
    api_instance.image_folders_id_children_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_children_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_children_fk_get**
> ImageFolder image_folders_id_children_fk_get(id, fk)

Find a related item by id for children.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Find a related item by id for children.
    api_response = api_instance.image_folders_id_children_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_children_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_children_fk_put**
> ImageFolder image_folders_id_children_fk_put(id, fk, data=data)

Update a related item by id for children.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for children
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for children.
    api_response = api_instance.image_folders_id_children_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_children_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for children | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_children_get**
> list[ImageFolder] image_folders_id_children_get(id, filter=filter)

Queries children of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries children of ImageFolder.
    api_response = api_instance.image_folders_id_children_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_children_post**
> ImageFolder image_folders_id_children_post(id, data=data)

Creates a new instance in children of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in children of this model.
    api_response = api_instance.image_folders_id_children_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_children_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_delete**
> object image_folders_id_delete(id)

Delete a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.image_folders_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_exists_get**
> InlineResponse2002 image_folders_id_exists_get(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.image_folders_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_exists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_folder_members_count_get**
> InlineResponse200 image_folders_id_folder_members_count_get(id, where=where)

Counts folderMembers of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts folderMembers of ImageFolder.
    api_response = api_instance.image_folders_id_folder_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_folder_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_folder_members_delete**
> image_folders_id_folder_members_delete(id)

Deletes all folderMembers of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id

try: 
    # Deletes all folderMembers of this model.
    api_instance.image_folders_id_folder_members_delete(id)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_folder_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_folder_members_fk_delete**
> image_folders_id_folder_members_fk_delete(id, fk)

Delete a related item by id for folderMembers.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for folderMembers

try: 
    # Delete a related item by id for folderMembers.
    api_instance.image_folders_id_folder_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_folder_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for folderMembers | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_folder_members_fk_get**
> ImageFolderMember image_folders_id_folder_members_fk_get(id, fk)

Find a related item by id for folderMembers.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for folderMembers

try: 
    # Find a related item by id for folderMembers.
    api_response = api_instance.image_folders_id_folder_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_folder_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for folderMembers | 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_folder_members_fk_put**
> ImageFolderMember image_folders_id_folder_members_fk_put(id, fk, data=data)

Update a related item by id for folderMembers.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for folderMembers
data = TweakApi.ImageFolderMember() # ImageFolderMember |  (optional)

try: 
    # Update a related item by id for folderMembers.
    api_response = api_instance.image_folders_id_folder_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_folder_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for folderMembers | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_folder_members_get**
> list[ImageFolderMember] image_folders_id_folder_members_get(id, filter=filter)

Queries folderMembers of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries folderMembers of ImageFolder.
    api_response = api_instance.image_folders_id_folder_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_folder_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolderMember]**](ImageFolderMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_folder_members_post**
> ImageFolderMember image_folders_id_folder_members_post(id, data=data)

Creates a new instance in folderMembers of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
data = TweakApi.ImageFolderMember() # ImageFolderMember |  (optional)

try: 
    # Creates a new instance in folderMembers of this model.
    api_response = api_instance.image_folders_id_folder_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_folder_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_get**
> ImageFolder image_folders_id_get(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.image_folders_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_head**
> InlineResponse2002 image_folders_id_head(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.image_folders_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_images_count_get**
> InlineResponse200 image_folders_id_images_count_get(id, where=where)

Counts images of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts images of ImageFolder.
    api_response = api_instance.image_folders_id_images_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_images_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_images_delete**
> image_folders_id_images_delete(id)

Deletes all images of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id

try: 
    # Deletes all images of this model.
    api_instance.image_folders_id_images_delete(id)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_images_fk_delete**
> image_folders_id_images_fk_delete(id, fk)

Delete a related item by id for images.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for images

try: 
    # Delete a related item by id for images.
    api_instance.image_folders_id_images_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_images_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for images | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_images_fk_get**
> Image image_folders_id_images_fk_get(id, fk)

Find a related item by id for images.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for images

try: 
    # Find a related item by id for images.
    api_response = api_instance.image_folders_id_images_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_images_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for images | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_images_fk_put**
> Image image_folders_id_images_fk_put(id, fk, data=data)

Update a related item by id for images.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for images
data = TweakApi.Image() # Image |  (optional)

try: 
    # Update a related item by id for images.
    api_response = api_instance.image_folders_id_images_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_images_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for images | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_images_get**
> list[Image] image_folders_id_images_get(id, filter=filter)

Queries images of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries images of ImageFolder.
    api_response = api_instance.image_folders_id_images_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_images_post**
> Image image_folders_id_images_post(id, data=data)

Creates a new instance in images of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
data = TweakApi.Image() # Image |  (optional)

try: 
    # Creates a new instance in images of this model.
    api_response = api_instance.image_folders_id_images_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_invitation_tickets_fk_delete**
> object image_folders_id_invitation_tickets_fk_delete(id, id2, fk)

Delete InvitationTickets for this ImageFolder

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
id2 = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | InvitationTicket id

try: 
    # Delete InvitationTickets for this ImageFolder
    api_response = api_instance.image_folders_id_invitation_tickets_fk_delete(id, id2, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_invitation_tickets_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **id2** | **str**| ImageFolder id | 
 **fk** | **str**| InvitationTicket id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_invitation_tickets_fk_get**
> InvitationTicket image_folders_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)

Get InvitationTicket by Id for this ImageFolder

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
id2 = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | InvitationTicket id
filter = 'filter_example' # str | Only include changes that match this filter (optional)

try: 
    # Get InvitationTicket by Id for this ImageFolder
    api_response = api_instance.image_folders_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_invitation_tickets_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **id2** | **str**| ImageFolder id | 
 **fk** | **str**| InvitationTicket id | 
 **filter** | **str**| Only include changes that match this filter | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_invitation_tickets_get**
> list[InvitationTicket] image_folders_id_invitation_tickets_get(id, id2, filter=filter)

List InvitationTickets for this ImageFolder

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
id2 = 'id_example' # str | ImageFolder id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List InvitationTickets for this ImageFolder
    api_response = api_instance.image_folders_id_invitation_tickets_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_invitation_tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **id2** | **str**| ImageFolder id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_count_get**
> InlineResponse200 image_folders_id_members_count_get(id, where=where)

Counts members of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of ImageFolder.
    api_response = api_instance.image_folders_id_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_delete**
> image_folders_id_members_delete(id)

Deletes all members of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id

try: 
    # Deletes all members of this model.
    api_instance.image_folders_id_members_delete(id)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_fk_delete**
> image_folders_id_members_fk_delete(id, fk)

Delete a related item by id for members.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.image_folders_id_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_fk_get**
> TeamMember image_folders_id_members_fk_get(id, fk)

Find a related item by id for members.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.image_folders_id_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_fk_put**
> TeamMember image_folders_id_members_fk_put(id, fk, data=data)

Update a related item by id for members.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.image_folders_id_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_get**
> list[TeamMember] image_folders_id_members_get(id, filter=filter)

Queries members of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of ImageFolder.
    api_response = api_instance.image_folders_id_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_post**
> TeamMember image_folders_id_members_post(id, data=data)

Creates a new instance in members of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.image_folders_id_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_rel_fk_delete**
> image_folders_id_members_rel_fk_delete(id, fk)

Remove the members relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.image_folders_id_members_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_rel_fk_head**
> bool image_folders_id_members_rel_fk_head(id, fk)

Check the existence of members relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.image_folders_id_members_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_members_rel_fk_put**
> ImageFolderMember image_folders_id_members_rel_fk_put(id, fk, data=data)

Add a related item by id for members.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.ImageFolderMember() # ImageFolderMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.image_folders_id_members_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_parent_get**
> ImageFolder image_folders_id_parent_get(id, refresh=refresh)

Fetches belongsTo relation parent.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation parent.
    api_response = api_instance.image_folders_id_parent_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_parent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_patch**
> ImageFolder image_folders_id_patch(id, data=data)

Patch attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
data = TweakApi.ImageFolder() # ImageFolder | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.image_folders_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **data** | [**ImageFolder**](ImageFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_count_get**
> InlineResponse200 image_folders_id_portals_count_get(id, where=where)

Counts portals of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of ImageFolder.
    api_response = api_instance.image_folders_id_portals_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_delete**
> image_folders_id_portals_delete(id)

Deletes all portals of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id

try: 
    # Deletes all portals of this model.
    api_instance.image_folders_id_portals_delete(id)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_fk_delete**
> image_folders_id_portals_fk_delete(id, fk)

Delete a related item by id for portals.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.image_folders_id_portals_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_fk_get**
> Portal image_folders_id_portals_fk_get(id, fk)

Find a related item by id for portals.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.image_folders_id_portals_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_fk_put**
> Portal image_folders_id_portals_fk_put(id, fk, data=data)

Update a related item by id for portals.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.image_folders_id_portals_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_get**
> list[Portal] image_folders_id_portals_get(id, filter=filter)

Queries portals of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of ImageFolder.
    api_response = api_instance.image_folders_id_portals_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_post**
> Portal image_folders_id_portals_post(id, data=data)

Creates a new instance in portals of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.image_folders_id_portals_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_rel_fk_delete**
> image_folders_id_portals_rel_fk_delete(id, fk)

Remove the portals relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Remove the portals relation to an item by id.
    api_instance.image_folders_id_portals_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_rel_fk_head**
> bool image_folders_id_portals_rel_fk_head(id, fk)

Check the existence of portals relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Check the existence of portals relation to an item by id.
    api_response = api_instance.image_folders_id_portals_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_portals_rel_fk_put**
> PortalImageFolder image_folders_id_portals_rel_fk_put(id, fk, data=data)

Add a related item by id for portals.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.PortalImageFolder() # PortalImageFolder |  (optional)

try: 
    # Add a related item by id for portals.
    api_response = api_instance.image_folders_id_portals_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_portals_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)|  | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_put**
> ImageFolder image_folders_id_put(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.ImageFolder() # ImageFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.image_folders_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ImageFolder**](ImageFolder.md)| Model instance data | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_replace_post**
> ImageFolder image_folders_id_replace_post(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.ImageFolder() # ImageFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.image_folders_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ImageFolder**](ImageFolder.md)| Model instance data | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_id_team_get**
> Team image_folders_id_team_get(id, refresh=refresh)

Fetches belongsTo relation team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
id = 'id_example' # str | ImageFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.image_folders_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_patch**
> ImageFolder image_folders_patch(data=data)

Patch an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
data = TweakApi.ImageFolder() # ImageFolder | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.image_folders_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolder**](ImageFolder.md)| Model instance data | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_post**
> ImageFolder image_folders_post(data=data)

Create a new instance of the model and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
data = TweakApi.ImageFolder() # ImageFolder | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.image_folders_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolder**](ImageFolder.md)| Model instance data | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_put**
> ImageFolder image_folders_put(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
data = TweakApi.ImageFolder() # ImageFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.image_folders_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolder**](ImageFolder.md)| Model instance data | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_replace_or_create_post**
> ImageFolder image_folders_replace_or_create_post(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
data = TweakApi.ImageFolder() # ImageFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.image_folders_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolder**](ImageFolder.md)| Model instance data | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_update_post**
> InlineResponse2001 image_folders_update_post(where=where, data=data)

Update instances of the model matched by {{where}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ImageFolder() # ImageFolder | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.image_folders_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ImageFolder**](ImageFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folders_upsert_with_where_post**
> ImageFolder image_folders_upsert_with_where_post(where=where, data=data)

Update an existing model instance or insert a new one into the data source based on the where criteria.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.ImageFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ImageFolder() # ImageFolder | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.image_folders_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderApi->image_folders_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ImageFolder**](ImageFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

