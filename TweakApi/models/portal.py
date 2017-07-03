# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 0.0.3
    
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


class Portal(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, logo=None, status=None, language=None, created=None, modified=None, id=None, team_id=None, templates=None, template_rels=None, members=None, portal_members=None, team=None, designs=None, template_folders=None, design_folders=None, image_folders=None):
        """
        Portal - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'logo': 'object',
            'status': 'str',
            'language': 'str',
            'created': 'datetime',
            'modified': 'datetime',
            'id': 'str',
            'team_id': 'str',
            'templates': 'list[Template]',
            'template_rels': 'list[PortalTemplate]',
            'members': 'list[TeamMember]',
            'portal_members': 'list[PortalMember]',
            'team': 'Team',
            'designs': 'list[Design]',
            'template_folders': 'list[PortalTemplateFolder]',
            'design_folders': 'list[DesignFolder]',
            'image_folders': 'list[ImageFolder]'
        }

        self.attribute_map = {
            'name': 'name',
            'logo': 'logo',
            'status': 'status',
            'language': 'language',
            'created': 'created',
            'modified': 'modified',
            'id': 'id',
            'team_id': 'teamId',
            'templates': 'templates',
            'template_rels': 'templateRels',
            'members': 'members',
            'portal_members': 'portalMembers',
            'team': 'team',
            'designs': 'designs',
            'template_folders': 'templateFolders',
            'design_folders': 'designFolders',
            'image_folders': 'imageFolders'
        }

        self._name = name
        self._logo = logo
        self._status = status
        self._language = language
        self._created = created
        self._modified = modified
        self._id = id
        self._team_id = team_id
        self._templates = templates
        self._template_rels = template_rels
        self._members = members
        self._portal_members = portal_members
        self._team = team
        self._designs = designs
        self._template_folders = template_folders
        self._design_folders = design_folders
        self._image_folders = image_folders


    @property
    def name(self):
        """
        Gets the name of this Portal.


        :return: The name of this Portal.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Portal.


        :param name: The name of this Portal.
        :type: str
        """

        self._name = name

    @property
    def logo(self):
        """
        Gets the logo of this Portal.


        :return: The logo of this Portal.
        :rtype: object
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this Portal.


        :param logo: The logo of this Portal.
        :type: object
        """

        self._logo = logo

    @property
    def status(self):
        """
        Gets the status of this Portal.


        :return: The status of this Portal.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Portal.


        :param status: The status of this Portal.
        :type: str
        """
        allowed_values = ["private", "public"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def language(self):
        """
        Gets the language of this Portal.


        :return: The language of this Portal.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Portal.


        :param language: The language of this Portal.
        :type: str
        """
        allowed_values = ["sq_AL", "sq", "ar_DZ", "ar_BH", "ar_EG", "ar_IQ", "ar_JO", "ar_KW", "ar_LB", "ar_LY", "ar_MA", "ar_OM", "ar_QA", "ar_SA", "ar_SD", "ar_SY", "ar_TN", "ar_AE", "ar_YE", "ar", "be_BY", "be", "bg_BG", "bg", "ca_ES", "ca", "zh_CN", "zh_HK", "zh_SG", "zh_TW", "zh", "hr_HR", "hr", "cs_CZ", "cs", "da_DK", "da", "nl_BE", "nl_NL", "nl", "en_AU", "en_CA", "en_IN", "en_IE", "en_MT", "en_NZ", "en_PH", "en_SG", "en_ZA", "en_GB", "en_US", "en", "et_EE", "et", "fi_FI", "fi", "fr_BE", "fr_CA", "fr_FR", "fr_LU", "fr_CH", "fr", "de_AT", "de_DE", "de_LU", "de_CH", "de", "el_CY", "el_GR", "el", "iw_IL", "iw", "hi_IN", "hu_HU", "hu", "is_IS", "is", "in_ID", "in", "ga_IE", "ga", "it_IT", "it_CH", "it", "ja_JP", "ja_JP_JP", "ja", "ko_KR", "ko", "lv_LV", "lv", "lt_LT", "lt", "mk_MK", "mk", "ms_MY", "ms", "mt_MT", "mt", "no_NO", "no_NO_NY", "no", "pl_PL", "pl", "pt_BR", "pt_PT", "pt", "ro_RO", "ro", "ru_RU", "ru", "sr_BA", "sr_ME", "sr_CS", "sr_RS", "sr", "sk_SK", "sk", "sl_SI", "sl", "es_AR", "es_BO", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_SV", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PY", "es_PE", "es_PR", "es_ES", "es_US", "es_UY", "es_VE", "es", "sv_SE", "sv", "th_TH", "th_TH_TH", "th", "tr_TR", "tr", "uk_UA", "uk", "vi_VN", "vi"]
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def created(self):
        """
        Gets the created of this Portal.


        :return: The created of this Portal.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Portal.


        :param created: The created of this Portal.
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """
        Gets the modified of this Portal.


        :return: The modified of this Portal.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this Portal.


        :param modified: The modified of this Portal.
        :type: datetime
        """

        self._modified = modified

    @property
    def id(self):
        """
        Gets the id of this Portal.


        :return: The id of this Portal.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Portal.


        :param id: The id of this Portal.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this Portal.


        :return: The team_id of this Portal.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this Portal.


        :param team_id: The team_id of this Portal.
        :type: str
        """

        self._team_id = team_id

    @property
    def templates(self):
        """
        Gets the templates of this Portal.


        :return: The templates of this Portal.
        :rtype: list[Template]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this Portal.


        :param templates: The templates of this Portal.
        :type: list[Template]
        """

        self._templates = templates

    @property
    def template_rels(self):
        """
        Gets the template_rels of this Portal.


        :return: The template_rels of this Portal.
        :rtype: list[PortalTemplate]
        """
        return self._template_rels

    @template_rels.setter
    def template_rels(self, template_rels):
        """
        Sets the template_rels of this Portal.


        :param template_rels: The template_rels of this Portal.
        :type: list[PortalTemplate]
        """

        self._template_rels = template_rels

    @property
    def members(self):
        """
        Gets the members of this Portal.


        :return: The members of this Portal.
        :rtype: list[TeamMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this Portal.


        :param members: The members of this Portal.
        :type: list[TeamMember]
        """

        self._members = members

    @property
    def portal_members(self):
        """
        Gets the portal_members of this Portal.


        :return: The portal_members of this Portal.
        :rtype: list[PortalMember]
        """
        return self._portal_members

    @portal_members.setter
    def portal_members(self, portal_members):
        """
        Sets the portal_members of this Portal.


        :param portal_members: The portal_members of this Portal.
        :type: list[PortalMember]
        """

        self._portal_members = portal_members

    @property
    def team(self):
        """
        Gets the team of this Portal.


        :return: The team of this Portal.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this Portal.


        :param team: The team of this Portal.
        :type: Team
        """

        self._team = team

    @property
    def designs(self):
        """
        Gets the designs of this Portal.


        :return: The designs of this Portal.
        :rtype: list[Design]
        """
        return self._designs

    @designs.setter
    def designs(self, designs):
        """
        Sets the designs of this Portal.


        :param designs: The designs of this Portal.
        :type: list[Design]
        """

        self._designs = designs

    @property
    def template_folders(self):
        """
        Gets the template_folders of this Portal.


        :return: The template_folders of this Portal.
        :rtype: list[PortalTemplateFolder]
        """
        return self._template_folders

    @template_folders.setter
    def template_folders(self, template_folders):
        """
        Sets the template_folders of this Portal.


        :param template_folders: The template_folders of this Portal.
        :type: list[PortalTemplateFolder]
        """

        self._template_folders = template_folders

    @property
    def design_folders(self):
        """
        Gets the design_folders of this Portal.


        :return: The design_folders of this Portal.
        :rtype: list[DesignFolder]
        """
        return self._design_folders

    @design_folders.setter
    def design_folders(self, design_folders):
        """
        Sets the design_folders of this Portal.


        :param design_folders: The design_folders of this Portal.
        :type: list[DesignFolder]
        """

        self._design_folders = design_folders

    @property
    def image_folders(self):
        """
        Gets the image_folders of this Portal.


        :return: The image_folders of this Portal.
        :rtype: list[ImageFolder]
        """
        return self._image_folders

    @image_folders.setter
    def image_folders(self, image_folders):
        """
        Sets the image_folders of this Portal.


        :param image_folders: The image_folders of this Portal.
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
