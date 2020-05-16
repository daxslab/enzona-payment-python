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


class FullOperationsOperationAmountDetails(object):
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
        'shipping': 'int',
        'tax': 'int',
        'discount': 'int',
        'tip': 'int'
    }

    attribute_map = {
        'shipping': 'shipping',
        'tax': 'tax',
        'discount': 'discount',
        'tip': 'tip'
    }

    def __init__(self, shipping=None, tax=None, discount=None, tip=None):  # noqa: E501
        """FullOperationsOperationAmountDetails - a model defined in Swagger"""  # noqa: E501

        self._shipping = None
        self._tax = None
        self._discount = None
        self._tip = None
        self.discriminator = None

        if shipping is not None:
            self.shipping = shipping
        if tax is not None:
            self.tax = tax
        if discount is not None:
            self.discount = discount
        if tip is not None:
            self.tip = tip

    @property
    def shipping(self):
        """Gets the shipping of this FullOperationsOperationAmountDetails.  # noqa: E501


        :return: The shipping of this FullOperationsOperationAmountDetails.  # noqa: E501
        :rtype: int
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this FullOperationsOperationAmountDetails.


        :param shipping: The shipping of this FullOperationsOperationAmountDetails.  # noqa: E501
        :type: int
        """

        self._shipping = shipping

    @property
    def tax(self):
        """Gets the tax of this FullOperationsOperationAmountDetails.  # noqa: E501


        :return: The tax of this FullOperationsOperationAmountDetails.  # noqa: E501
        :rtype: int
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this FullOperationsOperationAmountDetails.


        :param tax: The tax of this FullOperationsOperationAmountDetails.  # noqa: E501
        :type: int
        """

        self._tax = tax

    @property
    def discount(self):
        """Gets the discount of this FullOperationsOperationAmountDetails.  # noqa: E501


        :return: The discount of this FullOperationsOperationAmountDetails.  # noqa: E501
        :rtype: int
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this FullOperationsOperationAmountDetails.


        :param discount: The discount of this FullOperationsOperationAmountDetails.  # noqa: E501
        :type: int
        """

        self._discount = discount

    @property
    def tip(self):
        """Gets the tip of this FullOperationsOperationAmountDetails.  # noqa: E501


        :return: The tip of this FullOperationsOperationAmountDetails.  # noqa: E501
        :rtype: int
        """
        return self._tip

    @tip.setter
    def tip(self, tip):
        """Sets the tip of this FullOperationsOperationAmountDetails.


        :param tip: The tip of this FullOperationsOperationAmountDetails.  # noqa: E501
        :type: int
        """

        self._tip = tip

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
        if issubclass(FullOperationsOperationAmountDetails, dict):
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
        if not isinstance(other, FullOperationsOperationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other