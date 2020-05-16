# enzona_payment.PermiteCrearUnRecieveCodeApi

All URIs are relative to *https://apisandbox.enzona.net/payment/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_vendor_code_post**](PermiteCrearUnRecieveCodeApi.md#payments_vendor_code_post) | **POST** /payments/vendor/code | 


# **payments_vendor_code_post**
> object payments_vendor_code_post(payload=payload)



### Example
```python
from __future__ import print_function
import time
import enzona_payment
from enzona_payment.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
configuration = enzona_payment.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = enzona_payment.PermiteCrearUnRecieveCodeApi(enzona_payment.ApiClient(configuration))
payload = enzona_payment.Payload5() # Payload5 | Parametros de entrada (optional)

try:
    api_response = api_instance.payments_vendor_code_post(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermiteCrearUnRecieveCodeApi->payments_vendor_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload5**](Payload5.md)| Parametros de entrada | [optional] 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

