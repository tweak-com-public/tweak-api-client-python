# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3
    
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


class BillingLimitCounter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, limit=0.0, count=0.0, unit_type=None, unit_prefix=None, id=None):
        """
        BillingLimitCounter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'limit': 'float',
            'count': 'float',
            'unit_type': 'str',
            'unit_prefix': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'limit': 'limit',
            'count': 'count',
            'unit_type': 'unitType',
            'unit_prefix': 'unitPrefix',
            'id': 'id'
        }

        self._limit = limit
        self._count = count
        self._unit_type = unit_type
        self._unit_prefix = unit_prefix
        self._id = id


    @property
    def limit(self):
        """
        Gets the limit of this BillingLimitCounter.


        :return: The limit of this BillingLimitCounter.
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this BillingLimitCounter.


        :param limit: The limit of this BillingLimitCounter.
        :type: float
        """

        self._limit = limit

    @property
    def count(self):
        """
        Gets the count of this BillingLimitCounter.


        :return: The count of this BillingLimitCounter.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this BillingLimitCounter.


        :param count: The count of this BillingLimitCounter.
        :type: float
        """

        self._count = count

    @property
    def unit_type(self):
        """
        Gets the unit_type of this BillingLimitCounter.


        :return: The unit_type of this BillingLimitCounter.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """
        Sets the unit_type of this BillingLimitCounter.


        :param unit_type: The unit_type of this BillingLimitCounter.
        :type: str
        """
        allowed_values = ["none", "binary"]
        if unit_type not in allowed_values:
            raise ValueError(
                "Invalid value for `unit_type` ({0}), must be one of {1}"
                .format(unit_type, allowed_values)
            )

        self._unit_type = unit_type

    @property
    def unit_prefix(self):
        """
        Gets the unit_prefix of this BillingLimitCounter.


        :return: The unit_prefix of this BillingLimitCounter.
        :rtype: str
        """
        return self._unit_prefix

    @unit_prefix.setter
    def unit_prefix(self, unit_prefix):
        """
        Sets the unit_prefix of this BillingLimitCounter.


        :param unit_prefix: The unit_prefix of this BillingLimitCounter.
        :type: str
        """

        self._unit_prefix = unit_prefix

    @property
    def id(self):
        """
        Gets the id of this BillingLimitCounter.


        :return: The id of this BillingLimitCounter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingLimitCounter.


        :param id: The id of this BillingLimitCounter.
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
