# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.6
    
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
from TweakApi.apis.invitation_ticket_api import InvitationTicketApi


class TestInvitationTicketApi(unittest.TestCase):
    """ InvitationTicketApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.invitation_ticket_api.InvitationTicketApi()

    def tearDown(self):
        pass

    def test_invitation_tickets_change_stream_get(self):
        """
        Test case for invitation_tickets_change_stream_get

        Create a change stream.
        """
        pass

    def test_invitation_tickets_change_stream_post(self):
        """
        Test case for invitation_tickets_change_stream_post

        Create a change stream.
        """
        pass

    def test_invitation_tickets_count_get(self):
        """
        Test case for invitation_tickets_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_invitation_tickets_find_one_get(self):
        """
        Test case for invitation_tickets_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_invitation_tickets_get(self):
        """
        Test case for invitation_tickets_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_invitation_tickets_id_delete(self):
        """
        Test case for invitation_tickets_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_invitation_tickets_id_exists_get(self):
        """
        Test case for invitation_tickets_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_invitation_tickets_id_get(self):
        """
        Test case for invitation_tickets_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_invitation_tickets_id_head(self):
        """
        Test case for invitation_tickets_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_invitation_tickets_id_invitee_get(self):
        """
        Test case for invitation_tickets_id_invitee_get

        Fetches belongsTo relation invitee.
        """
        pass

    def test_invitation_tickets_id_inviter_get(self):
        """
        Test case for invitation_tickets_id_inviter_get

        Fetches belongsTo relation inviter.
        """
        pass

    def test_invitation_tickets_id_patch(self):
        """
        Test case for invitation_tickets_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_invitation_tickets_id_put(self):
        """
        Test case for invitation_tickets_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_invitation_tickets_id_replace_post(self):
        """
        Test case for invitation_tickets_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_invitation_tickets_id_target_design_get(self):
        """
        Test case for invitation_tickets_id_target_design_get

        Fetches belongsTo relation targetDesign.
        """
        pass

    def test_invitation_tickets_id_target_design_member_get(self):
        """
        Test case for invitation_tickets_id_target_design_member_get

        Fetches belongsTo relation targetDesignMember.
        """
        pass

    def test_invitation_tickets_id_target_image_folder_get(self):
        """
        Test case for invitation_tickets_id_target_image_folder_get

        Fetches belongsTo relation targetImageFolder.
        """
        pass

    def test_invitation_tickets_id_target_image_folder_member_get(self):
        """
        Test case for invitation_tickets_id_target_image_folder_member_get

        Fetches belongsTo relation targetImageFolderMember.
        """
        pass

    def test_invitation_tickets_id_target_portal_get(self):
        """
        Test case for invitation_tickets_id_target_portal_get

        Fetches belongsTo relation targetPortal.
        """
        pass

    def test_invitation_tickets_id_target_portal_member_get(self):
        """
        Test case for invitation_tickets_id_target_portal_member_get

        Fetches belongsTo relation targetPortalMember.
        """
        pass

    def test_invitation_tickets_id_target_team_get(self):
        """
        Test case for invitation_tickets_id_target_team_get

        Fetches belongsTo relation targetTeam.
        """
        pass

    def test_invitation_tickets_id_target_team_member_get(self):
        """
        Test case for invitation_tickets_id_target_team_member_get

        Fetches belongsTo relation targetTeamMember.
        """
        pass

    def test_invitation_tickets_id_target_template_get(self):
        """
        Test case for invitation_tickets_id_target_template_get

        Fetches belongsTo relation targetTemplate.
        """
        pass

    def test_invitation_tickets_id_target_template_member_get(self):
        """
        Test case for invitation_tickets_id_target_template_member_get

        Fetches belongsTo relation targetTemplateMember.
        """
        pass

    def test_invitation_tickets_patch(self):
        """
        Test case for invitation_tickets_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_invitation_tickets_post(self):
        """
        Test case for invitation_tickets_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_invitation_tickets_put(self):
        """
        Test case for invitation_tickets_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_invitation_tickets_replace_or_create_post(self):
        """
        Test case for invitation_tickets_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_invitation_tickets_update_post(self):
        """
        Test case for invitation_tickets_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_invitation_tickets_upsert_with_where_post(self):
        """
        Test case for invitation_tickets_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
