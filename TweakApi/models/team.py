# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.7-alpha.2
    
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
    def __init__(self, name=None, logo=None, subdomain=None, country='Ireland', created=None, modified=None, id=None, icon=None, client_key=None, java_script_key=None, rest_api_key=None, windows_key=None, master_key=None, status='sandbox', team_data_id=None, members=None, builder_configs=None, data_sources=None, dynamic_datas=None, team_members=None, portals=None, templates=None, brand=None, template_folders=None, workflows=None, images=None, image_folders=None, billing=None, permission=None, product_materials=None, product_size_materials=None, product_pdf_color_profiles=None, team_data=None):
        """
        Team - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'logo': 'CloudinaryImage',
            'subdomain': 'str',
            'country': 'str',
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
            'team_data_id': 'str',
            'members': 'list[Customer]',
            'builder_configs': 'list[TeamBuilderConfig]',
            'data_sources': 'list[DataSource]',
            'dynamic_datas': 'list[DynamicData]',
            'team_members': 'list[TeamMember]',
            'portals': 'list[Portal]',
            'templates': 'list[Template]',
            'brand': 'TeamBrand',
            'template_folders': 'list[TeamTemplateFolder]',
            'workflows': 'list[Workflow]',
            'images': 'list[Image]',
            'image_folders': 'list[ImageFolder]',
            'billing': 'Billing',
            'permission': 'TeamPermissionSet',
            'product_materials': 'list[ProductMaterial]',
            'product_size_materials': 'list[ProductSizeMaterial]',
            'product_pdf_color_profiles': 'list[ProductPdfColorProfile]',
            'team_data': 'DynamicData'
        }

        self.attribute_map = {
            'name': 'name',
            'logo': 'logo',
            'subdomain': 'subdomain',
            'country': 'country',
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
            'team_data_id': 'teamDataId',
            'members': 'members',
            'builder_configs': 'builderConfigs',
            'data_sources': 'dataSources',
            'dynamic_datas': 'dynamicDatas',
            'team_members': 'teamMembers',
            'portals': 'portals',
            'templates': 'templates',
            'brand': 'brand',
            'template_folders': 'templateFolders',
            'workflows': 'workflows',
            'images': 'images',
            'image_folders': 'imageFolders',
            'billing': 'billing',
            'permission': 'permission',
            'product_materials': 'productMaterials',
            'product_size_materials': 'productSizeMaterials',
            'product_pdf_color_profiles': 'productPdfColorProfiles',
            'team_data': 'teamData'
        }

        self._name = name
        self._logo = logo
        self._subdomain = subdomain
        self._country = country
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
        self._team_data_id = team_data_id
        self._members = members
        self._builder_configs = builder_configs
        self._data_sources = data_sources
        self._dynamic_datas = dynamic_datas
        self._team_members = team_members
        self._portals = portals
        self._templates = templates
        self._brand = brand
        self._template_folders = template_folders
        self._workflows = workflows
        self._images = images
        self._image_folders = image_folders
        self._billing = billing
        self._permission = permission
        self._product_materials = product_materials
        self._product_size_materials = product_size_materials
        self._product_pdf_color_profiles = product_pdf_color_profiles
        self._team_data = team_data


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
        :rtype: CloudinaryImage
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this Team.


        :param logo: The logo of this Team.
        :type: CloudinaryImage
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
    def country(self):
        """
        Gets the country of this Team.


        :return: The country of this Team.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Team.


        :param country: The country of this Team.
        :type: str
        """

        self._country = country

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
    def team_data_id(self):
        """
        Gets the team_data_id of this Team.


        :return: The team_data_id of this Team.
        :rtype: str
        """
        return self._team_data_id

    @team_data_id.setter
    def team_data_id(self, team_data_id):
        """
        Sets the team_data_id of this Team.


        :param team_data_id: The team_data_id of this Team.
        :type: str
        """

        self._team_data_id = team_data_id

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
    def builder_configs(self):
        """
        Gets the builder_configs of this Team.


        :return: The builder_configs of this Team.
        :rtype: list[TeamBuilderConfig]
        """
        return self._builder_configs

    @builder_configs.setter
    def builder_configs(self, builder_configs):
        """
        Sets the builder_configs of this Team.


        :param builder_configs: The builder_configs of this Team.
        :type: list[TeamBuilderConfig]
        """

        self._builder_configs = builder_configs

    @property
    def data_sources(self):
        """
        Gets the data_sources of this Team.


        :return: The data_sources of this Team.
        :rtype: list[DataSource]
        """
        return self._data_sources

    @data_sources.setter
    def data_sources(self, data_sources):
        """
        Sets the data_sources of this Team.


        :param data_sources: The data_sources of this Team.
        :type: list[DataSource]
        """

        self._data_sources = data_sources

    @property
    def dynamic_datas(self):
        """
        Gets the dynamic_datas of this Team.


        :return: The dynamic_datas of this Team.
        :rtype: list[DynamicData]
        """
        return self._dynamic_datas

    @dynamic_datas.setter
    def dynamic_datas(self, dynamic_datas):
        """
        Sets the dynamic_datas of this Team.


        :param dynamic_datas: The dynamic_datas of this Team.
        :type: list[DynamicData]
        """

        self._dynamic_datas = dynamic_datas

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

    @property
    def billing(self):
        """
        Gets the billing of this Team.


        :return: The billing of this Team.
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """
        Sets the billing of this Team.


        :param billing: The billing of this Team.
        :type: Billing
        """

        self._billing = billing

    @property
    def permission(self):
        """
        Gets the permission of this Team.


        :return: The permission of this Team.
        :rtype: TeamPermissionSet
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """
        Sets the permission of this Team.


        :param permission: The permission of this Team.
        :type: TeamPermissionSet
        """

        self._permission = permission

    @property
    def product_materials(self):
        """
        Gets the product_materials of this Team.


        :return: The product_materials of this Team.
        :rtype: list[ProductMaterial]
        """
        return self._product_materials

    @product_materials.setter
    def product_materials(self, product_materials):
        """
        Sets the product_materials of this Team.


        :param product_materials: The product_materials of this Team.
        :type: list[ProductMaterial]
        """

        self._product_materials = product_materials

    @property
    def product_size_materials(self):
        """
        Gets the product_size_materials of this Team.


        :return: The product_size_materials of this Team.
        :rtype: list[ProductSizeMaterial]
        """
        return self._product_size_materials

    @product_size_materials.setter
    def product_size_materials(self, product_size_materials):
        """
        Sets the product_size_materials of this Team.


        :param product_size_materials: The product_size_materials of this Team.
        :type: list[ProductSizeMaterial]
        """

        self._product_size_materials = product_size_materials

    @property
    def product_pdf_color_profiles(self):
        """
        Gets the product_pdf_color_profiles of this Team.


        :return: The product_pdf_color_profiles of this Team.
        :rtype: list[ProductPdfColorProfile]
        """
        return self._product_pdf_color_profiles

    @product_pdf_color_profiles.setter
    def product_pdf_color_profiles(self, product_pdf_color_profiles):
        """
        Sets the product_pdf_color_profiles of this Team.


        :param product_pdf_color_profiles: The product_pdf_color_profiles of this Team.
        :type: list[ProductPdfColorProfile]
        """

        self._product_pdf_color_profiles = product_pdf_color_profiles

    @property
    def team_data(self):
        """
        Gets the team_data of this Team.


        :return: The team_data of this Team.
        :rtype: DynamicData
        """
        return self._team_data

    @team_data.setter
    def team_data(self, team_data):
        """
        Sets the team_data of this Team.


        :param team_data: The team_data of this Team.
        :type: DynamicData
        """

        self._team_data = team_data

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
