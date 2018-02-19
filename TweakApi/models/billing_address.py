# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-beta.0
    
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


class BillingAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, city=None, country=None, line1=None, line2=None, postal_code=None, state=None, id=None):
        """
        BillingAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'city': 'str',
            'country': 'str',
            'line1': 'str',
            'line2': 'str',
            'postal_code': 'str',
            'state': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'city': 'city',
            'country': 'country',
            'line1': 'line1',
            'line2': 'line2',
            'postal_code': 'postalCode',
            'state': 'state',
            'id': 'id'
        }

        self._city = city
        self._country = country
        self._line1 = line1
        self._line2 = line2
        self._postal_code = postal_code
        self._state = state
        self._id = id


    @property
    def city(self):
        """
        Gets the city of this BillingAddress.


        :return: The city of this BillingAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this BillingAddress.


        :param city: The city of this BillingAddress.
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """
        Gets the country of this BillingAddress.


        :return: The country of this BillingAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillingAddress.


        :param country: The country of this BillingAddress.
        :type: str
        """

        self._country = country

    @property
    def line1(self):
        """
        Gets the line1 of this BillingAddress.


        :return: The line1 of this BillingAddress.
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """
        Sets the line1 of this BillingAddress.


        :param line1: The line1 of this BillingAddress.
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """
        Gets the line2 of this BillingAddress.


        :return: The line2 of this BillingAddress.
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """
        Sets the line2 of this BillingAddress.


        :param line2: The line2 of this BillingAddress.
        :type: str
        """

        self._line2 = line2

    @property
    def postal_code(self):
        """
        Gets the postal_code of this BillingAddress.


        :return: The postal_code of this BillingAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this BillingAddress.


        :param postal_code: The postal_code of this BillingAddress.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """
        Gets the state of this BillingAddress.


        :return: The state of this BillingAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this BillingAddress.


        :param state: The state of this BillingAddress.
        :type: str
        """

        self._state = state

    @property
    def id(self):
        """
        Gets the id of this BillingAddress.


        :return: The id of this BillingAddress.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingAddress.


        :param id: The id of this BillingAddress.
        :type: str
        """

        self._id = id

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
