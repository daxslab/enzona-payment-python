# enzona_payment.PermiteRealizarElCheckoutDeUnPagoApi

All URIs are relative to *https://apisandbox.enzona.net/payment/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_checkout_uuid_get**](PermiteRealizarElCheckoutDeUnPagoApi.md#payments_checkout_uuid_get) | **GET** /payments/checkout/{uuid} | 


# **payments_checkout_uuid_get**
> payments_checkout_uuid_get(uuid)



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
api_instance = enzona_payment.PermiteRealizarElCheckoutDeUnPagoApi(enzona_payment.ApiClient(configuration))
uuid = 'uuid_example' # str | Identificador del checkout.

try:
    api_instance.payments_checkout_uuid_get(uuid)
except ApiException as e:
    print("Exception when calling PermiteRealizarElCheckoutDeUnPagoApi->payments_checkout_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Identificador del checkout. | 

### Return type

void (empty response body)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

