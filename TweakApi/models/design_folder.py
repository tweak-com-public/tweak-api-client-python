# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.2
    
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


class DesignFolder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description='', path='/', created=None, modified=None, id=None, member_id=None, parent_id=None, portal_id=None, member=None, children=None, parent=None, designs=None, portal=None):
        """
        DesignFolder - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'path': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'member_id': 'str',
            'parent_id': 'str',
            'portal_id': 'str',
            'member': 'TeamMember',
            'children': 'list[DesignFolder]',
            'parent': 'DesignFolder',
            'designs': 'list[Design]',
            'portal': 'Portal'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'path': 'path',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'member_id': 'memberId',
            'parent_id': 'parentId',
            'portal_id': 'portalId',
            'member': 'member',
            'children': 'children',
            'parent': 'parent',
            'designs': 'designs',
            'portal': 'portal'
        }

        self._name = name
        self._description = description
        self._path = path
        self._created = created
        self._modified = modified
        self._id = id
        self._member_id = member_id
        self._parent_id = parent_id
        self._portal_id = portal_id
        self._member = member
        self._children = children
        self._parent = parent
        self._designs = designs
        self._portal = portal


    @property
    def name(self):
        """
        Gets the name of this DesignFolder.


        :return: The name of this DesignFolder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DesignFolder.


        :param name: The name of this DesignFolder.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DesignFolder.


        :return: The description of this DesignFolder.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DesignFolder.


        :param description: The description of this DesignFolder.
        :type: str
        """

        self._description = description

    @property
    def path(self):
        """
        Gets the path of this DesignFolder.


        :return: The path of this DesignFolder.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this DesignFolder.


        :param path: The path of this DesignFolder.
        :type: str
        """

        self._path = path

    @property
    def created(self):
        """
        Gets the created of this DesignFolder.


        :return: The created of this DesignFolder.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DesignFolder.


        :param created: The created of this DesignFolder.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this DesignFolder.


        :return: The modified of this DesignFolder.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this DesignFolder.


        :param modified: The modified of this DesignFolder.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this DesignFolder.


        :return: The id of this DesignFolder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DesignFolder.


        :param id: The id of this DesignFolder.
        :type: str
        """

        self._id = id

    @property
    def member_id(self):
        """
        Gets the member_id of this DesignFolder.


        :return: The member_id of this DesignFolder.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this DesignFolder.


        :param member_id: The member_id of this DesignFolder.
        :type: str
        """

        self._member_id = member_id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this DesignFolder.


        :return: The parent_id of this DesignFolder.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this DesignFolder.


        :param parent_id: The parent_id of this DesignFolder.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this DesignFolder.


        :return: The portal_id of this DesignFolder.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this DesignFolder.


        :param portal_id: The portal_id of this DesignFolder.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def member(self):
        """
        Gets the member of this DesignFolder.


        :return: The member of this DesignFolder.
        :rtype: TeamMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this DesignFolder.


        :param member: The member of this DesignFolder.
        :type: TeamMember
        """

        self._member = member

    @property
    def children(self):
        """
        Gets the children of this DesignFolder.


        :return: The children of this DesignFolder.
        :rtype: list[DesignFolder]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this DesignFolder.


        :param children: The children of this DesignFolder.
        :type: list[DesignFolder]
        """

        self._children = children

    @property
    def parent(self):
        """
        Gets the parent of this DesignFolder.


        :return: The parent of this DesignFolder.
        :rtype: DesignFolder
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this DesignFolder.


        :param parent: The parent of this DesignFolder.
        :type: DesignFolder
        """

        self._parent = parent

    @property
    def designs(self):
        """
        Gets the designs of this DesignFolder.


        :return: The designs of this DesignFolder.
        :rtype: list[Design]
        """
        return self._designs

    @designs.setter
    def designs(self, designs):
        """
        Sets the designs of this DesignFolder.


        :param designs: The designs of this DesignFolder.
        :type: list[Design]
        """

        self._designs = designs

    @property
    def portal(self):
        """
        Gets the portal of this DesignFolder.


        :return: The portal of this DesignFolder.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this DesignFolder.


        :param portal: The portal of this DesignFolder.
        :type: Portal
        """

        self._portal = portal

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
