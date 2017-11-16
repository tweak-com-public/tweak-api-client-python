# TweakApi.TeamBuilderConfigProductTypeApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_builder_config_product_types_change_stream_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_change_stream_get) | **GET** /TeamBuilderConfigProductTypes/change-stream | Create a change stream.
[**team_builder_config_product_types_change_stream_post**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_change_stream_post) | **POST** /TeamBuilderConfigProductTypes/change-stream | Create a change stream.
[**team_builder_config_product_types_count_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_count_get) | **GET** /TeamBuilderConfigProductTypes/count | Count instances of the model matched by where from the data source.
[**team_builder_config_product_types_find_one_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_find_one_get) | **GET** /TeamBuilderConfigProductTypes/findOne | Find first instance of the model matched by filter from the data source.
[**team_builder_config_product_types_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_get) | **GET** /TeamBuilderConfigProductTypes | Find all instances of the model matched by filter from the data source.
[**team_builder_config_product_types_id_builder_config_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_builder_config_get) | **GET** /TeamBuilderConfigProductTypes/{id}/builderConfig | Fetches belongsTo relation builderConfig.
[**team_builder_config_product_types_id_delete**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_delete) | **DELETE** /TeamBuilderConfigProductTypes/{id} | Delete a model instance by {{id}} from the data source.
[**team_builder_config_product_types_id_exists_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_exists_get) | **GET** /TeamBuilderConfigProductTypes/{id}/exists | Check whether a model instance exists in the data source.
[**team_builder_config_product_types_id_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_get) | **GET** /TeamBuilderConfigProductTypes/{id} | Find a model instance by {{id}} from the data source.
[**team_builder_config_product_types_id_head**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_head) | **HEAD** /TeamBuilderConfigProductTypes/{id} | Check whether a model instance exists in the data source.
[**team_builder_config_product_types_id_patch**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_patch) | **PATCH** /TeamBuilderConfigProductTypes/{id} | Patch attributes for a model instance and persist it into the data source.
[**team_builder_config_product_types_id_product_type_get**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_product_type_get) | **GET** /TeamBuilderConfigProductTypes/{id}/productType | Fetches belongsTo relation productType.
[**team_builder_config_product_types_id_put**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_put) | **PUT** /TeamBuilderConfigProductTypes/{id} | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_types_id_replace_post**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_id_replace_post) | **POST** /TeamBuilderConfigProductTypes/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_types_patch**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_patch) | **PATCH** /TeamBuilderConfigProductTypes | Patch an existing model instance or insert a new one into the data source.
[**team_builder_config_product_types_post**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_post) | **POST** /TeamBuilderConfigProductTypes | Create a new instance of the model and persist it into the data source.
[**team_builder_config_product_types_put**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_put) | **PUT** /TeamBuilderConfigProductTypes | Replace an existing model instance or insert a new one into the data source.
[**team_builder_config_product_types_replace_or_create_post**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_replace_or_create_post) | **POST** /TeamBuilderConfigProductTypes/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**team_builder_config_product_types_update_post**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_update_post) | **POST** /TeamBuilderConfigProductTypes/update | Update instances of the model matched by {{where}} from the data source.
[**team_builder_config_product_types_upsert_with_where_post**](TeamBuilderConfigProductTypeApi.md#team_builder_config_product_types_upsert_with_where_post) | **POST** /TeamBuilderConfigProductTypes/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **team_builder_config_product_types_change_stream_get**
> file team_builder_config_product_types_change_stream_get(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_types_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_change_stream_get: %s\n" % e)
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

# **team_builder_config_product_types_change_stream_post**
> file team_builder_config_product_types_change_stream_post(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_types_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_change_stream_post: %s\n" % e)
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

# **team_builder_config_product_types_count_get**
> InlineResponse200 team_builder_config_product_types_count_get(where=where)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.team_builder_config_product_types_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_count_get: %s\n" % e)
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

# **team_builder_config_product_types_find_one_get**
> TeamBuilderConfigProductType team_builder_config_product_types_find_one_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_types_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_get**
> list[TeamBuilderConfigProductType] team_builder_config_product_types_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_types_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamBuilderConfigProductType]**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_id_builder_config_get**
> TeamBuilderConfig team_builder_config_product_types_id_builder_config_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | TeamBuilderConfigProductType id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation builderConfig.
    api_response = api_instance.team_builder_config_product_types_id_builder_config_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_builder_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductType id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_id_delete**
> object team_builder_config_product_types_id_delete(id)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_types_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_delete: %s\n" % e)
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

# **team_builder_config_product_types_id_exists_get**
> InlineResponse2001 team_builder_config_product_types_id_exists_get(id)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_types_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_exists_get: %s\n" % e)
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

# **team_builder_config_product_types_id_get**
> TeamBuilderConfigProductType team_builder_config_product_types_id_get(id, filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_types_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_id_head**
> InlineResponse2001 team_builder_config_product_types_id_head(id)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_types_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_head: %s\n" % e)
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

# **team_builder_config_product_types_id_patch**
> TeamBuilderConfigProductType team_builder_config_product_types_id_patch(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | TeamBuilderConfigProductType id
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_types_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductType id | 
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_id_product_type_get**
> ProductType team_builder_config_product_types_id_product_type_get(id, refresh=refresh)

Fetches belongsTo relation productType.

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | TeamBuilderConfigProductType id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation productType.
    api_response = api_instance.team_builder_config_product_types_id_product_type_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_product_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductType id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_id_put**
> TeamBuilderConfigProductType team_builder_config_product_types_id_put(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_types_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_id_replace_post**
> TeamBuilderConfigProductType team_builder_config_product_types_id_replace_post(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_types_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_patch**
> TeamBuilderConfigProductType team_builder_config_product_types_patch(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_config_product_types_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_post**
> TeamBuilderConfigProductType team_builder_config_product_types_post(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.team_builder_config_product_types_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_put**
> TeamBuilderConfigProductType team_builder_config_product_types_put(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_config_product_types_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_replace_or_create_post**
> TeamBuilderConfigProductType team_builder_config_product_types_replace_or_create_post(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_config_product_types_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_update_post**
> InlineResponse2002 team_builder_config_product_types_update_post(where=where, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.team_builder_config_product_types_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_types_upsert_with_where_post**
> TeamBuilderConfigProductType team_builder_config_product_types_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductTypeApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.team_builder_config_product_types_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductTypeApi->team_builder_config_product_types_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

