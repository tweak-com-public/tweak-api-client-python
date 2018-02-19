# TweakApi.ProductTypeApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_types_change_stream_get**](ProductTypeApi.md#product_types_change_stream_get) | **GET** /ProductTypes/change-stream | Create a change stream.
[**product_types_change_stream_post**](ProductTypeApi.md#product_types_change_stream_post) | **POST** /ProductTypes/change-stream | Create a change stream.
[**product_types_count_get**](ProductTypeApi.md#product_types_count_get) | **GET** /ProductTypes/count | Count instances of the model matched by where from the data source.
[**product_types_find_one_get**](ProductTypeApi.md#product_types_find_one_get) | **GET** /ProductTypes/findOne | Find first instance of the model matched by filter from the data source.
[**product_types_get**](ProductTypeApi.md#product_types_get) | **GET** /ProductTypes | Find all instances of the model matched by filter from the data source.
[**product_types_id_delete**](ProductTypeApi.md#product_types_id_delete) | **DELETE** /ProductTypes/{id} | Delete a model instance by {{id}} from the data source.
[**product_types_id_exists_get**](ProductTypeApi.md#product_types_id_exists_get) | **GET** /ProductTypes/{id}/exists | Check whether a model instance exists in the data source.
[**product_types_id_get**](ProductTypeApi.md#product_types_id_get) | **GET** /ProductTypes/{id} | Find a model instance by {{id}} from the data source.
[**product_types_id_group_get**](ProductTypeApi.md#product_types_id_group_get) | **GET** /ProductTypes/{id}/group | Fetches belongsTo relation group.
[**product_types_id_head**](ProductTypeApi.md#product_types_id_head) | **HEAD** /ProductTypes/{id} | Check whether a model instance exists in the data source.
[**product_types_id_patch**](ProductTypeApi.md#product_types_id_patch) | **PATCH** /ProductTypes/{id} | Patch attributes for a model instance and persist it into the data source.
[**product_types_id_put**](ProductTypeApi.md#product_types_id_put) | **PUT** /ProductTypes/{id} | Replace attributes for a model instance and persist it into the data source.
[**product_types_id_replace_post**](ProductTypeApi.md#product_types_id_replace_post) | **POST** /ProductTypes/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**product_types_id_sizes_count_get**](ProductTypeApi.md#product_types_id_sizes_count_get) | **GET** /ProductTypes/{id}/sizes/count | Counts sizes of ProductType.
[**product_types_id_sizes_fk_delete**](ProductTypeApi.md#product_types_id_sizes_fk_delete) | **DELETE** /ProductTypes/{id}/sizes/{fk} | Delete a related item by id for sizes.
[**product_types_id_sizes_fk_get**](ProductTypeApi.md#product_types_id_sizes_fk_get) | **GET** /ProductTypes/{id}/sizes/{fk} | Find a related item by id for sizes.
[**product_types_id_sizes_fk_put**](ProductTypeApi.md#product_types_id_sizes_fk_put) | **PUT** /ProductTypes/{id}/sizes/{fk} | Update a related item by id for sizes.
[**product_types_id_sizes_get**](ProductTypeApi.md#product_types_id_sizes_get) | **GET** /ProductTypes/{id}/sizes | Queries sizes of ProductType.
[**product_types_id_sizes_post**](ProductTypeApi.md#product_types_id_sizes_post) | **POST** /ProductTypes/{id}/sizes | Creates a new instance in sizes of this model.
[**product_types_post**](ProductTypeApi.md#product_types_post) | **POST** /ProductTypes | Create a new instance of the model and persist it into the data source.


# **product_types_change_stream_get**
> file product_types_change_stream_get(options=options)

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
api_instance = TweakApi.ProductTypeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_types_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_change_stream_get: %s\n" % e)
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

# **product_types_change_stream_post**
> file product_types_change_stream_post(options=options)

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
api_instance = TweakApi.ProductTypeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_types_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_change_stream_post: %s\n" % e)
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

# **product_types_count_get**
> InlineResponse2001 product_types_count_get(where=where)

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
api_instance = TweakApi.ProductTypeApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.product_types_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_count_get: %s\n" % e)
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

# **product_types_find_one_get**
> ProductType product_types_find_one_get(filter=filter)

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
api_instance = TweakApi.ProductTypeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.product_types_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_get**
> list[ProductType] product_types_get(filter=filter)

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
api_instance = TweakApi.ProductTypeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.product_types_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ProductType]**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_delete**
> object product_types_id_delete(id)

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
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.product_types_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_delete: %s\n" % e)
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

# **product_types_id_exists_get**
> InlineResponse2002 product_types_id_exists_get(id)

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
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_types_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_exists_get: %s\n" % e)
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

# **product_types_id_get**
> ProductType product_types_id_get(id, filter=filter)

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
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.product_types_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_group_get**
> ProductGroup product_types_id_group_get(id, refresh=refresh)

Fetches belongsTo relation group.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation group.
    api_response = api_instance.product_types_id_group_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_head**
> InlineResponse2002 product_types_id_head(id)

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
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_types_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_head: %s\n" % e)
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

# **product_types_id_patch**
> ProductType product_types_id_patch(id, data=data)

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
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
data = TweakApi.ProductType() # ProductType | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_types_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **data** | [**ProductType**](ProductType.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_put**
> ProductType product_types_id_put(id, data=data)

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
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductType() # ProductType | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_types_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductType**](ProductType.md)| Model instance data | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_replace_post**
> ProductType product_types_id_replace_post(id, data=data)

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
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductType() # ProductType | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_types_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductType**](ProductType.md)| Model instance data | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_sizes_count_get**
> InlineResponse2001 product_types_id_sizes_count_get(id, where=where)

Counts sizes of ProductType.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts sizes of ProductType.
    api_response = api_instance.product_types_id_sizes_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_sizes_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_sizes_fk_delete**
> product_types_id_sizes_fk_delete(id, fk)

Delete a related item by id for sizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
fk = 'fk_example' # str | Foreign key for sizes

try: 
    # Delete a related item by id for sizes.
    api_instance.product_types_id_sizes_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_sizes_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **fk** | **str**| Foreign key for sizes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_sizes_fk_get**
> ProductSize product_types_id_sizes_fk_get(id, fk)

Find a related item by id for sizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
fk = 'fk_example' # str | Foreign key for sizes

try: 
    # Find a related item by id for sizes.
    api_response = api_instance.product_types_id_sizes_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_sizes_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **fk** | **str**| Foreign key for sizes | 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_sizes_fk_put**
> ProductSize product_types_id_sizes_fk_put(id, fk, data=data)

Update a related item by id for sizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
fk = 'fk_example' # str | Foreign key for sizes
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Update a related item by id for sizes.
    api_response = api_instance.product_types_id_sizes_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_sizes_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **fk** | **str**| Foreign key for sizes | 
 **data** | [**ProductSize**](ProductSize.md)|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_sizes_get**
> list[ProductSize] product_types_id_sizes_get(id, filter=filter)

Queries sizes of ProductType.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries sizes of ProductType.
    api_response = api_instance.product_types_id_sizes_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_sizes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSize]**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_id_sizes_post**
> ProductSize product_types_id_sizes_post(id, data=data)

Creates a new instance in sizes of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.ProductTypeApi()
id = 'id_example' # str | ProductType id
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Creates a new instance in sizes of this model.
    api_response = api_instance.product_types_id_sizes_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_id_sizes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductType id | 
 **data** | [**ProductSize**](ProductSize.md)|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types_post**
> ProductType product_types_post(data=data)

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
api_instance = TweakApi.ProductTypeApi()
data = TweakApi.ProductType() # ProductType | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.product_types_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypeApi->product_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductType**](ProductType.md)| Model instance data | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

