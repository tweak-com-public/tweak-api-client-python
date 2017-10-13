# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.2-alpha.0
    
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
from TweakApi.apis.portal_api import PortalApi


class TestPortalApi(unittest.TestCase):
    """ PortalApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.portal_api.PortalApi()

    def tearDown(self):
        pass

    def test_portals_change_stream_get(self):
        """
        Test case for portals_change_stream_get

        Create a change stream.
        """
        pass

    def test_portals_change_stream_post(self):
        """
        Test case for portals_change_stream_post

        Create a change stream.
        """
        pass

    def test_portals_count_get(self):
        """
        Test case for portals_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_portals_find_one_get(self):
        """
        Test case for portals_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_portals_get(self):
        """
        Test case for portals_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_portals_id_delete(self):
        """
        Test case for portals_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_portals_id_design_folders_count_get(self):
        """
        Test case for portals_id_design_folders_count_get

        Counts designFolders of Portal.
        """
        pass

    def test_portals_id_design_folders_delete(self):
        """
        Test case for portals_id_design_folders_delete

        Deletes all designFolders of this model.
        """
        pass

    def test_portals_id_design_folders_fk_delete(self):
        """
        Test case for portals_id_design_folders_fk_delete

        Delete a related item by id for designFolders.
        """
        pass

    def test_portals_id_design_folders_fk_get(self):
        """
        Test case for portals_id_design_folders_fk_get

        Find a related item by id for designFolders.
        """
        pass

    def test_portals_id_design_folders_fk_put(self):
        """
        Test case for portals_id_design_folders_fk_put

        Update a related item by id for designFolders.
        """
        pass

    def test_portals_id_design_folders_get(self):
        """
        Test case for portals_id_design_folders_get

        Queries designFolders of Portal.
        """
        pass

    def test_portals_id_design_folders_post(self):
        """
        Test case for portals_id_design_folders_post

        Creates a new instance in designFolders of this model.
        """
        pass

    def test_portals_id_designs_count_get(self):
        """
        Test case for portals_id_designs_count_get

        Counts designs of Portal.
        """
        pass

    def test_portals_id_designs_delete(self):
        """
        Test case for portals_id_designs_delete

        Deletes all designs of this model.
        """
        pass

    def test_portals_id_designs_fk_delete(self):
        """
        Test case for portals_id_designs_fk_delete

        Delete a related item by id for designs.
        """
        pass

    def test_portals_id_designs_fk_get(self):
        """
        Test case for portals_id_designs_fk_get

        Find a related item by id for designs.
        """
        pass

    def test_portals_id_designs_fk_put(self):
        """
        Test case for portals_id_designs_fk_put

        Update a related item by id for designs.
        """
        pass

    def test_portals_id_designs_get(self):
        """
        Test case for portals_id_designs_get

        Queries designs of Portal.
        """
        pass

    def test_portals_id_designs_nk_assignee_get(self):
        """
        Test case for portals_id_designs_nk_assignee_get

        Fetches belongsTo relation assignee.
        """
        pass

    def test_portals_id_designs_nk_commenters_count_get(self):
        """
        Test case for portals_id_designs_nk_commenters_count_get

        Counts commenters of Design.
        """
        pass

    def test_portals_id_designs_nk_commenters_delete(self):
        """
        Test case for portals_id_designs_nk_commenters_delete

        Deletes all commenters of this model.
        """
        pass

    def test_portals_id_designs_nk_commenters_fk_delete(self):
        """
        Test case for portals_id_designs_nk_commenters_fk_delete

        Delete a related item by id for commenters.
        """
        pass

    def test_portals_id_designs_nk_commenters_fk_get(self):
        """
        Test case for portals_id_designs_nk_commenters_fk_get

        Find a related item by id for commenters.
        """
        pass

    def test_portals_id_designs_nk_commenters_fk_put(self):
        """
        Test case for portals_id_designs_nk_commenters_fk_put

        Update a related item by id for commenters.
        """
        pass

    def test_portals_id_designs_nk_commenters_get(self):
        """
        Test case for portals_id_designs_nk_commenters_get

        Queries commenters of Design.
        """
        pass

    def test_portals_id_designs_nk_commenters_post(self):
        """
        Test case for portals_id_designs_nk_commenters_post

        Creates a new instance in commenters of this model.
        """
        pass

    def test_portals_id_designs_nk_commenters_rel_fk_delete(self):
        """
        Test case for portals_id_designs_nk_commenters_rel_fk_delete

        Remove the commenters relation to an item by id.
        """
        pass

    def test_portals_id_designs_nk_commenters_rel_fk_head(self):
        """
        Test case for portals_id_designs_nk_commenters_rel_fk_head

        Check the existence of commenters relation to an item by id.
        """
        pass

    def test_portals_id_designs_nk_commenters_rel_fk_put(self):
        """
        Test case for portals_id_designs_nk_commenters_rel_fk_put

        Add a related item by id for commenters.
        """
        pass

    def test_portals_id_designs_nk_comments_count_get(self):
        """
        Test case for portals_id_designs_nk_comments_count_get

        Counts comments of Design.
        """
        pass

    def test_portals_id_designs_nk_comments_delete(self):
        """
        Test case for portals_id_designs_nk_comments_delete

        Deletes all comments of this model.
        """
        pass

    def test_portals_id_designs_nk_comments_fk_delete(self):
        """
        Test case for portals_id_designs_nk_comments_fk_delete

        Delete a related item by id for comments.
        """
        pass

    def test_portals_id_designs_nk_comments_fk_get(self):
        """
        Test case for portals_id_designs_nk_comments_fk_get

        Find a related item by id for comments.
        """
        pass

    def test_portals_id_designs_nk_comments_fk_put(self):
        """
        Test case for portals_id_designs_nk_comments_fk_put

        Update a related item by id for comments.
        """
        pass

    def test_portals_id_designs_nk_comments_get(self):
        """
        Test case for portals_id_designs_nk_comments_get

        Queries comments of Design.
        """
        pass

    def test_portals_id_designs_nk_comments_post(self):
        """
        Test case for portals_id_designs_nk_comments_post

        Creates a new instance in comments of this model.
        """
        pass

    def test_portals_id_designs_nk_customer_get(self):
        """
        Test case for portals_id_designs_nk_customer_get

        Fetches belongsTo relation customer.
        """
        pass

    def test_portals_id_designs_nk_exports_count_get(self):
        """
        Test case for portals_id_designs_nk_exports_count_get

        Counts exports of Design.
        """
        pass

    def test_portals_id_designs_nk_exports_delete(self):
        """
        Test case for portals_id_designs_nk_exports_delete

        Deletes all exports of this model.
        """
        pass

    def test_portals_id_designs_nk_exports_fk_delete(self):
        """
        Test case for portals_id_designs_nk_exports_fk_delete

        Delete a related item by id for exports.
        """
        pass

    def test_portals_id_designs_nk_exports_fk_get(self):
        """
        Test case for portals_id_designs_nk_exports_fk_get

        Find a related item by id for exports.
        """
        pass

    def test_portals_id_designs_nk_exports_fk_put(self):
        """
        Test case for portals_id_designs_nk_exports_fk_put

        Update a related item by id for exports.
        """
        pass

    def test_portals_id_designs_nk_exports_get(self):
        """
        Test case for portals_id_designs_nk_exports_get

        Queries exports of Design.
        """
        pass

    def test_portals_id_designs_nk_exports_post(self):
        """
        Test case for portals_id_designs_nk_exports_post

        Creates a new instance in exports of this model.
        """
        pass

    def test_portals_id_designs_nk_folder_get(self):
        """
        Test case for portals_id_designs_nk_folder_get

        Fetches belongsTo relation folder.
        """
        pass

    def test_portals_id_designs_nk_permission_delete(self):
        """
        Test case for portals_id_designs_nk_permission_delete

        Deletes permission of this model.
        """
        pass

    def test_portals_id_designs_nk_permission_get(self):
        """
        Test case for portals_id_designs_nk_permission_get

        Fetches hasOne relation permission.
        """
        pass

    def test_portals_id_designs_nk_permission_post(self):
        """
        Test case for portals_id_designs_nk_permission_post

        Creates a new instance in permission of this model.
        """
        pass

    def test_portals_id_designs_nk_permission_put(self):
        """
        Test case for portals_id_designs_nk_permission_put

        Update permission of this model.
        """
        pass

    def test_portals_id_designs_nk_portal_get(self):
        """
        Test case for portals_id_designs_nk_portal_get

        Fetches belongsTo relation portal.
        """
        pass

    def test_portals_id_designs_nk_rejection_comment_get(self):
        """
        Test case for portals_id_designs_nk_rejection_comment_get

        Fetches belongsTo relation rejectionComment.
        """
        pass

    def test_portals_id_designs_nk_requester_get(self):
        """
        Test case for portals_id_designs_nk_requester_get

        Fetches belongsTo relation requester.
        """
        pass

    def test_portals_id_designs_nk_reviewer_get(self):
        """
        Test case for portals_id_designs_nk_reviewer_get

        Fetches belongsTo relation reviewer.
        """
        pass

    def test_portals_id_designs_nk_tags_count_get(self):
        """
        Test case for portals_id_designs_nk_tags_count_get

        Counts tags of Design.
        """
        pass

    def test_portals_id_designs_nk_tags_delete(self):
        """
        Test case for portals_id_designs_nk_tags_delete

        Deletes all tags of this model.
        """
        pass

    def test_portals_id_designs_nk_tags_fk_delete(self):
        """
        Test case for portals_id_designs_nk_tags_fk_delete

        Delete a related item by id for tags.
        """
        pass

    def test_portals_id_designs_nk_tags_fk_get(self):
        """
        Test case for portals_id_designs_nk_tags_fk_get

        Find a related item by id for tags.
        """
        pass

    def test_portals_id_designs_nk_tags_fk_put(self):
        """
        Test case for portals_id_designs_nk_tags_fk_put

        Update a related item by id for tags.
        """
        pass

    def test_portals_id_designs_nk_tags_get(self):
        """
        Test case for portals_id_designs_nk_tags_get

        Queries tags of Design.
        """
        pass

    def test_portals_id_designs_nk_tags_post(self):
        """
        Test case for portals_id_designs_nk_tags_post

        Creates a new instance in tags of this model.
        """
        pass

    def test_portals_id_designs_nk_tags_rel_fk_delete(self):
        """
        Test case for portals_id_designs_nk_tags_rel_fk_delete

        Remove the tags relation to an item by id.
        """
        pass

    def test_portals_id_designs_nk_tags_rel_fk_head(self):
        """
        Test case for portals_id_designs_nk_tags_rel_fk_head

        Check the existence of tags relation to an item by id.
        """
        pass

    def test_portals_id_designs_nk_tags_rel_fk_put(self):
        """
        Test case for portals_id_designs_nk_tags_rel_fk_put

        Add a related item by id for tags.
        """
        pass

    def test_portals_id_designs_nk_template_get(self):
        """
        Test case for portals_id_designs_nk_template_get

        Fetches belongsTo relation template.
        """
        pass

    def test_portals_id_designs_post(self):
        """
        Test case for portals_id_designs_post

        Creates a new instance in designs of this model.
        """
        pass

    def test_portals_id_exists_get(self):
        """
        Test case for portals_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_portals_id_get(self):
        """
        Test case for portals_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_portals_id_head(self):
        """
        Test case for portals_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_portals_id_image_folders_count_get(self):
        """
        Test case for portals_id_image_folders_count_get

        Counts imageFolders of Portal.
        """
        pass

    def test_portals_id_image_folders_delete(self):
        """
        Test case for portals_id_image_folders_delete

        Deletes all imageFolders of this model.
        """
        pass

    def test_portals_id_image_folders_fk_delete(self):
        """
        Test case for portals_id_image_folders_fk_delete

        Delete a related item by id for imageFolders.
        """
        pass

    def test_portals_id_image_folders_fk_get(self):
        """
        Test case for portals_id_image_folders_fk_get

        Find a related item by id for imageFolders.
        """
        pass

    def test_portals_id_image_folders_fk_put(self):
        """
        Test case for portals_id_image_folders_fk_put

        Update a related item by id for imageFolders.
        """
        pass

    def test_portals_id_image_folders_get(self):
        """
        Test case for portals_id_image_folders_get

        Queries imageFolders of Portal.
        """
        pass

    def test_portals_id_image_folders_post(self):
        """
        Test case for portals_id_image_folders_post

        Creates a new instance in imageFolders of this model.
        """
        pass

    def test_portals_id_image_folders_rel_fk_delete(self):
        """
        Test case for portals_id_image_folders_rel_fk_delete

        Remove the imageFolders relation to an item by id.
        """
        pass

    def test_portals_id_image_folders_rel_fk_head(self):
        """
        Test case for portals_id_image_folders_rel_fk_head

        Check the existence of imageFolders relation to an item by id.
        """
        pass

    def test_portals_id_image_folders_rel_fk_put(self):
        """
        Test case for portals_id_image_folders_rel_fk_put

        Add a related item by id for imageFolders.
        """
        pass

    def test_portals_id_invitation_tickets_fk_delete(self):
        """
        Test case for portals_id_invitation_tickets_fk_delete

        Delete InvitationTickets for this Portal
        """
        pass

    def test_portals_id_invitation_tickets_fk_get(self):
        """
        Test case for portals_id_invitation_tickets_fk_get

        Get InvitationTicket by Id for this Portal
        """
        pass

    def test_portals_id_invitation_tickets_get(self):
        """
        Test case for portals_id_invitation_tickets_get

        List InvitationTickets for this Portal
        """
        pass

    def test_portals_id_logo_put(self):
        """
        Test case for portals_id_logo_put

        Change logo
        """
        pass

    def test_portals_id_members_count_get(self):
        """
        Test case for portals_id_members_count_get

        Counts members of Portal.
        """
        pass

    def test_portals_id_members_delete(self):
        """
        Test case for portals_id_members_delete

        Deletes all members of this model.
        """
        pass

    def test_portals_id_members_fk_delete(self):
        """
        Test case for portals_id_members_fk_delete

        Delete a related item by id for members.
        """
        pass

    def test_portals_id_members_fk_get(self):
        """
        Test case for portals_id_members_fk_get

        Find a related item by id for members.
        """
        pass

    def test_portals_id_members_fk_put(self):
        """
        Test case for portals_id_members_fk_put

        Update a related item by id for members.
        """
        pass

    def test_portals_id_members_get(self):
        """
        Test case for portals_id_members_get

        Queries members of Portal.
        """
        pass

    def test_portals_id_members_post(self):
        """
        Test case for portals_id_members_post

        Creates a new instance in members of this model.
        """
        pass

    def test_portals_id_members_rel_fk_delete(self):
        """
        Test case for portals_id_members_rel_fk_delete

        Remove the members relation to an item by id.
        """
        pass

    def test_portals_id_members_rel_fk_head(self):
        """
        Test case for portals_id_members_rel_fk_head

        Check the existence of members relation to an item by id.
        """
        pass

    def test_portals_id_members_rel_fk_put(self):
        """
        Test case for portals_id_members_rel_fk_put

        Add a related item by id for members.
        """
        pass

    def test_portals_id_patch(self):
        """
        Test case for portals_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_portals_id_permission_delete(self):
        """
        Test case for portals_id_permission_delete

        Deletes permission of this model.
        """
        pass

    def test_portals_id_permission_get(self):
        """
        Test case for portals_id_permission_get

        Fetches hasOne relation permission.
        """
        pass

    def test_portals_id_permission_post(self):
        """
        Test case for portals_id_permission_post

        Creates a new instance in permission of this model.
        """
        pass

    def test_portals_id_permission_put(self):
        """
        Test case for portals_id_permission_put

        Update permission of this model.
        """
        pass

    def test_portals_id_portal_members_count_get(self):
        """
        Test case for portals_id_portal_members_count_get

        Counts portalMembers of Portal.
        """
        pass

    def test_portals_id_portal_members_delete(self):
        """
        Test case for portals_id_portal_members_delete

        Deletes all portalMembers of this model.
        """
        pass

    def test_portals_id_portal_members_fk_delete(self):
        """
        Test case for portals_id_portal_members_fk_delete

        Delete a related item by id for portalMembers.
        """
        pass

    def test_portals_id_portal_members_fk_get(self):
        """
        Test case for portals_id_portal_members_fk_get

        Find a related item by id for portalMembers.
        """
        pass

    def test_portals_id_portal_members_fk_put(self):
        """
        Test case for portals_id_portal_members_fk_put

        Update a related item by id for portalMembers.
        """
        pass

    def test_portals_id_portal_members_get(self):
        """
        Test case for portals_id_portal_members_get

        Queries portalMembers of Portal.
        """
        pass

    def test_portals_id_portal_members_post(self):
        """
        Test case for portals_id_portal_members_post

        Creates a new instance in portalMembers of this model.
        """
        pass

    def test_portals_id_put(self):
        """
        Test case for portals_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_portals_id_replace_post(self):
        """
        Test case for portals_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_portals_id_team_get(self):
        """
        Test case for portals_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_portals_id_template_folders_count_get(self):
        """
        Test case for portals_id_template_folders_count_get

        Counts templateFolders of Portal.
        """
        pass

    def test_portals_id_template_folders_delete(self):
        """
        Test case for portals_id_template_folders_delete

        Deletes all templateFolders of this model.
        """
        pass

    def test_portals_id_template_folders_fk_delete(self):
        """
        Test case for portals_id_template_folders_fk_delete

        Delete a related item by id for templateFolders.
        """
        pass

    def test_portals_id_template_folders_fk_get(self):
        """
        Test case for portals_id_template_folders_fk_get

        Find a related item by id for templateFolders.
        """
        pass

    def test_portals_id_template_folders_fk_put(self):
        """
        Test case for portals_id_template_folders_fk_put

        Update a related item by id for templateFolders.
        """
        pass

    def test_portals_id_template_folders_get(self):
        """
        Test case for portals_id_template_folders_get

        Queries templateFolders of Portal.
        """
        pass

    def test_portals_id_template_folders_nk_templates_fk_rel_delete(self):
        """
        Test case for portals_id_template_folders_nk_templates_fk_rel_delete

        Unlink folder with Template and Portal
        """
        pass

    def test_portals_id_template_folders_nk_templates_fk_rel_put(self):
        """
        Test case for portals_id_template_folders_nk_templates_fk_rel_put

        Link folder with Template and Portal
        """
        pass

    def test_portals_id_template_folders_post(self):
        """
        Test case for portals_id_template_folders_post

        Creates a new instance in templateFolders of this model.
        """
        pass

    def test_portals_id_template_folders_root_templates_get(self):
        """
        Test case for portals_id_template_folders_root_templates_get

        List templates on root folder
        """
        pass

    def test_portals_id_template_rels_count_get(self):
        """
        Test case for portals_id_template_rels_count_get

        Counts templateRels of Portal.
        """
        pass

    def test_portals_id_template_rels_delete(self):
        """
        Test case for portals_id_template_rels_delete

        Deletes all templateRels of this model.
        """
        pass

    def test_portals_id_template_rels_fk_delete(self):
        """
        Test case for portals_id_template_rels_fk_delete

        Delete a related item by id for templateRels.
        """
        pass

    def test_portals_id_template_rels_fk_get(self):
        """
        Test case for portals_id_template_rels_fk_get

        Find a related item by id for templateRels.
        """
        pass

    def test_portals_id_template_rels_fk_put(self):
        """
        Test case for portals_id_template_rels_fk_put

        Update a related item by id for templateRels.
        """
        pass

    def test_portals_id_template_rels_get(self):
        """
        Test case for portals_id_template_rels_get

        Queries templateRels of Portal.
        """
        pass

    def test_portals_id_template_rels_post(self):
        """
        Test case for portals_id_template_rels_post

        Creates a new instance in templateRels of this model.
        """
        pass

    def test_portals_id_templates_count_get(self):
        """
        Test case for portals_id_templates_count_get

        Counts templates of Portal.
        """
        pass

    def test_portals_id_templates_delete(self):
        """
        Test case for portals_id_templates_delete

        Deletes all templates of this model.
        """
        pass

    def test_portals_id_templates_fk_delete(self):
        """
        Test case for portals_id_templates_fk_delete

        Delete a related item by id for templates.
        """
        pass

    def test_portals_id_templates_fk_designs_generate_bulk_post(self):
        """
        Test case for portals_id_templates_fk_designs_generate_bulk_post

        Generate Design from Template
        """
        pass

    def test_portals_id_templates_fk_designs_generate_post(self):
        """
        Test case for portals_id_templates_fk_designs_generate_post

        Generate Design from Template
        """
        pass

    def test_portals_id_templates_fk_get(self):
        """
        Test case for portals_id_templates_fk_get

        Find a related item by id for templates.
        """
        pass

    def test_portals_id_templates_fk_put(self):
        """
        Test case for portals_id_templates_fk_put

        Update a related item by id for templates.
        """
        pass

    def test_portals_id_templates_get(self):
        """
        Test case for portals_id_templates_get

        Queries templates of Portal.
        """
        pass

    def test_portals_id_templates_post(self):
        """
        Test case for portals_id_templates_post

        Creates a new instance in templates of this model.
        """
        pass

    def test_portals_id_templates_rel_fk_delete(self):
        """
        Test case for portals_id_templates_rel_fk_delete

        Remove the templates relation to an item by id.
        """
        pass

    def test_portals_id_templates_rel_fk_head(self):
        """
        Test case for portals_id_templates_rel_fk_head

        Check the existence of templates relation to an item by id.
        """
        pass

    def test_portals_id_templates_rel_fk_put(self):
        """
        Test case for portals_id_templates_rel_fk_put

        Add a related item by id for templates.
        """
        pass

    def test_portals_patch(self):
        """
        Test case for portals_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_portals_post(self):
        """
        Test case for portals_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_portals_put(self):
        """
        Test case for portals_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_portals_replace_or_create_post(self):
        """
        Test case for portals_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_portals_update_post(self):
        """
        Test case for portals_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_portals_upsert_with_where_post(self):
        """
        Test case for portals_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
