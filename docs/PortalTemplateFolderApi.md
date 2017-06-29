# TweakApi.PortalTemplateFolderApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal_template_folders_change_stream_get**](PortalTemplateFolderApi.md#portal_template_folders_change_stream_get) | **GET** /PortalTemplateFolders/change-stream | Create a change stream.
[**portal_template_folders_change_stream_post**](PortalTemplateFolderApi.md#portal_template_folders_change_stream_post) | **POST** /PortalTemplateFolders/change-stream | Create a change stream.
[**portal_template_folders_count_get**](PortalTemplateFolderApi.md#portal_template_folders_count_get) | **GET** /PortalTemplateFolders/count | Count instances of the model matched by where from the data source.
[**portal_template_folders_find_one_get**](PortalTemplateFolderApi.md#portal_template_folders_find_one_get) | **GET** /PortalTemplateFolders/findOne | Find first instance of the model matched by filter from the data source.
[**portal_template_folders_get**](PortalTemplateFolderApi.md#portal_template_folders_get) | **GET** /PortalTemplateFolders | Find all instances of the model matched by filter from the data source.
[**portal_template_folders_id_children_count_get**](PortalTemplateFolderApi.md#portal_template_folders_id_children_count_get) | **GET** /PortalTemplateFolders/{id}/children/count | Counts children of PortalTemplateFolder.
[**portal_template_folders_id_children_delete**](PortalTemplateFolderApi.md#portal_template_folders_id_children_delete) | **DELETE** /PortalTemplateFolders/{id}/children | Deletes all children of this model.
[**portal_template_folders_id_children_fk_delete**](PortalTemplateFolderApi.md#portal_template_folders_id_children_fk_delete) | **DELETE** /PortalTemplateFolders/{id}/children/{fk} | Delete a related item by id for children.
[**portal_template_folders_id_children_fk_get**](PortalTemplateFolderApi.md#portal_template_folders_id_children_fk_get) | **GET** /PortalTemplateFolders/{id}/children/{fk} | Find a related item by id for children.
[**portal_template_folders_id_children_fk_put**](PortalTemplateFolderApi.md#portal_template_folders_id_children_fk_put) | **PUT** /PortalTemplateFolders/{id}/children/{fk} | Update a related item by id for children.
[**portal_template_folders_id_children_get**](PortalTemplateFolderApi.md#portal_template_folders_id_children_get) | **GET** /PortalTemplateFolders/{id}/children | Queries children of PortalTemplateFolder.
[**portal_template_folders_id_children_post**](PortalTemplateFolderApi.md#portal_template_folders_id_children_post) | **POST** /PortalTemplateFolders/{id}/children | Creates a new instance in children of this model.
[**portal_template_folders_id_delete**](PortalTemplateFolderApi.md#portal_template_folders_id_delete) | **DELETE** /PortalTemplateFolders/{id} | Delete a model instance by {{id}} from the data source.
[**portal_template_folders_id_exists_get**](PortalTemplateFolderApi.md#portal_template_folders_id_exists_get) | **GET** /PortalTemplateFolders/{id}/exists | Check whether a model instance exists in the data source.
[**portal_template_folders_id_get**](PortalTemplateFolderApi.md#portal_template_folders_id_get) | **GET** /PortalTemplateFolders/{id} | Find a model instance by {{id}} from the data source.
[**portal_template_folders_id_head**](PortalTemplateFolderApi.md#portal_template_folders_id_head) | **HEAD** /PortalTemplateFolders/{id} | Check whether a model instance exists in the data source.
[**portal_template_folders_id_parent_get**](PortalTemplateFolderApi.md#portal_template_folders_id_parent_get) | **GET** /PortalTemplateFolders/{id}/parent | Fetches belongsTo relation parent.
[**portal_template_folders_id_patch**](PortalTemplateFolderApi.md#portal_template_folders_id_patch) | **PATCH** /PortalTemplateFolders/{id} | Patch attributes for a model instance and persist it into the data source.
[**portal_template_folders_id_portal_get**](PortalTemplateFolderApi.md#portal_template_folders_id_portal_get) | **GET** /PortalTemplateFolders/{id}/portal | Fetches belongsTo relation portal.
[**portal_template_folders_id_put**](PortalTemplateFolderApi.md#portal_template_folders_id_put) | **PUT** /PortalTemplateFolders/{id} | Replace attributes for a model instance and persist it into the data source.
[**portal_template_folders_id_replace_post**](PortalTemplateFolderApi.md#portal_template_folders_id_replace_post) | **POST** /PortalTemplateFolders/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**portal_template_folders_id_templates_count_get**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_count_get) | **GET** /PortalTemplateFolders/{id}/templates/count | Counts templates of PortalTemplateFolder.
[**portal_template_folders_id_templates_delete**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_delete) | **DELETE** /PortalTemplateFolders/{id}/templates | Deletes all templates of this model.
[**portal_template_folders_id_templates_fk_delete**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_fk_delete) | **DELETE** /PortalTemplateFolders/{id}/templates/{fk} | Delete a related item by id for templates.
[**portal_template_folders_id_templates_fk_get**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_fk_get) | **GET** /PortalTemplateFolders/{id}/templates/{fk} | Find a related item by id for templates.
[**portal_template_folders_id_templates_fk_put**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_fk_put) | **PUT** /PortalTemplateFolders/{id}/templates/{fk} | Update a related item by id for templates.
[**portal_template_folders_id_templates_get**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_get) | **GET** /PortalTemplateFolders/{id}/templates | Queries templates of PortalTemplateFolder.
[**portal_template_folders_id_templates_post**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_post) | **POST** /PortalTemplateFolders/{id}/templates | Creates a new instance in templates of this model.
[**portal_template_folders_id_templates_rel_fk_delete**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_rel_fk_delete) | **DELETE** /PortalTemplateFolders/{id}/templates/rel/{fk} | Remove the templates relation to an item by id.
[**portal_template_folders_id_templates_rel_fk_head**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_rel_fk_head) | **HEAD** /PortalTemplateFolders/{id}/templates/rel/{fk} | Check the existence of templates relation to an item by id.
[**portal_template_folders_id_templates_rel_fk_put**](PortalTemplateFolderApi.md#portal_template_folders_id_templates_rel_fk_put) | **PUT** /PortalTemplateFolders/{id}/templates/rel/{fk} | Add a related item by id for templates.
[**portal_template_folders_patch**](PortalTemplateFolderApi.md#portal_template_folders_patch) | **PATCH** /PortalTemplateFolders | Patch an existing model instance or insert a new one into the data source.
[**portal_template_folders_post**](PortalTemplateFolderApi.md#portal_template_folders_post) | **POST** /PortalTemplateFolders | Create a new instance of the model and persist it into the data source.
[**portal_template_folders_put**](PortalTemplateFolderApi.md#portal_template_folders_put) | **PUT** /PortalTemplateFolders | Replace an existing model instance or insert a new one into the data source.
[**portal_template_folders_replace_or_create_post**](PortalTemplateFolderApi.md#portal_template_folders_replace_or_create_post) | **POST** /PortalTemplateFolders/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**portal_template_folders_update_post**](PortalTemplateFolderApi.md#portal_template_folders_update_post) | **POST** /PortalTemplateFolders/update | Update instances of the model matched by {{where}} from the data source.
[**portal_template_folders_upsert_with_where_post**](PortalTemplateFolderApi.md#portal_template_folders_upsert_with_where_post) | **POST** /PortalTemplateFolders/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **portal_template_folders_change_stream_get**
> file portal_template_folders_change_stream_get(options=options)

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
api_instance = TweakApi.PortalTemplateFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portal_template_folders_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_change_stream_get: %s\n" % e)
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

# **portal_template_folders_change_stream_post**
> file portal_template_folders_change_stream_post(options=options)

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
api_instance = TweakApi.PortalTemplateFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portal_template_folders_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_change_stream_post: %s\n" % e)
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

# **portal_template_folders_count_get**
> InlineResponse200 portal_template_folders_count_get(where=where)

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
api_instance = TweakApi.PortalTemplateFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.portal_template_folders_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_count_get: %s\n" % e)
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

# **portal_template_folders_find_one_get**
> PortalTemplateFolder portal_template_folders_find_one_get(filter=filter)

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
api_instance = TweakApi.PortalTemplateFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.portal_template_folders_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_get**
> list[PortalTemplateFolder] portal_template_folders_get(filter=filter)

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
api_instance = TweakApi.PortalTemplateFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.portal_template_folders_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[PortalTemplateFolder]**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_children_count_get**
> InlineResponse200 portal_template_folders_id_children_count_get(id, where=where)

Counts children of PortalTemplateFolder.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts children of PortalTemplateFolder.
    api_response = api_instance.portal_template_folders_id_children_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_children_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_children_delete**
> portal_template_folders_id_children_delete(id)

Deletes all children of this model.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id

try: 
    # Deletes all children of this model.
    api_instance.portal_template_folders_id_children_delete(id)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_children_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_children_fk_delete**
> portal_template_folders_id_children_fk_delete(id, fk)

Delete a related item by id for children.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Delete a related item by id for children.
    api_instance.portal_template_folders_id_children_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_children_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_children_fk_get**
> PortalTemplateFolder portal_template_folders_id_children_fk_get(id, fk)

Find a related item by id for children.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Find a related item by id for children.
    api_response = api_instance.portal_template_folders_id_children_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_children_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_children_fk_put**
> PortalTemplateFolder portal_template_folders_id_children_fk_put(id, fk, data=data)

Update a related item by id for children.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for children
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Update a related item by id for children.
    api_response = api_instance.portal_template_folders_id_children_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_children_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for children | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_children_get**
> list[PortalTemplateFolder] portal_template_folders_id_children_get(id, filter=filter)

Queries children of PortalTemplateFolder.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries children of PortalTemplateFolder.
    api_response = api_instance.portal_template_folders_id_children_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalTemplateFolder]**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_children_post**
> PortalTemplateFolder portal_template_folders_id_children_post(id, data=data)

Creates a new instance in children of this model.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Creates a new instance in children of this model.
    api_response = api_instance.portal_template_folders_id_children_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_children_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_delete**
> object portal_template_folders_id_delete(id)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.portal_template_folders_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_delete: %s\n" % e)
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

# **portal_template_folders_id_exists_get**
> InlineResponse2002 portal_template_folders_id_exists_get(id)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portal_template_folders_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_exists_get: %s\n" % e)
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

# **portal_template_folders_id_get**
> PortalTemplateFolder portal_template_folders_id_get(id, filter=filter)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.portal_template_folders_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_head**
> InlineResponse2002 portal_template_folders_id_head(id)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portal_template_folders_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_head: %s\n" % e)
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

# **portal_template_folders_id_parent_get**
> PortalTemplateFolder portal_template_folders_id_parent_get(id, refresh=refresh)

Fetches belongsTo relation parent.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation parent.
    api_response = api_instance.portal_template_folders_id_parent_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_parent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_patch**
> PortalTemplateFolder portal_template_folders_id_patch(id, data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_template_folders_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_portal_get**
> Portal portal_template_folders_id_portal_get(id, refresh=refresh)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation portal.
    api_response = api_instance.portal_template_folders_id_portal_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_portal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_put**
> PortalTemplateFolder portal_template_folders_id_put(id, data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_template_folders_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_replace_post**
> PortalTemplateFolder portal_template_folders_id_replace_post(id, data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_template_folders_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_count_get**
> InlineResponse200 portal_template_folders_id_templates_count_get(id, where=where)

Counts templates of PortalTemplateFolder.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of PortalTemplateFolder.
    api_response = api_instance.portal_template_folders_id_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_delete**
> portal_template_folders_id_templates_delete(id)

Deletes all templates of this model.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id

try: 
    # Deletes all templates of this model.
    api_instance.portal_template_folders_id_templates_delete(id)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_fk_delete**
> portal_template_folders_id_templates_fk_delete(id, fk)

Delete a related item by id for templates.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.portal_template_folders_id_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_fk_get**
> Template portal_template_folders_id_templates_fk_get(id, fk)

Find a related item by id for templates.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.portal_template_folders_id_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_fk_put**
> Template portal_template_folders_id_templates_fk_put(id, fk, data=data)

Update a related item by id for templates.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.portal_template_folders_id_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_get**
> list[Template] portal_template_folders_id_templates_get(id, filter=filter)

Queries templates of PortalTemplateFolder.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of PortalTemplateFolder.
    api_response = api_instance.portal_template_folders_id_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_post**
> Template portal_template_folders_id_templates_post(id, data=data)

Creates a new instance in templates of this model.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.portal_template_folders_id_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_rel_fk_delete**
> portal_template_folders_id_templates_rel_fk_delete(id, fk)

Remove the templates relation to an item by id.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Remove the templates relation to an item by id.
    api_instance.portal_template_folders_id_templates_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_rel_fk_head**
> bool portal_template_folders_id_templates_rel_fk_head(id, fk)

Check the existence of templates relation to an item by id.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Check the existence of templates relation to an item by id.
    api_response = api_instance.portal_template_folders_id_templates_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_id_templates_rel_fk_put**
> PortalTemplate portal_template_folders_id_templates_rel_fk_put(id, fk, data=data)

Add a related item by id for templates.

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
api_instance = TweakApi.PortalTemplateFolderApi()
id = 'id_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Add a related item by id for templates.
    api_response = api_instance.portal_template_folders_id_templates_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_id_templates_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_patch**
> PortalTemplateFolder portal_template_folders_patch(data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.portal_template_folders_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_post**
> PortalTemplateFolder portal_template_folders_post(data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.portal_template_folders_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_put**
> PortalTemplateFolder portal_template_folders_put(data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.portal_template_folders_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_replace_or_create_post**
> PortalTemplateFolder portal_template_folders_replace_or_create_post(data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.portal_template_folders_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_update_post**
> InlineResponse2001 portal_template_folders_update_post(where=where, data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.portal_template_folders_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_template_folders_upsert_with_where_post**
> PortalTemplateFolder portal_template_folders_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.PortalTemplateFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.portal_template_folders_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateFolderApi->portal_template_folders_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

