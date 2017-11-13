# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.0
    
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


class Bounds(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, top=0.0, bottom=0.0, left=0.0, right=0.0, id=None):
        """
        Bounds - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'top': 'float',
            'bottom': 'float',
            'left': 'float',
            'right': 'float',
            'id': 'str'
        }

        self.attribute_map = {
            'top': 'top',
            'bottom': 'bottom',
            'left': 'left',
            'right': 'right',
            'id': 'id'
        }

        self._top = top
        self._bottom = bottom
        self._left = left
        self._right = right
        self._id = id


    @property
    def top(self):
        """
        Gets the top of this Bounds.


        :return: The top of this Bounds.
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """
        Sets the top of this Bounds.


        :param top: The top of this Bounds.
        :type: float
        """

        if not top:
            raise ValueError("Invalid value for `top`, must not be `None`")
        if top < 0.0:
            raise ValueError("Invalid value for `top`, must be a value greater than or equal to `0.0`")

        self._top = top

    @property
    def bottom(self):
        """
        Gets the bottom of this Bounds.


        :return: The bottom of this Bounds.
        :rtype: float
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """
        Sets the bottom of this Bounds.


        :param bottom: The bottom of this Bounds.
        :type: float
        """

        if not bottom:
            raise ValueError("Invalid value for `bottom`, must not be `None`")
        if bottom < 0.0:
            raise ValueError("Invalid value for `bottom`, must be a value greater than or equal to `0.0`")

        self._bottom = bottom

    @property
    def left(self):
        """
        Gets the left of this Bounds.


        :return: The left of this Bounds.
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """
        Sets the left of this Bounds.


        :param left: The left of this Bounds.
        :type: float
        """

        if not left:
            raise ValueError("Invalid value for `left`, must not be `None`")
        if left < 0.0:
            raise ValueError("Invalid value for `left`, must be a value greater than or equal to `0.0`")

        self._left = left

    @property
    def right(self):
        """
        Gets the right of this Bounds.


        :return: The right of this Bounds.
        :rtype: float
        """
        return self._right

    @right.setter
    def right(self, right):
        """
        Sets the right of this Bounds.


        :param right: The right of this Bounds.
        :type: float
        """

        if not right:
            raise ValueError("Invalid value for `right`, must not be `None`")
        if right < 0.0:
            raise ValueError("Invalid value for `right`, must be a value greater than or equal to `0.0`")

        self._right = right

    @property
    def id(self):
        """
        Gets the id of this Bounds.


        :return: The id of this Bounds.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Bounds.


        :param id: The id of this Bounds.
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
