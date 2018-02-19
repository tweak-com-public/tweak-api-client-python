# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.13
    
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


class TeamTemplateFolder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, path='/', created=None, modified=None, id=None, team_id=None, parent_id=None, team=None, children=None, parent=None, templates=None):
        """
        TeamTemplateFolder - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'path': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'parent_id': 'str',
            'team': 'Team',
            'children': 'list[TeamTemplateFolder]',
            'parent': 'TeamTemplateFolder',
            'templates': 'list[Template]'
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'parent_id': 'parentId',
            'team': 'team',
            'children': 'children',
            'parent': 'parent',
            'templates': 'templates'
        }

        self._name = name
        self._path = path
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._parent_id = parent_id
        self._team = team
        self._children = children
        self._parent = parent
        self._templates = templates


    @property
    def name(self):
        """
        Gets the name of this TeamTemplateFolder.


        :return: The name of this TeamTemplateFolder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TeamTemplateFolder.


        :param name: The name of this TeamTemplateFolder.
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """
        Gets the path of this TeamTemplateFolder.


        :return: The path of this TeamTemplateFolder.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this TeamTemplateFolder.


        :param path: The path of this TeamTemplateFolder.
        :type: str
        """

        self._path = path

    @property
    def created(self):
        """
        Gets the created of this TeamTemplateFolder.


        :return: The created of this TeamTemplateFolder.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this TeamTemplateFolder.


        :param created: The created of this TeamTemplateFolder.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this TeamTemplateFolder.


        :return: The modified of this TeamTemplateFolder.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this TeamTemplateFolder.


        :param modified: The modified of this TeamTemplateFolder.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this TeamTemplateFolder.


        :return: The id of this TeamTemplateFolder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamTemplateFolder.


        :param id: The id of this TeamTemplateFolder.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this TeamTemplateFolder.


        :return: The team_id of this TeamTemplateFolder.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this TeamTemplateFolder.


        :param team_id: The team_id of this TeamTemplateFolder.
        :type: str
        """

        self._team_id = team_id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this TeamTemplateFolder.


        :return: The parent_id of this TeamTemplateFolder.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this TeamTemplateFolder.


        :param parent_id: The parent_id of this TeamTemplateFolder.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def team(self):
        """
        Gets the team of this TeamTemplateFolder.


        :return: The team of this TeamTemplateFolder.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this TeamTemplateFolder.


        :param team: The team of this TeamTemplateFolder.
        :type: Team
        """

        self._team = team

    @property
    def children(self):
        """
        Gets the children of this TeamTemplateFolder.


        :return: The children of this TeamTemplateFolder.
        :rtype: list[TeamTemplateFolder]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this TeamTemplateFolder.


        :param children: The children of this TeamTemplateFolder.
        :type: list[TeamTemplateFolder]
        """

        self._children = children

    @property
    def parent(self):
        """
        Gets the parent of this TeamTemplateFolder.


        :return: The parent of this TeamTemplateFolder.
        :rtype: TeamTemplateFolder
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this TeamTemplateFolder.


        :param parent: The parent of this TeamTemplateFolder.
        :type: TeamTemplateFolder
        """

        self._parent = parent

    @property
    def templates(self):
        """
        Gets the templates of this TeamTemplateFolder.


        :return: The templates of this TeamTemplateFolder.
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this TeamTemplateFolder.


        :param templates: The templates of this TeamTemplateFolder.
        :type: list[Template]
        """

        self._templates = templates

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
