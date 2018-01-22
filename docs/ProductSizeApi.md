# TweakApi.ProductSizeApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_sizes_change_stream_get**](ProductSizeApi.md#product_sizes_change_stream_get) | **GET** /ProductSizes/change-stream | Create a change stream.
[**product_sizes_change_stream_post**](ProductSizeApi.md#product_sizes_change_stream_post) | **POST** /ProductSizes/change-stream | Create a change stream.
[**product_sizes_count_get**](ProductSizeApi.md#product_sizes_count_get) | **GET** /ProductSizes/count | Count instances of the model matched by where from the data source.
[**product_sizes_find_one_get**](ProductSizeApi.md#product_sizes_find_one_get) | **GET** /ProductSizes/findOne | Find first instance of the model matched by filter from the data source.
[**product_sizes_get**](ProductSizeApi.md#product_sizes_get) | **GET** /ProductSizes | Find all instances of the model matched by filter from the data source.
[**product_sizes_id_delete**](ProductSizeApi.md#product_sizes_id_delete) | **DELETE** /ProductSizes/{id} | Delete a model instance by {{id}} from the data source.
[**product_sizes_id_exists_get**](ProductSizeApi.md#product_sizes_id_exists_get) | **GET** /ProductSizes/{id}/exists | Check whether a model instance exists in the data source.
[**product_sizes_id_get**](ProductSizeApi.md#product_sizes_id_get) | **GET** /ProductSizes/{id} | Find a model instance by {{id}} from the data source.
[**product_sizes_id_head**](ProductSizeApi.md#product_sizes_id_head) | **HEAD** /ProductSizes/{id} | Check whether a model instance exists in the data source.
[**product_sizes_id_materials_count_get**](ProductSizeApi.md#product_sizes_id_materials_count_get) | **GET** /ProductSizes/{id}/materials/count | Counts materials of ProductSize.
[**product_sizes_id_materials_delete**](ProductSizeApi.md#product_sizes_id_materials_delete) | **DELETE** /ProductSizes/{id}/materials | Deletes all materials of this model.
[**product_sizes_id_materials_fk_delete**](ProductSizeApi.md#product_sizes_id_materials_fk_delete) | **DELETE** /ProductSizes/{id}/materials/{fk} | Delete a related item by id for materials.
[**product_sizes_id_materials_fk_get**](ProductSizeApi.md#product_sizes_id_materials_fk_get) | **GET** /ProductSizes/{id}/materials/{fk} | Find a related item by id for materials.
[**product_sizes_id_materials_fk_put**](ProductSizeApi.md#product_sizes_id_materials_fk_put) | **PUT** /ProductSizes/{id}/materials/{fk} | Update a related item by id for materials.
[**product_sizes_id_materials_get**](ProductSizeApi.md#product_sizes_id_materials_get) | **GET** /ProductSizes/{id}/materials | Queries materials of ProductSize.
[**product_sizes_id_materials_post**](ProductSizeApi.md#product_sizes_id_materials_post) | **POST** /ProductSizes/{id}/materials | Creates a new instance in materials of this model.
[**product_sizes_id_materials_rel_fk_delete**](ProductSizeApi.md#product_sizes_id_materials_rel_fk_delete) | **DELETE** /ProductSizes/{id}/materials/rel/{fk} | Remove the materials relation to an item by id.
[**product_sizes_id_materials_rel_fk_head**](ProductSizeApi.md#product_sizes_id_materials_rel_fk_head) | **HEAD** /ProductSizes/{id}/materials/rel/{fk} | Check the existence of materials relation to an item by id.
[**product_sizes_id_materials_rel_fk_put**](ProductSizeApi.md#product_sizes_id_materials_rel_fk_put) | **PUT** /ProductSizes/{id}/materials/rel/{fk} | Add a related item by id for materials.
[**product_sizes_id_patch**](ProductSizeApi.md#product_sizes_id_patch) | **PATCH** /ProductSizes/{id} | Patch attributes for a model instance and persist it into the data source.
[**product_sizes_id_pdf_color_profile_get**](ProductSizeApi.md#product_sizes_id_pdf_color_profile_get) | **GET** /ProductSizes/{id}/pdfColorProfile | Fetches belongsTo relation pdfColorProfile.
[**product_sizes_id_products_count_get**](ProductSizeApi.md#product_sizes_id_products_count_get) | **GET** /ProductSizes/{id}/products/count | Counts products of ProductSize.
[**product_sizes_id_products_delete**](ProductSizeApi.md#product_sizes_id_products_delete) | **DELETE** /ProductSizes/{id}/products | Deletes all products of this model.
[**product_sizes_id_products_fk_delete**](ProductSizeApi.md#product_sizes_id_products_fk_delete) | **DELETE** /ProductSizes/{id}/products/{fk} | Delete a related item by id for products.
[**product_sizes_id_products_fk_get**](ProductSizeApi.md#product_sizes_id_products_fk_get) | **GET** /ProductSizes/{id}/products/{fk} | Find a related item by id for products.
[**product_sizes_id_products_fk_put**](ProductSizeApi.md#product_sizes_id_products_fk_put) | **PUT** /ProductSizes/{id}/products/{fk} | Update a related item by id for products.
[**product_sizes_id_products_get**](ProductSizeApi.md#product_sizes_id_products_get) | **GET** /ProductSizes/{id}/products | Queries products of ProductSize.
[**product_sizes_id_products_post**](ProductSizeApi.md#product_sizes_id_products_post) | **POST** /ProductSizes/{id}/products | Creates a new instance in products of this model.
[**product_sizes_id_put**](ProductSizeApi.md#product_sizes_id_put) | **PUT** /ProductSizes/{id} | Replace attributes for a model instance and persist it into the data source.
[**product_sizes_id_replace_post**](ProductSizeApi.md#product_sizes_id_replace_post) | **POST** /ProductSizes/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**product_sizes_id_size_materials_count_get**](ProductSizeApi.md#product_sizes_id_size_materials_count_get) | **GET** /ProductSizes/{id}/sizeMaterials/count | Counts sizeMaterials of ProductSize.
[**product_sizes_id_size_materials_delete**](ProductSizeApi.md#product_sizes_id_size_materials_delete) | **DELETE** /ProductSizes/{id}/sizeMaterials | Deletes all sizeMaterials of this model.
[**product_sizes_id_size_materials_fk_delete**](ProductSizeApi.md#product_sizes_id_size_materials_fk_delete) | **DELETE** /ProductSizes/{id}/sizeMaterials/{fk} | Delete a related item by id for sizeMaterials.
[**product_sizes_id_size_materials_fk_get**](ProductSizeApi.md#product_sizes_id_size_materials_fk_get) | **GET** /ProductSizes/{id}/sizeMaterials/{fk} | Find a related item by id for sizeMaterials.
[**product_sizes_id_size_materials_fk_put**](ProductSizeApi.md#product_sizes_id_size_materials_fk_put) | **PUT** /ProductSizes/{id}/sizeMaterials/{fk} | Update a related item by id for sizeMaterials.
[**product_sizes_id_size_materials_get**](ProductSizeApi.md#product_sizes_id_size_materials_get) | **GET** /ProductSizes/{id}/sizeMaterials | Queries sizeMaterials of ProductSize.
[**product_sizes_id_size_materials_post**](ProductSizeApi.md#product_sizes_id_size_materials_post) | **POST** /ProductSizes/{id}/sizeMaterials | Creates a new instance in sizeMaterials of this model.
[**product_sizes_id_type_get**](ProductSizeApi.md#product_sizes_id_type_get) | **GET** /ProductSizes/{id}/type | Fetches belongsTo relation type.
[**product_sizes_patch**](ProductSizeApi.md#product_sizes_patch) | **PATCH** /ProductSizes | Patch an existing model instance or insert a new one into the data source.
[**product_sizes_post**](ProductSizeApi.md#product_sizes_post) | **POST** /ProductSizes | Create a new instance of the model and persist it into the data source.
[**product_sizes_put**](ProductSizeApi.md#product_sizes_put) | **PUT** /ProductSizes | Replace an existing model instance or insert a new one into the data source.
[**product_sizes_replace_or_create_post**](ProductSizeApi.md#product_sizes_replace_or_create_post) | **POST** /ProductSizes/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**product_sizes_update_post**](ProductSizeApi.md#product_sizes_update_post) | **POST** /ProductSizes/update | Update instances of the model matched by {{where}} from the data source.
[**product_sizes_upsert_with_where_post**](ProductSizeApi.md#product_sizes_upsert_with_where_post) | **POST** /ProductSizes/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **product_sizes_change_stream_get**
> file product_sizes_change_stream_get(options=options)

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
api_instance = TweakApi.ProductSizeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_sizes_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_change_stream_get: %s\n" % e)
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

# **product_sizes_change_stream_post**
> file product_sizes_change_stream_post(options=options)

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
api_instance = TweakApi.ProductSizeApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.product_sizes_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_change_stream_post: %s\n" % e)
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

# **product_sizes_count_get**
> InlineResponse2001 product_sizes_count_get(where=where)

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
api_instance = TweakApi.ProductSizeApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.product_sizes_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_count_get: %s\n" % e)
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

# **product_sizes_find_one_get**
> ProductSize product_sizes_find_one_get(filter=filter)

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
api_instance = TweakApi.ProductSizeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.product_sizes_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_get**
> list[ProductSize] product_sizes_get(filter=filter)

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
api_instance = TweakApi.ProductSizeApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.product_sizes_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ProductSize]**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_delete**
> object product_sizes_id_delete(id)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.product_sizes_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_delete: %s\n" % e)
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

# **product_sizes_id_exists_get**
> InlineResponse2002 product_sizes_id_exists_get(id)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_sizes_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_exists_get: %s\n" % e)
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

# **product_sizes_id_get**
> ProductSize product_sizes_id_get(id, filter=filter)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.product_sizes_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_head**
> InlineResponse2002 product_sizes_id_head(id)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.product_sizes_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_head: %s\n" % e)
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

# **product_sizes_id_materials_count_get**
> InlineResponse2001 product_sizes_id_materials_count_get(id, where=where)

Counts materials of ProductSize.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts materials of ProductSize.
    api_response = api_instance.product_sizes_id_materials_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_delete**
> product_sizes_id_materials_delete(id)

Deletes all materials of this model.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id

try: 
    # Deletes all materials of this model.
    api_instance.product_sizes_id_materials_delete(id)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_fk_delete**
> product_sizes_id_materials_fk_delete(id, fk)

Delete a related item by id for materials.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Delete a related item by id for materials.
    api_instance.product_sizes_id_materials_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for materials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_fk_get**
> ProductMaterial product_sizes_id_materials_fk_get(id, fk)

Find a related item by id for materials.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Find a related item by id for materials.
    api_response = api_instance.product_sizes_id_materials_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for materials | 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_fk_put**
> ProductMaterial product_sizes_id_materials_fk_put(id, fk, data=data)

Update a related item by id for materials.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for materials
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Update a related item by id for materials.
    api_response = api_instance.product_sizes_id_materials_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for materials | 
 **data** | [**ProductMaterial**](ProductMaterial.md)|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_get**
> list[ProductMaterial] product_sizes_id_materials_get(id, filter=filter)

Queries materials of ProductSize.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries materials of ProductSize.
    api_response = api_instance.product_sizes_id_materials_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductMaterial]**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_post**
> ProductMaterial product_sizes_id_materials_post(id, data=data)

Creates a new instance in materials of this model.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Creates a new instance in materials of this model.
    api_response = api_instance.product_sizes_id_materials_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **data** | [**ProductMaterial**](ProductMaterial.md)|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_rel_fk_delete**
> product_sizes_id_materials_rel_fk_delete(id, fk)

Remove the materials relation to an item by id.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Remove the materials relation to an item by id.
    api_instance.product_sizes_id_materials_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for materials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_rel_fk_head**
> bool product_sizes_id_materials_rel_fk_head(id, fk)

Check the existence of materials relation to an item by id.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Check the existence of materials relation to an item by id.
    api_response = api_instance.product_sizes_id_materials_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for materials | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_materials_rel_fk_put**
> ProductSizeMaterial product_sizes_id_materials_rel_fk_put(id, fk, data=data)

Add a related item by id for materials.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for materials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Add a related item by id for materials.
    api_response = api_instance.product_sizes_id_materials_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_materials_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for materials | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_patch**
> ProductSize product_sizes_id_patch(id, data=data)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
data = TweakApi.ProductSize() # ProductSize | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_sizes_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **data** | [**ProductSize**](ProductSize.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_pdf_color_profile_get**
> ProductPdfColorProfile product_sizes_id_pdf_color_profile_get(id, refresh=refresh)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation pdfColorProfile.
    api_response = api_instance.product_sizes_id_pdf_color_profile_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_pdf_color_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_products_count_get**
> InlineResponse2001 product_sizes_id_products_count_get(id, where=where)

Counts products of ProductSize.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts products of ProductSize.
    api_response = api_instance.product_sizes_id_products_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_products_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_products_delete**
> product_sizes_id_products_delete(id)

Deletes all products of this model.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id

try: 
    # Deletes all products of this model.
    api_instance.product_sizes_id_products_delete(id)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_products_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_products_fk_delete**
> product_sizes_id_products_fk_delete(id, fk)

Delete a related item by id for products.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for products

try: 
    # Delete a related item by id for products.
    api_instance.product_sizes_id_products_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_products_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for products | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_products_fk_get**
> Product product_sizes_id_products_fk_get(id, fk)

Find a related item by id for products.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for products

try: 
    # Find a related item by id for products.
    api_response = api_instance.product_sizes_id_products_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_products_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for products | 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_products_fk_put**
> Product product_sizes_id_products_fk_put(id, fk, data=data)

Update a related item by id for products.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for products
data = TweakApi.Product() # Product |  (optional)

try: 
    # Update a related item by id for products.
    api_response = api_instance.product_sizes_id_products_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_products_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for products | 
 **data** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_products_get**
> list[Product] product_sizes_id_products_get(id, filter=filter)

Queries products of ProductSize.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries products of ProductSize.
    api_response = api_instance.product_sizes_id_products_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Product]**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_products_post**
> Product product_sizes_id_products_post(id, data=data)

Creates a new instance in products of this model.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
data = TweakApi.Product() # Product |  (optional)

try: 
    # Creates a new instance in products of this model.
    api_response = api_instance.product_sizes_id_products_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **data** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_put**
> ProductSize product_sizes_id_put(id, data=data)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductSize() # ProductSize | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_sizes_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductSize**](ProductSize.md)| Model instance data | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_replace_post**
> ProductSize product_sizes_id_replace_post(id, data=data)

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | Model id
data = TweakApi.ProductSize() # ProductSize | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.product_sizes_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**ProductSize**](ProductSize.md)| Model instance data | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_size_materials_count_get**
> InlineResponse2001 product_sizes_id_size_materials_count_get(id, where=where)

Counts sizeMaterials of ProductSize.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts sizeMaterials of ProductSize.
    api_response = api_instance.product_sizes_id_size_materials_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_size_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_size_materials_delete**
> product_sizes_id_size_materials_delete(id)

Deletes all sizeMaterials of this model.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id

try: 
    # Deletes all sizeMaterials of this model.
    api_instance.product_sizes_id_size_materials_delete(id)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_size_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_size_materials_fk_delete**
> product_sizes_id_size_materials_fk_delete(id, fk)

Delete a related item by id for sizeMaterials.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for sizeMaterials

try: 
    # Delete a related item by id for sizeMaterials.
    api_instance.product_sizes_id_size_materials_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_size_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for sizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_size_materials_fk_get**
> ProductSizeMaterial product_sizes_id_size_materials_fk_get(id, fk)

Find a related item by id for sizeMaterials.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for sizeMaterials

try: 
    # Find a related item by id for sizeMaterials.
    api_response = api_instance.product_sizes_id_size_materials_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_size_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for sizeMaterials | 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_size_materials_fk_put**
> ProductSizeMaterial product_sizes_id_size_materials_fk_put(id, fk, data=data)

Update a related item by id for sizeMaterials.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
fk = 'fk_example' # str | Foreign key for sizeMaterials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for sizeMaterials.
    api_response = api_instance.product_sizes_id_size_materials_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_size_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **fk** | **str**| Foreign key for sizeMaterials | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_size_materials_get**
> list[ProductSizeMaterial] product_sizes_id_size_materials_get(id, filter=filter)

Queries sizeMaterials of ProductSize.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries sizeMaterials of ProductSize.
    api_response = api_instance.product_sizes_id_size_materials_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_size_materials_post**
> ProductSizeMaterial product_sizes_id_size_materials_post(id, data=data)

Creates a new instance in sizeMaterials of this model.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in sizeMaterials of this model.
    api_response = api_instance.product_sizes_id_size_materials_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_id_type_get**
> ProductType product_sizes_id_type_get(id, refresh=refresh)

Fetches belongsTo relation type.

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
api_instance = TweakApi.ProductSizeApi()
id = 'id_example' # str | ProductSize id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation type.
    api_response = api_instance.product_sizes_id_type_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_id_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ProductSize id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_patch**
> ProductSize product_sizes_patch(data=data)

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
api_instance = TweakApi.ProductSizeApi()
data = TweakApi.ProductSize() # ProductSize | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.product_sizes_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSize**](ProductSize.md)| Model instance data | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_post**
> ProductSize product_sizes_post(data=data)

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
api_instance = TweakApi.ProductSizeApi()
data = TweakApi.ProductSize() # ProductSize | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.product_sizes_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSize**](ProductSize.md)| Model instance data | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_put**
> ProductSize product_sizes_put(data=data)

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
api_instance = TweakApi.ProductSizeApi()
data = TweakApi.ProductSize() # ProductSize | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.product_sizes_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSize**](ProductSize.md)| Model instance data | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_replace_or_create_post**
> ProductSize product_sizes_replace_or_create_post(data=data)

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
api_instance = TweakApi.ProductSizeApi()
data = TweakApi.ProductSize() # ProductSize | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.product_sizes_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductSize**](ProductSize.md)| Model instance data | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_update_post**
> InlineResponse2003 product_sizes_update_post(where=where, data=data)

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
api_instance = TweakApi.ProductSizeApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ProductSize() # ProductSize | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.product_sizes_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ProductSize**](ProductSize.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_sizes_upsert_with_where_post**
> ProductSize product_sizes_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.ProductSizeApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.ProductSize() # ProductSize | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.product_sizes_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSizeApi->product_sizes_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**ProductSize**](ProductSize.md)| An object of model property name/value pairs | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

