# TweakApi.PortalImageFolderApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal_image_folders_change_stream_get**](PortalImageFolderApi.md#portal_image_folders_change_stream_get) | **GET** /PortalImageFolders/change-stream | Create a change stream.
[**portal_image_folders_change_stream_post**](PortalImageFolderApi.md#portal_image_folders_change_stream_post) | **POST** /PortalImageFolders/change-stream | Create a change stream.
[**portal_image_folders_count_get**](PortalImageFolderApi.md#portal_image_folders_count_get) | **GET** /PortalImageFolders/count | Count instances of the model matched by where from the data source.
[**portal_image_folders_find_one_get**](PortalImageFolderApi.md#portal_image_folders_find_one_get) | **GET** /PortalImageFolders/findOne | Find first instance of the model matched by filter from the data source.
[**portal_image_folders_get**](PortalImageFolderApi.md#portal_image_folders_get) | **GET** /PortalImageFolders | Find all instances of the model matched by filter from the data source.
[**portal_image_folders_id_delete**](PortalImageFolderApi.md#portal_image_folders_id_delete) | **DELETE** /PortalImageFolders/{id} | Delete a model instance by {{id}} from the data source.
[**portal_image_folders_id_exists_get**](PortalImageFolderApi.md#portal_image_folders_id_exists_get) | **GET** /PortalImageFolders/{id}/exists | Check whether a model instance exists in the data source.
[**portal_image_folders_id_folder_get**](PortalImageFolderApi.md#portal_image_folders_id_folder_get) | **GET** /PortalImageFolders/{id}/folder | Fetches belongsTo relation folder.
[**portal_image_folders_id_get**](PortalImageFolderApi.md#portal_image_folders_id_get) | **GET** /PortalImageFolders/{id} | Find a model instance by {{id}} from the data source.
[**portal_image_folders_id_head**](PortalImageFolderApi.md#portal_image_folders_id_head) | **HEAD** /PortalImageFolders/{id} | Check whether a model instance exists in the data source.
[**portal_image_folders_id_patch**](PortalImageFolderApi.md#portal_image_folders_id_patch) | **PATCH** /PortalImageFolders/{id} | Patch attributes for a model instance and persist it into the data source.
[**portal_image_folders_id_portal_get**](PortalImageFolderApi.md#portal_image_folders_id_portal_get) | **GET** /PortalImageFolders/{id}/portal | Fetches belongsTo relation portal.
[**portal_image_folders_id_put**](PortalImageFolderApi.md#portal_image_folders_id_put) | **PUT** /PortalImageFolders/{id} | Replace attributes for a model instance and persist it into the data source.
[**portal_image_folders_id_replace_post**](PortalImageFolderApi.md#portal_image_folders_id_replace_post) | **POST** /PortalImageFolders/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**portal_image_folders_patch**](PortalImageFolderApi.md#portal_image_folders_patch) | **PATCH** /PortalImageFolders | Patch an existing model instance or insert a new one into the data source.
[**portal_image_folders_post**](PortalImageFolderApi.md#portal_image_folders_post) | **POST** /PortalImageFolders | Create a new instance of the model and persist it into the data source.
[**portal_image_folders_put**](PortalImageFolderApi.md#portal_image_folders_put) | **PUT** /PortalImageFolders | Replace an existing model instance or insert a new one into the data source.
[**portal_image_folders_replace_or_create_post**](PortalImageFolderApi.md#portal_image_folders_replace_or_create_post) | **POST** /PortalImageFolders/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**portal_image_folders_update_post**](PortalImageFolderApi.md#portal_image_folders_update_post) | **POST** /PortalImageFolders/update | Update instances of the model matched by {{where}} from the data source.
[**portal_image_folders_upsert_with_where_post**](PortalImageFolderApi.md#portal_image_folders_upsert_with_where_post) | **POST** /PortalImageFolders/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **portal_image_folders_change_stream_get**
> file portal_image_folders_change_stream_get(options=options)

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
api_instance = TweakApi.PortalImageFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portal_image_folders_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_change_stream_get: %s\n" % e)
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

# **portal_image_folders_change_stream_post**
> file portal_image_folders_change_stream_post(options=options)

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
api_instance = TweakApi.PortalImageFolderApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portal_image_folders_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_change_stream_post: %s\n" % e)
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

# **portal_image_folders_count_get**
> InlineResponse200 portal_image_folders_count_get(where=where)

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
api_instance = TweakApi.PortalImageFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.portal_image_folders_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_count_get: %s\n" % e)
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

# **portal_image_folders_find_one_get**
> PortalImageFolder portal_image_folders_find_one_get(filter=filter)

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
api_instance = TweakApi.PortalImageFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.portal_image_folders_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_get**
> list[PortalImageFolder] portal_image_folders_get(filter=filter)

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
api_instance = TweakApi.PortalImageFolderApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.portal_image_folders_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[PortalImageFolder]**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_id_delete**
> object portal_image_folders_id_delete(id)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.portal_image_folders_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_delete: %s\n" % e)
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

# **portal_image_folders_id_exists_get**
> InlineResponse2001 portal_image_folders_id_exists_get(id)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portal_image_folders_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_exists_get: %s\n" % e)
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

# **portal_image_folders_id_folder_get**
> ImageFolder portal_image_folders_id_folder_get(id, refresh=refresh)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | PortalImageFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation folder.
    api_response = api_instance.portal_image_folders_id_folder_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalImageFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_id_get**
> PortalImageFolder portal_image_folders_id_get(id, filter=filter)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.portal_image_folders_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_id_head**
> InlineResponse2001 portal_image_folders_id_head(id)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portal_image_folders_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_head: %s\n" % e)
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

# **portal_image_folders_id_patch**
> PortalImageFolder portal_image_folders_id_patch(id, data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | PortalImageFolder id
data = TweakApi.PortalImageFolder() # PortalImageFolder | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_image_folders_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalImageFolder id | 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_id_portal_get**
> Portal portal_image_folders_id_portal_get(id, refresh=refresh)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | PortalImageFolder id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation portal.
    api_response = api_instance.portal_image_folders_id_portal_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_portal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalImageFolder id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_id_put**
> PortalImageFolder portal_image_folders_id_put(id, data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.PortalImageFolder() # PortalImageFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_image_folders_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| Model instance data | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_id_replace_post**
> PortalImageFolder portal_image_folders_id_replace_post(id, data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
id = 'id_example' # str | Model id
data = TweakApi.PortalImageFolder() # PortalImageFolder | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_image_folders_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| Model instance data | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_patch**
> PortalImageFolder portal_image_folders_patch(data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
data = TweakApi.PortalImageFolder() # PortalImageFolder | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.portal_image_folders_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| Model instance data | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_post**
> PortalImageFolder portal_image_folders_post(data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
data = TweakApi.PortalImageFolder() # PortalImageFolder | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.portal_image_folders_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| Model instance data | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_put**
> PortalImageFolder portal_image_folders_put(data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
data = TweakApi.PortalImageFolder() # PortalImageFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.portal_image_folders_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| Model instance data | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_replace_or_create_post**
> PortalImageFolder portal_image_folders_replace_or_create_post(data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
data = TweakApi.PortalImageFolder() # PortalImageFolder | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.portal_image_folders_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| Model instance data | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_update_post**
> InlineResponse2002 portal_image_folders_update_post(where=where, data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.PortalImageFolder() # PortalImageFolder | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.portal_image_folders_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_image_folders_upsert_with_where_post**
> PortalImageFolder portal_image_folders_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.PortalImageFolderApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.PortalImageFolder() # PortalImageFolder | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.portal_image_folders_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalImageFolderApi->portal_image_folders_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)| An object of model property name/value pairs | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

