# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.4-alpha.6
    
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
from TweakApi.apis.image_folder_api import ImageFolderApi


class TestImageFolderApi(unittest.TestCase):
    """ ImageFolderApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.image_folder_api.ImageFolderApi()

    def tearDown(self):
        pass

    def test_image_folders_change_stream_get(self):
        """
        Test case for image_folders_change_stream_get

        Create a change stream.
        """
        pass

    def test_image_folders_change_stream_post(self):
        """
        Test case for image_folders_change_stream_post

        Create a change stream.
        """
        pass

    def test_image_folders_count_get(self):
        """
        Test case for image_folders_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_image_folders_find_one_get(self):
        """
        Test case for image_folders_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_image_folders_get(self):
        """
        Test case for image_folders_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_image_folders_id_children_count_get(self):
        """
        Test case for image_folders_id_children_count_get

        Counts children of ImageFolder.
        """
        pass

    def test_image_folders_id_children_delete(self):
        """
        Test case for image_folders_id_children_delete

        Deletes all children of this model.
        """
        pass

    def test_image_folders_id_children_fk_delete(self):
        """
        Test case for image_folders_id_children_fk_delete

        Delete a related item by id for children.
        """
        pass

    def test_image_folders_id_children_fk_get(self):
        """
        Test case for image_folders_id_children_fk_get

        Find a related item by id for children.
        """
        pass

    def test_image_folders_id_children_fk_put(self):
        """
        Test case for image_folders_id_children_fk_put

        Update a related item by id for children.
        """
        pass

    def test_image_folders_id_children_get(self):
        """
        Test case for image_folders_id_children_get

        Queries children of ImageFolder.
        """
        pass

    def test_image_folders_id_children_post(self):
        """
        Test case for image_folders_id_children_post

        Creates a new instance in children of this model.
        """
        pass

    def test_image_folders_id_delete(self):
        """
        Test case for image_folders_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_image_folders_id_exists_get(self):
        """
        Test case for image_folders_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_image_folders_id_folder_members_count_get(self):
        """
        Test case for image_folders_id_folder_members_count_get

        Counts folderMembers of ImageFolder.
        """
        pass

    def test_image_folders_id_folder_members_delete(self):
        """
        Test case for image_folders_id_folder_members_delete

        Deletes all folderMembers of this model.
        """
        pass

    def test_image_folders_id_folder_members_fk_delete(self):
        """
        Test case for image_folders_id_folder_members_fk_delete

        Delete a related item by id for folderMembers.
        """
        pass

    def test_image_folders_id_folder_members_fk_get(self):
        """
        Test case for image_folders_id_folder_members_fk_get

        Find a related item by id for folderMembers.
        """
        pass

    def test_image_folders_id_folder_members_fk_put(self):
        """
        Test case for image_folders_id_folder_members_fk_put

        Update a related item by id for folderMembers.
        """
        pass

    def test_image_folders_id_folder_members_get(self):
        """
        Test case for image_folders_id_folder_members_get

        Queries folderMembers of ImageFolder.
        """
        pass

    def test_image_folders_id_folder_members_post(self):
        """
        Test case for image_folders_id_folder_members_post

        Creates a new instance in folderMembers of this model.
        """
        pass

    def test_image_folders_id_get(self):
        """
        Test case for image_folders_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_image_folders_id_head(self):
        """
        Test case for image_folders_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_image_folders_id_images_count_get(self):
        """
        Test case for image_folders_id_images_count_get

        Counts images of ImageFolder.
        """
        pass

    def test_image_folders_id_images_delete(self):
        """
        Test case for image_folders_id_images_delete

        Deletes all images of this model.
        """
        pass

    def test_image_folders_id_images_fk_delete(self):
        """
        Test case for image_folders_id_images_fk_delete

        Delete a related item by id for images.
        """
        pass

    def test_image_folders_id_images_fk_get(self):
        """
        Test case for image_folders_id_images_fk_get

        Find a related item by id for images.
        """
        pass

    def test_image_folders_id_images_fk_put(self):
        """
        Test case for image_folders_id_images_fk_put

        Update a related item by id for images.
        """
        pass

    def test_image_folders_id_images_get(self):
        """
        Test case for image_folders_id_images_get

        Queries images of ImageFolder.
        """
        pass

    def test_image_folders_id_images_post(self):
        """
        Test case for image_folders_id_images_post

        Creates a new instance in images of this model.
        """
        pass

    def test_image_folders_id_invitation_tickets_fk_delete(self):
        """
        Test case for image_folders_id_invitation_tickets_fk_delete

        Delete InvitationTickets for this ImageFolder
        """
        pass

    def test_image_folders_id_invitation_tickets_fk_get(self):
        """
        Test case for image_folders_id_invitation_tickets_fk_get

        Get InvitationTicket by Id for this ImageFolder
        """
        pass

    def test_image_folders_id_invitation_tickets_get(self):
        """
        Test case for image_folders_id_invitation_tickets_get

        List InvitationTickets for this ImageFolder
        """
        pass

    def test_image_folders_id_members_count_get(self):
        """
        Test case for image_folders_id_members_count_get

        Counts members of ImageFolder.
        """
        pass

    def test_image_folders_id_members_delete(self):
        """
        Test case for image_folders_id_members_delete

        Deletes all members of this model.
        """
        pass

    def test_image_folders_id_members_fk_delete(self):
        """
        Test case for image_folders_id_members_fk_delete

        Delete a related item by id for members.
        """
        pass

    def test_image_folders_id_members_fk_get(self):
        """
        Test case for image_folders_id_members_fk_get

        Find a related item by id for members.
        """
        pass

    def test_image_folders_id_members_fk_put(self):
        """
        Test case for image_folders_id_members_fk_put

        Update a related item by id for members.
        """
        pass

    def test_image_folders_id_members_get(self):
        """
        Test case for image_folders_id_members_get

        Queries members of ImageFolder.
        """
        pass

    def test_image_folders_id_members_post(self):
        """
        Test case for image_folders_id_members_post

        Creates a new instance in members of this model.
        """
        pass

    def test_image_folders_id_members_rel_fk_delete(self):
        """
        Test case for image_folders_id_members_rel_fk_delete

        Remove the members relation to an item by id.
        """
        pass

    def test_image_folders_id_members_rel_fk_head(self):
        """
        Test case for image_folders_id_members_rel_fk_head

        Check the existence of members relation to an item by id.
        """
        pass

    def test_image_folders_id_members_rel_fk_put(self):
        """
        Test case for image_folders_id_members_rel_fk_put

        Add a related item by id for members.
        """
        pass

    def test_image_folders_id_parent_get(self):
        """
        Test case for image_folders_id_parent_get

        Fetches belongsTo relation parent.
        """
        pass

    def test_image_folders_id_patch(self):
        """
        Test case for image_folders_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_image_folders_id_portals_count_get(self):
        """
        Test case for image_folders_id_portals_count_get

        Counts portals of ImageFolder.
        """
        pass

    def test_image_folders_id_portals_delete(self):
        """
        Test case for image_folders_id_portals_delete

        Deletes all portals of this model.
        """
        pass

    def test_image_folders_id_portals_fk_delete(self):
        """
        Test case for image_folders_id_portals_fk_delete

        Delete a related item by id for portals.
        """
        pass

    def test_image_folders_id_portals_fk_get(self):
        """
        Test case for image_folders_id_portals_fk_get

        Find a related item by id for portals.
        """
        pass

    def test_image_folders_id_portals_fk_put(self):
        """
        Test case for image_folders_id_portals_fk_put

        Update a related item by id for portals.
        """
        pass

    def test_image_folders_id_portals_get(self):
        """
        Test case for image_folders_id_portals_get

        Queries portals of ImageFolder.
        """
        pass

    def test_image_folders_id_portals_post(self):
        """
        Test case for image_folders_id_portals_post

        Creates a new instance in portals of this model.
        """
        pass

    def test_image_folders_id_portals_rel_fk_delete(self):
        """
        Test case for image_folders_id_portals_rel_fk_delete

        Remove the portals relation to an item by id.
        """
        pass

    def test_image_folders_id_portals_rel_fk_head(self):
        """
        Test case for image_folders_id_portals_rel_fk_head

        Check the existence of portals relation to an item by id.
        """
        pass

    def test_image_folders_id_portals_rel_fk_put(self):
        """
        Test case for image_folders_id_portals_rel_fk_put

        Add a related item by id for portals.
        """
        pass

    def test_image_folders_id_put(self):
        """
        Test case for image_folders_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_image_folders_id_replace_post(self):
        """
        Test case for image_folders_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_image_folders_id_team_get(self):
        """
        Test case for image_folders_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_image_folders_patch(self):
        """
        Test case for image_folders_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_image_folders_post(self):
        """
        Test case for image_folders_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_image_folders_put(self):
        """
        Test case for image_folders_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_image_folders_replace_or_create_post(self):
        """
        Test case for image_folders_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_image_folders_update_post(self):
        """
        Test case for image_folders_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_image_folders_upsert_with_where_post(self):
        """
        Test case for image_folders_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
