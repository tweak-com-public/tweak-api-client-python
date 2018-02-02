# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.7-alpha.2
    
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


class Tag(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, created=None, modified=None, id=None, templates=None, designs=None, products=None):
        """
        Tag - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'templates': 'list[Template]',
            'designs': 'list[Design]',
            'products': 'list[Product]'
        }

        self.attribute_map = {
            'name': 'name',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'templates': 'templates',
            'designs': 'designs',
            'products': 'products'
        }

        self._name = name
        self._created = created
        self._modified = modified
        self._id = id
        self._templates = templates
        self._designs = designs
        self._products = products


    @property
    def name(self):
        """
        Gets the name of this Tag.


        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tag.


        :param name: The name of this Tag.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this Tag.


        :return: The created of this Tag.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Tag.


        :param created: The created of this Tag.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Tag.


        :return: The modified of this Tag.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Tag.


        :param modified: The modified of this Tag.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Tag.


        :return: The id of this Tag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tag.


        :param id: The id of this Tag.
        :type: str
        """

        self._id = id

    @property
    def templates(self):
        """
        Gets the templates of this Tag.


        :return: The templates of this Tag.
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this Tag.


        :param templates: The templates of this Tag.
        :type: list[Template]
        """

        self._templates = templates

    @property
    def designs(self):
        """
        Gets the designs of this Tag.


        :return: The designs of this Tag.
        :rtype: list[Design]
        """
        return self._designs

    @designs.setter
    def designs(self, designs):
        """
        Sets the designs of this Tag.


        :param designs: The designs of this Tag.
        :type: list[Design]
        """

        self._designs = designs

    @property
    def products(self):
        """
        Gets the products of this Tag.


        :return: The products of this Tag.
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this Tag.


        :param products: The products of this Tag.
        :type: list[Product]
        """

        self._products = products

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
