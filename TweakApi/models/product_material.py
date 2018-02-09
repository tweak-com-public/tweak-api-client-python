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


class ProductMaterial(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, code=None, description=None, thumbnail=None, status=None, created=None, modified=None, id=None, team_id=None, team=None):
        """
        ProductMaterial - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'code': 'str',
            'description': 'str',
            'thumbnail': 'CloudinaryImage',
            'status': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'team': 'Team'
        }

        self.attribute_map = {
            'name': 'name',
            'code': 'code',
            'description': 'description',
            'thumbnail': 'thumbnail',
            'status': 'status',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team'
        }

        self._name = name
        self._code = code
        self._description = description
        self._thumbnail = thumbnail
        self._status = status
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._team = team


    @property
    def name(self):
        """
        Gets the name of this ProductMaterial.


        :return: The name of this ProductMaterial.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductMaterial.


        :param name: The name of this ProductMaterial.
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """
        Gets the code of this ProductMaterial.


        :return: The code of this ProductMaterial.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ProductMaterial.


        :param code: The code of this ProductMaterial.
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """
        Gets the description of this ProductMaterial.


        :return: The description of this ProductMaterial.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProductMaterial.


        :param description: The description of this ProductMaterial.
        :type: str
        """

        self._description = description

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this ProductMaterial.


        :return: The thumbnail of this ProductMaterial.
        :rtype: CloudinaryImage
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this ProductMaterial.


        :param thumbnail: The thumbnail of this ProductMaterial.
        :type: CloudinaryImage
        """

        self._thumbnail = thumbnail

    @property
    def status(self):
        """
        Gets the status of this ProductMaterial.


        :return: The status of this ProductMaterial.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProductMaterial.


        :param status: The status of this ProductMaterial.
        :type: str
        """
        allowed_values = ["public", "private"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created(self):
        """
        Gets the created of this ProductMaterial.


        :return: The created of this ProductMaterial.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ProductMaterial.


        :param created: The created of this ProductMaterial.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this ProductMaterial.


        :return: The modified of this ProductMaterial.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this ProductMaterial.


        :param modified: The modified of this ProductMaterial.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this ProductMaterial.


        :return: The id of this ProductMaterial.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductMaterial.


        :param id: The id of this ProductMaterial.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this ProductMaterial.


        :return: The team_id of this ProductMaterial.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this ProductMaterial.


        :param team_id: The team_id of this ProductMaterial.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this ProductMaterial.


        :return: The team of this ProductMaterial.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this ProductMaterial.


        :param team: The team of this ProductMaterial.
        :type: Team
        """

        self._team = team

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
