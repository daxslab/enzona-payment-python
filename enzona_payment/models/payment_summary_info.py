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

from enzona_payment.models.payment_summary_info_operations import PaymentSummaryInfoOperations  # noqa: F401,E501


class PaymentSummaryInfo(object):
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
        'id': 'str',
        'created_at': 'datetime',
        'update_at': 'datetime',
        'state': 'str',
        'operations': 'PaymentSummaryInfoOperations'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'update_at': 'update_at',
        'state': 'state',
        'operations': 'operations'
    }

    def __init__(self, id=None, created_at=None, update_at=None, state=None, operations=None):  # noqa: E501
        """PaymentSummaryInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._update_at = None
        self._state = None
        self._operations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at
        if state is not None:
            self.state = state
        if operations is not None:
            self.operations = operations

    @property
    def id(self):
        """Gets the id of this PaymentSummaryInfo.  # noqa: E501


        :return: The id of this PaymentSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentSummaryInfo.


        :param id: The id of this PaymentSummaryInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this PaymentSummaryInfo.  # noqa: E501


        :return: The created_at of this PaymentSummaryInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentSummaryInfo.


        :param created_at: The created_at of this PaymentSummaryInfo.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def update_at(self):
        """Gets the update_at of this PaymentSummaryInfo.  # noqa: E501


        :return: The update_at of this PaymentSummaryInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this PaymentSummaryInfo.


        :param update_at: The update_at of this PaymentSummaryInfo.  # noqa: E501
        :type: datetime
        """

        self._update_at = update_at

    @property
    def state(self):
        """Gets the state of this PaymentSummaryInfo.  # noqa: E501


        :return: The state of this PaymentSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentSummaryInfo.


        :param state: The state of this PaymentSummaryInfo.  # noqa: E501
        :type: str
        """
        # allowed_values = ["created", "approved", "completed"]  # noqa: E501
        # if state not in allowed_values:
        #     raise ValueError(
        #         "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
        #         .format(state, allowed_values)
        #     )

        self._state = state

    @property
    def operations(self):
        """Gets the operations of this PaymentSummaryInfo.  # noqa: E501


        :return: The operations of this PaymentSummaryInfo.  # noqa: E501
        :rtype: PaymentSummaryInfoOperations
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this PaymentSummaryInfo.


        :param operations: The operations of this PaymentSummaryInfo.  # noqa: E501
        :type: PaymentSummaryInfoOperations
        """

        self._operations = operations

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
        if issubclass(PaymentSummaryInfo, dict):
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
        if not isinstance(other, PaymentSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other