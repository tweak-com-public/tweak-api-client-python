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


class InvitationTicket(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message='', token=None, invitee_email=None, target_model=None, target_id=None, target_attrs=None, status=None, notify=True, created=None, modified=None, id=None, invitee_id=None, inviter_id=None, target_team_id=None, target_team_member_id=None, target_portal_id=None, target_portal_member_id=None, target_template_id=None, target_design_id=None, target_template_member_id=None, target_design_member_id=None, target_image_folder_id=None, target_image_folder_member_id=None, invitee=None, inviter=None, target_team=None, target_team_member=None, target_portal=None, target_portal_member=None, target_template=None, target_template_member=None, target_image_folder=None, target_image_folder_member=None, target_design=None, target_design_member=None):
        """
        InvitationTicket - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'token': 'str',
            'invitee_email': 'str',
            'target_model': 'str',
            'target_id': 'str',
            'target_attrs': 'object',
            'status': 'str',
            'notify': 'bool',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'invitee_id': 'str',
            'inviter_id': 'str',
            'target_team_id': 'str',
            'target_team_member_id': 'str',
            'target_portal_id': 'str',
            'target_portal_member_id': 'str',
            'target_template_id': 'str',
            'target_design_id': 'str',
            'target_template_member_id': 'str',
            'target_design_member_id': 'str',
            'target_image_folder_id': 'str',
            'target_image_folder_member_id': 'str',
            'invitee': 'Customer',
            'inviter': 'TeamMember',
            'target_team': 'Team',
            'target_team_member': 'TeamMember',
            'target_portal': 'Portal',
            'target_portal_member': 'PortalMember',
            'target_template': 'Template',
            'target_template_member': 'TemplateMember',
            'target_image_folder': 'ImageFolder',
            'target_image_folder_member': 'ImageFolderMember',
            'target_design': 'Design',
            'target_design_member': 'DesignMember'
        }

        self.attribute_map = {
            'message': 'message',
            'token': 'token',
            'invitee_email': 'inviteeEmail',
            'target_model': 'targetModel',
            'target_id': 'targetId',
            'target_attrs': 'targetAttrs',
            'status': 'status',
            'notify': 'notify',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'invitee_id': 'inviteeId',
            'inviter_id': 'inviterId',
            'target_team_id': 'targetTeamId',
            'target_team_member_id': 'targetTeamMemberId',
            'target_portal_id': 'targetPortalId',
            'target_portal_member_id': 'targetPortalMemberId',
            'target_template_id': 'targetTemplateId',
            'target_design_id': 'targetDesignId',
            'target_template_member_id': 'targetTemplateMemberId',
            'target_design_member_id': 'targetDesignMemberId',
            'target_image_folder_id': 'targetImageFolderId',
            'target_image_folder_member_id': 'targetImageFolderMemberId',
            'invitee': 'invitee',
            'inviter': 'inviter',
            'target_team': 'targetTeam',
            'target_team_member': 'targetTeamMember',
            'target_portal': 'targetPortal',
            'target_portal_member': 'targetPortalMember',
            'target_template': 'targetTemplate',
            'target_template_member': 'targetTemplateMember',
            'target_image_folder': 'targetImageFolder',
            'target_image_folder_member': 'targetImageFolderMember',
            'target_design': 'targetDesign',
            'target_design_member': 'targetDesignMember'
        }

        self._message = message
        self._token = token
        self._invitee_email = invitee_email
        self._target_model = target_model
        self._target_id = target_id
        self._target_attrs = target_attrs
        self._status = status
        self._notify = notify
        self._created = created
        self._modified = modified
        self._id = id
        self._invitee_id = invitee_id
        self._inviter_id = inviter_id
        self._target_team_id = target_team_id
        self._target_team_member_id = target_team_member_id
        self._target_portal_id = target_portal_id
        self._target_portal_member_id = target_portal_member_id
        self._target_template_id = target_template_id
        self._target_design_id = target_design_id
        self._target_template_member_id = target_template_member_id
        self._target_design_member_id = target_design_member_id
        self._target_image_folder_id = target_image_folder_id
        self._target_image_folder_member_id = target_image_folder_member_id
        self._invitee = invitee
        self._inviter = inviter
        self._target_team = target_team
        self._target_team_member = target_team_member
        self._target_portal = target_portal
        self._target_portal_member = target_portal_member
        self._target_template = target_template
        self._target_template_member = target_template_member
        self._target_image_folder = target_image_folder
        self._target_image_folder_member = target_image_folder_member
        self._target_design = target_design
        self._target_design_member = target_design_member


    @property
    def message(self):
        """
        Gets the message of this InvitationTicket.


        :return: The message of this InvitationTicket.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InvitationTicket.


        :param message: The message of this InvitationTicket.
        :type: str
        """

        self._message = message

    @property
    def token(self):
        """
        Gets the token of this InvitationTicket.


        :return: The token of this InvitationTicket.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this InvitationTicket.


        :param token: The token of this InvitationTicket.
        :type: str
        """

        self._token = token

    @property
    def invitee_email(self):
        """
        Gets the invitee_email of this InvitationTicket.


        :return: The invitee_email of this InvitationTicket.
        :rtype: str
        """
        return self._invitee_email

    @invitee_email.setter
    def invitee_email(self, invitee_email):
        """
        Sets the invitee_email of this InvitationTicket.


        :param invitee_email: The invitee_email of this InvitationTicket.
        :type: str
        """

        self._invitee_email = invitee_email

    @property
    def target_model(self):
        """
        Gets the target_model of this InvitationTicket.


        :return: The target_model of this InvitationTicket.
        :rtype: str
        """
        return self._target_model

    @target_model.setter
    def target_model(self, target_model):
        """
        Sets the target_model of this InvitationTicket.


        :param target_model: The target_model of this InvitationTicket.
        :type: str
        """
        allowed_values = ["Team", "Portal", "Template", "ImageFolder", "Design"]
        if target_model not in allowed_values:
            raise ValueError(
                "Invalid value for `target_model` ({0}), must be one of {1}"
                .format(target_model, allowed_values)
            )

        self._target_model = target_model

    @property
    def target_id(self):
        """
        Gets the target_id of this InvitationTicket.


        :return: The target_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this InvitationTicket.


        :param target_id: The target_id of this InvitationTicket.
        :type: str
        """

        self._target_id = target_id

    @property
    def target_attrs(self):
        """
        Gets the target_attrs of this InvitationTicket.


        :return: The target_attrs of this InvitationTicket.
        :rtype: object
        """
        return self._target_attrs

    @target_attrs.setter
    def target_attrs(self, target_attrs):
        """
        Sets the target_attrs of this InvitationTicket.


        :param target_attrs: The target_attrs of this InvitationTicket.
        :type: object
        """

        self._target_attrs = target_attrs

    @property
    def status(self):
        """
        Gets the status of this InvitationTicket.


        :return: The status of this InvitationTicket.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InvitationTicket.


        :param status: The status of this InvitationTicket.
        :type: str
        """
        allowed_values = ["pending", "accepted"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def notify(self):
        """
        Gets the notify of this InvitationTicket.


        :return: The notify of this InvitationTicket.
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """
        Sets the notify of this InvitationTicket.


        :param notify: The notify of this InvitationTicket.
        :type: bool
        """

        self._notify = notify

    @property
    def created(self):
        """
        Gets the created of this InvitationTicket.


        :return: The created of this InvitationTicket.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this InvitationTicket.


        :param created: The created of this InvitationTicket.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this InvitationTicket.


        :return: The modified of this InvitationTicket.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this InvitationTicket.


        :param modified: The modified of this InvitationTicket.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this InvitationTicket.


        :return: The id of this InvitationTicket.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InvitationTicket.


        :param id: The id of this InvitationTicket.
        :type: str
        """

        self._id = id

    @property
    def invitee_id(self):
        """
        Gets the invitee_id of this InvitationTicket.


        :return: The invitee_id of this InvitationTicket.
        :rtype: str
        """
        return self._invitee_id

    @invitee_id.setter
    def invitee_id(self, invitee_id):
        """
        Sets the invitee_id of this InvitationTicket.


        :param invitee_id: The invitee_id of this InvitationTicket.
        :type: str
        """

        self._invitee_id = invitee_id

    @property
    def inviter_id(self):
        """
        Gets the inviter_id of this InvitationTicket.


        :return: The inviter_id of this InvitationTicket.
        :rtype: str
        """
        return self._inviter_id

    @inviter_id.setter
    def inviter_id(self, inviter_id):
        """
        Sets the inviter_id of this InvitationTicket.


        :param inviter_id: The inviter_id of this InvitationTicket.
        :type: str
        """

        self._inviter_id = inviter_id

    @property
    def target_team_id(self):
        """
        Gets the target_team_id of this InvitationTicket.


        :return: The target_team_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_team_id

    @target_team_id.setter
    def target_team_id(self, target_team_id):
        """
        Sets the target_team_id of this InvitationTicket.


        :param target_team_id: The target_team_id of this InvitationTicket.
        :type: str
        """

        self._target_team_id = target_team_id

    @property
    def target_team_member_id(self):
        """
        Gets the target_team_member_id of this InvitationTicket.


        :return: The target_team_member_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_team_member_id

    @target_team_member_id.setter
    def target_team_member_id(self, target_team_member_id):
        """
        Sets the target_team_member_id of this InvitationTicket.


        :param target_team_member_id: The target_team_member_id of this InvitationTicket.
        :type: str
        """

        self._target_team_member_id = target_team_member_id

    @property
    def target_portal_id(self):
        """
        Gets the target_portal_id of this InvitationTicket.


        :return: The target_portal_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_portal_id

    @target_portal_id.setter
    def target_portal_id(self, target_portal_id):
        """
        Sets the target_portal_id of this InvitationTicket.


        :param target_portal_id: The target_portal_id of this InvitationTicket.
        :type: str
        """

        self._target_portal_id = target_portal_id

    @property
    def target_portal_member_id(self):
        """
        Gets the target_portal_member_id of this InvitationTicket.


        :return: The target_portal_member_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_portal_member_id

    @target_portal_member_id.setter
    def target_portal_member_id(self, target_portal_member_id):
        """
        Sets the target_portal_member_id of this InvitationTicket.


        :param target_portal_member_id: The target_portal_member_id of this InvitationTicket.
        :type: str
        """

        self._target_portal_member_id = target_portal_member_id

    @property
    def target_template_id(self):
        """
        Gets the target_template_id of this InvitationTicket.


        :return: The target_template_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_template_id

    @target_template_id.setter
    def target_template_id(self, target_template_id):
        """
        Sets the target_template_id of this InvitationTicket.


        :param target_template_id: The target_template_id of this InvitationTicket.
        :type: str
        """

        self._target_template_id = target_template_id

    @property
    def target_design_id(self):
        """
        Gets the target_design_id of this InvitationTicket.


        :return: The target_design_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_design_id

    @target_design_id.setter
    def target_design_id(self, target_design_id):
        """
        Sets the target_design_id of this InvitationTicket.


        :param target_design_id: The target_design_id of this InvitationTicket.
        :type: str
        """

        self._target_design_id = target_design_id

    @property
    def target_template_member_id(self):
        """
        Gets the target_template_member_id of this InvitationTicket.


        :return: The target_template_member_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_template_member_id

    @target_template_member_id.setter
    def target_template_member_id(self, target_template_member_id):
        """
        Sets the target_template_member_id of this InvitationTicket.


        :param target_template_member_id: The target_template_member_id of this InvitationTicket.
        :type: str
        """

        self._target_template_member_id = target_template_member_id

    @property
    def target_design_member_id(self):
        """
        Gets the target_design_member_id of this InvitationTicket.


        :return: The target_design_member_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_design_member_id

    @target_design_member_id.setter
    def target_design_member_id(self, target_design_member_id):
        """
        Sets the target_design_member_id of this InvitationTicket.


        :param target_design_member_id: The target_design_member_id of this InvitationTicket.
        :type: str
        """

        self._target_design_member_id = target_design_member_id

    @property
    def target_image_folder_id(self):
        """
        Gets the target_image_folder_id of this InvitationTicket.


        :return: The target_image_folder_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_image_folder_id

    @target_image_folder_id.setter
    def target_image_folder_id(self, target_image_folder_id):
        """
        Sets the target_image_folder_id of this InvitationTicket.


        :param target_image_folder_id: The target_image_folder_id of this InvitationTicket.
        :type: str
        """

        self._target_image_folder_id = target_image_folder_id

    @property
    def target_image_folder_member_id(self):
        """
        Gets the target_image_folder_member_id of this InvitationTicket.


        :return: The target_image_folder_member_id of this InvitationTicket.
        :rtype: str
        """
        return self._target_image_folder_member_id

    @target_image_folder_member_id.setter
    def target_image_folder_member_id(self, target_image_folder_member_id):
        """
        Sets the target_image_folder_member_id of this InvitationTicket.


        :param target_image_folder_member_id: The target_image_folder_member_id of this InvitationTicket.
        :type: str
        """

        self._target_image_folder_member_id = target_image_folder_member_id

    @property
    def invitee(self):
        """
        Gets the invitee of this InvitationTicket.


        :return: The invitee of this InvitationTicket.
        :rtype: Customer
        """
        return self._invitee

    @invitee.setter
    def invitee(self, invitee):
        """
        Sets the invitee of this InvitationTicket.


        :param invitee: The invitee of this InvitationTicket.
        :type: Customer
        """

        self._invitee = invitee

    @property
    def inviter(self):
        """
        Gets the inviter of this InvitationTicket.


        :return: The inviter of this InvitationTicket.
        :rtype: TeamMember
        """
        return self._inviter

    @inviter.setter
    def inviter(self, inviter):
        """
        Sets the inviter of this InvitationTicket.


        :param inviter: The inviter of this InvitationTicket.
        :type: TeamMember
        """

        self._inviter = inviter

    @property
    def target_team(self):
        """
        Gets the target_team of this InvitationTicket.


        :return: The target_team of this InvitationTicket.
        :rtype: Team
        """
        return self._target_team

    @target_team.setter
    def target_team(self, target_team):
        """
        Sets the target_team of this InvitationTicket.


        :param target_team: The target_team of this InvitationTicket.
        :type: Team
        """

        self._target_team = target_team

    @property
    def target_team_member(self):
        """
        Gets the target_team_member of this InvitationTicket.


        :return: The target_team_member of this InvitationTicket.
        :rtype: TeamMember
        """
        return self._target_team_member

    @target_team_member.setter
    def target_team_member(self, target_team_member):
        """
        Sets the target_team_member of this InvitationTicket.


        :param target_team_member: The target_team_member of this InvitationTicket.
        :type: TeamMember
        """

        self._target_team_member = target_team_member

    @property
    def target_portal(self):
        """
        Gets the target_portal of this InvitationTicket.


        :return: The target_portal of this InvitationTicket.
        :rtype: Portal
        """
        return self._target_portal

    @target_portal.setter
    def target_portal(self, target_portal):
        """
        Sets the target_portal of this InvitationTicket.


        :param target_portal: The target_portal of this InvitationTicket.
        :type: Portal
        """

        self._target_portal = target_portal

    @property
    def target_portal_member(self):
        """
        Gets the target_portal_member of this InvitationTicket.


        :return: The target_portal_member of this InvitationTicket.
        :rtype: PortalMember
        """
        return self._target_portal_member

    @target_portal_member.setter
    def target_portal_member(self, target_portal_member):
        """
        Sets the target_portal_member of this InvitationTicket.


        :param target_portal_member: The target_portal_member of this InvitationTicket.
        :type: PortalMember
        """

        self._target_portal_member = target_portal_member

    @property
    def target_template(self):
        """
        Gets the target_template of this InvitationTicket.


        :return: The target_template of this InvitationTicket.
        :rtype: Template
        """
        return self._target_template

    @target_template.setter
    def target_template(self, target_template):
        """
        Sets the target_template of this InvitationTicket.


        :param target_template: The target_template of this InvitationTicket.
        :type: Template
        """

        self._target_template = target_template

    @property
    def target_template_member(self):
        """
        Gets the target_template_member of this InvitationTicket.


        :return: The target_template_member of this InvitationTicket.
        :rtype: TemplateMember
        """
        return self._target_template_member

    @target_template_member.setter
    def target_template_member(self, target_template_member):
        """
        Sets the target_template_member of this InvitationTicket.


        :param target_template_member: The target_template_member of this InvitationTicket.
        :type: TemplateMember
        """

        self._target_template_member = target_template_member

    @property
    def target_image_folder(self):
        """
        Gets the target_image_folder of this InvitationTicket.


        :return: The target_image_folder of this InvitationTicket.
        :rtype: ImageFolder
        """
        return self._target_image_folder

    @target_image_folder.setter
    def target_image_folder(self, target_image_folder):
        """
        Sets the target_image_folder of this InvitationTicket.


        :param target_image_folder: The target_image_folder of this InvitationTicket.
        :type: ImageFolder
        """

        self._target_image_folder = target_image_folder

    @property
    def target_image_folder_member(self):
        """
        Gets the target_image_folder_member of this InvitationTicket.


        :return: The target_image_folder_member of this InvitationTicket.
        :rtype: ImageFolderMember
        """
        return self._target_image_folder_member

    @target_image_folder_member.setter
    def target_image_folder_member(self, target_image_folder_member):
        """
        Sets the target_image_folder_member of this InvitationTicket.


        :param target_image_folder_member: The target_image_folder_member of this InvitationTicket.
        :type: ImageFolderMember
        """

        self._target_image_folder_member = target_image_folder_member

    @property
    def target_design(self):
        """
        Gets the target_design of this InvitationTicket.


        :return: The target_design of this InvitationTicket.
        :rtype: Design
        """
        return self._target_design

    @target_design.setter
    def target_design(self, target_design):
        """
        Sets the target_design of this InvitationTicket.


        :param target_design: The target_design of this InvitationTicket.
        :type: Design
        """

        self._target_design = target_design

    @property
    def target_design_member(self):
        """
        Gets the target_design_member of this InvitationTicket.


        :return: The target_design_member of this InvitationTicket.
        :rtype: DesignMember
        """
        return self._target_design_member

    @target_design_member.setter
    def target_design_member(self, target_design_member):
        """
        Sets the target_design_member of this InvitationTicket.


        :param target_design_member: The target_design_member of this InvitationTicket.
        :type: DesignMember
        """

        self._target_design_member = target_design_member

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
