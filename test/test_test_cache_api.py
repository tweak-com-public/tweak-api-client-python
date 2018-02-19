# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.13
    
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
from TweakApi.apis.test_cache_api import TestCacheApi


class TestTestCacheApi(unittest.TestCase):
    """ TestCacheApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.test_cache_api.TestCacheApi()

    def tearDown(self):
        pass

    def test_test_caches_change_stream_get(self):
        """
        Test case for test_caches_change_stream_get

        Create a change stream.
        """
        pass

    def test_test_caches_change_stream_post(self):
        """
        Test case for test_caches_change_stream_post

        Create a change stream.
        """
        pass

    def test_test_caches_count_get(self):
        """
        Test case for test_caches_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_test_caches_find_one_get(self):
        """
        Test case for test_caches_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_test_caches_get(self):
        """
        Test case for test_caches_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_test_caches_id_delete(self):
        """
        Test case for test_caches_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_test_caches_id_exists_get(self):
        """
        Test case for test_caches_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_test_caches_id_get(self):
        """
        Test case for test_caches_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_test_caches_id_head(self):
        """
        Test case for test_caches_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_test_caches_id_patch(self):
        """
        Test case for test_caches_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_test_caches_id_put(self):
        """
        Test case for test_caches_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_test_caches_id_replace_post(self):
        """
        Test case for test_caches_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_test_caches_post(self):
        """
        Test case for test_caches_post

        Create a new instance of the model and persist it into the data source.
        """
        pass


if __name__ == '__main__':
    unittest.main()
