# TweakApi.DesignTagApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**design_tags_change_stream_get**](DesignTagApi.md#design_tags_change_stream_get) | **GET** /DesignTags/change-stream | Create a change stream.
[**design_tags_change_stream_post**](DesignTagApi.md#design_tags_change_stream_post) | **POST** /DesignTags/change-stream | Create a change stream.
[**design_tags_count_get**](DesignTagApi.md#design_tags_count_get) | **GET** /DesignTags/count | Count instances of the model matched by where from the data source.
[**design_tags_find_one_get**](DesignTagApi.md#design_tags_find_one_get) | **GET** /DesignTags/findOne | Find first instance of the model matched by filter from the data source.
[**design_tags_get**](DesignTagApi.md#design_tags_get) | **GET** /DesignTags | Find all instances of the model matched by filter from the data source.
[**design_tags_id_delete**](DesignTagApi.md#design_tags_id_delete) | **DELETE** /DesignTags/{id} | Delete a model instance by {{id}} from the data source.
[**design_tags_id_design_get**](DesignTagApi.md#design_tags_id_design_get) | **GET** /DesignTags/{id}/design | Fetches belongsTo relation design.
[**design_tags_id_exists_get**](DesignTagApi.md#design_tags_id_exists_get) | **GET** /DesignTags/{id}/exists | Check whether a model instance exists in the data source.
[**design_tags_id_get**](DesignTagApi.md#design_tags_id_get) | **GET** /DesignTags/{id} | Find a model instance by {{id}} from the data source.
[**design_tags_id_head**](DesignTagApi.md#design_tags_id_head) | **HEAD** /DesignTags/{id} | Check whether a model instance exists in the data source.
[**design_tags_id_patch**](DesignTagApi.md#design_tags_id_patch) | **PATCH** /DesignTags/{id} | Patch attributes for a model instance and persist it into the data source.
[**design_tags_id_put**](DesignTagApi.md#design_tags_id_put) | **PUT** /DesignTags/{id} | Replace attributes for a model instance and persist it into the data source.
[**design_tags_id_replace_post**](DesignTagApi.md#design_tags_id_replace_post) | **POST** /DesignTags/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**design_tags_id_tag_get**](DesignTagApi.md#design_tags_id_tag_get) | **GET** /DesignTags/{id}/tag | Fetches belongsTo relation tag.
[**design_tags_patch**](DesignTagApi.md#design_tags_patch) | **PATCH** /DesignTags | Patch an existing model instance or insert a new one into the data source.
[**design_tags_post**](DesignTagApi.md#design_tags_post) | **POST** /DesignTags | Create a new instance of the model and persist it into the data source.
[**design_tags_put**](DesignTagApi.md#design_tags_put) | **PUT** /DesignTags | Replace an existing model instance or insert a new one into the data source.
[**design_tags_replace_or_create_post**](DesignTagApi.md#design_tags_replace_or_create_post) | **POST** /DesignTags/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**design_tags_update_post**](DesignTagApi.md#design_tags_update_post) | **POST** /DesignTags/update | Update instances of the model matched by {{where}} from the data source.
[**design_tags_upsert_with_where_post**](DesignTagApi.md#design_tags_upsert_with_where_post) | **POST** /DesignTags/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **design_tags_change_stream_get**
> file design_tags_change_stream_get(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.design_tags_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_change_stream_get: %s\n" % e)
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

# **design_tags_change_stream_post**
> file design_tags_change_stream_post(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.design_tags_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_change_stream_post: %s\n" % e)
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

# **design_tags_count_get**
> InlineResponse200 design_tags_count_get(where=where)

Count instances of the model matched by where from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.design_tags_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_count_get: %s\n" % e)
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

# **design_tags_find_one_get**
> DesignTag design_tags_find_one_get(filter=filter)

Find first instance of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.design_tags_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_get**
> list[DesignTag] design_tags_get(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.design_tags_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[DesignTag]**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_id_delete**
> object design_tags_id_delete(id)

Delete a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.design_tags_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_delete: %s\n" % e)
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

# **design_tags_id_design_get**
> Design design_tags_id_design_get(id, refresh=refresh)

Fetches belongsTo relation design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | DesignTag id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation design.
    api_response = api_instance.design_tags_id_design_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_design_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignTag id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_id_exists_get**
> InlineResponse2002 design_tags_id_exists_get(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.design_tags_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_exists_get: %s\n" % e)
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

# **design_tags_id_get**
> DesignTag design_tags_id_get(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.design_tags_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_id_head**
> InlineResponse2002 design_tags_id_head(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.design_tags_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_head: %s\n" % e)
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

# **design_tags_id_patch**
> DesignTag design_tags_id_patch(id, data=data)

Patch attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | DesignTag id
data = TweakApi.DesignTag() # DesignTag | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_tags_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignTag id | 
 **data** | [**DesignTag**](DesignTag.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_id_put**
> DesignTag design_tags_id_put(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | Model id
data = TweakApi.DesignTag() # DesignTag | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_tags_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DesignTag**](DesignTag.md)| Model instance data | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_id_replace_post**
> DesignTag design_tags_id_replace_post(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | Model id
data = TweakApi.DesignTag() # DesignTag | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_tags_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DesignTag**](DesignTag.md)| Model instance data | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_id_tag_get**
> Tag design_tags_id_tag_get(id, refresh=refresh)

Fetches belongsTo relation tag.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
id = 'id_example' # str | DesignTag id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation tag.
    api_response = api_instance.design_tags_id_tag_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_id_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignTag id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_patch**
> DesignTag design_tags_patch(data=data)

Patch an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
data = TweakApi.DesignTag() # DesignTag | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_tags_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignTag**](DesignTag.md)| Model instance data | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_post**
> DesignTag design_tags_post(data=data)

Create a new instance of the model and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
data = TweakApi.DesignTag() # DesignTag | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.design_tags_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignTag**](DesignTag.md)| Model instance data | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_put**
> DesignTag design_tags_put(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
data = TweakApi.DesignTag() # DesignTag | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_tags_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignTag**](DesignTag.md)| Model instance data | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_replace_or_create_post**
> DesignTag design_tags_replace_or_create_post(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
data = TweakApi.DesignTag() # DesignTag | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_tags_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignTag**](DesignTag.md)| Model instance data | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_update_post**
> InlineResponse2001 design_tags_update_post(where=where, data=data)

Update instances of the model matched by {{where}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DesignTag() # DesignTag | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.design_tags_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DesignTag**](DesignTag.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_tags_upsert_with_where_post**
> DesignTag design_tags_upsert_with_where_post(where=where, data=data)

Update an existing model instance or insert a new one into the data source based on the where criteria.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.DesignTagApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DesignTag() # DesignTag | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.design_tags_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignTagApi->design_tags_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DesignTag**](DesignTag.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

