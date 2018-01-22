# TweakApi.DataSourceApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_sources_id_keys_count_get**](DataSourceApi.md#data_sources_id_keys_count_get) | **GET** /DataSources/{id}/keys/count | Counts keys of DataSource.
[**data_sources_id_keys_delete**](DataSourceApi.md#data_sources_id_keys_delete) | **DELETE** /DataSources/{id}/keys | Deletes all keys of this model.
[**data_sources_id_keys_fk_delete**](DataSourceApi.md#data_sources_id_keys_fk_delete) | **DELETE** /DataSources/{id}/keys/{fk} | Delete a related item by id for keys.
[**data_sources_id_keys_fk_get**](DataSourceApi.md#data_sources_id_keys_fk_get) | **GET** /DataSources/{id}/keys/{fk} | Find a related item by id for keys.
[**data_sources_id_keys_fk_put**](DataSourceApi.md#data_sources_id_keys_fk_put) | **PUT** /DataSources/{id}/keys/{fk} | Update a related item by id for keys.
[**data_sources_id_keys_get**](DataSourceApi.md#data_sources_id_keys_get) | **GET** /DataSources/{id}/keys | Queries keys of DataSource.
[**data_sources_id_keys_post**](DataSourceApi.md#data_sources_id_keys_post) | **POST** /DataSources/{id}/keys | Creates a new instance in keys of this model.


# **data_sources_id_keys_count_get**
> InlineResponse2001 data_sources_id_keys_count_get(id, where=where)

Counts keys of DataSource.

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
api_instance = TweakApi.DataSourceApi()
id = 'id_example' # str | DataSource id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts keys of DataSource.
    api_response = api_instance.data_sources_id_keys_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceApi->data_sources_id_keys_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSource id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_id_keys_delete**
> data_sources_id_keys_delete(id)

Deletes all keys of this model.

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
api_instance = TweakApi.DataSourceApi()
id = 'id_example' # str | DataSource id

try: 
    # Deletes all keys of this model.
    api_instance.data_sources_id_keys_delete(id)
except ApiException as e:
    print("Exception when calling DataSourceApi->data_sources_id_keys_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSource id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_id_keys_fk_delete**
> data_sources_id_keys_fk_delete(id, fk)

Delete a related item by id for keys.

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
api_instance = TweakApi.DataSourceApi()
id = 'id_example' # str | DataSource id
fk = 'fk_example' # str | Foreign key for keys

try: 
    # Delete a related item by id for keys.
    api_instance.data_sources_id_keys_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DataSourceApi->data_sources_id_keys_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSource id | 
 **fk** | **str**| Foreign key for keys | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_id_keys_fk_get**
> DataSourceKey data_sources_id_keys_fk_get(id, fk)

Find a related item by id for keys.

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
api_instance = TweakApi.DataSourceApi()
id = 'id_example' # str | DataSource id
fk = 'fk_example' # str | Foreign key for keys

try: 
    # Find a related item by id for keys.
    api_response = api_instance.data_sources_id_keys_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceApi->data_sources_id_keys_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSource id | 
 **fk** | **str**| Foreign key for keys | 

### Return type

[**DataSourceKey**](DataSourceKey.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_id_keys_fk_put**
> DataSourceKey data_sources_id_keys_fk_put(id, fk, data=data)

Update a related item by id for keys.

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
api_instance = TweakApi.DataSourceApi()
id = 'id_example' # str | DataSource id
fk = 'fk_example' # str | Foreign key for keys
data = TweakApi.DataSourceKey() # DataSourceKey |  (optional)

try: 
    # Update a related item by id for keys.
    api_response = api_instance.data_sources_id_keys_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceApi->data_sources_id_keys_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSource id | 
 **fk** | **str**| Foreign key for keys | 
 **data** | [**DataSourceKey**](DataSourceKey.md)|  | [optional] 

### Return type

[**DataSourceKey**](DataSourceKey.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_id_keys_get**
> list[DataSourceKey] data_sources_id_keys_get(id, filter=filter)

Queries keys of DataSource.

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
api_instance = TweakApi.DataSourceApi()
id = 'id_example' # str | DataSource id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries keys of DataSource.
    api_response = api_instance.data_sources_id_keys_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceApi->data_sources_id_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSource id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DataSourceKey]**](DataSourceKey.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_sources_id_keys_post**
> DataSourceKey data_sources_id_keys_post(id, data=data)

Creates a new instance in keys of this model.

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
api_instance = TweakApi.DataSourceApi()
id = 'id_example' # str | DataSource id
data = TweakApi.DataSourceKey() # DataSourceKey |  (optional)

try: 
    # Creates a new instance in keys of this model.
    api_response = api_instance.data_sources_id_keys_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceApi->data_sources_id_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSource id | 
 **data** | [**DataSourceKey**](DataSourceKey.md)|  | [optional] 

### Return type

[**DataSourceKey**](DataSourceKey.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

