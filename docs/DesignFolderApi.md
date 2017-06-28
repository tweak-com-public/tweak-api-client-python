# TweakApi.DesignFolderApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**design_folders_change_stream_get**](DesignFolderApi.md#design_folders_change_stream_get) | **GET** /DesignFolders/change-stream | Create a change stream.
[**design_folders_change_stream_post**](DesignFolderApi.md#design_folders_change_stream_post) | **POST** /DesignFolders/change-stream | Create a change stream.
[**design_folders_count_get**](DesignFolderApi.md#design_folders_count_get) | **GET** /DesignFolders/count | Count instances of the model matched by where from the data source.
[**design_folders_find_one_get**](DesignFolderApi.md#design_folders_find_one_get) | **GET** /DesignFolders/findOne | Find first instance of the model matched by filter from the data source.
[**design_folders_get**](DesignFolderApi.md#design_folders_get) | **GET** /DesignFolders | Find all instances of the model matched by filter from the data source.
[**design_folders_id_children_count_get**](DesignFolderApi.md#design_folders_id_children_count_get) | **GET** /DesignFolders/{id}/children/count | Counts children of DesignFolder.
[**design_folders_id_children_delete**](DesignFolderApi.md#design_folders_id_children_delete) | **DELETE** /DesignFolders/{id}/children | Deletes all children of this model.
[**design_folders_id_children_fk_delete**](DesignFolderApi.md#design_folders_id_children_fk_delete) | **DELETE** /DesignFolders/{id}/children/{fk} | Delete a related item by id for children.
[**design_folders_id_children_fk_get**](DesignFolderApi.md#design_folders_id_children_fk_get) | **GET** /DesignFolders/{id}/children/{fk} | Find a related item by id for children.
[**design_folders_id_children_fk_put**](DesignFolderApi.md#design_folders_id_children_fk_put) | **PUT** /DesignFolders/{id}/children/{fk} | Update a related item by id for children.
[**design_folders_id_children_get**](DesignFolderApi.md#design_folders_id_children_get) | **GET** /DesignFolders/{id}/children | Queries children of DesignFolder.
[**design_folders_id_children_post**](DesignFolderApi.md#design_folders_id_children_post) | **POST** /DesignFolders/{id}/children | Creates a new instance in children of this model.
[**design_folders_id_delete**](DesignFolderApi.md#design_folders_id_delete) | **DELETE** /DesignFolders/{id} | Delete a model instance by {{id}} from the data source.
[**design_folders_id_designs_count_get**](DesignFolderApi.md#design_folders_id_designs_count_get) | **GET** /DesignFolders/{id}/designs/count | Counts designs of DesignFolder.
[**design_folders_id_designs_delete**](DesignFolderApi.md#design_folders_id_designs_delete) | **DELETE** /DesignFolders/{id}/designs | Deletes all designs of this model.
[**design_folders_id_designs_fk_delete**](DesignFolderApi.md#design_folders_id_designs_fk_delete) | **DELETE** /DesignFolders/{id}/designs/{fk} | Delete a related item by id for designs.
[**design_folders_id_designs_fk_get**](DesignFolderApi.md#design_folders_id_designs_fk_get) | **GET** /DesignFolders/{id}/designs/{fk} | Find a related item by id for designs.
[**design_folders_id_designs_fk_put**](DesignFolderApi.md#design_folders_id_designs_fk_put) | **PUT** /DesignFolders/{id}/designs/{fk} | Update a related item by id for designs.
[**design_folders_id_designs_get**](DesignFolderApi.md#design_folders_id_designs_get) | **GET** /DesignFolders/{id}/designs | Queries designs of DesignFolder.
[**design_folders_id_designs_post**](DesignFolderApi.md#design_folders_id_designs_post) | **POST** /DesignFolders/{id}/designs | Creates a new instance in designs of this model.
[**design_folders_id_exists_get**](DesignFolderApi.md#design_folders_id_exists_get) | **GET** /DesignFolders/{id}/exists | Check whether a model instance exists in the data source.
[**design_folders_id_get**](DesignFolderApi.md#design_folders_id_get) | **GET** /DesignFolders/{id} | Find a model instance by {{id}} from the data source.
[**design_folders_id_head**](DesignFolderApi.md#design_folders_id_head) | **HEAD** /DesignFolders/{id} | Check whether a model instance exists in the data source.
[**design_folders_id_member_get**](DesignFolderApi.md#design_folders_id_member_get) | **GET** /DesignFolders/{id}/member | Fetches belongsTo relation member.
[**design_folders_id_parent_get**](DesignFolderApi.md#design_folders_id_parent_get) | **GET** /DesignFolders/{id}/parent | Fetches belongsTo relation parent.
[**design_folders_id_patch**](DesignFolderApi.md#design_folders_id_patch) | **PATCH** /DesignFolders/{id} | Patch attributes for a model instance and persist it into the data source.
[**design_folders_id_portal_get**](DesignFolderApi.md#design_folders_id_portal_get) | **GET** /DesignFolders/{id}/portal | Fetches belongsTo relation portal.
[**design_folders_id_put**](DesignFolderApi.md#design_folders_id_put) | **PUT** /DesignFolders/{id} | Replace attributes for a model instance and persist it into the data source.
[**design_folders_id_replace_post**](DesignFolderApi.md#design_folders_id_replace_post) | **POST** /DesignFolders/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**design_folders_patch**](DesignFolderApi.md#design_folders_patch) | **PATCH** /DesignFolders | Patch an existing model instance or insert a new one into the data source.
[**design_folders_post**](DesignFolderApi.md#design_folders_post) | **POST** /DesignFolders | Create a new instance of the model and persist it into the data source.
[**design_folders_put**](DesignFolderApi.md#design_folders_put) | **PUT** /DesignFolders | Replace an existing model instance or insert a new one into the data source.
[**design_folders_replace_or_create_post**](DesignFolderApi.md#design_folders_replace_or_create_post) | **POST** /DesignFolders/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**design_folders_update_post**](DesignFolderApi.md#design_folders_update_post) | **POST** /DesignFolders/update | Update instances of the model matched by {{where}} from the data source.
[**design_folders_upsert_with_where_post**](DesignFolderApi.md#design_folders_upsert_with_where_post) | **POST** /DesignFolders/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **design_folders_change_stream_get**
> file design_folders_change_stream_get(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.design_folders_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_change_stream_get: %s\n" % e)
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

# **design_folders_change_stream_post**
> file design_folders_change_stream_post(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.design_folders_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_change_stream_post: %s\n" % e)
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

# **design_folders_count_get**
> InlineResponse200 design_folders_count_get(where=where)

Count instances of the model matched by where from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.design_folders_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_count_get: %s\n" % e)
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

# **design_folders_find_one_get**
> DesignFolder design_folders_find_one_get(filter=filter)

Find first instance of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.design_folders_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_get**
> list[DesignFolder] design_folders_get(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.design_folders_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[DesignFolder]**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_children_count_get**
> InlineResponse200 design_folders_id_children_count_get(id, where=where)

Counts children of DesignFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts children of DesignFolder.
    api_response = api_instance.design_folders_id_children_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_children_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_children_delete**
> design_folders_id_children_delete(id)

Deletes all children of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id

try: 
    # Deletes all children of this model.
    api_instance.design_folders_id_children_delete(id)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_children_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_children_fk_delete**
> design_folders_id_children_fk_delete(id, fk)

Delete a related item by id for children.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Delete a related item by id for children.
    api_instance.design_folders_id_children_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_children_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_children_fk_get**
> DesignFolder design_folders_id_children_fk_get(id, fk)

Find a related item by id for children.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Find a related item by id for children.
    api_response = api_instance.design_folders_id_children_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_children_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_children_fk_put**
> DesignFolder design_folders_id_children_fk_put(id, fk, data=data)

Update a related item by id for children.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
fk = 'fk_example' # str | Foreign key for children
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Update a related item by id for children.
    api_response = api_instance.design_folders_id_children_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_children_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **fk** | **str**| Foreign key for children | 
 **data** | [**DesignFolder**](DesignFolder.md)|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_children_get**
> list[DesignFolder] design_folders_id_children_get(id, filter=filter)

Queries children of DesignFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries children of DesignFolder.
    api_response = api_instance.design_folders_id_children_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignFolder]**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_children_post**
> DesignFolder design_folders_id_children_post(id, data=data)

Creates a new instance in children of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Creates a new instance in children of this model.
    api_response = api_instance.design_folders_id_children_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_children_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **data** | [**DesignFolder**](DesignFolder.md)|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_delete**
> object design_folders_id_delete(id)

Delete a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.design_folders_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_delete: %s\n" % e)
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

# **design_folders_id_designs_count_get**
> InlineResponse200 design_folders_id_designs_count_get(id, where=where)

Counts designs of DesignFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of DesignFolder.
    api_response = api_instance.design_folders_id_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_designs_delete**
> design_folders_id_designs_delete(id)

Deletes all designs of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id

try: 
    # Deletes all designs of this model.
    api_instance.design_folders_id_designs_delete(id)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_designs_fk_delete**
> design_folders_id_designs_fk_delete(id, fk)

Delete a related item by id for designs.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.design_folders_id_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_designs_fk_get**
> Design design_folders_id_designs_fk_get(id, fk)

Find a related item by id for designs.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.design_folders_id_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_designs_fk_put**
> Design design_folders_id_designs_fk_put(id, fk, data=data)

Update a related item by id for designs.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.design_folders_id_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_designs_get**
> list[Design] design_folders_id_designs_get(id, filter=filter)

Queries designs of DesignFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of DesignFolder.
    api_response = api_instance.design_folders_id_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_designs_post**
> Design design_folders_id_designs_post(id, data=data)

Creates a new instance in designs of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.design_folders_id_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_exists_get**
> InlineResponse2002 design_folders_id_exists_get(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.design_folders_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_exists_get: %s\n" % e)
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

# **design_folders_id_get**
> DesignFolder design_folders_id_get(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.design_folders_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_head**
> InlineResponse2002 design_folders_id_head(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.design_folders_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_head: %s\n" % e)
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

# **design_folders_id_member_get**
> TeamMember design_folders_id_member_get(id, refresh=refresh)

Fetches belongsTo relation member.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation member.
    api_response = api_instance.design_folders_id_member_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_parent_get**
> DesignFolder design_folders_id_parent_get(id, refresh=refresh)

Fetches belongsTo relation parent.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation parent.
    api_response = api_instance.design_folders_id_parent_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_parent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_patch**
> DesignFolder design_folders_id_patch(id, data=data)

Patch attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
data = TweakApi.DesignFolder() # DesignFolder | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_folders_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **data** | [**DesignFolder**](DesignFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_portal_get**
> Portal design_folders_id_portal_get(id, refresh=refresh)

Fetches belongsTo relation portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | DesignFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation portal.
    api_response = api_instance.design_folders_id_portal_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_portal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_put**
> DesignFolder design_folders_id_put(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.DesignFolder() # DesignFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_folders_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DesignFolder**](DesignFolder.md)| Model instance data | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_id_replace_post**
> DesignFolder design_folders_id_replace_post(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.DesignFolder() # DesignFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_folders_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DesignFolder**](DesignFolder.md)| Model instance data | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_patch**
> DesignFolder design_folders_patch(data=data)

Patch an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
data = TweakApi.DesignFolder() # DesignFolder | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_folders_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignFolder**](DesignFolder.md)| Model instance data | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_post**
> DesignFolder design_folders_post(data=data)

Create a new instance of the model and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
data = TweakApi.DesignFolder() # DesignFolder | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.design_folders_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignFolder**](DesignFolder.md)| Model instance data | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_put**
> DesignFolder design_folders_put(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
data = TweakApi.DesignFolder() # DesignFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_folders_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignFolder**](DesignFolder.md)| Model instance data | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_replace_or_create_post**
> DesignFolder design_folders_replace_or_create_post(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
data = TweakApi.DesignFolder() # DesignFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_folders_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignFolder**](DesignFolder.md)| Model instance data | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_update_post**
> InlineResponse2001 design_folders_update_post(where=where, data=data)

Update instances of the model matched by {{where}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DesignFolder() # DesignFolder | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.design_folders_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DesignFolder**](DesignFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_folders_upsert_with_where_post**
> DesignFolder design_folders_upsert_with_where_post(where=where, data=data)

Update an existing model instance or insert a new one into the data source based on the where criteria.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DesignFolder() # DesignFolder | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.design_folders_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignFolderApi->design_folders_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DesignFolder**](DesignFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

