# enzona_payment.ObtieneUnListaDeDevolucionesRealizadasApi

All URIs are relative to *https://apisandbox.enzona.net/payment/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_refunds_get**](ObtieneUnListaDeDevolucionesRealizadasApi.md#payments_refunds_get) | **GET** /payments/refunds | 


# **payments_refunds_get**
> object payments_refunds_get(merchant_uuid=merchant_uuid, limit=limit, offset=offset, status_filter=status_filter, start_date_filter=start_date_filter, end_date_filter=end_date_filter, order_filter=order_filter)



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
api_instance = enzona_payment.ObtieneUnListaDeDevolucionesRealizadasApi(enzona_payment.ApiClient(configuration))
merchant_uuid = 'merchant_uuid_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
status_filter = 'status_filter_example' # str |  (optional)
start_date_filter = 'start_date_filter_example' # str |  (optional)
end_date_filter = 'end_date_filter_example' # str |  (optional)
order_filter = 'order_filter_example' # str |  (optional)

try:
    api_response = api_instance.payments_refunds_get(merchant_uuid=merchant_uuid, limit=limit, offset=offset, status_filter=status_filter, start_date_filter=start_date_filter, end_date_filter=end_date_filter, order_filter=order_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObtieneUnListaDeDevolucionesRealizadasApi->payments_refunds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_uuid** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 
 **status_filter** | **str**|  | [optional] 
 **start_date_filter** | **str**|  | [optional] 
 **end_date_filter** | **str**|  | [optional] 
 **order_filter** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

