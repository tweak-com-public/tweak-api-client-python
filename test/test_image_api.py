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

from __future__ import absolute_import

import os
import sys
import unittest

import TweakApi
from TweakApi.rest import ApiException
from TweakApi.apis.image_api import ImageApi


class TestImageApi(unittest.TestCase):
    """ ImageApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.image_api.ImageApi()

    def tearDown(self):
        pass

    def test_images_change_stream_get(self):
        """
        Test case for images_change_stream_get

        Create a change stream.
        """
        pass

    def test_images_change_stream_post(self):
        """
        Test case for images_change_stream_post

        Create a change stream.
        """
        pass

    def test_images_count_get(self):
        """
        Test case for images_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_images_find_one_get(self):
        """
        Test case for images_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_images_get(self):
        """
        Test case for images_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_images_id_delete(self):
        """
        Test case for images_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_images_id_exists_get(self):
        """
        Test case for images_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_images_id_folder_get(self):
        """
        Test case for images_id_folder_get

        Fetches belongsTo relation folder.
        """
        pass

    def test_images_id_get(self):
        """
        Test case for images_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_images_id_head(self):
        """
        Test case for images_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_images_id_patch(self):
        """
        Test case for images_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_images_id_put(self):
        """
        Test case for images_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_images_id_replace_post(self):
        """
        Test case for images_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_images_id_team_get(self):
        """
        Test case for images_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_images_patch(self):
        """
        Test case for images_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_images_post(self):
        """
        Test case for images_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_images_put(self):
        """
        Test case for images_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_images_replace_or_create_post(self):
        """
        Test case for images_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_images_update_post(self):
        """
        Test case for images_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_images_upsert_with_where_post(self):
        """
        Test case for images_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
