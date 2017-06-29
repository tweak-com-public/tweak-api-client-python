# TweakApi.ImageFolderMemberApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_folder_members_change_stream_get**](ImageFolderMemberApi.md#image_folder_members_change_stream_get) | **GET** /ImageFolderMembers/change-stream | Create a change stream.
[**image_folder_members_change_stream_post**](ImageFolderMemberApi.md#image_folder_members_change_stream_post) | **POST** /ImageFolderMembers/change-stream | Create a change stream.
[**image_folder_members_count_get**](ImageFolderMemberApi.md#image_folder_members_count_get) | **GET** /ImageFolderMembers/count | Count instances of the model matched by where from the data source.
[**image_folder_members_find_one_get**](ImageFolderMemberApi.md#image_folder_members_find_one_get) | **GET** /ImageFolderMembers/findOne | Find first instance of the model matched by filter from the data source.
[**image_folder_members_get**](ImageFolderMemberApi.md#image_folder_members_get) | **GET** /ImageFolderMembers | Find all instances of the model matched by filter from the data source.
[**image_folder_members_id_delete**](ImageFolderMemberApi.md#image_folder_members_id_delete) | **DELETE** /ImageFolderMembers/{id} | Delete a model instance by {{id}} from the data source.
[**image_folder_members_id_exists_get**](ImageFolderMemberApi.md#image_folder_members_id_exists_get) | **GET** /ImageFolderMembers/{id}/exists | Check whether a model instance exists in the data source.
[**image_folder_members_id_folder_get**](ImageFolderMemberApi.md#image_folder_members_id_folder_get) | **GET** /ImageFolderMembers/{id}/folder | Fetches belongsTo relation folder.
[**image_folder_members_id_get**](ImageFolderMemberApi.md#image_folder_members_id_get) | **GET** /ImageFolderMembers/{id} | Find a model instance by {{id}} from the data source.
[**image_folder_members_id_head**](ImageFolderMemberApi.md#image_folder_members_id_head) | **HEAD** /ImageFolderMembers/{id} | Check whether a model instance exists in the data source.
[**image_folder_members_id_member_get**](ImageFolderMemberApi.md#image_folder_members_id_member_get) | **GET** /ImageFolderMembers/{id}/member | Fetches belongsTo relation member.
[**image_folder_members_id_patch**](ImageFolderMemberApi.md#image_folder_members_id_patch) | **PATCH** /ImageFolderMembers/{id} | Patch attributes for a model instance and persist it into the data source.
[**image_folder_members_id_put**](ImageFolderMemberApi.md#image_folder_members_id_put) | **PUT** /ImageFolderMembers/{id} | Replace attributes for a model instance and persist it into the data source.
[**image_folder_members_id_replace_post**](ImageFolderMemberApi.md#image_folder_members_id_replace_post) | **POST** /ImageFolderMembers/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**image_folder_members_patch**](ImageFolderMemberApi.md#image_folder_members_patch) | **PATCH** /ImageFolderMembers | Patch an existing model instance or insert a new one into the data source.
[**image_folder_members_post**](ImageFolderMemberApi.md#image_folder_members_post) | **POST** /ImageFolderMembers | Create a new instance of the model and persist it into the data source.
[**image_folder_members_put**](ImageFolderMemberApi.md#image_folder_members_put) | **PUT** /ImageFolderMembers | Replace an existing model instance or insert a new one into the data source.
[**image_folder_members_replace_or_create_post**](ImageFolderMemberApi.md#image_folder_members_replace_or_create_post) | **POST** /ImageFolderMembers/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**image_folder_members_update_post**](ImageFolderMemberApi.md#image_folder_members_update_post) | **POST** /ImageFolderMembers/update | Update instances of the model matched by {{where}} from the data source.
[**image_folder_members_upsert_with_where_post**](ImageFolderMemberApi.md#image_folder_members_upsert_with_where_post) | **POST** /ImageFolderMembers/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **image_folder_members_change_stream_get**
> file image_folder_members_change_stream_get(options=options)

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
api_instance = TweakApi.ImageFolderMemberApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.image_folder_members_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_change_stream_get: %s\n" % e)
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

# **image_folder_members_change_stream_post**
> file image_folder_members_change_stream_post(options=options)

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
api_instance = TweakApi.ImageFolderMemberApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.image_folder_members_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_change_stream_post: %s\n" % e)
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

# **image_folder_members_count_get**
> InlineResponse200 image_folder_members_count_get(where=where)

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
api_instance = TweakApi.ImageFolderMemberApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.image_folder_members_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_count_get: %s\n" % e)
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

# **image_folder_members_find_one_get**
> ImageFolderMember image_folder_members_find_one_get(filter=filter)

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
api_instance = TweakApi.ImageFolderMemberApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.image_folder_members_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_get**
> list[ImageFolderMember] image_folder_members_get(filter=filter)

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
api_instance = TweakApi.ImageFolderMemberApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.image_folder_members_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ImageFolderMember]**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_id_delete**
> object image_folder_members_id_delete(id)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.image_folder_members_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_delete: %s\n" % e)
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

# **image_folder_members_id_exists_get**
> InlineResponse2002 image_folder_members_id_exists_get(id)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.image_folder_members_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_exists_get: %s\n" % e)
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

# **image_folder_members_id_folder_get**
> ImageFolder image_folder_members_id_folder_get(id, refresh=refresh)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | ImageFolderMember id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation folder.
    api_response = api_instance.image_folder_members_id_folder_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolderMember id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_id_get**
> ImageFolderMember image_folder_members_id_get(id, filter=filter)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.image_folder_members_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_id_head**
> InlineResponse2002 image_folder_members_id_head(id)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.image_folder_members_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_head: %s\n" % e)
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

# **image_folder_members_id_member_get**
> TeamMember image_folder_members_id_member_get(id, refresh=refresh)

Fetches belongsTo relation member.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | ImageFolderMember id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation member.
    api_response = api_instance.image_folder_members_id_member_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolderMember id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_id_patch**
> ImageFolderMember image_folder_members_id_patch(id, data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | ImageFolderMember id
data = TweakApi.ImageFolderMember() # ImageFolderMember | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.image_folder_members_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImageFolderMember id | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_id_put**
> ImageFolderMember image_folder_members_id_put(id, data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | Model id
data = TweakApi.ImageFolderMember() # ImageFolderMember | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.image_folder_members_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| Model instance data | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_id_replace_post**
> ImageFolderMember image_folder_members_id_replace_post(id, data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
id = 'id_example' # str | Model id
data = TweakApi.ImageFolderMember() # ImageFolderMember | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.image_folder_members_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| Model instance data | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_patch**
> ImageFolderMember image_folder_members_patch(data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
data = TweakApi.ImageFolderMember() # ImageFolderMember | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.image_folder_members_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| Model instance data | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_post**
> ImageFolderMember image_folder_members_post(data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
data = TweakApi.ImageFolderMember() # ImageFolderMember | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.image_folder_members_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| Model instance data | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_put**
> ImageFolderMember image_folder_members_put(data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
data = TweakApi.ImageFolderMember() # ImageFolderMember | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.image_folder_members_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| Model instance data | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_replace_or_create_post**
> ImageFolderMember image_folder_members_replace_or_create_post(data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
data = TweakApi.ImageFolderMember() # ImageFolderMember | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.image_folder_members_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| Model instance data | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_update_post**
> InlineResponse2001 image_folder_members_update_post(where=where, data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ImageFolderMember() # ImageFolderMember | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.image_folder_members_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_folder_members_upsert_with_where_post**
> ImageFolderMember image_folder_members_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.ImageFolderMemberApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ImageFolderMember() # ImageFolderMember | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.image_folder_members_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFolderMemberApi->image_folder_members_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

