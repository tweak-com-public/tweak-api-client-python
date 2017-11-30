# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.3-beta.0
    
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
from TweakApi.apis.dynamic_data_api import DynamicDataApi


class TestDynamicDataApi(unittest.TestCase):
    """ DynamicDataApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.dynamic_data_api.DynamicDataApi()

    def tearDown(self):
        pass

    def test_dynamic_data_change_stream_get(self):
        """
        Test case for dynamic_data_change_stream_get

        Create a change stream.
        """
        pass

    def test_dynamic_data_change_stream_post(self):
        """
        Test case for dynamic_data_change_stream_post

        Create a change stream.
        """
        pass

    def test_dynamic_data_count_get(self):
        """
        Test case for dynamic_data_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_dynamic_data_find_one_get(self):
        """
        Test case for dynamic_data_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_dynamic_data_get(self):
        """
        Test case for dynamic_data_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_dynamic_data_id_delete(self):
        """
        Test case for dynamic_data_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_dynamic_data_id_designs_count_get(self):
        """
        Test case for dynamic_data_id_designs_count_get

        Counts designs of DynamicData.
        """
        pass

    def test_dynamic_data_id_designs_delete(self):
        """
        Test case for dynamic_data_id_designs_delete

        Deletes all designs of this model.
        """
        pass

    def test_dynamic_data_id_designs_fk_delete(self):
        """
        Test case for dynamic_data_id_designs_fk_delete

        Delete a related item by id for designs.
        """
        pass

    def test_dynamic_data_id_designs_fk_get(self):
        """
        Test case for dynamic_data_id_designs_fk_get

        Find a related item by id for designs.
        """
        pass

    def test_dynamic_data_id_designs_fk_put(self):
        """
        Test case for dynamic_data_id_designs_fk_put

        Update a related item by id for designs.
        """
        pass

    def test_dynamic_data_id_designs_get(self):
        """
        Test case for dynamic_data_id_designs_get

        Queries designs of DynamicData.
        """
        pass

    def test_dynamic_data_id_designs_post(self):
        """
        Test case for dynamic_data_id_designs_post

        Creates a new instance in designs of this model.
        """
        pass

    def test_dynamic_data_id_exists_get(self):
        """
        Test case for dynamic_data_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_dynamic_data_id_get(self):
        """
        Test case for dynamic_data_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_dynamic_data_id_head(self):
        """
        Test case for dynamic_data_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_dynamic_data_id_patch(self):
        """
        Test case for dynamic_data_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dynamic_data_id_put(self):
        """
        Test case for dynamic_data_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dynamic_data_id_records_count_get(self):
        """
        Test case for dynamic_data_id_records_count_get

        Count Dynamic Data records
        """
        pass

    def test_dynamic_data_id_records_delete(self):
        """
        Test case for dynamic_data_id_records_delete

        Delete all matching records.
        """
        pass

    def test_dynamic_data_id_records_fk_delete(self):
        """
        Test case for dynamic_data_id_records_fk_delete

        Delete a model instance by {{fk}} from the data source.
        """
        pass

    def test_dynamic_data_id_records_fk_get(self):
        """
        Test case for dynamic_data_id_records_fk_get

        Find a model instance by {{fk}} from the data source.
        """
        pass

    def test_dynamic_data_id_records_fk_property_name_upload_put(self):
        """
        Test case for dynamic_data_id_records_fk_property_name_upload_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dynamic_data_id_records_fk_put(self):
        """
        Test case for dynamic_data_id_records_fk_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dynamic_data_id_records_get(self):
        """
        Test case for dynamic_data_id_records_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_dynamic_data_id_records_migrate_post(self):
        """
        Test case for dynamic_data_id_records_migrate_post

        Request migration for Dynamic Data records
        """
        pass

    def test_dynamic_data_id_records_post(self):
        """
        Test case for dynamic_data_id_records_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_dynamic_data_id_records_upload_csv_post(self):
        """
        Test case for dynamic_data_id_records_upload_csv_post

        Upload CSV for this Dynamic Data
        """
        pass

    def test_dynamic_data_id_replace_post(self):
        """
        Test case for dynamic_data_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dynamic_data_id_team_get(self):
        """
        Test case for dynamic_data_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_dynamic_data_patch(self):
        """
        Test case for dynamic_data_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_dynamic_data_post(self):
        """
        Test case for dynamic_data_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_dynamic_data_put(self):
        """
        Test case for dynamic_data_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_dynamic_data_replace_or_create_post(self):
        """
        Test case for dynamic_data_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_dynamic_data_update_post(self):
        """
        Test case for dynamic_data_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_dynamic_data_upsert_with_where_post(self):
        """
        Test case for dynamic_data_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
