# TweakApi.ProductSizeMaterialApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_size_materials_change_stream_get**](ProductSizeMaterialApi.md#product_size_materials_change_stream_get) | **GET** /ProductSizeMaterials/change-stream | Create a change stream.
[**product_size_materials_change_stream_post**](ProductSizeMaterialApi.md#product_size_materials_change_stream_post) | **POST** /ProductSizeMaterials/change-stream | Create a change stream.
[**product_size_materials_count_get**](ProductSizeMaterialApi.md#product_size_materials_count_get) | **GET** /ProductSizeMaterials/count | Count instances of the model matched by where from the data source.
[**product_size_materials_find_one_get**](ProductSizeMaterialApi.md#product_size_materials_find_one_get) | **GET** /ProductSizeMaterials/findOne | Find first instance of the model matched by filter from the data source.
[**product_size_materials_get**](ProductSizeMaterialApi.md#product_size_materials_get) | **GET** /ProductSizeMaterials | Find all instances of the model matched by filter from the data source.
[**product_size_materials_id_delete**](ProductSizeMaterialApi.md#product_size_materials_id_delete) | **DELETE** /ProductSizeMaterials/{id} | Delete a model instance by {{id}} from the data source.
[**product_size_materials_id_exists_get**](ProductSizeMaterialApi.md#product_size_materials_id_exists_get) | **GET** /ProductSizeMaterials/{id}/exists | Check whether a model instance exists in the data source.
[**product_size_materials_id_get**](ProductSizeMaterialApi.md#product_size_materials_id_get) | **GET** /ProductSizeMaterials/{id} | Find a model instance by {{id}} from the data source.
[**product_size_materials_id_head**](ProductSizeMaterialApi.md#product_size_materials_id_head) | **HEAD** /ProductSizeMaterials/{id} | Check whether a model instance exists in the data source.
[**product_size_materials_id_material_get**](ProductSizeMaterialApi.md#product_size_materials_id_material_get) | **GET** /ProductSizeMaterials/{id}/material | Fetches belongsTo relation material.
[**product_size_materials_id_patch**](ProductSizeMaterialApi.md#product_size_materials_id_patch) | **PATCH** /ProductSizeMaterials/{id} | Patch attributes for a model instance and persist it into the data source.
[**product_size_materials_id_pdf_color_profile_get**](ProductSizeMaterialApi.md#product_size_materials_id_pdf_color_profile_get) | **GET** /ProductSizeMaterials/{id}/pdfColorProfile | Fetches belongsTo relation pdfColorProfile.
[**product_size_materials_id_put**](ProductSizeMaterialApi.md#product_size_materials_id_put) | **PUT** /ProductSizeMaterials/{id} | Replace attributes for a model instance and persist it into the data source.
[**product_size_materials_id_replace_post**](ProductSizeMaterialApi.md#product_size_materials_id_replace_post) | **POST** /ProductSizeMaterials/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**product_size_materials_id_size_get**](ProductSizeMaterialApi.md#product_size_materials_id_size_get) | **GET** /ProductSizeMaterials/{id}/size | Fetches belongsTo relation size.
[**product_size_materials_id_team_get**](ProductSizeMaterialApi.md#product_size_materials_id_team_get) | **GET** /ProductSizeMaterials/{id}/team | Fetches belongsTo relation team.
[**product_size_materials_patch**](ProductSizeMaterialApi.md#product_size_materials_patch) | **PATCH** /ProductSizeMaterials | Patch an existing model instance or insert a new one into the data source.
[**product_size_materials_post**](ProductSizeMaterialApi.md#product_size_materials_post) | **POST** /ProductSizeMaterials | Create a new instance of the model and persist it into the data source.
[**product_size_materials_put**](ProductSizeMaterialApi.md#product_size_materials_put) | **PUT** /ProductSizeMaterials | Replace an existing model instance or insert a new one into the data source.
[**product_size_materials_replace_or_create_post**](ProductSizeMaterialApi.md#product_size_materials_replace_or_create_post) | **POST** /ProductSizeMaterials/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**product_size_materials_update_post**](ProductSizeMaterialApi.md#product_size_materials_update_post) | **POST** /ProductSizeMaterials/update | Update instances of the model matched by {{where}} from the data source.
[**product_size_materials_upsert_with_where_post**](ProductSizeMaterialApi.md#product_size_materials_upsert_with_where_post) | **POST** /ProductSizeMaterials/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **product_size_materials_change_stream_get**
> file product_size_materials_change_stream_get(options=options)

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
api_instance = TweakApi.ProductSizeMaterialApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_size_materials_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_change_stream_get: %s\n" % e)
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

# **product_size_materials_change_stream_post**
> file product_size_materials_change_stream_post(options=options)

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
api_instance = TweakApi.ProductSizeMaterialApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_size_materials_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_change_stream_post: %s\n" % e)
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

# **product_size_materials_count_get**
> InlineResponse200 product_size_materials_count_get(where=where)

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
api_instance = TweakApi.ProductSizeMaterialApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.product_size_materials_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_count_get: %s\n" % e)
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

# **product_size_materials_find_one_get**
> ProductSizeMaterial product_size_materials_find_one_get(filter=filter)

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
api_instance = TweakApi.ProductSizeMaterialApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.product_size_materials_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_get**
> list[ProductSizeMaterial] product_size_materials_get(filter=filter)

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
api_instance = TweakApi.ProductSizeMaterialApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.product_size_materials_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_delete**
> object product_size_materials_id_delete(id)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.product_size_materials_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_delete: %s\n" % e)
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

# **product_size_materials_id_exists_get**
> InlineResponse2001 product_size_materials_id_exists_get(id)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_size_materials_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_exists_get: %s\n" % e)
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

# **product_size_materials_id_get**
> ProductSizeMaterial product_size_materials_id_get(id, filter=filter)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.product_size_materials_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_head**
> InlineResponse2001 product_size_materials_id_head(id)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_size_materials_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_head: %s\n" % e)
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

# **product_size_materials_id_material_get**
> ProductMaterial product_size_materials_id_material_get(id, refresh=refresh)

Fetches belongsTo relation material.

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | ProductSizeMaterial id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation material.
    api_response = api_instance.product_size_materials_id_material_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_material_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSizeMaterial id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_patch**
> ProductSizeMaterial product_size_materials_id_patch(id, data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | ProductSizeMaterial id
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_size_materials_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSizeMaterial id | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_pdf_color_profile_get**
> ProductPdfColorProfile product_size_materials_id_pdf_color_profile_get(id, refresh=refresh)

Fetches belongsTo relation pdfColorProfile.

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | ProductSizeMaterial id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation pdfColorProfile.
    api_response = api_instance.product_size_materials_id_pdf_color_profile_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_pdf_color_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSizeMaterial id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_put**
> ProductSizeMaterial product_size_materials_id_put(id, data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_size_materials_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_replace_post**
> ProductSizeMaterial product_size_materials_id_replace_post(id, data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_size_materials_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_size_get**
> ProductSize product_size_materials_id_size_get(id, refresh=refresh)

Fetches belongsTo relation size.

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | ProductSizeMaterial id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation size.
    api_response = api_instance.product_size_materials_id_size_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSizeMaterial id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_id_team_get**
> Team product_size_materials_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.ProductSizeMaterialApi()
id = 'id_example' # str | ProductSizeMaterial id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.product_size_materials_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSizeMaterial id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_patch**
> ProductSizeMaterial product_size_materials_patch(data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.product_size_materials_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_post**
> ProductSizeMaterial product_size_materials_post(data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.product_size_materials_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_put**
> ProductSizeMaterial product_size_materials_put(data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.product_size_materials_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_replace_or_create_post**
> ProductSizeMaterial product_size_materials_replace_or_create_post(data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.product_size_materials_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_update_post**
> InlineResponse2002 product_size_materials_update_post(where=where, data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.product_size_materials_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_size_materials_upsert_with_where_post**
> ProductSizeMaterial product_size_materials_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.ProductSizeMaterialApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.product_size_materials_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeMaterialApi->product_size_materials_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

