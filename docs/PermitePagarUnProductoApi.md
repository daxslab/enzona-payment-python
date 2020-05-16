# enzona_payment.PermitePagarUnProductoApi

All URIs are relative to *https://apisandbox.enzona.net/payment/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_store_post**](PermitePagarUnProductoApi.md#payments_store_post) | **POST** /payments/store | 


# **payments_store_post**
> object payments_store_post(payload=payload)



### Example
```python
from __future__ import print_function
import time
import enzona_payment
from enzona_payment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = enzona_payment.PermitePagarUnProductoApi()
payload = enzona_payment.Payload1() # Payload1 | Parametros de entrada (optional)

try:
    api_response = api_instance.payments_store_post(payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermitePagarUnProductoApi->payments_store_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**Payload1**](Payload1.md)| Parametros de entrada | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

