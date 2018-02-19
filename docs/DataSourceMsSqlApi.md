# TweakApi.DataSourceMsSqlApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_source_ms_sqls_change_stream_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_change_stream_get) | **GET** /DataSourceMsSqls/change-stream | Create a change stream.
[**data_source_ms_sqls_change_stream_post**](DataSourceMsSqlApi.md#data_source_ms_sqls_change_stream_post) | **POST** /DataSourceMsSqls/change-stream | Create a change stream.
[**data_source_ms_sqls_count_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_count_get) | **GET** /DataSourceMsSqls/count | Count instances of the model matched by where from the data source.
[**data_source_ms_sqls_find_one_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_find_one_get) | **GET** /DataSourceMsSqls/findOne | Find first instance of the model matched by filter from the data source.
[**data_source_ms_sqls_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_get) | **GET** /DataSourceMsSqls | Find all instances of the model matched by filter from the data source.
[**data_source_ms_sqls_id_delete**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_delete) | **DELETE** /DataSourceMsSqls/{id} | Delete a model instance by {{id}} from the data source.
[**data_source_ms_sqls_id_dynamic_datas_count_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_dynamic_datas_count_get) | **GET** /DataSourceMsSqls/{id}/dynamicDatas/count | Counts dynamicDatas of DataSourceMsSql.
[**data_source_ms_sqls_id_dynamic_datas_delete**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_dynamic_datas_delete) | **DELETE** /DataSourceMsSqls/{id}/dynamicDatas | Deletes all dynamicDatas of this model.
[**data_source_ms_sqls_id_dynamic_datas_fk_delete**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_dynamic_datas_fk_delete) | **DELETE** /DataSourceMsSqls/{id}/dynamicDatas/{fk} | Delete a related item by id for dynamicDatas.
[**data_source_ms_sqls_id_dynamic_datas_fk_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_dynamic_datas_fk_get) | **GET** /DataSourceMsSqls/{id}/dynamicDatas/{fk} | Find a related item by id for dynamicDatas.
[**data_source_ms_sqls_id_dynamic_datas_fk_put**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_dynamic_datas_fk_put) | **PUT** /DataSourceMsSqls/{id}/dynamicDatas/{fk} | Update a related item by id for dynamicDatas.
[**data_source_ms_sqls_id_dynamic_datas_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_dynamic_datas_get) | **GET** /DataSourceMsSqls/{id}/dynamicDatas | Queries dynamicDatas of DataSourceMsSql.
[**data_source_ms_sqls_id_dynamic_datas_post**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_dynamic_datas_post) | **POST** /DataSourceMsSqls/{id}/dynamicDatas | Creates a new instance in dynamicDatas of this model.
[**data_source_ms_sqls_id_exists_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_exists_get) | **GET** /DataSourceMsSqls/{id}/exists | Check whether a model instance exists in the data source.
[**data_source_ms_sqls_id_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_get) | **GET** /DataSourceMsSqls/{id} | Find a model instance by {{id}} from the data source.
[**data_source_ms_sqls_id_head**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_head) | **HEAD** /DataSourceMsSqls/{id} | Check whether a model instance exists in the data source.
[**data_source_ms_sqls_id_patch**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_patch) | **PATCH** /DataSourceMsSqls/{id} | Patch attributes for a model instance and persist it into the data source.
[**data_source_ms_sqls_id_put**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_put) | **PUT** /DataSourceMsSqls/{id} | Replace attributes for a model instance and persist it into the data source.
[**data_source_ms_sqls_id_replace_post**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_replace_post) | **POST** /DataSourceMsSqls/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**data_source_ms_sqls_id_team_get**](DataSourceMsSqlApi.md#data_source_ms_sqls_id_team_get) | **GET** /DataSourceMsSqls/{id}/team | Fetches belongsTo relation team.
[**data_source_ms_sqls_post**](DataSourceMsSqlApi.md#data_source_ms_sqls_post) | **POST** /DataSourceMsSqls | Create a new instance of the model and persist it into the data source.


# **data_source_ms_sqls_change_stream_get**
> file data_source_ms_sqls_change_stream_get(options=options)

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
api_instance = TweakApi.DataSourceMsSqlApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.data_source_ms_sqls_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_change_stream_get: %s\n" % e)
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

# **data_source_ms_sqls_change_stream_post**
> file data_source_ms_sqls_change_stream_post(options=options)

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
api_instance = TweakApi.DataSourceMsSqlApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.data_source_ms_sqls_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_change_stream_post: %s\n" % e)
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

# **data_source_ms_sqls_count_get**
> InlineResponse2001 data_source_ms_sqls_count_get(where=where)

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
api_instance = TweakApi.DataSourceMsSqlApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.data_source_ms_sqls_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_count_get: %s\n" % e)
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

# **data_source_ms_sqls_find_one_get**
> DataSourceMsSql data_source_ms_sqls_find_one_get(filter=filter)

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
api_instance = TweakApi.DataSourceMsSqlApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.data_source_ms_sqls_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_get**
> list[DataSourceMsSql] data_source_ms_sqls_get(filter=filter)

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
api_instance = TweakApi.DataSourceMsSqlApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.data_source_ms_sqls_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[DataSourceMsSql]**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_delete**
> object data_source_ms_sqls_id_delete(id)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.data_source_ms_sqls_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_delete: %s\n" % e)
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

# **data_source_ms_sqls_id_dynamic_datas_count_get**
> InlineResponse2001 data_source_ms_sqls_id_dynamic_datas_count_get(id, where=where)

Counts dynamicDatas of DataSourceMsSql.

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts dynamicDatas of DataSourceMsSql.
    api_response = api_instance.data_source_ms_sqls_id_dynamic_datas_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_dynamic_datas_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_dynamic_datas_delete**
> data_source_ms_sqls_id_dynamic_datas_delete(id)

Deletes all dynamicDatas of this model.

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id

try: 
    # Deletes all dynamicDatas of this model.
    api_instance.data_source_ms_sqls_id_dynamic_datas_delete(id)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_dynamic_datas_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_dynamic_datas_fk_delete**
> data_source_ms_sqls_id_dynamic_datas_fk_delete(id, fk)

Delete a related item by id for dynamicDatas.

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Delete a related item by id for dynamicDatas.
    api_instance.data_source_ms_sqls_id_dynamic_datas_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_dynamic_datas_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_dynamic_datas_fk_get**
> DynamicData data_source_ms_sqls_id_dynamic_datas_fk_get(id, fk)

Find a related item by id for dynamicDatas.

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Find a related item by id for dynamicDatas.
    api_response = api_instance.data_source_ms_sqls_id_dynamic_datas_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_dynamic_datas_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_dynamic_datas_fk_put**
> DynamicData data_source_ms_sqls_id_dynamic_datas_fk_put(id, fk, data=data)

Update a related item by id for dynamicDatas.

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
fk = 'fk_example' # str | Foreign key for dynamicDatas
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Update a related item by id for dynamicDatas.
    api_response = api_instance.data_source_ms_sqls_id_dynamic_datas_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_dynamic_datas_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **fk** | **str**| Foreign key for dynamicDatas | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_dynamic_datas_get**
> list[DynamicData] data_source_ms_sqls_id_dynamic_datas_get(id, filter=filter)

Queries dynamicDatas of DataSourceMsSql.

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries dynamicDatas of DataSourceMsSql.
    api_response = api_instance.data_source_ms_sqls_id_dynamic_datas_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_dynamic_datas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DynamicData]**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_dynamic_datas_post**
> DynamicData data_source_ms_sqls_id_dynamic_datas_post(id, data=data)

Creates a new instance in dynamicDatas of this model.

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Creates a new instance in dynamicDatas of this model.
    api_response = api_instance.data_source_ms_sqls_id_dynamic_datas_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_dynamic_datas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_exists_get**
> InlineResponse2002 data_source_ms_sqls_id_exists_get(id)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.data_source_ms_sqls_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_exists_get: %s\n" % e)
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

# **data_source_ms_sqls_id_get**
> DataSourceMsSql data_source_ms_sqls_id_get(id, filter=filter)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.data_source_ms_sqls_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_head**
> InlineResponse2002 data_source_ms_sqls_id_head(id)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.data_source_ms_sqls_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_head: %s\n" % e)
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

# **data_source_ms_sqls_id_patch**
> DataSourceMsSql data_source_ms_sqls_id_patch(id, data=data)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
data = TweakApi.DataSourceMsSql() # DataSourceMsSql | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.data_source_ms_sqls_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **data** | [**DataSourceMsSql**](DataSourceMsSql.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_put**
> DataSourceMsSql data_source_ms_sqls_id_put(id, data=data)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | Model id
data = TweakApi.DataSourceMsSql() # DataSourceMsSql | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.data_source_ms_sqls_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DataSourceMsSql**](DataSourceMsSql.md)| Model instance data | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_replace_post**
> DataSourceMsSql data_source_ms_sqls_id_replace_post(id, data=data)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | Model id
data = TweakApi.DataSourceMsSql() # DataSourceMsSql | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.data_source_ms_sqls_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DataSourceMsSql**](DataSourceMsSql.md)| Model instance data | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_id_team_get**
> Team data_source_ms_sqls_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.DataSourceMsSqlApi()
id = 'id_example' # str | DataSourceMsSql id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.data_source_ms_sqls_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceMsSql id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_ms_sqls_post**
> DataSourceMsSql data_source_ms_sqls_post(data=data)

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
api_instance = TweakApi.DataSourceMsSqlApi()
data = TweakApi.DataSourceMsSql() # DataSourceMsSql | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.data_source_ms_sqls_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceMsSqlApi->data_source_ms_sqls_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DataSourceMsSql**](DataSourceMsSql.md)| Model instance data | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

