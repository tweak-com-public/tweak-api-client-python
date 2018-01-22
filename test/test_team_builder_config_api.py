# coding: utf-8

"""
    tweak-api

    Tweak API to integrate with all the Tweak services.  You can find out more about Tweak      at <a href='https://www.tweak.com'>https://www.tweak.com</a>, #tweak.

    OpenAPI spec version: 1.0.6-alpha.2
    
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
from TweakApi.apis.team_builder_config_api import TeamBuilderConfigApi


class TestTeamBuilderConfigApi(unittest.TestCase):
    """ TeamBuilderConfigApi unit test stubs """

    def setUp(self):
        self.api = TweakApi.apis.team_builder_config_api.TeamBuilderConfigApi()

    def tearDown(self):
        pass

    def test_team_builder_configs_change_stream_get(self):
        """
        Test case for team_builder_configs_change_stream_get

        Create a change stream.
        """
        pass

    def test_team_builder_configs_change_stream_post(self):
        """
        Test case for team_builder_configs_change_stream_post

        Create a change stream.
        """
        pass

    def test_team_builder_configs_count_get(self):
        """
        Test case for team_builder_configs_count_get

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_team_builder_configs_find_one_get(self):
        """
        Test case for team_builder_configs_find_one_get

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_team_builder_configs_get(self):
        """
        Test case for team_builder_configs_get

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_team_builder_configs_id_delete(self):
        """
        Test case for team_builder_configs_id_delete

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_team_builder_configs_id_exists_get(self):
        """
        Test case for team_builder_configs_id_exists_get

        Check whether a model instance exists in the data source.
        """
        pass

    def test_team_builder_configs_id_get(self):
        """
        Test case for team_builder_configs_id_get

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_team_builder_configs_id_head(self):
        """
        Test case for team_builder_configs_id_head

        Check whether a model instance exists in the data source.
        """
        pass

    def test_team_builder_configs_id_patch(self):
        """
        Test case for team_builder_configs_id_patch

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_team_builder_configs_id_product_groups_count_get(self):
        """
        Test case for team_builder_configs_id_product_groups_count_get

        Counts productGroups of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_groups_delete(self):
        """
        Test case for team_builder_configs_id_product_groups_delete

        Deletes all productGroups of this model.
        """
        pass

    def test_team_builder_configs_id_product_groups_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_groups_fk_delete

        Delete a related item by id for productGroups.
        """
        pass

    def test_team_builder_configs_id_product_groups_fk_get(self):
        """
        Test case for team_builder_configs_id_product_groups_fk_get

        Find a related item by id for productGroups.
        """
        pass

    def test_team_builder_configs_id_product_groups_fk_put(self):
        """
        Test case for team_builder_configs_id_product_groups_fk_put

        Update a related item by id for productGroups.
        """
        pass

    def test_team_builder_configs_id_product_groups_get(self):
        """
        Test case for team_builder_configs_id_product_groups_get

        Queries productGroups of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_groups_nk_types_count_get(self):
        """
        Test case for team_builder_configs_id_product_groups_nk_types_count_get

        Counts types of ProductGroup.
        """
        pass

    def test_team_builder_configs_id_product_groups_nk_types_delete(self):
        """
        Test case for team_builder_configs_id_product_groups_nk_types_delete

        Deletes all types of this model.
        """
        pass

    def test_team_builder_configs_id_product_groups_nk_types_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_groups_nk_types_fk_delete

        Delete a related item by id for types.
        """
        pass

    def test_team_builder_configs_id_product_groups_nk_types_fk_get(self):
        """
        Test case for team_builder_configs_id_product_groups_nk_types_fk_get

        Find a related item by id for types.
        """
        pass

    def test_team_builder_configs_id_product_groups_nk_types_fk_put(self):
        """
        Test case for team_builder_configs_id_product_groups_nk_types_fk_put

        Update a related item by id for types.
        """
        pass

    def test_team_builder_configs_id_product_groups_nk_types_get(self):
        """
        Test case for team_builder_configs_id_product_groups_nk_types_get

        Queries types of ProductGroup.
        """
        pass

    def test_team_builder_configs_id_product_groups_nk_types_post(self):
        """
        Test case for team_builder_configs_id_product_groups_nk_types_post

        Creates a new instance in types of this model.
        """
        pass

    def test_team_builder_configs_id_product_groups_post(self):
        """
        Test case for team_builder_configs_id_product_groups_post

        Creates a new instance in productGroups of this model.
        """
        pass

    def test_team_builder_configs_id_product_groups_rel_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_groups_rel_fk_delete

        Remove the productGroups relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_groups_rel_fk_head(self):
        """
        Test case for team_builder_configs_id_product_groups_rel_fk_head

        Check the existence of productGroups relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_groups_rel_fk_put(self):
        """
        Test case for team_builder_configs_id_product_groups_rel_fk_put

        Add a related item by id for productGroups.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_count_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_count_get

        Counts productSizeMaterials of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_delete(self):
        """
        Test case for team_builder_configs_id_product_size_materials_delete

        Deletes all productSizeMaterials of this model.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_size_materials_fk_delete

        Delete a related item by id for productSizeMaterials.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_fk_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_fk_get

        Find a related item by id for productSizeMaterials.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_fk_put(self):
        """
        Test case for team_builder_configs_id_product_size_materials_fk_put

        Update a related item by id for productSizeMaterials.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_get

        Queries productSizeMaterials of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_nk_material_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_nk_material_get

        Fetches belongsTo relation material.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get

        Fetches belongsTo relation pdfColorProfile.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_nk_size_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_nk_size_get

        Fetches belongsTo relation size.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_nk_team_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_nk_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_post(self):
        """
        Test case for team_builder_configs_id_product_size_materials_post

        Creates a new instance in productSizeMaterials of this model.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_count_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_count_get

        Counts productSizeMaterialsRel of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_delete(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_delete

        Deletes all productSizeMaterialsRel of this model.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_fk_delete

        Remove the productSizeMaterials relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_fk_delete_0(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_fk_delete_0

        Delete a related item by id for productSizeMaterialsRel.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_fk_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_fk_get

        Find a related item by id for productSizeMaterialsRel.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_fk_head(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_fk_head

        Check the existence of productSizeMaterials relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_fk_put(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_fk_put

        Add a related item by id for productSizeMaterials.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_fk_put_0(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_fk_put_0

        Update a related item by id for productSizeMaterialsRel.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_get

        Queries productSizeMaterialsRel of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_nk_builder_config_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_nk_builder_config_get

        Fetches belongsTo relation builderConfig.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get

        Fetches belongsTo relation pdfColorProfile.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get

        Fetches belongsTo relation productSizeMaterial.
        """
        pass

    def test_team_builder_configs_id_product_size_materials_rel_post(self):
        """
        Test case for team_builder_configs_id_product_size_materials_rel_post

        Creates a new instance in productSizeMaterialsRel of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_count_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_count_get

        Counts productSizes of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_sizes_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_delete

        Deletes all productSizes of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_fk_delete

        Delete a related item by id for productSizes.
        """
        pass

    def test_team_builder_configs_id_product_sizes_fk_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_fk_get

        Find a related item by id for productSizes.
        """
        pass

    def test_team_builder_configs_id_product_sizes_fk_put(self):
        """
        Test case for team_builder_configs_id_product_sizes_fk_put

        Update a related item by id for productSizes.
        """
        pass

    def test_team_builder_configs_id_product_sizes_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_get

        Queries productSizes of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_count_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_count_get

        Counts materials of ProductSize.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_delete

        Deletes all materials of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_fk_delete

        Delete a related item by id for materials.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_fk_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_fk_get

        Find a related item by id for materials.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_fk_put(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_fk_put

        Update a related item by id for materials.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_get

        Queries materials of ProductSize.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_post(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_post

        Creates a new instance in materials of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete

        Remove the materials relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_rel_fk_head(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_rel_fk_head

        Check the existence of materials relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_materials_rel_fk_put(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_materials_rel_fk_put

        Add a related item by id for materials.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_pdf_color_profile_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_pdf_color_profile_get

        Fetches belongsTo relation pdfColorProfile.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_products_count_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_products_count_get

        Counts products of ProductSize.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_products_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_products_delete

        Deletes all products of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_products_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_products_fk_delete

        Delete a related item by id for products.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_products_fk_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_products_fk_get

        Find a related item by id for products.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_products_fk_put(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_products_fk_put

        Update a related item by id for products.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_products_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_products_get

        Queries products of ProductSize.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_products_post(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_products_post

        Creates a new instance in products of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_size_materials_count_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_size_materials_count_get

        Counts sizeMaterials of ProductSize.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_size_materials_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_size_materials_delete

        Deletes all sizeMaterials of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_size_materials_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_size_materials_fk_delete

        Delete a related item by id for sizeMaterials.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_size_materials_fk_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_size_materials_fk_get

        Find a related item by id for sizeMaterials.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_size_materials_fk_put(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_size_materials_fk_put

        Update a related item by id for sizeMaterials.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_size_materials_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_size_materials_get

        Queries sizeMaterials of ProductSize.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_size_materials_post(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_size_materials_post

        Creates a new instance in sizeMaterials of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_nk_type_get(self):
        """
        Test case for team_builder_configs_id_product_sizes_nk_type_get

        Fetches belongsTo relation type.
        """
        pass

    def test_team_builder_configs_id_product_sizes_post(self):
        """
        Test case for team_builder_configs_id_product_sizes_post

        Creates a new instance in productSizes of this model.
        """
        pass

    def test_team_builder_configs_id_product_sizes_rel_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_sizes_rel_fk_delete

        Remove the productSizes relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_sizes_rel_fk_head(self):
        """
        Test case for team_builder_configs_id_product_sizes_rel_fk_head

        Check the existence of productSizes relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_sizes_rel_fk_put(self):
        """
        Test case for team_builder_configs_id_product_sizes_rel_fk_put

        Add a related item by id for productSizes.
        """
        pass

    def test_team_builder_configs_id_product_types_count_get(self):
        """
        Test case for team_builder_configs_id_product_types_count_get

        Counts productTypes of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_types_delete(self):
        """
        Test case for team_builder_configs_id_product_types_delete

        Deletes all productTypes of this model.
        """
        pass

    def test_team_builder_configs_id_product_types_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_types_fk_delete

        Delete a related item by id for productTypes.
        """
        pass

    def test_team_builder_configs_id_product_types_fk_get(self):
        """
        Test case for team_builder_configs_id_product_types_fk_get

        Find a related item by id for productTypes.
        """
        pass

    def test_team_builder_configs_id_product_types_fk_put(self):
        """
        Test case for team_builder_configs_id_product_types_fk_put

        Update a related item by id for productTypes.
        """
        pass

    def test_team_builder_configs_id_product_types_get(self):
        """
        Test case for team_builder_configs_id_product_types_get

        Queries productTypes of TeamBuilderConfig.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_group_get(self):
        """
        Test case for team_builder_configs_id_product_types_nk_group_get

        Fetches belongsTo relation group.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_sizes_count_get(self):
        """
        Test case for team_builder_configs_id_product_types_nk_sizes_count_get

        Counts sizes of ProductType.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_sizes_delete(self):
        """
        Test case for team_builder_configs_id_product_types_nk_sizes_delete

        Deletes all sizes of this model.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_sizes_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_types_nk_sizes_fk_delete

        Delete a related item by id for sizes.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_sizes_fk_get(self):
        """
        Test case for team_builder_configs_id_product_types_nk_sizes_fk_get

        Find a related item by id for sizes.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_sizes_fk_put(self):
        """
        Test case for team_builder_configs_id_product_types_nk_sizes_fk_put

        Update a related item by id for sizes.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_sizes_get(self):
        """
        Test case for team_builder_configs_id_product_types_nk_sizes_get

        Queries sizes of ProductType.
        """
        pass

    def test_team_builder_configs_id_product_types_nk_sizes_post(self):
        """
        Test case for team_builder_configs_id_product_types_nk_sizes_post

        Creates a new instance in sizes of this model.
        """
        pass

    def test_team_builder_configs_id_product_types_post(self):
        """
        Test case for team_builder_configs_id_product_types_post

        Creates a new instance in productTypes of this model.
        """
        pass

    def test_team_builder_configs_id_product_types_rel_fk_delete(self):
        """
        Test case for team_builder_configs_id_product_types_rel_fk_delete

        Remove the productTypes relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_types_rel_fk_head(self):
        """
        Test case for team_builder_configs_id_product_types_rel_fk_head

        Check the existence of productTypes relation to an item by id.
        """
        pass

    def test_team_builder_configs_id_product_types_rel_fk_put(self):
        """
        Test case for team_builder_configs_id_product_types_rel_fk_put

        Add a related item by id for productTypes.
        """
        pass

    def test_team_builder_configs_id_put(self):
        """
        Test case for team_builder_configs_id_put

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_team_builder_configs_id_replace_post(self):
        """
        Test case for team_builder_configs_id_replace_post

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_team_builder_configs_id_team_get(self):
        """
        Test case for team_builder_configs_id_team_get

        Fetches belongsTo relation team.
        """
        pass

    def test_team_builder_configs_patch(self):
        """
        Test case for team_builder_configs_patch

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_team_builder_configs_post(self):
        """
        Test case for team_builder_configs_post

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_team_builder_configs_put(self):
        """
        Test case for team_builder_configs_put

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_team_builder_configs_replace_or_create_post(self):
        """
        Test case for team_builder_configs_replace_or_create_post

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_team_builder_configs_update_post(self):
        """
        Test case for team_builder_configs_update_post

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_team_builder_configs_upsert_with_where_post(self):
        """
        Test case for team_builder_configs_upsert_with_where_post

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
