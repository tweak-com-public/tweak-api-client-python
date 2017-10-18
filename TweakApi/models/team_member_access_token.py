# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.2-alpha.1
    
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


class TeamMemberAccessToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, roles=None, refresh_token=None, id=None, ttl=1209600.0, scopes=None, created=None, user_id=None, team_id=None, team_member_id=None, portal_id=None, portal_member_id=None, customer=None, team=None, team_member=None, portal=None, portal_member=None):
        """
        TeamMemberAccessToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'roles': 'list[str]',
            'refresh_token': 'str',
            'id': 'str',
            'ttl': 'float',
            'scopes': 'list[str]',
            'created': 'datetime',
            'user_id': 'str',
            'team_id': 'str',
            'team_member_id': 'str',
            'portal_id': 'str',
            'portal_member_id': 'str',
            'customer': 'Customer',
            'team': 'Team',
            'team_member': 'TeamMember',
            'portal': 'Portal',
            'portal_member': 'PortalMember'
        }

        self.attribute_map = {
            'roles': 'roles',
            'refresh_token': 'refreshToken',
            'id': 'id',
            'ttl': 'ttl',
            'scopes': 'scopes',
            'created': 'created',
            'user_id': 'userId',
            'team_id': 'teamId',
            'team_member_id': 'teamMemberId',
            'portal_id': 'portalId',
            'portal_member_id': 'portalMemberId',
            'customer': 'customer',
            'team': 'team',
            'team_member': 'teamMember',
            'portal': 'portal',
            'portal_member': 'portalMember'
        }

        self._roles = roles
        self._refresh_token = refresh_token
        self._id = id
        self._ttl = ttl
        self._scopes = scopes
        self._created = created
        self._user_id = user_id
        self._team_id = team_id
        self._team_member_id = team_member_id
        self._portal_id = portal_id
        self._portal_member_id = portal_member_id
        self._customer = customer
        self._team = team
        self._team_member = team_member
        self._portal = portal
        self._portal_member = portal_member


    @property
    def roles(self):
        """
        Gets the roles of this TeamMemberAccessToken.


        :return: The roles of this TeamMemberAccessToken.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this TeamMemberAccessToken.


        :param roles: The roles of this TeamMemberAccessToken.
        :type: list[str]
        """

        self._roles = roles

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this TeamMemberAccessToken.


        :return: The refresh_token of this TeamMemberAccessToken.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this TeamMemberAccessToken.


        :param refresh_token: The refresh_token of this TeamMemberAccessToken.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def id(self):
        """
        Gets the id of this TeamMemberAccessToken.


        :return: The id of this TeamMemberAccessToken.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TeamMemberAccessToken.


        :param id: The id of this TeamMemberAccessToken.
        :type: str
        """

        self._id = id

    @property
    def ttl(self):
        """
        Gets the ttl of this TeamMemberAccessToken.
        time to live in seconds (2 weeks by default)

        :return: The ttl of this TeamMemberAccessToken.
        :rtype: float
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this TeamMemberAccessToken.
        time to live in seconds (2 weeks by default)

        :param ttl: The ttl of this TeamMemberAccessToken.
        :type: float
        """

        self._ttl = ttl

    @property
    def scopes(self):
        """
        Gets the scopes of this TeamMemberAccessToken.
        Array of scopes granted to this access token.

        :return: The scopes of this TeamMemberAccessToken.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this TeamMemberAccessToken.
        Array of scopes granted to this access token.

        :param scopes: The scopes of this TeamMemberAccessToken.
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def created(self):
        """
        Gets the created of this TeamMemberAccessToken.


        :return: The created of this TeamMemberAccessToken.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this TeamMemberAccessToken.


        :param created: The created of this TeamMemberAccessToken.
        :type: datetime
        """

        self._created = created

    @property
    def user_id(self):
        """
        Gets the user_id of this TeamMemberAccessToken.


        :return: The user_id of this TeamMemberAccessToken.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this TeamMemberAccessToken.


        :param user_id: The user_id of this TeamMemberAccessToken.
        :type: str
        """

        self._user_id = user_id

    @property
    def team_id(self):
        """
        Gets the team_id of this TeamMemberAccessToken.


        :return: The team_id of this TeamMemberAccessToken.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this TeamMemberAccessToken.


        :param team_id: The team_id of this TeamMemberAccessToken.
        :type: str
        """

        self._team_id = team_id

    @property
    def team_member_id(self):
        """
        Gets the team_member_id of this TeamMemberAccessToken.


        :return: The team_member_id of this TeamMemberAccessToken.
        :rtype: str
        """
        return self._team_member_id

    @team_member_id.setter
    def team_member_id(self, team_member_id):
        """
        Sets the team_member_id of this TeamMemberAccessToken.


        :param team_member_id: The team_member_id of this TeamMemberAccessToken.
        :type: str
        """

        self._team_member_id = team_member_id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this TeamMemberAccessToken.


        :return: The portal_id of this TeamMemberAccessToken.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this TeamMemberAccessToken.


        :param portal_id: The portal_id of this TeamMemberAccessToken.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def portal_member_id(self):
        """
        Gets the portal_member_id of this TeamMemberAccessToken.


        :return: The portal_member_id of this TeamMemberAccessToken.
        :rtype: str
        """
        return self._portal_member_id

    @portal_member_id.setter
    def portal_member_id(self, portal_member_id):
        """
        Sets the portal_member_id of this TeamMemberAccessToken.


        :param portal_member_id: The portal_member_id of this TeamMemberAccessToken.
        :type: str
        """

        self._portal_member_id = portal_member_id

    @property
    def customer(self):
        """
        Gets the customer of this TeamMemberAccessToken.


        :return: The customer of this TeamMemberAccessToken.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this TeamMemberAccessToken.


        :param customer: The customer of this TeamMemberAccessToken.
        :type: Customer
        """

        self._customer = customer

    @property
    def team(self):
        """
        Gets the team of this TeamMemberAccessToken.


        :return: The team of this TeamMemberAccessToken.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this TeamMemberAccessToken.


        :param team: The team of this TeamMemberAccessToken.
        :type: Team
        """

        self._team = team

    @property
    def team_member(self):
        """
        Gets the team_member of this TeamMemberAccessToken.


        :return: The team_member of this TeamMemberAccessToken.
        :rtype: TeamMember
        """
        return self._team_member

    @team_member.setter
    def team_member(self, team_member):
        """
        Sets the team_member of this TeamMemberAccessToken.


        :param team_member: The team_member of this TeamMemberAccessToken.
        :type: TeamMember
        """

        self._team_member = team_member

    @property
    def portal(self):
        """
        Gets the portal of this TeamMemberAccessToken.


        :return: The portal of this TeamMemberAccessToken.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this TeamMemberAccessToken.


        :param portal: The portal of this TeamMemberAccessToken.
        :type: Portal
        """

        self._portal = portal

    @property
    def portal_member(self):
        """
        Gets the portal_member of this TeamMemberAccessToken.


        :return: The portal_member of this TeamMemberAccessToken.
        :rtype: PortalMember
        """
        return self._portal_member

    @portal_member.setter
    def portal_member(self, portal_member):
        """
        Sets the portal_member of this TeamMemberAccessToken.


        :param portal_member: The portal_member of this TeamMemberAccessToken.
        :type: PortalMember
        """

        self._portal_member = portal_member

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
