# TweakApi.TagApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_change_stream_get**](TagApi.md#tags_change_stream_get) | **GET** /Tags/change-stream | Create a change stream.
[**tags_change_stream_post**](TagApi.md#tags_change_stream_post) | **POST** /Tags/change-stream | Create a change stream.
[**tags_count_get**](TagApi.md#tags_count_get) | **GET** /Tags/count | Count instances of the model matched by where from the data source.
[**tags_find_one_get**](TagApi.md#tags_find_one_get) | **GET** /Tags/findOne | Find first instance of the model matched by filter from the data source.
[**tags_get**](TagApi.md#tags_get) | **GET** /Tags | Find all instances of the model matched by filter from the data source.
[**tags_id_delete**](TagApi.md#tags_id_delete) | **DELETE** /Tags/{id} | Delete a model instance by {{id}} from the data source.
[**tags_id_designs_count_get**](TagApi.md#tags_id_designs_count_get) | **GET** /Tags/{id}/designs/count | Counts designs of Tag.
[**tags_id_designs_delete**](TagApi.md#tags_id_designs_delete) | **DELETE** /Tags/{id}/designs | Deletes all designs of this model.
[**tags_id_designs_fk_delete**](TagApi.md#tags_id_designs_fk_delete) | **DELETE** /Tags/{id}/designs/{fk} | Delete a related item by id for designs.
[**tags_id_designs_fk_get**](TagApi.md#tags_id_designs_fk_get) | **GET** /Tags/{id}/designs/{fk} | Find a related item by id for designs.
[**tags_id_designs_fk_put**](TagApi.md#tags_id_designs_fk_put) | **PUT** /Tags/{id}/designs/{fk} | Update a related item by id for designs.
[**tags_id_designs_get**](TagApi.md#tags_id_designs_get) | **GET** /Tags/{id}/designs | Queries designs of Tag.
[**tags_id_designs_post**](TagApi.md#tags_id_designs_post) | **POST** /Tags/{id}/designs | Creates a new instance in designs of this model.
[**tags_id_designs_rel_fk_delete**](TagApi.md#tags_id_designs_rel_fk_delete) | **DELETE** /Tags/{id}/designs/rel/{fk} | Remove the designs relation to an item by id.
[**tags_id_designs_rel_fk_head**](TagApi.md#tags_id_designs_rel_fk_head) | **HEAD** /Tags/{id}/designs/rel/{fk} | Check the existence of designs relation to an item by id.
[**tags_id_designs_rel_fk_put**](TagApi.md#tags_id_designs_rel_fk_put) | **PUT** /Tags/{id}/designs/rel/{fk} | Add a related item by id for designs.
[**tags_id_exists_get**](TagApi.md#tags_id_exists_get) | **GET** /Tags/{id}/exists | Check whether a model instance exists in the data source.
[**tags_id_get**](TagApi.md#tags_id_get) | **GET** /Tags/{id} | Find a model instance by {{id}} from the data source.
[**tags_id_head**](TagApi.md#tags_id_head) | **HEAD** /Tags/{id} | Check whether a model instance exists in the data source.
[**tags_id_patch**](TagApi.md#tags_id_patch) | **PATCH** /Tags/{id} | Patch attributes for a model instance and persist it into the data source.
[**tags_id_products_count_get**](TagApi.md#tags_id_products_count_get) | **GET** /Tags/{id}/products/count | Counts products of Tag.
[**tags_id_products_delete**](TagApi.md#tags_id_products_delete) | **DELETE** /Tags/{id}/products | Deletes all products of this model.
[**tags_id_products_fk_delete**](TagApi.md#tags_id_products_fk_delete) | **DELETE** /Tags/{id}/products/{fk} | Delete a related item by id for products.
[**tags_id_products_fk_get**](TagApi.md#tags_id_products_fk_get) | **GET** /Tags/{id}/products/{fk} | Find a related item by id for products.
[**tags_id_products_fk_put**](TagApi.md#tags_id_products_fk_put) | **PUT** /Tags/{id}/products/{fk} | Update a related item by id for products.
[**tags_id_products_get**](TagApi.md#tags_id_products_get) | **GET** /Tags/{id}/products | Queries products of Tag.
[**tags_id_products_post**](TagApi.md#tags_id_products_post) | **POST** /Tags/{id}/products | Creates a new instance in products of this model.
[**tags_id_products_rel_fk_delete**](TagApi.md#tags_id_products_rel_fk_delete) | **DELETE** /Tags/{id}/products/rel/{fk} | Remove the products relation to an item by id.
[**tags_id_products_rel_fk_head**](TagApi.md#tags_id_products_rel_fk_head) | **HEAD** /Tags/{id}/products/rel/{fk} | Check the existence of products relation to an item by id.
[**tags_id_products_rel_fk_put**](TagApi.md#tags_id_products_rel_fk_put) | **PUT** /Tags/{id}/products/rel/{fk} | Add a related item by id for products.
[**tags_id_put**](TagApi.md#tags_id_put) | **PUT** /Tags/{id} | Replace attributes for a model instance and persist it into the data source.
[**tags_id_replace_post**](TagApi.md#tags_id_replace_post) | **POST** /Tags/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**tags_id_templates_count_get**](TagApi.md#tags_id_templates_count_get) | **GET** /Tags/{id}/templates/count | Counts templates of Tag.
[**tags_id_templates_delete**](TagApi.md#tags_id_templates_delete) | **DELETE** /Tags/{id}/templates | Deletes all templates of this model.
[**tags_id_templates_fk_delete**](TagApi.md#tags_id_templates_fk_delete) | **DELETE** /Tags/{id}/templates/{fk} | Delete a related item by id for templates.
[**tags_id_templates_fk_get**](TagApi.md#tags_id_templates_fk_get) | **GET** /Tags/{id}/templates/{fk} | Find a related item by id for templates.
[**tags_id_templates_fk_put**](TagApi.md#tags_id_templates_fk_put) | **PUT** /Tags/{id}/templates/{fk} | Update a related item by id for templates.
[**tags_id_templates_get**](TagApi.md#tags_id_templates_get) | **GET** /Tags/{id}/templates | Queries templates of Tag.
[**tags_id_templates_post**](TagApi.md#tags_id_templates_post) | **POST** /Tags/{id}/templates | Creates a new instance in templates of this model.
[**tags_id_templates_rel_fk_delete**](TagApi.md#tags_id_templates_rel_fk_delete) | **DELETE** /Tags/{id}/templates/rel/{fk} | Remove the templates relation to an item by id.
[**tags_id_templates_rel_fk_head**](TagApi.md#tags_id_templates_rel_fk_head) | **HEAD** /Tags/{id}/templates/rel/{fk} | Check the existence of templates relation to an item by id.
[**tags_id_templates_rel_fk_put**](TagApi.md#tags_id_templates_rel_fk_put) | **PUT** /Tags/{id}/templates/rel/{fk} | Add a related item by id for templates.
[**tags_patch**](TagApi.md#tags_patch) | **PATCH** /Tags | Patch an existing model instance or insert a new one into the data source.
[**tags_post**](TagApi.md#tags_post) | **POST** /Tags | Create a new instance of the model and persist it into the data source.
[**tags_put**](TagApi.md#tags_put) | **PUT** /Tags | Replace an existing model instance or insert a new one into the data source.
[**tags_replace_or_create_post**](TagApi.md#tags_replace_or_create_post) | **POST** /Tags/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**tags_update_post**](TagApi.md#tags_update_post) | **POST** /Tags/update | Update instances of the model matched by {{where}} from the data source.
[**tags_upsert_with_where_post**](TagApi.md#tags_upsert_with_where_post) | **POST** /Tags/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **tags_change_stream_get**
> file tags_change_stream_get(options=options)

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
api_instance = TweakApi.TagApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.tags_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_change_stream_get: %s\n" % e)
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

# **tags_change_stream_post**
> file tags_change_stream_post(options=options)

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
api_instance = TweakApi.TagApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.tags_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_change_stream_post: %s\n" % e)
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

# **tags_count_get**
> InlineResponse200 tags_count_get(where=where)

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
api_instance = TweakApi.TagApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.tags_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_count_get: %s\n" % e)
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

# **tags_find_one_get**
> Tag tags_find_one_get(filter=filter)

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
api_instance = TweakApi.TagApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.tags_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get**
> list[Tag] tags_get(filter=filter)

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
api_instance = TweakApi.TagApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.tags_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_delete**
> object tags_id_delete(id)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.tags_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_delete: %s\n" % e)
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

# **tags_id_designs_count_get**
> InlineResponse200 tags_id_designs_count_get(id, where=where)

Counts designs of Tag.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of Tag.
    api_response = api_instance.tags_id_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_delete**
> tags_id_designs_delete(id)

Deletes all designs of this model.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id

try: 
    # Deletes all designs of this model.
    api_instance.tags_id_designs_delete(id)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_fk_delete**
> tags_id_designs_fk_delete(id, fk)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.tags_id_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_fk_get**
> Design tags_id_designs_fk_get(id, fk)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.tags_id_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_fk_put**
> Design tags_id_designs_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.tags_id_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
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

# **tags_id_designs_get**
> list[Design] tags_id_designs_get(id, filter=filter)

Queries designs of Tag.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of Tag.
    api_response = api_instance.tags_id_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_post**
> Design tags_id_designs_post(id, data=data)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.tags_id_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_rel_fk_delete**
> tags_id_designs_rel_fk_delete(id, fk)

Remove the designs relation to an item by id.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Remove the designs relation to an item by id.
    api_instance.tags_id_designs_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_rel_fk_head**
> bool tags_id_designs_rel_fk_head(id, fk)

Check the existence of designs relation to an item by id.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Check the existence of designs relation to an item by id.
    api_response = api_instance.tags_id_designs_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_designs_rel_fk_put**
> DesignTag tags_id_designs_rel_fk_put(id, fk, data=data)

Add a related item by id for designs.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.DesignTag() # DesignTag |  (optional)

try: 
    # Add a related item by id for designs.
    api_response = api_instance.tags_id_designs_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_designs_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**DesignTag**](DesignTag.md)|  | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_exists_get**
> InlineResponse2001 tags_id_exists_get(id)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.tags_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_exists_get: %s\n" % e)
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

# **tags_id_get**
> Tag tags_id_get(id, filter=filter)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.tags_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_head**
> InlineResponse2001 tags_id_head(id)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.tags_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_head: %s\n" % e)
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

# **tags_id_patch**
> Tag tags_id_patch(id, data=data)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
data = TweakApi.Tag() # Tag | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.tags_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **data** | [**Tag**](Tag.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_count_get**
> InlineResponse200 tags_id_products_count_get(id, where=where)

Counts products of Tag.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts products of Tag.
    api_response = api_instance.tags_id_products_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_delete**
> tags_id_products_delete(id)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id

try: 
    # Deletes all products of this model.
    api_instance.tags_id_products_delete(id)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_fk_delete**
> tags_id_products_fk_delete(id, fk)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for products

try: 
    # Delete a related item by id for products.
    api_instance.tags_id_products_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for products | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_fk_get**
> Product tags_id_products_fk_get(id, fk)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for products

try: 
    # Find a related item by id for products.
    api_response = api_instance.tags_id_products_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for products | 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_fk_put**
> Product tags_id_products_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for products
data = TweakApi.Product() # Product |  (optional)

try: 
    # Update a related item by id for products.
    api_response = api_instance.tags_id_products_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
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

# **tags_id_products_get**
> list[Product] tags_id_products_get(id, filter=filter)

Queries products of Tag.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries products of Tag.
    api_response = api_instance.tags_id_products_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Product]**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_post**
> Product tags_id_products_post(id, data=data)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
data = TweakApi.Product() # Product |  (optional)

try: 
    # Creates a new instance in products of this model.
    api_response = api_instance.tags_id_products_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **data** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_rel_fk_delete**
> tags_id_products_rel_fk_delete(id, fk)

Remove the products relation to an item by id.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for products

try: 
    # Remove the products relation to an item by id.
    api_instance.tags_id_products_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for products | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_rel_fk_head**
> bool tags_id_products_rel_fk_head(id, fk)

Check the existence of products relation to an item by id.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for products

try: 
    # Check the existence of products relation to an item by id.
    api_response = api_instance.tags_id_products_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for products | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_products_rel_fk_put**
> ProductTag tags_id_products_rel_fk_put(id, fk, data=data)

Add a related item by id for products.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for products
data = TweakApi.ProductTag() # ProductTag |  (optional)

try: 
    # Add a related item by id for products.
    api_response = api_instance.tags_id_products_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_products_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for products | 
 **data** | [**ProductTag**](ProductTag.md)|  | [optional] 

### Return type

[**ProductTag**](ProductTag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_put**
> Tag tags_id_put(id, data=data)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Model id
data = TweakApi.Tag() # Tag | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.tags_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Tag**](Tag.md)| Model instance data | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_replace_post**
> Tag tags_id_replace_post(id, data=data)

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Model id
data = TweakApi.Tag() # Tag | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.tags_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Tag**](Tag.md)| Model instance data | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_count_get**
> InlineResponse200 tags_id_templates_count_get(id, where=where)

Counts templates of Tag.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of Tag.
    api_response = api_instance.tags_id_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_delete**
> tags_id_templates_delete(id)

Deletes all templates of this model.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id

try: 
    # Deletes all templates of this model.
    api_instance.tags_id_templates_delete(id)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_fk_delete**
> tags_id_templates_fk_delete(id, fk)

Delete a related item by id for templates.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.tags_id_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_fk_get**
> Template tags_id_templates_fk_get(id, fk)

Find a related item by id for templates.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.tags_id_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_fk_put**
> Template tags_id_templates_fk_put(id, fk, data=data)

Update a related item by id for templates.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.tags_id_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_get**
> list[Template] tags_id_templates_get(id, filter=filter)

Queries templates of Tag.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of Tag.
    api_response = api_instance.tags_id_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_post**
> Template tags_id_templates_post(id, data=data)

Creates a new instance in templates of this model.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.tags_id_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_rel_fk_delete**
> tags_id_templates_rel_fk_delete(id, fk)

Remove the templates relation to an item by id.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Remove the templates relation to an item by id.
    api_instance.tags_id_templates_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_rel_fk_head**
> bool tags_id_templates_rel_fk_head(id, fk)

Check the existence of templates relation to an item by id.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Check the existence of templates relation to an item by id.
    api_response = api_instance.tags_id_templates_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_templates_rel_fk_put**
> TemplateTag tags_id_templates_rel_fk_put(id, fk, data=data)

Add a related item by id for templates.

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
api_instance = TweakApi.TagApi()
id = 'id_example' # str | Tag id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.TemplateTag() # TemplateTag |  (optional)

try: 
    # Add a related item by id for templates.
    api_response = api_instance.tags_id_templates_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_id_templates_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag id | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**TemplateTag**](TemplateTag.md)|  | [optional] 

### Return type

[**TemplateTag**](TemplateTag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_patch**
> Tag tags_patch(data=data)

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
api_instance = TweakApi.TagApi()
data = TweakApi.Tag() # Tag | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.tags_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)| Model instance data | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_post**
> Tag tags_post(data=data)

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
api_instance = TweakApi.TagApi()
data = TweakApi.Tag() # Tag | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.tags_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)| Model instance data | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_put**
> Tag tags_put(data=data)

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
api_instance = TweakApi.TagApi()
data = TweakApi.Tag() # Tag | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.tags_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)| Model instance data | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_replace_or_create_post**
> Tag tags_replace_or_create_post(data=data)

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
api_instance = TweakApi.TagApi()
data = TweakApi.Tag() # Tag | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.tags_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)| Model instance data | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_update_post**
> InlineResponse2002 tags_update_post(where=where, data=data)

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
api_instance = TweakApi.TagApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Tag() # Tag | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.tags_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Tag**](Tag.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_upsert_with_where_post**
> Tag tags_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.TagApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Tag() # Tag | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.tags_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->tags_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Tag**](Tag.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

