# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.4-alpha.4
    
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


class PortalPermissionSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, template_permission=None, tweak_template_permission=None, id=None, portal_id=None, portal=None):
        """
        PortalPermissionSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'template_permission': 'TemplatePermissionSet',
            'tweak_template_permission': 'TemplatePermissionSet',
            'id': 'str',
            'portal_id': 'str',
            'portal': 'Portal'
        }

        self.attribute_map = {
            'template_permission': 'templatePermission',
            'tweak_template_permission': 'tweakTemplatePermission',
            'id': 'id',
            'portal_id': 'portalId',
            'portal': 'portal'
        }

        self._template_permission = template_permission
        self._tweak_template_permission = tweak_template_permission
        self._id = id
        self._portal_id = portal_id
        self._portal = portal


    @property
    def template_permission(self):
        """
        Gets the template_permission of this PortalPermissionSet.


        :return: The template_permission of this PortalPermissionSet.
        :rtype: TemplatePermissionSet
        """
        return self._template_permission

    @template_permission.setter
    def template_permission(self, template_permission):
        """
        Sets the template_permission of this PortalPermissionSet.


        :param template_permission: The template_permission of this PortalPermissionSet.
        :type: TemplatePermissionSet
        """

        self._template_permission = template_permission

    @property
    def tweak_template_permission(self):
        """
        Gets the tweak_template_permission of this PortalPermissionSet.


        :return: The tweak_template_permission of this PortalPermissionSet.
        :rtype: TemplatePermissionSet
        """
        return self._tweak_template_permission

    @tweak_template_permission.setter
    def tweak_template_permission(self, tweak_template_permission):
        """
        Sets the tweak_template_permission of this PortalPermissionSet.


        :param tweak_template_permission: The tweak_template_permission of this PortalPermissionSet.
        :type: TemplatePermissionSet
        """

        self._tweak_template_permission = tweak_template_permission

    @property
    def id(self):
        """
        Gets the id of this PortalPermissionSet.


        :return: The id of this PortalPermissionSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PortalPermissionSet.


        :param id: The id of this PortalPermissionSet.
        :type: str
        """

        self._id = id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this PortalPermissionSet.


        :return: The portal_id of this PortalPermissionSet.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this PortalPermissionSet.


        :param portal_id: The portal_id of this PortalPermissionSet.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def portal(self):
        """
        Gets the portal of this PortalPermissionSet.


        :return: The portal of this PortalPermissionSet.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this PortalPermissionSet.


        :param portal: The portal of this PortalPermissionSet.
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
