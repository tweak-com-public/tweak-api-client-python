# TweakApi.PublicVBuilderConfigApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_builder_config_default_get**](PublicVBuilderConfigApi.md#v1_builder_config_default_get) | **GET** /v1/BuilderConfig/default | Get default BuilderConfig
[**v1_builder_config_default_product_size_materials_get**](PublicVBuilderConfigApi.md#v1_builder_config_default_product_size_materials_get) | **GET** /v1/BuilderConfig/default/productSizeMaterials | Get default BuilderConfig ProductSizeMaterial


# **v1_builder_config_default_get**
> TeamBuilderConfig v1_builder_config_default_get()

Get default BuilderConfig

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: teamKey
TweakApi.configuration.api_key['teamKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['teamKey'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PublicVBuilderConfigApi()

try: 
    # Get default BuilderConfig
    api_response = api_instance.v1_builder_config_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVBuilderConfigApi->v1_builder_config_default_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_builder_config_default_product_size_materials_get**
> ProductSizeMaterial v1_builder_config_default_product_size_materials_get()

Get default BuilderConfig ProductSizeMaterial

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: teamKey
TweakApi.configuration.api_key['teamKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['teamKey'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PublicVBuilderConfigApi()

try: 
    # Get default BuilderConfig ProductSizeMaterial
    api_response = api_instance.v1_builder_config_default_product_size_materials_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVBuilderConfigApi->v1_builder_config_default_product_size_materials_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

