# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.8-alpha.10
    
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
from TweakApi.apis.billing_api import BillingApi


class TestBillingApi(unittest.TestCase):
    """ BillingApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.billing_api.BillingApi()

    def tearDown(self):
        pass

    def test_billings_change_stream_get(self):
        """
        Test case for billings_change_stream_get

        Create a change stream.
        """
        pass

    def test_billings_change_stream_post(self):
        """
        Test case for billings_change_stream_post

        Create a change stream.
        """
        pass

    def test_billings_countries_get(self):
        """
        Test case for billings_countries_get

        List available countries
        """
        pass

    def test_billings_id_put(self):
        """
        Test case for billings_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_billings_id_replace_post(self):
        """
        Test case for billings_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_billings_put(self):
        """
        Test case for billings_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_billings_replace_or_create_post(self):
        """
        Test case for billings_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_billings_tax_evidence_country_vat_get(self):
        """
        Test case for billings_tax_evidence_country_vat_get

        Get Tax Evidence by country and VAT
        """
        pass

    def test_billings_upsert_with_where_post(self):
        """
        Test case for billings_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
