# TweakApi.PublicVTeamApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_team_builder_configs_default_get**](PublicVTeamApi.md#v1_team_builder_configs_default_get) | **GET** /v1/Team/builderConfigs/default | Get default Team&#39;s BuilderConfig
[**v1_team_builder_configs_default_product_size_materials_get**](PublicVTeamApi.md#v1_team_builder_configs_default_product_size_materials_get) | **GET** /v1/Team/builderConfigs/default/productSizeMaterials | Get default Team&#39;s BuilderConfig ProductSizeMaterial
[**v1_team_builder_configs_id_get**](PublicVTeamApi.md#v1_team_builder_configs_id_get) | **GET** /v1/Team/builderConfigs/{id} | Get Team&#39;s BuilderConfig by id
[**v1_team_builder_configs_id_product_size_materials_get**](PublicVTeamApi.md#v1_team_builder_configs_id_product_size_materials_get) | **GET** /v1/Team/builderConfigs/{id}/productSizeMaterials | Get Team&#39;s BuilderConfig ProductSizeMaterial by BuilderConfig id


# **v1_team_builder_configs_default_get**
> TeamBuilderConfig v1_team_builder_configs_default_get()

Get default Team's BuilderConfig

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
api_instance = TweakApi.PublicVTeamApi()

try: 
    # Get default Team's BuilderConfig
    api_response = api_instance.v1_team_builder_configs_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVTeamApi->v1_team_builder_configs_default_get: %s\n" % e)
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

# **v1_team_builder_configs_default_product_size_materials_get**
> ProductSizeMaterial v1_team_builder_configs_default_product_size_materials_get()

Get default Team's BuilderConfig ProductSizeMaterial

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
api_instance = TweakApi.PublicVTeamApi()

try: 
    # Get default Team's BuilderConfig ProductSizeMaterial
    api_response = api_instance.v1_team_builder_configs_default_product_size_materials_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVTeamApi->v1_team_builder_configs_default_product_size_materials_get: %s\n" % e)
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

# **v1_team_builder_configs_id_get**
> TeamBuilderConfig v1_team_builder_configs_id_get(id)

Get Team's BuilderConfig by id

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
api_instance = TweakApi.PublicVTeamApi()
id = 'id_example' # str | BuilderConfig id

try: 
    # Get Team's BuilderConfig by id
    api_response = api_instance.v1_team_builder_configs_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVTeamApi->v1_team_builder_configs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| BuilderConfig id | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_team_builder_configs_id_product_size_materials_get**
> TeamBuilderConfigProductSizeMaterial v1_team_builder_configs_id_product_size_materials_get(id)

Get Team's BuilderConfig ProductSizeMaterial by BuilderConfig id

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
api_instance = TweakApi.PublicVTeamApi()
id = 'id_example' # str | BuilderConfig id

try: 
    # Get Team's BuilderConfig ProductSizeMaterial by BuilderConfig id
    api_response = api_instance.v1_team_builder_configs_id_product_size_materials_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVTeamApi->v1_team_builder_configs_id_product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| BuilderConfig id | 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

