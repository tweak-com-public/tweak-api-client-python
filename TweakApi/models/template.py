# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.1-beta.1
    
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


class Template(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, thumbnail=None, object=None, description='', edited=None, path='/', status=None, shared=None, permission_set_updated=None, created=None, modified=None, id=None, team_id=None, uploader_id=None, team_folder_id=None, workflow_id=None, portals=None, team=None, members=None, template_members=None, permission=None, designs=None, tags=None, team_folder=None, portal_folders=None, workflow=None, uploader=None):
        """
        Template - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'thumbnail': 'str',
            'object': 'object',
            'description': 'str',
            'edited': 'datetime',
            'path': 'str',
            'status': 'str',
            'shared': 'datetime',
            'permission_set_updated': 'datetime',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'uploader_id': 'str',
            'team_folder_id': 'str',
            'workflow_id': 'str',
            'portals': 'list[Portal]',
            'team': 'Team',
            'members': 'list[TeamMember]',
            'template_members': 'list[TemplateMember]',
            'permission': 'TemplatePermissionSet',
            'designs': 'list[Design]',
            'tags': 'list[Tag]',
            'team_folder': 'TeamTemplateFolder',
            'portal_folders': 'list[PortalTemplateFolder]',
            'workflow': 'Workflow',
            'uploader': 'TeamMember'
        }

        self.attribute_map = {
            'name': 'name',
            'thumbnail': 'thumbnail',
            'object': 'object',
            'description': 'description',
            'edited': 'edited',
            'path': 'path',
            'status': 'status',
            'shared': 'shared',
            'permission_set_updated': 'permissionSetUpdated',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'uploader_id': 'uploaderId',
            'team_folder_id': 'teamFolderId',
            'workflow_id': 'workflowId',
            'portals': 'portals',
            'team': 'team',
            'members': 'members',
            'template_members': 'templateMembers',
            'permission': 'permission',
            'designs': 'designs',
            'tags': 'tags',
            'team_folder': 'teamFolder',
            'portal_folders': 'portalFolders',
            'workflow': 'workflow',
            'uploader': 'uploader'
        }

        self._name = name
        self._thumbnail = thumbnail
        self._object = object
        self._description = description
        self._edited = edited
        self._path = path
        self._status = status
        self._shared = shared
        self._permission_set_updated = permission_set_updated
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._uploader_id = uploader_id
        self._team_folder_id = team_folder_id
        self._workflow_id = workflow_id
        self._portals = portals
        self._team = team
        self._members = members
        self._template_members = template_members
        self._permission = permission
        self._designs = designs
        self._tags = tags
        self._team_folder = team_folder
        self._portal_folders = portal_folders
        self._workflow = workflow
        self._uploader = uploader


    @property
    def name(self):
        """
        Gets the name of this Template.


        :return: The name of this Template.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Template.


        :param name: The name of this Template.
        :type: str
        """

        self._name = name

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this Template.


        :return: The thumbnail of this Template.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this Template.


        :param thumbnail: The thumbnail of this Template.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def object(self):
        """
        Gets the object of this Template.


        :return: The object of this Template.
        :rtype: object
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this Template.


        :param object: The object of this Template.
        :type: object
        """

        self._object = object

    @property
    def description(self):
        """
        Gets the description of this Template.


        :return: The description of this Template.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Template.


        :param description: The description of this Template.
        :type: str
        """

        self._description = description

    @property
    def edited(self):
        """
        Gets the edited of this Template.


        :return: The edited of this Template.
        :rtype: datetime
        """
        return self._edited

    @edited.setter
    def edited(self, edited):
        """
        Sets the edited of this Template.


        :param edited: The edited of this Template.
        :type: datetime
        """

        self._edited = edited

    @property
    def path(self):
        """
        Gets the path of this Template.


        :return: The path of this Template.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Template.


        :param path: The path of this Template.
        :type: str
        """

        self._path = path

    @property
    def status(self):
        """
        Gets the status of this Template.


        :return: The status of this Template.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Template.


        :param status: The status of this Template.
        :type: str
        """
        allowed_values = ["pendingApproval", "approved", "rejected"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def shared(self):
        """
        Gets the shared of this Template.


        :return: The shared of this Template.
        :rtype: datetime
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this Template.


        :param shared: The shared of this Template.
        :type: datetime
        """

        self._shared = shared

    @property
    def permission_set_updated(self):
        """
        Gets the permission_set_updated of this Template.


        :return: The permission_set_updated of this Template.
        :rtype: datetime
        """
        return self._permission_set_updated

    @permission_set_updated.setter
    def permission_set_updated(self, permission_set_updated):
        """
        Sets the permission_set_updated of this Template.


        :param permission_set_updated: The permission_set_updated of this Template.
        :type: datetime
        """

        self._permission_set_updated = permission_set_updated

    @property
    def created(self):
        """
        Gets the created of this Template.


        :return: The created of this Template.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Template.


        :param created: The created of this Template.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Template.


        :return: The modified of this Template.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Template.


        :param modified: The modified of this Template.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Template.


        :return: The id of this Template.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Template.


        :param id: The id of this Template.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this Template.


        :return: The team_id of this Template.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this Template.


        :param team_id: The team_id of this Template.
        :type: str
        """

        self._team_id = team_id

    @property
    def uploader_id(self):
        """
        Gets the uploader_id of this Template.


        :return: The uploader_id of this Template.
        :rtype: str
        """
        return self._uploader_id

    @uploader_id.setter
    def uploader_id(self, uploader_id):
        """
        Sets the uploader_id of this Template.


        :param uploader_id: The uploader_id of this Template.
        :type: str
        """

        self._uploader_id = uploader_id

    @property
    def team_folder_id(self):
        """
        Gets the team_folder_id of this Template.


        :return: The team_folder_id of this Template.
        :rtype: str
        """
        return self._team_folder_id

    @team_folder_id.setter
    def team_folder_id(self, team_folder_id):
        """
        Sets the team_folder_id of this Template.


        :param team_folder_id: The team_folder_id of this Template.
        :type: str
        """

        self._team_folder_id = team_folder_id

    @property
    def workflow_id(self):
        """
        Gets the workflow_id of this Template.


        :return: The workflow_id of this Template.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """
        Sets the workflow_id of this Template.


        :param workflow_id: The workflow_id of this Template.
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def portals(self):
        """
        Gets the portals of this Template.


        :return: The portals of this Template.
        :rtype: list[Portal]
        """
        return self._portals

    @portals.setter
    def portals(self, portals):
        """
        Sets the portals of this Template.


        :param portals: The portals of this Template.
        :type: list[Portal]
        """

        self._portals = portals

    @property
    def team(self):
        """
        Gets the team of this Template.


        :return: The team of this Template.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Template.


        :param team: The team of this Template.
        :type: Team
        """

        self._team = team

    @property
    def members(self):
        """
        Gets the members of this Template.


        :return: The members of this Template.
        :rtype: list[TeamMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this Template.


        :param members: The members of this Template.
        :type: list[TeamMember]
        """

        self._members = members

    @property
    def template_members(self):
        """
        Gets the template_members of this Template.


        :return: The template_members of this Template.
        :rtype: list[TemplateMember]
        """
        return self._template_members

    @template_members.setter
    def template_members(self, template_members):
        """
        Sets the template_members of this Template.


        :param template_members: The template_members of this Template.
        :type: list[TemplateMember]
        """

        self._template_members = template_members

    @property
    def permission(self):
        """
        Gets the permission of this Template.


        :return: The permission of this Template.
        :rtype: TemplatePermissionSet
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """
        Sets the permission of this Template.


        :param permission: The permission of this Template.
        :type: TemplatePermissionSet
        """

        self._permission = permission

    @property
    def designs(self):
        """
        Gets the designs of this Template.


        :return: The designs of this Template.
        :rtype: list[Design]
        """
        return self._designs

    @designs.setter
    def designs(self, designs):
        """
        Sets the designs of this Template.


        :param designs: The designs of this Template.
        :type: list[Design]
        """

        self._designs = designs

    @property
    def tags(self):
        """
        Gets the tags of this Template.


        :return: The tags of this Template.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Template.


        :param tags: The tags of this Template.
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def team_folder(self):
        """
        Gets the team_folder of this Template.


        :return: The team_folder of this Template.
        :rtype: TeamTemplateFolder
        """
        return self._team_folder

    @team_folder.setter
    def team_folder(self, team_folder):
        """
        Sets the team_folder of this Template.


        :param team_folder: The team_folder of this Template.
        :type: TeamTemplateFolder
        """

        self._team_folder = team_folder

    @property
    def portal_folders(self):
        """
        Gets the portal_folders of this Template.


        :return: The portal_folders of this Template.
        :rtype: list[PortalTemplateFolder]
        """
        return self._portal_folders

    @portal_folders.setter
    def portal_folders(self, portal_folders):
        """
        Sets the portal_folders of this Template.


        :param portal_folders: The portal_folders of this Template.
        :type: list[PortalTemplateFolder]
        """

        self._portal_folders = portal_folders

    @property
    def workflow(self):
        """
        Gets the workflow of this Template.


        :return: The workflow of this Template.
        :rtype: Workflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """
        Sets the workflow of this Template.


        :param workflow: The workflow of this Template.
        :type: Workflow
        """

        self._workflow = workflow

    @property
    def uploader(self):
        """
        Gets the uploader of this Template.


        :return: The uploader of this Template.
        :rtype: TeamMember
        """
        return self._uploader

    @uploader.setter
    def uploader(self, uploader):
        """
        Sets the uploader of this Template.


        :param uploader: The uploader of this Template.
        :type: TeamMember
        """

        self._uploader = uploader

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
