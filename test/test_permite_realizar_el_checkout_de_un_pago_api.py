# coding: utf-8

"""
    PaymentAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import enzona_payment
from enzona_payment.api.permite_realizar_el_checkout_de_un_pago_api import PermiteRealizarElCheckoutDeUnPagoApi  # noqa: E501
from enzona_payment.rest import ApiException


class TestPermiteRealizarElCheckoutDeUnPagoApi(unittest.TestCase):
    """PermiteRealizarElCheckoutDeUnPagoApi unit test stubs"""

    def setUp(self):
        self.api = enzona_payment.api.permite_realizar_el_checkout_de_un_pago_api.PermiteRealizarElCheckoutDeUnPagoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_payments_checkout_uuid_get(self):
        """Test case for payments_checkout_uuid_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
