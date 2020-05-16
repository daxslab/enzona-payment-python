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

from enzona_payment.models.pagination_links_first_page import PaginationLinksFirstPage  # noqa: F401,E501


class PaginationLinks(object):
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
        'first_page': 'PaginationLinksFirstPage',
        'last_page': 'PaginationLinksFirstPage',
        'next_page': 'PaginationLinksFirstPage',
        'prev_page': 'PaginationLinksFirstPage'
    }

    attribute_map = {
        'first_page': 'first_page',
        'last_page': 'last_page',
        'next_page': 'next_page',
        'prev_page': 'prev_page'
    }

    def __init__(self, first_page=None, last_page=None, next_page=None, prev_page=None):  # noqa: E501
        """PaginationLinks - a model defined in Swagger"""  # noqa: E501

        self._first_page = None
        self._last_page = None
        self._next_page = None
        self._prev_page = None
        self.discriminator = None

        if first_page is not None:
            self.first_page = first_page
        if last_page is not None:
            self.last_page = last_page
        if next_page is not None:
            self.next_page = next_page
        if prev_page is not None:
            self.prev_page = prev_page

    @property
    def first_page(self):
        """Gets the first_page of this PaginationLinks.  # noqa: E501


        :return: The first_page of this PaginationLinks.  # noqa: E501
        :rtype: PaginationLinksFirstPage
        """
        return self._first_page

    @first_page.setter
    def first_page(self, first_page):
        """Sets the first_page of this PaginationLinks.


        :param first_page: The first_page of this PaginationLinks.  # noqa: E501
        :type: PaginationLinksFirstPage
        """

        self._first_page = first_page

    @property
    def last_page(self):
        """Gets the last_page of this PaginationLinks.  # noqa: E501


        :return: The last_page of this PaginationLinks.  # noqa: E501
        :rtype: PaginationLinksFirstPage
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this PaginationLinks.


        :param last_page: The last_page of this PaginationLinks.  # noqa: E501
        :type: PaginationLinksFirstPage
        """

        self._last_page = last_page

    @property
    def next_page(self):
        """Gets the next_page of this PaginationLinks.  # noqa: E501


        :return: The next_page of this PaginationLinks.  # noqa: E501
        :rtype: PaginationLinksFirstPage
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this PaginationLinks.


        :param next_page: The next_page of this PaginationLinks.  # noqa: E501
        :type: PaginationLinksFirstPage
        """

        self._next_page = next_page

    @property
    def prev_page(self):
        """Gets the prev_page of this PaginationLinks.  # noqa: E501


        :return: The prev_page of this PaginationLinks.  # noqa: E501
        :rtype: PaginationLinksFirstPage
        """
        return self._prev_page

    @prev_page.setter
    def prev_page(self, prev_page):
        """Sets the prev_page of this PaginationLinks.


        :param prev_page: The prev_page of this PaginationLinks.  # noqa: E501
        :type: PaginationLinksFirstPage
        """

        self._prev_page = prev_page

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
        if issubclass(PaginationLinks, dict):
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
        if not isinstance(other, PaginationLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other