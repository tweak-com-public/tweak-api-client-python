# TweakApi.PublicVBuilderAssetApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_builder_asset_backgrounds_folders_folder_path_get**](PublicVBuilderAssetApi.md#v1_builder_asset_backgrounds_folders_folder_path_get) | **GET** /v1/BuilderAsset/backgrounds/folders/{folderPath} | Get Builder Asset Backgrounds on a folders
[**v1_builder_asset_backgrounds_folders_get**](PublicVBuilderAssetApi.md#v1_builder_asset_backgrounds_folders_get) | **GET** /v1/BuilderAsset/backgrounds/folders | Get folders for Builder Asset Backgrounds
[**v1_builder_asset_backgrounds_get**](PublicVBuilderAssetApi.md#v1_builder_asset_backgrounds_get) | **GET** /v1/BuilderAsset/backgrounds | Get all Builder Asset Backgrounds


# **v1_builder_asset_backgrounds_folders_folder_path_get**
> list[CloudinaryImage] v1_builder_asset_backgrounds_folders_folder_path_get(folder_path, filter=filter)

Get Builder Asset Backgrounds on a folders

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
api_instance = TweakApi.PublicVBuilderAssetApi()
folder_path = 'folder_path_example' # str | Folder path for backgrounds
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Get Builder Asset Backgrounds on a folders
    api_response = api_instance.v1_builder_asset_backgrounds_folders_folder_path_get(folder_path, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVBuilderAssetApi->v1_builder_asset_backgrounds_folders_folder_path_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_path** | **str**| Folder path for backgrounds | 
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[CloudinaryImage]**](CloudinaryImage.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_builder_asset_backgrounds_folders_get**
> list[BuilderAssetBackgroundFolder] v1_builder_asset_backgrounds_folders_get()

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
# Configure API key authorization: teamKey
TweakApi.configuration.api_key['teamKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['teamKey'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PublicVBuilderAssetApi()

try: 
    # Get folders for Builder Asset Backgrounds
    api_response = api_instance.v1_builder_asset_backgrounds_folders_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVBuilderAssetApi->v1_builder_asset_backgrounds_folders_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BuilderAssetBackgroundFolder]**](BuilderAssetBackgroundFolder.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_builder_asset_backgrounds_get**
> list[CloudinaryImage] v1_builder_asset_backgrounds_get(filter=filter)

Get all Builder Asset Backgrounds

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
api_instance = TweakApi.PublicVBuilderAssetApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Get all Builder Asset Backgrounds
    api_response = api_instance.v1_builder_asset_backgrounds_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVBuilderAssetApi->v1_builder_asset_backgrounds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[CloudinaryImage]**](CloudinaryImage.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

