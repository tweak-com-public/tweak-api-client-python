# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.6
    
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


class PortalTemplateFolder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, path='/', created=None, modified=None, id=None, portal_id=None, parent_id=None, portal=None, children=None, parent=None, templates=None):
        """
        PortalTemplateFolder - a model defined in Swagger

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
            'portal_id': 'str',
            'parent_id': 'str',
            'portal': 'Portal',
            'children': 'list[PortalTemplateFolder]',
            'parent': 'PortalTemplateFolder',
            'templates': 'list[Template]'
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'portal_id': 'portalId',
            'parent_id': 'parentId',
            'portal': 'portal',
            'children': 'children',
            'parent': 'parent',
            'templates': 'templates'
        }

        self._name = name
        self._path = path
        self._created = created
        self._modified = modified
        self._id = id
        self._portal_id = portal_id
        self._parent_id = parent_id
        self._portal = portal
        self._children = children
        self._parent = parent
        self._templates = templates


    @property
    def name(self):
        """
        Gets the name of this PortalTemplateFolder.


        :return: The name of this PortalTemplateFolder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PortalTemplateFolder.


        :param name: The name of this PortalTemplateFolder.
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """
        Gets the path of this PortalTemplateFolder.


        :return: The path of this PortalTemplateFolder.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this PortalTemplateFolder.


        :param path: The path of this PortalTemplateFolder.
        :type: str
        """

        self._path = path

    @property
    def created(self):
        """
        Gets the created of this PortalTemplateFolder.


        :return: The created of this PortalTemplateFolder.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this PortalTemplateFolder.


        :param created: The created of this PortalTemplateFolder.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this PortalTemplateFolder.


        :return: The modified of this PortalTemplateFolder.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this PortalTemplateFolder.


        :param modified: The modified of this PortalTemplateFolder.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this PortalTemplateFolder.


        :return: The id of this PortalTemplateFolder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PortalTemplateFolder.


        :param id: The id of this PortalTemplateFolder.
        :type: str
        """

        self._id = id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this PortalTemplateFolder.


        :return: The portal_id of this PortalTemplateFolder.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this PortalTemplateFolder.


        :param portal_id: The portal_id of this PortalTemplateFolder.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this PortalTemplateFolder.


        :return: The parent_id of this PortalTemplateFolder.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this PortalTemplateFolder.


        :param parent_id: The parent_id of this PortalTemplateFolder.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def portal(self):
        """
        Gets the portal of this PortalTemplateFolder.


        :return: The portal of this PortalTemplateFolder.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this PortalTemplateFolder.


        :param portal: The portal of this PortalTemplateFolder.
        :type: Portal
        """

        self._portal = portal

    @property
    def children(self):
        """
        Gets the children of this PortalTemplateFolder.


        :return: The children of this PortalTemplateFolder.
        :rtype: list[PortalTemplateFolder]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this PortalTemplateFolder.


        :param children: The children of this PortalTemplateFolder.
        :type: list[PortalTemplateFolder]
        """

        self._children = children

    @property
    def parent(self):
        """
        Gets the parent of this PortalTemplateFolder.


        :return: The parent of this PortalTemplateFolder.
        :rtype: PortalTemplateFolder
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this PortalTemplateFolder.


        :param parent: The parent of this PortalTemplateFolder.
        :type: PortalTemplateFolder
        """

        self._parent = parent

    @property
    def templates(self):
        """
        Gets the templates of this PortalTemplateFolder.


        :return: The templates of this PortalTemplateFolder.
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this PortalTemplateFolder.


        :param templates: The templates of this PortalTemplateFolder.
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
