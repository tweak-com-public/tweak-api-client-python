# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 0.0.4
    
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

from __future__ import absolute_import

import os
import sys
import unittest

import TweakApi
from TweakApi.rest import ApiException
from TweakApi.apis.customer_api import CustomerApi


class TestCustomerApi(unittest.TestCase):
    """ CustomerApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.customer_api.CustomerApi()

    def tearDown(self):
        pass

    def test_customers_change_password_post(self):
        """
        Test case for customers_change_password_post

        Change a user's password.
        """
        pass

    def test_customers_change_stream_get(self):
        """
        Test case for customers_change_stream_get

        Create a change stream.
        """
        pass

    def test_customers_change_stream_post(self):
        """
        Test case for customers_change_stream_post

        Create a change stream.
        """
        pass

    def test_customers_confirm_get(self):
        """
        Test case for customers_confirm_get

        Confirm a user registration with identity verification token.
        """
        pass

    def test_customers_count_get(self):
        """
        Test case for customers_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_customers_email_email_exists_get(self):
        """
        Test case for customers_email_email_exists_get

        Define whether customer exists or not
        """
        pass

    def test_customers_find_one_get(self):
        """
        Test case for customers_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_customers_get(self):
        """
        Test case for customers_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_customers_id_access_tokens_count_get(self):
        """
        Test case for customers_id_access_tokens_count_get

        Counts accessTokens of Customer.
        """
        pass

    def test_customers_id_access_tokens_delete(self):
        """
        Test case for customers_id_access_tokens_delete

        Deletes all accessTokens of this model.
        """
        pass

    def test_customers_id_access_tokens_fk_delete(self):
        """
        Test case for customers_id_access_tokens_fk_delete

        Delete a related item by id for accessTokens.
        """
        pass

    def test_customers_id_access_tokens_fk_get(self):
        """
        Test case for customers_id_access_tokens_fk_get

        Find a related item by id for accessTokens.
        """
        pass

    def test_customers_id_access_tokens_fk_put(self):
        """
        Test case for customers_id_access_tokens_fk_put

        Update a related item by id for accessTokens.
        """
        pass

    def test_customers_id_access_tokens_get(self):
        """
        Test case for customers_id_access_tokens_get

        Queries accessTokens of Customer.
        """
        pass

    def test_customers_id_access_tokens_post(self):
        """
        Test case for customers_id_access_tokens_post

        Creates a new instance in accessTokens of this model.
        """
        pass

    def test_customers_id_active_get(self):
        """
        Test case for customers_id_active_get

        Define whether customer is active or not
        """
        pass

    def test_customers_id_delete(self):
        """
        Test case for customers_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_customers_id_designs_count_get(self):
        """
        Test case for customers_id_designs_count_get

        Counts designs of Customer.
        """
        pass

    def test_customers_id_designs_delete(self):
        """
        Test case for customers_id_designs_delete

        Deletes all designs of this model.
        """
        pass

    def test_customers_id_designs_fk_delete(self):
        """
        Test case for customers_id_designs_fk_delete

        Delete a related item by id for designs.
        """
        pass

    def test_customers_id_designs_fk_get(self):
        """
        Test case for customers_id_designs_fk_get

        Find a related item by id for designs.
        """
        pass

    def test_customers_id_designs_fk_put(self):
        """
        Test case for customers_id_designs_fk_put

        Update a related item by id for designs.
        """
        pass

    def test_customers_id_designs_get(self):
        """
        Test case for customers_id_designs_get

        Queries designs of Customer.
        """
        pass

    def test_customers_id_designs_post(self):
        """
        Test case for customers_id_designs_post

        Creates a new instance in designs of this model.
        """
        pass

    def test_customers_id_exists_get(self):
        """
        Test case for customers_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_customers_id_get(self):
        """
        Test case for customers_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_customers_id_head(self):
        """
        Test case for customers_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_customers_id_invitation_tickets_count_get(self):
        """
        Test case for customers_id_invitation_tickets_count_get

        Counts invitationTickets of Customer.
        """
        pass

    def test_customers_id_invitation_tickets_delete(self):
        """
        Test case for customers_id_invitation_tickets_delete

        Deletes all invitationTickets of this model.
        """
        pass

    def test_customers_id_invitation_tickets_fk_delete(self):
        """
        Test case for customers_id_invitation_tickets_fk_delete

        Delete a related item by id for invitationTickets.
        """
        pass

    def test_customers_id_invitation_tickets_fk_get(self):
        """
        Test case for customers_id_invitation_tickets_fk_get

        Find a related item by id for invitationTickets.
        """
        pass

    def test_customers_id_invitation_tickets_fk_put(self):
        """
        Test case for customers_id_invitation_tickets_fk_put

        Update a related item by id for invitationTickets.
        """
        pass

    def test_customers_id_invitation_tickets_get(self):
        """
        Test case for customers_id_invitation_tickets_get

        Queries invitationTickets of Customer.
        """
        pass

    def test_customers_id_invitation_tickets_post(self):
        """
        Test case for customers_id_invitation_tickets_post

        Creates a new instance in invitationTickets of this model.
        """
        pass

    def test_customers_id_patch(self):
        """
        Test case for customers_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_customers_id_permission_delete(self):
        """
        Test case for customers_id_permission_delete

        Deletes permission of this model.
        """
        pass

    def test_customers_id_permission_get(self):
        """
        Test case for customers_id_permission_get

        Fetches hasOne relation permission.
        """
        pass

    def test_customers_id_permission_post(self):
        """
        Test case for customers_id_permission_post

        Creates a new instance in permission of this model.
        """
        pass

    def test_customers_id_permission_put(self):
        """
        Test case for customers_id_permission_put

        Update permission of this model.
        """
        pass

    def test_customers_id_profile_picture_put(self):
        """
        Test case for customers_id_profile_picture_put

        Change profile picture
        """
        pass

    def test_customers_id_put(self):
        """
        Test case for customers_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_customers_id_register_team_post(self):
        """
        Test case for customers_id_register_team_post

        Register team and assign it to the customer
        """
        pass

    def test_customers_id_replace_post(self):
        """
        Test case for customers_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_customers_id_teams_count_get(self):
        """
        Test case for customers_id_teams_count_get

        Counts teams of Customer.
        """
        pass

    def test_customers_id_teams_delete(self):
        """
        Test case for customers_id_teams_delete

        Deletes all teams of this model.
        """
        pass

    def test_customers_id_teams_fk_delete(self):
        """
        Test case for customers_id_teams_fk_delete

        Delete a related item by id for teams.
        """
        pass

    def test_customers_id_teams_fk_get(self):
        """
        Test case for customers_id_teams_fk_get

        Find a related item by id for teams.
        """
        pass

    def test_customers_id_teams_fk_put(self):
        """
        Test case for customers_id_teams_fk_put

        Update a related item by id for teams.
        """
        pass

    def test_customers_id_teams_get(self):
        """
        Test case for customers_id_teams_get

        Queries teams of Customer.
        """
        pass

    def test_customers_id_teams_nk_billing_delete(self):
        """
        Test case for customers_id_teams_nk_billing_delete

        Deletes billing of this model.
        """
        pass

    def test_customers_id_teams_nk_billing_get(self):
        """
        Test case for customers_id_teams_nk_billing_get

        Fetches hasOne relation billing.
        """
        pass

    def test_customers_id_teams_nk_billing_post(self):
        """
        Test case for customers_id_teams_nk_billing_post

        Creates a new instance in billing of this model.
        """
        pass

    def test_customers_id_teams_nk_billing_put(self):
        """
        Test case for customers_id_teams_nk_billing_put

        Update billing of this model.
        """
        pass

    def test_customers_id_teams_nk_brand_delete(self):
        """
        Test case for customers_id_teams_nk_brand_delete

        Deletes brand of this model.
        """
        pass

    def test_customers_id_teams_nk_brand_get(self):
        """
        Test case for customers_id_teams_nk_brand_get

        Fetches hasOne relation brand.
        """
        pass

    def test_customers_id_teams_nk_brand_post(self):
        """
        Test case for customers_id_teams_nk_brand_post

        Creates a new instance in brand of this model.
        """
        pass

    def test_customers_id_teams_nk_brand_put(self):
        """
        Test case for customers_id_teams_nk_brand_put

        Update brand of this model.
        """
        pass

    def test_customers_id_teams_nk_data_sources_count_get(self):
        """
        Test case for customers_id_teams_nk_data_sources_count_get

        Counts dataSources of Team.
        """
        pass

    def test_customers_id_teams_nk_data_sources_delete(self):
        """
        Test case for customers_id_teams_nk_data_sources_delete

        Deletes all dataSources of this model.
        """
        pass

    def test_customers_id_teams_nk_data_sources_fk_delete(self):
        """
        Test case for customers_id_teams_nk_data_sources_fk_delete

        Delete a related item by id for dataSources.
        """
        pass

    def test_customers_id_teams_nk_data_sources_fk_get(self):
        """
        Test case for customers_id_teams_nk_data_sources_fk_get

        Find a related item by id for dataSources.
        """
        pass

    def test_customers_id_teams_nk_data_sources_fk_put(self):
        """
        Test case for customers_id_teams_nk_data_sources_fk_put

        Update a related item by id for dataSources.
        """
        pass

    def test_customers_id_teams_nk_data_sources_get(self):
        """
        Test case for customers_id_teams_nk_data_sources_get

        Queries dataSources of Team.
        """
        pass

    def test_customers_id_teams_nk_data_sources_post(self):
        """
        Test case for customers_id_teams_nk_data_sources_post

        Creates a new instance in dataSources of this model.
        """
        pass

    def test_customers_id_teams_nk_image_folders_count_get(self):
        """
        Test case for customers_id_teams_nk_image_folders_count_get

        Counts imageFolders of Team.
        """
        pass

    def test_customers_id_teams_nk_image_folders_delete(self):
        """
        Test case for customers_id_teams_nk_image_folders_delete

        Deletes all imageFolders of this model.
        """
        pass

    def test_customers_id_teams_nk_image_folders_fk_delete(self):
        """
        Test case for customers_id_teams_nk_image_folders_fk_delete

        Delete a related item by id for imageFolders.
        """
        pass

    def test_customers_id_teams_nk_image_folders_fk_get(self):
        """
        Test case for customers_id_teams_nk_image_folders_fk_get

        Find a related item by id for imageFolders.
        """
        pass

    def test_customers_id_teams_nk_image_folders_fk_put(self):
        """
        Test case for customers_id_teams_nk_image_folders_fk_put

        Update a related item by id for imageFolders.
        """
        pass

    def test_customers_id_teams_nk_image_folders_get(self):
        """
        Test case for customers_id_teams_nk_image_folders_get

        Queries imageFolders of Team.
        """
        pass

    def test_customers_id_teams_nk_image_folders_post(self):
        """
        Test case for customers_id_teams_nk_image_folders_post

        Creates a new instance in imageFolders of this model.
        """
        pass

    def test_customers_id_teams_nk_images_count_get(self):
        """
        Test case for customers_id_teams_nk_images_count_get

        Counts images of Team.
        """
        pass

    def test_customers_id_teams_nk_images_delete(self):
        """
        Test case for customers_id_teams_nk_images_delete

        Deletes all images of this model.
        """
        pass

    def test_customers_id_teams_nk_images_fk_delete(self):
        """
        Test case for customers_id_teams_nk_images_fk_delete

        Delete a related item by id for images.
        """
        pass

    def test_customers_id_teams_nk_images_fk_get(self):
        """
        Test case for customers_id_teams_nk_images_fk_get

        Find a related item by id for images.
        """
        pass

    def test_customers_id_teams_nk_images_fk_put(self):
        """
        Test case for customers_id_teams_nk_images_fk_put

        Update a related item by id for images.
        """
        pass

    def test_customers_id_teams_nk_images_get(self):
        """
        Test case for customers_id_teams_nk_images_get

        Queries images of Team.
        """
        pass

    def test_customers_id_teams_nk_images_post(self):
        """
        Test case for customers_id_teams_nk_images_post

        Creates a new instance in images of this model.
        """
        pass

    def test_customers_id_teams_nk_members_count_get(self):
        """
        Test case for customers_id_teams_nk_members_count_get

        Counts members of Team.
        """
        pass

    def test_customers_id_teams_nk_members_delete(self):
        """
        Test case for customers_id_teams_nk_members_delete

        Deletes all members of this model.
        """
        pass

    def test_customers_id_teams_nk_members_fk_delete(self):
        """
        Test case for customers_id_teams_nk_members_fk_delete

        Delete a related item by id for members.
        """
        pass

    def test_customers_id_teams_nk_members_fk_get(self):
        """
        Test case for customers_id_teams_nk_members_fk_get

        Find a related item by id for members.
        """
        pass

    def test_customers_id_teams_nk_members_fk_put(self):
        """
        Test case for customers_id_teams_nk_members_fk_put

        Update a related item by id for members.
        """
        pass

    def test_customers_id_teams_nk_members_get(self):
        """
        Test case for customers_id_teams_nk_members_get

        Queries members of Team.
        """
        pass

    def test_customers_id_teams_nk_members_post(self):
        """
        Test case for customers_id_teams_nk_members_post

        Creates a new instance in members of this model.
        """
        pass

    def test_customers_id_teams_nk_members_rel_fk_delete(self):
        """
        Test case for customers_id_teams_nk_members_rel_fk_delete

        Remove the members relation to an item by id.
        """
        pass

    def test_customers_id_teams_nk_members_rel_fk_head(self):
        """
        Test case for customers_id_teams_nk_members_rel_fk_head

        Check the existence of members relation to an item by id.
        """
        pass

    def test_customers_id_teams_nk_members_rel_fk_put(self):
        """
        Test case for customers_id_teams_nk_members_rel_fk_put

        Add a related item by id for members.
        """
        pass

    def test_customers_id_teams_nk_permission_delete(self):
        """
        Test case for customers_id_teams_nk_permission_delete

        Deletes permission of this model.
        """
        pass

    def test_customers_id_teams_nk_permission_get(self):
        """
        Test case for customers_id_teams_nk_permission_get

        Fetches hasOne relation permission.
        """
        pass

    def test_customers_id_teams_nk_permission_post(self):
        """
        Test case for customers_id_teams_nk_permission_post

        Creates a new instance in permission of this model.
        """
        pass

    def test_customers_id_teams_nk_permission_put(self):
        """
        Test case for customers_id_teams_nk_permission_put

        Update permission of this model.
        """
        pass

    def test_customers_id_teams_nk_portals_count_get(self):
        """
        Test case for customers_id_teams_nk_portals_count_get

        Counts portals of Team.
        """
        pass

    def test_customers_id_teams_nk_portals_delete(self):
        """
        Test case for customers_id_teams_nk_portals_delete

        Deletes all portals of this model.
        """
        pass

    def test_customers_id_teams_nk_portals_fk_delete(self):
        """
        Test case for customers_id_teams_nk_portals_fk_delete

        Delete a related item by id for portals.
        """
        pass

    def test_customers_id_teams_nk_portals_fk_get(self):
        """
        Test case for customers_id_teams_nk_portals_fk_get

        Find a related item by id for portals.
        """
        pass

    def test_customers_id_teams_nk_portals_fk_put(self):
        """
        Test case for customers_id_teams_nk_portals_fk_put

        Update a related item by id for portals.
        """
        pass

    def test_customers_id_teams_nk_portals_get(self):
        """
        Test case for customers_id_teams_nk_portals_get

        Queries portals of Team.
        """
        pass

    def test_customers_id_teams_nk_portals_post(self):
        """
        Test case for customers_id_teams_nk_portals_post

        Creates a new instance in portals of this model.
        """
        pass

    def test_customers_id_teams_nk_team_members_count_get(self):
        """
        Test case for customers_id_teams_nk_team_members_count_get

        Counts teamMembers of Team.
        """
        pass

    def test_customers_id_teams_nk_team_members_delete(self):
        """
        Test case for customers_id_teams_nk_team_members_delete

        Deletes all teamMembers of this model.
        """
        pass

    def test_customers_id_teams_nk_team_members_fk_delete(self):
        """
        Test case for customers_id_teams_nk_team_members_fk_delete

        Delete a related item by id for teamMembers.
        """
        pass

    def test_customers_id_teams_nk_team_members_fk_get(self):
        """
        Test case for customers_id_teams_nk_team_members_fk_get

        Find a related item by id for teamMembers.
        """
        pass

    def test_customers_id_teams_nk_team_members_fk_put(self):
        """
        Test case for customers_id_teams_nk_team_members_fk_put

        Update a related item by id for teamMembers.
        """
        pass

    def test_customers_id_teams_nk_team_members_get(self):
        """
        Test case for customers_id_teams_nk_team_members_get

        Queries teamMembers of Team.
        """
        pass

    def test_customers_id_teams_nk_team_members_post(self):
        """
        Test case for customers_id_teams_nk_team_members_post

        Creates a new instance in teamMembers of this model.
        """
        pass

    def test_customers_id_teams_nk_template_folders_count_get(self):
        """
        Test case for customers_id_teams_nk_template_folders_count_get

        Counts templateFolders of Team.
        """
        pass

    def test_customers_id_teams_nk_template_folders_delete(self):
        """
        Test case for customers_id_teams_nk_template_folders_delete

        Deletes all templateFolders of this model.
        """
        pass

    def test_customers_id_teams_nk_template_folders_fk_delete(self):
        """
        Test case for customers_id_teams_nk_template_folders_fk_delete

        Delete a related item by id for templateFolders.
        """
        pass

    def test_customers_id_teams_nk_template_folders_fk_get(self):
        """
        Test case for customers_id_teams_nk_template_folders_fk_get

        Find a related item by id for templateFolders.
        """
        pass

    def test_customers_id_teams_nk_template_folders_fk_put(self):
        """
        Test case for customers_id_teams_nk_template_folders_fk_put

        Update a related item by id for templateFolders.
        """
        pass

    def test_customers_id_teams_nk_template_folders_get(self):
        """
        Test case for customers_id_teams_nk_template_folders_get

        Queries templateFolders of Team.
        """
        pass

    def test_customers_id_teams_nk_template_folders_post(self):
        """
        Test case for customers_id_teams_nk_template_folders_post

        Creates a new instance in templateFolders of this model.
        """
        pass

    def test_customers_id_teams_nk_templates_count_get(self):
        """
        Test case for customers_id_teams_nk_templates_count_get

        Counts templates of Team.
        """
        pass

    def test_customers_id_teams_nk_templates_delete(self):
        """
        Test case for customers_id_teams_nk_templates_delete

        Deletes all templates of this model.
        """
        pass

    def test_customers_id_teams_nk_templates_fk_delete(self):
        """
        Test case for customers_id_teams_nk_templates_fk_delete

        Delete a related item by id for templates.
        """
        pass

    def test_customers_id_teams_nk_templates_fk_get(self):
        """
        Test case for customers_id_teams_nk_templates_fk_get

        Find a related item by id for templates.
        """
        pass

    def test_customers_id_teams_nk_templates_fk_put(self):
        """
        Test case for customers_id_teams_nk_templates_fk_put

        Update a related item by id for templates.
        """
        pass

    def test_customers_id_teams_nk_templates_get(self):
        """
        Test case for customers_id_teams_nk_templates_get

        Queries templates of Team.
        """
        pass

    def test_customers_id_teams_nk_templates_post(self):
        """
        Test case for customers_id_teams_nk_templates_post

        Creates a new instance in templates of this model.
        """
        pass

    def test_customers_id_teams_nk_workflows_count_get(self):
        """
        Test case for customers_id_teams_nk_workflows_count_get

        Counts workflows of Team.
        """
        pass

    def test_customers_id_teams_nk_workflows_delete(self):
        """
        Test case for customers_id_teams_nk_workflows_delete

        Deletes all workflows of this model.
        """
        pass

    def test_customers_id_teams_nk_workflows_fk_delete(self):
        """
        Test case for customers_id_teams_nk_workflows_fk_delete

        Delete a related item by id for workflows.
        """
        pass

    def test_customers_id_teams_nk_workflows_fk_get(self):
        """
        Test case for customers_id_teams_nk_workflows_fk_get

        Find a related item by id for workflows.
        """
        pass

    def test_customers_id_teams_nk_workflows_fk_put(self):
        """
        Test case for customers_id_teams_nk_workflows_fk_put

        Update a related item by id for workflows.
        """
        pass

    def test_customers_id_teams_nk_workflows_get(self):
        """
        Test case for customers_id_teams_nk_workflows_get

        Queries workflows of Team.
        """
        pass

    def test_customers_id_teams_nk_workflows_post(self):
        """
        Test case for customers_id_teams_nk_workflows_post

        Creates a new instance in workflows of this model.
        """
        pass

    def test_customers_id_teams_post(self):
        """
        Test case for customers_id_teams_post

        Creates a new instance in teams of this model.
        """
        pass

    def test_customers_id_teams_rel_fk_delete(self):
        """
        Test case for customers_id_teams_rel_fk_delete

        Remove the teams relation to an item by id.
        """
        pass

    def test_customers_id_teams_rel_fk_head(self):
        """
        Test case for customers_id_teams_rel_fk_head

        Check the existence of teams relation to an item by id.
        """
        pass

    def test_customers_id_teams_rel_fk_put(self):
        """
        Test case for customers_id_teams_rel_fk_put

        Add a related item by id for teams.
        """
        pass

    def test_customers_id_teams_team_id_change_post(self):
        """
        Test case for customers_id_teams_team_id_change_post

        Move authentication to a Team
        """
        pass

    def test_customers_id_teams_team_id_portals_portal_id_change_post(self):
        """
        Test case for customers_id_teams_team_id_portals_portal_id_change_post

        Move authentication to a Portal
        """
        pass

    def test_customers_id_token_get(self):
        """
        Test case for customers_id_token_get

        Get token info
        """
        pass

    def test_customers_id_verify_post(self):
        """
        Test case for customers_id_verify_post

        Trigger user's identity verification with configured verifyOptions
        """
        pass

    def test_customers_invitation_tickets_token_accept_post(self):
        """
        Test case for customers_invitation_tickets_token_accept_post

        Accept invitation with token
        """
        pass

    def test_customers_invitation_tickets_token_get(self):
        """
        Test case for customers_invitation_tickets_token_get

        Get invitation details with token
        """
        pass

    def test_customers_login_post(self):
        """
        Test case for customers_login_post

        Login a user with username/email and password.
        """
        pass

    def test_customers_logout_post(self):
        """
        Test case for customers_logout_post

        Logout a user with access token.
        """
        pass

    def test_customers_me_token_get(self):
        """
        Test case for customers_me_token_get

        Get token info
        """
        pass

    def test_customers_me_token_refresh_get(self):
        """
        Test case for customers_me_token_refresh_get

        Refresh current access token
        """
        pass

    def test_customers_patch(self):
        """
        Test case for customers_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_customers_post(self):
        """
        Test case for customers_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_customers_put(self):
        """
        Test case for customers_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_customers_register_post(self):
        """
        Test case for customers_register_post

        Create customer and assign it to a team
        """
        pass

    def test_customers_replace_or_create_post(self):
        """
        Test case for customers_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_customers_reset_password_post(self):
        """
        Test case for customers_reset_password_post

        Reset user's password via a password-reset token.
        """
        pass

    def test_customers_reset_password_token_get(self):
        """
        Test case for customers_reset_password_token_get

        Get token info for reset password token
        """
        pass

    def test_customers_reset_post(self):
        """
        Test case for customers_reset_post

        Reset password for a user with email.
        """
        pass

    def test_customers_update_post(self):
        """
        Test case for customers_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_customers_upsert_with_where_post(self):
        """
        Test case for customers_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
