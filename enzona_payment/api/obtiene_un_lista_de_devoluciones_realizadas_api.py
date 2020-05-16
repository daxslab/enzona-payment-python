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


class ObtieneUnListaDeDevolucionesRealizadasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def payments_refunds_get(self, **kwargs):  # noqa: E501
        """payments_refunds_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_refunds_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_uuid: 
        :param str limit: 
        :param str offset: 
        :param str status_filter:
        :param str start_date_filter:
        :param str end_date_filter:
        :param str order_filter:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_refunds_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.payments_refunds_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def payments_refunds_get_with_http_info(self, **kwargs):  # noqa: E501
        """payments_refunds_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_refunds_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_uuid: 
        :param str limit: 
        :param str offset: 
        :param str status_filter:
        :param str start_date_filter:
        :param str end_date_filter:
        :param str order_filter:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_uuid', 'limit', 'offset', 'status_filter', 'start_date_filter', 'end_date_filter', 'order_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_refunds_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'merchant_uuid' in params:
            query_params.append(('merchant_uuid', params['merchant_uuid']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'status_filter' in params:
            query_params.append(('status_filter', params['status_filter']))  # noqa: E501
        if 'start_date_filter' in params:
            query_params.append(('start_date_filter', params['start_date_filter']))  # noqa: E501
        if 'end_date_filter' in params:
            query_params.append(('end_date_filter', params['end_date_filter']))  # noqa: E501
        if 'order_filter' in params:
            query_params.append(('order_filter', params['order_filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['default']  # noqa: E501

        return self.api_client.call_api(
            '/payments/refunds', 'GET',
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
