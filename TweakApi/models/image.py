# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-beta.3
    
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


class Image(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, file_name=None, link=None, path='/', created=None, modified=None, id=None, team_id=None, folder_id=None, folder=None, team=None):
        """
        Image - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'file_name': 'str',
            'link': 'str',
            'path': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'folder_id': 'str',
            'folder': 'ImageFolder',
            'team': 'Team'
        }

        self.attribute_map = {
            'name': 'name',
            'file_name': 'fileName',
            'link': 'link',
            'path': 'path',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'folder_id': 'folderId',
            'folder': 'folder',
            'team': 'team'
        }

        self._name = name
        self._file_name = file_name
        self._link = link
        self._path = path
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._folder_id = folder_id
        self._folder = folder
        self._team = team


    @property
    def name(self):
        """
        Gets the name of this Image.


        :return: The name of this Image.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Image.


        :param name: The name of this Image.
        :type: str
        """

        self._name = name

    @property
    def file_name(self):
        """
        Gets the file_name of this Image.


        :return: The file_name of this Image.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this Image.


        :param file_name: The file_name of this Image.
        :type: str
        """

        self._file_name = file_name

    @property
    def link(self):
        """
        Gets the link of this Image.


        :return: The link of this Image.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this Image.


        :param link: The link of this Image.
        :type: str
        """

        self._link = link

    @property
    def path(self):
        """
        Gets the path of this Image.


        :return: The path of this Image.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Image.


        :param path: The path of this Image.
        :type: str
        """

        self._path = path

    @property
    def created(self):
        """
        Gets the created of this Image.


        :return: The created of this Image.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Image.


        :param created: The created of this Image.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Image.


        :return: The modified of this Image.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Image.


        :param modified: The modified of this Image.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Image.


        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.


        :param id: The id of this Image.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this Image.


        :return: The team_id of this Image.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this Image.


        :param team_id: The team_id of this Image.
        :type: str
        """

        self._team_id = team_id

    @property
    def folder_id(self):
        """
        Gets the folder_id of this Image.


        :return: The folder_id of this Image.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this Image.


        :param folder_id: The folder_id of this Image.
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder(self):
        """
        Gets the folder of this Image.


        :return: The folder of this Image.
        :rtype: ImageFolder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder of this Image.


        :param folder: The folder of this Image.
        :type: ImageFolder
        """

        self._folder = folder

    @property
    def team(self):
        """
        Gets the team of this Image.


        :return: The team of this Image.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Image.


        :param team: The team of this Image.
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
