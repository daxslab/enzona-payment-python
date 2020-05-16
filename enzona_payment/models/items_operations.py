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


class ItemsOperations(object):
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
        'description': 'str',
        'quantity': 'int',
        'price': 'int',
        'tax': 'int',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'quantity': 'quantity',
        'price': 'price',
        'tax': 'tax',
        'name': 'name'
    }

    def __init__(self, description=None, quantity=None, price=None, tax=None, name=None):  # noqa: E501
        """ItemsOperations - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._quantity = None
        self._price = None
        self._tax = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if tax is not None:
            self.tax = tax
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this ItemsOperations.  # noqa: E501


        :return: The description of this ItemsOperations.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemsOperations.


        :param description: The description of this ItemsOperations.  # noqa: E501
        :type: str
        """
        # allowed_values = ["Pan"]  # noqa: E501
        # if description not in allowed_values:
        #     raise ValueError(
        #         "Invalid value for `description` ({0}), must be one of {1}"  # noqa: E501
        #         .format(description, allowed_values)
        #     )

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this ItemsOperations.  # noqa: E501


        :return: The quantity of this ItemsOperations.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ItemsOperations.


        :param quantity: The quantity of this ItemsOperations.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this ItemsOperations.  # noqa: E501


        :return: The price of this ItemsOperations.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ItemsOperations.


        :param price: The price of this ItemsOperations.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def tax(self):
        """Gets the tax of this ItemsOperations.  # noqa: E501


        :return: The tax of this ItemsOperations.  # noqa: E501
        :rtype: int
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this ItemsOperations.


        :param tax: The tax of this ItemsOperations.  # noqa: E501
        :type: int
        """

        self._tax = tax

    @property
    def name(self):
        """Gets the name of this ItemsOperations.  # noqa: E501


        :return: The name of this ItemsOperations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemsOperations.


        :param name: The name of this ItemsOperations.  # noqa: E501
        :type: str
        """
        # allowed_values = ["Arroz a la Cubana"]  # noqa: E501
        # if name not in allowed_values:
        #     raise ValueError(
        #         "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
        #         .format(name, allowed_values)
        #     )

        self._name = name

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
        if issubclass(ItemsOperations, dict):
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
        if not isinstance(other, ItemsOperations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
