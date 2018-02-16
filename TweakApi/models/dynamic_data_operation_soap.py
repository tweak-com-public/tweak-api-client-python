# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.10
    
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


class DynamicDataOperationSoap(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, params=None, root=None, parse_root_xml=False, map=None, id=None):
        """
        DynamicDataOperationSoap - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'params': 'object',
            'root': 'XAny',
            'parse_root_xml': 'bool',
            'map': 'XAny',
            'id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'params': 'params',
            'root': 'root',
            'parse_root_xml': 'parseRootXml',
            'map': 'map',
            'id': 'id'
        }

        self._name = name
        self._params = params
        self._root = root
        self._parse_root_xml = parse_root_xml
        self._map = map
        self._id = id


    @property
    def name(self):
        """
        Gets the name of this DynamicDataOperationSoap.


        :return: The name of this DynamicDataOperationSoap.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DynamicDataOperationSoap.


        :param name: The name of this DynamicDataOperationSoap.
        :type: str
        """

        self._name = name

    @property
    def params(self):
        """
        Gets the params of this DynamicDataOperationSoap.


        :return: The params of this DynamicDataOperationSoap.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this DynamicDataOperationSoap.


        :param params: The params of this DynamicDataOperationSoap.
        :type: object
        """

        self._params = params

    @property
    def root(self):
        """
        Gets the root of this DynamicDataOperationSoap.


        :return: The root of this DynamicDataOperationSoap.
        :rtype: XAny
        """
        return self._root

    @root.setter
    def root(self, root):
        """
        Sets the root of this DynamicDataOperationSoap.


        :param root: The root of this DynamicDataOperationSoap.
        :type: XAny
        """

        self._root = root

    @property
    def parse_root_xml(self):
        """
        Gets the parse_root_xml of this DynamicDataOperationSoap.


        :return: The parse_root_xml of this DynamicDataOperationSoap.
        :rtype: bool
        """
        return self._parse_root_xml

    @parse_root_xml.setter
    def parse_root_xml(self, parse_root_xml):
        """
        Sets the parse_root_xml of this DynamicDataOperationSoap.


        :param parse_root_xml: The parse_root_xml of this DynamicDataOperationSoap.
        :type: bool
        """

        self._parse_root_xml = parse_root_xml

    @property
    def map(self):
        """
        Gets the map of this DynamicDataOperationSoap.


        :return: The map of this DynamicDataOperationSoap.
        :rtype: XAny
        """
        return self._map

    @map.setter
    def map(self, map):
        """
        Sets the map of this DynamicDataOperationSoap.


        :param map: The map of this DynamicDataOperationSoap.
        :type: XAny
        """

        self._map = map

    @property
    def id(self):
        """
        Gets the id of this DynamicDataOperationSoap.


        :return: The id of this DynamicDataOperationSoap.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DynamicDataOperationSoap.


        :param id: The id of this DynamicDataOperationSoap.
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
