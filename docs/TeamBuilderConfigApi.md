# TweakApi.TeamBuilderConfigApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_builder_configs_change_stream_get**](TeamBuilderConfigApi.md#team_builder_configs_change_stream_get) | **GET** /TeamBuilderConfigs/change-stream | Create a change stream.
[**team_builder_configs_change_stream_post**](TeamBuilderConfigApi.md#team_builder_configs_change_stream_post) | **POST** /TeamBuilderConfigs/change-stream | Create a change stream.
[**team_builder_configs_count_get**](TeamBuilderConfigApi.md#team_builder_configs_count_get) | **GET** /TeamBuilderConfigs/count | Count instances of the model matched by where from the data source.
[**team_builder_configs_find_one_get**](TeamBuilderConfigApi.md#team_builder_configs_find_one_get) | **GET** /TeamBuilderConfigs/findOne | Find first instance of the model matched by filter from the data source.
[**team_builder_configs_get**](TeamBuilderConfigApi.md#team_builder_configs_get) | **GET** /TeamBuilderConfigs | Find all instances of the model matched by filter from the data source.
[**team_builder_configs_id_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_delete) | **DELETE** /TeamBuilderConfigs/{id} | Delete a model instance by {{id}} from the data source.
[**team_builder_configs_id_exists_get**](TeamBuilderConfigApi.md#team_builder_configs_id_exists_get) | **GET** /TeamBuilderConfigs/{id}/exists | Check whether a model instance exists in the data source.
[**team_builder_configs_id_get**](TeamBuilderConfigApi.md#team_builder_configs_id_get) | **GET** /TeamBuilderConfigs/{id} | Find a model instance by {{id}} from the data source.
[**team_builder_configs_id_head**](TeamBuilderConfigApi.md#team_builder_configs_id_head) | **HEAD** /TeamBuilderConfigs/{id} | Check whether a model instance exists in the data source.
[**team_builder_configs_id_patch**](TeamBuilderConfigApi.md#team_builder_configs_id_patch) | **PATCH** /TeamBuilderConfigs/{id} | Patch attributes for a model instance and persist it into the data source.
[**team_builder_configs_id_portals_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_portals_count_get) | **GET** /TeamBuilderConfigs/{id}/portals/count | Counts portals of TeamBuilderConfig.
[**team_builder_configs_id_portals_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_portals_delete) | **DELETE** /TeamBuilderConfigs/{id}/portals | Deletes all portals of this model.
[**team_builder_configs_id_portals_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_portals_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/portals/{fk} | Delete a related item by id for portals.
[**team_builder_configs_id_portals_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_portals_fk_get) | **GET** /TeamBuilderConfigs/{id}/portals/{fk} | Find a related item by id for portals.
[**team_builder_configs_id_portals_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_portals_fk_put) | **PUT** /TeamBuilderConfigs/{id}/portals/{fk} | Update a related item by id for portals.
[**team_builder_configs_id_portals_get**](TeamBuilderConfigApi.md#team_builder_configs_id_portals_get) | **GET** /TeamBuilderConfigs/{id}/portals | Queries portals of TeamBuilderConfig.
[**team_builder_configs_id_portals_post**](TeamBuilderConfigApi.md#team_builder_configs_id_portals_post) | **POST** /TeamBuilderConfigs/{id}/portals | Creates a new instance in portals of this model.
[**team_builder_configs_id_product_groups_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_count_get) | **GET** /TeamBuilderConfigs/{id}/productGroups/count | Counts productGroups of TeamBuilderConfig.
[**team_builder_configs_id_product_groups_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_delete) | **DELETE** /TeamBuilderConfigs/{id}/productGroups | Deletes all productGroups of this model.
[**team_builder_configs_id_product_groups_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productGroups/{fk} | Delete a related item by id for productGroups.
[**team_builder_configs_id_product_groups_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_fk_get) | **GET** /TeamBuilderConfigs/{id}/productGroups/{fk} | Find a related item by id for productGroups.
[**team_builder_configs_id_product_groups_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productGroups/{fk} | Update a related item by id for productGroups.
[**team_builder_configs_id_product_groups_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_get) | **GET** /TeamBuilderConfigs/{id}/productGroups | Queries productGroups of TeamBuilderConfig.
[**team_builder_configs_id_product_groups_nk_types_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_nk_types_count_get) | **GET** /TeamBuilderConfigs/{id}/productGroups/{nk}/types/count | Counts types of ProductGroup.
[**team_builder_configs_id_product_groups_nk_types_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_nk_types_delete) | **DELETE** /TeamBuilderConfigs/{id}/productGroups/{nk}/types | Deletes all types of this model.
[**team_builder_configs_id_product_groups_nk_types_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_nk_types_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productGroups/{nk}/types/{fk} | Delete a related item by id for types.
[**team_builder_configs_id_product_groups_nk_types_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_nk_types_fk_get) | **GET** /TeamBuilderConfigs/{id}/productGroups/{nk}/types/{fk} | Find a related item by id for types.
[**team_builder_configs_id_product_groups_nk_types_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_nk_types_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productGroups/{nk}/types/{fk} | Update a related item by id for types.
[**team_builder_configs_id_product_groups_nk_types_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_nk_types_get) | **GET** /TeamBuilderConfigs/{id}/productGroups/{nk}/types | Queries types of ProductGroup.
[**team_builder_configs_id_product_groups_nk_types_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_nk_types_post) | **POST** /TeamBuilderConfigs/{id}/productGroups/{nk}/types | Creates a new instance in types of this model.
[**team_builder_configs_id_product_groups_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_post) | **POST** /TeamBuilderConfigs/{id}/productGroups | Creates a new instance in productGroups of this model.
[**team_builder_configs_id_product_groups_rel_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_rel_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productGroups/rel/{fk} | Remove the productGroups relation to an item by id.
[**team_builder_configs_id_product_groups_rel_fk_head**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_rel_fk_head) | **HEAD** /TeamBuilderConfigs/{id}/productGroups/rel/{fk} | Check the existence of productGroups relation to an item by id.
[**team_builder_configs_id_product_groups_rel_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_groups_rel_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productGroups/rel/{fk} | Add a related item by id for productGroups.
[**team_builder_configs_id_product_size_materials_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_count_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterials/count | Counts productSizeMaterials of TeamBuilderConfig.
[**team_builder_configs_id_product_size_materials_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizeMaterials | Deletes all productSizeMaterials of this model.
[**team_builder_configs_id_product_size_materials_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizeMaterials/{fk} | Delete a related item by id for productSizeMaterials.
[**team_builder_configs_id_product_size_materials_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_fk_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterials/{fk} | Find a related item by id for productSizeMaterials.
[**team_builder_configs_id_product_size_materials_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizeMaterials/{fk} | Update a related item by id for productSizeMaterials.
[**team_builder_configs_id_product_size_materials_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterials | Queries productSizeMaterials of TeamBuilderConfig.
[**team_builder_configs_id_product_size_materials_nk_material_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_nk_material_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterials/{nk}/material | Fetches belongsTo relation material.
[**team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterials/{nk}/pdfColorProfile | Fetches belongsTo relation pdfColorProfile.
[**team_builder_configs_id_product_size_materials_nk_size_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_nk_size_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterials/{nk}/size | Fetches belongsTo relation size.
[**team_builder_configs_id_product_size_materials_nk_team_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_nk_team_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterials/{nk}/team | Fetches belongsTo relation team.
[**team_builder_configs_id_product_size_materials_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_post) | **POST** /TeamBuilderConfigs/{id}/productSizeMaterials | Creates a new instance in productSizeMaterials of this model.
[**team_builder_configs_id_product_size_materials_rel_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_count_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterialsRel/count | Counts productSizeMaterialsRel of TeamBuilderConfig.
[**team_builder_configs_id_product_size_materials_rel_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizeMaterialsRel | Deletes all productSizeMaterialsRel of this model.
[**team_builder_configs_id_product_size_materials_rel_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizeMaterials/rel/{fk} | Remove the productSizeMaterials relation to an item by id.
[**team_builder_configs_id_product_size_materials_rel_fk_delete_0**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_fk_delete_0) | **DELETE** /TeamBuilderConfigs/{id}/productSizeMaterialsRel/{fk} | Delete a related item by id for productSizeMaterialsRel.
[**team_builder_configs_id_product_size_materials_rel_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_fk_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterialsRel/{fk} | Find a related item by id for productSizeMaterialsRel.
[**team_builder_configs_id_product_size_materials_rel_fk_head**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_fk_head) | **HEAD** /TeamBuilderConfigs/{id}/productSizeMaterials/rel/{fk} | Check the existence of productSizeMaterials relation to an item by id.
[**team_builder_configs_id_product_size_materials_rel_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizeMaterials/rel/{fk} | Add a related item by id for productSizeMaterials.
[**team_builder_configs_id_product_size_materials_rel_fk_put_0**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_fk_put_0) | **PUT** /TeamBuilderConfigs/{id}/productSizeMaterialsRel/{fk} | Update a related item by id for productSizeMaterialsRel.
[**team_builder_configs_id_product_size_materials_rel_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterialsRel | Queries productSizeMaterialsRel of TeamBuilderConfig.
[**team_builder_configs_id_product_size_materials_rel_nk_builder_config_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_nk_builder_config_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterialsRel/{nk}/builderConfig | Fetches belongsTo relation builderConfig.
[**team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterialsRel/{nk}/pdfColorProfile | Fetches belongsTo relation pdfColorProfile.
[**team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get) | **GET** /TeamBuilderConfigs/{id}/productSizeMaterialsRel/{nk}/productSizeMaterial | Fetches belongsTo relation productSizeMaterial.
[**team_builder_configs_id_product_size_materials_rel_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_size_materials_rel_post) | **POST** /TeamBuilderConfigs/{id}/productSizeMaterialsRel | Creates a new instance in productSizeMaterialsRel of this model.
[**team_builder_configs_id_product_sizes_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_count_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/count | Counts productSizes of TeamBuilderConfig.
[**team_builder_configs_id_product_sizes_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes | Deletes all productSizes of this model.
[**team_builder_configs_id_product_sizes_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{fk} | Delete a related item by id for productSizes.
[**team_builder_configs_id_product_sizes_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_fk_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{fk} | Find a related item by id for productSizes.
[**team_builder_configs_id_product_sizes_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizes/{fk} | Update a related item by id for productSizes.
[**team_builder_configs_id_product_sizes_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_get) | **GET** /TeamBuilderConfigs/{id}/productSizes | Queries productSizes of TeamBuilderConfig.
[**team_builder_configs_id_product_sizes_nk_materials_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_count_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials/count | Counts materials of ProductSize.
[**team_builder_configs_id_product_sizes_nk_materials_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials | Deletes all materials of this model.
[**team_builder_configs_id_product_sizes_nk_materials_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials/{fk} | Delete a related item by id for materials.
[**team_builder_configs_id_product_sizes_nk_materials_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_fk_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials/{fk} | Find a related item by id for materials.
[**team_builder_configs_id_product_sizes_nk_materials_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials/{fk} | Update a related item by id for materials.
[**team_builder_configs_id_product_sizes_nk_materials_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials | Queries materials of ProductSize.
[**team_builder_configs_id_product_sizes_nk_materials_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_post) | **POST** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials | Creates a new instance in materials of this model.
[**team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials/rel/{fk} | Remove the materials relation to an item by id.
[**team_builder_configs_id_product_sizes_nk_materials_rel_fk_head**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_rel_fk_head) | **HEAD** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials/rel/{fk} | Check the existence of materials relation to an item by id.
[**team_builder_configs_id_product_sizes_nk_materials_rel_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_materials_rel_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizes/{nk}/materials/rel/{fk} | Add a related item by id for materials.
[**team_builder_configs_id_product_sizes_nk_pdf_color_profile_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_pdf_color_profile_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/pdfColorProfile | Fetches belongsTo relation pdfColorProfile.
[**team_builder_configs_id_product_sizes_nk_products_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_products_count_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/products/count | Counts products of ProductSize.
[**team_builder_configs_id_product_sizes_nk_products_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_products_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{nk}/products | Deletes all products of this model.
[**team_builder_configs_id_product_sizes_nk_products_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_products_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{nk}/products/{fk} | Delete a related item by id for products.
[**team_builder_configs_id_product_sizes_nk_products_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_products_fk_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/products/{fk} | Find a related item by id for products.
[**team_builder_configs_id_product_sizes_nk_products_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_products_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizes/{nk}/products/{fk} | Update a related item by id for products.
[**team_builder_configs_id_product_sizes_nk_products_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_products_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/products | Queries products of ProductSize.
[**team_builder_configs_id_product_sizes_nk_products_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_products_post) | **POST** /TeamBuilderConfigs/{id}/productSizes/{nk}/products | Creates a new instance in products of this model.
[**team_builder_configs_id_product_sizes_nk_size_materials_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_size_materials_count_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/sizeMaterials/count | Counts sizeMaterials of ProductSize.
[**team_builder_configs_id_product_sizes_nk_size_materials_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_size_materials_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{nk}/sizeMaterials | Deletes all sizeMaterials of this model.
[**team_builder_configs_id_product_sizes_nk_size_materials_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_size_materials_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/{nk}/sizeMaterials/{fk} | Delete a related item by id for sizeMaterials.
[**team_builder_configs_id_product_sizes_nk_size_materials_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_size_materials_fk_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/sizeMaterials/{fk} | Find a related item by id for sizeMaterials.
[**team_builder_configs_id_product_sizes_nk_size_materials_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_size_materials_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizes/{nk}/sizeMaterials/{fk} | Update a related item by id for sizeMaterials.
[**team_builder_configs_id_product_sizes_nk_size_materials_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_size_materials_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/sizeMaterials | Queries sizeMaterials of ProductSize.
[**team_builder_configs_id_product_sizes_nk_size_materials_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_size_materials_post) | **POST** /TeamBuilderConfigs/{id}/productSizes/{nk}/sizeMaterials | Creates a new instance in sizeMaterials of this model.
[**team_builder_configs_id_product_sizes_nk_type_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_nk_type_get) | **GET** /TeamBuilderConfigs/{id}/productSizes/{nk}/type | Fetches belongsTo relation type.
[**team_builder_configs_id_product_sizes_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_post) | **POST** /TeamBuilderConfigs/{id}/productSizes | Creates a new instance in productSizes of this model.
[**team_builder_configs_id_product_sizes_rel_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_rel_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productSizes/rel/{fk} | Remove the productSizes relation to an item by id.
[**team_builder_configs_id_product_sizes_rel_fk_head**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_rel_fk_head) | **HEAD** /TeamBuilderConfigs/{id}/productSizes/rel/{fk} | Check the existence of productSizes relation to an item by id.
[**team_builder_configs_id_product_sizes_rel_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_sizes_rel_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productSizes/rel/{fk} | Add a related item by id for productSizes.
[**team_builder_configs_id_product_types_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_count_get) | **GET** /TeamBuilderConfigs/{id}/productTypes/count | Counts productTypes of TeamBuilderConfig.
[**team_builder_configs_id_product_types_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_delete) | **DELETE** /TeamBuilderConfigs/{id}/productTypes | Deletes all productTypes of this model.
[**team_builder_configs_id_product_types_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productTypes/{fk} | Delete a related item by id for productTypes.
[**team_builder_configs_id_product_types_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_fk_get) | **GET** /TeamBuilderConfigs/{id}/productTypes/{fk} | Find a related item by id for productTypes.
[**team_builder_configs_id_product_types_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productTypes/{fk} | Update a related item by id for productTypes.
[**team_builder_configs_id_product_types_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_get) | **GET** /TeamBuilderConfigs/{id}/productTypes | Queries productTypes of TeamBuilderConfig.
[**team_builder_configs_id_product_types_nk_group_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_group_get) | **GET** /TeamBuilderConfigs/{id}/productTypes/{nk}/group | Fetches belongsTo relation group.
[**team_builder_configs_id_product_types_nk_sizes_count_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_sizes_count_get) | **GET** /TeamBuilderConfigs/{id}/productTypes/{nk}/sizes/count | Counts sizes of ProductType.
[**team_builder_configs_id_product_types_nk_sizes_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_sizes_delete) | **DELETE** /TeamBuilderConfigs/{id}/productTypes/{nk}/sizes | Deletes all sizes of this model.
[**team_builder_configs_id_product_types_nk_sizes_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_sizes_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productTypes/{nk}/sizes/{fk} | Delete a related item by id for sizes.
[**team_builder_configs_id_product_types_nk_sizes_fk_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_sizes_fk_get) | **GET** /TeamBuilderConfigs/{id}/productTypes/{nk}/sizes/{fk} | Find a related item by id for sizes.
[**team_builder_configs_id_product_types_nk_sizes_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_sizes_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productTypes/{nk}/sizes/{fk} | Update a related item by id for sizes.
[**team_builder_configs_id_product_types_nk_sizes_get**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_sizes_get) | **GET** /TeamBuilderConfigs/{id}/productTypes/{nk}/sizes | Queries sizes of ProductType.
[**team_builder_configs_id_product_types_nk_sizes_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_nk_sizes_post) | **POST** /TeamBuilderConfigs/{id}/productTypes/{nk}/sizes | Creates a new instance in sizes of this model.
[**team_builder_configs_id_product_types_post**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_post) | **POST** /TeamBuilderConfigs/{id}/productTypes | Creates a new instance in productTypes of this model.
[**team_builder_configs_id_product_types_rel_fk_delete**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_rel_fk_delete) | **DELETE** /TeamBuilderConfigs/{id}/productTypes/rel/{fk} | Remove the productTypes relation to an item by id.
[**team_builder_configs_id_product_types_rel_fk_head**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_rel_fk_head) | **HEAD** /TeamBuilderConfigs/{id}/productTypes/rel/{fk} | Check the existence of productTypes relation to an item by id.
[**team_builder_configs_id_product_types_rel_fk_put**](TeamBuilderConfigApi.md#team_builder_configs_id_product_types_rel_fk_put) | **PUT** /TeamBuilderConfigs/{id}/productTypes/rel/{fk} | Add a related item by id for productTypes.
[**team_builder_configs_id_put**](TeamBuilderConfigApi.md#team_builder_configs_id_put) | **PUT** /TeamBuilderConfigs/{id} | Replace attributes for a model instance and persist it into the data source.
[**team_builder_configs_id_replace_post**](TeamBuilderConfigApi.md#team_builder_configs_id_replace_post) | **POST** /TeamBuilderConfigs/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**team_builder_configs_id_team_get**](TeamBuilderConfigApi.md#team_builder_configs_id_team_get) | **GET** /TeamBuilderConfigs/{id}/team | Fetches belongsTo relation team.
[**team_builder_configs_patch**](TeamBuilderConfigApi.md#team_builder_configs_patch) | **PATCH** /TeamBuilderConfigs | Patch an existing model instance or insert a new one into the data source.
[**team_builder_configs_post**](TeamBuilderConfigApi.md#team_builder_configs_post) | **POST** /TeamBuilderConfigs | Create a new instance of the model and persist it into the data source.
[**team_builder_configs_put**](TeamBuilderConfigApi.md#team_builder_configs_put) | **PUT** /TeamBuilderConfigs | Replace an existing model instance or insert a new one into the data source.
[**team_builder_configs_replace_or_create_post**](TeamBuilderConfigApi.md#team_builder_configs_replace_or_create_post) | **POST** /TeamBuilderConfigs/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**team_builder_configs_update_post**](TeamBuilderConfigApi.md#team_builder_configs_update_post) | **POST** /TeamBuilderConfigs/update | Update instances of the model matched by {{where}} from the data source.
[**team_builder_configs_upsert_with_where_post**](TeamBuilderConfigApi.md#team_builder_configs_upsert_with_where_post) | **POST** /TeamBuilderConfigs/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **team_builder_configs_change_stream_get**
> file team_builder_configs_change_stream_get(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_configs_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_change_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_change_stream_post**
> file team_builder_configs_change_stream_post(options=options)

Create a change stream.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_builder_configs_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_change_stream_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **str**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_count_get**
> InlineResponse2001 team_builder_configs_count_get(where=where)

Count instances of the model matched by where from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.team_builder_configs_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_find_one_get**
> TeamBuilderConfig team_builder_configs_find_one_get(filter=filter)

Find first instance of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.team_builder_configs_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_get**
> list[TeamBuilderConfig] team_builder_configs_get(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.team_builder_configs_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamBuilderConfig]**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_delete**
> object team_builder_configs_id_delete(id)

Delete a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_configs_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_exists_get**
> InlineResponse2002 team_builder_configs_id_exists_get(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_configs_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_exists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_get**
> TeamBuilderConfig team_builder_configs_id_get(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.team_builder_configs_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_head**
> InlineResponse2002 team_builder_configs_id_head(id)

Check whether a model instance exists in the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_builder_configs_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_patch**
> TeamBuilderConfig team_builder_configs_id_patch(id, data=data)

Patch attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_configs_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_portals_count_get**
> InlineResponse2001 team_builder_configs_id_portals_count_get(id, where=where)

Counts portals of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_portals_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_portals_delete**
> team_builder_configs_id_portals_delete(id)

Deletes all portals of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id

try: 
    # Deletes all portals of this model.
    api_instance.team_builder_configs_id_portals_delete(id)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_portals_fk_delete**
> team_builder_configs_id_portals_fk_delete(id, fk)

Delete a related item by id for portals.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.team_builder_configs_id_portals_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_portals_fk_get**
> Portal team_builder_configs_id_portals_fk_get(id, fk)

Find a related item by id for portals.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.team_builder_configs_id_portals_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_portals_fk_put**
> Portal team_builder_configs_id_portals_fk_put(id, fk, data=data)

Update a related item by id for portals.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.team_builder_configs_id_portals_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_portals_get**
> list[Portal] team_builder_configs_id_portals_get(id, filter=filter)

Queries portals of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_portals_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_portals_post**
> Portal team_builder_configs_id_portals_post(id, data=data)

Creates a new instance in portals of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.team_builder_configs_id_portals_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_count_get**
> InlineResponse2001 team_builder_configs_id_product_groups_count_get(id, where=where)

Counts productGroups of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productGroups of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_groups_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_delete**
> team_builder_configs_id_product_groups_delete(id)

Deletes all productGroups of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id

try: 
    # Deletes all productGroups of this model.
    api_instance.team_builder_configs_id_product_groups_delete(id)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_fk_delete**
> team_builder_configs_id_product_groups_fk_delete(id, fk)

Delete a related item by id for productGroups.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Delete a related item by id for productGroups.
    api_instance.team_builder_configs_id_product_groups_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_fk_get**
> ProductGroup team_builder_configs_id_product_groups_fk_get(id, fk)

Find a related item by id for productGroups.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Find a related item by id for productGroups.
    api_response = api_instance.team_builder_configs_id_product_groups_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_fk_put**
> ProductGroup team_builder_configs_id_product_groups_fk_put(id, fk, data=data)

Update a related item by id for productGroups.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productGroups
data = TweakApi.ProductGroup() # ProductGroup |  (optional)

try: 
    # Update a related item by id for productGroups.
    api_response = api_instance.team_builder_configs_id_product_groups_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productGroups | 
 **data** | [**ProductGroup**](ProductGroup.md)|  | [optional] 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_get**
> list[ProductGroup] team_builder_configs_id_product_groups_get(id, filter=filter)

Queries productGroups of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productGroups of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_groups_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductGroup]**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_nk_types_count_get**
> InlineResponse2001 team_builder_configs_id_product_groups_nk_types_count_get(id, nk, where=where)

Counts types of ProductGroup.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productGroups.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts types of ProductGroup.
    api_response = api_instance.team_builder_configs_id_product_groups_nk_types_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_nk_types_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productGroups. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_nk_types_delete**
> team_builder_configs_id_product_groups_nk_types_delete(id, nk)

Deletes all types of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productGroups.

try: 
    # Deletes all types of this model.
    api_instance.team_builder_configs_id_product_groups_nk_types_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_nk_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productGroups. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_nk_types_fk_delete**
> team_builder_configs_id_product_groups_nk_types_fk_delete(id, nk, fk)

Delete a related item by id for types.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productGroups.
fk = 'fk_example' # str | Foreign key for types

try: 
    # Delete a related item by id for types.
    api_instance.team_builder_configs_id_product_groups_nk_types_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_nk_types_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productGroups. | 
 **fk** | **str**| Foreign key for types | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_nk_types_fk_get**
> ProductType team_builder_configs_id_product_groups_nk_types_fk_get(id, nk, fk)

Find a related item by id for types.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productGroups.
fk = 'fk_example' # str | Foreign key for types

try: 
    # Find a related item by id for types.
    api_response = api_instance.team_builder_configs_id_product_groups_nk_types_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_nk_types_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productGroups. | 
 **fk** | **str**| Foreign key for types | 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_nk_types_fk_put**
> ProductType team_builder_configs_id_product_groups_nk_types_fk_put(id, nk, fk, data=data)

Update a related item by id for types.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productGroups.
fk = 'fk_example' # str | Foreign key for types
data = TweakApi.ProductType() # ProductType |  (optional)

try: 
    # Update a related item by id for types.
    api_response = api_instance.team_builder_configs_id_product_groups_nk_types_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_nk_types_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productGroups. | 
 **fk** | **str**| Foreign key for types | 
 **data** | [**ProductType**](ProductType.md)|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_nk_types_get**
> list[ProductType] team_builder_configs_id_product_groups_nk_types_get(id, nk, filter=filter)

Queries types of ProductGroup.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productGroups.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries types of ProductGroup.
    api_response = api_instance.team_builder_configs_id_product_groups_nk_types_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_nk_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productGroups. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductType]**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_nk_types_post**
> ProductType team_builder_configs_id_product_groups_nk_types_post(id, nk, data=data)

Creates a new instance in types of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productGroups.
data = TweakApi.ProductType() # ProductType |  (optional)

try: 
    # Creates a new instance in types of this model.
    api_response = api_instance.team_builder_configs_id_product_groups_nk_types_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_nk_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productGroups. | 
 **data** | [**ProductType**](ProductType.md)|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_post**
> ProductGroup team_builder_configs_id_product_groups_post(id, data=data)

Creates a new instance in productGroups of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
data = TweakApi.ProductGroup() # ProductGroup |  (optional)

try: 
    # Creates a new instance in productGroups of this model.
    api_response = api_instance.team_builder_configs_id_product_groups_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **data** | [**ProductGroup**](ProductGroup.md)|  | [optional] 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_rel_fk_delete**
> team_builder_configs_id_product_groups_rel_fk_delete(id, fk)

Remove the productGroups relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Remove the productGroups relation to an item by id.
    api_instance.team_builder_configs_id_product_groups_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_rel_fk_head**
> bool team_builder_configs_id_product_groups_rel_fk_head(id, fk)

Check the existence of productGroups relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Check the existence of productGroups relation to an item by id.
    api_response = api_instance.team_builder_configs_id_product_groups_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_groups_rel_fk_put**
> TeamBuilderConfigProductGroup team_builder_configs_id_product_groups_rel_fk_put(id, fk, data=data)

Add a related item by id for productGroups.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productGroups
data = TweakApi.TeamBuilderConfigProductGroup() # TeamBuilderConfigProductGroup |  (optional)

try: 
    # Add a related item by id for productGroups.
    api_response = api_instance.team_builder_configs_id_product_groups_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_groups_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productGroups | 
 **data** | [**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)|  | [optional] 

### Return type

[**TeamBuilderConfigProductGroup**](TeamBuilderConfigProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_count_get**
> InlineResponse2001 team_builder_configs_id_product_size_materials_count_get(id, where=where)

Counts productSizeMaterials of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizeMaterials of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_size_materials_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_delete**
> team_builder_configs_id_product_size_materials_delete(id)

Deletes all productSizeMaterials of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id

try: 
    # Deletes all productSizeMaterials of this model.
    api_instance.team_builder_configs_id_product_size_materials_delete(id)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_fk_delete**
> team_builder_configs_id_product_size_materials_fk_delete(id, fk)

Delete a related item by id for productSizeMaterials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Delete a related item by id for productSizeMaterials.
    api_instance.team_builder_configs_id_product_size_materials_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_fk_get**
> ProductSizeMaterial team_builder_configs_id_product_size_materials_fk_get(id, fk)

Find a related item by id for productSizeMaterials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Find a related item by id for productSizeMaterials.
    api_response = api_instance.team_builder_configs_id_product_size_materials_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_fk_put**
> ProductSizeMaterial team_builder_configs_id_product_size_materials_fk_put(id, fk, data=data)

Update a related item by id for productSizeMaterials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for productSizeMaterials.
    api_response = api_instance.team_builder_configs_id_product_size_materials_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_get**
> list[ProductSizeMaterial] team_builder_configs_id_product_size_materials_get(id, filter=filter)

Queries productSizeMaterials of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizeMaterials of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_size_materials_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_nk_material_get**
> ProductMaterial team_builder_configs_id_product_size_materials_nk_material_get(id, nk, refresh=refresh)

Fetches belongsTo relation material.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation material.
    api_response = api_instance.team_builder_configs_id_product_size_materials_nk_material_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_nk_material_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizeMaterials. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get**
> ProductPdfColorProfile team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get(id, nk, refresh=refresh)

Fetches belongsTo relation pdfColorProfile.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation pdfColorProfile.
    api_response = api_instance.team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_nk_pdf_color_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizeMaterials. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_nk_size_get**
> ProductSize team_builder_configs_id_product_size_materials_nk_size_get(id, nk, refresh=refresh)

Fetches belongsTo relation size.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation size.
    api_response = api_instance.team_builder_configs_id_product_size_materials_nk_size_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_nk_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizeMaterials. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_nk_team_get**
> Team team_builder_configs_id_product_size_materials_nk_team_get(id, nk, refresh=refresh)

Fetches belongsTo relation team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.team_builder_configs_id_product_size_materials_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizeMaterials. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_post**
> ProductSizeMaterial team_builder_configs_id_product_size_materials_post(id, data=data)

Creates a new instance in productSizeMaterials of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in productSizeMaterials of this model.
    api_response = api_instance.team_builder_configs_id_product_size_materials_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_count_get**
> InlineResponse2001 team_builder_configs_id_product_size_materials_rel_count_get(id, where=where)

Counts productSizeMaterialsRel of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizeMaterialsRel of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_delete**
> team_builder_configs_id_product_size_materials_rel_delete(id)

Deletes all productSizeMaterialsRel of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id

try: 
    # Deletes all productSizeMaterialsRel of this model.
    api_instance.team_builder_configs_id_product_size_materials_rel_delete(id)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_fk_delete**
> team_builder_configs_id_product_size_materials_rel_fk_delete(id, fk)

Remove the productSizeMaterials relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Remove the productSizeMaterials relation to an item by id.
    api_instance.team_builder_configs_id_product_size_materials_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_fk_delete_0**
> team_builder_configs_id_product_size_materials_rel_fk_delete_0(id, fk)

Delete a related item by id for productSizeMaterialsRel.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterialsRel

try: 
    # Delete a related item by id for productSizeMaterialsRel.
    api_instance.team_builder_configs_id_product_size_materials_rel_fk_delete_0(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_fk_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterialsRel | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_fk_get**
> TeamBuilderConfigProductSizeMaterial team_builder_configs_id_product_size_materials_rel_fk_get(id, fk)

Find a related item by id for productSizeMaterialsRel.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterialsRel

try: 
    # Find a related item by id for productSizeMaterialsRel.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterialsRel | 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_fk_head**
> bool team_builder_configs_id_product_size_materials_rel_fk_head(id, fk)

Check the existence of productSizeMaterials relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Check the existence of productSizeMaterials relation to an item by id.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_fk_put**
> TeamBuilderConfigProductSizeMaterial team_builder_configs_id_product_size_materials_rel_fk_put(id, fk, data=data)

Add a related item by id for productSizeMaterials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterials
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial |  (optional)

try: 
    # Add a related item by id for productSizeMaterials.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)|  | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_fk_put_0**
> TeamBuilderConfigProductSizeMaterial team_builder_configs_id_product_size_materials_rel_fk_put_0(id, fk, data=data)

Update a related item by id for productSizeMaterialsRel.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizeMaterialsRel
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for productSizeMaterialsRel.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_fk_put_0(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_fk_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizeMaterialsRel | 
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)|  | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_get**
> list[TeamBuilderConfigProductSizeMaterial] team_builder_configs_id_product_size_materials_rel_get(id, filter=filter)

Queries productSizeMaterialsRel of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizeMaterialsRel of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamBuilderConfigProductSizeMaterial]**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_nk_builder_config_get**
> TeamBuilderConfig team_builder_configs_id_product_size_materials_rel_nk_builder_config_get(id, nk, refresh=refresh)

Fetches belongsTo relation builderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizeMaterialsRel.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation builderConfig.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_nk_builder_config_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_nk_builder_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizeMaterialsRel. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get**
> ProductPdfColorProfile team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get(id, nk, refresh=refresh)

Fetches belongsTo relation pdfColorProfile.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizeMaterialsRel.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation pdfColorProfile.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_nk_pdf_color_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizeMaterialsRel. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get**
> ProductSizeMaterial team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get(id, nk, refresh=refresh)

Fetches belongsTo relation productSizeMaterial.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizeMaterialsRel.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation productSizeMaterial.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_nk_product_size_material_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizeMaterialsRel. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_size_materials_rel_post**
> TeamBuilderConfigProductSizeMaterial team_builder_configs_id_product_size_materials_rel_post(id, data=data)

Creates a new instance in productSizeMaterialsRel of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in productSizeMaterialsRel of this model.
    api_response = api_instance.team_builder_configs_id_product_size_materials_rel_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_size_materials_rel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)|  | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_count_get**
> InlineResponse2001 team_builder_configs_id_product_sizes_count_get(id, where=where)

Counts productSizes of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizes of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_sizes_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_delete**
> team_builder_configs_id_product_sizes_delete(id)

Deletes all productSizes of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id

try: 
    # Deletes all productSizes of this model.
    api_instance.team_builder_configs_id_product_sizes_delete(id)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_fk_delete**
> team_builder_configs_id_product_sizes_fk_delete(id, fk)

Delete a related item by id for productSizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Delete a related item by id for productSizes.
    api_instance.team_builder_configs_id_product_sizes_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_fk_get**
> ProductSize team_builder_configs_id_product_sizes_fk_get(id, fk)

Find a related item by id for productSizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Find a related item by id for productSizes.
    api_response = api_instance.team_builder_configs_id_product_sizes_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_fk_put**
> ProductSize team_builder_configs_id_product_sizes_fk_put(id, fk, data=data)

Update a related item by id for productSizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizes
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Update a related item by id for productSizes.
    api_response = api_instance.team_builder_configs_id_product_sizes_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizes | 
 **data** | [**ProductSize**](ProductSize.md)|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_get**
> list[ProductSize] team_builder_configs_id_product_sizes_get(id, filter=filter)

Queries productSizes of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizes of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_sizes_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSize]**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_count_get**
> InlineResponse2001 team_builder_configs_id_product_sizes_nk_materials_count_get(id, nk, where=where)

Counts materials of ProductSize.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts materials of ProductSize.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_materials_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_delete**
> team_builder_configs_id_product_sizes_nk_materials_delete(id, nk)

Deletes all materials of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.

try: 
    # Deletes all materials of this model.
    api_instance.team_builder_configs_id_product_sizes_nk_materials_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_fk_delete**
> team_builder_configs_id_product_sizes_nk_materials_fk_delete(id, nk, fk)

Delete a related item by id for materials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Delete a related item by id for materials.
    api_instance.team_builder_configs_id_product_sizes_nk_materials_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for materials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_fk_get**
> ProductMaterial team_builder_configs_id_product_sizes_nk_materials_fk_get(id, nk, fk)

Find a related item by id for materials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Find a related item by id for materials.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_materials_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for materials | 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_fk_put**
> ProductMaterial team_builder_configs_id_product_sizes_nk_materials_fk_put(id, nk, fk, data=data)

Update a related item by id for materials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for materials
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Update a related item by id for materials.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_materials_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for materials | 
 **data** | [**ProductMaterial**](ProductMaterial.md)|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_get**
> list[ProductMaterial] team_builder_configs_id_product_sizes_nk_materials_get(id, nk, filter=filter)

Queries materials of ProductSize.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries materials of ProductSize.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_materials_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductMaterial]**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_post**
> ProductMaterial team_builder_configs_id_product_sizes_nk_materials_post(id, nk, data=data)

Creates a new instance in materials of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Creates a new instance in materials of this model.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_materials_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **data** | [**ProductMaterial**](ProductMaterial.md)|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete**
> team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete(id, nk, fk)

Remove the materials relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Remove the materials relation to an item by id.
    api_instance.team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for materials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_rel_fk_head**
> bool team_builder_configs_id_product_sizes_nk_materials_rel_fk_head(id, nk, fk)

Check the existence of materials relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for materials

try: 
    # Check the existence of materials relation to an item by id.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_materials_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for materials | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_materials_rel_fk_put**
> ProductSizeMaterial team_builder_configs_id_product_sizes_nk_materials_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for materials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for materials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Add a related item by id for materials.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_materials_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_materials_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for materials | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_pdf_color_profile_get**
> ProductPdfColorProfile team_builder_configs_id_product_sizes_nk_pdf_color_profile_get(id, nk, refresh=refresh)

Fetches belongsTo relation pdfColorProfile.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation pdfColorProfile.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_pdf_color_profile_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_pdf_color_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_products_count_get**
> InlineResponse2001 team_builder_configs_id_product_sizes_nk_products_count_get(id, nk, where=where)

Counts products of ProductSize.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts products of ProductSize.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_products_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_products_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_products_delete**
> team_builder_configs_id_product_sizes_nk_products_delete(id, nk)

Deletes all products of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.

try: 
    # Deletes all products of this model.
    api_instance.team_builder_configs_id_product_sizes_nk_products_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_products_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_products_fk_delete**
> team_builder_configs_id_product_sizes_nk_products_fk_delete(id, nk, fk)

Delete a related item by id for products.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for products

try: 
    # Delete a related item by id for products.
    api_instance.team_builder_configs_id_product_sizes_nk_products_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_products_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for products | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_products_fk_get**
> Product team_builder_configs_id_product_sizes_nk_products_fk_get(id, nk, fk)

Find a related item by id for products.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for products

try: 
    # Find a related item by id for products.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_products_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_products_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for products | 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_products_fk_put**
> Product team_builder_configs_id_product_sizes_nk_products_fk_put(id, nk, fk, data=data)

Update a related item by id for products.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for products
data = TweakApi.Product() # Product |  (optional)

try: 
    # Update a related item by id for products.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_products_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_products_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for products | 
 **data** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_products_get**
> list[Product] team_builder_configs_id_product_sizes_nk_products_get(id, nk, filter=filter)

Queries products of ProductSize.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries products of ProductSize.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_products_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Product]**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_products_post**
> Product team_builder_configs_id_product_sizes_nk_products_post(id, nk, data=data)

Creates a new instance in products of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
data = TweakApi.Product() # Product |  (optional)

try: 
    # Creates a new instance in products of this model.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_products_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **data** | [**Product**](Product.md)|  | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_size_materials_count_get**
> InlineResponse2001 team_builder_configs_id_product_sizes_nk_size_materials_count_get(id, nk, where=where)

Counts sizeMaterials of ProductSize.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts sizeMaterials of ProductSize.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_size_materials_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_size_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_size_materials_delete**
> team_builder_configs_id_product_sizes_nk_size_materials_delete(id, nk)

Deletes all sizeMaterials of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.

try: 
    # Deletes all sizeMaterials of this model.
    api_instance.team_builder_configs_id_product_sizes_nk_size_materials_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_size_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_size_materials_fk_delete**
> team_builder_configs_id_product_sizes_nk_size_materials_fk_delete(id, nk, fk)

Delete a related item by id for sizeMaterials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for sizeMaterials

try: 
    # Delete a related item by id for sizeMaterials.
    api_instance.team_builder_configs_id_product_sizes_nk_size_materials_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_size_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for sizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_size_materials_fk_get**
> ProductSizeMaterial team_builder_configs_id_product_sizes_nk_size_materials_fk_get(id, nk, fk)

Find a related item by id for sizeMaterials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for sizeMaterials

try: 
    # Find a related item by id for sizeMaterials.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_size_materials_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_size_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for sizeMaterials | 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_size_materials_fk_put**
> ProductSizeMaterial team_builder_configs_id_product_sizes_nk_size_materials_fk_put(id, nk, fk, data=data)

Update a related item by id for sizeMaterials.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
fk = 'fk_example' # str | Foreign key for sizeMaterials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for sizeMaterials.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_size_materials_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_size_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **fk** | **str**| Foreign key for sizeMaterials | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_size_materials_get**
> list[ProductSizeMaterial] team_builder_configs_id_product_sizes_nk_size_materials_get(id, nk, filter=filter)

Queries sizeMaterials of ProductSize.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries sizeMaterials of ProductSize.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_size_materials_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_size_materials_post**
> ProductSizeMaterial team_builder_configs_id_product_sizes_nk_size_materials_post(id, nk, data=data)

Creates a new instance in sizeMaterials of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in sizeMaterials of this model.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_size_materials_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_nk_type_get**
> ProductType team_builder_configs_id_product_sizes_nk_type_get(id, nk, refresh=refresh)

Fetches belongsTo relation type.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productSizes.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation type.
    api_response = api_instance.team_builder_configs_id_product_sizes_nk_type_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_nk_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productSizes. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_post**
> ProductSize team_builder_configs_id_product_sizes_post(id, data=data)

Creates a new instance in productSizes of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Creates a new instance in productSizes of this model.
    api_response = api_instance.team_builder_configs_id_product_sizes_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **data** | [**ProductSize**](ProductSize.md)|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_rel_fk_delete**
> team_builder_configs_id_product_sizes_rel_fk_delete(id, fk)

Remove the productSizes relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Remove the productSizes relation to an item by id.
    api_instance.team_builder_configs_id_product_sizes_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_rel_fk_head**
> bool team_builder_configs_id_product_sizes_rel_fk_head(id, fk)

Check the existence of productSizes relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Check the existence of productSizes relation to an item by id.
    api_response = api_instance.team_builder_configs_id_product_sizes_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_sizes_rel_fk_put**
> TeamBuilderConfigProductSize team_builder_configs_id_product_sizes_rel_fk_put(id, fk, data=data)

Add a related item by id for productSizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productSizes
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize |  (optional)

try: 
    # Add a related item by id for productSizes.
    api_response = api_instance.team_builder_configs_id_product_sizes_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_sizes_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productSizes | 
 **data** | [**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)|  | [optional] 

### Return type

[**TeamBuilderConfigProductSize**](TeamBuilderConfigProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_count_get**
> InlineResponse2001 team_builder_configs_id_product_types_count_get(id, where=where)

Counts productTypes of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productTypes of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_types_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_delete**
> team_builder_configs_id_product_types_delete(id)

Deletes all productTypes of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id

try: 
    # Deletes all productTypes of this model.
    api_instance.team_builder_configs_id_product_types_delete(id)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_fk_delete**
> team_builder_configs_id_product_types_fk_delete(id, fk)

Delete a related item by id for productTypes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Delete a related item by id for productTypes.
    api_instance.team_builder_configs_id_product_types_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_fk_get**
> ProductType team_builder_configs_id_product_types_fk_get(id, fk)

Find a related item by id for productTypes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Find a related item by id for productTypes.
    api_response = api_instance.team_builder_configs_id_product_types_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_fk_put**
> ProductType team_builder_configs_id_product_types_fk_put(id, fk, data=data)

Update a related item by id for productTypes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productTypes
data = TweakApi.ProductType() # ProductType |  (optional)

try: 
    # Update a related item by id for productTypes.
    api_response = api_instance.team_builder_configs_id_product_types_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productTypes | 
 **data** | [**ProductType**](ProductType.md)|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_get**
> list[ProductType] team_builder_configs_id_product_types_get(id, filter=filter)

Queries productTypes of TeamBuilderConfig.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productTypes of TeamBuilderConfig.
    api_response = api_instance.team_builder_configs_id_product_types_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductType]**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_group_get**
> ProductGroup team_builder_configs_id_product_types_nk_group_get(id, nk, refresh=refresh)

Fetches belongsTo relation group.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation group.
    api_response = api_instance.team_builder_configs_id_product_types_nk_group_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_sizes_count_get**
> InlineResponse2001 team_builder_configs_id_product_types_nk_sizes_count_get(id, nk, where=where)

Counts sizes of ProductType.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts sizes of ProductType.
    api_response = api_instance.team_builder_configs_id_product_types_nk_sizes_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_sizes_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_sizes_delete**
> team_builder_configs_id_product_types_nk_sizes_delete(id, nk)

Deletes all sizes of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.

try: 
    # Deletes all sizes of this model.
    api_instance.team_builder_configs_id_product_types_nk_sizes_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_sizes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_sizes_fk_delete**
> team_builder_configs_id_product_types_nk_sizes_fk_delete(id, nk, fk)

Delete a related item by id for sizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.
fk = 'fk_example' # str | Foreign key for sizes

try: 
    # Delete a related item by id for sizes.
    api_instance.team_builder_configs_id_product_types_nk_sizes_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_sizes_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 
 **fk** | **str**| Foreign key for sizes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_sizes_fk_get**
> ProductSize team_builder_configs_id_product_types_nk_sizes_fk_get(id, nk, fk)

Find a related item by id for sizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.
fk = 'fk_example' # str | Foreign key for sizes

try: 
    # Find a related item by id for sizes.
    api_response = api_instance.team_builder_configs_id_product_types_nk_sizes_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_sizes_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 
 **fk** | **str**| Foreign key for sizes | 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_sizes_fk_put**
> ProductSize team_builder_configs_id_product_types_nk_sizes_fk_put(id, nk, fk, data=data)

Update a related item by id for sizes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.
fk = 'fk_example' # str | Foreign key for sizes
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Update a related item by id for sizes.
    api_response = api_instance.team_builder_configs_id_product_types_nk_sizes_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_sizes_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 
 **fk** | **str**| Foreign key for sizes | 
 **data** | [**ProductSize**](ProductSize.md)|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_sizes_get**
> list[ProductSize] team_builder_configs_id_product_types_nk_sizes_get(id, nk, filter=filter)

Queries sizes of ProductType.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries sizes of ProductType.
    api_response = api_instance.team_builder_configs_id_product_types_nk_sizes_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_sizes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSize]**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_nk_sizes_post**
> ProductSize team_builder_configs_id_product_types_nk_sizes_post(id, nk, data=data)

Creates a new instance in sizes of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
nk = 'nk_example' # str | Foreign key for productTypes.
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Creates a new instance in sizes of this model.
    api_response = api_instance.team_builder_configs_id_product_types_nk_sizes_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_nk_sizes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **nk** | **str**| Foreign key for productTypes. | 
 **data** | [**ProductSize**](ProductSize.md)|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_post**
> ProductType team_builder_configs_id_product_types_post(id, data=data)

Creates a new instance in productTypes of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
data = TweakApi.ProductType() # ProductType |  (optional)

try: 
    # Creates a new instance in productTypes of this model.
    api_response = api_instance.team_builder_configs_id_product_types_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **data** | [**ProductType**](ProductType.md)|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_rel_fk_delete**
> team_builder_configs_id_product_types_rel_fk_delete(id, fk)

Remove the productTypes relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Remove the productTypes relation to an item by id.
    api_instance.team_builder_configs_id_product_types_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_rel_fk_head**
> bool team_builder_configs_id_product_types_rel_fk_head(id, fk)

Check the existence of productTypes relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Check the existence of productTypes relation to an item by id.
    api_response = api_instance.team_builder_configs_id_product_types_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_product_types_rel_fk_put**
> TeamBuilderConfigProductType team_builder_configs_id_product_types_rel_fk_put(id, fk, data=data)

Add a related item by id for productTypes.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
fk = 'fk_example' # str | Foreign key for productTypes
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType |  (optional)

try: 
    # Add a related item by id for productTypes.
    api_response = api_instance.team_builder_configs_id_product_types_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_product_types_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **fk** | **str**| Foreign key for productTypes | 
 **data** | [**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)|  | [optional] 

### Return type

[**TeamBuilderConfigProductType**](TeamBuilderConfigProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_put**
> TeamBuilderConfig team_builder_configs_id_put(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_configs_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_replace_post**
> TeamBuilderConfig team_builder_configs_id_replace_post(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_builder_configs_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_id_team_get**
> Team team_builder_configs_id_team_get(id, refresh=refresh)

Fetches belongsTo relation team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
id = 'id_example' # str | TeamBuilderConfig id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.team_builder_configs_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamBuilderConfig id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_patch**
> TeamBuilderConfig team_builder_configs_patch(data=data)

Patch an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_configs_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_post**
> TeamBuilderConfig team_builder_configs_post(data=data)

Create a new instance of the model and persist it into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.team_builder_configs_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_put**
> TeamBuilderConfig team_builder_configs_put(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_configs_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_replace_or_create_post**
> TeamBuilderConfig team_builder_configs_replace_or_create_post(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_builder_configs_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| Model instance data | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_update_post**
> InlineResponse2003 team_builder_configs_update_post(where=where, data=data)

Update instances of the model matched by {{where}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.team_builder_configs_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_builder_configs_upsert_with_where_post**
> TeamBuilderConfig team_builder_configs_upsert_with_where_post(where=where, data=data)

Update an existing model instance or insert a new one into the data source based on the where criteria.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamBuilderConfigApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.team_builder_configs_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBuilderConfigApi->team_builder_configs_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

