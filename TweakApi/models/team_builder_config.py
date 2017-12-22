# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.4-alpha.9
    
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


class TeamBuilderConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, debug_mode=False, features=None, ui=None, created=None, modified=None, id=None, team_id=None, team=None, product_groups=None, product_types=None, product_sizes=None, product_size_materials=None, product_size_materials_rel=None):
        """
        TeamBuilderConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'debug_mode': 'bool',
            'features': 'object',
            'ui': 'object',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'team': 'Team',
            'product_groups': 'list[ProductGroup]',
            'product_types': 'list[ProductType]',
            'product_sizes': 'list[ProductSize]',
            'product_size_materials': 'list[ProductSizeMaterial]',
            'product_size_materials_rel': 'list[TeamBuilderConfigProductSizeMaterial]'
        }

        self.attribute_map = {
            'name': 'name',
            'debug_mode': 'debugMode',
            'features': 'features',
            'ui': 'ui',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team',
            'product_groups': 'productGroups',
            'product_types': 'productTypes',
            'product_sizes': 'productSizes',
            'product_size_materials': 'productSizeMaterials',
            'product_size_materials_rel': 'productSizeMaterialsRel'
        }

        self._name = name
        self._debug_mode = debug_mode
        self._features = features
        self._ui = ui
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._team = team
        self._product_groups = product_groups
        self._product_types = product_types
        self._product_sizes = product_sizes
        self._product_size_materials = product_size_materials
        self._product_size_materials_rel = product_size_materials_rel


    @property
    def name(self):
        """
        Gets the name of this TeamBuilderConfig.


        :return: The name of this TeamBuilderConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TeamBuilderConfig.


        :param name: The name of this TeamBuilderConfig.
        :type: str
        """

        self._name = name

    @property
    def debug_mode(self):
        """
        Gets the debug_mode of this TeamBuilderConfig.


        :return: The debug_mode of this TeamBuilderConfig.
        :rtype: bool
        """
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, debug_mode):
        """
        Sets the debug_mode of this TeamBuilderConfig.


        :param debug_mode: The debug_mode of this TeamBuilderConfig.
        :type: bool
        """

        self._debug_mode = debug_mode

    @property
    def features(self):
        """
        Gets the features of this TeamBuilderConfig.


        :return: The features of this TeamBuilderConfig.
        :rtype: object
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this TeamBuilderConfig.


        :param features: The features of this TeamBuilderConfig.
        :type: object
        """

        self._features = features

    @property
    def ui(self):
        """
        Gets the ui of this TeamBuilderConfig.


        :return: The ui of this TeamBuilderConfig.
        :rtype: object
        """
        return self._ui

    @ui.setter
    def ui(self, ui):
        """
        Sets the ui of this TeamBuilderConfig.


        :param ui: The ui of this TeamBuilderConfig.
        :type: object
        """

        self._ui = ui

    @property
    def created(self):
        """
        Gets the created of this TeamBuilderConfig.


        :return: The created of this TeamBuilderConfig.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this TeamBuilderConfig.


        :param created: The created of this TeamBuilderConfig.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this TeamBuilderConfig.


        :return: The modified of this TeamBuilderConfig.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this TeamBuilderConfig.


        :param modified: The modified of this TeamBuilderConfig.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this TeamBuilderConfig.


        :return: The id of this TeamBuilderConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamBuilderConfig.


        :param id: The id of this TeamBuilderConfig.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this TeamBuilderConfig.


        :return: The team_id of this TeamBuilderConfig.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this TeamBuilderConfig.


        :param team_id: The team_id of this TeamBuilderConfig.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this TeamBuilderConfig.


        :return: The team of this TeamBuilderConfig.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this TeamBuilderConfig.


        :param team: The team of this TeamBuilderConfig.
        :type: Team
        """

        self._team = team

    @property
    def product_groups(self):
        """
        Gets the product_groups of this TeamBuilderConfig.


        :return: The product_groups of this TeamBuilderConfig.
        :rtype: list[ProductGroup]
        """
        return self._product_groups

    @product_groups.setter
    def product_groups(self, product_groups):
        """
        Sets the product_groups of this TeamBuilderConfig.


        :param product_groups: The product_groups of this TeamBuilderConfig.
        :type: list[ProductGroup]
        """

        self._product_groups = product_groups

    @property
    def product_types(self):
        """
        Gets the product_types of this TeamBuilderConfig.


        :return: The product_types of this TeamBuilderConfig.
        :rtype: list[ProductType]
        """
        return self._product_types

    @product_types.setter
    def product_types(self, product_types):
        """
        Sets the product_types of this TeamBuilderConfig.


        :param product_types: The product_types of this TeamBuilderConfig.
        :type: list[ProductType]
        """

        self._product_types = product_types

    @property
    def product_sizes(self):
        """
        Gets the product_sizes of this TeamBuilderConfig.


        :return: The product_sizes of this TeamBuilderConfig.
        :rtype: list[ProductSize]
        """
        return self._product_sizes

    @product_sizes.setter
    def product_sizes(self, product_sizes):
        """
        Sets the product_sizes of this TeamBuilderConfig.


        :param product_sizes: The product_sizes of this TeamBuilderConfig.
        :type: list[ProductSize]
        """

        self._product_sizes = product_sizes

    @property
    def product_size_materials(self):
        """
        Gets the product_size_materials of this TeamBuilderConfig.


        :return: The product_size_materials of this TeamBuilderConfig.
        :rtype: list[ProductSizeMaterial]
        """
        return self._product_size_materials

    @product_size_materials.setter
    def product_size_materials(self, product_size_materials):
        """
        Sets the product_size_materials of this TeamBuilderConfig.


        :param product_size_materials: The product_size_materials of this TeamBuilderConfig.
        :type: list[ProductSizeMaterial]
        """

        self._product_size_materials = product_size_materials

    @property
    def product_size_materials_rel(self):
        """
        Gets the product_size_materials_rel of this TeamBuilderConfig.


        :return: The product_size_materials_rel of this TeamBuilderConfig.
        :rtype: list[TeamBuilderConfigProductSizeMaterial]
        """
        return self._product_size_materials_rel

    @product_size_materials_rel.setter
    def product_size_materials_rel(self, product_size_materials_rel):
        """
        Sets the product_size_materials_rel of this TeamBuilderConfig.


        :param product_size_materials_rel: The product_size_materials_rel of this TeamBuilderConfig.
        :type: list[TeamBuilderConfigProductSizeMaterial]
        """

        self._product_size_materials_rel = product_size_materials_rel

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
