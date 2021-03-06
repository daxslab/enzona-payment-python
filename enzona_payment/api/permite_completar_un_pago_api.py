# coding: utf-8

"""
    PaymentAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from enzona_payment.api_client import ApiClient


class PermiteCompletarUnPagoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def payments_transaction_uuid_complete_post(self, transaction_uuid, **kwargs):  # noqa: E501
        """payments_transaction_uuid_complete_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_transaction_uuid_complete_post(transaction_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_uuid:  (required)
        :param InBody payload: Request Body
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_transaction_uuid_complete_post_with_http_info(transaction_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_transaction_uuid_complete_post_with_http_info(transaction_uuid, **kwargs)  # noqa: E501
            return data

    def payments_transaction_uuid_complete_post_with_http_info(self, transaction_uuid, **kwargs):  # noqa: E501
        """payments_transaction_uuid_complete_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_transaction_uuid_complete_post_with_http_info(transaction_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str transaction_uuid:  (required)
        :param InBody payload: Request Body
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_uuid', 'payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_transaction_uuid_complete_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transaction_uuid' is set
        if ('transaction_uuid' not in params or
                params['transaction_uuid'] is None):
            raise ValueError("Missing the required parameter `transaction_uuid` when calling `payments_transaction_uuid_complete_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_uuid' in params:
            path_params['transaction_uuid'] = params['transaction_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # Authentication setting
        auth_settings = ['default']  # noqa: E501

        return self.api_client.call_api(
            '/payments/{transaction_uuid}/complete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
