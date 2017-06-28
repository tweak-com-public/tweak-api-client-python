# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class CustomerPermissionSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, tweak_email=True, id=None, customer_id=None, customer=None):
        """
        CustomerPermissionSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'tweak_email': 'bool',
            'id': 'str',
            'customer_id': 'str',
            'customer': 'Customer'
        }

        self.attribute_map = {
            'tweak_email': 'tweakEmail',
            'id': 'id',
            'customer_id': 'customerId',
            'customer': 'customer'
        }

        self._tweak_email = tweak_email
        self._id = id
        self._customer_id = customer_id
        self._customer = customer


    @property
    def tweak_email(self):
        """
        Gets the tweak_email of this CustomerPermissionSet.


        :return: The tweak_email of this CustomerPermissionSet.
        :rtype: bool
        """
        return self._tweak_email

    @tweak_email.setter
    def tweak_email(self, tweak_email):
        """
        Sets the tweak_email of this CustomerPermissionSet.


        :param tweak_email: The tweak_email of this CustomerPermissionSet.
        :type: bool
        """

        self._tweak_email = tweak_email

    @property
    def id(self):
        """
        Gets the id of this CustomerPermissionSet.


        :return: The id of this CustomerPermissionSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomerPermissionSet.


        :param id: The id of this CustomerPermissionSet.
        :type: str
        """

        self._id = id

    @property
    def customer_id(self):
        """
        Gets the customer_id of this CustomerPermissionSet.


        :return: The customer_id of this CustomerPermissionSet.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this CustomerPermissionSet.


        :param customer_id: The customer_id of this CustomerPermissionSet.
        :type: str
        """

        self._customer_id = customer_id

    @property
    def customer(self):
        """
        Gets the customer of this CustomerPermissionSet.


        :return: The customer of this CustomerPermissionSet.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this CustomerPermissionSet.


        :param customer: The customer of this CustomerPermissionSet.
        :type: Customer
        """

        self._customer = customer

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
