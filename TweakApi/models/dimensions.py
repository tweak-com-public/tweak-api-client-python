# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.2
    
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


class Dimensions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, width=None, height=None, depth=None, id=None):
        """
        Dimensions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'width': 'float',
            'height': 'float',
            'depth': 'float',
            'id': 'str'
        }

        self.attribute_map = {
            'width': 'width',
            'height': 'height',
            'depth': 'depth',
            'id': 'id'
        }

        self._width = width
        self._height = height
        self._depth = depth
        self._id = id


    @property
    def width(self):
        """
        Gets the width of this Dimensions.


        :return: The width of this Dimensions.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this Dimensions.


        :param width: The width of this Dimensions.
        :type: float
        """

        if not width:
            raise ValueError("Invalid value for `width`, must not be `None`")
        if width < 0.0:
            raise ValueError("Invalid value for `width`, must be a value greater than or equal to `0.0`")

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this Dimensions.


        :return: The height of this Dimensions.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this Dimensions.


        :param height: The height of this Dimensions.
        :type: float
        """

        if not height:
            raise ValueError("Invalid value for `height`, must not be `None`")
        if height < 0.0:
            raise ValueError("Invalid value for `height`, must be a value greater than or equal to `0.0`")

        self._height = height

    @property
    def depth(self):
        """
        Gets the depth of this Dimensions.


        :return: The depth of this Dimensions.
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        Sets the depth of this Dimensions.


        :param depth: The depth of this Dimensions.
        :type: float
        """

        if not depth:
            raise ValueError("Invalid value for `depth`, must not be `None`")
        if depth < 0.0:
            raise ValueError("Invalid value for `depth`, must be a value greater than or equal to `0.0`")

        self._depth = depth

    @property
    def id(self):
        """
        Gets the id of this Dimensions.


        :return: The id of this Dimensions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Dimensions.


        :param id: The id of this Dimensions.
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
