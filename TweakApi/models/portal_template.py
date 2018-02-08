# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.1
    
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


class PortalTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, path='/', created=None, modified=None, id=None, portal_id=None, template_id=None, folder_id=None, portal=None, template=None, folder=None):
        """
        PortalTemplate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'path': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'portal_id': 'str',
            'template_id': 'str',
            'folder_id': 'str',
            'portal': 'Portal',
            'template': 'Template',
            'folder': 'PortalTemplateFolder'
        }

        self.attribute_map = {
            'path': 'path',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'portal_id': 'portalId',
            'template_id': 'templateId',
            'folder_id': 'folderId',
            'portal': 'portal',
            'template': 'template',
            'folder': 'folder'
        }

        self._path = path
        self._created = created
        self._modified = modified
        self._id = id
        self._portal_id = portal_id
        self._template_id = template_id
        self._folder_id = folder_id
        self._portal = portal
        self._template = template
        self._folder = folder


    @property
    def path(self):
        """
        Gets the path of this PortalTemplate.


        :return: The path of this PortalTemplate.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this PortalTemplate.


        :param path: The path of this PortalTemplate.
        :type: str
        """

        self._path = path

    @property
    def created(self):
        """
        Gets the created of this PortalTemplate.


        :return: The created of this PortalTemplate.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this PortalTemplate.


        :param created: The created of this PortalTemplate.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this PortalTemplate.


        :return: The modified of this PortalTemplate.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this PortalTemplate.


        :param modified: The modified of this PortalTemplate.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this PortalTemplate.


        :return: The id of this PortalTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PortalTemplate.


        :param id: The id of this PortalTemplate.
        :type: str
        """

        self._id = id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this PortalTemplate.


        :return: The portal_id of this PortalTemplate.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this PortalTemplate.


        :param portal_id: The portal_id of this PortalTemplate.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def template_id(self):
        """
        Gets the template_id of this PortalTemplate.


        :return: The template_id of this PortalTemplate.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this PortalTemplate.


        :param template_id: The template_id of this PortalTemplate.
        :type: str
        """

        self._template_id = template_id

    @property
    def folder_id(self):
        """
        Gets the folder_id of this PortalTemplate.


        :return: The folder_id of this PortalTemplate.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this PortalTemplate.


        :param folder_id: The folder_id of this PortalTemplate.
        :type: str
        """

        self._folder_id = folder_id

    @property
    def portal(self):
        """
        Gets the portal of this PortalTemplate.


        :return: The portal of this PortalTemplate.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this PortalTemplate.


        :param portal: The portal of this PortalTemplate.
        :type: Portal
        """

        self._portal = portal

    @property
    def template(self):
        """
        Gets the template of this PortalTemplate.


        :return: The template of this PortalTemplate.
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this PortalTemplate.


        :param template: The template of this PortalTemplate.
        :type: Template
        """

        self._template = template

    @property
    def folder(self):
        """
        Gets the folder of this PortalTemplate.


        :return: The folder of this PortalTemplate.
        :rtype: PortalTemplateFolder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder of this PortalTemplate.


        :param folder: The folder of this PortalTemplate.
        :type: PortalTemplateFolder
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
