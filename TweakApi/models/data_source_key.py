# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.4-alpha.4
    
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


class DataSourceKey(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, label=None, column=None, value_default=None, primary_key=False, value_required=False, value_min=0.0, value_max=0.0, value_type=None, id=None, team_id=None, data_source_id=None, team=None, data_source=None, record_values=None):
        """
        DataSourceKey - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'label': 'str',
            'column': 'float',
            'value_default': 'str',
            'primary_key': 'bool',
            'value_required': 'bool',
            'value_min': 'float',
            'value_max': 'float',
            'value_type': 'str',
            'id': 'str',
            'team_id': 'str',
            'data_source_id': 'str',
            'team': 'Team',
            'data_source': 'DataSource',
            'record_values': 'list[DataSourceRecordValue]'
        }

        self.attribute_map = {
            'label': 'label',
            'column': 'column',
            'value_default': 'valueDefault',
            'primary_key': 'primaryKey',
            'value_required': 'valueRequired',
            'value_min': 'valueMin',
            'value_max': 'valueMax',
            'value_type': 'valueType',
            'id': 'id',
            'team_id': 'teamId',
            'data_source_id': 'dataSourceId',
            'team': 'team',
            'data_source': 'dataSource',
            'record_values': 'recordValues'
        }

        self._label = label
        self._column = column
        self._value_default = value_default
        self._primary_key = primary_key
        self._value_required = value_required
        self._value_min = value_min
        self._value_max = value_max
        self._value_type = value_type
        self._id = id
        self._team_id = team_id
        self._data_source_id = data_source_id
        self._team = team
        self._data_source = data_source
        self._record_values = record_values


    @property
    def label(self):
        """
        Gets the label of this DataSourceKey.


        :return: The label of this DataSourceKey.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this DataSourceKey.


        :param label: The label of this DataSourceKey.
        :type: str
        """

        self._label = label

    @property
    def column(self):
        """
        Gets the column of this DataSourceKey.


        :return: The column of this DataSourceKey.
        :rtype: float
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this DataSourceKey.


        :param column: The column of this DataSourceKey.
        :type: float
        """

        self._column = column

    @property
    def value_default(self):
        """
        Gets the value_default of this DataSourceKey.


        :return: The value_default of this DataSourceKey.
        :rtype: str
        """
        return self._value_default

    @value_default.setter
    def value_default(self, value_default):
        """
        Sets the value_default of this DataSourceKey.


        :param value_default: The value_default of this DataSourceKey.
        :type: str
        """

        self._value_default = value_default

    @property
    def primary_key(self):
        """
        Gets the primary_key of this DataSourceKey.


        :return: The primary_key of this DataSourceKey.
        :rtype: bool
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """
        Sets the primary_key of this DataSourceKey.


        :param primary_key: The primary_key of this DataSourceKey.
        :type: bool
        """

        self._primary_key = primary_key

    @property
    def value_required(self):
        """
        Gets the value_required of this DataSourceKey.


        :return: The value_required of this DataSourceKey.
        :rtype: bool
        """
        return self._value_required

    @value_required.setter
    def value_required(self, value_required):
        """
        Sets the value_required of this DataSourceKey.


        :param value_required: The value_required of this DataSourceKey.
        :type: bool
        """

        self._value_required = value_required

    @property
    def value_min(self):
        """
        Gets the value_min of this DataSourceKey.


        :return: The value_min of this DataSourceKey.
        :rtype: float
        """
        return self._value_min

    @value_min.setter
    def value_min(self, value_min):
        """
        Sets the value_min of this DataSourceKey.


        :param value_min: The value_min of this DataSourceKey.
        :type: float
        """

        self._value_min = value_min

    @property
    def value_max(self):
        """
        Gets the value_max of this DataSourceKey.


        :return: The value_max of this DataSourceKey.
        :rtype: float
        """
        return self._value_max

    @value_max.setter
    def value_max(self, value_max):
        """
        Sets the value_max of this DataSourceKey.


        :param value_max: The value_max of this DataSourceKey.
        :type: float
        """

        self._value_max = value_max

    @property
    def value_type(self):
        """
        Gets the value_type of this DataSourceKey.


        :return: The value_type of this DataSourceKey.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this DataSourceKey.


        :param value_type: The value_type of this DataSourceKey.
        :type: str
        """
        allowed_values = ["string", "boolean", "number", "date"]
        if value_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def id(self):
        """
        Gets the id of this DataSourceKey.


        :return: The id of this DataSourceKey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataSourceKey.


        :param id: The id of this DataSourceKey.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this DataSourceKey.


        :return: The team_id of this DataSourceKey.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this DataSourceKey.


        :param team_id: The team_id of this DataSourceKey.
        :type: str
        """

        self._team_id = team_id

    @property
    def data_source_id(self):
        """
        Gets the data_source_id of this DataSourceKey.


        :return: The data_source_id of this DataSourceKey.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """
        Sets the data_source_id of this DataSourceKey.


        :param data_source_id: The data_source_id of this DataSourceKey.
        :type: str
        """

        self._data_source_id = data_source_id

    @property
    def team(self):
        """
        Gets the team of this DataSourceKey.


        :return: The team of this DataSourceKey.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this DataSourceKey.


        :param team: The team of this DataSourceKey.
        :type: Team
        """

        self._team = team

    @property
    def data_source(self):
        """
        Gets the data_source of this DataSourceKey.


        :return: The data_source of this DataSourceKey.
        :rtype: DataSource
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """
        Sets the data_source of this DataSourceKey.


        :param data_source: The data_source of this DataSourceKey.
        :type: DataSource
        """

        self._data_source = data_source

    @property
    def record_values(self):
        """
        Gets the record_values of this DataSourceKey.


        :return: The record_values of this DataSourceKey.
        :rtype: list[DataSourceRecordValue]
        """
        return self._record_values

    @record_values.setter
    def record_values(self, record_values):
        """
        Sets the record_values of this DataSourceKey.


        :param record_values: The record_values of this DataSourceKey.
        :type: list[DataSourceRecordValue]
        """

        self._record_values = record_values

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
