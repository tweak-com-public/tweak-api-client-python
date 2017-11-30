# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.0
    
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


class ProductTag(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, tag_id=None, product_id=None, product=None, tag=None):
        """
        ProductTag - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'tag_id': 'str',
            'product_id': 'str',
            'product': 'Product',
            'tag': 'Tag'
        }

        self.attribute_map = {
            'id': 'id',
            'tag_id': 'tagId',
            'product_id': 'productId',
            'product': 'product',
            'tag': 'tag'
        }

        self._id = id
        self._tag_id = tag_id
        self._product_id = product_id
        self._product = product
        self._tag = tag


    @property
    def id(self):
        """
        Gets the id of this ProductTag.


        :return: The id of this ProductTag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductTag.


        :param id: The id of this ProductTag.
        :type: str
        """

        self._id = id

    @property
    def tag_id(self):
        """
        Gets the tag_id of this ProductTag.


        :return: The tag_id of this ProductTag.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """
        Sets the tag_id of this ProductTag.


        :param tag_id: The tag_id of this ProductTag.
        :type: str
        """

        self._tag_id = tag_id

    @property
    def product_id(self):
        """
        Gets the product_id of this ProductTag.


        :return: The product_id of this ProductTag.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ProductTag.


        :param product_id: The product_id of this ProductTag.
        :type: str
        """

        self._product_id = product_id

    @property
    def product(self):
        """
        Gets the product of this ProductTag.


        :return: The product of this ProductTag.
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this ProductTag.


        :param product: The product of this ProductTag.
        :type: Product
        """

        self._product = product

    @property
    def tag(self):
        """
        Gets the tag of this ProductTag.


        :return: The tag of this ProductTag.
        :rtype: Tag
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this ProductTag.


        :param tag: The tag of this ProductTag.
        :type: Tag
        """

        self._tag = tag

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
