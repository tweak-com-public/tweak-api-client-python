# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.2
    
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


class Customer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, profile_picture=None, first_name=None, last_name=None, initials=None, status=None, created=None, modified=None, realm=None, username=None, email=None, email_verified=None, id=None, teams=None, invitation_tickets=None, access_tokens=None, permission=None):
        """
        Customer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'profile_picture': 'object',
            'first_name': 'str',
            'last_name': 'str',
            'initials': 'str',
            'status': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'realm': 'str',
            'username': 'str',
            'email': 'str',
            'email_verified': 'bool',
            'id': 'str',
            'teams': 'list[Team]',
            'invitation_tickets': 'list[InvitationTicket]',
            'access_tokens': 'list[TeamMemberAccessToken]',
            'permission': 'CustomerPermissionSet'
        }

        self.attribute_map = {
            'profile_picture': 'profilePicture',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'initials': 'initials',
            'status': 'status',
            'created': 'created',
            'modified': 'modified',
            'realm': 'realm',
            'username': 'username',
            'email': 'email',
            'email_verified': 'emailVerified',
            'id': 'id',
            'teams': 'teams',
            'invitation_tickets': 'invitationTickets',
            'access_tokens': 'accessTokens',
            'permission': 'permission'
        }

        self._profile_picture = profile_picture
        self._first_name = first_name
        self._last_name = last_name
        self._initials = initials
        self._status = status
        self._created = created
        self._modified = modified
        self._realm = realm
        self._username = username
        self._email = email
        self._email_verified = email_verified
        self._id = id
        self._teams = teams
        self._invitation_tickets = invitation_tickets
        self._access_tokens = access_tokens
        self._permission = permission


    @property
    def profile_picture(self):
        """
        Gets the profile_picture of this Customer.


        :return: The profile_picture of this Customer.
        :rtype: object
        """
        return self._profile_picture

    @profile_picture.setter
    def profile_picture(self, profile_picture):
        """
        Sets the profile_picture of this Customer.


        :param profile_picture: The profile_picture of this Customer.
        :type: object
        """

        self._profile_picture = profile_picture

    @property
    def first_name(self):
        """
        Gets the first_name of this Customer.


        :return: The first_name of this Customer.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Customer.


        :return: The last_name of this Customer.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.
        :type: str
        """

        self._last_name = last_name

    @property
    def initials(self):
        """
        Gets the initials of this Customer.


        :return: The initials of this Customer.
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials):
        """
        Sets the initials of this Customer.


        :param initials: The initials of this Customer.
        :type: str
        """

        self._initials = initials

    @property
    def status(self):
        """
        Gets the status of this Customer.


        :return: The status of this Customer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Customer.


        :param status: The status of this Customer.
        :type: str
        """
        allowed_values = ["active", "inactive", "godmode"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created(self):
        """
        Gets the created of this Customer.


        :return: The created of this Customer.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Customer.


        :param created: The created of this Customer.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Customer.


        :return: The modified of this Customer.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Customer.


        :param modified: The modified of this Customer.
        :type: datetime
        """

        self._modified = modified

    @property
    def realm(self):
        """
        Gets the realm of this Customer.


        :return: The realm of this Customer.
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """
        Sets the realm of this Customer.


        :param realm: The realm of this Customer.
        :type: str
        """

        self._realm = realm

    @property
    def username(self):
        """
        Gets the username of this Customer.


        :return: The username of this Customer.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this Customer.


        :param username: The username of this Customer.
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """
        Gets the email of this Customer.


        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Customer.


        :param email: The email of this Customer.
        :type: str
        """

        self._email = email

    @property
    def email_verified(self):
        """
        Gets the email_verified of this Customer.


        :return: The email_verified of this Customer.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """
        Sets the email_verified of this Customer.


        :param email_verified: The email_verified of this Customer.
        :type: bool
        """

        self._email_verified = email_verified

    @property
    def id(self):
        """
        Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Customer.


        :param id: The id of this Customer.
        :type: str
        """

        self._id = id

    @property
    def teams(self):
        """
        Gets the teams of this Customer.


        :return: The teams of this Customer.
        :rtype: list[Team]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """
        Sets the teams of this Customer.


        :param teams: The teams of this Customer.
        :type: list[Team]
        """

        self._teams = teams

    @property
    def invitation_tickets(self):
        """
        Gets the invitation_tickets of this Customer.


        :return: The invitation_tickets of this Customer.
        :rtype: list[InvitationTicket]
        """
        return self._invitation_tickets

    @invitation_tickets.setter
    def invitation_tickets(self, invitation_tickets):
        """
        Sets the invitation_tickets of this Customer.


        :param invitation_tickets: The invitation_tickets of this Customer.
        :type: list[InvitationTicket]
        """

        self._invitation_tickets = invitation_tickets

    @property
    def access_tokens(self):
        """
        Gets the access_tokens of this Customer.


        :return: The access_tokens of this Customer.
        :rtype: list[TeamMemberAccessToken]
        """
        return self._access_tokens

    @access_tokens.setter
    def access_tokens(self, access_tokens):
        """
        Sets the access_tokens of this Customer.


        :param access_tokens: The access_tokens of this Customer.
        :type: list[TeamMemberAccessToken]
        """

        self._access_tokens = access_tokens

    @property
    def permission(self):
        """
        Gets the permission of this Customer.


        :return: The permission of this Customer.
        :rtype: CustomerPermissionSet
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """
        Sets the permission of this Customer.


        :param permission: The permission of this Customer.
        :type: CustomerPermissionSet
        """

        self._permission = permission

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
