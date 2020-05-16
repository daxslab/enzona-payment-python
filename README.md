# enzona-payment

***This is a work in progress, there are rough corners and the 
API can change witouth previuos warnings. 
Not recommended for production usage.***

Python Client library for interacting with [EnZona's Payment API](https://api.enzona.net). 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.0.0
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import enzona_payment 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import enzona_payment
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = enzona_payment.ListaDeDevolucionesDeUnPagoApi(enzona_payment.ApiClient(configuration))
transaction_uuid = 'transaction_uuid_example' # str | 
limit = 'limit_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
status_filter = 'status_filter_example' # str |  (optional)
start_date_filter = 'start_date_filter_example' # str |  (optional)
end_date_filter = 'end_date_filter_example' # str |  (optional)
order_filter = 'order_filter_example' # str |  (optional)

try:
    api_response = api_instance.payments_transaction_uuid_refunds_get(transaction_uuid, limit=limit, offset=offset, status_filter=status_filter, start_date_filter=start_date_filter, end_date_filter=end_date_filter, order_filter=order_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListaDeDevolucionesDeUnPagoApi->payments_transaction_uuid_refunds_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apisandbox.enzona.net/payment/v1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ListaDeDevolucionesDeUnPagoApi* | [**payments_transaction_uuid_refunds_get**](docs/ListaDeDevolucionesDeUnPagoApi.md#payments_transaction_uuid_refunds_get) | **GET** /payments/{transaction_uuid}/refunds | 
*ObtieneListadoDePagosRealizadosApi* | [**payments_get**](docs/ObtieneListadoDePagosRealizadosApi.md#payments_get) | **GET** /payments | 
*ObtieneLosDetallesDeUnPagoRealizadoApi* | [**payments_transaction_uuid_get**](docs/ObtieneLosDetallesDeUnPagoRealizadoApi.md#payments_transaction_uuid_get) | **GET** /payments/{transaction_uuid} | 
*ObtieneLosDetallesDeUnaDevolucinRealizadaApi* | [**payments_refund_transaction_uuid_get**](docs/ObtieneLosDetallesDeUnaDevolucinRealizadaApi.md#payments_refund_transaction_uuid_get) | **GET** /payments/refund/{transaction_uuid} | 
*ObtieneUnListaDeDevolucionesRealizadasApi* | [**payments_refunds_get**](docs/ObtieneUnListaDeDevolucionesRealizadasApi.md#payments_refunds_get) | **GET** /payments/refunds | 
*PermiteCancelarUnPagoApi* | [**payments_transaction_uuid_cancel_post**](docs/PermiteCancelarUnPagoApi.md#payments_transaction_uuid_cancel_post) | **POST** /payments/{transaction_uuid}/cancel | 
*PermiteCompletarUnPagoApi* | [**payments_transaction_uuid_complete_post**](docs/PermiteCompletarUnPagoApi.md#payments_transaction_uuid_complete_post) | **POST** /payments/{transaction_uuid}/complete | 
*PermiteConfirmarUnPagoApi* | [**payments_transaction_uuid_confirm_post**](docs/PermiteConfirmarUnPagoApi.md#payments_transaction_uuid_confirm_post) | **POST** /payments/{transaction_uuid}/confirm | 
*PermiteCrearUnPagoApi* | [**payments_post**](docs/PermiteCrearUnPagoApi.md#payments_post) | **POST** /payments | 
*PermiteCrearUnRecieveCodeApi* | [**payments_vendor_code_post**](docs/PermiteCrearUnRecieveCodeApi.md#payments_vendor_code_post) | **POST** /payments/vendor/code | 
*PermiteCrearUnaOrdenDePagoApi* | [**payment_orders_post**](docs/PermiteCrearUnaOrdenDePagoApi.md#payment_orders_post) | **POST** /payment-orders | 
*PermitePagarUnProductoApi* | [**payments_store_post**](docs/PermitePagarUnProductoApi.md#payments_store_post) | **POST** /payments/store | 
*PermiteRealizarElCheckoutDeUnPagoApi* | [**payments_checkout_uuid_get**](docs/PermiteRealizarElCheckoutDeUnPagoApi.md#payments_checkout_uuid_get) | **GET** /payments/checkout/{uuid} | 
*PermiteRealizarLaDevolucinDeUnPagoApi* | [**payments_transaction_uuid_refund_post**](docs/PermiteRealizarLaDevolucinDeUnPagoApi.md#payments_transaction_uuid_refund_post) | **POST** /payments/{transaction_uuid}/refund | 


## Documentation For Models

 - [AmountOperations](docs/AmountOperations.md)
 - [DetailsOperations](docs/DetailsOperations.md)
 - [FullOperations](docs/FullOperations.md)
 - [FullOperationsOperation](docs/FullOperationsOperation.md)
 - [FullOperationsOperationAmount](docs/FullOperationsOperationAmount.md)
 - [FullOperationsOperationAmountDetails](docs/FullOperationsOperationAmountDetails.md)
 - [FullOperationsOperationItems](docs/FullOperationsOperationItems.md)
 - [InBody](docs/InBody.md)
 - [ItemsOperations](docs/ItemsOperations.md)
 - [LinksSchema](docs/LinksSchema.md)
 - [OperationsPostComplete](docs/OperationsPostComplete.md)
 - [OperationsPostCompleteItems](docs/OperationsPostCompleteItems.md)
 - [Pagination](docs/Pagination.md)
 - [PaginationLinks](docs/PaginationLinks.md)
 - [PaginationLinksFirstPage](docs/PaginationLinksFirstPage.md)
 - [Payload](docs/Payload.md)
 - [Payload1](docs/Payload1.md)
 - [Payload2](docs/Payload2.md)
 - [Payload3](docs/Payload3.md)
 - [Payload4](docs/Payload4.md)
 - [Payload5](docs/Payload5.md)
 - [PaymentFullInfo](docs/PaymentFullInfo.md)
 - [PaymentFullInfoPayer](docs/PaymentFullInfoPayer.md)
 - [PaymentFullInfoPayerPayerInfo](docs/PaymentFullInfoPayerPayerInfo.md)
 - [PaymentFullOperations](docs/PaymentFullOperations.md)
 - [PaymentRefundOperations](docs/PaymentRefundOperations.md)
 - [PaymentRefundOperationsAmount](docs/PaymentRefundOperationsAmount.md)
 - [PaymentRefundOperationsAmountDetails](docs/PaymentRefundOperationsAmountDetails.md)
 - [PaymentSummaryInfo](docs/PaymentSummaryInfo.md)
 - [PaymentSummaryInfoOperations](docs/PaymentSummaryInfoOperations.md)
 - [PaymentSummaryInfoOperationsOperation](docs/PaymentSummaryInfoOperationsOperation.md)
 - [PaymentSummaryInfoOperationsOperationAmount](docs/PaymentSummaryInfoOperationsOperationAmount.md)
 - [PaymentSummaryInfoOperationsOperationAmountDetails](docs/PaymentSummaryInfoOperationsOperationAmountDetails.md)
 - [PaymentSummaryInfoOperationsOperationBankDebitDetails](docs/PaymentSummaryInfoOperationsOperationBankDebitDetails.md)
 - [PaymentsAmount](docs/PaymentsAmount.md)
 - [PaymentsAmountDetails](docs/PaymentsAmountDetails.md)
 - [PaymentsInfo](docs/PaymentsInfo.md)
 - [PaymentsItems](docs/PaymentsItems.md)
 - [PaymentsstoreAmount](docs/PaymentsstoreAmount.md)
 - [PaymentsstoreItems](docs/PaymentsstoreItems.md)
 - [PaymentstransactionUuidrefundAmount](docs/PaymentstransactionUuidrefundAmount.md)


## Documentation For Authorization


## default

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://apisandbox.enzona.net/authorize
- **Scopes**: 
 - **enzona_business_payment**: enzona_business_payment


## Author



