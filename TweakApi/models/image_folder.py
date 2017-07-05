# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 0.0.3
    
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


class ImageFolder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, path='/', created=None, modified=None, id=None, team_id=None, parent_id=None, images=None, team=None, portals=None, members=None, folder_members=None, parent=None, children=None):
        """
        ImageFolder - a model defined in Swagger

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
            'images': 'list[Image]',
            'team': 'Team',
            'portals': 'list[Portal]',
            'members': 'list[TeamMember]',
            'folder_members': 'list[ImageFolderMember]',
            'parent': 'ImageFolder',
            'children': 'list[ImageFolder]'
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'parent_id': 'parentId',
            'images': 'images',
            'team': 'team',
            'portals': 'portals',
            'members': 'members',
            'folder_members': 'folderMembers',
            'parent': 'parent',
            'children': 'children'
        }

        self._name = name
        self._path = path
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._parent_id = parent_id
        self._images = images
        self._team = team
        self._portals = portals
        self._members = members
        self._folder_members = folder_members
        self._parent = parent
        self._children = children


    @property
    def name(self):
        """
        Gets the name of this ImageFolder.


        :return: The name of this ImageFolder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ImageFolder.


        :param name: The name of this ImageFolder.
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """
        Gets the path of this ImageFolder.


        :return: The path of this ImageFolder.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ImageFolder.


        :param path: The path of this ImageFolder.
        :type: str
        """

        self._path = path

    @property
    def created(self):
        """
        Gets the created of this ImageFolder.


        :return: The created of this ImageFolder.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ImageFolder.


        :param created: The created of this ImageFolder.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this ImageFolder.


        :return: The modified of this ImageFolder.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this ImageFolder.


        :param modified: The modified of this ImageFolder.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this ImageFolder.


        :return: The id of this ImageFolder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ImageFolder.


        :param id: The id of this ImageFolder.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this ImageFolder.


        :return: The team_id of this ImageFolder.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this ImageFolder.


        :param team_id: The team_id of this ImageFolder.
        :type: str
        """

        self._team_id = team_id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this ImageFolder.


        :return: The parent_id of this ImageFolder.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this ImageFolder.


        :param parent_id: The parent_id of this ImageFolder.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def images(self):
        """
        Gets the images of this ImageFolder.


        :return: The images of this ImageFolder.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this ImageFolder.


        :param images: The images of this ImageFolder.
        :type: list[Image]
        """

        self._images = images

    @property
    def team(self):
        """
        Gets the team of this ImageFolder.


        :return: The team of this ImageFolder.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this ImageFolder.


        :param team: The team of this ImageFolder.
        :type: Team
        """

        self._team = team

    @property
    def portals(self):
        """
        Gets the portals of this ImageFolder.


        :return: The portals of this ImageFolder.
        :rtype: list[Portal]
        """
        return self._portals

    @portals.setter
    def portals(self, portals):
        """
        Sets the portals of this ImageFolder.


        :param portals: The portals of this ImageFolder.
        :type: list[Portal]
        """

        self._portals = portals

    @property
    def members(self):
        """
        Gets the members of this ImageFolder.


        :return: The members of this ImageFolder.
        :rtype: list[TeamMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this ImageFolder.


        :param members: The members of this ImageFolder.
        :type: list[TeamMember]
        """

        self._members = members

    @property
    def folder_members(self):
        """
        Gets the folder_members of this ImageFolder.


        :return: The folder_members of this ImageFolder.
        :rtype: list[ImageFolderMember]
        """
        return self._folder_members

    @folder_members.setter
    def folder_members(self, folder_members):
        """
        Sets the folder_members of this ImageFolder.


        :param folder_members: The folder_members of this ImageFolder.
        :type: list[ImageFolderMember]
        """

        self._folder_members = folder_members

    @property
    def parent(self):
        """
        Gets the parent of this ImageFolder.


        :return: The parent of this ImageFolder.
        :rtype: ImageFolder
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ImageFolder.


        :param parent: The parent of this ImageFolder.
        :type: ImageFolder
        """

        self._parent = parent

    @property
    def children(self):
        """
        Gets the children of this ImageFolder.


        :return: The children of this ImageFolder.
        :rtype: list[ImageFolder]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this ImageFolder.


        :param children: The children of this ImageFolder.
        :type: list[ImageFolder]
        """

        self._children = children

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
