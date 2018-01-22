# TweakApi.TeamBuilderConfigProductSizeApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_builder_config_product_sizes_change_stream_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_change_stream_get) | **GET** /TeamBuilderConfigProductSizes/change-stream | Create a change stream.
[**team_builder_config_product_sizes_change_stream_post**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_change_stream_post) | **POST** /TeamBuilderConfigProductSizes/change-stream | Create a change stream.
[**team_builder_config_product_sizes_count_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_count_get) | **GET** /TeamBuilderConfigProductSizes/count | Count instances of the model matched by where from the data source.
[**team_builder_config_product_sizes_find_one_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_find_one_get) | **GET** /TeamBuilderConfigProductSizes/findOne | Find first instance of the model matched by filter from the data source.
[**team_builder_config_product_sizes_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_get) | **GET** /TeamBuilderConfigProductSizes | Find all instances of the model matched by filter from the data source.
[**team_builder_config_product_sizes_id_builder_config_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_builder_config_get) | **GET** /TeamBuilderConfigProductSizes/{id}/builderConfig | Fetches belongsTo relation builderConfig.
[**team_builder_config_product_sizes_id_delete**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_delete) | **DELETE** /TeamBuilderConfigProductSizes/{id} | Delete a model instance by {{id}} from the data source.
[**team_builder_config_product_sizes_id_exists_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_exists_get) | **GET** /TeamBuilderConfigProductSizes/{id}/exists | Check whether a model instance exists in the data source.
[**team_builder_config_product_sizes_id_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_get) | **GET** /TeamBuilderConfigProductSizes/{id} | Find a model instance by {{id}} from the data source.
[**team_builder_config_product_sizes_id_head**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_head) | **HEAD** /TeamBuilderConfigProductSizes/{id} | Check whether a model instance exists in the data source.
[**team_builder_config_product_sizes_id_patch**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_patch) | **PATCH** /TeamBuilderConfigProductSizes/{id} | Patch attributes for a model instance and persist it into the data source.
[**team_builder_config_product_sizes_id_product_size_get**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_product_size_get) | **GET** /TeamBuilderConfigProductSizes/{id}/productSize | Fetches belongsTo relation productSize.
[**team_builder_config_product_sizes_id_put**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_put) | **PUT** /TeamBuilderConfigProductSizes/{id} | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_sizes_id_replace_post**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_id_replace_post) | **POST** /TeamBuilderConfigProductSizes/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_sizes_patch**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_patch) | **PATCH** /TeamBuilderConfigProductSizes | Patch an existing model instance or insert a new one into the data source.
[**team_builder_config_product_sizes_post**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_post) | **POST** /TeamBuilderConfigProductSizes | Create a new instance of the model and persist it into the data source.
[**team_builder_config_product_sizes_put**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_put) | **PUT** /TeamBuilderConfigProductSizes | Replace an existing model instance or insert a new one into the data source.
[**team_builder_config_product_sizes_replace_or_create_post**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_replace_or_create_post) | **POST** /TeamBuilderConfigProductSizes/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**team_builder_config_product_sizes_update_post**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_update_post) | **POST** /TeamBuilderConfigProductSizes/update | Update instances of the model matched by {{where}} from the data source.
[**team_builder_config_product_sizes_upsert_with_where_post**](TeamBuilderConfigProductSizeApi.md#team_builder_config_product_sizes_upsert_with_where_post) | **POST** /TeamBuilderConfigProductSizes/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **team_builder_config_product_sizes_change_stream_get**
> file team_builder_config_product_sizes_change_stream_get(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_sizes_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_change_stream_get: %s\n" % e)
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

# **team_builder_config_product_sizes_change_stream_post**
> file team_builder_config_product_sizes_change_stream_post(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_sizes_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_change_stream_post: %s\n" % e)
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

# **team_builder_config_product_sizes_count_get**
> InlineResponse2001 team_builder_config_product_sizes_count_get(where=where)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.team_builder_config_product_sizes_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_count_get: %s\n" % e)
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

# **team_builder_config_product_sizes_find_one_get**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_find_one_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_sizes_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_get**
> list[TeamBuilderConfigProductSize] team_builder_config_product_sizes_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_sizes_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamBuilderConfigProductSize]**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_id_builder_config_get**
> TeamBuilderConfig team_builder_config_product_sizes_id_builder_config_get(id, refresh=refresh)

Fetches belongsTo relation builderConfig.

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | TeamBuilderConfigProductSize id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation builderConfig.
    api_response = api_instance.team_builder_config_product_sizes_id_builder_config_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_builder_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductSize id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_id_delete**
> object team_builder_config_product_sizes_id_delete(id)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_sizes_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_delete: %s\n" % e)
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

# **team_builder_config_product_sizes_id_exists_get**
> InlineResponse2002 team_builder_config_product_sizes_id_exists_get(id)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_sizes_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_exists_get: %s\n" % e)
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

# **team_builder_config_product_sizes_id_get**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_id_get(id, filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_sizes_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_id_head**
> InlineResponse2002 team_builder_config_product_sizes_id_head(id)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_sizes_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_head: %s\n" % e)
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

# **team_builder_config_product_sizes_id_patch**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_id_patch(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | TeamBuilderConfigProductSize id
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_sizes_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductSize id | 
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_id_product_size_get**
> ProductSize team_builder_config_product_sizes_id_product_size_get(id, refresh=refresh)

Fetches belongsTo relation productSize.

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | TeamBuilderConfigProductSize id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation productSize.
    api_response = api_instance.team_builder_config_product_sizes_id_product_size_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_product_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductSize id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_id_put**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_id_put(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_sizes_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_id_replace_post**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_id_replace_post(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_sizes_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_patch**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_patch(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_config_product_sizes_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_post**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_post(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.team_builder_config_product_sizes_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_put**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_put(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_config_product_sizes_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_replace_or_create_post**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_replace_or_create_post(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_config_product_sizes_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_update_post**
> InlineResponse2003 team_builder_config_product_sizes_update_post(where=where, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.team_builder_config_product_sizes_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_sizes_upsert_with_where_post**
> TeamBuilderConfigProductSize team_builder_config_product_sizes_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.team_builder_config_product_sizes_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeApi->team_builder_config_product_sizes_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

