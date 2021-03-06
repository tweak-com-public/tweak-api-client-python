# TweakApi.PortalTemplateApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal_templates_change_stream_get**](PortalTemplateApi.md#portal_templates_change_stream_get) | **GET** /PortalTemplates/change-stream | Create a change stream.
[**portal_templates_change_stream_post**](PortalTemplateApi.md#portal_templates_change_stream_post) | **POST** /PortalTemplates/change-stream | Create a change stream.
[**portal_templates_count_get**](PortalTemplateApi.md#portal_templates_count_get) | **GET** /PortalTemplates/count | Count instances of the model matched by where from the data source.
[**portal_templates_find_one_get**](PortalTemplateApi.md#portal_templates_find_one_get) | **GET** /PortalTemplates/findOne | Find first instance of the model matched by filter from the data source.
[**portal_templates_get**](PortalTemplateApi.md#portal_templates_get) | **GET** /PortalTemplates | Find all instances of the model matched by filter from the data source.
[**portal_templates_id_delete**](PortalTemplateApi.md#portal_templates_id_delete) | **DELETE** /PortalTemplates/{id} | Delete a model instance by {{id}} from the data source.
[**portal_templates_id_exists_get**](PortalTemplateApi.md#portal_templates_id_exists_get) | **GET** /PortalTemplates/{id}/exists | Check whether a model instance exists in the data source.
[**portal_templates_id_folder_get**](PortalTemplateApi.md#portal_templates_id_folder_get) | **GET** /PortalTemplates/{id}/folder | Fetches belongsTo relation folder.
[**portal_templates_id_get**](PortalTemplateApi.md#portal_templates_id_get) | **GET** /PortalTemplates/{id} | Find a model instance by {{id}} from the data source.
[**portal_templates_id_head**](PortalTemplateApi.md#portal_templates_id_head) | **HEAD** /PortalTemplates/{id} | Check whether a model instance exists in the data source.
[**portal_templates_id_patch**](PortalTemplateApi.md#portal_templates_id_patch) | **PATCH** /PortalTemplates/{id} | Patch attributes for a model instance and persist it into the data source.
[**portal_templates_id_portal_get**](PortalTemplateApi.md#portal_templates_id_portal_get) | **GET** /PortalTemplates/{id}/portal | Fetches belongsTo relation portal.
[**portal_templates_id_put**](PortalTemplateApi.md#portal_templates_id_put) | **PUT** /PortalTemplates/{id} | Replace attributes for a model instance and persist it into the data source.
[**portal_templates_id_replace_post**](PortalTemplateApi.md#portal_templates_id_replace_post) | **POST** /PortalTemplates/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**portal_templates_id_template_get**](PortalTemplateApi.md#portal_templates_id_template_get) | **GET** /PortalTemplates/{id}/template | Fetches belongsTo relation template.
[**portal_templates_post**](PortalTemplateApi.md#portal_templates_post) | **POST** /PortalTemplates | Create a new instance of the model and persist it into the data source.


# **portal_templates_change_stream_get**
> file portal_templates_change_stream_get(options=options)

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
api_instance = TweakApi.PortalTemplateApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portal_templates_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_change_stream_get: %s\n" % e)
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

# **portal_templates_change_stream_post**
> file portal_templates_change_stream_post(options=options)

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
api_instance = TweakApi.PortalTemplateApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portal_templates_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_change_stream_post: %s\n" % e)
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

# **portal_templates_count_get**
> InlineResponse2001 portal_templates_count_get(where=where)

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
api_instance = TweakApi.PortalTemplateApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.portal_templates_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_count_get: %s\n" % e)
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

# **portal_templates_find_one_get**
> PortalTemplate portal_templates_find_one_get(filter=filter)

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
api_instance = TweakApi.PortalTemplateApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.portal_templates_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_get**
> list[PortalTemplate] portal_templates_get(filter=filter)

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
api_instance = TweakApi.PortalTemplateApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.portal_templates_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[PortalTemplate]**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_id_delete**
> object portal_templates_id_delete(id)

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
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.portal_templates_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_delete: %s\n" % e)
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

# **portal_templates_id_exists_get**
> InlineResponse2002 portal_templates_id_exists_get(id)

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
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portal_templates_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_exists_get: %s\n" % e)
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

# **portal_templates_id_folder_get**
> PortalTemplateFolder portal_templates_id_folder_get(id, refresh=refresh)

Fetches belongsTo relation folder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | PortalTemplate id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation folder.
    api_response = api_instance.portal_templates_id_folder_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplate id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_id_get**
> PortalTemplate portal_templates_id_get(id, filter=filter)

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
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.portal_templates_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_id_head**
> InlineResponse2002 portal_templates_id_head(id)

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
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portal_templates_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_head: %s\n" % e)
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

# **portal_templates_id_patch**
> PortalTemplate portal_templates_id_patch(id, data=data)

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
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | PortalTemplate id
data = TweakApi.PortalTemplate() # PortalTemplate | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_templates_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplate id | 
 **data** | [**PortalTemplate**](PortalTemplate.md)| An object of model property name/value pairs | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_id_portal_get**
> Portal portal_templates_id_portal_get(id, refresh=refresh)

Fetches belongsTo relation portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | PortalTemplate id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation portal.
    api_response = api_instance.portal_templates_id_portal_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_portal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplate id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_id_put**
> PortalTemplate portal_templates_id_put(id, data=data)

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
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | Model id
data = TweakApi.PortalTemplate() # PortalTemplate | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_templates_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**PortalTemplate**](PortalTemplate.md)| Model instance data | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_id_replace_post**
> PortalTemplate portal_templates_id_replace_post(id, data=data)

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
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | Model id
data = TweakApi.PortalTemplate() # PortalTemplate | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portal_templates_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**PortalTemplate**](PortalTemplate.md)| Model instance data | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_id_template_get**
> Template portal_templates_id_template_get(id, refresh=refresh)

Fetches belongsTo relation template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalTemplateApi()
id = 'id_example' # str | PortalTemplate id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation template.
    api_response = api_instance.portal_templates_id_template_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_id_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| PortalTemplate id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portal_templates_post**
> PortalTemplate portal_templates_post(data=data)

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
api_instance = TweakApi.PortalTemplateApi()
data = TweakApi.PortalTemplate() # PortalTemplate | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.portal_templates_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalTemplateApi->portal_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PortalTemplate**](PortalTemplate.md)| Model instance data | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

