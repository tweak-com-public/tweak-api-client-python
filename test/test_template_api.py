# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3
    
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
from TweakApi.apis.template_api import TemplateApi


class TestTemplateApi(unittest.TestCase):
    """ TemplateApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.template_api.TemplateApi()

    def tearDown(self):
        pass

    def test_templates_change_stream_get(self):
        """
        Test case for templates_change_stream_get

        Create a change stream.
        """
        pass

    def test_templates_change_stream_post(self):
        """
        Test case for templates_change_stream_post

        Create a change stream.
        """
        pass

    def test_templates_count_get(self):
        """
        Test case for templates_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_templates_find_one_get(self):
        """
        Test case for templates_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_templates_get(self):
        """
        Test case for templates_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_templates_id_delete(self):
        """
        Test case for templates_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_templates_id_designs_count_get(self):
        """
        Test case for templates_id_designs_count_get

        Counts designs of Template.
        """
        pass

    def test_templates_id_designs_delete(self):
        """
        Test case for templates_id_designs_delete

        Deletes all designs of this model.
        """
        pass

    def test_templates_id_designs_fk_delete(self):
        """
        Test case for templates_id_designs_fk_delete

        Delete a related item by id for designs.
        """
        pass

    def test_templates_id_designs_fk_get(self):
        """
        Test case for templates_id_designs_fk_get

        Find a related item by id for designs.
        """
        pass

    def test_templates_id_designs_fk_put(self):
        """
        Test case for templates_id_designs_fk_put

        Update a related item by id for designs.
        """
        pass

    def test_templates_id_designs_generate_post(self):
        """
        Test case for templates_id_designs_generate_post

        Generate design from template
        """
        pass

    def test_templates_id_designs_get(self):
        """
        Test case for templates_id_designs_get

        Queries designs of Template.
        """
        pass

    def test_templates_id_designs_post(self):
        """
        Test case for templates_id_designs_post

        Creates a new instance in designs of this model.
        """
        pass

    def test_templates_id_exists_get(self):
        """
        Test case for templates_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_templates_id_get(self):
        """
        Test case for templates_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_templates_id_head(self):
        """
        Test case for templates_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_templates_id_invitation_tickets_fk_delete(self):
        """
        Test case for templates_id_invitation_tickets_fk_delete

        Delete InvitationTickets for this Template
        """
        pass

    def test_templates_id_invitation_tickets_fk_get(self):
        """
        Test case for templates_id_invitation_tickets_fk_get

        Get InvitationTicket by Id for this Template
        """
        pass

    def test_templates_id_invitation_tickets_get(self):
        """
        Test case for templates_id_invitation_tickets_get

        List InvitationTickets for this Template
        """
        pass

    def test_templates_id_members_count_get(self):
        """
        Test case for templates_id_members_count_get

        Counts members of Template.
        """
        pass

    def test_templates_id_members_delete(self):
        """
        Test case for templates_id_members_delete

        Deletes all members of this model.
        """
        pass

    def test_templates_id_members_fk_delete(self):
        """
        Test case for templates_id_members_fk_delete

        Delete a related item by id for members.
        """
        pass

    def test_templates_id_members_fk_get(self):
        """
        Test case for templates_id_members_fk_get

        Find a related item by id for members.
        """
        pass

    def test_templates_id_members_fk_put(self):
        """
        Test case for templates_id_members_fk_put

        Update a related item by id for members.
        """
        pass

    def test_templates_id_members_get(self):
        """
        Test case for templates_id_members_get

        Queries members of Template.
        """
        pass

    def test_templates_id_members_post(self):
        """
        Test case for templates_id_members_post

        Creates a new instance in members of this model.
        """
        pass

    def test_templates_id_members_rel_fk_delete(self):
        """
        Test case for templates_id_members_rel_fk_delete

        Remove the members relation to an item by id.
        """
        pass

    def test_templates_id_members_rel_fk_head(self):
        """
        Test case for templates_id_members_rel_fk_head

        Check the existence of members relation to an item by id.
        """
        pass

    def test_templates_id_members_rel_fk_put(self):
        """
        Test case for templates_id_members_rel_fk_put

        Add a related item by id for members.
        """
        pass

    def test_templates_id_patch(self):
        """
        Test case for templates_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_templates_id_permission_delete(self):
        """
        Test case for templates_id_permission_delete

        Deletes permission of this model.
        """
        pass

    def test_templates_id_permission_get(self):
        """
        Test case for templates_id_permission_get

        Fetches hasOne relation permission.
        """
        pass

    def test_templates_id_permission_post(self):
        """
        Test case for templates_id_permission_post

        Creates a new instance in permission of this model.
        """
        pass

    def test_templates_id_permission_put(self):
        """
        Test case for templates_id_permission_put

        Update permission of this model.
        """
        pass

    def test_templates_id_portal_folders_count_get(self):
        """
        Test case for templates_id_portal_folders_count_get

        Counts portalFolders of Template.
        """
        pass

    def test_templates_id_portal_folders_delete(self):
        """
        Test case for templates_id_portal_folders_delete

        Deletes all portalFolders of this model.
        """
        pass

    def test_templates_id_portal_folders_fk_delete(self):
        """
        Test case for templates_id_portal_folders_fk_delete

        Delete a related item by id for portalFolders.
        """
        pass

    def test_templates_id_portal_folders_fk_get(self):
        """
        Test case for templates_id_portal_folders_fk_get

        Find a related item by id for portalFolders.
        """
        pass

    def test_templates_id_portal_folders_fk_put(self):
        """
        Test case for templates_id_portal_folders_fk_put

        Update a related item by id for portalFolders.
        """
        pass

    def test_templates_id_portal_folders_get(self):
        """
        Test case for templates_id_portal_folders_get

        Queries portalFolders of Template.
        """
        pass

    def test_templates_id_portal_folders_post(self):
        """
        Test case for templates_id_portal_folders_post

        Creates a new instance in portalFolders of this model.
        """
        pass

    def test_templates_id_portal_folders_rel_fk_delete(self):
        """
        Test case for templates_id_portal_folders_rel_fk_delete

        Remove the portalFolders relation to an item by id.
        """
        pass

    def test_templates_id_portal_folders_rel_fk_head(self):
        """
        Test case for templates_id_portal_folders_rel_fk_head

        Check the existence of portalFolders relation to an item by id.
        """
        pass

    def test_templates_id_portal_folders_rel_fk_put(self):
        """
        Test case for templates_id_portal_folders_rel_fk_put

        Add a related item by id for portalFolders.
        """
        pass

    def test_templates_id_portals_count_get(self):
        """
        Test case for templates_id_portals_count_get

        Counts portals of Template.
        """
        pass

    def test_templates_id_portals_delete(self):
        """
        Test case for templates_id_portals_delete

        Deletes all portals of this model.
        """
        pass

    def test_templates_id_portals_fk_delete(self):
        """
        Test case for templates_id_portals_fk_delete

        Delete a related item by id for portals.
        """
        pass

    def test_templates_id_portals_fk_get(self):
        """
        Test case for templates_id_portals_fk_get

        Find a related item by id for portals.
        """
        pass

    def test_templates_id_portals_fk_put(self):
        """
        Test case for templates_id_portals_fk_put

        Update a related item by id for portals.
        """
        pass

    def test_templates_id_portals_get(self):
        """
        Test case for templates_id_portals_get

        Queries portals of Template.
        """
        pass

    def test_templates_id_portals_post(self):
        """
        Test case for templates_id_portals_post

        Creates a new instance in portals of this model.
        """
        pass

    def test_templates_id_portals_rel_fk_delete(self):
        """
        Test case for templates_id_portals_rel_fk_delete

        Remove the portals relation to an item by id.
        """
        pass

    def test_templates_id_portals_rel_fk_head(self):
        """
        Test case for templates_id_portals_rel_fk_head

        Check the existence of portals relation to an item by id.
        """
        pass

    def test_templates_id_portals_rel_fk_put(self):
        """
        Test case for templates_id_portals_rel_fk_put

        Add a related item by id for portals.
        """
        pass

    def test_templates_id_put(self):
        """
        Test case for templates_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_templates_id_replace_post(self):
        """
        Test case for templates_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_templates_id_tags_count_get(self):
        """
        Test case for templates_id_tags_count_get

        Counts tags of Template.
        """
        pass

    def test_templates_id_tags_delete(self):
        """
        Test case for templates_id_tags_delete

        Deletes all tags of this model.
        """
        pass

    def test_templates_id_tags_fk_delete(self):
        """
        Test case for templates_id_tags_fk_delete

        Delete a related item by id for tags.
        """
        pass

    def test_templates_id_tags_fk_get(self):
        """
        Test case for templates_id_tags_fk_get

        Find a related item by id for tags.
        """
        pass

    def test_templates_id_tags_fk_put(self):
        """
        Test case for templates_id_tags_fk_put

        Update a related item by id for tags.
        """
        pass

    def test_templates_id_tags_get(self):
        """
        Test case for templates_id_tags_get

        Queries tags of Template.
        """
        pass

    def test_templates_id_tags_post(self):
        """
        Test case for templates_id_tags_post

        Creates a new instance in tags of this model.
        """
        pass

    def test_templates_id_tags_rel_fk_delete(self):
        """
        Test case for templates_id_tags_rel_fk_delete

        Remove the tags relation to an item by id.
        """
        pass

    def test_templates_id_tags_rel_fk_head(self):
        """
        Test case for templates_id_tags_rel_fk_head

        Check the existence of tags relation to an item by id.
        """
        pass

    def test_templates_id_tags_rel_fk_put(self):
        """
        Test case for templates_id_tags_rel_fk_put

        Add a related item by id for tags.
        """
        pass

    def test_templates_id_team_folder_get(self):
        """
        Test case for templates_id_team_folder_get

        Fetches belongsTo relation teamFolder.
        """
        pass

    def test_templates_id_team_get(self):
        """
        Test case for templates_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_templates_id_template_members_count_get(self):
        """
        Test case for templates_id_template_members_count_get

        Counts templateMembers of Template.
        """
        pass

    def test_templates_id_template_members_delete(self):
        """
        Test case for templates_id_template_members_delete

        Deletes all templateMembers of this model.
        """
        pass

    def test_templates_id_template_members_fk_delete(self):
        """
        Test case for templates_id_template_members_fk_delete

        Delete a related item by id for templateMembers.
        """
        pass

    def test_templates_id_template_members_fk_get(self):
        """
        Test case for templates_id_template_members_fk_get

        Find a related item by id for templateMembers.
        """
        pass

    def test_templates_id_template_members_fk_put(self):
        """
        Test case for templates_id_template_members_fk_put

        Update a related item by id for templateMembers.
        """
        pass

    def test_templates_id_template_members_get(self):
        """
        Test case for templates_id_template_members_get

        Queries templateMembers of Template.
        """
        pass

    def test_templates_id_template_members_post(self):
        """
        Test case for templates_id_template_members_post

        Creates a new instance in templateMembers of this model.
        """
        pass

    def test_templates_id_uploader_get(self):
        """
        Test case for templates_id_uploader_get

        Fetches belongsTo relation uploader.
        """
        pass

    def test_templates_id_url_review_get(self):
        """
        Test case for templates_id_url_review_get

        Get URL to review a template
        """
        pass

    def test_templates_id_workflow_get(self):
        """
        Test case for templates_id_workflow_get

        Fetches belongsTo relation workflow.
        """
        pass

    def test_templates_patch(self):
        """
        Test case for templates_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_templates_post(self):
        """
        Test case for templates_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_templates_put(self):
        """
        Test case for templates_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_templates_replace_or_create_post(self):
        """
        Test case for templates_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_templates_update_post(self):
        """
        Test case for templates_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_templates_upsert_with_where_post(self):
        """
        Test case for templates_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
