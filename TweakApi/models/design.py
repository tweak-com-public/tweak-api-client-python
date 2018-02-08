# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.0
    
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


class Design(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, colors=None, image=None, name=None, object=None, thumbnail=None, description='', purpose=None, status=None, form_data=None, high_res_pdf_url='', proof_pdf_url='', jpegs_url='', edited=None, expired=None, path='/', sent_for_approval=None, approved=None, shared=None, created=None, modified=None, id=None, dynamic_data_id=None, team_id=None, requester_id=None, assignee_id=None, reviewer_id=None, template_id=None, portal_id=None, rejection_comment_id=None, folder_id=None, tags=None, template=None, portal=None, team=None, comments=None, rejection_comment=None, exports=None, requester=None, assignee=None, reviewer=None, commenters=None, folder=None, permission=None, members=None, design_members=None, dynamic_data=None):
        """
        Design - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'colors': 'list[str]',
            'image': 'str',
            'name': 'str',
            'object': 'object',
            'thumbnail': 'str',
            'description': 'str',
            'purpose': 'str',
            'status': 'str',
            'form_data': 'list[object]',
            'high_res_pdf_url': 'str',
            'proof_pdf_url': 'str',
            'jpegs_url': 'str',
            'edited': 'datetime',
            'expired': 'datetime',
            'path': 'str',
            'sent_for_approval': 'datetime',
            'approved': 'datetime',
            'shared': 'datetime',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'dynamic_data_id': 'str',
            'team_id': 'str',
            'requester_id': 'str',
            'assignee_id': 'str',
            'reviewer_id': 'str',
            'template_id': 'str',
            'portal_id': 'str',
            'rejection_comment_id': 'str',
            'folder_id': 'str',
            'tags': 'list[Tag]',
            'template': 'Template',
            'portal': 'Portal',
            'team': 'Team',
            'comments': 'list[DesignComment]',
            'rejection_comment': 'DesignComment',
            'exports': 'list[DesignExport]',
            'requester': 'TeamMember',
            'assignee': 'TeamMember',
            'reviewer': 'TeamMember',
            'commenters': 'list[TeamMember]',
            'folder': 'DesignFolder',
            'permission': 'DesignPermissionSet',
            'members': 'list[TeamMember]',
            'design_members': 'list[DesignMember]',
            'dynamic_data': 'DynamicData'
        }

        self.attribute_map = {
            'colors': 'colors',
            'image': 'image',
            'name': 'name',
            'object': 'object',
            'thumbnail': 'thumbnail',
            'description': 'description',
            'purpose': 'purpose',
            'status': 'status',
            'form_data': 'formData',
            'high_res_pdf_url': 'highResPdfUrl',
            'proof_pdf_url': 'proofPdfUrl',
            'jpegs_url': 'jpegsUrl',
            'edited': 'edited',
            'expired': 'expired',
            'path': 'path',
            'sent_for_approval': 'sentForApproval',
            'approved': 'approved',
            'shared': 'shared',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'dynamic_data_id': 'dynamicDataId',
            'team_id': 'teamId',
            'requester_id': 'requesterId',
            'assignee_id': 'assigneeId',
            'reviewer_id': 'reviewerId',
            'template_id': 'templateId',
            'portal_id': 'portalId',
            'rejection_comment_id': 'rejectionCommentId',
            'folder_id': 'folderId',
            'tags': 'tags',
            'template': 'template',
            'portal': 'portal',
            'team': 'team',
            'comments': 'comments',
            'rejection_comment': 'rejectionComment',
            'exports': 'exports',
            'requester': 'requester',
            'assignee': 'assignee',
            'reviewer': 'reviewer',
            'commenters': 'commenters',
            'folder': 'folder',
            'permission': 'permission',
            'members': 'members',
            'design_members': 'designMembers',
            'dynamic_data': 'dynamicData'
        }

        self._colors = colors
        self._image = image
        self._name = name
        self._object = object
        self._thumbnail = thumbnail
        self._description = description
        self._purpose = purpose
        self._status = status
        self._form_data = form_data
        self._high_res_pdf_url = high_res_pdf_url
        self._proof_pdf_url = proof_pdf_url
        self._jpegs_url = jpegs_url
        self._edited = edited
        self._expired = expired
        self._path = path
        self._sent_for_approval = sent_for_approval
        self._approved = approved
        self._shared = shared
        self._created = created
        self._modified = modified
        self._id = id
        self._dynamic_data_id = dynamic_data_id
        self._team_id = team_id
        self._requester_id = requester_id
        self._assignee_id = assignee_id
        self._reviewer_id = reviewer_id
        self._template_id = template_id
        self._portal_id = portal_id
        self._rejection_comment_id = rejection_comment_id
        self._folder_id = folder_id
        self._tags = tags
        self._template = template
        self._portal = portal
        self._team = team
        self._comments = comments
        self._rejection_comment = rejection_comment
        self._exports = exports
        self._requester = requester
        self._assignee = assignee
        self._reviewer = reviewer
        self._commenters = commenters
        self._folder = folder
        self._permission = permission
        self._members = members
        self._design_members = design_members
        self._dynamic_data = dynamic_data


    @property
    def colors(self):
        """
        Gets the colors of this Design.


        :return: The colors of this Design.
        :rtype: list[str]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """
        Sets the colors of this Design.


        :param colors: The colors of this Design.
        :type: list[str]
        """

        self._colors = colors

    @property
    def image(self):
        """
        Gets the image of this Design.


        :return: The image of this Design.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Design.


        :param image: The image of this Design.
        :type: str
        """

        self._image = image

    @property
    def name(self):
        """
        Gets the name of this Design.


        :return: The name of this Design.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Design.


        :param name: The name of this Design.
        :type: str
        """

        self._name = name

    @property
    def object(self):
        """
        Gets the object of this Design.


        :return: The object of this Design.
        :rtype: object
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this Design.


        :param object: The object of this Design.
        :type: object
        """

        self._object = object

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this Design.


        :return: The thumbnail of this Design.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this Design.


        :param thumbnail: The thumbnail of this Design.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def description(self):
        """
        Gets the description of this Design.


        :return: The description of this Design.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Design.


        :param description: The description of this Design.
        :type: str
        """

        self._description = description

    @property
    def purpose(self):
        """
        Gets the purpose of this Design.


        :return: The purpose of this Design.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this Design.


        :param purpose: The purpose of this Design.
        :type: str
        """
        allowed_values = ["none", "printOrder"]
        if purpose not in allowed_values:
            raise ValueError(
                "Invalid value for `purpose` ({0}), must be one of {1}"
                .format(purpose, allowed_values)
            )

        self._purpose = purpose

    @property
    def status(self):
        """
        Gets the status of this Design.


        :return: The status of this Design.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Design.


        :param status: The status of this Design.
        :type: str
        """
        allowed_values = ["pendingAction", "pendingApproval", "approved", "rejected"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def form_data(self):
        """
        Gets the form_data of this Design.


        :return: The form_data of this Design.
        :rtype: list[object]
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        """
        Sets the form_data of this Design.


        :param form_data: The form_data of this Design.
        :type: list[object]
        """

        self._form_data = form_data

    @property
    def high_res_pdf_url(self):
        """
        Gets the high_res_pdf_url of this Design.


        :return: The high_res_pdf_url of this Design.
        :rtype: str
        """
        return self._high_res_pdf_url

    @high_res_pdf_url.setter
    def high_res_pdf_url(self, high_res_pdf_url):
        """
        Sets the high_res_pdf_url of this Design.


        :param high_res_pdf_url: The high_res_pdf_url of this Design.
        :type: str
        """

        self._high_res_pdf_url = high_res_pdf_url

    @property
    def proof_pdf_url(self):
        """
        Gets the proof_pdf_url of this Design.


        :return: The proof_pdf_url of this Design.
        :rtype: str
        """
        return self._proof_pdf_url

    @proof_pdf_url.setter
    def proof_pdf_url(self, proof_pdf_url):
        """
        Sets the proof_pdf_url of this Design.


        :param proof_pdf_url: The proof_pdf_url of this Design.
        :type: str
        """

        self._proof_pdf_url = proof_pdf_url

    @property
    def jpegs_url(self):
        """
        Gets the jpegs_url of this Design.


        :return: The jpegs_url of this Design.
        :rtype: str
        """
        return self._jpegs_url

    @jpegs_url.setter
    def jpegs_url(self, jpegs_url):
        """
        Sets the jpegs_url of this Design.


        :param jpegs_url: The jpegs_url of this Design.
        :type: str
        """

        self._jpegs_url = jpegs_url

    @property
    def edited(self):
        """
        Gets the edited of this Design.


        :return: The edited of this Design.
        :rtype: datetime
        """
        return self._edited

    @edited.setter
    def edited(self, edited):
        """
        Sets the edited of this Design.


        :param edited: The edited of this Design.
        :type: datetime
        """

        self._edited = edited

    @property
    def expired(self):
        """
        Gets the expired of this Design.


        :return: The expired of this Design.
        :rtype: datetime
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """
        Sets the expired of this Design.


        :param expired: The expired of this Design.
        :type: datetime
        """

        self._expired = expired

    @property
    def path(self):
        """
        Gets the path of this Design.


        :return: The path of this Design.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Design.


        :param path: The path of this Design.
        :type: str
        """

        self._path = path

    @property
    def sent_for_approval(self):
        """
        Gets the sent_for_approval of this Design.


        :return: The sent_for_approval of this Design.
        :rtype: datetime
        """
        return self._sent_for_approval

    @sent_for_approval.setter
    def sent_for_approval(self, sent_for_approval):
        """
        Sets the sent_for_approval of this Design.


        :param sent_for_approval: The sent_for_approval of this Design.
        :type: datetime
        """

        self._sent_for_approval = sent_for_approval

    @property
    def approved(self):
        """
        Gets the approved of this Design.


        :return: The approved of this Design.
        :rtype: datetime
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """
        Sets the approved of this Design.


        :param approved: The approved of this Design.
        :type: datetime
        """

        self._approved = approved

    @property
    def shared(self):
        """
        Gets the shared of this Design.


        :return: The shared of this Design.
        :rtype: datetime
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this Design.


        :param shared: The shared of this Design.
        :type: datetime
        """

        self._shared = shared

    @property
    def created(self):
        """
        Gets the created of this Design.


        :return: The created of this Design.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Design.


        :param created: The created of this Design.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Design.


        :return: The modified of this Design.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Design.


        :param modified: The modified of this Design.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Design.


        :return: The id of this Design.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Design.


        :param id: The id of this Design.
        :type: str
        """

        self._id = id

    @property
    def dynamic_data_id(self):
        """
        Gets the dynamic_data_id of this Design.


        :return: The dynamic_data_id of this Design.
        :rtype: str
        """
        return self._dynamic_data_id

    @dynamic_data_id.setter
    def dynamic_data_id(self, dynamic_data_id):
        """
        Sets the dynamic_data_id of this Design.


        :param dynamic_data_id: The dynamic_data_id of this Design.
        :type: str
        """

        self._dynamic_data_id = dynamic_data_id

    @property
    def team_id(self):
        """
        Gets the team_id of this Design.


        :return: The team_id of this Design.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this Design.


        :param team_id: The team_id of this Design.
        :type: str
        """

        self._team_id = team_id

    @property
    def requester_id(self):
        """
        Gets the requester_id of this Design.


        :return: The requester_id of this Design.
        :rtype: str
        """
        return self._requester_id

    @requester_id.setter
    def requester_id(self, requester_id):
        """
        Sets the requester_id of this Design.


        :param requester_id: The requester_id of this Design.
        :type: str
        """

        self._requester_id = requester_id

    @property
    def assignee_id(self):
        """
        Gets the assignee_id of this Design.


        :return: The assignee_id of this Design.
        :rtype: str
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        """
        Sets the assignee_id of this Design.


        :param assignee_id: The assignee_id of this Design.
        :type: str
        """

        self._assignee_id = assignee_id

    @property
    def reviewer_id(self):
        """
        Gets the reviewer_id of this Design.


        :return: The reviewer_id of this Design.
        :rtype: str
        """
        return self._reviewer_id

    @reviewer_id.setter
    def reviewer_id(self, reviewer_id):
        """
        Sets the reviewer_id of this Design.


        :param reviewer_id: The reviewer_id of this Design.
        :type: str
        """

        self._reviewer_id = reviewer_id

    @property
    def template_id(self):
        """
        Gets the template_id of this Design.


        :return: The template_id of this Design.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this Design.


        :param template_id: The template_id of this Design.
        :type: str
        """

        self._template_id = template_id

    @property
    def portal_id(self):
        """
        Gets the portal_id of this Design.


        :return: The portal_id of this Design.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this Design.


        :param portal_id: The portal_id of this Design.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def rejection_comment_id(self):
        """
        Gets the rejection_comment_id of this Design.


        :return: The rejection_comment_id of this Design.
        :rtype: str
        """
        return self._rejection_comment_id

    @rejection_comment_id.setter
    def rejection_comment_id(self, rejection_comment_id):
        """
        Sets the rejection_comment_id of this Design.


        :param rejection_comment_id: The rejection_comment_id of this Design.
        :type: str
        """

        self._rejection_comment_id = rejection_comment_id

    @property
    def folder_id(self):
        """
        Gets the folder_id of this Design.


        :return: The folder_id of this Design.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this Design.


        :param folder_id: The folder_id of this Design.
        :type: str
        """

        self._folder_id = folder_id

    @property
    def tags(self):
        """
        Gets the tags of this Design.


        :return: The tags of this Design.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Design.


        :param tags: The tags of this Design.
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def template(self):
        """
        Gets the template of this Design.


        :return: The template of this Design.
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this Design.


        :param template: The template of this Design.
        :type: Template
        """

        self._template = template

    @property
    def portal(self):
        """
        Gets the portal of this Design.


        :return: The portal of this Design.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this Design.


        :param portal: The portal of this Design.
        :type: Portal
        """

        self._portal = portal

    @property
    def team(self):
        """
        Gets the team of this Design.


        :return: The team of this Design.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Design.


        :param team: The team of this Design.
        :type: Team
        """

        self._team = team

    @property
    def comments(self):
        """
        Gets the comments of this Design.


        :return: The comments of this Design.
        :rtype: list[DesignComment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Design.


        :param comments: The comments of this Design.
        :type: list[DesignComment]
        """

        self._comments = comments

    @property
    def rejection_comment(self):
        """
        Gets the rejection_comment of this Design.


        :return: The rejection_comment of this Design.
        :rtype: DesignComment
        """
        return self._rejection_comment

    @rejection_comment.setter
    def rejection_comment(self, rejection_comment):
        """
        Sets the rejection_comment of this Design.


        :param rejection_comment: The rejection_comment of this Design.
        :type: DesignComment
        """

        self._rejection_comment = rejection_comment

    @property
    def exports(self):
        """
        Gets the exports of this Design.


        :return: The exports of this Design.
        :rtype: list[DesignExport]
        """
        return self._exports

    @exports.setter
    def exports(self, exports):
        """
        Sets the exports of this Design.


        :param exports: The exports of this Design.
        :type: list[DesignExport]
        """

        self._exports = exports

    @property
    def requester(self):
        """
        Gets the requester of this Design.


        :return: The requester of this Design.
        :rtype: TeamMember
        """
        return self._requester

    @requester.setter
    def requester(self, requester):
        """
        Sets the requester of this Design.


        :param requester: The requester of this Design.
        :type: TeamMember
        """

        self._requester = requester

    @property
    def assignee(self):
        """
        Gets the assignee of this Design.


        :return: The assignee of this Design.
        :rtype: TeamMember
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """
        Sets the assignee of this Design.


        :param assignee: The assignee of this Design.
        :type: TeamMember
        """

        self._assignee = assignee

    @property
    def reviewer(self):
        """
        Gets the reviewer of this Design.


        :return: The reviewer of this Design.
        :rtype: TeamMember
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        """
        Sets the reviewer of this Design.


        :param reviewer: The reviewer of this Design.
        :type: TeamMember
        """

        self._reviewer = reviewer

    @property
    def commenters(self):
        """
        Gets the commenters of this Design.


        :return: The commenters of this Design.
        :rtype: list[TeamMember]
        """
        return self._commenters

    @commenters.setter
    def commenters(self, commenters):
        """
        Sets the commenters of this Design.


        :param commenters: The commenters of this Design.
        :type: list[TeamMember]
        """

        self._commenters = commenters

    @property
    def folder(self):
        """
        Gets the folder of this Design.


        :return: The folder of this Design.
        :rtype: DesignFolder
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder of this Design.


        :param folder: The folder of this Design.
        :type: DesignFolder
        """

        self._folder = folder

    @property
    def permission(self):
        """
        Gets the permission of this Design.


        :return: The permission of this Design.
        :rtype: DesignPermissionSet
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """
        Sets the permission of this Design.


        :param permission: The permission of this Design.
        :type: DesignPermissionSet
        """

        self._permission = permission

    @property
    def members(self):
        """
        Gets the members of this Design.


        :return: The members of this Design.
        :rtype: list[TeamMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this Design.


        :param members: The members of this Design.
        :type: list[TeamMember]
        """

        self._members = members

    @property
    def design_members(self):
        """
        Gets the design_members of this Design.


        :return: The design_members of this Design.
        :rtype: list[DesignMember]
        """
        return self._design_members

    @design_members.setter
    def design_members(self, design_members):
        """
        Sets the design_members of this Design.


        :param design_members: The design_members of this Design.
        :type: list[DesignMember]
        """

        self._design_members = design_members

    @property
    def dynamic_data(self):
        """
        Gets the dynamic_data of this Design.


        :return: The dynamic_data of this Design.
        :rtype: DynamicData
        """
        return self._dynamic_data

    @dynamic_data.setter
    def dynamic_data(self, dynamic_data):
        """
        Sets the dynamic_data of this Design.


        :param dynamic_data: The dynamic_data of this Design.
        :type: DynamicData
        """

        self._dynamic_data = dynamic_data

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
