# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-beta.0
    
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
from TweakApi.apis.data_source_postgre_sql_api import DataSourcePostgreSqlApi


class TestDataSourcePostgreSqlApi(unittest.TestCase):
    """ DataSourcePostgreSqlApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.data_source_postgre_sql_api.DataSourcePostgreSqlApi()

    def tearDown(self):
        pass

    def test_data_source_postgre_sqls_change_stream_get(self):
        """
        Test case for data_source_postgre_sqls_change_stream_get

        Create a change stream.
        """
        pass

    def test_data_source_postgre_sqls_change_stream_post(self):
        """
        Test case for data_source_postgre_sqls_change_stream_post

        Create a change stream.
        """
        pass

    def test_data_source_postgre_sqls_count_get(self):
        """
        Test case for data_source_postgre_sqls_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_data_source_postgre_sqls_find_one_get(self):
        """
        Test case for data_source_postgre_sqls_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_data_source_postgre_sqls_get(self):
        """
        Test case for data_source_postgre_sqls_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_delete(self):
        """
        Test case for data_source_postgre_sqls_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_dynamic_datas_count_get(self):
        """
        Test case for data_source_postgre_sqls_id_dynamic_datas_count_get

        Counts dynamicDatas of DataSourcePostgreSql.
        """
        pass

    def test_data_source_postgre_sqls_id_dynamic_datas_delete(self):
        """
        Test case for data_source_postgre_sqls_id_dynamic_datas_delete

        Deletes all dynamicDatas of this model.
        """
        pass

    def test_data_source_postgre_sqls_id_dynamic_datas_fk_delete(self):
        """
        Test case for data_source_postgre_sqls_id_dynamic_datas_fk_delete

        Delete a related item by id for dynamicDatas.
        """
        pass

    def test_data_source_postgre_sqls_id_dynamic_datas_fk_get(self):
        """
        Test case for data_source_postgre_sqls_id_dynamic_datas_fk_get

        Find a related item by id for dynamicDatas.
        """
        pass

    def test_data_source_postgre_sqls_id_dynamic_datas_fk_put(self):
        """
        Test case for data_source_postgre_sqls_id_dynamic_datas_fk_put

        Update a related item by id for dynamicDatas.
        """
        pass

    def test_data_source_postgre_sqls_id_dynamic_datas_get(self):
        """
        Test case for data_source_postgre_sqls_id_dynamic_datas_get

        Queries dynamicDatas of DataSourcePostgreSql.
        """
        pass

    def test_data_source_postgre_sqls_id_dynamic_datas_post(self):
        """
        Test case for data_source_postgre_sqls_id_dynamic_datas_post

        Creates a new instance in dynamicDatas of this model.
        """
        pass

    def test_data_source_postgre_sqls_id_exists_get(self):
        """
        Test case for data_source_postgre_sqls_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_get(self):
        """
        Test case for data_source_postgre_sqls_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_head(self):
        """
        Test case for data_source_postgre_sqls_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_patch(self):
        """
        Test case for data_source_postgre_sqls_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_put(self):
        """
        Test case for data_source_postgre_sqls_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_replace_post(self):
        """
        Test case for data_source_postgre_sqls_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_data_source_postgre_sqls_id_team_get(self):
        """
        Test case for data_source_postgre_sqls_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_data_source_postgre_sqls_post(self):
        """
        Test case for data_source_postgre_sqls_post

        Create a new instance of the model and persist it into the data source.
        """
        pass


if __name__ == '__main__':
    unittest.main()
