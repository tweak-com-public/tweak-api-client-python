# TweakApi.BuilderAssetUrlApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**builder_asset_urls_designs_id_get**](BuilderAssetUrlApi.md#builder_asset_urls_designs_id_get) | **GET** /BuilderAsset/urls/designs/{id} | Get folders for Builder Asset Backgrounds
[**builder_asset_urls_templates_id_get**](BuilderAssetUrlApi.md#builder_asset_urls_templates_id_get) | **GET** /BuilderAsset/urls/templates/{id} | Get folders for Builder Asset Backgrounds
[**builder_asset_urls_tweak_templates_id_get**](BuilderAssetUrlApi.md#builder_asset_urls_tweak_templates_id_get) | **GET** /BuilderAsset/urls/tweakTemplates/{id} | Get folders for Builder Asset Backgrounds


# **builder_asset_urls_designs_id_get**
> InlineResponse200 builder_asset_urls_designs_id_get(id)

Get folders for Builder Asset Backgrounds

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
api_instance = TweakApi.BuilderAssetUrlApi()
id = 'id_example' # str | Design Id

try: 
    # Get folders for Builder Asset Backgrounds
    api_response = api_instance.builder_asset_urls_designs_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuilderAssetUrlApi->builder_asset_urls_designs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Design Id | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builder_asset_urls_templates_id_get**
> InlineResponse200 builder_asset_urls_templates_id_get(id)

Get folders for Builder Asset Backgrounds

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
api_instance = TweakApi.BuilderAssetUrlApi()
id = 'id_example' # str | Template Id

try: 
    # Get folders for Builder Asset Backgrounds
    api_response = api_instance.builder_asset_urls_templates_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuilderAssetUrlApi->builder_asset_urls_templates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Template Id | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builder_asset_urls_tweak_templates_id_get**
> InlineResponse200 builder_asset_urls_tweak_templates_id_get(id)

Get folders for Builder Asset Backgrounds

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
api_instance = TweakApi.BuilderAssetUrlApi()
id = 'id_example' # str | Tweak Template Id

try: 
    # Get folders for Builder Asset Backgrounds
    api_response = api_instance.builder_asset_urls_tweak_templates_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuilderAssetUrlApi->builder_asset_urls_tweak_templates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tweak Template Id | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

