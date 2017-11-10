# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.2-alpha.13
    
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


class TeamBuilderConfigProductGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, modified=None, id=None, product_group_id=None, builder_config_id=None, builder_config=None, product_group=None):
        """
        TeamBuilderConfigProductGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'product_group_id': 'str',
            'builder_config_id': 'str',
            'builder_config': 'TeamBuilderConfig',
            'product_group': 'ProductGroup'
        }

        self.attribute_map = {
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'product_group_id': 'productGroupId',
            'builder_config_id': 'builderConfigId',
            'builder_config': 'builderConfig',
            'product_group': 'productGroup'
        }

        self._created = created
        self._modified = modified
        self._id = id
        self._product_group_id = product_group_id
        self._builder_config_id = builder_config_id
        self._builder_config = builder_config
        self._product_group = product_group


    @property
    def created(self):
        """
        Gets the created of this TeamBuilderConfigProductGroup.


        :return: The created of this TeamBuilderConfigProductGroup.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this TeamBuilderConfigProductGroup.


        :param created: The created of this TeamBuilderConfigProductGroup.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this TeamBuilderConfigProductGroup.


        :return: The modified of this TeamBuilderConfigProductGroup.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this TeamBuilderConfigProductGroup.


        :param modified: The modified of this TeamBuilderConfigProductGroup.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this TeamBuilderConfigProductGroup.


        :return: The id of this TeamBuilderConfigProductGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamBuilderConfigProductGroup.


        :param id: The id of this TeamBuilderConfigProductGroup.
        :type: str
        """

        self._id = id

    @property
    def product_group_id(self):
        """
        Gets the product_group_id of this TeamBuilderConfigProductGroup.


        :return: The product_group_id of this TeamBuilderConfigProductGroup.
        :rtype: str
        """
        return self._product_group_id

    @product_group_id.setter
    def product_group_id(self, product_group_id):
        """
        Sets the product_group_id of this TeamBuilderConfigProductGroup.


        :param product_group_id: The product_group_id of this TeamBuilderConfigProductGroup.
        :type: str
        """

        self._product_group_id = product_group_id

    @property
    def builder_config_id(self):
        """
        Gets the builder_config_id of this TeamBuilderConfigProductGroup.


        :return: The builder_config_id of this TeamBuilderConfigProductGroup.
        :rtype: str
        """
        return self._builder_config_id

    @builder_config_id.setter
    def builder_config_id(self, builder_config_id):
        """
        Sets the builder_config_id of this TeamBuilderConfigProductGroup.


        :param builder_config_id: The builder_config_id of this TeamBuilderConfigProductGroup.
        :type: str
        """

        self._builder_config_id = builder_config_id

    @property
    def builder_config(self):
        """
        Gets the builder_config of this TeamBuilderConfigProductGroup.


        :return: The builder_config of this TeamBuilderConfigProductGroup.
        :rtype: TeamBuilderConfig
        """
        return self._builder_config

    @builder_config.setter
    def builder_config(self, builder_config):
        """
        Sets the builder_config of this TeamBuilderConfigProductGroup.


        :param builder_config: The builder_config of this TeamBuilderConfigProductGroup.
        :type: TeamBuilderConfig
        """

        self._builder_config = builder_config

    @property
    def product_group(self):
        """
        Gets the product_group of this TeamBuilderConfigProductGroup.


        :return: The product_group of this TeamBuilderConfigProductGroup.
        :rtype: ProductGroup
        """
        return self._product_group

    @product_group.setter
    def product_group(self, product_group):
        """
        Sets the product_group of this TeamBuilderConfigProductGroup.


        :param product_group: The product_group of this TeamBuilderConfigProductGroup.
        :type: ProductGroup
        """

        self._product_group = product_group

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
