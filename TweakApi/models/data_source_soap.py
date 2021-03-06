# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-beta.0
    
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


class DataSourceSoap(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, url=None, wsdl=None, wsdl_options=None, security=None, soap_headers=None, created=None, modified=None, id=None, team_id=None, team=None, dynamic_datas=None):
        """
        DataSourceSoap - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'url': 'str',
            'wsdl': 'str',
            'wsdl_options': 'object',
            'security': 'object',
            'soap_headers': 'list[object]',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'team': 'Team',
            'dynamic_datas': 'list[DynamicData]'
        }

        self.attribute_map = {
            'name': 'name',
            'url': 'url',
            'wsdl': 'wsdl',
            'wsdl_options': 'wsdl_options',
            'security': 'security',
            'soap_headers': 'soapHeaders',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team',
            'dynamic_datas': 'dynamicDatas'
        }

        self._name = name
        self._url = url
        self._wsdl = wsdl
        self._wsdl_options = wsdl_options
        self._security = security
        self._soap_headers = soap_headers
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._team = team
        self._dynamic_datas = dynamic_datas


    @property
    def name(self):
        """
        Gets the name of this DataSourceSoap.


        :return: The name of this DataSourceSoap.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataSourceSoap.


        :param name: The name of this DataSourceSoap.
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """
        Gets the url of this DataSourceSoap.


        :return: The url of this DataSourceSoap.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DataSourceSoap.


        :param url: The url of this DataSourceSoap.
        :type: str
        """

        self._url = url

    @property
    def wsdl(self):
        """
        Gets the wsdl of this DataSourceSoap.


        :return: The wsdl of this DataSourceSoap.
        :rtype: str
        """
        return self._wsdl

    @wsdl.setter
    def wsdl(self, wsdl):
        """
        Sets the wsdl of this DataSourceSoap.


        :param wsdl: The wsdl of this DataSourceSoap.
        :type: str
        """

        self._wsdl = wsdl

    @property
    def wsdl_options(self):
        """
        Gets the wsdl_options of this DataSourceSoap.


        :return: The wsdl_options of this DataSourceSoap.
        :rtype: object
        """
        return self._wsdl_options

    @wsdl_options.setter
    def wsdl_options(self, wsdl_options):
        """
        Sets the wsdl_options of this DataSourceSoap.


        :param wsdl_options: The wsdl_options of this DataSourceSoap.
        :type: object
        """

        self._wsdl_options = wsdl_options

    @property
    def security(self):
        """
        Gets the security of this DataSourceSoap.


        :return: The security of this DataSourceSoap.
        :rtype: object
        """
        return self._security

    @security.setter
    def security(self, security):
        """
        Sets the security of this DataSourceSoap.


        :param security: The security of this DataSourceSoap.
        :type: object
        """

        self._security = security

    @property
    def soap_headers(self):
        """
        Gets the soap_headers of this DataSourceSoap.


        :return: The soap_headers of this DataSourceSoap.
        :rtype: list[object]
        """
        return self._soap_headers

    @soap_headers.setter
    def soap_headers(self, soap_headers):
        """
        Sets the soap_headers of this DataSourceSoap.


        :param soap_headers: The soap_headers of this DataSourceSoap.
        :type: list[object]
        """

        self._soap_headers = soap_headers

    @property
    def created(self):
        """
        Gets the created of this DataSourceSoap.


        :return: The created of this DataSourceSoap.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DataSourceSoap.


        :param created: The created of this DataSourceSoap.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this DataSourceSoap.


        :return: The modified of this DataSourceSoap.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this DataSourceSoap.


        :param modified: The modified of this DataSourceSoap.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this DataSourceSoap.


        :return: The id of this DataSourceSoap.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataSourceSoap.


        :param id: The id of this DataSourceSoap.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this DataSourceSoap.


        :return: The team_id of this DataSourceSoap.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this DataSourceSoap.


        :param team_id: The team_id of this DataSourceSoap.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this DataSourceSoap.


        :return: The team of this DataSourceSoap.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this DataSourceSoap.


        :param team: The team of this DataSourceSoap.
        :type: Team
        """

        self._team = team

    @property
    def dynamic_datas(self):
        """
        Gets the dynamic_datas of this DataSourceSoap.


        :return: The dynamic_datas of this DataSourceSoap.
        :rtype: list[DynamicData]
        """
        return self._dynamic_datas

    @dynamic_datas.setter
    def dynamic_datas(self, dynamic_datas):
        """
        Sets the dynamic_datas of this DataSourceSoap.


        :param dynamic_datas: The dynamic_datas of this DataSourceSoap.
        :type: list[DynamicData]
        """

        self._dynamic_datas = dynamic_datas

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
