# TweakApi.ProductPdfColorProfileApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_pdf_color_profiles_change_stream_get**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_change_stream_get) | **GET** /ProductPdfColorProfiles/change-stream | Create a change stream.
[**product_pdf_color_profiles_change_stream_post**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_change_stream_post) | **POST** /ProductPdfColorProfiles/change-stream | Create a change stream.
[**product_pdf_color_profiles_count_get**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_count_get) | **GET** /ProductPdfColorProfiles/count | Count instances of the model matched by where from the data source.
[**product_pdf_color_profiles_find_one_get**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_find_one_get) | **GET** /ProductPdfColorProfiles/findOne | Find first instance of the model matched by filter from the data source.
[**product_pdf_color_profiles_get**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_get) | **GET** /ProductPdfColorProfiles | Find all instances of the model matched by filter from the data source.
[**product_pdf_color_profiles_id_delete**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_delete) | **DELETE** /ProductPdfColorProfiles/{id} | Delete a model instance by {{id}} from the data source.
[**product_pdf_color_profiles_id_exists_get**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_exists_get) | **GET** /ProductPdfColorProfiles/{id}/exists | Check whether a model instance exists in the data source.
[**product_pdf_color_profiles_id_get**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_get) | **GET** /ProductPdfColorProfiles/{id} | Find a model instance by {{id}} from the data source.
[**product_pdf_color_profiles_id_head**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_head) | **HEAD** /ProductPdfColorProfiles/{id} | Check whether a model instance exists in the data source.
[**product_pdf_color_profiles_id_patch**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_patch) | **PATCH** /ProductPdfColorProfiles/{id} | Patch attributes for a model instance and persist it into the data source.
[**product_pdf_color_profiles_id_put**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_put) | **PUT** /ProductPdfColorProfiles/{id} | Replace attributes for a model instance and persist it into the data source.
[**product_pdf_color_profiles_id_replace_post**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_replace_post) | **POST** /ProductPdfColorProfiles/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**product_pdf_color_profiles_id_team_get**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_id_team_get) | **GET** /ProductPdfColorProfiles/{id}/team | Fetches belongsTo relation team.
[**product_pdf_color_profiles_post**](ProductPdfColorProfileApi.md#product_pdf_color_profiles_post) | **POST** /ProductPdfColorProfiles | Create a new instance of the model and persist it into the data source.


# **product_pdf_color_profiles_change_stream_get**
> file product_pdf_color_profiles_change_stream_get(options=options)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_pdf_color_profiles_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_change_stream_get: %s\n" % e)
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

# **product_pdf_color_profiles_change_stream_post**
> file product_pdf_color_profiles_change_stream_post(options=options)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_pdf_color_profiles_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_change_stream_post: %s\n" % e)
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

# **product_pdf_color_profiles_count_get**
> InlineResponse2001 product_pdf_color_profiles_count_get(where=where)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.product_pdf_color_profiles_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_count_get: %s\n" % e)
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

# **product_pdf_color_profiles_find_one_get**
> ProductPdfColorProfile product_pdf_color_profiles_find_one_get(filter=filter)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.product_pdf_color_profiles_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_pdf_color_profiles_get**
> list[ProductPdfColorProfile] product_pdf_color_profiles_get(filter=filter)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.product_pdf_color_profiles_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ProductPdfColorProfile]**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_pdf_color_profiles_id_delete**
> object product_pdf_color_profiles_id_delete(id)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.product_pdf_color_profiles_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_delete: %s\n" % e)
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

# **product_pdf_color_profiles_id_exists_get**
> InlineResponse2002 product_pdf_color_profiles_id_exists_get(id)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_pdf_color_profiles_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_exists_get: %s\n" % e)
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

# **product_pdf_color_profiles_id_get**
> ProductPdfColorProfile product_pdf_color_profiles_id_get(id, filter=filter)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.product_pdf_color_profiles_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_pdf_color_profiles_id_head**
> InlineResponse2002 product_pdf_color_profiles_id_head(id)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_pdf_color_profiles_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_head: %s\n" % e)
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

# **product_pdf_color_profiles_id_patch**
> ProductPdfColorProfile product_pdf_color_profiles_id_patch(id, data=data)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | ProductPdfColorProfile id
data = TweakApi.ProductPdfColorProfile() # ProductPdfColorProfile | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_pdf_color_profiles_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductPdfColorProfile id | 
 **data** | [**ProductPdfColorProfile**](ProductPdfColorProfile.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_pdf_color_profiles_id_put**
> ProductPdfColorProfile product_pdf_color_profiles_id_put(id, data=data)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductPdfColorProfile() # ProductPdfColorProfile | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_pdf_color_profiles_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductPdfColorProfile**](ProductPdfColorProfile.md)| Model instance data | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_pdf_color_profiles_id_replace_post**
> ProductPdfColorProfile product_pdf_color_profiles_id_replace_post(id, data=data)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductPdfColorProfile() # ProductPdfColorProfile | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_pdf_color_profiles_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductPdfColorProfile**](ProductPdfColorProfile.md)| Model instance data | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_pdf_color_profiles_id_team_get**
> Team product_pdf_color_profiles_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
id = 'id_example' # str | ProductPdfColorProfile id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.product_pdf_color_profiles_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductPdfColorProfile id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_pdf_color_profiles_post**
> ProductPdfColorProfile product_pdf_color_profiles_post(data=data)

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
api_instance = TweakApi.ProductPdfColorProfileApi()
data = TweakApi.ProductPdfColorProfile() # ProductPdfColorProfile | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.product_pdf_color_profiles_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPdfColorProfileApi->product_pdf_color_profiles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductPdfColorProfile**](ProductPdfColorProfile.md)| Model instance data | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

