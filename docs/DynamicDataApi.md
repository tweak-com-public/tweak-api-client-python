# TweakApi.DynamicDataApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dynamic_data_change_stream_get**](DynamicDataApi.md#dynamic_data_change_stream_get) | **GET** /DynamicData/change-stream | Create a change stream.
[**dynamic_data_change_stream_post**](DynamicDataApi.md#dynamic_data_change_stream_post) | **POST** /DynamicData/change-stream | Create a change stream.
[**dynamic_data_count_get**](DynamicDataApi.md#dynamic_data_count_get) | **GET** /DynamicData/count | Count instances of the model matched by where from the data source.
[**dynamic_data_find_one_get**](DynamicDataApi.md#dynamic_data_find_one_get) | **GET** /DynamicData/findOne | Find first instance of the model matched by filter from the data source.
[**dynamic_data_get**](DynamicDataApi.md#dynamic_data_get) | **GET** /DynamicData | Find all instances of the model matched by filter from the data source.
[**dynamic_data_id_data_source_mongo_get**](DynamicDataApi.md#dynamic_data_id_data_source_mongo_get) | **GET** /DynamicData/{id}/dataSourceMongo | Fetches belongsTo relation dataSourceMongo.
[**dynamic_data_id_data_source_ms_sql_get**](DynamicDataApi.md#dynamic_data_id_data_source_ms_sql_get) | **GET** /DynamicData/{id}/dataSourceMsSql | Fetches belongsTo relation dataSourceMsSql.
[**dynamic_data_id_data_source_my_sql_get**](DynamicDataApi.md#dynamic_data_id_data_source_my_sql_get) | **GET** /DynamicData/{id}/dataSourceMySql | Fetches belongsTo relation dataSourceMySql.
[**dynamic_data_id_data_source_oracle_get**](DynamicDataApi.md#dynamic_data_id_data_source_oracle_get) | **GET** /DynamicData/{id}/dataSourceOracle | Fetches belongsTo relation dataSourceOracle.
[**dynamic_data_id_data_source_postgre_sql_get**](DynamicDataApi.md#dynamic_data_id_data_source_postgre_sql_get) | **GET** /DynamicData/{id}/dataSourcePostgreSql | Fetches belongsTo relation dataSourcePostgreSql.
[**dynamic_data_id_data_source_rest_get**](DynamicDataApi.md#dynamic_data_id_data_source_rest_get) | **GET** /DynamicData/{id}/dataSourceRest | Fetches belongsTo relation dataSourceRest.
[**dynamic_data_id_data_source_soap_get**](DynamicDataApi.md#dynamic_data_id_data_source_soap_get) | **GET** /DynamicData/{id}/dataSourceSoap | Fetches belongsTo relation dataSourceSoap.
[**dynamic_data_id_delete**](DynamicDataApi.md#dynamic_data_id_delete) | **DELETE** /DynamicData/{id} | Delete a model instance by {{id}} from the data source.
[**dynamic_data_id_designs_count_get**](DynamicDataApi.md#dynamic_data_id_designs_count_get) | **GET** /DynamicData/{id}/designs/count | Counts designs of DynamicData.
[**dynamic_data_id_designs_fk_delete**](DynamicDataApi.md#dynamic_data_id_designs_fk_delete) | **DELETE** /DynamicData/{id}/designs/{fk} | Delete a related item by id for designs.
[**dynamic_data_id_designs_fk_get**](DynamicDataApi.md#dynamic_data_id_designs_fk_get) | **GET** /DynamicData/{id}/designs/{fk} | Find a related item by id for designs.
[**dynamic_data_id_designs_fk_put**](DynamicDataApi.md#dynamic_data_id_designs_fk_put) | **PUT** /DynamicData/{id}/designs/{fk} | Update a related item by id for designs.
[**dynamic_data_id_designs_get**](DynamicDataApi.md#dynamic_data_id_designs_get) | **GET** /DynamicData/{id}/designs | Queries designs of DynamicData.
[**dynamic_data_id_designs_post**](DynamicDataApi.md#dynamic_data_id_designs_post) | **POST** /DynamicData/{id}/designs | Creates a new instance in designs of this model.
[**dynamic_data_id_exists_get**](DynamicDataApi.md#dynamic_data_id_exists_get) | **GET** /DynamicData/{id}/exists | Check whether a model instance exists in the data source.
[**dynamic_data_id_fetch_raw_get**](DynamicDataApi.md#dynamic_data_id_fetch_raw_get) | **GET** /DynamicData/{id}/fetch/raw | Fetch raw datas from external servers.
[**dynamic_data_id_get**](DynamicDataApi.md#dynamic_data_id_get) | **GET** /DynamicData/{id} | Find a model instance by {{id}} from the data source.
[**dynamic_data_id_head**](DynamicDataApi.md#dynamic_data_id_head) | **HEAD** /DynamicData/{id} | Check whether a model instance exists in the data source.
[**dynamic_data_id_patch**](DynamicDataApi.md#dynamic_data_id_patch) | **PATCH** /DynamicData/{id} | Patch attributes for a model instance and persist it into the data source.
[**dynamic_data_id_put**](DynamicDataApi.md#dynamic_data_id_put) | **PUT** /DynamicData/{id} | Replace attributes for a model instance and persist it into the data source.
[**dynamic_data_id_records_count_get**](DynamicDataApi.md#dynamic_data_id_records_count_get) | **GET** /DynamicData/{id}/records/count | Count Dynamic Data records
[**dynamic_data_id_records_delete**](DynamicDataApi.md#dynamic_data_id_records_delete) | **DELETE** /DynamicData/{id}/records | Delete all matching records.
[**dynamic_data_id_records_fk_delete**](DynamicDataApi.md#dynamic_data_id_records_fk_delete) | **DELETE** /DynamicData/{id}/records/{fk} | Delete a model instance by {{fk}} from the data source.
[**dynamic_data_id_records_fk_get**](DynamicDataApi.md#dynamic_data_id_records_fk_get) | **GET** /DynamicData/{id}/records/{fk} | Find a model instance by {{fk}} from the data source.
[**dynamic_data_id_records_fk_property_name_upload_put**](DynamicDataApi.md#dynamic_data_id_records_fk_property_name_upload_put) | **PUT** /DynamicData/{id}/records/{fk}/{propertyName}/upload | Replace attributes for a model instance and persist it into the data source.
[**dynamic_data_id_records_fk_put**](DynamicDataApi.md#dynamic_data_id_records_fk_put) | **PUT** /DynamicData/{id}/records/{fk} | Replace attributes for a model instance and persist it into the data source.
[**dynamic_data_id_records_get**](DynamicDataApi.md#dynamic_data_id_records_get) | **GET** /DynamicData/{id}/records | Find all instances of the model matched by filter from the data source.
[**dynamic_data_id_records_migrate_post**](DynamicDataApi.md#dynamic_data_id_records_migrate_post) | **POST** /DynamicData/{id}/records/migrate | Request migration for Dynamic Data records
[**dynamic_data_id_records_post**](DynamicDataApi.md#dynamic_data_id_records_post) | **POST** /DynamicData/{id}/records | Create a new instance of the model and persist it into the data source.
[**dynamic_data_id_records_upload_csv_post**](DynamicDataApi.md#dynamic_data_id_records_upload_csv_post) | **POST** /DynamicData/{id}/records/upload/csv | Upload CSV for this Dynamic Data
[**dynamic_data_id_replace_post**](DynamicDataApi.md#dynamic_data_id_replace_post) | **POST** /DynamicData/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**dynamic_data_id_team_get**](DynamicDataApi.md#dynamic_data_id_team_get) | **GET** /DynamicData/{id}/team | Fetches belongsTo relation team.
[**dynamic_data_post**](DynamicDataApi.md#dynamic_data_post) | **POST** /DynamicData | Create a new instance of the model and persist it into the data source.


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
> InlineResponse2001 dynamic_data_count_get(where=where)

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

[**InlineResponse2001**](InlineResponse2001.md)

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

# **dynamic_data_id_data_source_mongo_get**
> DataSourceMongo dynamic_data_id_data_source_mongo_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceMongo.

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
    # Fetches belongsTo relation dataSourceMongo.
    api_response = api_instance.dynamic_data_id_data_source_mongo_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_data_source_mongo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMongo**](DataSourceMongo.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_data_source_ms_sql_get**
> DataSourceMsSql dynamic_data_id_data_source_ms_sql_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceMsSql.

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
    # Fetches belongsTo relation dataSourceMsSql.
    api_response = api_instance.dynamic_data_id_data_source_ms_sql_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_data_source_ms_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_data_source_my_sql_get**
> DataSourceMySql dynamic_data_id_data_source_my_sql_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceMySql.

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
    # Fetches belongsTo relation dataSourceMySql.
    api_response = api_instance.dynamic_data_id_data_source_my_sql_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_data_source_my_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMySql**](DataSourceMySql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_data_source_oracle_get**
> DataSourceOracle dynamic_data_id_data_source_oracle_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceOracle.

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
    # Fetches belongsTo relation dataSourceOracle.
    api_response = api_instance.dynamic_data_id_data_source_oracle_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_data_source_oracle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceOracle**](DataSourceOracle.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_data_source_postgre_sql_get**
> DataSourcePostgreSql dynamic_data_id_data_source_postgre_sql_get(id, refresh=refresh)

Fetches belongsTo relation dataSourcePostgreSql.

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
    # Fetches belongsTo relation dataSourcePostgreSql.
    api_response = api_instance.dynamic_data_id_data_source_postgre_sql_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_data_source_postgre_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourcePostgreSql**](DataSourcePostgreSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_data_source_rest_get**
> DataSourceRest dynamic_data_id_data_source_rest_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceRest.

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
    # Fetches belongsTo relation dataSourceRest.
    api_response = api_instance.dynamic_data_id_data_source_rest_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_data_source_rest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceRest**](DataSourceRest.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_data_source_soap_get**
> DataSourceSoap dynamic_data_id_data_source_soap_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceSoap.

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
    # Fetches belongsTo relation dataSourceSoap.
    api_response = api_instance.dynamic_data_id_data_source_soap_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_data_source_soap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceSoap**](DataSourceSoap.md)

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

# **dynamic_data_id_designs_count_get**
> InlineResponse2001 dynamic_data_id_designs_count_get(id, where=where)

Counts designs of DynamicData.

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
    # Counts designs of DynamicData.
    api_response = api_instance.dynamic_data_id_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_designs_fk_delete**
> dynamic_data_id_designs_fk_delete(id, fk)

Delete a related item by id for designs.

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
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.dynamic_data_id_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_designs_fk_get**
> Design dynamic_data_id_designs_fk_get(id, fk)

Find a related item by id for designs.

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
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.dynamic_data_id_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_designs_fk_put**
> Design dynamic_data_id_designs_fk_put(id, fk, data=data)

Update a related item by id for designs.

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
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.dynamic_data_id_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_designs_get**
> list[Design] dynamic_data_id_designs_get(id, filter=filter)

Queries designs of DynamicData.

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
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of DynamicData.
    api_response = api_instance.dynamic_data_id_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_designs_post**
> Design dynamic_data_id_designs_post(id, data=data)

Creates a new instance in designs of this model.

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
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.dynamic_data_id_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_exists_get**
> InlineResponse2002 dynamic_data_id_exists_get(id)

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

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dynamic_data_id_fetch_raw_get**
> XAny dynamic_data_id_fetch_raw_get(id, params=params)

Fetch raw datas from external servers.

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
params = 'params_example' # str | Request parameters (optional)

try: 
    # Fetch raw datas from external servers.
    api_response = api_instance.dynamic_data_id_fetch_raw_get(id, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_fetch_raw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **params** | **str**| Request parameters | [optional] 

### Return type

[**XAny**](XAny.md)

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
> InlineResponse2002 dynamic_data_id_head(id)

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

[**InlineResponse2002**](InlineResponse2002.md)

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
> InlineResponse2001 dynamic_data_id_records_count_get(id, where=where)

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

[**InlineResponse2001**](InlineResponse2001.md)

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

# **dynamic_data_id_records_fk_property_name_upload_put**
> object dynamic_data_id_records_fk_property_name_upload_put(id, fk, property_name, data=data)

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
property_name = 'property_name_example' # str | Model property name
data = TweakApi.DynamicData() # DynamicData | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.dynamic_data_id_records_fk_property_name_upload_put(id, fk, property_name, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicDataApi->dynamic_data_id_records_fk_property_name_upload_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DynamicData id | 
 **fk** | **str**| Model id | 
 **property_name** | **str**| Model property name | 
 **data** | [**DynamicData**](DynamicData.md)| Model instance data | [optional] 

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

