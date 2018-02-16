# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.10
    
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


class ImageFolderMember(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, modified=None, id=None, member_id=None, folder_id=None, member=None, folder=None):
        """
        ImageFolderMember - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'member_id': 'str',
            'folder_id': 'str',
            'member': 'TeamMember',
            'folder': 'ImageFolder'
        }

        self.attribute_map = {
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'member_id': 'memberId',
            'folder_id': 'folderId',
            'member': 'member',
            'folder': 'folder'
        }

        self._created = created
        self._modified = modified
        self._id = id
        self._member_id = member_id
        self._folder_id = folder_id
        self._member = member
        self._folder = folder


    @property
    def created(self):
        """
        Gets the created of this ImageFolderMember.


        :return: The created of this ImageFolderMember.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this ImageFolderMember.


        :param created: The created of this ImageFolderMember.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this ImageFolderMember.


        :return: The modified of this ImageFolderMember.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this ImageFolderMember.


        :param modified: The modified of this ImageFolderMember.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this ImageFolderMember.


        :return: The id of this ImageFolderMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ImageFolderMember.


        :param id: The id of this ImageFolderMember.
        :type: str
        """

        self._id = id

    @property
    def member_id(self):
        """
        Gets the member_id of this ImageFolderMember.


        :return: The member_id of this ImageFolderMember.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this ImageFolderMember.


        :param member_id: The member_id of this ImageFolderMember.
        :type: str
        """

        self._member_id = member_id

    @property
    def folder_id(self):
        """
        Gets the folder_id of this ImageFolderMember.


        :return: The folder_id of this ImageFolderMember.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this ImageFolderMember.


        :param folder_id: The folder_id of this ImageFolderMember.
        :type: str
        """

        self._folder_id = folder_id

    @property
    def member(self):
        """
        Gets the member of this ImageFolderMember.


        :return: The member of this ImageFolderMember.
        :rtype: TeamMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this ImageFolderMember.


        :param member: The member of this ImageFolderMember.
        :type: TeamMember
        """

        self._member = member

    @property
    def folder(self):
        """
        Gets the folder of this ImageFolderMember.


        :return: The folder of this ImageFolderMember.
        :rtype: ImageFolder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder of this ImageFolderMember.


        :param folder: The folder of this ImageFolderMember.
        :type: ImageFolder
        """

        self._folder = folder

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
