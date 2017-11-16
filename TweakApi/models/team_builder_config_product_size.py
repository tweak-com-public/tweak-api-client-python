# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.3
    
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


class TeamBuilderConfigProductSize(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, modified=None, id=None, product_size_id=None, builder_config_id=None, builder_config=None, product_size=None):
        """
        TeamBuilderConfigProductSize - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'product_size_id': 'str',
            'builder_config_id': 'str',
            'builder_config': 'TeamBuilderConfig',
            'product_size': 'ProductSize'
        }

        self.attribute_map = {
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'product_size_id': 'productSizeId',
            'builder_config_id': 'builderConfigId',
            'builder_config': 'builderConfig',
            'product_size': 'productSize'
        }

        self._created = created
        self._modified = modified
        self._id = id
        self._product_size_id = product_size_id
        self._builder_config_id = builder_config_id
        self._builder_config = builder_config
        self._product_size = product_size


    @property
    def created(self):
        """
        Gets the created of this TeamBuilderConfigProductSize.


        :return: The created of this TeamBuilderConfigProductSize.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this TeamBuilderConfigProductSize.


        :param created: The created of this TeamBuilderConfigProductSize.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this TeamBuilderConfigProductSize.


        :return: The modified of this TeamBuilderConfigProductSize.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this TeamBuilderConfigProductSize.


        :param modified: The modified of this TeamBuilderConfigProductSize.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this TeamBuilderConfigProductSize.


        :return: The id of this TeamBuilderConfigProductSize.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamBuilderConfigProductSize.


        :param id: The id of this TeamBuilderConfigProductSize.
        :type: str
        """

        self._id = id

    @property
    def product_size_id(self):
        """
        Gets the product_size_id of this TeamBuilderConfigProductSize.


        :return: The product_size_id of this TeamBuilderConfigProductSize.
        :rtype: str
        """
        return self._product_size_id

    @product_size_id.setter
    def product_size_id(self, product_size_id):
        """
        Sets the product_size_id of this TeamBuilderConfigProductSize.


        :param product_size_id: The product_size_id of this TeamBuilderConfigProductSize.
        :type: str
        """

        self._product_size_id = product_size_id

    @property
    def builder_config_id(self):
        """
        Gets the builder_config_id of this TeamBuilderConfigProductSize.


        :return: The builder_config_id of this TeamBuilderConfigProductSize.
        :rtype: str
        """
        return self._builder_config_id

    @builder_config_id.setter
    def builder_config_id(self, builder_config_id):
        """
        Sets the builder_config_id of this TeamBuilderConfigProductSize.


        :param builder_config_id: The builder_config_id of this TeamBuilderConfigProductSize.
        :type: str
        """

        self._builder_config_id = builder_config_id

    @property
    def builder_config(self):
        """
        Gets the builder_config of this TeamBuilderConfigProductSize.


        :return: The builder_config of this TeamBuilderConfigProductSize.
        :rtype: TeamBuilderConfig
        """
        return self._builder_config

    @builder_config.setter
    def builder_config(self, builder_config):
        """
        Sets the builder_config of this TeamBuilderConfigProductSize.


        :param builder_config: The builder_config of this TeamBuilderConfigProductSize.
        :type: TeamBuilderConfig
        """

        self._builder_config = builder_config

    @property
    def product_size(self):
        """
        Gets the product_size of this TeamBuilderConfigProductSize.


        :return: The product_size of this TeamBuilderConfigProductSize.
        :rtype: ProductSize
        """
        return self._product_size

    @product_size.setter
    def product_size(self, product_size):
        """
        Sets the product_size of this TeamBuilderConfigProductSize.


        :param product_size: The product_size of this TeamBuilderConfigProductSize.
        :type: ProductSize
        """

        self._product_size = product_size

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
