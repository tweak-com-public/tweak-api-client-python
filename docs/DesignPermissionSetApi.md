# TweakApi.DesignPermissionSetApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**design_permission_sets_change_stream_get**](DesignPermissionSetApi.md#design_permission_sets_change_stream_get) | **GET** /DesignPermissionSets/change-stream | Create a change stream.
[**design_permission_sets_change_stream_post**](DesignPermissionSetApi.md#design_permission_sets_change_stream_post) | **POST** /DesignPermissionSets/change-stream | Create a change stream.
[**design_permission_sets_count_get**](DesignPermissionSetApi.md#design_permission_sets_count_get) | **GET** /DesignPermissionSets/count | Count instances of the model matched by where from the data source.
[**design_permission_sets_find_one_get**](DesignPermissionSetApi.md#design_permission_sets_find_one_get) | **GET** /DesignPermissionSets/findOne | Find first instance of the model matched by filter from the data source.
[**design_permission_sets_get**](DesignPermissionSetApi.md#design_permission_sets_get) | **GET** /DesignPermissionSets | Find all instances of the model matched by filter from the data source.
[**design_permission_sets_id_delete**](DesignPermissionSetApi.md#design_permission_sets_id_delete) | **DELETE** /DesignPermissionSets/{id} | Delete a model instance by {{id}} from the data source.
[**design_permission_sets_id_design_get**](DesignPermissionSetApi.md#design_permission_sets_id_design_get) | **GET** /DesignPermissionSets/{id}/design | Fetches belongsTo relation design.
[**design_permission_sets_id_exists_get**](DesignPermissionSetApi.md#design_permission_sets_id_exists_get) | **GET** /DesignPermissionSets/{id}/exists | Check whether a model instance exists in the data source.
[**design_permission_sets_id_get**](DesignPermissionSetApi.md#design_permission_sets_id_get) | **GET** /DesignPermissionSets/{id} | Find a model instance by {{id}} from the data source.
[**design_permission_sets_id_head**](DesignPermissionSetApi.md#design_permission_sets_id_head) | **HEAD** /DesignPermissionSets/{id} | Check whether a model instance exists in the data source.
[**design_permission_sets_id_patch**](DesignPermissionSetApi.md#design_permission_sets_id_patch) | **PATCH** /DesignPermissionSets/{id} | Patch attributes for a model instance and persist it into the data source.
[**design_permission_sets_id_put**](DesignPermissionSetApi.md#design_permission_sets_id_put) | **PUT** /DesignPermissionSets/{id} | Replace attributes for a model instance and persist it into the data source.
[**design_permission_sets_id_replace_post**](DesignPermissionSetApi.md#design_permission_sets_id_replace_post) | **POST** /DesignPermissionSets/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**design_permission_sets_patch**](DesignPermissionSetApi.md#design_permission_sets_patch) | **PATCH** /DesignPermissionSets | Patch an existing model instance or insert a new one into the data source.
[**design_permission_sets_post**](DesignPermissionSetApi.md#design_permission_sets_post) | **POST** /DesignPermissionSets | Create a new instance of the model and persist it into the data source.
[**design_permission_sets_put**](DesignPermissionSetApi.md#design_permission_sets_put) | **PUT** /DesignPermissionSets | Replace an existing model instance or insert a new one into the data source.
[**design_permission_sets_replace_or_create_post**](DesignPermissionSetApi.md#design_permission_sets_replace_or_create_post) | **POST** /DesignPermissionSets/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**design_permission_sets_update_post**](DesignPermissionSetApi.md#design_permission_sets_update_post) | **POST** /DesignPermissionSets/update | Update instances of the model matched by {{where}} from the data source.
[**design_permission_sets_upsert_with_where_post**](DesignPermissionSetApi.md#design_permission_sets_upsert_with_where_post) | **POST** /DesignPermissionSets/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **design_permission_sets_change_stream_get**
> file design_permission_sets_change_stream_get(options=options)

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
api_instance = TweakApi.DesignPermissionSetApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.design_permission_sets_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_change_stream_get: %s\n" % e)
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

# **design_permission_sets_change_stream_post**
> file design_permission_sets_change_stream_post(options=options)

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
api_instance = TweakApi.DesignPermissionSetApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.design_permission_sets_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_change_stream_post: %s\n" % e)
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

# **design_permission_sets_count_get**
> InlineResponse2001 design_permission_sets_count_get(where=where)

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
api_instance = TweakApi.DesignPermissionSetApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.design_permission_sets_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_count_get: %s\n" % e)
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

# **design_permission_sets_find_one_get**
> DesignPermissionSet design_permission_sets_find_one_get(filter=filter)

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
api_instance = TweakApi.DesignPermissionSetApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.design_permission_sets_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_get**
> list[DesignPermissionSet] design_permission_sets_get(filter=filter)

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
api_instance = TweakApi.DesignPermissionSetApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.design_permission_sets_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[DesignPermissionSet]**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_id_delete**
> object design_permission_sets_id_delete(id)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.design_permission_sets_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_delete: %s\n" % e)
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

# **design_permission_sets_id_design_get**
> Design design_permission_sets_id_design_get(id, refresh=refresh)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | DesignPermissionSet id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation design.
    api_response = api_instance.design_permission_sets_id_design_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_design_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignPermissionSet id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_id_exists_get**
> InlineResponse2002 design_permission_sets_id_exists_get(id)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.design_permission_sets_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_exists_get: %s\n" % e)
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

# **design_permission_sets_id_get**
> DesignPermissionSet design_permission_sets_id_get(id, filter=filter)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.design_permission_sets_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_id_head**
> InlineResponse2002 design_permission_sets_id_head(id)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.design_permission_sets_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_head: %s\n" % e)
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

# **design_permission_sets_id_patch**
> DesignPermissionSet design_permission_sets_id_patch(id, data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | DesignPermissionSet id
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_permission_sets_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DesignPermissionSet id | 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_id_put**
> DesignPermissionSet design_permission_sets_id_put(id, data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | Model id
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_permission_sets_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| Model instance data | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_id_replace_post**
> DesignPermissionSet design_permission_sets_id_replace_post(id, data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
id = 'id_example' # str | Model id
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.design_permission_sets_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| Model instance data | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_patch**
> DesignPermissionSet design_permission_sets_patch(data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_permission_sets_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| Model instance data | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_post**
> DesignPermissionSet design_permission_sets_post(data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.design_permission_sets_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| Model instance data | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_put**
> DesignPermissionSet design_permission_sets_put(data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_permission_sets_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| Model instance data | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_replace_or_create_post**
> DesignPermissionSet design_permission_sets_replace_or_create_post(data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.design_permission_sets_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| Model instance data | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_update_post**
> InlineResponse2003 design_permission_sets_update_post(where=where, data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.design_permission_sets_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **design_permission_sets_upsert_with_where_post**
> DesignPermissionSet design_permission_sets_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.DesignPermissionSetApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DesignPermissionSet() # DesignPermissionSet | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.design_permission_sets_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignPermissionSetApi->design_permission_sets_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

