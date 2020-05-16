# enzona_payment.PermiteRealizarLaDevolucinDeUnPagoApi

All URIs are relative to *https://apisandbox.enzona.net/payment/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_transaction_uuid_refund_post**](PermiteRealizarLaDevolucinDeUnPagoApi.md#payments_transaction_uuid_refund_post) | **POST** /payments/{transaction_uuid}/refund | 


# **payments_transaction_uuid_refund_post**
> object payments_transaction_uuid_refund_post(transaction_uuid, payload=payload)



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
api_instance = enzona_payment.PermiteRealizarLaDevolucinDeUnPagoApi(enzona_payment.ApiClient(configuration))
transaction_uuid = 'transaction_uuid_example' # str | 
payload = enzona_payment.Payload4() # Payload4 | Request Body (optional)

try:
    api_response = api_instance.payments_transaction_uuid_refund_post(transaction_uuid, payload=payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermiteRealizarLaDevolucinDeUnPagoApi->payments_transaction_uuid_refund_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_uuid** | **str**|  | 
 **payload** | [**Payload4**](Payload4.md)| Request Body | [optional] 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

