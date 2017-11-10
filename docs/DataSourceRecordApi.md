# TweakApi.DataSourceRecordApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_source_records_change_stream_get**](DataSourceRecordApi.md#data_source_records_change_stream_get) | **GET** /DataSourceRecords/change-stream | Create a change stream.
[**data_source_records_change_stream_post**](DataSourceRecordApi.md#data_source_records_change_stream_post) | **POST** /DataSourceRecords/change-stream | Create a change stream.
[**data_source_records_count_get**](DataSourceRecordApi.md#data_source_records_count_get) | **GET** /DataSourceRecords/count | Count instances of the model matched by where from the data source.
[**data_source_records_find_one_get**](DataSourceRecordApi.md#data_source_records_find_one_get) | **GET** /DataSourceRecords/findOne | Find first instance of the model matched by filter from the data source.
[**data_source_records_get**](DataSourceRecordApi.md#data_source_records_get) | **GET** /DataSourceRecords | Find all instances of the model matched by filter from the data source.
[**data_source_records_id_data_source_get**](DataSourceRecordApi.md#data_source_records_id_data_source_get) | **GET** /DataSourceRecords/{id}/dataSource | Fetches belongsTo relation dataSource.
[**data_source_records_id_delete**](DataSourceRecordApi.md#data_source_records_id_delete) | **DELETE** /DataSourceRecords/{id} | Delete a model instance by {{id}} from the data source.
[**data_source_records_id_exists_get**](DataSourceRecordApi.md#data_source_records_id_exists_get) | **GET** /DataSourceRecords/{id}/exists | Check whether a model instance exists in the data source.
[**data_source_records_id_get**](DataSourceRecordApi.md#data_source_records_id_get) | **GET** /DataSourceRecords/{id} | Find a model instance by {{id}} from the data source.
[**data_source_records_id_head**](DataSourceRecordApi.md#data_source_records_id_head) | **HEAD** /DataSourceRecords/{id} | Check whether a model instance exists in the data source.
[**data_source_records_id_patch**](DataSourceRecordApi.md#data_source_records_id_patch) | **PATCH** /DataSourceRecords/{id} | Patch attributes for a model instance and persist it into the data source.
[**data_source_records_id_put**](DataSourceRecordApi.md#data_source_records_id_put) | **PUT** /DataSourceRecords/{id} | Replace attributes for a model instance and persist it into the data source.
[**data_source_records_id_replace_post**](DataSourceRecordApi.md#data_source_records_id_replace_post) | **POST** /DataSourceRecords/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**data_source_records_id_team_get**](DataSourceRecordApi.md#data_source_records_id_team_get) | **GET** /DataSourceRecords/{id}/team | Fetches belongsTo relation team.
[**data_source_records_id_values_count_get**](DataSourceRecordApi.md#data_source_records_id_values_count_get) | **GET** /DataSourceRecords/{id}/values/count | Counts values of DataSourceRecord.
[**data_source_records_id_values_delete**](DataSourceRecordApi.md#data_source_records_id_values_delete) | **DELETE** /DataSourceRecords/{id}/values | Deletes all values of this model.
[**data_source_records_id_values_fk_delete**](DataSourceRecordApi.md#data_source_records_id_values_fk_delete) | **DELETE** /DataSourceRecords/{id}/values/{fk} | Delete a related item by id for values.
[**data_source_records_id_values_fk_get**](DataSourceRecordApi.md#data_source_records_id_values_fk_get) | **GET** /DataSourceRecords/{id}/values/{fk} | Find a related item by id for values.
[**data_source_records_id_values_fk_put**](DataSourceRecordApi.md#data_source_records_id_values_fk_put) | **PUT** /DataSourceRecords/{id}/values/{fk} | Update a related item by id for values.
[**data_source_records_id_values_get**](DataSourceRecordApi.md#data_source_records_id_values_get) | **GET** /DataSourceRecords/{id}/values | Queries values of DataSourceRecord.
[**data_source_records_id_values_post**](DataSourceRecordApi.md#data_source_records_id_values_post) | **POST** /DataSourceRecords/{id}/values | Creates a new instance in values of this model.
[**data_source_records_patch**](DataSourceRecordApi.md#data_source_records_patch) | **PATCH** /DataSourceRecords | Patch an existing model instance or insert a new one into the data source.
[**data_source_records_post**](DataSourceRecordApi.md#data_source_records_post) | **POST** /DataSourceRecords | Create a new instance of the model and persist it into the data source.
[**data_source_records_put**](DataSourceRecordApi.md#data_source_records_put) | **PUT** /DataSourceRecords | Replace an existing model instance or insert a new one into the data source.
[**data_source_records_replace_or_create_post**](DataSourceRecordApi.md#data_source_records_replace_or_create_post) | **POST** /DataSourceRecords/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**data_source_records_update_post**](DataSourceRecordApi.md#data_source_records_update_post) | **POST** /DataSourceRecords/update | Update instances of the model matched by {{where}} from the data source.
[**data_source_records_upsert_with_where_post**](DataSourceRecordApi.md#data_source_records_upsert_with_where_post) | **POST** /DataSourceRecords/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **data_source_records_change_stream_get**
> file data_source_records_change_stream_get(options=options)

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
api_instance = TweakApi.DataSourceRecordApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.data_source_records_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_change_stream_get: %s\n" % e)
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

# **data_source_records_change_stream_post**
> file data_source_records_change_stream_post(options=options)

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
api_instance = TweakApi.DataSourceRecordApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.data_source_records_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_change_stream_post: %s\n" % e)
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

# **data_source_records_count_get**
> InlineResponse200 data_source_records_count_get(where=where)

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
api_instance = TweakApi.DataSourceRecordApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.data_source_records_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_count_get: %s\n" % e)
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

# **data_source_records_find_one_get**
> DataSourceRecord data_source_records_find_one_get(filter=filter)

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
api_instance = TweakApi.DataSourceRecordApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.data_source_records_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_get**
> list[DataSourceRecord] data_source_records_get(filter=filter)

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
api_instance = TweakApi.DataSourceRecordApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.data_source_records_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[DataSourceRecord]**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_data_source_get**
> DataSource data_source_records_id_data_source_get(id, refresh=refresh)

Fetches belongsTo relation dataSource.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSource.
    api_response = api_instance.data_source_records_id_data_source_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_data_source_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_delete**
> object data_source_records_id_delete(id)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.data_source_records_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_delete: %s\n" % e)
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

# **data_source_records_id_exists_get**
> InlineResponse2001 data_source_records_id_exists_get(id)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.data_source_records_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_exists_get: %s\n" % e)
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

# **data_source_records_id_get**
> DataSourceRecord data_source_records_id_get(id, filter=filter)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.data_source_records_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_head**
> InlineResponse2001 data_source_records_id_head(id)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.data_source_records_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_head: %s\n" % e)
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

# **data_source_records_id_patch**
> DataSourceRecord data_source_records_id_patch(id, data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
data = TweakApi.DataSourceRecord() # DataSourceRecord | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.data_source_records_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_put**
> DataSourceRecord data_source_records_id_put(id, data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | Model id
data = TweakApi.DataSourceRecord() # DataSourceRecord | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.data_source_records_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| Model instance data | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_replace_post**
> DataSourceRecord data_source_records_id_replace_post(id, data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | Model id
data = TweakApi.DataSourceRecord() # DataSourceRecord | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.data_source_records_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| Model instance data | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_team_get**
> Team data_source_records_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.data_source_records_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_values_count_get**
> InlineResponse200 data_source_records_id_values_count_get(id, where=where)

Counts values of DataSourceRecord.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts values of DataSourceRecord.
    api_response = api_instance.data_source_records_id_values_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_values_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_values_delete**
> data_source_records_id_values_delete(id)

Deletes all values of this model.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id

try: 
    # Deletes all values of this model.
    api_instance.data_source_records_id_values_delete(id)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_values_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_values_fk_delete**
> data_source_records_id_values_fk_delete(id, fk)

Delete a related item by id for values.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
fk = 'fk_example' # str | Foreign key for values

try: 
    # Delete a related item by id for values.
    api_instance.data_source_records_id_values_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_values_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **fk** | **str**| Foreign key for values | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_values_fk_get**
> DataSourceRecordValue data_source_records_id_values_fk_get(id, fk)

Find a related item by id for values.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
fk = 'fk_example' # str | Foreign key for values

try: 
    # Find a related item by id for values.
    api_response = api_instance.data_source_records_id_values_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_values_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **fk** | **str**| Foreign key for values | 

### Return type

[**DataSourceRecordValue**](DataSourceRecordValue.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_values_fk_put**
> DataSourceRecordValue data_source_records_id_values_fk_put(id, fk, data=data)

Update a related item by id for values.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
fk = 'fk_example' # str | Foreign key for values
data = TweakApi.DataSourceRecordValue() # DataSourceRecordValue |  (optional)

try: 
    # Update a related item by id for values.
    api_response = api_instance.data_source_records_id_values_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_values_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **fk** | **str**| Foreign key for values | 
 **data** | [**DataSourceRecordValue**](DataSourceRecordValue.md)|  | [optional] 

### Return type

[**DataSourceRecordValue**](DataSourceRecordValue.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_values_get**
> list[DataSourceRecordValue] data_source_records_id_values_get(id, filter=filter)

Queries values of DataSourceRecord.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries values of DataSourceRecord.
    api_response = api_instance.data_source_records_id_values_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_values_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DataSourceRecordValue]**](DataSourceRecordValue.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_id_values_post**
> DataSourceRecordValue data_source_records_id_values_post(id, data=data)

Creates a new instance in values of this model.

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
api_instance = TweakApi.DataSourceRecordApi()
id = 'id_example' # str | DataSourceRecord id
data = TweakApi.DataSourceRecordValue() # DataSourceRecordValue |  (optional)

try: 
    # Creates a new instance in values of this model.
    api_response = api_instance.data_source_records_id_values_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_id_values_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DataSourceRecord id | 
 **data** | [**DataSourceRecordValue**](DataSourceRecordValue.md)|  | [optional] 

### Return type

[**DataSourceRecordValue**](DataSourceRecordValue.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_patch**
> DataSourceRecord data_source_records_patch(data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
data = TweakApi.DataSourceRecord() # DataSourceRecord | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.data_source_records_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| Model instance data | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_post**
> DataSourceRecord data_source_records_post(data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
data = TweakApi.DataSourceRecord() # DataSourceRecord | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.data_source_records_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| Model instance data | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_put**
> DataSourceRecord data_source_records_put(data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
data = TweakApi.DataSourceRecord() # DataSourceRecord | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.data_source_records_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| Model instance data | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_replace_or_create_post**
> DataSourceRecord data_source_records_replace_or_create_post(data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
data = TweakApi.DataSourceRecord() # DataSourceRecord | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.data_source_records_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| Model instance data | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_update_post**
> InlineResponse2002 data_source_records_update_post(where=where, data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DataSourceRecord() # DataSourceRecord | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.data_source_records_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_source_records_upsert_with_where_post**
> DataSourceRecord data_source_records_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.DataSourceRecordApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DataSourceRecord() # DataSourceRecord | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.data_source_records_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourceRecordApi->data_source_records_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DataSourceRecord**](DataSourceRecord.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DataSourceRecord**](DataSourceRecord.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

