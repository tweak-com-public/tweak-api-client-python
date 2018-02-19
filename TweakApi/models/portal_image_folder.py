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


class PortalImageFolder(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, portal_id=None, folder_id=None, portal=None, folder=None):
        """
        PortalImageFolder - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'portal_id': 'str',
            'folder_id': 'str',
            'portal': 'Portal',
            'folder': 'ImageFolder'
        }

        self.attribute_map = {
            'id': 'id',
            'portal_id': 'portalId',
            'folder_id': 'folderId',
            'portal': 'portal',
            'folder': 'folder'
        }

        self._id = id
        self._portal_id = portal_id
        self._folder_id = folder_id
        self._portal = portal
        self._folder = folder


    @property
    def id(self):
        """
        Gets the id of this PortalImageFolder.


        :return: The id of this PortalImageFolder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PortalImageFolder.


        :param id: The id of this PortalImageFolder.
        :type: str
        """

        self._id = id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this PortalImageFolder.


        :return: The portal_id of this PortalImageFolder.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this PortalImageFolder.


        :param portal_id: The portal_id of this PortalImageFolder.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def folder_id(self):
        """
        Gets the folder_id of this PortalImageFolder.


        :return: The folder_id of this PortalImageFolder.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this PortalImageFolder.


        :param folder_id: The folder_id of this PortalImageFolder.
        :type: str
        """

        self._folder_id = folder_id

    @property
    def portal(self):
        """
        Gets the portal of this PortalImageFolder.


        :return: The portal of this PortalImageFolder.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this PortalImageFolder.


        :param portal: The portal of this PortalImageFolder.
        :type: Portal
        """

        self._portal = portal

    @property
    def folder(self):
        """
        Gets the folder of this PortalImageFolder.


        :return: The folder of this PortalImageFolder.
        :rtype: ImageFolder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder of this PortalImageFolder.


        :param folder: The folder of this PortalImageFolder.
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
