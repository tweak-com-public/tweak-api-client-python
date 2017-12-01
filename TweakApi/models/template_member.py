# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.1
    
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


class TemplateMember(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, template_id=None, member_id=None, portal_id=None, template=None, member=None, portal=None):
        """
        TemplateMember - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'template_id': 'str',
            'member_id': 'str',
            'portal_id': 'str',
            'template': 'Template',
            'member': 'TeamMember',
            'portal': 'Portal'
        }

        self.attribute_map = {
            'id': 'id',
            'template_id': 'templateId',
            'member_id': 'memberId',
            'portal_id': 'portalId',
            'template': 'template',
            'member': 'member',
            'portal': 'portal'
        }

        self._id = id
        self._template_id = template_id
        self._member_id = member_id
        self._portal_id = portal_id
        self._template = template
        self._member = member
        self._portal = portal


    @property
    def id(self):
        """
        Gets the id of this TemplateMember.


        :return: The id of this TemplateMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TemplateMember.


        :param id: The id of this TemplateMember.
        :type: str
        """

        self._id = id

    @property
    def template_id(self):
        """
        Gets the template_id of this TemplateMember.


        :return: The template_id of this TemplateMember.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this TemplateMember.


        :param template_id: The template_id of this TemplateMember.
        :type: str
        """

        self._template_id = template_id

    @property
    def member_id(self):
        """
        Gets the member_id of this TemplateMember.


        :return: The member_id of this TemplateMember.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this TemplateMember.


        :param member_id: The member_id of this TemplateMember.
        :type: str
        """

        self._member_id = member_id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this TemplateMember.


        :return: The portal_id of this TemplateMember.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this TemplateMember.


        :param portal_id: The portal_id of this TemplateMember.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def template(self):
        """
        Gets the template of this TemplateMember.


        :return: The template of this TemplateMember.
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this TemplateMember.


        :param template: The template of this TemplateMember.
        :type: Template
        """

        self._template = template

    @property
    def member(self):
        """
        Gets the member of this TemplateMember.


        :return: The member of this TemplateMember.
        :rtype: TeamMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this TemplateMember.


        :param member: The member of this TemplateMember.
        :type: TeamMember
        """

        self._member = member

    @property
    def portal(self):
        """
        Gets the portal of this TemplateMember.


        :return: The portal of this TemplateMember.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this TemplateMember.


        :param portal: The portal of this TemplateMember.
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
