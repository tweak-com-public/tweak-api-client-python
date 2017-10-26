# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.2-alpha.4
    
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


class DataSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, created=None, modified=None, id=None, team_id=None, team=None, keys=None):
        """
        DataSource - a model defined in Swagger

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
            'team_id': 'str',
            'team': 'Team',
            'keys': 'list[DataSourceKey]'
        }

        self.attribute_map = {
            'name': 'name',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team',
            'keys': 'keys'
        }

        self._name = name
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._team = team
        self._keys = keys


    @property
    def name(self):
        """
        Gets the name of this DataSource.


        :return: The name of this DataSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataSource.


        :param name: The name of this DataSource.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this DataSource.


        :return: The created of this DataSource.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DataSource.


        :param created: The created of this DataSource.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this DataSource.


        :return: The modified of this DataSource.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this DataSource.


        :param modified: The modified of this DataSource.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this DataSource.


        :return: The id of this DataSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataSource.


        :param id: The id of this DataSource.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this DataSource.


        :return: The team_id of this DataSource.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this DataSource.


        :param team_id: The team_id of this DataSource.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this DataSource.


        :return: The team of this DataSource.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this DataSource.


        :param team: The team of this DataSource.
        :type: Team
        """

        self._team = team

    @property
    def keys(self):
        """
        Gets the keys of this DataSource.


        :return: The keys of this DataSource.
        :rtype: list[DataSourceKey]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """
        Sets the keys of this DataSource.


        :param keys: The keys of this DataSource.
        :type: list[DataSourceKey]
        """

        self._keys = keys

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
