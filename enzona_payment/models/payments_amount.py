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

from enzona_payment.models.payments_amount_details import PaymentsAmountDetails  # noqa: F401,E501


class PaymentsAmount(object):
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
        'total': 'float',
        'details': 'PaymentsAmountDetails'
    }

    attribute_map = {
        'total': 'total',
        'details': 'details'
    }

    def __init__(self, total=None, details=None):  # noqa: E501
        """PaymentsAmount - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._details = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if details is not None:
            self.details = details

    @property
    def total(self):
        """Gets the total of this PaymentsAmount.  # noqa: E501


        :return: The total of this PaymentsAmount.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PaymentsAmount.


        :param total: The total of this PaymentsAmount.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def details(self):
        """Gets the details of this PaymentsAmount.  # noqa: E501


        :return: The details of this PaymentsAmount.  # noqa: E501
        :rtype: PaymentsAmountDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this PaymentsAmount.


        :param details: The details of this PaymentsAmount.  # noqa: E501
        :type: PaymentsAmountDetails
        """

        self._details = details

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
        if issubclass(PaymentsAmount, dict):
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
        if not isinstance(other, PaymentsAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
