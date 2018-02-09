# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.2
    
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


class DynamicData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, properties_order=None, properties=None, relations=None, validations=None, created=None, modified=None, record_count=0.0, id=None, team_id=None, team=None, designs=None):
        """
        DynamicData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'properties_order': 'list[str]',
            'properties': 'object',
            'relations': 'object',
            'validations': 'object',
            'created': 'datetime',
            'modified': 'datetime',
            'record_count': 'float',
            'id': 'str',
            'team_id': 'str',
            'team': 'Team',
            'designs': 'list[Design]'
        }

        self.attribute_map = {
            'name': 'name',
            'properties_order': 'propertiesOrder',
            'properties': 'properties',
            'relations': 'relations',
            'validations': 'validations',
            'created': 'created',
            'modified': 'modified',
            'record_count': 'recordCount',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team',
            'designs': 'designs'
        }

        self._name = name
        self._properties_order = properties_order
        self._properties = properties
        self._relations = relations
        self._validations = validations
        self._created = created
        self._modified = modified
        self._record_count = record_count
        self._id = id
        self._team_id = team_id
        self._team = team
        self._designs = designs


    @property
    def name(self):
        """
        Gets the name of this DynamicData.


        :return: The name of this DynamicData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DynamicData.


        :param name: The name of this DynamicData.
        :type: str
        """

        self._name = name

    @property
    def properties_order(self):
        """
        Gets the properties_order of this DynamicData.


        :return: The properties_order of this DynamicData.
        :rtype: list[str]
        """
        return self._properties_order

    @properties_order.setter
    def properties_order(self, properties_order):
        """
        Sets the properties_order of this DynamicData.


        :param properties_order: The properties_order of this DynamicData.
        :type: list[str]
        """

        self._properties_order = properties_order

    @property
    def properties(self):
        """
        Gets the properties of this DynamicData.


        :return: The properties of this DynamicData.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this DynamicData.


        :param properties: The properties of this DynamicData.
        :type: object
        """

        self._properties = properties

    @property
    def relations(self):
        """
        Gets the relations of this DynamicData.


        :return: The relations of this DynamicData.
        :rtype: object
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """
        Sets the relations of this DynamicData.


        :param relations: The relations of this DynamicData.
        :type: object
        """

        self._relations = relations

    @property
    def validations(self):
        """
        Gets the validations of this DynamicData.


        :return: The validations of this DynamicData.
        :rtype: object
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """
        Sets the validations of this DynamicData.


        :param validations: The validations of this DynamicData.
        :type: object
        """

        self._validations = validations

    @property
    def created(self):
        """
        Gets the created of this DynamicData.


        :return: The created of this DynamicData.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DynamicData.


        :param created: The created of this DynamicData.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this DynamicData.


        :return: The modified of this DynamicData.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this DynamicData.


        :param modified: The modified of this DynamicData.
        :type: datetime
        """

        self._modified = modified

    @property
    def record_count(self):
        """
        Gets the record_count of this DynamicData.


        :return: The record_count of this DynamicData.
        :rtype: float
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """
        Sets the record_count of this DynamicData.


        :param record_count: The record_count of this DynamicData.
        :type: float
        """

        self._record_count = record_count

    @property
    def id(self):
        """
        Gets the id of this DynamicData.


        :return: The id of this DynamicData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DynamicData.


        :param id: The id of this DynamicData.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this DynamicData.


        :return: The team_id of this DynamicData.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this DynamicData.


        :param team_id: The team_id of this DynamicData.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this DynamicData.


        :return: The team of this DynamicData.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this DynamicData.


        :param team: The team of this DynamicData.
        :type: Team
        """

        self._team = team

    @property
    def designs(self):
        """
        Gets the designs of this DynamicData.


        :return: The designs of this DynamicData.
        :rtype: list[Design]
        """
        return self._designs

    @designs.setter
    def designs(self, designs):
        """
        Sets the designs of this DynamicData.


        :param designs: The designs of this DynamicData.
        :type: list[Design]
        """

        self._designs = designs

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
