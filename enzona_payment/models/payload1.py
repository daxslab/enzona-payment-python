# coding: utf-8

"""
    PaymentAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from enzona_payment.models.paymentsstore_amount import PaymentsstoreAmount  # noqa: F401,E501
from enzona_payment.models.paymentsstore_items import PaymentsstoreItems  # noqa: F401,E501


class Payload1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'funding_source_uuid': 'str',
        'description': 'str',
        'currency': 'str',
        'payment_password': 'str',
        'amount': 'PaymentsstoreAmount',
        'items': 'list[PaymentsstoreItems]'
    }

    attribute_map = {
        'funding_source_uuid': 'funding_source_uuid',
        'description': 'description',
        'currency': 'currency',
        'payment_password': 'payment_password',
        'amount': 'amount',
        'items': 'items'
    }

    def __init__(self, funding_source_uuid=None, description=None, currency=None, payment_password=None, amount=None, items=None):  # noqa: E501
        """Payload1 - a model defined in Swagger"""  # noqa: E501

        self._funding_source_uuid = None
        self._description = None
        self._currency = None
        self._payment_password = None
        self._amount = None
        self._items = None
        self.discriminator = None

        if funding_source_uuid is not None:
            self.funding_source_uuid = funding_source_uuid
        if description is not None:
            self.description = description
        if currency is not None:
            self.currency = currency
        if payment_password is not None:
            self.payment_password = payment_password
        if amount is not None:
            self.amount = amount
        if items is not None:
            self.items = items

    @property
    def funding_source_uuid(self):
        """Gets the funding_source_uuid of this Payload1.  # noqa: E501


        :return: The funding_source_uuid of this Payload1.  # noqa: E501
        :rtype: str
        """
        return self._funding_source_uuid

    @funding_source_uuid.setter
    def funding_source_uuid(self, funding_source_uuid):
        """Sets the funding_source_uuid of this Payload1.


        :param funding_source_uuid: The funding_source_uuid of this Payload1.  # noqa: E501
        :type: str
        """

        self._funding_source_uuid = funding_source_uuid

    @property
    def description(self):
        """Gets the description of this Payload1.  # noqa: E501


        :return: The description of this Payload1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Payload1.


        :param description: The description of this Payload1.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def currency(self):
        """Gets the currency of this Payload1.  # noqa: E501


        :return: The currency of this Payload1.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Payload1.


        :param currency: The currency of this Payload1.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def payment_password(self):
        """Gets the payment_password of this Payload1.  # noqa: E501


        :return: The payment_password of this Payload1.  # noqa: E501
        :rtype: str
        """
        return self._payment_password

    @payment_password.setter
    def payment_password(self, payment_password):
        """Sets the payment_password of this Payload1.


        :param payment_password: The payment_password of this Payload1.  # noqa: E501
        :type: str
        """

        self._payment_password = payment_password

    @property
    def amount(self):
        """Gets the amount of this Payload1.  # noqa: E501


        :return: The amount of this Payload1.  # noqa: E501
        :rtype: PaymentsstoreAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payload1.


        :param amount: The amount of this Payload1.  # noqa: E501
        :type: PaymentsstoreAmount
        """

        self._amount = amount

    @property
    def items(self):
        """Gets the items of this Payload1.  # noqa: E501


        :return: The items of this Payload1.  # noqa: E501
        :rtype: list[PaymentsstoreItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Payload1.


        :param items: The items of this Payload1.  # noqa: E501
        :type: list[PaymentsstoreItems]
        """

        self._items = items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Payload1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Payload1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
