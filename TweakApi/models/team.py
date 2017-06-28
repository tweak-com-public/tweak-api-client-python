# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 0.0.1
    
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


class Team(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, logo=None, subdomain=None, created=None, modified=None, id=None, icon=None, client_key=None, java_script_key=None, rest_api_key=None, windows_key=None, master_key=None, status='sandbox', members=None, team_members=None, portals=None, templates=None, brand=None, template_folders=None, workflows=None, images=None, image_folders=None):
        """
        Team - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'logo': 'object',
            'subdomain': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'icon': 'str',
            'client_key': 'str',
            'java_script_key': 'str',
            'rest_api_key': 'str',
            'windows_key': 'str',
            'master_key': 'str',
            'status': 'str',
            'members': 'list[Customer]',
            'team_members': 'list[TeamMember]',
            'portals': 'list[Portal]',
            'templates': 'list[Template]',
            'brand': 'TeamBrand',
            'template_folders': 'list[TeamTemplateFolder]',
            'workflows': 'list[Workflow]',
            'images': 'list[Image]',
            'image_folders': 'list[ImageFolder]'
        }

        self.attribute_map = {
            'name': 'name',
            'logo': 'logo',
            'subdomain': 'subdomain',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'icon': 'icon',
            'client_key': 'clientKey',
            'java_script_key': 'javaScriptKey',
            'rest_api_key': 'restApiKey',
            'windows_key': 'windowsKey',
            'master_key': 'masterKey',
            'status': 'status',
            'members': 'members',
            'team_members': 'teamMembers',
            'portals': 'portals',
            'templates': 'templates',
            'brand': 'brand',
            'template_folders': 'templateFolders',
            'workflows': 'workflows',
            'images': 'images',
            'image_folders': 'imageFolders'
        }

        self._name = name
        self._logo = logo
        self._subdomain = subdomain
        self._created = created
        self._modified = modified
        self._id = id
        self._icon = icon
        self._client_key = client_key
        self._java_script_key = java_script_key
        self._rest_api_key = rest_api_key
        self._windows_key = windows_key
        self._master_key = master_key
        self._status = status
        self._members = members
        self._team_members = team_members
        self._portals = portals
        self._templates = templates
        self._brand = brand
        self._template_folders = template_folders
        self._workflows = workflows
        self._images = images
        self._image_folders = image_folders


    @property
    def name(self):
        """
        Gets the name of this Team.


        :return: The name of this Team.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Team.


        :param name: The name of this Team.
        :type: str
        """

        self._name = name

    @property
    def logo(self):
        """
        Gets the logo of this Team.


        :return: The logo of this Team.
        :rtype: object
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this Team.


        :param logo: The logo of this Team.
        :type: object
        """

        self._logo = logo

    @property
    def subdomain(self):
        """
        Gets the subdomain of this Team.


        :return: The subdomain of this Team.
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """
        Sets the subdomain of this Team.


        :param subdomain: The subdomain of this Team.
        :type: str
        """

        self._subdomain = subdomain

    @property
    def created(self):
        """
        Gets the created of this Team.


        :return: The created of this Team.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Team.


        :param created: The created of this Team.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Team.


        :return: The modified of this Team.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Team.


        :param modified: The modified of this Team.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Team.


        :return: The id of this Team.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Team.


        :param id: The id of this Team.
        :type: str
        """

        self._id = id

    @property
    def icon(self):
        """
        Gets the icon of this Team.
        The icon image url

        :return: The icon of this Team.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this Team.
        The icon image url

        :param icon: The icon of this Team.
        :type: str
        """

        self._icon = icon

    @property
    def client_key(self):
        """
        Gets the client_key of this Team.


        :return: The client_key of this Team.
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """
        Sets the client_key of this Team.


        :param client_key: The client_key of this Team.
        :type: str
        """

        self._client_key = client_key

    @property
    def java_script_key(self):
        """
        Gets the java_script_key of this Team.


        :return: The java_script_key of this Team.
        :rtype: str
        """
        return self._java_script_key

    @java_script_key.setter
    def java_script_key(self, java_script_key):
        """
        Sets the java_script_key of this Team.


        :param java_script_key: The java_script_key of this Team.
        :type: str
        """

        self._java_script_key = java_script_key

    @property
    def rest_api_key(self):
        """
        Gets the rest_api_key of this Team.


        :return: The rest_api_key of this Team.
        :rtype: str
        """
        return self._rest_api_key

    @rest_api_key.setter
    def rest_api_key(self, rest_api_key):
        """
        Sets the rest_api_key of this Team.


        :param rest_api_key: The rest_api_key of this Team.
        :type: str
        """

        self._rest_api_key = rest_api_key

    @property
    def windows_key(self):
        """
        Gets the windows_key of this Team.


        :return: The windows_key of this Team.
        :rtype: str
        """
        return self._windows_key

    @windows_key.setter
    def windows_key(self, windows_key):
        """
        Sets the windows_key of this Team.


        :param windows_key: The windows_key of this Team.
        :type: str
        """

        self._windows_key = windows_key

    @property
    def master_key(self):
        """
        Gets the master_key of this Team.


        :return: The master_key of this Team.
        :rtype: str
        """
        return self._master_key

    @master_key.setter
    def master_key(self, master_key):
        """
        Sets the master_key of this Team.


        :param master_key: The master_key of this Team.
        :type: str
        """

        self._master_key = master_key

    @property
    def status(self):
        """
        Gets the status of this Team.
        Status of the application, production/sandbox/disabled

        :return: The status of this Team.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Team.
        Status of the application, production/sandbox/disabled

        :param status: The status of this Team.
        :type: str
        """

        self._status = status

    @property
    def members(self):
        """
        Gets the members of this Team.


        :return: The members of this Team.
        :rtype: list[Customer]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this Team.


        :param members: The members of this Team.
        :type: list[Customer]
        """

        self._members = members

    @property
    def team_members(self):
        """
        Gets the team_members of this Team.


        :return: The team_members of this Team.
        :rtype: list[TeamMember]
        """
        return self._team_members

    @team_members.setter
    def team_members(self, team_members):
        """
        Sets the team_members of this Team.


        :param team_members: The team_members of this Team.
        :type: list[TeamMember]
        """

        self._team_members = team_members

    @property
    def portals(self):
        """
        Gets the portals of this Team.


        :return: The portals of this Team.
        :rtype: list[Portal]
        """
        return self._portals

    @portals.setter
    def portals(self, portals):
        """
        Sets the portals of this Team.


        :param portals: The portals of this Team.
        :type: list[Portal]
        """

        self._portals = portals

    @property
    def templates(self):
        """
        Gets the templates of this Team.


        :return: The templates of this Team.
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this Team.


        :param templates: The templates of this Team.
        :type: list[Template]
        """

        self._templates = templates

    @property
    def brand(self):
        """
        Gets the brand of this Team.


        :return: The brand of this Team.
        :rtype: TeamBrand
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """
        Sets the brand of this Team.


        :param brand: The brand of this Team.
        :type: TeamBrand
        """

        self._brand = brand

    @property
    def template_folders(self):
        """
        Gets the template_folders of this Team.


        :return: The template_folders of this Team.
        :rtype: list[TeamTemplateFolder]
        """
        return self._template_folders

    @template_folders.setter
    def template_folders(self, template_folders):
        """
        Sets the template_folders of this Team.


        :param template_folders: The template_folders of this Team.
        :type: list[TeamTemplateFolder]
        """

        self._template_folders = template_folders

    @property
    def workflows(self):
        """
        Gets the workflows of this Team.


        :return: The workflows of this Team.
        :rtype: list[Workflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this Team.


        :param workflows: The workflows of this Team.
        :type: list[Workflow]
        """

        self._workflows = workflows

    @property
    def images(self):
        """
        Gets the images of this Team.


        :return: The images of this Team.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Team.


        :param images: The images of this Team.
        :type: list[Image]
        """

        self._images = images

    @property
    def image_folders(self):
        """
        Gets the image_folders of this Team.


        :return: The image_folders of this Team.
        :rtype: list[ImageFolder]
        """
        return self._image_folders

    @image_folders.setter
    def image_folders(self, image_folders):
        """
        Sets the image_folders of this Team.


        :param image_folders: The image_folders of this Team.
        :type: list[ImageFolder]
        """

        self._image_folders = image_folders

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
