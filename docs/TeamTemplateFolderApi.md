# TweakApi.TeamTemplateFolderApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_template_folders_change_stream_get**](TeamTemplateFolderApi.md#team_template_folders_change_stream_get) | **GET** /TeamTemplateFolders/change-stream | Create a change stream.
[**team_template_folders_change_stream_post**](TeamTemplateFolderApi.md#team_template_folders_change_stream_post) | **POST** /TeamTemplateFolders/change-stream | Create a change stream.
[**team_template_folders_count_get**](TeamTemplateFolderApi.md#team_template_folders_count_get) | **GET** /TeamTemplateFolders/count | Count instances of the model matched by where from the data source.
[**team_template_folders_find_one_get**](TeamTemplateFolderApi.md#team_template_folders_find_one_get) | **GET** /TeamTemplateFolders/findOne | Find first instance of the model matched by filter from the data source.
[**team_template_folders_get**](TeamTemplateFolderApi.md#team_template_folders_get) | **GET** /TeamTemplateFolders | Find all instances of the model matched by filter from the data source.
[**team_template_folders_id_children_count_get**](TeamTemplateFolderApi.md#team_template_folders_id_children_count_get) | **GET** /TeamTemplateFolders/{id}/children/count | Counts children of TeamTemplateFolder.
[**team_template_folders_id_children_delete**](TeamTemplateFolderApi.md#team_template_folders_id_children_delete) | **DELETE** /TeamTemplateFolders/{id}/children | Deletes all children of this model.
[**team_template_folders_id_children_fk_delete**](TeamTemplateFolderApi.md#team_template_folders_id_children_fk_delete) | **DELETE** /TeamTemplateFolders/{id}/children/{fk} | Delete a related item by id for children.
[**team_template_folders_id_children_fk_get**](TeamTemplateFolderApi.md#team_template_folders_id_children_fk_get) | **GET** /TeamTemplateFolders/{id}/children/{fk} | Find a related item by id for children.
[**team_template_folders_id_children_fk_put**](TeamTemplateFolderApi.md#team_template_folders_id_children_fk_put) | **PUT** /TeamTemplateFolders/{id}/children/{fk} | Update a related item by id for children.
[**team_template_folders_id_children_get**](TeamTemplateFolderApi.md#team_template_folders_id_children_get) | **GET** /TeamTemplateFolders/{id}/children | Queries children of TeamTemplateFolder.
[**team_template_folders_id_children_post**](TeamTemplateFolderApi.md#team_template_folders_id_children_post) | **POST** /TeamTemplateFolders/{id}/children | Creates a new instance in children of this model.
[**team_template_folders_id_delete**](TeamTemplateFolderApi.md#team_template_folders_id_delete) | **DELETE** /TeamTemplateFolders/{id} | Delete a model instance by {{id}} from the data source.
[**team_template_folders_id_exists_get**](TeamTemplateFolderApi.md#team_template_folders_id_exists_get) | **GET** /TeamTemplateFolders/{id}/exists | Check whether a model instance exists in the data source.
[**team_template_folders_id_get**](TeamTemplateFolderApi.md#team_template_folders_id_get) | **GET** /TeamTemplateFolders/{id} | Find a model instance by {{id}} from the data source.
[**team_template_folders_id_head**](TeamTemplateFolderApi.md#team_template_folders_id_head) | **HEAD** /TeamTemplateFolders/{id} | Check whether a model instance exists in the data source.
[**team_template_folders_id_parent_get**](TeamTemplateFolderApi.md#team_template_folders_id_parent_get) | **GET** /TeamTemplateFolders/{id}/parent | Fetches belongsTo relation parent.
[**team_template_folders_id_patch**](TeamTemplateFolderApi.md#team_template_folders_id_patch) | **PATCH** /TeamTemplateFolders/{id} | Patch attributes for a model instance and persist it into the data source.
[**team_template_folders_id_put**](TeamTemplateFolderApi.md#team_template_folders_id_put) | **PUT** /TeamTemplateFolders/{id} | Replace attributes for a model instance and persist it into the data source.
[**team_template_folders_id_replace_post**](TeamTemplateFolderApi.md#team_template_folders_id_replace_post) | **POST** /TeamTemplateFolders/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**team_template_folders_id_team_get**](TeamTemplateFolderApi.md#team_template_folders_id_team_get) | **GET** /TeamTemplateFolders/{id}/team | Fetches belongsTo relation team.
[**team_template_folders_id_templates_count_get**](TeamTemplateFolderApi.md#team_template_folders_id_templates_count_get) | **GET** /TeamTemplateFolders/{id}/templates/count | Counts templates of TeamTemplateFolder.
[**team_template_folders_id_templates_delete**](TeamTemplateFolderApi.md#team_template_folders_id_templates_delete) | **DELETE** /TeamTemplateFolders/{id}/templates | Deletes all templates of this model.
[**team_template_folders_id_templates_fk_delete**](TeamTemplateFolderApi.md#team_template_folders_id_templates_fk_delete) | **DELETE** /TeamTemplateFolders/{id}/templates/{fk} | Delete a related item by id for templates.
[**team_template_folders_id_templates_fk_get**](TeamTemplateFolderApi.md#team_template_folders_id_templates_fk_get) | **GET** /TeamTemplateFolders/{id}/templates/{fk} | Find a related item by id for templates.
[**team_template_folders_id_templates_fk_put**](TeamTemplateFolderApi.md#team_template_folders_id_templates_fk_put) | **PUT** /TeamTemplateFolders/{id}/templates/{fk} | Update a related item by id for templates.
[**team_template_folders_id_templates_get**](TeamTemplateFolderApi.md#team_template_folders_id_templates_get) | **GET** /TeamTemplateFolders/{id}/templates | Queries templates of TeamTemplateFolder.
[**team_template_folders_id_templates_post**](TeamTemplateFolderApi.md#team_template_folders_id_templates_post) | **POST** /TeamTemplateFolders/{id}/templates | Creates a new instance in templates of this model.
[**team_template_folders_patch**](TeamTemplateFolderApi.md#team_template_folders_patch) | **PATCH** /TeamTemplateFolders | Patch an existing model instance or insert a new one into the data source.
[**team_template_folders_post**](TeamTemplateFolderApi.md#team_template_folders_post) | **POST** /TeamTemplateFolders | Create a new instance of the model and persist it into the data source.
[**team_template_folders_put**](TeamTemplateFolderApi.md#team_template_folders_put) | **PUT** /TeamTemplateFolders | Replace an existing model instance or insert a new one into the data source.
[**team_template_folders_replace_or_create_post**](TeamTemplateFolderApi.md#team_template_folders_replace_or_create_post) | **POST** /TeamTemplateFolders/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**team_template_folders_update_post**](TeamTemplateFolderApi.md#team_template_folders_update_post) | **POST** /TeamTemplateFolders/update | Update instances of the model matched by {{where}} from the data source.
[**team_template_folders_upsert_with_where_post**](TeamTemplateFolderApi.md#team_template_folders_upsert_with_where_post) | **POST** /TeamTemplateFolders/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **team_template_folders_change_stream_get**
> file team_template_folders_change_stream_get(options=options)

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
api_instance = TweakApi.TeamTemplateFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_template_folders_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_change_stream_get: %s\n" % e)
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

# **team_template_folders_change_stream_post**
> file team_template_folders_change_stream_post(options=options)

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
api_instance = TweakApi.TeamTemplateFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_template_folders_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_change_stream_post: %s\n" % e)
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

# **team_template_folders_count_get**
> InlineResponse200 team_template_folders_count_get(where=where)

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
api_instance = TweakApi.TeamTemplateFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.team_template_folders_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_count_get: %s\n" % e)
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

# **team_template_folders_find_one_get**
> TeamTemplateFolder team_template_folders_find_one_get(filter=filter)

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
api_instance = TweakApi.TeamTemplateFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.team_template_folders_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_get**
> list[TeamTemplateFolder] team_template_folders_get(filter=filter)

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
api_instance = TweakApi.TeamTemplateFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.team_template_folders_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamTemplateFolder]**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_children_count_get**
> InlineResponse200 team_template_folders_id_children_count_get(id, where=where)

Counts children of TeamTemplateFolder.

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts children of TeamTemplateFolder.
    api_response = api_instance.team_template_folders_id_children_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_children_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_children_delete**
> team_template_folders_id_children_delete(id)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id

try: 
    # Deletes all children of this model.
    api_instance.team_template_folders_id_children_delete(id)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_children_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_children_fk_delete**
> team_template_folders_id_children_fk_delete(id, fk)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Delete a related item by id for children.
    api_instance.team_template_folders_id_children_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_children_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_children_fk_get**
> TeamTemplateFolder team_template_folders_id_children_fk_get(id, fk)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
fk = 'fk_example' # str | Foreign key for children

try: 
    # Find a related item by id for children.
    api_response = api_instance.team_template_folders_id_children_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_children_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **fk** | **str**| Foreign key for children | 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_children_fk_put**
> TeamTemplateFolder team_template_folders_id_children_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
fk = 'fk_example' # str | Foreign key for children
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Update a related item by id for children.
    api_response = api_instance.team_template_folders_id_children_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_children_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **fk** | **str**| Foreign key for children | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_children_get**
> list[TeamTemplateFolder] team_template_folders_id_children_get(id, filter=filter)

Queries children of TeamTemplateFolder.

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries children of TeamTemplateFolder.
    api_response = api_instance.team_template_folders_id_children_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamTemplateFolder]**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_children_post**
> TeamTemplateFolder team_template_folders_id_children_post(id, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Creates a new instance in children of this model.
    api_response = api_instance.team_template_folders_id_children_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_children_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_delete**
> object team_template_folders_id_delete(id)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.team_template_folders_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_delete: %s\n" % e)
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

# **team_template_folders_id_exists_get**
> InlineResponse2001 team_template_folders_id_exists_get(id)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_template_folders_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_exists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_get**
> TeamTemplateFolder team_template_folders_id_get(id, filter=filter)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.team_template_folders_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_head**
> InlineResponse2001 team_template_folders_id_head(id)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_template_folders_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_parent_get**
> TeamTemplateFolder team_template_folders_id_parent_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation parent.
    api_response = api_instance.team_template_folders_id_parent_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_parent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_patch**
> TeamTemplateFolder team_template_folders_id_patch(id, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_template_folders_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_put**
> TeamTemplateFolder team_template_folders_id_put(id, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_template_folders_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_replace_post**
> TeamTemplateFolder team_template_folders_id_replace_post(id, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_template_folders_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_team_get**
> Team team_template_folders_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.team_template_folders_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_templates_count_get**
> InlineResponse200 team_template_folders_id_templates_count_get(id, where=where)

Counts templates of TeamTemplateFolder.

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of TeamTemplateFolder.
    api_response = api_instance.team_template_folders_id_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_templates_delete**
> team_template_folders_id_templates_delete(id)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id

try: 
    # Deletes all templates of this model.
    api_instance.team_template_folders_id_templates_delete(id)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_templates_fk_delete**
> team_template_folders_id_templates_fk_delete(id, fk)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.team_template_folders_id_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_templates_fk_get**
> Template team_template_folders_id_templates_fk_get(id, fk)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.team_template_folders_id_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_templates_fk_put**
> Template team_template_folders_id_templates_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.team_template_folders_id_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
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

# **team_template_folders_id_templates_get**
> list[Template] team_template_folders_id_templates_get(id, filter=filter)

Queries templates of TeamTemplateFolder.

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of TeamTemplateFolder.
    api_response = api_instance.team_template_folders_id_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_id_templates_post**
> Template team_template_folders_id_templates_post(id, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
id = 'id_example' # str | TeamTemplateFolder id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.team_template_folders_id_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_id_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamTemplateFolder id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_patch**
> TeamTemplateFolder team_template_folders_patch(data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_template_folders_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_post**
> TeamTemplateFolder team_template_folders_post(data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.team_template_folders_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_put**
> TeamTemplateFolder team_template_folders_put(data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_template_folders_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_replace_or_create_post**
> TeamTemplateFolder team_template_folders_replace_or_create_post(data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_template_folders_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| Model instance data | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_update_post**
> InlineResponse2002 team_template_folders_update_post(where=where, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.team_template_folders_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_template_folders_upsert_with_where_post**
> TeamTemplateFolder team_template_folders_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.TeamTemplateFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.team_template_folders_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamTemplateFolderApi->team_template_folders_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

