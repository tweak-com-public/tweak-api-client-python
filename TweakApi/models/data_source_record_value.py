# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.2
    
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


class DataSourceRecordValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, value=None, id=None, team_id=None, data_source_id=None, record_id=None, key_id=None, team=None, data_source=None, values=None, key=None):
        """
        DataSourceRecordValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'value': 'str',
            'id': 'str',
            'team_id': 'str',
            'data_source_id': 'str',
            'record_id': 'str',
            'key_id': 'str',
            'team': 'Team',
            'data_source': 'DataSource',
            'values': 'DataSourceRecord',
            'key': 'DataSourceKey'
        }

        self.attribute_map = {
            'value': 'value',
            'id': 'id',
            'team_id': 'teamId',
            'data_source_id': 'dataSourceId',
            'record_id': 'recordId',
            'key_id': 'keyId',
            'team': 'team',
            'data_source': 'dataSource',
            'values': 'values',
            'key': 'key'
        }

        self._value = value
        self._id = id
        self._team_id = team_id
        self._data_source_id = data_source_id
        self._record_id = record_id
        self._key_id = key_id
        self._team = team
        self._data_source = data_source
        self._values = values
        self._key = key


    @property
    def value(self):
        """
        Gets the value of this DataSourceRecordValue.


        :return: The value of this DataSourceRecordValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DataSourceRecordValue.


        :param value: The value of this DataSourceRecordValue.
        :type: str
        """

        self._value = value

    @property
    def id(self):
        """
        Gets the id of this DataSourceRecordValue.


        :return: The id of this DataSourceRecordValue.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataSourceRecordValue.


        :param id: The id of this DataSourceRecordValue.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this DataSourceRecordValue.


        :return: The team_id of this DataSourceRecordValue.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this DataSourceRecordValue.


        :param team_id: The team_id of this DataSourceRecordValue.
        :type: str
        """

        self._team_id = team_id

    @property
    def data_source_id(self):
        """
        Gets the data_source_id of this DataSourceRecordValue.


        :return: The data_source_id of this DataSourceRecordValue.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """
        Sets the data_source_id of this DataSourceRecordValue.


        :param data_source_id: The data_source_id of this DataSourceRecordValue.
        :type: str
        """

        self._data_source_id = data_source_id

    @property
    def record_id(self):
        """
        Gets the record_id of this DataSourceRecordValue.


        :return: The record_id of this DataSourceRecordValue.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """
        Sets the record_id of this DataSourceRecordValue.


        :param record_id: The record_id of this DataSourceRecordValue.
        :type: str
        """

        self._record_id = record_id

    @property
    def key_id(self):
        """
        Gets the key_id of this DataSourceRecordValue.


        :return: The key_id of this DataSourceRecordValue.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this DataSourceRecordValue.


        :param key_id: The key_id of this DataSourceRecordValue.
        :type: str
        """

        self._key_id = key_id

    @property
    def team(self):
        """
        Gets the team of this DataSourceRecordValue.


        :return: The team of this DataSourceRecordValue.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this DataSourceRecordValue.


        :param team: The team of this DataSourceRecordValue.
        :type: Team
        """

        self._team = team

    @property
    def data_source(self):
        """
        Gets the data_source of this DataSourceRecordValue.


        :return: The data_source of this DataSourceRecordValue.
        :rtype: DataSource
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """
        Sets the data_source of this DataSourceRecordValue.


        :param data_source: The data_source of this DataSourceRecordValue.
        :type: DataSource
        """

        self._data_source = data_source

    @property
    def values(self):
        """
        Gets the values of this DataSourceRecordValue.


        :return: The values of this DataSourceRecordValue.
        :rtype: DataSourceRecord
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this DataSourceRecordValue.


        :param values: The values of this DataSourceRecordValue.
        :type: DataSourceRecord
        """

        self._values = values

    @property
    def key(self):
        """
        Gets the key of this DataSourceRecordValue.


        :return: The key of this DataSourceRecordValue.
        :rtype: DataSourceKey
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataSourceRecordValue.


        :param key: The key of this DataSourceRecordValue.
        :type: DataSourceKey
        """

        self._key = key

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
