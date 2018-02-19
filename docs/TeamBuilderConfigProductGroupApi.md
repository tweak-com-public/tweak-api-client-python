# TweakApi.TeamBuilderConfigProductGroupApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_builder_config_product_groups_change_stream_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_change_stream_get) | **GET** /TeamBuilderConfigProductGroups/change-stream | Create a change stream.
[**team_builder_config_product_groups_change_stream_post**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_change_stream_post) | **POST** /TeamBuilderConfigProductGroups/change-stream | Create a change stream.
[**team_builder_config_product_groups_count_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_count_get) | **GET** /TeamBuilderConfigProductGroups/count | Count instances of the model matched by where from the data source.
[**team_builder_config_product_groups_find_one_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_find_one_get) | **GET** /TeamBuilderConfigProductGroups/findOne | Find first instance of the model matched by filter from the data source.
[**team_builder_config_product_groups_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_get) | **GET** /TeamBuilderConfigProductGroups | Find all instances of the model matched by filter from the data source.
[**team_builder_config_product_groups_id_builder_config_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_builder_config_get) | **GET** /TeamBuilderConfigProductGroups/{id}/builderConfig | Fetches belongsTo relation builderConfig.
[**team_builder_config_product_groups_id_delete**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_delete) | **DELETE** /TeamBuilderConfigProductGroups/{id} | Delete a model instance by {{id}} from the data source.
[**team_builder_config_product_groups_id_exists_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_exists_get) | **GET** /TeamBuilderConfigProductGroups/{id}/exists | Check whether a model instance exists in the data source.
[**team_builder_config_product_groups_id_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_get) | **GET** /TeamBuilderConfigProductGroups/{id} | Find a model instance by {{id}} from the data source.
[**team_builder_config_product_groups_id_head**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_head) | **HEAD** /TeamBuilderConfigProductGroups/{id} | Check whether a model instance exists in the data source.
[**team_builder_config_product_groups_id_patch**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_patch) | **PATCH** /TeamBuilderConfigProductGroups/{id} | Patch attributes for a model instance and persist it into the data source.
[**team_builder_config_product_groups_id_product_group_get**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_product_group_get) | **GET** /TeamBuilderConfigProductGroups/{id}/productGroup | Fetches belongsTo relation productGroup.
[**team_builder_config_product_groups_id_put**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_put) | **PUT** /TeamBuilderConfigProductGroups/{id} | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_groups_id_replace_post**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_id_replace_post) | **POST** /TeamBuilderConfigProductGroups/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_groups_post**](TeamBuilderConfigProductGroupApi.md#team_builder_config_product_groups_post) | **POST** /TeamBuilderConfigProductGroups | Create a new instance of the model and persist it into the data source.


# **team_builder_config_product_groups_change_stream_get**
> file team_builder_config_product_groups_change_stream_get(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_groups_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_change_stream_get: %s\n" % e)
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

# **team_builder_config_product_groups_change_stream_post**
> file team_builder_config_product_groups_change_stream_post(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_groups_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_change_stream_post: %s\n" % e)
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

# **team_builder_config_product_groups_count_get**
> InlineResponse2001 team_builder_config_product_groups_count_get(where=where)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.team_builder_config_product_groups_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_count_get: %s\n" % e)
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

# **team_builder_config_product_groups_find_one_get**
> TeamBuilderConfigProductGroup team_builder_config_product_groups_find_one_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_groups_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_get**
> list[TeamBuilderConfigProductGroup] team_builder_config_product_groups_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_groups_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamBuilderConfigProductGroup]**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_id_builder_config_get**
> TeamBuilderConfig team_builder_config_product_groups_id_builder_config_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | TeamBuilderConfigProductGroup id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation builderConfig.
    api_response = api_instance.team_builder_config_product_groups_id_builder_config_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_builder_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductGroup id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_id_delete**
> object team_builder_config_product_groups_id_delete(id)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_groups_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_delete: %s\n" % e)
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

# **team_builder_config_product_groups_id_exists_get**
> InlineResponse2002 team_builder_config_product_groups_id_exists_get(id)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_groups_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_exists_get: %s\n" % e)
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

# **team_builder_config_product_groups_id_get**
> TeamBuilderConfigProductGroup team_builder_config_product_groups_id_get(id, filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_groups_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_id_head**
> InlineResponse2002 team_builder_config_product_groups_id_head(id)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_groups_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_head: %s\n" % e)
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

# **team_builder_config_product_groups_id_patch**
> TeamBuilderConfigProductGroup team_builder_config_product_groups_id_patch(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | TeamBuilderConfigProductGroup id
data = TweakApi.TeamBuilderConfigProductGroup() # TeamBuilderConfigProductGroup | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_groups_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductGroup id | 
 **data** | [**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_id_product_group_get**
> ProductGroup team_builder_config_product_groups_id_product_group_get(id, refresh=refresh)

Fetches belongsTo relation productGroup.

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | TeamBuilderConfigProductGroup id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation productGroup.
    api_response = api_instance.team_builder_config_product_groups_id_product_group_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_product_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductGroup id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_id_put**
> TeamBuilderConfigProductGroup team_builder_config_product_groups_id_put(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductGroup() # TeamBuilderConfigProductGroup | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_groups_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_id_replace_post**
> TeamBuilderConfigProductGroup team_builder_config_product_groups_id_replace_post(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductGroup() # TeamBuilderConfigProductGroup | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_groups_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_groups_post**
> TeamBuilderConfigProductGroup team_builder_config_product_groups_post(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductGroupApi()
data = TweakApi.TeamBuilderConfigProductGroup() # TeamBuilderConfigProductGroup | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.team_builder_config_product_groups_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductGroupApi->team_builder_config_product_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

