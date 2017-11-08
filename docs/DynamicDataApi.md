# TweakApi.DynamicDataApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dynamic_data_change_stream_get**](DynamicDataApi.md#dynamic_data_change_stream_get) | **GET** /DynamicData/change-stream | Create a change stream.
[**dynamic_data_change_stream_post**](DynamicDataApi.md#dynamic_data_change_stream_post) | **POST** /DynamicData/change-stream | Create a change stream.
[**dynamic_data_count_get**](DynamicDataApi.md#dynamic_data_count_get) | **GET** /DynamicData/count | Count instances of the model matched by where from the data source.
[**dynamic_data_find_one_get**](DynamicDataApi.md#dynamic_data_find_one_get) | **GET** /DynamicData/findOne | Find first instance of the model matched by filter from the data source.
[**dynamic_data_get**](DynamicDataApi.md#dynamic_data_get) | **GET** /DynamicData | Find all instances of the model matched by filter from the data source.
[**dynamic_data_id_delete**](DynamicDataApi.md#dynamic_data_id_delete) | **DELETE** /DynamicData/{id} | Delete a model instance by {{id}} from the data source.
[**dynamic_data_id_exists_get**](DynamicDataApi.md#dynamic_data_id_exists_get) | **GET** /DynamicData/{id}/exists | Check whether a model instance exists in the data source.
[**dynamic_data_id_get**](DynamicDataApi.md#dynamic_data_id_get) | **GET** /DynamicData/{id} | Find a model instance by {{id}} from the data source.
[**dynamic_data_id_head**](DynamicDataApi.md#dynamic_data_id_head) | **HEAD** /DynamicData/{id} | Check whether a model instance exists in the data source.
[**dynamic_data_id_patch**](DynamicDataApi.md#dynamic_data_id_patch) | **PATCH** /DynamicData/{id} | Patch attributes for a model instance and persist it into the data source.
[**dynamic_data_id_put**](DynamicDataApi.md#dynamic_data_id_put) | **PUT** /DynamicData/{id} | Replace attributes for a model instance and persist it into the data source.
[**dynamic_data_id_records_count_get**](DynamicDataApi.md#dynamic_data_id_records_count_get) | **GET** /DynamicData/{id}/records/count | Count Dynamic Data records
[**dynamic_data_id_records_delete**](DynamicDataApi.md#dynamic_data_id_records_delete) | **DELETE** /DynamicData/{id}/records | Delete all matching records.
[**dynamic_data_id_records_fk_delete**](DynamicDataApi.md#dynamic_data_id_records_fk_delete) | **DELETE** /DynamicData/{id}/records/{fk} | Delete a model instance by {{fk}} from the data source.
[**dynamic_data_id_records_fk_get**](DynamicDataApi.md#dynamic_data_id_records_fk_get) | **GET** /DynamicData/{id}/records/{fk} | Find a model instance by {{fk}} from the data source.
[**dynamic_data_id_records_fk_put**](DynamicDataApi.md#dynamic_data_id_records_fk_put) | **PUT** /DynamicData/{id}/records/{fk} | Replace attributes for a model instance and persist it into the data source.
[**dynamic_data_id_records_get**](DynamicDataApi.md#dynamic_data_id_records_get) | **GET** /DynamicData/{id}/records | Find all instances of the model matched by filter from the data source.
[**dynamic_data_id_records_migrate_post**](DynamicDataApi.md#dynamic_data_id_records_migrate_post) | **POST** /DynamicData/{id}/records/migrate | Request migration for Dynamic Data records
[**dynamic_data_id_records_post**](DynamicDataApi.md#dynamic_data_id_records_post) | **POST** /DynamicData/{id}/records | Create a new instance of the model and persist it into the data source.
[**dynamic_data_id_records_upload_csv_post**](DynamicDataApi.md#dynamic_data_id_records_upload_csv_post) | **POST** /DynamicData/{id}/records/upload/csv | Upload CSV for this Dynamic Data
[**dynamic_data_id_replace_post**](DynamicDataApi.md#dynamic_data_id_replace_post) | **POST** /DynamicData/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**dynamic_data_id_team_get**](DynamicDataApi.md#dynamic_data_id_team_get) | **GET** /DynamicData/{id}/team | Fetches belongsTo relation team.
[**dynamic_data_patch**](DynamicDataApi.md#dynamic_data_patch) | **PATCH** /DynamicData | Patch an existing model instance or insert a new one into the data source.
[**dynamic_data_post**](DynamicDataApi.md#dynamic_data_post) | **POST** /DynamicData | Create a new instance of the model and persist it into the data source.
[**dynamic_data_put**](DynamicDataApi.md#dynamic_data_put) | **PUT** /DynamicData | Replace an existing model instance or insert a new one into the data source.
[**dynamic_data_replace_or_create_post**](DynamicDataApi.md#dynamic_data_replace_or_create_post) | **POST** /DynamicData/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**dynamic_data_update_post**](DynamicDataApi.md#dynamic_data_update_post) | **POST** /DynamicData/update | Update instances of the model matched by {{where}} from the data source.
[**dynamic_data_upsert_with_where_post**](DynamicDataApi.md#dynamic_data_upsert_with_where_post) | **POST** /DynamicData/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **dynamic_data_change_stream_get**
> file dynamic_data_change_stream_get(options=options)

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
api_instance = TweakApi.DynamicDataApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.dynamic_data_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_change_stream_get: %s\n" % e)
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

# **dynamic_data_change_stream_post**
> file dynamic_data_change_stream_post(options=options)

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
api_instance = TweakApi.DynamicDataApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.dynamic_data_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_change_stream_post: %s\n" % e)
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

# **dynamic_data_count_get**
> InlineResponse200 dynamic_data_count_get(where=where)

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
api_instance = TweakApi.DynamicDataApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.dynamic_data_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_count_get: %s\n" % e)
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

# **dynamic_data_find_one_get**
> DynamicData dynamic_data_find_one_get(filter=filter)

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
api_instance = TweakApi.DynamicDataApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.dynamic_data_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_get**
> list[DynamicData] dynamic_data_get(filter=filter)

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
api_instance = TweakApi.DynamicDataApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.dynamic_data_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[DynamicData]**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_delete**
> object dynamic_data_id_delete(id)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.dynamic_data_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_delete: %s\n" % e)
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

# **dynamic_data_id_exists_get**
> InlineResponse2001 dynamic_data_id_exists_get(id)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.dynamic_data_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_exists_get: %s\n" % e)
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

# **dynamic_data_id_get**
> DynamicData dynamic_data_id_get(id, filter=filter)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.dynamic_data_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_head**
> InlineResponse2001 dynamic_data_id_head(id)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.dynamic_data_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_head: %s\n" % e)
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

# **dynamic_data_id_patch**
> DynamicData dynamic_data_id_patch(id, data=data)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
data = TweakApi.DynamicData() # DynamicData | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.dynamic_data_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **data** | [**DynamicData**](DynamicData.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_put**
> DynamicData dynamic_data_id_put(id, data=data)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | Model id
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.dynamic_data_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_count_get**
> InlineResponse200 dynamic_data_id_records_count_get(id, where=where)

Count Dynamic Data records

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count Dynamic Data records
    api_response = api_instance.dynamic_data_id_records_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_delete**
> object dynamic_data_id_records_delete(id, where=where)

Delete all matching records.

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
where = 'where_example' # str | filter.where object (optional)

try: 
    # Delete all matching records.
    api_response = api_instance.dynamic_data_id_records_delete(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **where** | **str**| filter.where object | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_fk_delete**
> object dynamic_data_id_records_fk_delete(id, fk)

Delete a model instance by {{fk}} from the data source.

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
fk = 'fk_example' # str | Model id

try: 
    # Delete a model instance by {{fk}} from the data source.
    api_response = api_instance.dynamic_data_id_records_fk_delete(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **fk** | **str**| Model id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_fk_get**
> object dynamic_data_id_records_fk_get(id, fk, filter=filter)

Find a model instance by {{fk}} from the data source.

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
fk = 'fk_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{fk}} from the data source.
    api_response = api_instance.dynamic_data_id_records_fk_get(id, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **fk** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_fk_put**
> object dynamic_data_id_records_fk_put(id, fk, data=data)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
fk = 'fk_example' # str | Model id
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.dynamic_data_id_records_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **fk** | **str**| Model id | 
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_get**
> list[object] dynamic_data_id_records_get(id, filter=filter)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.dynamic_data_id_records_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

**list[object]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_migrate_post**
> object dynamic_data_id_records_migrate_post(id, data=data)

Request migration for Dynamic Data records

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Request migration for Dynamic Data records
    api_response = api_instance.dynamic_data_id_records_migrate_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_migrate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_post**
> object dynamic_data_id_records_post(id, data=data)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.dynamic_data_id_records_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_records_upload_csv_post**
> object dynamic_data_id_records_upload_csv_post(id)

Upload CSV for this Dynamic Data

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id

try: 
    # Upload CSV for this Dynamic Data
    api_response = api_instance.dynamic_data_id_records_upload_csv_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_upload_csv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_replace_post**
> DynamicData dynamic_data_id_replace_post(id, data=data)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | Model id
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.dynamic_data_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_team_get**
> Team dynamic_data_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.DynamicDataApi()
id = 'id_example' # str | DynamicData id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.dynamic_data_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_patch**
> DynamicData dynamic_data_patch(data=data)

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
api_instance = TweakApi.DynamicDataApi()
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.dynamic_data_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_post**
> DynamicData dynamic_data_post(data=data)

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
api_instance = TweakApi.DynamicDataApi()
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.dynamic_data_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_put**
> DynamicData dynamic_data_put(data=data)

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
api_instance = TweakApi.DynamicDataApi()
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.dynamic_data_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_replace_or_create_post**
> DynamicData dynamic_data_replace_or_create_post(data=data)

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
api_instance = TweakApi.DynamicDataApi()
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.dynamic_data_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_update_post**
> InlineResponse2002 dynamic_data_update_post(where=where, data=data)

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
api_instance = TweakApi.DynamicDataApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DynamicData() # DynamicData | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.dynamic_data_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DynamicData**](DynamicData.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_upsert_with_where_post**
> DynamicData dynamic_data_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.DynamicDataApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.DynamicData() # DynamicData | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.dynamic_data_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**DynamicData**](DynamicData.md)| An object of model property name/value pairs | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

