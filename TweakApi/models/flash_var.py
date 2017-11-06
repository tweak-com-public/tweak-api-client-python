# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.2-alpha.12
    
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


class FlashVar(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_partner_auth_url='', plugin_product_id=None, saved_product_id=None, allow_add_image=False, allow_add_text=False, allow_jpeg=False, allow_low_res_pdf=False, allow_high_res_pdf=False, allow_save_for_later=False, allow_save_as_template=False, allow_duplicate_design=False, block_editing=False, make_all_items_editable=False, show_confirm=False, allow_approve_plugin_product=False, allow_send_to_approve_plugin_product=False, workflow_form=None, design_form_data=None, show_plugin_images=False, plugin_image_libraries=None, is_tweak_template=False, show_item_navigator=False, show_item_counts=False, show_editable_item_toggle=False, id=None, team_id=None, team=None, team_member_id=None, team_member=None, portal_id=None, portal=None, portal_member_id=None, portal_member=None, design_id=None, design=None, template_id=None, template=None):
        """
        FlashVar - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_partner_auth_url': 'str',
            'plugin_product_id': 'str',
            'saved_product_id': 'str',
            'allow_add_image': 'bool',
            'allow_add_text': 'bool',
            'allow_jpeg': 'bool',
            'allow_low_res_pdf': 'bool',
            'allow_high_res_pdf': 'bool',
            'allow_save_for_later': 'bool',
            'allow_save_as_template': 'bool',
            'allow_duplicate_design': 'bool',
            'block_editing': 'bool',
            'make_all_items_editable': 'bool',
            'show_confirm': 'bool',
            'allow_approve_plugin_product': 'bool',
            'allow_send_to_approve_plugin_product': 'bool',
            'workflow_form': 'str',
            'design_form_data': 'list[object]',
            'show_plugin_images': 'bool',
            'plugin_image_libraries': 'list[str]',
            'is_tweak_template': 'bool',
            'show_item_navigator': 'bool',
            'show_item_counts': 'bool',
            'show_editable_item_toggle': 'bool',
            'id': 'str',
            'team_id': 'str',
            'team': 'Team',
            'team_member_id': 'str',
            'team_member': 'TeamMember',
            'portal_id': 'str',
            'portal': 'Portal',
            'portal_member_id': 'str',
            'portal_member': 'PortalMember',
            'design_id': 'str',
            'design': 'Design',
            'template_id': 'str',
            'template': 'Template'
        }

        self.attribute_map = {
            'api_partner_auth_url': 'apiPartnerAuthUrl',
            'plugin_product_id': 'pluginProductId',
            'saved_product_id': 'savedProductId',
            'allow_add_image': 'allowAddImage',
            'allow_add_text': 'allowAddText',
            'allow_jpeg': 'allowJPEG',
            'allow_low_res_pdf': 'allowLowResPDF',
            'allow_high_res_pdf': 'allowHighResPDF',
            'allow_save_for_later': 'allowSaveForLater',
            'allow_save_as_template': 'allowSaveAsTemplate',
            'allow_duplicate_design': 'allowDuplicateDesign',
            'block_editing': 'blockEditing',
            'make_all_items_editable': 'makeAllItemsEditable',
            'show_confirm': 'showConfirm',
            'allow_approve_plugin_product': 'allowApprovePluginProduct',
            'allow_send_to_approve_plugin_product': 'allowSendToApprovePluginProduct',
            'workflow_form': 'workflowForm',
            'design_form_data': 'designFormData',
            'show_plugin_images': 'showPluginImages',
            'plugin_image_libraries': 'pluginImageLibraries',
            'is_tweak_template': 'isTweakTemplate',
            'show_item_navigator': 'showItemNavigator',
            'show_item_counts': 'showItemCounts',
            'show_editable_item_toggle': 'showEditableItemToggle',
            'id': 'id',
            'team_id': 'teamId',
            'team': 'team',
            'team_member_id': 'teamMemberId',
            'team_member': 'teamMember',
            'portal_id': 'portalId',
            'portal': 'portal',
            'portal_member_id': 'portalMemberId',
            'portal_member': 'portalMember',
            'design_id': 'designId',
            'design': 'design',
            'template_id': 'templateId',
            'template': 'template'
        }

        self._api_partner_auth_url = api_partner_auth_url
        self._plugin_product_id = plugin_product_id
        self._saved_product_id = saved_product_id
        self._allow_add_image = allow_add_image
        self._allow_add_text = allow_add_text
        self._allow_jpeg = allow_jpeg
        self._allow_low_res_pdf = allow_low_res_pdf
        self._allow_high_res_pdf = allow_high_res_pdf
        self._allow_save_for_later = allow_save_for_later
        self._allow_save_as_template = allow_save_as_template
        self._allow_duplicate_design = allow_duplicate_design
        self._block_editing = block_editing
        self._make_all_items_editable = make_all_items_editable
        self._show_confirm = show_confirm
        self._allow_approve_plugin_product = allow_approve_plugin_product
        self._allow_send_to_approve_plugin_product = allow_send_to_approve_plugin_product
        self._workflow_form = workflow_form
        self._design_form_data = design_form_data
        self._show_plugin_images = show_plugin_images
        self._plugin_image_libraries = plugin_image_libraries
        self._is_tweak_template = is_tweak_template
        self._show_item_navigator = show_item_navigator
        self._show_item_counts = show_item_counts
        self._show_editable_item_toggle = show_editable_item_toggle
        self._id = id
        self._team_id = team_id
        self._team = team
        self._team_member_id = team_member_id
        self._team_member = team_member
        self._portal_id = portal_id
        self._portal = portal
        self._portal_member_id = portal_member_id
        self._portal_member = portal_member
        self._design_id = design_id
        self._design = design
        self._template_id = template_id
        self._template = template


    @property
    def api_partner_auth_url(self):
        """
        Gets the api_partner_auth_url of this FlashVar.


        :return: The api_partner_auth_url of this FlashVar.
        :rtype: str
        """
        return self._api_partner_auth_url

    @api_partner_auth_url.setter
    def api_partner_auth_url(self, api_partner_auth_url):
        """
        Sets the api_partner_auth_url of this FlashVar.


        :param api_partner_auth_url: The api_partner_auth_url of this FlashVar.
        :type: str
        """

        self._api_partner_auth_url = api_partner_auth_url

    @property
    def plugin_product_id(self):
        """
        Gets the plugin_product_id of this FlashVar.


        :return: The plugin_product_id of this FlashVar.
        :rtype: str
        """
        return self._plugin_product_id

    @plugin_product_id.setter
    def plugin_product_id(self, plugin_product_id):
        """
        Sets the plugin_product_id of this FlashVar.


        :param plugin_product_id: The plugin_product_id of this FlashVar.
        :type: str
        """

        self._plugin_product_id = plugin_product_id

    @property
    def saved_product_id(self):
        """
        Gets the saved_product_id of this FlashVar.


        :return: The saved_product_id of this FlashVar.
        :rtype: str
        """
        return self._saved_product_id

    @saved_product_id.setter
    def saved_product_id(self, saved_product_id):
        """
        Sets the saved_product_id of this FlashVar.


        :param saved_product_id: The saved_product_id of this FlashVar.
        :type: str
        """

        self._saved_product_id = saved_product_id

    @property
    def allow_add_image(self):
        """
        Gets the allow_add_image of this FlashVar.


        :return: The allow_add_image of this FlashVar.
        :rtype: bool
        """
        return self._allow_add_image

    @allow_add_image.setter
    def allow_add_image(self, allow_add_image):
        """
        Sets the allow_add_image of this FlashVar.


        :param allow_add_image: The allow_add_image of this FlashVar.
        :type: bool
        """

        self._allow_add_image = allow_add_image

    @property
    def allow_add_text(self):
        """
        Gets the allow_add_text of this FlashVar.


        :return: The allow_add_text of this FlashVar.
        :rtype: bool
        """
        return self._allow_add_text

    @allow_add_text.setter
    def allow_add_text(self, allow_add_text):
        """
        Sets the allow_add_text of this FlashVar.


        :param allow_add_text: The allow_add_text of this FlashVar.
        :type: bool
        """

        self._allow_add_text = allow_add_text

    @property
    def allow_jpeg(self):
        """
        Gets the allow_jpeg of this FlashVar.


        :return: The allow_jpeg of this FlashVar.
        :rtype: bool
        """
        return self._allow_jpeg

    @allow_jpeg.setter
    def allow_jpeg(self, allow_jpeg):
        """
        Sets the allow_jpeg of this FlashVar.


        :param allow_jpeg: The allow_jpeg of this FlashVar.
        :type: bool
        """

        self._allow_jpeg = allow_jpeg

    @property
    def allow_low_res_pdf(self):
        """
        Gets the allow_low_res_pdf of this FlashVar.


        :return: The allow_low_res_pdf of this FlashVar.
        :rtype: bool
        """
        return self._allow_low_res_pdf

    @allow_low_res_pdf.setter
    def allow_low_res_pdf(self, allow_low_res_pdf):
        """
        Sets the allow_low_res_pdf of this FlashVar.


        :param allow_low_res_pdf: The allow_low_res_pdf of this FlashVar.
        :type: bool
        """

        self._allow_low_res_pdf = allow_low_res_pdf

    @property
    def allow_high_res_pdf(self):
        """
        Gets the allow_high_res_pdf of this FlashVar.


        :return: The allow_high_res_pdf of this FlashVar.
        :rtype: bool
        """
        return self._allow_high_res_pdf

    @allow_high_res_pdf.setter
    def allow_high_res_pdf(self, allow_high_res_pdf):
        """
        Sets the allow_high_res_pdf of this FlashVar.


        :param allow_high_res_pdf: The allow_high_res_pdf of this FlashVar.
        :type: bool
        """

        self._allow_high_res_pdf = allow_high_res_pdf

    @property
    def allow_save_for_later(self):
        """
        Gets the allow_save_for_later of this FlashVar.


        :return: The allow_save_for_later of this FlashVar.
        :rtype: bool
        """
        return self._allow_save_for_later

    @allow_save_for_later.setter
    def allow_save_for_later(self, allow_save_for_later):
        """
        Sets the allow_save_for_later of this FlashVar.


        :param allow_save_for_later: The allow_save_for_later of this FlashVar.
        :type: bool
        """

        self._allow_save_for_later = allow_save_for_later

    @property
    def allow_save_as_template(self):
        """
        Gets the allow_save_as_template of this FlashVar.


        :return: The allow_save_as_template of this FlashVar.
        :rtype: bool
        """
        return self._allow_save_as_template

    @allow_save_as_template.setter
    def allow_save_as_template(self, allow_save_as_template):
        """
        Sets the allow_save_as_template of this FlashVar.


        :param allow_save_as_template: The allow_save_as_template of this FlashVar.
        :type: bool
        """

        self._allow_save_as_template = allow_save_as_template

    @property
    def allow_duplicate_design(self):
        """
        Gets the allow_duplicate_design of this FlashVar.


        :return: The allow_duplicate_design of this FlashVar.
        :rtype: bool
        """
        return self._allow_duplicate_design

    @allow_duplicate_design.setter
    def allow_duplicate_design(self, allow_duplicate_design):
        """
        Sets the allow_duplicate_design of this FlashVar.


        :param allow_duplicate_design: The allow_duplicate_design of this FlashVar.
        :type: bool
        """

        self._allow_duplicate_design = allow_duplicate_design

    @property
    def block_editing(self):
        """
        Gets the block_editing of this FlashVar.


        :return: The block_editing of this FlashVar.
        :rtype: bool
        """
        return self._block_editing

    @block_editing.setter
    def block_editing(self, block_editing):
        """
        Sets the block_editing of this FlashVar.


        :param block_editing: The block_editing of this FlashVar.
        :type: bool
        """

        self._block_editing = block_editing

    @property
    def make_all_items_editable(self):
        """
        Gets the make_all_items_editable of this FlashVar.


        :return: The make_all_items_editable of this FlashVar.
        :rtype: bool
        """
        return self._make_all_items_editable

    @make_all_items_editable.setter
    def make_all_items_editable(self, make_all_items_editable):
        """
        Sets the make_all_items_editable of this FlashVar.


        :param make_all_items_editable: The make_all_items_editable of this FlashVar.
        :type: bool
        """

        self._make_all_items_editable = make_all_items_editable

    @property
    def show_confirm(self):
        """
        Gets the show_confirm of this FlashVar.


        :return: The show_confirm of this FlashVar.
        :rtype: bool
        """
        return self._show_confirm

    @show_confirm.setter
    def show_confirm(self, show_confirm):
        """
        Sets the show_confirm of this FlashVar.


        :param show_confirm: The show_confirm of this FlashVar.
        :type: bool
        """

        self._show_confirm = show_confirm

    @property
    def allow_approve_plugin_product(self):
        """
        Gets the allow_approve_plugin_product of this FlashVar.


        :return: The allow_approve_plugin_product of this FlashVar.
        :rtype: bool
        """
        return self._allow_approve_plugin_product

    @allow_approve_plugin_product.setter
    def allow_approve_plugin_product(self, allow_approve_plugin_product):
        """
        Sets the allow_approve_plugin_product of this FlashVar.


        :param allow_approve_plugin_product: The allow_approve_plugin_product of this FlashVar.
        :type: bool
        """

        self._allow_approve_plugin_product = allow_approve_plugin_product

    @property
    def allow_send_to_approve_plugin_product(self):
        """
        Gets the allow_send_to_approve_plugin_product of this FlashVar.


        :return: The allow_send_to_approve_plugin_product of this FlashVar.
        :rtype: bool
        """
        return self._allow_send_to_approve_plugin_product

    @allow_send_to_approve_plugin_product.setter
    def allow_send_to_approve_plugin_product(self, allow_send_to_approve_plugin_product):
        """
        Sets the allow_send_to_approve_plugin_product of this FlashVar.


        :param allow_send_to_approve_plugin_product: The allow_send_to_approve_plugin_product of this FlashVar.
        :type: bool
        """

        self._allow_send_to_approve_plugin_product = allow_send_to_approve_plugin_product

    @property
    def workflow_form(self):
        """
        Gets the workflow_form of this FlashVar.


        :return: The workflow_form of this FlashVar.
        :rtype: str
        """
        return self._workflow_form

    @workflow_form.setter
    def workflow_form(self, workflow_form):
        """
        Sets the workflow_form of this FlashVar.


        :param workflow_form: The workflow_form of this FlashVar.
        :type: str
        """

        self._workflow_form = workflow_form

    @property
    def design_form_data(self):
        """
        Gets the design_form_data of this FlashVar.


        :return: The design_form_data of this FlashVar.
        :rtype: list[object]
        """
        return self._design_form_data

    @design_form_data.setter
    def design_form_data(self, design_form_data):
        """
        Sets the design_form_data of this FlashVar.


        :param design_form_data: The design_form_data of this FlashVar.
        :type: list[object]
        """

        self._design_form_data = design_form_data

    @property
    def show_plugin_images(self):
        """
        Gets the show_plugin_images of this FlashVar.


        :return: The show_plugin_images of this FlashVar.
        :rtype: bool
        """
        return self._show_plugin_images

    @show_plugin_images.setter
    def show_plugin_images(self, show_plugin_images):
        """
        Sets the show_plugin_images of this FlashVar.


        :param show_plugin_images: The show_plugin_images of this FlashVar.
        :type: bool
        """

        self._show_plugin_images = show_plugin_images

    @property
    def plugin_image_libraries(self):
        """
        Gets the plugin_image_libraries of this FlashVar.


        :return: The plugin_image_libraries of this FlashVar.
        :rtype: list[str]
        """
        return self._plugin_image_libraries

    @plugin_image_libraries.setter
    def plugin_image_libraries(self, plugin_image_libraries):
        """
        Sets the plugin_image_libraries of this FlashVar.


        :param plugin_image_libraries: The plugin_image_libraries of this FlashVar.
        :type: list[str]
        """

        self._plugin_image_libraries = plugin_image_libraries

    @property
    def is_tweak_template(self):
        """
        Gets the is_tweak_template of this FlashVar.


        :return: The is_tweak_template of this FlashVar.
        :rtype: bool
        """
        return self._is_tweak_template

    @is_tweak_template.setter
    def is_tweak_template(self, is_tweak_template):
        """
        Sets the is_tweak_template of this FlashVar.


        :param is_tweak_template: The is_tweak_template of this FlashVar.
        :type: bool
        """

        self._is_tweak_template = is_tweak_template

    @property
    def show_item_navigator(self):
        """
        Gets the show_item_navigator of this FlashVar.


        :return: The show_item_navigator of this FlashVar.
        :rtype: bool
        """
        return self._show_item_navigator

    @show_item_navigator.setter
    def show_item_navigator(self, show_item_navigator):
        """
        Sets the show_item_navigator of this FlashVar.


        :param show_item_navigator: The show_item_navigator of this FlashVar.
        :type: bool
        """

        self._show_item_navigator = show_item_navigator

    @property
    def show_item_counts(self):
        """
        Gets the show_item_counts of this FlashVar.


        :return: The show_item_counts of this FlashVar.
        :rtype: bool
        """
        return self._show_item_counts

    @show_item_counts.setter
    def show_item_counts(self, show_item_counts):
        """
        Sets the show_item_counts of this FlashVar.


        :param show_item_counts: The show_item_counts of this FlashVar.
        :type: bool
        """

        self._show_item_counts = show_item_counts

    @property
    def show_editable_item_toggle(self):
        """
        Gets the show_editable_item_toggle of this FlashVar.


        :return: The show_editable_item_toggle of this FlashVar.
        :rtype: bool
        """
        return self._show_editable_item_toggle

    @show_editable_item_toggle.setter
    def show_editable_item_toggle(self, show_editable_item_toggle):
        """
        Sets the show_editable_item_toggle of this FlashVar.


        :param show_editable_item_toggle: The show_editable_item_toggle of this FlashVar.
        :type: bool
        """

        self._show_editable_item_toggle = show_editable_item_toggle

    @property
    def id(self):
        """
        Gets the id of this FlashVar.


        :return: The id of this FlashVar.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FlashVar.


        :param id: The id of this FlashVar.
        :type: str
        """

        self._id = id

    @property
    def team_id(self):
        """
        Gets the team_id of this FlashVar.


        :return: The team_id of this FlashVar.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this FlashVar.


        :param team_id: The team_id of this FlashVar.
        :type: str
        """

        self._team_id = team_id

    @property
    def team(self):
        """
        Gets the team of this FlashVar.


        :return: The team of this FlashVar.
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        Sets the team of this FlashVar.


        :param team: The team of this FlashVar.
        :type: Team
        """

        self._team = team

    @property
    def team_member_id(self):
        """
        Gets the team_member_id of this FlashVar.


        :return: The team_member_id of this FlashVar.
        :rtype: str
        """
        return self._team_member_id

    @team_member_id.setter
    def team_member_id(self, team_member_id):
        """
        Sets the team_member_id of this FlashVar.


        :param team_member_id: The team_member_id of this FlashVar.
        :type: str
        """

        self._team_member_id = team_member_id

    @property
    def team_member(self):
        """
        Gets the team_member of this FlashVar.


        :return: The team_member of this FlashVar.
        :rtype: TeamMember
        """
        return self._team_member

    @team_member.setter
    def team_member(self, team_member):
        """
        Sets the team_member of this FlashVar.


        :param team_member: The team_member of this FlashVar.
        :type: TeamMember
        """

        self._team_member = team_member

    @property
    def portal_id(self):
        """
        Gets the portal_id of this FlashVar.


        :return: The portal_id of this FlashVar.
        :rtype: str
        """
        return self._portal_id

    @portal_id.setter
    def portal_id(self, portal_id):
        """
        Sets the portal_id of this FlashVar.


        :param portal_id: The portal_id of this FlashVar.
        :type: str
        """

        self._portal_id = portal_id

    @property
    def portal(self):
        """
        Gets the portal of this FlashVar.


        :return: The portal of this FlashVar.
        :rtype: Portal
        """
        return self._portal

    @portal.setter
    def portal(self, portal):
        """
        Sets the portal of this FlashVar.


        :param portal: The portal of this FlashVar.
        :type: Portal
        """

        self._portal = portal

    @property
    def portal_member_id(self):
        """
        Gets the portal_member_id of this FlashVar.


        :return: The portal_member_id of this FlashVar.
        :rtype: str
        """
        return self._portal_member_id

    @portal_member_id.setter
    def portal_member_id(self, portal_member_id):
        """
        Sets the portal_member_id of this FlashVar.


        :param portal_member_id: The portal_member_id of this FlashVar.
        :type: str
        """

        self._portal_member_id = portal_member_id

    @property
    def portal_member(self):
        """
        Gets the portal_member of this FlashVar.


        :return: The portal_member of this FlashVar.
        :rtype: PortalMember
        """
        return self._portal_member

    @portal_member.setter
    def portal_member(self, portal_member):
        """
        Sets the portal_member of this FlashVar.


        :param portal_member: The portal_member of this FlashVar.
        :type: PortalMember
        """

        self._portal_member = portal_member

    @property
    def design_id(self):
        """
        Gets the design_id of this FlashVar.


        :return: The design_id of this FlashVar.
        :rtype: str
        """
        return self._design_id

    @design_id.setter
    def design_id(self, design_id):
        """
        Sets the design_id of this FlashVar.


        :param design_id: The design_id of this FlashVar.
        :type: str
        """

        self._design_id = design_id

    @property
    def design(self):
        """
        Gets the design of this FlashVar.


        :return: The design of this FlashVar.
        :rtype: Design
        """
        return self._design

    @design.setter
    def design(self, design):
        """
        Sets the design of this FlashVar.


        :param design: The design of this FlashVar.
        :type: Design
        """

        self._design = design

    @property
    def template_id(self):
        """
        Gets the template_id of this FlashVar.


        :return: The template_id of this FlashVar.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this FlashVar.


        :param template_id: The template_id of this FlashVar.
        :type: str
        """

        self._template_id = template_id

    @property
    def template(self):
        """
        Gets the template of this FlashVar.


        :return: The template of this FlashVar.
        :rtype: Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this FlashVar.


        :param template: The template of this FlashVar.
        :type: Template
        """

        self._template = template

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
