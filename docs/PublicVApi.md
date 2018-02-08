# TweakApi.PublicVApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_base_locale_country_code_get**](PublicVApi.md#v1_base_locale_country_code_get) | **GET** /v1/Base/locale/country/code | Get locale from Country Code
[**v1_base_locale_country_name_get**](PublicVApi.md#v1_base_locale_country_name_get) | **GET** /v1/Base/locale/country/name | Get locale from Country Name
[**v1_base_locale_get**](PublicVApi.md#v1_base_locale_get) | **GET** /v1/Base/locale | Get locale from client IP


# **v1_base_locale_country_code_get**
> object v1_base_locale_country_code_get(country_code)

Get locale from Country Code

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
api_instance = TweakApi.PublicVApi()
country_code = 'country_code_example' # str | Country code

try: 
    # Get locale from Country Code
    api_response = api_instance.v1_base_locale_country_code_get(country_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVApi->v1_base_locale_country_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Country code | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_base_locale_country_name_get**
> object v1_base_locale_country_name_get(country_name)

Get locale from Country Name

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
api_instance = TweakApi.PublicVApi()
country_name = 'country_name_example' # str | Country name

try: 
    # Get locale from Country Name
    api_response = api_instance.v1_base_locale_country_name_get(country_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVApi->v1_base_locale_country_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_name** | **str**| Country name | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_base_locale_get**
> object v1_base_locale_get()

Get locale from client IP

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
api_instance = TweakApi.PublicVApi()

try: 
    # Get locale from client IP
    api_response = api_instance.v1_base_locale_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicVApi->v1_base_locale_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[access_token](../README.md#access_token), [teamKey](../README.md#teamKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

