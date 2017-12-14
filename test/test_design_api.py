# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-alpha.15
    
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
from TweakApi.apis.design_api import DesignApi


class TestDesignApi(unittest.TestCase):
    """ DesignApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.design_api.DesignApi()

    def tearDown(self):
        pass

    def test_designs_change_stream_get(self):
        """
        Test case for designs_change_stream_get

        Create a change stream.
        """
        pass

    def test_designs_change_stream_post(self):
        """
        Test case for designs_change_stream_post

        Create a change stream.
        """
        pass

    def test_designs_count_get(self):
        """
        Test case for designs_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_designs_find_one_get(self):
        """
        Test case for designs_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_designs_get(self):
        """
        Test case for designs_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_designs_id_approve_post(self):
        """
        Test case for designs_id_approve_post

        Approve design
        """
        pass

    def test_designs_id_assignee_get(self):
        """
        Test case for designs_id_assignee_get

        Fetches belongsTo relation assignee.
        """
        pass

    def test_designs_id_commenters_count_get(self):
        """
        Test case for designs_id_commenters_count_get

        Counts commenters of Design.
        """
        pass

    def test_designs_id_commenters_delete(self):
        """
        Test case for designs_id_commenters_delete

        Deletes all commenters of this model.
        """
        pass

    def test_designs_id_commenters_fk_delete(self):
        """
        Test case for designs_id_commenters_fk_delete

        Delete a related item by id for commenters.
        """
        pass

    def test_designs_id_commenters_fk_get(self):
        """
        Test case for designs_id_commenters_fk_get

        Find a related item by id for commenters.
        """
        pass

    def test_designs_id_commenters_fk_put(self):
        """
        Test case for designs_id_commenters_fk_put

        Update a related item by id for commenters.
        """
        pass

    def test_designs_id_commenters_get(self):
        """
        Test case for designs_id_commenters_get

        Queries commenters of Design.
        """
        pass

    def test_designs_id_commenters_post(self):
        """
        Test case for designs_id_commenters_post

        Creates a new instance in commenters of this model.
        """
        pass

    def test_designs_id_commenters_rel_fk_delete(self):
        """
        Test case for designs_id_commenters_rel_fk_delete

        Remove the commenters relation to an item by id.
        """
        pass

    def test_designs_id_commenters_rel_fk_head(self):
        """
        Test case for designs_id_commenters_rel_fk_head

        Check the existence of commenters relation to an item by id.
        """
        pass

    def test_designs_id_commenters_rel_fk_put(self):
        """
        Test case for designs_id_commenters_rel_fk_put

        Add a related item by id for commenters.
        """
        pass

    def test_designs_id_comments_count_get(self):
        """
        Test case for designs_id_comments_count_get

        Counts comments of Design.
        """
        pass

    def test_designs_id_comments_delete(self):
        """
        Test case for designs_id_comments_delete

        Deletes all comments of this model.
        """
        pass

    def test_designs_id_comments_fk_delete(self):
        """
        Test case for designs_id_comments_fk_delete

        Delete a related item by id for comments.
        """
        pass

    def test_designs_id_comments_fk_get(self):
        """
        Test case for designs_id_comments_fk_get

        Find a related item by id for comments.
        """
        pass

    def test_designs_id_comments_fk_put(self):
        """
        Test case for designs_id_comments_fk_put

        Update a related item by id for comments.
        """
        pass

    def test_designs_id_comments_get(self):
        """
        Test case for designs_id_comments_get

        Queries comments of Design.
        """
        pass

    def test_designs_id_comments_nk_commenter_get(self):
        """
        Test case for designs_id_comments_nk_commenter_get

        Fetches belongsTo relation commenter.
        """
        pass

    def test_designs_id_comments_nk_design_get(self):
        """
        Test case for designs_id_comments_nk_design_get

        Fetches belongsTo relation design.
        """
        pass

    def test_designs_id_comments_nk_replies_count_get(self):
        """
        Test case for designs_id_comments_nk_replies_count_get

        Counts replies of DesignComment.
        """
        pass

    def test_designs_id_comments_nk_replies_delete(self):
        """
        Test case for designs_id_comments_nk_replies_delete

        Deletes all replies of this model.
        """
        pass

    def test_designs_id_comments_nk_replies_fk_delete(self):
        """
        Test case for designs_id_comments_nk_replies_fk_delete

        Delete a related item by id for replies.
        """
        pass

    def test_designs_id_comments_nk_replies_fk_get(self):
        """
        Test case for designs_id_comments_nk_replies_fk_get

        Find a related item by id for replies.
        """
        pass

    def test_designs_id_comments_nk_replies_fk_put(self):
        """
        Test case for designs_id_comments_nk_replies_fk_put

        Update a related item by id for replies.
        """
        pass

    def test_designs_id_comments_nk_replies_get(self):
        """
        Test case for designs_id_comments_nk_replies_get

        Queries replies of DesignComment.
        """
        pass

    def test_designs_id_comments_nk_replies_post(self):
        """
        Test case for designs_id_comments_nk_replies_post

        Creates a new instance in replies of this model.
        """
        pass

    def test_designs_id_comments_nk_reply_of_get(self):
        """
        Test case for designs_id_comments_nk_reply_of_get

        Fetches belongsTo relation replyOf.
        """
        pass

    def test_designs_id_comments_post(self):
        """
        Test case for designs_id_comments_post

        Creates a new instance in comments of this model.
        """
        pass

    def test_designs_id_delete(self):
        """
        Test case for designs_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_designs_id_design_members_count_get(self):
        """
        Test case for designs_id_design_members_count_get

        Counts designMembers of Design.
        """
        pass

    def test_designs_id_design_members_delete(self):
        """
        Test case for designs_id_design_members_delete

        Deletes all designMembers of this model.
        """
        pass

    def test_designs_id_design_members_fk_delete(self):
        """
        Test case for designs_id_design_members_fk_delete

        Delete a related item by id for designMembers.
        """
        pass

    def test_designs_id_design_members_fk_get(self):
        """
        Test case for designs_id_design_members_fk_get

        Find a related item by id for designMembers.
        """
        pass

    def test_designs_id_design_members_fk_put(self):
        """
        Test case for designs_id_design_members_fk_put

        Update a related item by id for designMembers.
        """
        pass

    def test_designs_id_design_members_get(self):
        """
        Test case for designs_id_design_members_get

        Queries designMembers of Design.
        """
        pass

    def test_designs_id_design_members_post(self):
        """
        Test case for designs_id_design_members_post

        Creates a new instance in designMembers of this model.
        """
        pass

    def test_designs_id_dynamic_data_get(self):
        """
        Test case for designs_id_dynamic_data_get

        Fetches belongsTo relation dynamicData.
        """
        pass

    def test_designs_id_exists_get(self):
        """
        Test case for designs_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_designs_id_exports_count_get(self):
        """
        Test case for designs_id_exports_count_get

        Counts exports of Design.
        """
        pass

    def test_designs_id_exports_delete(self):
        """
        Test case for designs_id_exports_delete

        Deletes all exports of this model.
        """
        pass

    def test_designs_id_exports_fk_delete(self):
        """
        Test case for designs_id_exports_fk_delete

        Delete a related item by id for exports.
        """
        pass

    def test_designs_id_exports_fk_get(self):
        """
        Test case for designs_id_exports_fk_get

        Find a related item by id for exports.
        """
        pass

    def test_designs_id_exports_fk_put(self):
        """
        Test case for designs_id_exports_fk_put

        Update a related item by id for exports.
        """
        pass

    def test_designs_id_exports_get(self):
        """
        Test case for designs_id_exports_get

        Queries exports of Design.
        """
        pass

    def test_designs_id_exports_post(self):
        """
        Test case for designs_id_exports_post

        Creates a new instance in exports of this model.
        """
        pass

    def test_designs_id_folder_get(self):
        """
        Test case for designs_id_folder_get

        Fetches belongsTo relation folder.
        """
        pass

    def test_designs_id_get(self):
        """
        Test case for designs_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_designs_id_head(self):
        """
        Test case for designs_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_designs_id_members_count_get(self):
        """
        Test case for designs_id_members_count_get

        Counts members of Design.
        """
        pass

    def test_designs_id_members_delete(self):
        """
        Test case for designs_id_members_delete

        Deletes all members of this model.
        """
        pass

    def test_designs_id_members_fk_delete(self):
        """
        Test case for designs_id_members_fk_delete

        Delete a related item by id for members.
        """
        pass

    def test_designs_id_members_fk_get(self):
        """
        Test case for designs_id_members_fk_get

        Find a related item by id for members.
        """
        pass

    def test_designs_id_members_fk_put(self):
        """
        Test case for designs_id_members_fk_put

        Update a related item by id for members.
        """
        pass

    def test_designs_id_members_get(self):
        """
        Test case for designs_id_members_get

        Queries members of Design.
        """
        pass

    def test_designs_id_members_post(self):
        """
        Test case for designs_id_members_post

        Creates a new instance in members of this model.
        """
        pass

    def test_designs_id_members_rel_fk_delete(self):
        """
        Test case for designs_id_members_rel_fk_delete

        Remove the members relation to an item by id.
        """
        pass

    def test_designs_id_members_rel_fk_head(self):
        """
        Test case for designs_id_members_rel_fk_head

        Check the existence of members relation to an item by id.
        """
        pass

    def test_designs_id_members_rel_fk_put(self):
        """
        Test case for designs_id_members_rel_fk_put

        Add a related item by id for members.
        """
        pass

    def test_designs_id_patch(self):
        """
        Test case for designs_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_designs_id_permission_delete(self):
        """
        Test case for designs_id_permission_delete

        Deletes permission of this model.
        """
        pass

    def test_designs_id_permission_get(self):
        """
        Test case for designs_id_permission_get

        Fetches hasOne relation permission.
        """
        pass

    def test_designs_id_permission_post(self):
        """
        Test case for designs_id_permission_post

        Creates a new instance in permission of this model.
        """
        pass

    def test_designs_id_permission_put(self):
        """
        Test case for designs_id_permission_put

        Update permission of this model.
        """
        pass

    def test_designs_id_portal_get(self):
        """
        Test case for designs_id_portal_get

        Fetches belongsTo relation portal.
        """
        pass

    def test_designs_id_put(self):
        """
        Test case for designs_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_designs_id_reject_post(self):
        """
        Test case for designs_id_reject_post

        Reject design
        """
        pass

    def test_designs_id_rejection_comment_get(self):
        """
        Test case for designs_id_rejection_comment_get

        Fetches belongsTo relation rejectionComment.
        """
        pass

    def test_designs_id_replace_post(self):
        """
        Test case for designs_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_designs_id_requester_get(self):
        """
        Test case for designs_id_requester_get

        Fetches belongsTo relation requester.
        """
        pass

    def test_designs_id_reviewer_get(self):
        """
        Test case for designs_id_reviewer_get

        Fetches belongsTo relation reviewer.
        """
        pass

    def test_designs_id_submit_post(self):
        """
        Test case for designs_id_submit_post

        Submit design for approval
        """
        pass

    def test_designs_id_tags_count_get(self):
        """
        Test case for designs_id_tags_count_get

        Counts tags of Design.
        """
        pass

    def test_designs_id_tags_delete(self):
        """
        Test case for designs_id_tags_delete

        Deletes all tags of this model.
        """
        pass

    def test_designs_id_tags_fk_delete(self):
        """
        Test case for designs_id_tags_fk_delete

        Delete a related item by id for tags.
        """
        pass

    def test_designs_id_tags_fk_get(self):
        """
        Test case for designs_id_tags_fk_get

        Find a related item by id for tags.
        """
        pass

    def test_designs_id_tags_fk_put(self):
        """
        Test case for designs_id_tags_fk_put

        Update a related item by id for tags.
        """
        pass

    def test_designs_id_tags_get(self):
        """
        Test case for designs_id_tags_get

        Queries tags of Design.
        """
        pass

    def test_designs_id_tags_post(self):
        """
        Test case for designs_id_tags_post

        Creates a new instance in tags of this model.
        """
        pass

    def test_designs_id_tags_rel_fk_delete(self):
        """
        Test case for designs_id_tags_rel_fk_delete

        Remove the tags relation to an item by id.
        """
        pass

    def test_designs_id_tags_rel_fk_head(self):
        """
        Test case for designs_id_tags_rel_fk_head

        Check the existence of tags relation to an item by id.
        """
        pass

    def test_designs_id_tags_rel_fk_put(self):
        """
        Test case for designs_id_tags_rel_fk_put

        Add a related item by id for tags.
        """
        pass

    def test_designs_id_team_get(self):
        """
        Test case for designs_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_designs_id_template_get(self):
        """
        Test case for designs_id_template_get

        Fetches belongsTo relation template.
        """
        pass

    def test_designs_patch(self):
        """
        Test case for designs_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_designs_post(self):
        """
        Test case for designs_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_designs_put(self):
        """
        Test case for designs_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_designs_replace_or_create_post(self):
        """
        Test case for designs_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_designs_update_post(self):
        """
        Test case for designs_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_designs_upsert_with_where_post(self):
        """
        Test case for designs_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
