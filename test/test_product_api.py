# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-beta.1
    
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
from TweakApi.apis.product_api import ProductApi


class TestProductApi(unittest.TestCase):
    """ ProductApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.product_api.ProductApi()

    def tearDown(self):
        pass

    def test_products_change_stream_get(self):
        """
        Test case for products_change_stream_get

        Create a change stream.
        """
        pass

    def test_products_change_stream_post(self):
        """
        Test case for products_change_stream_post

        Create a change stream.
        """
        pass

    def test_products_count_get(self):
        """
        Test case for products_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_products_find_one_get(self):
        """
        Test case for products_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_products_get(self):
        """
        Test case for products_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_products_id_delete(self):
        """
        Test case for products_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_products_id_exists_get(self):
        """
        Test case for products_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_products_id_get(self):
        """
        Test case for products_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_products_id_head(self):
        """
        Test case for products_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_products_id_patch(self):
        """
        Test case for products_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_products_id_put(self):
        """
        Test case for products_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_products_id_replace_post(self):
        """
        Test case for products_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_products_id_size_get(self):
        """
        Test case for products_id_size_get

        Fetches belongsTo relation size.
        """
        pass

    def test_products_id_tags_count_get(self):
        """
        Test case for products_id_tags_count_get

        Counts tags of Product.
        """
        pass

    def test_products_id_tags_delete(self):
        """
        Test case for products_id_tags_delete

        Deletes all tags of this model.
        """
        pass

    def test_products_id_tags_fk_delete(self):
        """
        Test case for products_id_tags_fk_delete

        Delete a related item by id for tags.
        """
        pass

    def test_products_id_tags_fk_get(self):
        """
        Test case for products_id_tags_fk_get

        Find a related item by id for tags.
        """
        pass

    def test_products_id_tags_fk_put(self):
        """
        Test case for products_id_tags_fk_put

        Update a related item by id for tags.
        """
        pass

    def test_products_id_tags_get(self):
        """
        Test case for products_id_tags_get

        Queries tags of Product.
        """
        pass

    def test_products_id_tags_post(self):
        """
        Test case for products_id_tags_post

        Creates a new instance in tags of this model.
        """
        pass

    def test_products_id_tags_rel_fk_delete(self):
        """
        Test case for products_id_tags_rel_fk_delete

        Remove the tags relation to an item by id.
        """
        pass

    def test_products_id_tags_rel_fk_head(self):
        """
        Test case for products_id_tags_rel_fk_head

        Check the existence of tags relation to an item by id.
        """
        pass

    def test_products_id_tags_rel_fk_put(self):
        """
        Test case for products_id_tags_rel_fk_put

        Add a related item by id for tags.
        """
        pass

    def test_products_patch(self):
        """
        Test case for products_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_products_post(self):
        """
        Test case for products_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_products_put(self):
        """
        Test case for products_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_products_replace_or_create_post(self):
        """
        Test case for products_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_products_update_post(self):
        """
        Test case for products_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_products_upsert_with_where_post(self):
        """
        Test case for products_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
