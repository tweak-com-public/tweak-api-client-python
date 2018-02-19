# TweakApi.TeamBuilderConfigProductSizeMaterialApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_builder_config_product_size_materials_change_stream_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_change_stream_get) | **GET** /TeamBuilderConfigProductSizeMaterials/change-stream | Create a change stream.
[**team_builder_config_product_size_materials_change_stream_post**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_change_stream_post) | **POST** /TeamBuilderConfigProductSizeMaterials/change-stream | Create a change stream.
[**team_builder_config_product_size_materials_count_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_count_get) | **GET** /TeamBuilderConfigProductSizeMaterials/count | Count instances of the model matched by where from the data source.
[**team_builder_config_product_size_materials_find_one_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_find_one_get) | **GET** /TeamBuilderConfigProductSizeMaterials/findOne | Find first instance of the model matched by filter from the data source.
[**team_builder_config_product_size_materials_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_get) | **GET** /TeamBuilderConfigProductSizeMaterials | Find all instances of the model matched by filter from the data source.
[**team_builder_config_product_size_materials_id_builder_config_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_builder_config_get) | **GET** /TeamBuilderConfigProductSizeMaterials/{id}/builderConfig | Fetches belongsTo relation builderConfig.
[**team_builder_config_product_size_materials_id_delete**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_delete) | **DELETE** /TeamBuilderConfigProductSizeMaterials/{id} | Delete a model instance by {{id}} from the data source.
[**team_builder_config_product_size_materials_id_exists_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_exists_get) | **GET** /TeamBuilderConfigProductSizeMaterials/{id}/exists | Check whether a model instance exists in the data source.
[**team_builder_config_product_size_materials_id_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_get) | **GET** /TeamBuilderConfigProductSizeMaterials/{id} | Find a model instance by {{id}} from the data source.
[**team_builder_config_product_size_materials_id_head**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_head) | **HEAD** /TeamBuilderConfigProductSizeMaterials/{id} | Check whether a model instance exists in the data source.
[**team_builder_config_product_size_materials_id_patch**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_patch) | **PATCH** /TeamBuilderConfigProductSizeMaterials/{id} | Patch attributes for a model instance and persist it into the data source.
[**team_builder_config_product_size_materials_id_pdf_color_profile_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_pdf_color_profile_get) | **GET** /TeamBuilderConfigProductSizeMaterials/{id}/pdfColorProfile | Fetches belongsTo relation pdfColorProfile.
[**team_builder_config_product_size_materials_id_product_size_material_get**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_product_size_material_get) | **GET** /TeamBuilderConfigProductSizeMaterials/{id}/productSizeMaterial | Fetches belongsTo relation productSizeMaterial.
[**team_builder_config_product_size_materials_id_put**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_put) | **PUT** /TeamBuilderConfigProductSizeMaterials/{id} | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_size_materials_id_replace_post**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_id_replace_post) | **POST** /TeamBuilderConfigProductSizeMaterials/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**team_builder_config_product_size_materials_post**](TeamBuilderConfigProductSizeMaterialApi.md#team_builder_config_product_size_materials_post) | **POST** /TeamBuilderConfigProductSizeMaterials | Create a new instance of the model and persist it into the data source.


# **team_builder_config_product_size_materials_change_stream_get**
> file team_builder_config_product_size_materials_change_stream_get(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_size_materials_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_change_stream_get: %s\n" % e)
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

# **team_builder_config_product_size_materials_change_stream_post**
> file team_builder_config_product_size_materials_change_stream_post(options=options)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_config_product_size_materials_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_change_stream_post: %s\n" % e)
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

# **team_builder_config_product_size_materials_count_get**
> InlineResponse2001 team_builder_config_product_size_materials_count_get(where=where)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.team_builder_config_product_size_materials_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_count_get: %s\n" % e)
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

# **team_builder_config_product_size_materials_find_one_get**
> TeamBuilderConfigProductSizeMaterial team_builder_config_product_size_materials_find_one_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_size_materials_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_get**
> list[TeamBuilderConfigProductSizeMaterial] team_builder_config_product_size_materials_get(filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.team_builder_config_product_size_materials_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamBuilderConfigProductSizeMaterial]**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_id_builder_config_get**
> TeamBuilderConfig team_builder_config_product_size_materials_id_builder_config_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | TeamBuilderConfigProductSizeMaterial id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation builderConfig.
    api_response = api_instance.team_builder_config_product_size_materials_id_builder_config_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_builder_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductSizeMaterial id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_id_delete**
> object team_builder_config_product_size_materials_id_delete(id)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_size_materials_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_delete: %s\n" % e)
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

# **team_builder_config_product_size_materials_id_exists_get**
> InlineResponse2002 team_builder_config_product_size_materials_id_exists_get(id)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_size_materials_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_exists_get: %s\n" % e)
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

# **team_builder_config_product_size_materials_id_get**
> TeamBuilderConfigProductSizeMaterial team_builder_config_product_size_materials_id_get(id, filter=filter)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_config_product_size_materials_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_id_head**
> InlineResponse2002 team_builder_config_product_size_materials_id_head(id)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_config_product_size_materials_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_head: %s\n" % e)
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

# **team_builder_config_product_size_materials_id_patch**
> TeamBuilderConfigProductSizeMaterial team_builder_config_product_size_materials_id_patch(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | TeamBuilderConfigProductSizeMaterial id
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_size_materials_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductSizeMaterial id | 
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_id_pdf_color_profile_get**
> ProductPdfColorProfile team_builder_config_product_size_materials_id_pdf_color_profile_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | TeamBuilderConfigProductSizeMaterial id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation pdfColorProfile.
    api_response = api_instance.team_builder_config_product_size_materials_id_pdf_color_profile_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_pdf_color_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductSizeMaterial id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_id_product_size_material_get**
> ProductSizeMaterial team_builder_config_product_size_materials_id_product_size_material_get(id, refresh=refresh)

Fetches belongsTo relation productSizeMaterial.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | TeamBuilderConfigProductSizeMaterial id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation productSizeMaterial.
    api_response = api_instance.team_builder_config_product_size_materials_id_product_size_material_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_product_size_material_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfigProductSizeMaterial id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_id_put**
> TeamBuilderConfigProductSizeMaterial team_builder_config_product_size_materials_id_put(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_size_materials_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_id_replace_post**
> TeamBuilderConfigProductSizeMaterial team_builder_config_product_size_materials_id_replace_post(id, data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_config_product_size_materials_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_config_product_size_materials_post**
> TeamBuilderConfigProductSizeMaterial team_builder_config_product_size_materials_post(data=data)

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
api_instance = TweakApi.TeamBuilderConfigProductSizeMaterialApi()
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.team_builder_config_product_size_materials_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigProductSizeMaterialApi->team_builder_config_product_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

