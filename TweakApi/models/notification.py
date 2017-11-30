# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.0
    
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


class Notification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, title=None, body=None, read=False, buttons=None, created=None, modified=None, id=None, team_id=None, portal_id=None, member_id=None, team=None, portal=None, member=None):
        """
        Notification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'title': 'str',
            'body': 'str',
            'read': 'bool',
            'buttons': 'list[NotificationButton]',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'portal_id': 'str',
            'member_id': 'str',
            'team': 'Team',
            'portal': 'Portal',
            'member': 'TeamMember'
        }

        self.attribute_map = {
            'type': 'type',
            'title': 'title',
            'body': 'body',
            'read': 'read',
            'buttons': 'buttons',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'portal_id': 'portalId',
            'member_id': 'memberId',
            'team': 'team',
            'portal': 'portal',
            'member': 'member'
        }

        self._type = type
        self._title = title
        self._body = body
        self._read = read
        self._buttons = buttons
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._portal_id = portal_id
        self._member_id = member_id
        self._team = team
        self._portal = portal
        self._member = member


    @property
    def type(self):
        """
        Gets the type of this Notification.


        :return: The type of this Notification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Notification.


        :param type: The type of this Notification.
        :type: str
        """
        allowed_values = ["team.billing.subscription.trial_will_end", "team.billing.subscription.updated_plan", "team.billing.subscription.updated_additional", "team.billing.subscription.deleted", "team.billing.invoice.created", "team.billing.invoice.upcoming", "team.billing.invoice.payment_succeeded", "team.billing.invoice.payment_failed"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def title(self):
        """
        Gets the title of this Notification.


        :return: The title of this Notification.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Notification.


        :param title: The title of this Notification.
        :type: str
        """

        self._title = title

    @property
    def body(self):
        """
        Gets the body of this Notification.


        :return: The body of this Notification.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this Notification.


        :param body: The body of this Notification.
        :type: str
        """

        self._body = body

    @property
    def read(self):
        """
        Gets the read of this Notification.


        :return: The read of this Notification.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """
        Sets the read of this Notification.


        :param read: The read of this Notification.
        :type: bool
        """

        self._read = read

    @property
    def buttons(self):
        """
        Gets the buttons of this Notification.


        :return: The buttons of this Notification.
        :rtype: list[NotificationButton]
        """
        return self._buttons

    @buttons.setter
    def buttons(self, buttons):
        """
        Sets the buttons of this Notification.


        :param buttons: The buttons of this Notification.
        :type: list[NotificationButton]
        """

        self._buttons = buttons

    @property
    def created(self):
        """
        Gets the created of this Notification.


        :return: The created of this Notification.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Notification.


        :param created: The created of this Notification.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Notification.


        :return: The modified of this Notification.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Notification.


        :param modified: The modified of this Notification.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Notification.


        :return: The id of this Notification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Notification.


        :param id: The id of this Notification.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this Notification.


        :return: The team_id of this Notification.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this Notification.


        :param team_id: The team_id of this Notification.
        :type: str
        """

        self._team_id = team_id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this Notification.


        :return: The portal_id of this Notification.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this Notification.


        :param portal_id: The portal_id of this Notification.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def member_id(self):
        """
        Gets the member_id of this Notification.


        :return: The member_id of this Notification.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this Notification.


        :param member_id: The member_id of this Notification.
        :type: str
        """

        self._member_id = member_id

    @property
    def team(self):
        """
        Gets the team of this Notification.


        :return: The team of this Notification.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Notification.


        :param team: The team of this Notification.
        :type: Team
        """

        self._team = team

    @property
    def portal(self):
        """
        Gets the portal of this Notification.


        :return: The portal of this Notification.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this Notification.


        :param portal: The portal of this Notification.
        :type: Portal
        """

        self._portal = portal

    @property
    def member(self):
        """
        Gets the member of this Notification.


        :return: The member of this Notification.
        :rtype: TeamMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this Notification.


        :param member: The member of this Notification.
        :type: TeamMember
        """

        self._member = member

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
