# enzona_payment.ObtieneLosDetallesDeUnaDevolucinRealizadaApi

All URIs are relative to *https://apisandbox.enzona.net/payment/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_refund_transaction_uuid_get**](ObtieneLosDetallesDeUnaDevolucinRealizadaApi.md#payments_refund_transaction_uuid_get) | **GET** /payments/refund/{transaction_uuid} | 


# **payments_refund_transaction_uuid_get**
> object payments_refund_transaction_uuid_get(transaction_uuid)



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
api_instance = enzona_payment.ObtieneLosDetallesDeUnaDevolucinRealizadaApi(enzona_payment.ApiClient(configuration))
transaction_uuid = 'transaction_uuid_example' # str | 

try:
    api_response = api_instance.payments_refund_transaction_uuid_get(transaction_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObtieneLosDetallesDeUnaDevolucinRealizadaApi->payments_refund_transaction_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_uuid** | **str**|  | 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

