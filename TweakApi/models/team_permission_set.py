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


class TeamPermissionSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email_notification=True, template_permission=None, tweak_template_permission=None, team_customer_permission=None, id=None, team_id=None, team=None):
        """
        TeamPermissionSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email_notification': 'bool',
            'template_permission': 'TemplatePermissionSet',
            'tweak_template_permission': 'TemplatePermissionSet',
            'team_customer_permission': 'TeamCustomerPermissionSet',
            'id': 'str',
            'team_id': 'str',
            'team': 'Team'
        }

        self.attribute_map = {
            'email_notification': 'emailNotification',
            'template_permission': 'templatePermission',
            'tweak_template_permission': 'tweakTemplatePermission',
            'team_customer_permission': 'teamCustomerPermission',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team'
        }

        self._email_notification = email_notification
        self._template_permission = template_permission
        self._tweak_template_permission = tweak_template_permission
        self._team_customer_permission = team_customer_permission
        self._id = id
        self._team_id = team_id
        self._team = team


    @property
    def email_notification(self):
        """
        Gets the email_notification of this TeamPermissionSet.


        :return: The email_notification of this TeamPermissionSet.
        :rtype: bool
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """
        Sets the email_notification of this TeamPermissionSet.


        :param email_notification: The email_notification of this TeamPermissionSet.
        :type: bool
        """

        self._email_notification = email_notification

    @property
    def template_permission(self):
        """
        Gets the template_permission of this TeamPermissionSet.


        :return: The template_permission of this TeamPermissionSet.
        :rtype: TemplatePermissionSet
        """
        return self._template_permission

    @template_permission.setter
    def template_permission(self, template_permission):
        """
        Sets the template_permission of this TeamPermissionSet.


        :param template_permission: The template_permission of this TeamPermissionSet.
        :type: TemplatePermissionSet
        """

        self._template_permission = template_permission

    @property
    def tweak_template_permission(self):
        """
        Gets the tweak_template_permission of this TeamPermissionSet.


        :return: The tweak_template_permission of this TeamPermissionSet.
        :rtype: TemplatePermissionSet
        """
        return self._tweak_template_permission

    @tweak_template_permission.setter
    def tweak_template_permission(self, tweak_template_permission):
        """
        Sets the tweak_template_permission of this TeamPermissionSet.


        :param tweak_template_permission: The tweak_template_permission of this TeamPermissionSet.
        :type: TemplatePermissionSet
        """

        self._tweak_template_permission = tweak_template_permission

    @property
    def team_customer_permission(self):
        """
        Gets the team_customer_permission of this TeamPermissionSet.


        :return: The team_customer_permission of this TeamPermissionSet.
        :rtype: TeamCustomerPermissionSet
        """
        return self._team_customer_permission

    @team_customer_permission.setter
    def team_customer_permission(self, team_customer_permission):
        """
        Sets the team_customer_permission of this TeamPermissionSet.


        :param team_customer_permission: The team_customer_permission of this TeamPermissionSet.
        :type: TeamCustomerPermissionSet
        """

        self._team_customer_permission = team_customer_permission

    @property
    def id(self):
        """
        Gets the id of this TeamPermissionSet.


        :return: The id of this TeamPermissionSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamPermissionSet.


        :param id: The id of this TeamPermissionSet.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this TeamPermissionSet.


        :return: The team_id of this TeamPermissionSet.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this TeamPermissionSet.


        :param team_id: The team_id of this TeamPermissionSet.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this TeamPermissionSet.


        :return: The team of this TeamPermissionSet.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this TeamPermissionSet.


        :param team: The team of this TeamPermissionSet.
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
