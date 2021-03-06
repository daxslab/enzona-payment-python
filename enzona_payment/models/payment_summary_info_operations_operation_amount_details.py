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


class PaymentSummaryInfoOperationsOperationAmountDetails(object):
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
        'tip': 'str',
        'tax': 'int',
        'shipping': 'int'
    }

    attribute_map = {
        'tip': 'tip',
        'tax': 'tax',
        'shipping': 'shipping'
    }

    def __init__(self, tip=None, tax=None, shipping=None):  # noqa: E501
        """PaymentSummaryInfoOperationsOperationAmountDetails - a model defined in Swagger"""  # noqa: E501

        self._tip = None
        self._tax = None
        self._shipping = None
        self.discriminator = None

        if tip is not None:
            self.tip = tip
        if tax is not None:
            self.tax = tax
        if shipping is not None:
            self.shipping = shipping

    @property
    def tip(self):
        """Gets the tip of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501


        :return: The tip of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501
        :rtype: str
        """
        return self._tip

    @tip.setter
    def tip(self, tip):
        """Sets the tip of this PaymentSummaryInfoOperationsOperationAmountDetails.


        :param tip: The tip of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501
        :type: str
        """

        self._tip = tip

    @property
    def tax(self):
        """Gets the tax of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501


        :return: The tax of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501
        :rtype: int
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this PaymentSummaryInfoOperationsOperationAmountDetails.


        :param tax: The tax of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501
        :type: int
        """

        self._tax = tax

    @property
    def shipping(self):
        """Gets the shipping of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501


        :return: The shipping of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501
        :rtype: int
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this PaymentSummaryInfoOperationsOperationAmountDetails.


        :param shipping: The shipping of this PaymentSummaryInfoOperationsOperationAmountDetails.  # noqa: E501
        :type: int
        """

        self._shipping = shipping

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
        if issubclass(PaymentSummaryInfoOperationsOperationAmountDetails, dict):
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
        if not isinstance(other, PaymentSummaryInfoOperationsOperationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
