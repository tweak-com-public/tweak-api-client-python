# TweakApi.TeamApi

All URIs are relative to *https://apicdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_change_stream_get**](TeamApi.md#teams_change_stream_get) | **GET** /Teams/change-stream | Create a change stream.
[**teams_change_stream_post**](TeamApi.md#teams_change_stream_post) | **POST** /Teams/change-stream | Create a change stream.
[**teams_count_get**](TeamApi.md#teams_count_get) | **GET** /Teams/count | Count instances of the model matched by where from the data source.
[**teams_find_one_get**](TeamApi.md#teams_find_one_get) | **GET** /Teams/findOne | Find first instance of the model matched by filter from the data source.
[**teams_get**](TeamApi.md#teams_get) | **GET** /Teams | Find all instances of the model matched by filter from the data source.
[**teams_id_auth_reset_keys_delete**](TeamApi.md#teams_id_auth_reset_keys_delete) | **DELETE** /Teams/{id}/auth/reset-keys | Reset Team keys
[**teams_id_brand_delete**](TeamApi.md#teams_id_brand_delete) | **DELETE** /Teams/{id}/brand | Deletes brand of this model.
[**teams_id_brand_get**](TeamApi.md#teams_id_brand_get) | **GET** /Teams/{id}/brand | Fetches hasOne relation brand.
[**teams_id_brand_post**](TeamApi.md#teams_id_brand_post) | **POST** /Teams/{id}/brand | Creates a new instance in brand of this model.
[**teams_id_brand_put**](TeamApi.md#teams_id_brand_put) | **PUT** /Teams/{id}/brand | Update brand of this model.
[**teams_id_builder_configs_count_get**](TeamApi.md#teams_id_builder_configs_count_get) | **GET** /Teams/{id}/builderConfigs/count | Counts builderConfigs of Team.
[**teams_id_builder_configs_default_get**](TeamApi.md#teams_id_builder_configs_default_get) | **GET** /Teams/{id}/builderConfigs/default | Get default TeamBuilderConfig for this Team
[**teams_id_builder_configs_default_product_size_materials_get**](TeamApi.md#teams_id_builder_configs_default_product_size_materials_get) | **GET** /Teams/{id}/builderConfigs/default/productSizeMaterials | Get default TeamBuilderConfig ProductSizeMaterials for this Team
[**teams_id_builder_configs_delete**](TeamApi.md#teams_id_builder_configs_delete) | **DELETE** /Teams/{id}/builderConfigs | Deletes all builderConfigs of this model.
[**teams_id_builder_configs_fk_delete**](TeamApi.md#teams_id_builder_configs_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{fk} | Delete a related item by id for builderConfigs.
[**teams_id_builder_configs_fk_get**](TeamApi.md#teams_id_builder_configs_fk_get) | **GET** /Teams/{id}/builderConfigs/{fk} | Find a related item by id for builderConfigs.
[**teams_id_builder_configs_fk_logo_put**](TeamApi.md#teams_id_builder_configs_fk_logo_put) | **PUT** /Teams/{id}/builderConfigs/{fk}/logo | Change Builder Config logo
[**teams_id_builder_configs_fk_put**](TeamApi.md#teams_id_builder_configs_fk_put) | **PUT** /Teams/{id}/builderConfigs/{fk} | Update a related item by id for builderConfigs.
[**teams_id_builder_configs_fk_watermark_put**](TeamApi.md#teams_id_builder_configs_fk_watermark_put) | **PUT** /Teams/{id}/builderConfigs/{fk}/watermark | Change Builder Config watermark
[**teams_id_builder_configs_get**](TeamApi.md#teams_id_builder_configs_get) | **GET** /Teams/{id}/builderConfigs | Queries builderConfigs of Team.
[**teams_id_builder_configs_nk_portals_count_get**](TeamApi.md#teams_id_builder_configs_nk_portals_count_get) | **GET** /Teams/{id}/builderConfigs/{nk}/portals/count | Counts portals of TeamBuilderConfig.
[**teams_id_builder_configs_nk_portals_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_portals_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/portals/{fk} | Delete a related item by id for portals.
[**teams_id_builder_configs_nk_portals_fk_get**](TeamApi.md#teams_id_builder_configs_nk_portals_fk_get) | **GET** /Teams/{id}/builderConfigs/{nk}/portals/{fk} | Find a related item by id for portals.
[**teams_id_builder_configs_nk_portals_fk_put**](TeamApi.md#teams_id_builder_configs_nk_portals_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/portals/{fk} | Update a related item by id for portals.
[**teams_id_builder_configs_nk_portals_get**](TeamApi.md#teams_id_builder_configs_nk_portals_get) | **GET** /Teams/{id}/builderConfigs/{nk}/portals | Queries portals of TeamBuilderConfig.
[**teams_id_builder_configs_nk_portals_post**](TeamApi.md#teams_id_builder_configs_nk_portals_post) | **POST** /Teams/{id}/builderConfigs/{nk}/portals | Creates a new instance in portals of this model.
[**teams_id_builder_configs_nk_product_groups_count_get**](TeamApi.md#teams_id_builder_configs_nk_product_groups_count_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productGroups/count | Counts productGroups of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_groups_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_groups_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productGroups/{fk} | Delete a related item by id for productGroups.
[**teams_id_builder_configs_nk_product_groups_fk_get**](TeamApi.md#teams_id_builder_configs_nk_product_groups_fk_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productGroups/{fk} | Find a related item by id for productGroups.
[**teams_id_builder_configs_nk_product_groups_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_groups_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productGroups/{fk} | Update a related item by id for productGroups.
[**teams_id_builder_configs_nk_product_groups_get**](TeamApi.md#teams_id_builder_configs_nk_product_groups_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productGroups | Queries productGroups of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_groups_post**](TeamApi.md#teams_id_builder_configs_nk_product_groups_post) | **POST** /Teams/{id}/builderConfigs/{nk}/productGroups | Creates a new instance in productGroups of this model.
[**teams_id_builder_configs_nk_product_groups_rel_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_groups_rel_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productGroups/rel/{fk} | Remove the productGroups relation to an item by id.
[**teams_id_builder_configs_nk_product_groups_rel_fk_head**](TeamApi.md#teams_id_builder_configs_nk_product_groups_rel_fk_head) | **HEAD** /Teams/{id}/builderConfigs/{nk}/productGroups/rel/{fk} | Check the existence of productGroups relation to an item by id.
[**teams_id_builder_configs_nk_product_groups_rel_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_groups_rel_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productGroups/rel/{fk} | Add a related item by id for productGroups.
[**teams_id_builder_configs_nk_product_size_materials_count_get**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_count_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials/count | Counts productSizeMaterials of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_size_materials_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials/{fk} | Delete a related item by id for productSizeMaterials.
[**teams_id_builder_configs_nk_product_size_materials_fk_get**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_fk_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials/{fk} | Find a related item by id for productSizeMaterials.
[**teams_id_builder_configs_nk_product_size_materials_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials/{fk} | Update a related item by id for productSizeMaterials.
[**teams_id_builder_configs_nk_product_size_materials_get**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials | Queries productSizeMaterials of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_size_materials_post**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_post) | **POST** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials | Creates a new instance in productSizeMaterials of this model.
[**teams_id_builder_configs_nk_product_size_materials_rel_count_get**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_count_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizeMaterialsRel/count | Counts productSizeMaterialsRel of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_size_materials_rel_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials/rel/{fk} | Remove the productSizeMaterials relation to an item by id.
[**teams_id_builder_configs_nk_product_size_materials_rel_fk_delete_0**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_fk_delete_0) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productSizeMaterialsRel/{fk} | Delete a related item by id for productSizeMaterialsRel.
[**teams_id_builder_configs_nk_product_size_materials_rel_fk_get**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_fk_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizeMaterialsRel/{fk} | Find a related item by id for productSizeMaterialsRel.
[**teams_id_builder_configs_nk_product_size_materials_rel_fk_head**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_fk_head) | **HEAD** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials/rel/{fk} | Check the existence of productSizeMaterials relation to an item by id.
[**teams_id_builder_configs_nk_product_size_materials_rel_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productSizeMaterials/rel/{fk} | Add a related item by id for productSizeMaterials.
[**teams_id_builder_configs_nk_product_size_materials_rel_fk_put_0**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_fk_put_0) | **PUT** /Teams/{id}/builderConfigs/{nk}/productSizeMaterialsRel/{fk} | Update a related item by id for productSizeMaterialsRel.
[**teams_id_builder_configs_nk_product_size_materials_rel_get**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizeMaterialsRel | Queries productSizeMaterialsRel of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_size_materials_rel_post**](TeamApi.md#teams_id_builder_configs_nk_product_size_materials_rel_post) | **POST** /Teams/{id}/builderConfigs/{nk}/productSizeMaterialsRel | Creates a new instance in productSizeMaterialsRel of this model.
[**teams_id_builder_configs_nk_product_sizes_count_get**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_count_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizes/count | Counts productSizes of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_sizes_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productSizes/{fk} | Delete a related item by id for productSizes.
[**teams_id_builder_configs_nk_product_sizes_fk_get**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_fk_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizes/{fk} | Find a related item by id for productSizes.
[**teams_id_builder_configs_nk_product_sizes_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productSizes/{fk} | Update a related item by id for productSizes.
[**teams_id_builder_configs_nk_product_sizes_get**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productSizes | Queries productSizes of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_sizes_post**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_post) | **POST** /Teams/{id}/builderConfigs/{nk}/productSizes | Creates a new instance in productSizes of this model.
[**teams_id_builder_configs_nk_product_sizes_rel_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_rel_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productSizes/rel/{fk} | Remove the productSizes relation to an item by id.
[**teams_id_builder_configs_nk_product_sizes_rel_fk_head**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_rel_fk_head) | **HEAD** /Teams/{id}/builderConfigs/{nk}/productSizes/rel/{fk} | Check the existence of productSizes relation to an item by id.
[**teams_id_builder_configs_nk_product_sizes_rel_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_sizes_rel_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productSizes/rel/{fk} | Add a related item by id for productSizes.
[**teams_id_builder_configs_nk_product_types_count_get**](TeamApi.md#teams_id_builder_configs_nk_product_types_count_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productTypes/count | Counts productTypes of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_types_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_types_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productTypes/{fk} | Delete a related item by id for productTypes.
[**teams_id_builder_configs_nk_product_types_fk_get**](TeamApi.md#teams_id_builder_configs_nk_product_types_fk_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productTypes/{fk} | Find a related item by id for productTypes.
[**teams_id_builder_configs_nk_product_types_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_types_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productTypes/{fk} | Update a related item by id for productTypes.
[**teams_id_builder_configs_nk_product_types_get**](TeamApi.md#teams_id_builder_configs_nk_product_types_get) | **GET** /Teams/{id}/builderConfigs/{nk}/productTypes | Queries productTypes of TeamBuilderConfig.
[**teams_id_builder_configs_nk_product_types_post**](TeamApi.md#teams_id_builder_configs_nk_product_types_post) | **POST** /Teams/{id}/builderConfigs/{nk}/productTypes | Creates a new instance in productTypes of this model.
[**teams_id_builder_configs_nk_product_types_rel_fk_delete**](TeamApi.md#teams_id_builder_configs_nk_product_types_rel_fk_delete) | **DELETE** /Teams/{id}/builderConfigs/{nk}/productTypes/rel/{fk} | Remove the productTypes relation to an item by id.
[**teams_id_builder_configs_nk_product_types_rel_fk_head**](TeamApi.md#teams_id_builder_configs_nk_product_types_rel_fk_head) | **HEAD** /Teams/{id}/builderConfigs/{nk}/productTypes/rel/{fk} | Check the existence of productTypes relation to an item by id.
[**teams_id_builder_configs_nk_product_types_rel_fk_put**](TeamApi.md#teams_id_builder_configs_nk_product_types_rel_fk_put) | **PUT** /Teams/{id}/builderConfigs/{nk}/productTypes/rel/{fk} | Add a related item by id for productTypes.
[**teams_id_builder_configs_nk_team_get**](TeamApi.md#teams_id_builder_configs_nk_team_get) | **GET** /Teams/{id}/builderConfigs/{nk}/team | Fetches belongsTo relation team.
[**teams_id_builder_configs_post**](TeamApi.md#teams_id_builder_configs_post) | **POST** /Teams/{id}/builderConfigs | Creates a new instance in builderConfigs of this model.
[**teams_id_data_source_soaps_count_get**](TeamApi.md#teams_id_data_source_soaps_count_get) | **GET** /Teams/{id}/dataSourceSoaps/count | Counts dataSourceSoaps of Team.
[**teams_id_data_source_soaps_fk_delete**](TeamApi.md#teams_id_data_source_soaps_fk_delete) | **DELETE** /Teams/{id}/dataSourceSoaps/{fk} | Delete a related item by id for dataSourceSoaps.
[**teams_id_data_source_soaps_fk_get**](TeamApi.md#teams_id_data_source_soaps_fk_get) | **GET** /Teams/{id}/dataSourceSoaps/{fk} | Find a related item by id for dataSourceSoaps.
[**teams_id_data_source_soaps_fk_put**](TeamApi.md#teams_id_data_source_soaps_fk_put) | **PUT** /Teams/{id}/dataSourceSoaps/{fk} | Update a related item by id for dataSourceSoaps.
[**teams_id_data_source_soaps_get**](TeamApi.md#teams_id_data_source_soaps_get) | **GET** /Teams/{id}/dataSourceSoaps | Queries dataSourceSoaps of Team.
[**teams_id_data_source_soaps_nk_dynamic_datas_count_get**](TeamApi.md#teams_id_data_source_soaps_nk_dynamic_datas_count_get) | **GET** /Teams/{id}/dataSourceSoaps/{nk}/dynamicDatas/count | Counts dynamicDatas of DataSourceSoap.
[**teams_id_data_source_soaps_nk_dynamic_datas_delete**](TeamApi.md#teams_id_data_source_soaps_nk_dynamic_datas_delete) | **DELETE** /Teams/{id}/dataSourceSoaps/{nk}/dynamicDatas | Deletes all dynamicDatas of this model.
[**teams_id_data_source_soaps_nk_dynamic_datas_fk_delete**](TeamApi.md#teams_id_data_source_soaps_nk_dynamic_datas_fk_delete) | **DELETE** /Teams/{id}/dataSourceSoaps/{nk}/dynamicDatas/{fk} | Delete a related item by id for dynamicDatas.
[**teams_id_data_source_soaps_nk_dynamic_datas_fk_get**](TeamApi.md#teams_id_data_source_soaps_nk_dynamic_datas_fk_get) | **GET** /Teams/{id}/dataSourceSoaps/{nk}/dynamicDatas/{fk} | Find a related item by id for dynamicDatas.
[**teams_id_data_source_soaps_nk_dynamic_datas_fk_put**](TeamApi.md#teams_id_data_source_soaps_nk_dynamic_datas_fk_put) | **PUT** /Teams/{id}/dataSourceSoaps/{nk}/dynamicDatas/{fk} | Update a related item by id for dynamicDatas.
[**teams_id_data_source_soaps_nk_dynamic_datas_get**](TeamApi.md#teams_id_data_source_soaps_nk_dynamic_datas_get) | **GET** /Teams/{id}/dataSourceSoaps/{nk}/dynamicDatas | Queries dynamicDatas of DataSourceSoap.
[**teams_id_data_source_soaps_nk_dynamic_datas_post**](TeamApi.md#teams_id_data_source_soaps_nk_dynamic_datas_post) | **POST** /Teams/{id}/dataSourceSoaps/{nk}/dynamicDatas | Creates a new instance in dynamicDatas of this model.
[**teams_id_data_source_soaps_nk_team_get**](TeamApi.md#teams_id_data_source_soaps_nk_team_get) | **GET** /Teams/{id}/dataSourceSoaps/{nk}/team | Fetches belongsTo relation team.
[**teams_id_data_source_soaps_post**](TeamApi.md#teams_id_data_source_soaps_post) | **POST** /Teams/{id}/dataSourceSoaps | Creates a new instance in dataSourceSoaps of this model.
[**teams_id_delete**](TeamApi.md#teams_id_delete) | **DELETE** /Teams/{id} | Delete a model instance by {{id}} from the data source.
[**teams_id_dynamic_datas_count_get**](TeamApi.md#teams_id_dynamic_datas_count_get) | **GET** /Teams/{id}/dynamicDatas/count | Counts dynamicDatas of Team.
[**teams_id_dynamic_datas_fk_delete**](TeamApi.md#teams_id_dynamic_datas_fk_delete) | **DELETE** /Teams/{id}/dynamicDatas/{fk} | Delete a related item by id for dynamicDatas.
[**teams_id_dynamic_datas_fk_get**](TeamApi.md#teams_id_dynamic_datas_fk_get) | **GET** /Teams/{id}/dynamicDatas/{fk} | Find a related item by id for dynamicDatas.
[**teams_id_dynamic_datas_fk_put**](TeamApi.md#teams_id_dynamic_datas_fk_put) | **PUT** /Teams/{id}/dynamicDatas/{fk} | Update a related item by id for dynamicDatas.
[**teams_id_dynamic_datas_get**](TeamApi.md#teams_id_dynamic_datas_get) | **GET** /Teams/{id}/dynamicDatas | Queries dynamicDatas of Team.
[**teams_id_dynamic_datas_nk_data_source_mongo_get**](TeamApi.md#teams_id_dynamic_datas_nk_data_source_mongo_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/dataSourceMongo | Fetches belongsTo relation dataSourceMongo.
[**teams_id_dynamic_datas_nk_data_source_ms_sql_get**](TeamApi.md#teams_id_dynamic_datas_nk_data_source_ms_sql_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/dataSourceMsSql | Fetches belongsTo relation dataSourceMsSql.
[**teams_id_dynamic_datas_nk_data_source_my_sql_get**](TeamApi.md#teams_id_dynamic_datas_nk_data_source_my_sql_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/dataSourceMySql | Fetches belongsTo relation dataSourceMySql.
[**teams_id_dynamic_datas_nk_data_source_oracle_get**](TeamApi.md#teams_id_dynamic_datas_nk_data_source_oracle_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/dataSourceOracle | Fetches belongsTo relation dataSourceOracle.
[**teams_id_dynamic_datas_nk_data_source_postgre_sql_get**](TeamApi.md#teams_id_dynamic_datas_nk_data_source_postgre_sql_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/dataSourcePostgreSql | Fetches belongsTo relation dataSourcePostgreSql.
[**teams_id_dynamic_datas_nk_data_source_rest_get**](TeamApi.md#teams_id_dynamic_datas_nk_data_source_rest_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/dataSourceRest | Fetches belongsTo relation dataSourceRest.
[**teams_id_dynamic_datas_nk_data_source_soap_get**](TeamApi.md#teams_id_dynamic_datas_nk_data_source_soap_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/dataSourceSoap | Fetches belongsTo relation dataSourceSoap.
[**teams_id_dynamic_datas_nk_designs_count_get**](TeamApi.md#teams_id_dynamic_datas_nk_designs_count_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/designs/count | Counts designs of DynamicData.
[**teams_id_dynamic_datas_nk_designs_fk_delete**](TeamApi.md#teams_id_dynamic_datas_nk_designs_fk_delete) | **DELETE** /Teams/{id}/dynamicDatas/{nk}/designs/{fk} | Delete a related item by id for designs.
[**teams_id_dynamic_datas_nk_designs_fk_get**](TeamApi.md#teams_id_dynamic_datas_nk_designs_fk_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/designs/{fk} | Find a related item by id for designs.
[**teams_id_dynamic_datas_nk_designs_fk_put**](TeamApi.md#teams_id_dynamic_datas_nk_designs_fk_put) | **PUT** /Teams/{id}/dynamicDatas/{nk}/designs/{fk} | Update a related item by id for designs.
[**teams_id_dynamic_datas_nk_designs_get**](TeamApi.md#teams_id_dynamic_datas_nk_designs_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/designs | Queries designs of DynamicData.
[**teams_id_dynamic_datas_nk_designs_post**](TeamApi.md#teams_id_dynamic_datas_nk_designs_post) | **POST** /Teams/{id}/dynamicDatas/{nk}/designs | Creates a new instance in designs of this model.
[**teams_id_dynamic_datas_nk_records_count_get**](TeamApi.md#teams_id_dynamic_datas_nk_records_count_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/records/count | Count Dynamic Data records
[**teams_id_dynamic_datas_nk_records_delete**](TeamApi.md#teams_id_dynamic_datas_nk_records_delete) | **DELETE** /Teams/{id}/dynamicDatas/{nk}/records | Delete all matching records.
[**teams_id_dynamic_datas_nk_records_fk_delete**](TeamApi.md#teams_id_dynamic_datas_nk_records_fk_delete) | **DELETE** /Teams/{id}/dynamicDatas/{nk}/records/{fk} | Delete a model instance by {{fk}} from the data source.
[**teams_id_dynamic_datas_nk_records_fk_get**](TeamApi.md#teams_id_dynamic_datas_nk_records_fk_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/records/{fk} | Find a model instance by {{fk}} from the data source.
[**teams_id_dynamic_datas_nk_records_fk_property_name_upload_put**](TeamApi.md#teams_id_dynamic_datas_nk_records_fk_property_name_upload_put) | **PUT** /Teams/{id}/dynamicDatas/{nk}/records/{fk}/{propertyName}/upload | Replace attributes for a model instance and persist it into the data source.
[**teams_id_dynamic_datas_nk_records_fk_put**](TeamApi.md#teams_id_dynamic_datas_nk_records_fk_put) | **PUT** /Teams/{id}/dynamicDatas/{nk}/records/{fk} | Replace attributes for a model instance and persist it into the data source.
[**teams_id_dynamic_datas_nk_records_get**](TeamApi.md#teams_id_dynamic_datas_nk_records_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/records | Find all instances of the model matched by filter from the data source.
[**teams_id_dynamic_datas_nk_records_migrate_post**](TeamApi.md#teams_id_dynamic_datas_nk_records_migrate_post) | **POST** /Teams/{id}/dynamicDatas/{nk}/records/migrate | Request migration for Dynamic Data records
[**teams_id_dynamic_datas_nk_records_post**](TeamApi.md#teams_id_dynamic_datas_nk_records_post) | **POST** /Teams/{id}/dynamicDatas/{nk}/records | Create a new instance of the model and persist it into the data source.
[**teams_id_dynamic_datas_nk_records_upload_csv_post**](TeamApi.md#teams_id_dynamic_datas_nk_records_upload_csv_post) | **POST** /Teams/{id}/dynamicDatas/{nk}/records/upload/csv | Upload CSV for this Dynamic Data
[**teams_id_dynamic_datas_nk_team_get**](TeamApi.md#teams_id_dynamic_datas_nk_team_get) | **GET** /Teams/{id}/dynamicDatas/{nk}/team | Fetches belongsTo relation team.
[**teams_id_dynamic_datas_post**](TeamApi.md#teams_id_dynamic_datas_post) | **POST** /Teams/{id}/dynamicDatas | Creates a new instance in dynamicDatas of this model.
[**teams_id_exists_get**](TeamApi.md#teams_id_exists_get) | **GET** /Teams/{id}/exists | Check whether a model instance exists in the data source.
[**teams_id_get**](TeamApi.md#teams_id_get) | **GET** /Teams/{id} | Find a model instance by {{id}} from the data source.
[**teams_id_head**](TeamApi.md#teams_id_head) | **HEAD** /Teams/{id} | Check whether a model instance exists in the data source.
[**teams_id_image_folders_count_get**](TeamApi.md#teams_id_image_folders_count_get) | **GET** /Teams/{id}/imageFolders/count | Counts imageFolders of Team.
[**teams_id_image_folders_delete**](TeamApi.md#teams_id_image_folders_delete) | **DELETE** /Teams/{id}/imageFolders | Deletes all imageFolders of this model.
[**teams_id_image_folders_fk_delete**](TeamApi.md#teams_id_image_folders_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{fk} | Delete a related item by id for imageFolders.
[**teams_id_image_folders_fk_get**](TeamApi.md#teams_id_image_folders_fk_get) | **GET** /Teams/{id}/imageFolders/{fk} | Find a related item by id for imageFolders.
[**teams_id_image_folders_fk_put**](TeamApi.md#teams_id_image_folders_fk_put) | **PUT** /Teams/{id}/imageFolders/{fk} | Update a related item by id for imageFolders.
[**teams_id_image_folders_get**](TeamApi.md#teams_id_image_folders_get) | **GET** /Teams/{id}/imageFolders | Queries imageFolders of Team.
[**teams_id_image_folders_nk_children_count_get**](TeamApi.md#teams_id_image_folders_nk_children_count_get) | **GET** /Teams/{id}/imageFolders/{nk}/children/count | Counts children of ImageFolder.
[**teams_id_image_folders_nk_children_fk_delete**](TeamApi.md#teams_id_image_folders_nk_children_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/children/{fk} | Delete a related item by id for children.
[**teams_id_image_folders_nk_children_fk_get**](TeamApi.md#teams_id_image_folders_nk_children_fk_get) | **GET** /Teams/{id}/imageFolders/{nk}/children/{fk} | Find a related item by id for children.
[**teams_id_image_folders_nk_children_fk_put**](TeamApi.md#teams_id_image_folders_nk_children_fk_put) | **PUT** /Teams/{id}/imageFolders/{nk}/children/{fk} | Update a related item by id for children.
[**teams_id_image_folders_nk_children_get**](TeamApi.md#teams_id_image_folders_nk_children_get) | **GET** /Teams/{id}/imageFolders/{nk}/children | Queries children of ImageFolder.
[**teams_id_image_folders_nk_children_post**](TeamApi.md#teams_id_image_folders_nk_children_post) | **POST** /Teams/{id}/imageFolders/{nk}/children | Creates a new instance in children of this model.
[**teams_id_image_folders_nk_folder_members_count_get**](TeamApi.md#teams_id_image_folders_nk_folder_members_count_get) | **GET** /Teams/{id}/imageFolders/{nk}/folderMembers/count | Counts folderMembers of ImageFolder.
[**teams_id_image_folders_nk_folder_members_delete**](TeamApi.md#teams_id_image_folders_nk_folder_members_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/folderMembers | Deletes all folderMembers of this model.
[**teams_id_image_folders_nk_folder_members_fk_delete**](TeamApi.md#teams_id_image_folders_nk_folder_members_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/folderMembers/{fk} | Delete a related item by id for folderMembers.
[**teams_id_image_folders_nk_folder_members_fk_get**](TeamApi.md#teams_id_image_folders_nk_folder_members_fk_get) | **GET** /Teams/{id}/imageFolders/{nk}/folderMembers/{fk} | Find a related item by id for folderMembers.
[**teams_id_image_folders_nk_folder_members_fk_put**](TeamApi.md#teams_id_image_folders_nk_folder_members_fk_put) | **PUT** /Teams/{id}/imageFolders/{nk}/folderMembers/{fk} | Update a related item by id for folderMembers.
[**teams_id_image_folders_nk_folder_members_get**](TeamApi.md#teams_id_image_folders_nk_folder_members_get) | **GET** /Teams/{id}/imageFolders/{nk}/folderMembers | Queries folderMembers of ImageFolder.
[**teams_id_image_folders_nk_folder_members_post**](TeamApi.md#teams_id_image_folders_nk_folder_members_post) | **POST** /Teams/{id}/imageFolders/{nk}/folderMembers | Creates a new instance in folderMembers of this model.
[**teams_id_image_folders_nk_images_count_get**](TeamApi.md#teams_id_image_folders_nk_images_count_get) | **GET** /Teams/{id}/imageFolders/{nk}/images/count | Counts images of ImageFolder.
[**teams_id_image_folders_nk_images_fk_delete**](TeamApi.md#teams_id_image_folders_nk_images_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/images/{fk} | Delete a related item by id for images.
[**teams_id_image_folders_nk_images_fk_get**](TeamApi.md#teams_id_image_folders_nk_images_fk_get) | **GET** /Teams/{id}/imageFolders/{nk}/images/{fk} | Find a related item by id for images.
[**teams_id_image_folders_nk_images_fk_put**](TeamApi.md#teams_id_image_folders_nk_images_fk_put) | **PUT** /Teams/{id}/imageFolders/{nk}/images/{fk} | Update a related item by id for images.
[**teams_id_image_folders_nk_images_get**](TeamApi.md#teams_id_image_folders_nk_images_get) | **GET** /Teams/{id}/imageFolders/{nk}/images | Queries images of ImageFolder.
[**teams_id_image_folders_nk_images_post**](TeamApi.md#teams_id_image_folders_nk_images_post) | **POST** /Teams/{id}/imageFolders/{nk}/images | Creates a new instance in images of this model.
[**teams_id_image_folders_nk_members_count_get**](TeamApi.md#teams_id_image_folders_nk_members_count_get) | **GET** /Teams/{id}/imageFolders/{nk}/members/count | Counts members of ImageFolder.
[**teams_id_image_folders_nk_members_delete**](TeamApi.md#teams_id_image_folders_nk_members_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/members | Deletes all members of this model.
[**teams_id_image_folders_nk_members_fk_delete**](TeamApi.md#teams_id_image_folders_nk_members_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/members/{fk} | Delete a related item by id for members.
[**teams_id_image_folders_nk_members_fk_get**](TeamApi.md#teams_id_image_folders_nk_members_fk_get) | **GET** /Teams/{id}/imageFolders/{nk}/members/{fk} | Find a related item by id for members.
[**teams_id_image_folders_nk_members_fk_put**](TeamApi.md#teams_id_image_folders_nk_members_fk_put) | **PUT** /Teams/{id}/imageFolders/{nk}/members/{fk} | Update a related item by id for members.
[**teams_id_image_folders_nk_members_get**](TeamApi.md#teams_id_image_folders_nk_members_get) | **GET** /Teams/{id}/imageFolders/{nk}/members | Queries members of ImageFolder.
[**teams_id_image_folders_nk_members_post**](TeamApi.md#teams_id_image_folders_nk_members_post) | **POST** /Teams/{id}/imageFolders/{nk}/members | Creates a new instance in members of this model.
[**teams_id_image_folders_nk_members_rel_fk_delete**](TeamApi.md#teams_id_image_folders_nk_members_rel_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/members/rel/{fk} | Remove the members relation to an item by id.
[**teams_id_image_folders_nk_members_rel_fk_head**](TeamApi.md#teams_id_image_folders_nk_members_rel_fk_head) | **HEAD** /Teams/{id}/imageFolders/{nk}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**teams_id_image_folders_nk_members_rel_fk_put**](TeamApi.md#teams_id_image_folders_nk_members_rel_fk_put) | **PUT** /Teams/{id}/imageFolders/{nk}/members/rel/{fk} | Add a related item by id for members.
[**teams_id_image_folders_nk_parent_get**](TeamApi.md#teams_id_image_folders_nk_parent_get) | **GET** /Teams/{id}/imageFolders/{nk}/parent | Fetches belongsTo relation parent.
[**teams_id_image_folders_nk_portals_count_get**](TeamApi.md#teams_id_image_folders_nk_portals_count_get) | **GET** /Teams/{id}/imageFolders/{nk}/portals/count | Counts portals of ImageFolder.
[**teams_id_image_folders_nk_portals_delete**](TeamApi.md#teams_id_image_folders_nk_portals_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/portals | Deletes all portals of this model.
[**teams_id_image_folders_nk_portals_fk_delete**](TeamApi.md#teams_id_image_folders_nk_portals_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/portals/{fk} | Delete a related item by id for portals.
[**teams_id_image_folders_nk_portals_fk_get**](TeamApi.md#teams_id_image_folders_nk_portals_fk_get) | **GET** /Teams/{id}/imageFolders/{nk}/portals/{fk} | Find a related item by id for portals.
[**teams_id_image_folders_nk_portals_fk_put**](TeamApi.md#teams_id_image_folders_nk_portals_fk_put) | **PUT** /Teams/{id}/imageFolders/{nk}/portals/{fk} | Update a related item by id for portals.
[**teams_id_image_folders_nk_portals_get**](TeamApi.md#teams_id_image_folders_nk_portals_get) | **GET** /Teams/{id}/imageFolders/{nk}/portals | Queries portals of ImageFolder.
[**teams_id_image_folders_nk_portals_post**](TeamApi.md#teams_id_image_folders_nk_portals_post) | **POST** /Teams/{id}/imageFolders/{nk}/portals | Creates a new instance in portals of this model.
[**teams_id_image_folders_nk_portals_rel_fk_delete**](TeamApi.md#teams_id_image_folders_nk_portals_rel_fk_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/portals/rel/{fk} | Remove the portals relation to an item by id.
[**teams_id_image_folders_nk_portals_rel_fk_head**](TeamApi.md#teams_id_image_folders_nk_portals_rel_fk_head) | **HEAD** /Teams/{id}/imageFolders/{nk}/portals/rel/{fk} | Check the existence of portals relation to an item by id.
[**teams_id_image_folders_nk_portals_rel_fk_put**](TeamApi.md#teams_id_image_folders_nk_portals_rel_fk_put) | **PUT** /Teams/{id}/imageFolders/{nk}/portals/rel/{fk} | Add a related item by id for portals.
[**teams_id_image_folders_nk_team_get**](TeamApi.md#teams_id_image_folders_nk_team_get) | **GET** /Teams/{id}/imageFolders/{nk}/team | Fetches belongsTo relation team.
[**teams_id_image_folders_post**](TeamApi.md#teams_id_image_folders_post) | **POST** /Teams/{id}/imageFolders | Creates a new instance in imageFolders of this model.
[**teams_id_images_count_get**](TeamApi.md#teams_id_images_count_get) | **GET** /Teams/{id}/images/count | Counts images of Team.
[**teams_id_images_delete**](TeamApi.md#teams_id_images_delete) | **DELETE** /Teams/{id}/images | Deletes all images of this model.
[**teams_id_images_fk_delete**](TeamApi.md#teams_id_images_fk_delete) | **DELETE** /Teams/{id}/images/{fk} | Delete a related item by id for images.
[**teams_id_images_fk_get**](TeamApi.md#teams_id_images_fk_get) | **GET** /Teams/{id}/images/{fk} | Find a related item by id for images.
[**teams_id_images_fk_put**](TeamApi.md#teams_id_images_fk_put) | **PUT** /Teams/{id}/images/{fk} | Update a related item by id for images.
[**teams_id_images_get**](TeamApi.md#teams_id_images_get) | **GET** /Teams/{id}/images | Queries images of Team.
[**teams_id_images_nk_folder_get**](TeamApi.md#teams_id_images_nk_folder_get) | **GET** /Teams/{id}/images/{nk}/folder | Fetches belongsTo relation folder.
[**teams_id_images_nk_team_get**](TeamApi.md#teams_id_images_nk_team_get) | **GET** /Teams/{id}/images/{nk}/team | Fetches belongsTo relation team.
[**teams_id_images_post**](TeamApi.md#teams_id_images_post) | **POST** /Teams/{id}/images | Creates a new instance in images of this model.
[**teams_id_invitation_tickets_fk_delete**](TeamApi.md#teams_id_invitation_tickets_fk_delete) | **DELETE** /Teams/{id}/invitationTickets/{fk} | Delete InvitationTickets for this Team
[**teams_id_invitation_tickets_fk_get**](TeamApi.md#teams_id_invitation_tickets_fk_get) | **GET** /Teams/{id}/invitationTickets/{fk} | Get InvitationTicket by Id for this Team
[**teams_id_invitation_tickets_get**](TeamApi.md#teams_id_invitation_tickets_get) | **GET** /Teams/{id}/invitationTickets | List InvitationTickets for this Team
[**teams_id_logo_put**](TeamApi.md#teams_id_logo_put) | **PUT** /Teams/{id}/logo | Change logo
[**teams_id_members_count_get**](TeamApi.md#teams_id_members_count_get) | **GET** /Teams/{id}/members/count | Counts members of Team.
[**teams_id_members_delete**](TeamApi.md#teams_id_members_delete) | **DELETE** /Teams/{id}/members | Deletes all members of this model.
[**teams_id_members_fk_delete**](TeamApi.md#teams_id_members_fk_delete) | **DELETE** /Teams/{id}/members/{fk} | Delete a related item by id for members.
[**teams_id_members_fk_get**](TeamApi.md#teams_id_members_fk_get) | **GET** /Teams/{id}/members/{fk} | Find a related item by id for members.
[**teams_id_members_fk_put**](TeamApi.md#teams_id_members_fk_put) | **PUT** /Teams/{id}/members/{fk} | Update a related item by id for members.
[**teams_id_members_get**](TeamApi.md#teams_id_members_get) | **GET** /Teams/{id}/members | Queries members of Team.
[**teams_id_members_post**](TeamApi.md#teams_id_members_post) | **POST** /Teams/{id}/members | Creates a new instance in members of this model.
[**teams_id_members_rel_fk_delete**](TeamApi.md#teams_id_members_rel_fk_delete) | **DELETE** /Teams/{id}/members/rel/{fk} | Remove the members relation to an item by id.
[**teams_id_members_rel_fk_head**](TeamApi.md#teams_id_members_rel_fk_head) | **HEAD** /Teams/{id}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**teams_id_members_rel_fk_put**](TeamApi.md#teams_id_members_rel_fk_put) | **PUT** /Teams/{id}/members/rel/{fk} | Add a related item by id for members.
[**teams_id_patch**](TeamApi.md#teams_id_patch) | **PATCH** /Teams/{id} | Patch attributes for a model instance and persist it into the data source.
[**teams_id_permission_delete**](TeamApi.md#teams_id_permission_delete) | **DELETE** /Teams/{id}/permission | Deletes permission of this model.
[**teams_id_permission_get**](TeamApi.md#teams_id_permission_get) | **GET** /Teams/{id}/permission | Fetches hasOne relation permission.
[**teams_id_permission_post**](TeamApi.md#teams_id_permission_post) | **POST** /Teams/{id}/permission | Creates a new instance in permission of this model.
[**teams_id_permission_put**](TeamApi.md#teams_id_permission_put) | **PUT** /Teams/{id}/permission | Update permission of this model.
[**teams_id_portals_count_get**](TeamApi.md#teams_id_portals_count_get) | **GET** /Teams/{id}/portals/count | Counts portals of Team.
[**teams_id_portals_delete**](TeamApi.md#teams_id_portals_delete) | **DELETE** /Teams/{id}/portals | Deletes all portals of this model.
[**teams_id_portals_fk_delete**](TeamApi.md#teams_id_portals_fk_delete) | **DELETE** /Teams/{id}/portals/{fk} | Delete a related item by id for portals.
[**teams_id_portals_fk_get**](TeamApi.md#teams_id_portals_fk_get) | **GET** /Teams/{id}/portals/{fk} | Find a related item by id for portals.
[**teams_id_portals_fk_put**](TeamApi.md#teams_id_portals_fk_put) | **PUT** /Teams/{id}/portals/{fk} | Update a related item by id for portals.
[**teams_id_portals_get**](TeamApi.md#teams_id_portals_get) | **GET** /Teams/{id}/portals | Queries portals of Team.
[**teams_id_portals_nk_default_builder_config_get**](TeamApi.md#teams_id_portals_nk_default_builder_config_get) | **GET** /Teams/{id}/portals/{nk}/defaultBuilderConfig | Fetches belongsTo relation defaultBuilderConfig.
[**teams_id_portals_nk_design_folders_count_get**](TeamApi.md#teams_id_portals_nk_design_folders_count_get) | **GET** /Teams/{id}/portals/{nk}/designFolders/count | Counts designFolders of Portal.
[**teams_id_portals_nk_design_folders_delete**](TeamApi.md#teams_id_portals_nk_design_folders_delete) | **DELETE** /Teams/{id}/portals/{nk}/designFolders | Deletes all designFolders of this model.
[**teams_id_portals_nk_design_folders_fk_delete**](TeamApi.md#teams_id_portals_nk_design_folders_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/designFolders/{fk} | Delete a related item by id for designFolders.
[**teams_id_portals_nk_design_folders_fk_get**](TeamApi.md#teams_id_portals_nk_design_folders_fk_get) | **GET** /Teams/{id}/portals/{nk}/designFolders/{fk} | Find a related item by id for designFolders.
[**teams_id_portals_nk_design_folders_fk_put**](TeamApi.md#teams_id_portals_nk_design_folders_fk_put) | **PUT** /Teams/{id}/portals/{nk}/designFolders/{fk} | Update a related item by id for designFolders.
[**teams_id_portals_nk_design_folders_get**](TeamApi.md#teams_id_portals_nk_design_folders_get) | **GET** /Teams/{id}/portals/{nk}/designFolders | Queries designFolders of Portal.
[**teams_id_portals_nk_design_folders_post**](TeamApi.md#teams_id_portals_nk_design_folders_post) | **POST** /Teams/{id}/portals/{nk}/designFolders | Creates a new instance in designFolders of this model.
[**teams_id_portals_nk_designs_count_get**](TeamApi.md#teams_id_portals_nk_designs_count_get) | **GET** /Teams/{id}/portals/{nk}/designs/count | Counts designs of Portal.
[**teams_id_portals_nk_designs_fk_delete**](TeamApi.md#teams_id_portals_nk_designs_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/designs/{fk} | Delete a related item by id for designs.
[**teams_id_portals_nk_designs_fk_get**](TeamApi.md#teams_id_portals_nk_designs_fk_get) | **GET** /Teams/{id}/portals/{nk}/designs/{fk} | Find a related item by id for designs.
[**teams_id_portals_nk_designs_fk_put**](TeamApi.md#teams_id_portals_nk_designs_fk_put) | **PUT** /Teams/{id}/portals/{nk}/designs/{fk} | Update a related item by id for designs.
[**teams_id_portals_nk_designs_get**](TeamApi.md#teams_id_portals_nk_designs_get) | **GET** /Teams/{id}/portals/{nk}/designs | Queries designs of Portal.
[**teams_id_portals_nk_designs_post**](TeamApi.md#teams_id_portals_nk_designs_post) | **POST** /Teams/{id}/portals/{nk}/designs | Creates a new instance in designs of this model.
[**teams_id_portals_nk_image_folders_count_get**](TeamApi.md#teams_id_portals_nk_image_folders_count_get) | **GET** /Teams/{id}/portals/{nk}/imageFolders/count | Counts imageFolders of Portal.
[**teams_id_portals_nk_image_folders_delete**](TeamApi.md#teams_id_portals_nk_image_folders_delete) | **DELETE** /Teams/{id}/portals/{nk}/imageFolders | Deletes all imageFolders of this model.
[**teams_id_portals_nk_image_folders_fk_delete**](TeamApi.md#teams_id_portals_nk_image_folders_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/imageFolders/{fk} | Delete a related item by id for imageFolders.
[**teams_id_portals_nk_image_folders_fk_get**](TeamApi.md#teams_id_portals_nk_image_folders_fk_get) | **GET** /Teams/{id}/portals/{nk}/imageFolders/{fk} | Find a related item by id for imageFolders.
[**teams_id_portals_nk_image_folders_fk_put**](TeamApi.md#teams_id_portals_nk_image_folders_fk_put) | **PUT** /Teams/{id}/portals/{nk}/imageFolders/{fk} | Update a related item by id for imageFolders.
[**teams_id_portals_nk_image_folders_get**](TeamApi.md#teams_id_portals_nk_image_folders_get) | **GET** /Teams/{id}/portals/{nk}/imageFolders | Queries imageFolders of Portal.
[**teams_id_portals_nk_image_folders_post**](TeamApi.md#teams_id_portals_nk_image_folders_post) | **POST** /Teams/{id}/portals/{nk}/imageFolders | Creates a new instance in imageFolders of this model.
[**teams_id_portals_nk_image_folders_rel_fk_delete**](TeamApi.md#teams_id_portals_nk_image_folders_rel_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/imageFolders/rel/{fk} | Remove the imageFolders relation to an item by id.
[**teams_id_portals_nk_image_folders_rel_fk_head**](TeamApi.md#teams_id_portals_nk_image_folders_rel_fk_head) | **HEAD** /Teams/{id}/portals/{nk}/imageFolders/rel/{fk} | Check the existence of imageFolders relation to an item by id.
[**teams_id_portals_nk_image_folders_rel_fk_put**](TeamApi.md#teams_id_portals_nk_image_folders_rel_fk_put) | **PUT** /Teams/{id}/portals/{nk}/imageFolders/rel/{fk} | Add a related item by id for imageFolders.
[**teams_id_portals_nk_members_count_get**](TeamApi.md#teams_id_portals_nk_members_count_get) | **GET** /Teams/{id}/portals/{nk}/members/count | Counts members of Portal.
[**teams_id_portals_nk_members_delete**](TeamApi.md#teams_id_portals_nk_members_delete) | **DELETE** /Teams/{id}/portals/{nk}/members | Deletes all members of this model.
[**teams_id_portals_nk_members_fk_delete**](TeamApi.md#teams_id_portals_nk_members_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/members/{fk} | Delete a related item by id for members.
[**teams_id_portals_nk_members_fk_get**](TeamApi.md#teams_id_portals_nk_members_fk_get) | **GET** /Teams/{id}/portals/{nk}/members/{fk} | Find a related item by id for members.
[**teams_id_portals_nk_members_fk_put**](TeamApi.md#teams_id_portals_nk_members_fk_put) | **PUT** /Teams/{id}/portals/{nk}/members/{fk} | Update a related item by id for members.
[**teams_id_portals_nk_members_get**](TeamApi.md#teams_id_portals_nk_members_get) | **GET** /Teams/{id}/portals/{nk}/members | Queries members of Portal.
[**teams_id_portals_nk_members_post**](TeamApi.md#teams_id_portals_nk_members_post) | **POST** /Teams/{id}/portals/{nk}/members | Creates a new instance in members of this model.
[**teams_id_portals_nk_members_rel_fk_delete**](TeamApi.md#teams_id_portals_nk_members_rel_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/members/rel/{fk} | Remove the members relation to an item by id.
[**teams_id_portals_nk_members_rel_fk_head**](TeamApi.md#teams_id_portals_nk_members_rel_fk_head) | **HEAD** /Teams/{id}/portals/{nk}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**teams_id_portals_nk_members_rel_fk_put**](TeamApi.md#teams_id_portals_nk_members_rel_fk_put) | **PUT** /Teams/{id}/portals/{nk}/members/rel/{fk} | Add a related item by id for members.
[**teams_id_portals_nk_permission_delete**](TeamApi.md#teams_id_portals_nk_permission_delete) | **DELETE** /Teams/{id}/portals/{nk}/permission | Deletes permission of this model.
[**teams_id_portals_nk_permission_get**](TeamApi.md#teams_id_portals_nk_permission_get) | **GET** /Teams/{id}/portals/{nk}/permission | Fetches hasOne relation permission.
[**teams_id_portals_nk_permission_post**](TeamApi.md#teams_id_portals_nk_permission_post) | **POST** /Teams/{id}/portals/{nk}/permission | Creates a new instance in permission of this model.
[**teams_id_portals_nk_permission_put**](TeamApi.md#teams_id_portals_nk_permission_put) | **PUT** /Teams/{id}/portals/{nk}/permission | Update permission of this model.
[**teams_id_portals_nk_portal_members_count_get**](TeamApi.md#teams_id_portals_nk_portal_members_count_get) | **GET** /Teams/{id}/portals/{nk}/portalMembers/count | Counts portalMembers of Portal.
[**teams_id_portals_nk_portal_members_delete**](TeamApi.md#teams_id_portals_nk_portal_members_delete) | **DELETE** /Teams/{id}/portals/{nk}/portalMembers | Deletes all portalMembers of this model.
[**teams_id_portals_nk_portal_members_fk_delete**](TeamApi.md#teams_id_portals_nk_portal_members_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/portalMembers/{fk} | Delete a related item by id for portalMembers.
[**teams_id_portals_nk_portal_members_fk_get**](TeamApi.md#teams_id_portals_nk_portal_members_fk_get) | **GET** /Teams/{id}/portals/{nk}/portalMembers/{fk} | Find a related item by id for portalMembers.
[**teams_id_portals_nk_portal_members_fk_put**](TeamApi.md#teams_id_portals_nk_portal_members_fk_put) | **PUT** /Teams/{id}/portals/{nk}/portalMembers/{fk} | Update a related item by id for portalMembers.
[**teams_id_portals_nk_portal_members_get**](TeamApi.md#teams_id_portals_nk_portal_members_get) | **GET** /Teams/{id}/portals/{nk}/portalMembers | Queries portalMembers of Portal.
[**teams_id_portals_nk_portal_members_post**](TeamApi.md#teams_id_portals_nk_portal_members_post) | **POST** /Teams/{id}/portals/{nk}/portalMembers | Creates a new instance in portalMembers of this model.
[**teams_id_portals_nk_team_get**](TeamApi.md#teams_id_portals_nk_team_get) | **GET** /Teams/{id}/portals/{nk}/team | Fetches belongsTo relation team.
[**teams_id_portals_nk_template_folders_count_get**](TeamApi.md#teams_id_portals_nk_template_folders_count_get) | **GET** /Teams/{id}/portals/{nk}/templateFolders/count | Counts templateFolders of Portal.
[**teams_id_portals_nk_template_folders_delete**](TeamApi.md#teams_id_portals_nk_template_folders_delete) | **DELETE** /Teams/{id}/portals/{nk}/templateFolders | Deletes all templateFolders of this model.
[**teams_id_portals_nk_template_folders_fk_delete**](TeamApi.md#teams_id_portals_nk_template_folders_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/templateFolders/{fk} | Delete a related item by id for templateFolders.
[**teams_id_portals_nk_template_folders_fk_get**](TeamApi.md#teams_id_portals_nk_template_folders_fk_get) | **GET** /Teams/{id}/portals/{nk}/templateFolders/{fk} | Find a related item by id for templateFolders.
[**teams_id_portals_nk_template_folders_fk_put**](TeamApi.md#teams_id_portals_nk_template_folders_fk_put) | **PUT** /Teams/{id}/portals/{nk}/templateFolders/{fk} | Update a related item by id for templateFolders.
[**teams_id_portals_nk_template_folders_get**](TeamApi.md#teams_id_portals_nk_template_folders_get) | **GET** /Teams/{id}/portals/{nk}/templateFolders | Queries templateFolders of Portal.
[**teams_id_portals_nk_template_folders_post**](TeamApi.md#teams_id_portals_nk_template_folders_post) | **POST** /Teams/{id}/portals/{nk}/templateFolders | Creates a new instance in templateFolders of this model.
[**teams_id_portals_nk_template_rels_count_get**](TeamApi.md#teams_id_portals_nk_template_rels_count_get) | **GET** /Teams/{id}/portals/{nk}/templateRels/count | Counts templateRels of Portal.
[**teams_id_portals_nk_template_rels_delete**](TeamApi.md#teams_id_portals_nk_template_rels_delete) | **DELETE** /Teams/{id}/portals/{nk}/templateRels | Deletes all templateRels of this model.
[**teams_id_portals_nk_template_rels_fk_delete**](TeamApi.md#teams_id_portals_nk_template_rels_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/templateRels/{fk} | Delete a related item by id for templateRels.
[**teams_id_portals_nk_template_rels_fk_get**](TeamApi.md#teams_id_portals_nk_template_rels_fk_get) | **GET** /Teams/{id}/portals/{nk}/templateRels/{fk} | Find a related item by id for templateRels.
[**teams_id_portals_nk_template_rels_fk_put**](TeamApi.md#teams_id_portals_nk_template_rels_fk_put) | **PUT** /Teams/{id}/portals/{nk}/templateRels/{fk} | Update a related item by id for templateRels.
[**teams_id_portals_nk_template_rels_get**](TeamApi.md#teams_id_portals_nk_template_rels_get) | **GET** /Teams/{id}/portals/{nk}/templateRels | Queries templateRels of Portal.
[**teams_id_portals_nk_template_rels_post**](TeamApi.md#teams_id_portals_nk_template_rels_post) | **POST** /Teams/{id}/portals/{nk}/templateRels | Creates a new instance in templateRels of this model.
[**teams_id_portals_nk_templates_count_get**](TeamApi.md#teams_id_portals_nk_templates_count_get) | **GET** /Teams/{id}/portals/{nk}/templates/count | Counts templates of Portal.
[**teams_id_portals_nk_templates_delete**](TeamApi.md#teams_id_portals_nk_templates_delete) | **DELETE** /Teams/{id}/portals/{nk}/templates | Deletes all templates of this model.
[**teams_id_portals_nk_templates_fk_delete**](TeamApi.md#teams_id_portals_nk_templates_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/templates/{fk} | Delete a related item by id for templates.
[**teams_id_portals_nk_templates_fk_get**](TeamApi.md#teams_id_portals_nk_templates_fk_get) | **GET** /Teams/{id}/portals/{nk}/templates/{fk} | Find a related item by id for templates.
[**teams_id_portals_nk_templates_fk_put**](TeamApi.md#teams_id_portals_nk_templates_fk_put) | **PUT** /Teams/{id}/portals/{nk}/templates/{fk} | Update a related item by id for templates.
[**teams_id_portals_nk_templates_get**](TeamApi.md#teams_id_portals_nk_templates_get) | **GET** /Teams/{id}/portals/{nk}/templates | Queries templates of Portal.
[**teams_id_portals_nk_templates_post**](TeamApi.md#teams_id_portals_nk_templates_post) | **POST** /Teams/{id}/portals/{nk}/templates | Creates a new instance in templates of this model.
[**teams_id_portals_nk_templates_rel_fk_delete**](TeamApi.md#teams_id_portals_nk_templates_rel_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/templates/rel/{fk} | Remove the templates relation to an item by id.
[**teams_id_portals_nk_templates_rel_fk_head**](TeamApi.md#teams_id_portals_nk_templates_rel_fk_head) | **HEAD** /Teams/{id}/portals/{nk}/templates/rel/{fk} | Check the existence of templates relation to an item by id.
[**teams_id_portals_nk_templates_rel_fk_put**](TeamApi.md#teams_id_portals_nk_templates_rel_fk_put) | **PUT** /Teams/{id}/portals/{nk}/templates/rel/{fk} | Add a related item by id for templates.
[**teams_id_portals_post**](TeamApi.md#teams_id_portals_post) | **POST** /Teams/{id}/portals | Creates a new instance in portals of this model.
[**teams_id_product_materials_count_get**](TeamApi.md#teams_id_product_materials_count_get) | **GET** /Teams/{id}/productMaterials/count | Counts productMaterials of Team.
[**teams_id_product_materials_delete**](TeamApi.md#teams_id_product_materials_delete) | **DELETE** /Teams/{id}/productMaterials | Deletes all productMaterials of this model.
[**teams_id_product_materials_fk_delete**](TeamApi.md#teams_id_product_materials_fk_delete) | **DELETE** /Teams/{id}/productMaterials/{fk} | Delete a related item by id for productMaterials.
[**teams_id_product_materials_fk_get**](TeamApi.md#teams_id_product_materials_fk_get) | **GET** /Teams/{id}/productMaterials/{fk} | Find a related item by id for productMaterials.
[**teams_id_product_materials_fk_put**](TeamApi.md#teams_id_product_materials_fk_put) | **PUT** /Teams/{id}/productMaterials/{fk} | Update a related item by id for productMaterials.
[**teams_id_product_materials_get**](TeamApi.md#teams_id_product_materials_get) | **GET** /Teams/{id}/productMaterials | Queries productMaterials of Team.
[**teams_id_product_materials_nk_team_get**](TeamApi.md#teams_id_product_materials_nk_team_get) | **GET** /Teams/{id}/productMaterials/{nk}/team | Fetches belongsTo relation team.
[**teams_id_product_materials_post**](TeamApi.md#teams_id_product_materials_post) | **POST** /Teams/{id}/productMaterials | Creates a new instance in productMaterials of this model.
[**teams_id_product_pdf_color_profiles_available_get**](TeamApi.md#teams_id_product_pdf_color_profiles_available_get) | **GET** /Teams/{id}/productPdfColorProfiles/available | Find all available PdfColorProfile
[**teams_id_product_pdf_color_profiles_count_get**](TeamApi.md#teams_id_product_pdf_color_profiles_count_get) | **GET** /Teams/{id}/productPdfColorProfiles/count | Counts productPdfColorProfiles of Team.
[**teams_id_product_pdf_color_profiles_delete**](TeamApi.md#teams_id_product_pdf_color_profiles_delete) | **DELETE** /Teams/{id}/productPdfColorProfiles | Deletes all productPdfColorProfiles of this model.
[**teams_id_product_pdf_color_profiles_fk_delete**](TeamApi.md#teams_id_product_pdf_color_profiles_fk_delete) | **DELETE** /Teams/{id}/productPdfColorProfiles/{fk} | Delete a related item by id for productPdfColorProfiles.
[**teams_id_product_pdf_color_profiles_fk_get**](TeamApi.md#teams_id_product_pdf_color_profiles_fk_get) | **GET** /Teams/{id}/productPdfColorProfiles/{fk} | Find a related item by id for productPdfColorProfiles.
[**teams_id_product_pdf_color_profiles_fk_put**](TeamApi.md#teams_id_product_pdf_color_profiles_fk_put) | **PUT** /Teams/{id}/productPdfColorProfiles/{fk} | Update a related item by id for productPdfColorProfiles.
[**teams_id_product_pdf_color_profiles_get**](TeamApi.md#teams_id_product_pdf_color_profiles_get) | **GET** /Teams/{id}/productPdfColorProfiles | Queries productPdfColorProfiles of Team.
[**teams_id_product_pdf_color_profiles_upload_post**](TeamApi.md#teams_id_product_pdf_color_profiles_upload_post) | **POST** /Teams/{id}/productPdfColorProfiles/upload | Upload ICC PDF Color Profile for this Team
[**teams_id_product_size_materials_count_get**](TeamApi.md#teams_id_product_size_materials_count_get) | **GET** /Teams/{id}/productSizeMaterials/count | Counts productSizeMaterials of Team.
[**teams_id_product_size_materials_delete**](TeamApi.md#teams_id_product_size_materials_delete) | **DELETE** /Teams/{id}/productSizeMaterials | Deletes all productSizeMaterials of this model.
[**teams_id_product_size_materials_fk_delete**](TeamApi.md#teams_id_product_size_materials_fk_delete) | **DELETE** /Teams/{id}/productSizeMaterials/{fk} | Delete a related item by id for productSizeMaterials.
[**teams_id_product_size_materials_fk_get**](TeamApi.md#teams_id_product_size_materials_fk_get) | **GET** /Teams/{id}/productSizeMaterials/{fk} | Find a related item by id for productSizeMaterials.
[**teams_id_product_size_materials_fk_put**](TeamApi.md#teams_id_product_size_materials_fk_put) | **PUT** /Teams/{id}/productSizeMaterials/{fk} | Update a related item by id for productSizeMaterials.
[**teams_id_product_size_materials_get**](TeamApi.md#teams_id_product_size_materials_get) | **GET** /Teams/{id}/productSizeMaterials | Queries productSizeMaterials of Team.
[**teams_id_product_size_materials_nk_material_get**](TeamApi.md#teams_id_product_size_materials_nk_material_get) | **GET** /Teams/{id}/productSizeMaterials/{nk}/material | Fetches belongsTo relation material.
[**teams_id_product_size_materials_nk_pdf_color_profile_get**](TeamApi.md#teams_id_product_size_materials_nk_pdf_color_profile_get) | **GET** /Teams/{id}/productSizeMaterials/{nk}/pdfColorProfile | Fetches belongsTo relation pdfColorProfile.
[**teams_id_product_size_materials_nk_size_get**](TeamApi.md#teams_id_product_size_materials_nk_size_get) | **GET** /Teams/{id}/productSizeMaterials/{nk}/size | Fetches belongsTo relation size.
[**teams_id_product_size_materials_nk_team_get**](TeamApi.md#teams_id_product_size_materials_nk_team_get) | **GET** /Teams/{id}/productSizeMaterials/{nk}/team | Fetches belongsTo relation team.
[**teams_id_product_size_materials_post**](TeamApi.md#teams_id_product_size_materials_post) | **POST** /Teams/{id}/productSizeMaterials | Creates a new instance in productSizeMaterials of this model.
[**teams_id_put**](TeamApi.md#teams_id_put) | **PUT** /Teams/{id} | Replace attributes for a model instance and persist it into the data source.
[**teams_id_replace_post**](TeamApi.md#teams_id_replace_post) | **POST** /Teams/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**teams_id_team_data_data_source_mongo_get**](TeamApi.md#teams_id_team_data_data_source_mongo_get) | **GET** /Teams/{id}/teamData/dataSourceMongo | Fetches belongsTo relation dataSourceMongo.
[**teams_id_team_data_data_source_ms_sql_get**](TeamApi.md#teams_id_team_data_data_source_ms_sql_get) | **GET** /Teams/{id}/teamData/dataSourceMsSql | Fetches belongsTo relation dataSourceMsSql.
[**teams_id_team_data_data_source_my_sql_get**](TeamApi.md#teams_id_team_data_data_source_my_sql_get) | **GET** /Teams/{id}/teamData/dataSourceMySql | Fetches belongsTo relation dataSourceMySql.
[**teams_id_team_data_data_source_oracle_get**](TeamApi.md#teams_id_team_data_data_source_oracle_get) | **GET** /Teams/{id}/teamData/dataSourceOracle | Fetches belongsTo relation dataSourceOracle.
[**teams_id_team_data_data_source_postgre_sql_get**](TeamApi.md#teams_id_team_data_data_source_postgre_sql_get) | **GET** /Teams/{id}/teamData/dataSourcePostgreSql | Fetches belongsTo relation dataSourcePostgreSql.
[**teams_id_team_data_data_source_rest_get**](TeamApi.md#teams_id_team_data_data_source_rest_get) | **GET** /Teams/{id}/teamData/dataSourceRest | Fetches belongsTo relation dataSourceRest.
[**teams_id_team_data_data_source_soap_get**](TeamApi.md#teams_id_team_data_data_source_soap_get) | **GET** /Teams/{id}/teamData/dataSourceSoap | Fetches belongsTo relation dataSourceSoap.
[**teams_id_team_data_designs_count_get**](TeamApi.md#teams_id_team_data_designs_count_get) | **GET** /Teams/{id}/teamData/designs/count | Counts designs of DynamicData.
[**teams_id_team_data_designs_fk_delete**](TeamApi.md#teams_id_team_data_designs_fk_delete) | **DELETE** /Teams/{id}/teamData/designs/{fk} | Delete a related item by id for designs.
[**teams_id_team_data_designs_fk_get**](TeamApi.md#teams_id_team_data_designs_fk_get) | **GET** /Teams/{id}/teamData/designs/{fk} | Find a related item by id for designs.
[**teams_id_team_data_designs_fk_put**](TeamApi.md#teams_id_team_data_designs_fk_put) | **PUT** /Teams/{id}/teamData/designs/{fk} | Update a related item by id for designs.
[**teams_id_team_data_designs_get**](TeamApi.md#teams_id_team_data_designs_get) | **GET** /Teams/{id}/teamData/designs | Queries designs of DynamicData.
[**teams_id_team_data_designs_post**](TeamApi.md#teams_id_team_data_designs_post) | **POST** /Teams/{id}/teamData/designs | Creates a new instance in designs of this model.
[**teams_id_team_data_get**](TeamApi.md#teams_id_team_data_get) | **GET** /Teams/{id}/teamData | Fetches belongsTo relation teamData.
[**teams_id_team_data_records_count_get**](TeamApi.md#teams_id_team_data_records_count_get) | **GET** /Teams/{id}/teamData/records/count | Count Dynamic Data records
[**teams_id_team_data_records_delete**](TeamApi.md#teams_id_team_data_records_delete) | **DELETE** /Teams/{id}/teamData/records | Delete all matching records.
[**teams_id_team_data_records_fk_delete**](TeamApi.md#teams_id_team_data_records_fk_delete) | **DELETE** /Teams/{id}/teamData/records/{fk} | Delete a model instance by {{fk}} from the data source.
[**teams_id_team_data_records_fk_get**](TeamApi.md#teams_id_team_data_records_fk_get) | **GET** /Teams/{id}/teamData/records/{fk} | Find a model instance by {{fk}} from the data source.
[**teams_id_team_data_records_fk_property_name_upload_put**](TeamApi.md#teams_id_team_data_records_fk_property_name_upload_put) | **PUT** /Teams/{id}/teamData/records/{fk}/{propertyName}/upload | Replace attributes for a model instance and persist it into the data source.
[**teams_id_team_data_records_fk_put**](TeamApi.md#teams_id_team_data_records_fk_put) | **PUT** /Teams/{id}/teamData/records/{fk} | Replace attributes for a model instance and persist it into the data source.
[**teams_id_team_data_records_get**](TeamApi.md#teams_id_team_data_records_get) | **GET** /Teams/{id}/teamData/records | Find all instances of the model matched by filter from the data source.
[**teams_id_team_data_records_migrate_post**](TeamApi.md#teams_id_team_data_records_migrate_post) | **POST** /Teams/{id}/teamData/records/migrate | Request migration for Dynamic Data records
[**teams_id_team_data_records_post**](TeamApi.md#teams_id_team_data_records_post) | **POST** /Teams/{id}/teamData/records | Create a new instance of the model and persist it into the data source.
[**teams_id_team_data_records_upload_csv_post**](TeamApi.md#teams_id_team_data_records_upload_csv_post) | **POST** /Teams/{id}/teamData/records/upload/csv | Upload CSV for this Dynamic Data
[**teams_id_team_data_team_get**](TeamApi.md#teams_id_team_data_team_get) | **GET** /Teams/{id}/teamData/team | Fetches belongsTo relation team.
[**teams_id_team_members_count_get**](TeamApi.md#teams_id_team_members_count_get) | **GET** /Teams/{id}/teamMembers/count | Counts teamMembers of Team.
[**teams_id_team_members_delete**](TeamApi.md#teams_id_team_members_delete) | **DELETE** /Teams/{id}/teamMembers | Deletes all teamMembers of this model.
[**teams_id_team_members_fk_delete**](TeamApi.md#teams_id_team_members_fk_delete) | **DELETE** /Teams/{id}/teamMembers/{fk} | Delete a related item by id for teamMembers.
[**teams_id_team_members_fk_get**](TeamApi.md#teams_id_team_members_fk_get) | **GET** /Teams/{id}/teamMembers/{fk} | Find a related item by id for teamMembers.
[**teams_id_team_members_fk_put**](TeamApi.md#teams_id_team_members_fk_put) | **PUT** /Teams/{id}/teamMembers/{fk} | Update a related item by id for teamMembers.
[**teams_id_team_members_get**](TeamApi.md#teams_id_team_members_get) | **GET** /Teams/{id}/teamMembers | Queries teamMembers of Team.
[**teams_id_team_members_map_keys_get**](TeamApi.md#teams_id_team_members_map_keys_get) | **GET** /Teams/{id}/teamMembers/map-keys | Map teamMembers emails to teamMembers keys
[**teams_id_team_members_post**](TeamApi.md#teams_id_team_members_post) | **POST** /Teams/{id}/teamMembers | Creates a new instance in teamMembers of this model.
[**teams_id_template_folders_count_get**](TeamApi.md#teams_id_template_folders_count_get) | **GET** /Teams/{id}/templateFolders/count | Counts templateFolders of Team.
[**teams_id_template_folders_delete**](TeamApi.md#teams_id_template_folders_delete) | **DELETE** /Teams/{id}/templateFolders | Deletes all templateFolders of this model.
[**teams_id_template_folders_fk_delete**](TeamApi.md#teams_id_template_folders_fk_delete) | **DELETE** /Teams/{id}/templateFolders/{fk} | Delete a related item by id for templateFolders.
[**teams_id_template_folders_fk_get**](TeamApi.md#teams_id_template_folders_fk_get) | **GET** /Teams/{id}/templateFolders/{fk} | Find a related item by id for templateFolders.
[**teams_id_template_folders_fk_put**](TeamApi.md#teams_id_template_folders_fk_put) | **PUT** /Teams/{id}/templateFolders/{fk} | Update a related item by id for templateFolders.
[**teams_id_template_folders_get**](TeamApi.md#teams_id_template_folders_get) | **GET** /Teams/{id}/templateFolders | Queries templateFolders of Team.
[**teams_id_template_folders_post**](TeamApi.md#teams_id_template_folders_post) | **POST** /Teams/{id}/templateFolders | Creates a new instance in templateFolders of this model.
[**teams_id_templates_count_get**](TeamApi.md#teams_id_templates_count_get) | **GET** /Teams/{id}/templates/count | Counts templates of Team.
[**teams_id_templates_delete**](TeamApi.md#teams_id_templates_delete) | **DELETE** /Teams/{id}/templates | Deletes all templates of this model.
[**teams_id_templates_fk_delete**](TeamApi.md#teams_id_templates_fk_delete) | **DELETE** /Teams/{id}/templates/{fk} | Delete a related item by id for templates.
[**teams_id_templates_fk_get**](TeamApi.md#teams_id_templates_fk_get) | **GET** /Teams/{id}/templates/{fk} | Find a related item by id for templates.
[**teams_id_templates_fk_put**](TeamApi.md#teams_id_templates_fk_put) | **PUT** /Teams/{id}/templates/{fk} | Update a related item by id for templates.
[**teams_id_templates_get**](TeamApi.md#teams_id_templates_get) | **GET** /Teams/{id}/templates | Queries templates of Team.
[**teams_id_templates_nk_designs_count_get**](TeamApi.md#teams_id_templates_nk_designs_count_get) | **GET** /Teams/{id}/templates/{nk}/designs/count | Counts designs of Template.
[**teams_id_templates_nk_designs_fk_delete**](TeamApi.md#teams_id_templates_nk_designs_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/designs/{fk} | Delete a related item by id for designs.
[**teams_id_templates_nk_designs_fk_get**](TeamApi.md#teams_id_templates_nk_designs_fk_get) | **GET** /Teams/{id}/templates/{nk}/designs/{fk} | Find a related item by id for designs.
[**teams_id_templates_nk_designs_fk_put**](TeamApi.md#teams_id_templates_nk_designs_fk_put) | **PUT** /Teams/{id}/templates/{nk}/designs/{fk} | Update a related item by id for designs.
[**teams_id_templates_nk_designs_get**](TeamApi.md#teams_id_templates_nk_designs_get) | **GET** /Teams/{id}/templates/{nk}/designs | Queries designs of Template.
[**teams_id_templates_nk_designs_post**](TeamApi.md#teams_id_templates_nk_designs_post) | **POST** /Teams/{id}/templates/{nk}/designs | Creates a new instance in designs of this model.
[**teams_id_templates_nk_members_count_get**](TeamApi.md#teams_id_templates_nk_members_count_get) | **GET** /Teams/{id}/templates/{nk}/members/count | Counts members of Template.
[**teams_id_templates_nk_members_delete**](TeamApi.md#teams_id_templates_nk_members_delete) | **DELETE** /Teams/{id}/templates/{nk}/members | Deletes all members of this model.
[**teams_id_templates_nk_members_fk_delete**](TeamApi.md#teams_id_templates_nk_members_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/members/{fk} | Delete a related item by id for members.
[**teams_id_templates_nk_members_fk_get**](TeamApi.md#teams_id_templates_nk_members_fk_get) | **GET** /Teams/{id}/templates/{nk}/members/{fk} | Find a related item by id for members.
[**teams_id_templates_nk_members_fk_put**](TeamApi.md#teams_id_templates_nk_members_fk_put) | **PUT** /Teams/{id}/templates/{nk}/members/{fk} | Update a related item by id for members.
[**teams_id_templates_nk_members_get**](TeamApi.md#teams_id_templates_nk_members_get) | **GET** /Teams/{id}/templates/{nk}/members | Queries members of Template.
[**teams_id_templates_nk_members_post**](TeamApi.md#teams_id_templates_nk_members_post) | **POST** /Teams/{id}/templates/{nk}/members | Creates a new instance in members of this model.
[**teams_id_templates_nk_members_rel_fk_delete**](TeamApi.md#teams_id_templates_nk_members_rel_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/members/rel/{fk} | Remove the members relation to an item by id.
[**teams_id_templates_nk_members_rel_fk_head**](TeamApi.md#teams_id_templates_nk_members_rel_fk_head) | **HEAD** /Teams/{id}/templates/{nk}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**teams_id_templates_nk_members_rel_fk_put**](TeamApi.md#teams_id_templates_nk_members_rel_fk_put) | **PUT** /Teams/{id}/templates/{nk}/members/rel/{fk} | Add a related item by id for members.
[**teams_id_templates_nk_permission_delete**](TeamApi.md#teams_id_templates_nk_permission_delete) | **DELETE** /Teams/{id}/templates/{nk}/permission | Deletes permission of this model.
[**teams_id_templates_nk_permission_get**](TeamApi.md#teams_id_templates_nk_permission_get) | **GET** /Teams/{id}/templates/{nk}/permission | Fetches hasOne relation permission.
[**teams_id_templates_nk_permission_post**](TeamApi.md#teams_id_templates_nk_permission_post) | **POST** /Teams/{id}/templates/{nk}/permission | Creates a new instance in permission of this model.
[**teams_id_templates_nk_permission_put**](TeamApi.md#teams_id_templates_nk_permission_put) | **PUT** /Teams/{id}/templates/{nk}/permission | Update permission of this model.
[**teams_id_templates_nk_portal_folders_count_get**](TeamApi.md#teams_id_templates_nk_portal_folders_count_get) | **GET** /Teams/{id}/templates/{nk}/portalFolders/count | Counts portalFolders of Template.
[**teams_id_templates_nk_portal_folders_delete**](TeamApi.md#teams_id_templates_nk_portal_folders_delete) | **DELETE** /Teams/{id}/templates/{nk}/portalFolders | Deletes all portalFolders of this model.
[**teams_id_templates_nk_portal_folders_fk_delete**](TeamApi.md#teams_id_templates_nk_portal_folders_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/portalFolders/{fk} | Delete a related item by id for portalFolders.
[**teams_id_templates_nk_portal_folders_fk_get**](TeamApi.md#teams_id_templates_nk_portal_folders_fk_get) | **GET** /Teams/{id}/templates/{nk}/portalFolders/{fk} | Find a related item by id for portalFolders.
[**teams_id_templates_nk_portal_folders_fk_put**](TeamApi.md#teams_id_templates_nk_portal_folders_fk_put) | **PUT** /Teams/{id}/templates/{nk}/portalFolders/{fk} | Update a related item by id for portalFolders.
[**teams_id_templates_nk_portal_folders_get**](TeamApi.md#teams_id_templates_nk_portal_folders_get) | **GET** /Teams/{id}/templates/{nk}/portalFolders | Queries portalFolders of Template.
[**teams_id_templates_nk_portal_folders_post**](TeamApi.md#teams_id_templates_nk_portal_folders_post) | **POST** /Teams/{id}/templates/{nk}/portalFolders | Creates a new instance in portalFolders of this model.
[**teams_id_templates_nk_portal_folders_rel_fk_delete**](TeamApi.md#teams_id_templates_nk_portal_folders_rel_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/portalFolders/rel/{fk} | Remove the portalFolders relation to an item by id.
[**teams_id_templates_nk_portal_folders_rel_fk_head**](TeamApi.md#teams_id_templates_nk_portal_folders_rel_fk_head) | **HEAD** /Teams/{id}/templates/{nk}/portalFolders/rel/{fk} | Check the existence of portalFolders relation to an item by id.
[**teams_id_templates_nk_portal_folders_rel_fk_put**](TeamApi.md#teams_id_templates_nk_portal_folders_rel_fk_put) | **PUT** /Teams/{id}/templates/{nk}/portalFolders/rel/{fk} | Add a related item by id for portalFolders.
[**teams_id_templates_nk_portals_count_get**](TeamApi.md#teams_id_templates_nk_portals_count_get) | **GET** /Teams/{id}/templates/{nk}/portals/count | Counts portals of Template.
[**teams_id_templates_nk_portals_delete**](TeamApi.md#teams_id_templates_nk_portals_delete) | **DELETE** /Teams/{id}/templates/{nk}/portals | Deletes all portals of this model.
[**teams_id_templates_nk_portals_fk_delete**](TeamApi.md#teams_id_templates_nk_portals_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/portals/{fk} | Delete a related item by id for portals.
[**teams_id_templates_nk_portals_fk_get**](TeamApi.md#teams_id_templates_nk_portals_fk_get) | **GET** /Teams/{id}/templates/{nk}/portals/{fk} | Find a related item by id for portals.
[**teams_id_templates_nk_portals_fk_put**](TeamApi.md#teams_id_templates_nk_portals_fk_put) | **PUT** /Teams/{id}/templates/{nk}/portals/{fk} | Update a related item by id for portals.
[**teams_id_templates_nk_portals_get**](TeamApi.md#teams_id_templates_nk_portals_get) | **GET** /Teams/{id}/templates/{nk}/portals | Queries portals of Template.
[**teams_id_templates_nk_portals_post**](TeamApi.md#teams_id_templates_nk_portals_post) | **POST** /Teams/{id}/templates/{nk}/portals | Creates a new instance in portals of this model.
[**teams_id_templates_nk_portals_rel_fk_delete**](TeamApi.md#teams_id_templates_nk_portals_rel_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/portals/rel/{fk} | Remove the portals relation to an item by id.
[**teams_id_templates_nk_portals_rel_fk_head**](TeamApi.md#teams_id_templates_nk_portals_rel_fk_head) | **HEAD** /Teams/{id}/templates/{nk}/portals/rel/{fk} | Check the existence of portals relation to an item by id.
[**teams_id_templates_nk_portals_rel_fk_put**](TeamApi.md#teams_id_templates_nk_portals_rel_fk_put) | **PUT** /Teams/{id}/templates/{nk}/portals/rel/{fk} | Add a related item by id for portals.
[**teams_id_templates_nk_tags_count_get**](TeamApi.md#teams_id_templates_nk_tags_count_get) | **GET** /Teams/{id}/templates/{nk}/tags/count | Counts tags of Template.
[**teams_id_templates_nk_tags_delete**](TeamApi.md#teams_id_templates_nk_tags_delete) | **DELETE** /Teams/{id}/templates/{nk}/tags | Deletes all tags of this model.
[**teams_id_templates_nk_tags_fk_delete**](TeamApi.md#teams_id_templates_nk_tags_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/tags/{fk} | Delete a related item by id for tags.
[**teams_id_templates_nk_tags_fk_get**](TeamApi.md#teams_id_templates_nk_tags_fk_get) | **GET** /Teams/{id}/templates/{nk}/tags/{fk} | Find a related item by id for tags.
[**teams_id_templates_nk_tags_fk_put**](TeamApi.md#teams_id_templates_nk_tags_fk_put) | **PUT** /Teams/{id}/templates/{nk}/tags/{fk} | Update a related item by id for tags.
[**teams_id_templates_nk_tags_get**](TeamApi.md#teams_id_templates_nk_tags_get) | **GET** /Teams/{id}/templates/{nk}/tags | Queries tags of Template.
[**teams_id_templates_nk_tags_post**](TeamApi.md#teams_id_templates_nk_tags_post) | **POST** /Teams/{id}/templates/{nk}/tags | Creates a new instance in tags of this model.
[**teams_id_templates_nk_tags_rel_fk_delete**](TeamApi.md#teams_id_templates_nk_tags_rel_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/tags/rel/{fk} | Remove the tags relation to an item by id.
[**teams_id_templates_nk_tags_rel_fk_head**](TeamApi.md#teams_id_templates_nk_tags_rel_fk_head) | **HEAD** /Teams/{id}/templates/{nk}/tags/rel/{fk} | Check the existence of tags relation to an item by id.
[**teams_id_templates_nk_tags_rel_fk_put**](TeamApi.md#teams_id_templates_nk_tags_rel_fk_put) | **PUT** /Teams/{id}/templates/{nk}/tags/rel/{fk} | Add a related item by id for tags.
[**teams_id_templates_nk_team_folder_get**](TeamApi.md#teams_id_templates_nk_team_folder_get) | **GET** /Teams/{id}/templates/{nk}/teamFolder | Fetches belongsTo relation teamFolder.
[**teams_id_templates_nk_team_get**](TeamApi.md#teams_id_templates_nk_team_get) | **GET** /Teams/{id}/templates/{nk}/team | Fetches belongsTo relation team.
[**teams_id_templates_nk_template_members_count_get**](TeamApi.md#teams_id_templates_nk_template_members_count_get) | **GET** /Teams/{id}/templates/{nk}/templateMembers/count | Counts templateMembers of Template.
[**teams_id_templates_nk_template_members_delete**](TeamApi.md#teams_id_templates_nk_template_members_delete) | **DELETE** /Teams/{id}/templates/{nk}/templateMembers | Deletes all templateMembers of this model.
[**teams_id_templates_nk_template_members_fk_delete**](TeamApi.md#teams_id_templates_nk_template_members_fk_delete) | **DELETE** /Teams/{id}/templates/{nk}/templateMembers/{fk} | Delete a related item by id for templateMembers.
[**teams_id_templates_nk_template_members_fk_get**](TeamApi.md#teams_id_templates_nk_template_members_fk_get) | **GET** /Teams/{id}/templates/{nk}/templateMembers/{fk} | Find a related item by id for templateMembers.
[**teams_id_templates_nk_template_members_fk_put**](TeamApi.md#teams_id_templates_nk_template_members_fk_put) | **PUT** /Teams/{id}/templates/{nk}/templateMembers/{fk} | Update a related item by id for templateMembers.
[**teams_id_templates_nk_template_members_get**](TeamApi.md#teams_id_templates_nk_template_members_get) | **GET** /Teams/{id}/templates/{nk}/templateMembers | Queries templateMembers of Template.
[**teams_id_templates_nk_template_members_post**](TeamApi.md#teams_id_templates_nk_template_members_post) | **POST** /Teams/{id}/templates/{nk}/templateMembers | Creates a new instance in templateMembers of this model.
[**teams_id_templates_nk_uploader_get**](TeamApi.md#teams_id_templates_nk_uploader_get) | **GET** /Teams/{id}/templates/{nk}/uploader | Fetches belongsTo relation uploader.
[**teams_id_templates_nk_workflow_get**](TeamApi.md#teams_id_templates_nk_workflow_get) | **GET** /Teams/{id}/templates/{nk}/workflow | Fetches belongsTo relation workflow.
[**teams_id_templates_post**](TeamApi.md#teams_id_templates_post) | **POST** /Teams/{id}/templates | Creates a new instance in templates of this model.
[**teams_id_templates_with_designs_get**](TeamApi.md#teams_id_templates_with_designs_get) | **GET** /Teams/{id}/templatesWithDesigns | List Templates with Designs for this Team
[**teams_id_workflows_count_get**](TeamApi.md#teams_id_workflows_count_get) | **GET** /Teams/{id}/workflows/count | Counts workflows of Team.
[**teams_id_workflows_delete**](TeamApi.md#teams_id_workflows_delete) | **DELETE** /Teams/{id}/workflows | Deletes all workflows of this model.
[**teams_id_workflows_fk_delete**](TeamApi.md#teams_id_workflows_fk_delete) | **DELETE** /Teams/{id}/workflows/{fk} | Delete a related item by id for workflows.
[**teams_id_workflows_fk_get**](TeamApi.md#teams_id_workflows_fk_get) | **GET** /Teams/{id}/workflows/{fk} | Find a related item by id for workflows.
[**teams_id_workflows_fk_put**](TeamApi.md#teams_id_workflows_fk_put) | **PUT** /Teams/{id}/workflows/{fk} | Update a related item by id for workflows.
[**teams_id_workflows_get**](TeamApi.md#teams_id_workflows_get) | **GET** /Teams/{id}/workflows | Queries workflows of Team.
[**teams_id_workflows_post**](TeamApi.md#teams_id_workflows_post) | **POST** /Teams/{id}/workflows | Creates a new instance in workflows of this model.
[**teams_name_name_exists_get**](TeamApi.md#teams_name_name_exists_get) | **GET** /Teams/name/{name}/exists | Define whether team exists or not
[**teams_post**](TeamApi.md#teams_post) | **POST** /Teams | Create a new instance of the model and persist it into the data source.
[**teams_subdomain_subdomain_exists_get**](TeamApi.md#teams_subdomain_subdomain_exists_get) | **GET** /Teams/subdomain/{subdomain}/exists | Define whether team exists or not


# **teams_change_stream_get**
> file teams_change_stream_get(options=options)

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
api_instance = TweakApi.TeamApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.teams_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_change_stream_get: %s\n" % e)
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

# **teams_change_stream_post**
> file teams_change_stream_post(options=options)

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
api_instance = TweakApi.TeamApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.teams_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_change_stream_post: %s\n" % e)
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

# **teams_count_get**
> InlineResponse2001 teams_count_get(where=where)

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
api_instance = TweakApi.TeamApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.teams_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_count_get: %s\n" % e)
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

# **teams_find_one_get**
> Team teams_find_one_get(filter=filter)

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
api_instance = TweakApi.TeamApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.teams_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get**
> list[Team] teams_get(filter=filter)

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
api_instance = TweakApi.TeamApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.teams_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Team]**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_auth_reset_keys_delete**
> Team teams_id_auth_reset_keys_delete(id)

Reset Team keys

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Reset Team keys
    api_response = api_instance.teams_id_auth_reset_keys_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_auth_reset_keys_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_brand_delete**
> teams_id_brand_delete(id)

Deletes brand of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes brand of this model.
    api_instance.teams_id_brand_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_brand_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_brand_get**
> TeamBrand teams_id_brand_get(id, refresh=refresh)

Fetches hasOne relation brand.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation brand.
    api_response = api_instance.teams_id_brand_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_brand_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_brand_post**
> TeamBrand teams_id_brand_post(id, data=data)

Creates a new instance in brand of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.TeamBrand() # TeamBrand |  (optional)

try: 
    # Creates a new instance in brand of this model.
    api_response = api_instance.teams_id_brand_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_brand_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**TeamBrand**](TeamBrand.md)|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_brand_put**
> TeamBrand teams_id_brand_put(id, data=data)

Update brand of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.TeamBrand() # TeamBrand |  (optional)

try: 
    # Update brand of this model.
    api_response = api_instance.teams_id_brand_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_brand_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**TeamBrand**](TeamBrand.md)|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_count_get**
> InlineResponse2001 teams_id_builder_configs_count_get(id, where=where)

Counts builderConfigs of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts builderConfigs of Team.
    api_response = api_instance.teams_id_builder_configs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_default_get**
> TeamBuilderConfig teams_id_builder_configs_default_get(id)

Get default TeamBuilderConfig for this Team

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Get default TeamBuilderConfig for this Team
    api_response = api_instance.teams_id_builder_configs_default_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_default_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_default_product_size_materials_get**
> list[ProductSizeMaterial] teams_id_builder_configs_default_product_size_materials_get(id)

Get default TeamBuilderConfig ProductSizeMaterials for this Team

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Get default TeamBuilderConfig ProductSizeMaterials for this Team
    api_response = api_instance.teams_id_builder_configs_default_product_size_materials_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_default_product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_delete**
> teams_id_builder_configs_delete(id)

Deletes all builderConfigs of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all builderConfigs of this model.
    api_instance.teams_id_builder_configs_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_fk_delete**
> teams_id_builder_configs_fk_delete(id, fk)

Delete a related item by id for builderConfigs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for builderConfigs

try: 
    # Delete a related item by id for builderConfigs.
    api_instance.teams_id_builder_configs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for builderConfigs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_fk_get**
> TeamBuilderConfig teams_id_builder_configs_fk_get(id, fk)

Find a related item by id for builderConfigs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for builderConfigs

try: 
    # Find a related item by id for builderConfigs.
    api_response = api_instance.teams_id_builder_configs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for builderConfigs | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_fk_logo_put**
> TeamBuilderConfig teams_id_builder_configs_fk_logo_put(id, fk, data)

Change Builder Config logo

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | BuilderConfig id
data = TweakApi.Team() # Team | Logo

try: 
    # Change Builder Config logo
    api_response = api_instance.teams_id_builder_configs_fk_logo_put(id, fk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_fk_logo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| BuilderConfig id | 
 **data** | [**Team**](Team.md)| Logo | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_fk_put**
> TeamBuilderConfig teams_id_builder_configs_fk_put(id, fk, data=data)

Update a related item by id for builderConfigs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for builderConfigs
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig |  (optional)

try: 
    # Update a related item by id for builderConfigs.
    api_response = api_instance.teams_id_builder_configs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for builderConfigs | 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_fk_watermark_put**
> TeamBuilderConfig teams_id_builder_configs_fk_watermark_put(id, fk, data)

Change Builder Config watermark

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | BuilderConfig id
data = TweakApi.Team() # Team | Watermark

try: 
    # Change Builder Config watermark
    api_response = api_instance.teams_id_builder_configs_fk_watermark_put(id, fk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_fk_watermark_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| BuilderConfig id | 
 **data** | [**Team**](Team.md)| Watermark | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_get**
> list[TeamBuilderConfig] teams_id_builder_configs_get(id, filter=filter)

Queries builderConfigs of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries builderConfigs of Team.
    api_response = api_instance.teams_id_builder_configs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamBuilderConfig]**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_portals_count_get**
> InlineResponse2001 teams_id_builder_configs_nk_portals_count_get(id, nk, where=where)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_portals_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_portals_fk_delete**
> teams_id_builder_configs_nk_portals_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.teams_id_builder_configs_nk_portals_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_portals_fk_get**
> Portal teams_id_builder_configs_nk_portals_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.teams_id_builder_configs_nk_portals_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_portals_fk_put**
> Portal teams_id_builder_configs_nk_portals_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.teams_id_builder_configs_nk_portals_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_portals_get**
> list[Portal] teams_id_builder_configs_nk_portals_get(id, nk, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_portals_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_portals_post**
> Portal teams_id_builder_configs_nk_portals_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.teams_id_builder_configs_nk_portals_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_count_get**
> InlineResponse2001 teams_id_builder_configs_nk_product_groups_count_get(id, nk, where=where)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productGroups of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_groups_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_fk_delete**
> teams_id_builder_configs_nk_product_groups_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Delete a related item by id for productGroups.
    api_instance.teams_id_builder_configs_nk_product_groups_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_fk_get**
> ProductGroup teams_id_builder_configs_nk_product_groups_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Find a related item by id for productGroups.
    api_response = api_instance.teams_id_builder_configs_nk_product_groups_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_fk_put**
> ProductGroup teams_id_builder_configs_nk_product_groups_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productGroups
data = TweakApi.ProductGroup() # ProductGroup |  (optional)

try: 
    # Update a related item by id for productGroups.
    api_response = api_instance.teams_id_builder_configs_nk_product_groups_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_groups_get**
> list[ProductGroup] teams_id_builder_configs_nk_product_groups_get(id, nk, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productGroups of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_groups_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductGroup]**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_post**
> ProductGroup teams_id_builder_configs_nk_product_groups_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
data = TweakApi.ProductGroup() # ProductGroup |  (optional)

try: 
    # Creates a new instance in productGroups of this model.
    api_response = api_instance.teams_id_builder_configs_nk_product_groups_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **data** | [**ProductGroup**](ProductGroup.md)|  | [optional] 

### Return type

[**ProductGroup**](ProductGroup.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_rel_fk_delete**
> teams_id_builder_configs_nk_product_groups_rel_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Remove the productGroups relation to an item by id.
    api_instance.teams_id_builder_configs_nk_product_groups_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_rel_fk_head**
> bool teams_id_builder_configs_nk_product_groups_rel_fk_head(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productGroups

try: 
    # Check the existence of productGroups relation to an item by id.
    api_response = api_instance.teams_id_builder_configs_nk_product_groups_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productGroups | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_groups_rel_fk_put**
> TeamBuilderConfigProductGroup teams_id_builder_configs_nk_product_groups_rel_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productGroups
data = TweakApi.TeamBuilderConfigProductGroup() # TeamBuilderConfigProductGroup |  (optional)

try: 
    # Add a related item by id for productGroups.
    api_response = api_instance.teams_id_builder_configs_nk_product_groups_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_groups_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_size_materials_count_get**
> InlineResponse2001 teams_id_builder_configs_nk_product_size_materials_count_get(id, nk, where=where)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizeMaterials of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_fk_delete**
> teams_id_builder_configs_nk_product_size_materials_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Delete a related item by id for productSizeMaterials.
    api_instance.teams_id_builder_configs_nk_product_size_materials_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_fk_get**
> ProductSizeMaterial teams_id_builder_configs_nk_product_size_materials_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Find a related item by id for productSizeMaterials.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_fk_put**
> ProductSizeMaterial teams_id_builder_configs_nk_product_size_materials_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for productSizeMaterials.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_size_materials_get**
> list[ProductSizeMaterial] teams_id_builder_configs_nk_product_size_materials_get(id, nk, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizeMaterials of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_post**
> ProductSizeMaterial teams_id_builder_configs_nk_product_size_materials_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in productSizeMaterials of this model.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_rel_count_get**
> InlineResponse2001 teams_id_builder_configs_nk_product_size_materials_rel_count_get(id, nk, where=where)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizeMaterialsRel of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_rel_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_rel_fk_delete**
> teams_id_builder_configs_nk_product_size_materials_rel_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Remove the productSizeMaterials relation to an item by id.
    api_instance.teams_id_builder_configs_nk_product_size_materials_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_rel_fk_delete_0**
> teams_id_builder_configs_nk_product_size_materials_rel_fk_delete_0(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterialsRel

try: 
    # Delete a related item by id for productSizeMaterialsRel.
    api_instance.teams_id_builder_configs_nk_product_size_materials_rel_fk_delete_0(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_fk_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizeMaterialsRel | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_rel_fk_get**
> TeamBuilderConfigProductSizeMaterial teams_id_builder_configs_nk_product_size_materials_rel_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterialsRel

try: 
    # Find a related item by id for productSizeMaterialsRel.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_rel_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizeMaterialsRel | 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_rel_fk_head**
> bool teams_id_builder_configs_nk_product_size_materials_rel_fk_head(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Check the existence of productSizeMaterials relation to an item by id.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_rel_fk_put**
> TeamBuilderConfigProductSizeMaterial teams_id_builder_configs_nk_product_size_materials_rel_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterials
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial |  (optional)

try: 
    # Add a related item by id for productSizeMaterials.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_size_materials_rel_fk_put_0**
> TeamBuilderConfigProductSizeMaterial teams_id_builder_configs_nk_product_size_materials_rel_fk_put_0(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizeMaterialsRel
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for productSizeMaterialsRel.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_rel_fk_put_0(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_fk_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_size_materials_rel_get**
> list[TeamBuilderConfigProductSizeMaterial] teams_id_builder_configs_nk_product_size_materials_rel_get(id, nk, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizeMaterialsRel of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_rel_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamBuilderConfigProductSizeMaterial]**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_size_materials_rel_post**
> TeamBuilderConfigProductSizeMaterial teams_id_builder_configs_nk_product_size_materials_rel_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
data = TweakApi.TeamBuilderConfigProductSizeMaterial() # TeamBuilderConfigProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in productSizeMaterialsRel of this model.
    api_response = api_instance.teams_id_builder_configs_nk_product_size_materials_rel_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_size_materials_rel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **data** | [**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)|  | [optional] 

### Return type

[**TeamBuilderConfigProductSizeMaterial**](TeamBuilderConfigProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_count_get**
> InlineResponse2001 teams_id_builder_configs_nk_product_sizes_count_get(id, nk, where=where)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizes of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_sizes_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_fk_delete**
> teams_id_builder_configs_nk_product_sizes_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Delete a related item by id for productSizes.
    api_instance.teams_id_builder_configs_nk_product_sizes_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_fk_get**
> ProductSize teams_id_builder_configs_nk_product_sizes_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Find a related item by id for productSizes.
    api_response = api_instance.teams_id_builder_configs_nk_product_sizes_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_fk_put**
> ProductSize teams_id_builder_configs_nk_product_sizes_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizes
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Update a related item by id for productSizes.
    api_response = api_instance.teams_id_builder_configs_nk_product_sizes_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_sizes_get**
> list[ProductSize] teams_id_builder_configs_nk_product_sizes_get(id, nk, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizes of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_sizes_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSize]**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_post**
> ProductSize teams_id_builder_configs_nk_product_sizes_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
data = TweakApi.ProductSize() # ProductSize |  (optional)

try: 
    # Creates a new instance in productSizes of this model.
    api_response = api_instance.teams_id_builder_configs_nk_product_sizes_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **data** | [**ProductSize**](ProductSize.md)|  | [optional] 

### Return type

[**ProductSize**](ProductSize.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_rel_fk_delete**
> teams_id_builder_configs_nk_product_sizes_rel_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Remove the productSizes relation to an item by id.
    api_instance.teams_id_builder_configs_nk_product_sizes_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_rel_fk_head**
> bool teams_id_builder_configs_nk_product_sizes_rel_fk_head(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizes

try: 
    # Check the existence of productSizes relation to an item by id.
    api_response = api_instance.teams_id_builder_configs_nk_product_sizes_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productSizes | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_sizes_rel_fk_put**
> TeamBuilderConfigProductSize teams_id_builder_configs_nk_product_sizes_rel_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productSizes
data = TweakApi.TeamBuilderConfigProductSize() # TeamBuilderConfigProductSize |  (optional)

try: 
    # Add a related item by id for productSizes.
    api_response = api_instance.teams_id_builder_configs_nk_product_sizes_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_sizes_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_types_count_get**
> InlineResponse2001 teams_id_builder_configs_nk_product_types_count_get(id, nk, where=where)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productTypes of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_types_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_types_fk_delete**
> teams_id_builder_configs_nk_product_types_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Delete a related item by id for productTypes.
    api_instance.teams_id_builder_configs_nk_product_types_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_types_fk_get**
> ProductType teams_id_builder_configs_nk_product_types_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Find a related item by id for productTypes.
    api_response = api_instance.teams_id_builder_configs_nk_product_types_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_types_fk_put**
> ProductType teams_id_builder_configs_nk_product_types_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productTypes
data = TweakApi.ProductType() # ProductType |  (optional)

try: 
    # Update a related item by id for productTypes.
    api_response = api_instance.teams_id_builder_configs_nk_product_types_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_product_types_get**
> list[ProductType] teams_id_builder_configs_nk_product_types_get(id, nk, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productTypes of TeamBuilderConfig.
    api_response = api_instance.teams_id_builder_configs_nk_product_types_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductType]**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_types_post**
> ProductType teams_id_builder_configs_nk_product_types_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
data = TweakApi.ProductType() # ProductType |  (optional)

try: 
    # Creates a new instance in productTypes of this model.
    api_response = api_instance.teams_id_builder_configs_nk_product_types_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **data** | [**ProductType**](ProductType.md)|  | [optional] 

### Return type

[**ProductType**](ProductType.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_types_rel_fk_delete**
> teams_id_builder_configs_nk_product_types_rel_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Remove the productTypes relation to an item by id.
    api_instance.teams_id_builder_configs_nk_product_types_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_types_rel_fk_head**
> bool teams_id_builder_configs_nk_product_types_rel_fk_head(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productTypes

try: 
    # Check the existence of productTypes relation to an item by id.
    api_response = api_instance.teams_id_builder_configs_nk_product_types_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **fk** | **str**| Foreign key for productTypes | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_nk_product_types_rel_fk_put**
> TeamBuilderConfigProductType teams_id_builder_configs_nk_product_types_rel_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
fk = 'fk_example' # str | Foreign key for productTypes
data = TweakApi.TeamBuilderConfigProductType() # TeamBuilderConfigProductType |  (optional)

try: 
    # Add a related item by id for productTypes.
    api_response = api_instance.teams_id_builder_configs_nk_product_types_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_product_types_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
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

# **teams_id_builder_configs_nk_team_get**
> Team teams_id_builder_configs_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for builderConfigs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_builder_configs_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for builderConfigs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_builder_configs_post**
> TeamBuilderConfig teams_id_builder_configs_post(id, data=data)

Creates a new instance in builderConfigs of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig |  (optional)

try: 
    # Creates a new instance in builderConfigs of this model.
    api_response = api_instance.teams_id_builder_configs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_builder_configs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_count_get**
> InlineResponse2001 teams_id_data_source_soaps_count_get(id, where=where)

Counts dataSourceSoaps of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts dataSourceSoaps of Team.
    api_response = api_instance.teams_id_data_source_soaps_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_fk_delete**
> teams_id_data_source_soaps_fk_delete(id, fk)

Delete a related item by id for dataSourceSoaps.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for dataSourceSoaps

try: 
    # Delete a related item by id for dataSourceSoaps.
    api_instance.teams_id_data_source_soaps_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for dataSourceSoaps | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_fk_get**
> DataSourceSoap teams_id_data_source_soaps_fk_get(id, fk)

Find a related item by id for dataSourceSoaps.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for dataSourceSoaps

try: 
    # Find a related item by id for dataSourceSoaps.
    api_response = api_instance.teams_id_data_source_soaps_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for dataSourceSoaps | 

### Return type

[**DataSourceSoap**](DataSourceSoap.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_fk_put**
> DataSourceSoap teams_id_data_source_soaps_fk_put(id, fk, data=data)

Update a related item by id for dataSourceSoaps.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for dataSourceSoaps
data = TweakApi.DataSourceSoap() # DataSourceSoap |  (optional)

try: 
    # Update a related item by id for dataSourceSoaps.
    api_response = api_instance.teams_id_data_source_soaps_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for dataSourceSoaps | 
 **data** | [**DataSourceSoap**](DataSourceSoap.md)|  | [optional] 

### Return type

[**DataSourceSoap**](DataSourceSoap.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_get**
> list[DataSourceSoap] teams_id_data_source_soaps_get(id, filter=filter)

Queries dataSourceSoaps of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries dataSourceSoaps of Team.
    api_response = api_instance.teams_id_data_source_soaps_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DataSourceSoap]**](DataSourceSoap.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_dynamic_datas_count_get**
> InlineResponse2001 teams_id_data_source_soaps_nk_dynamic_datas_count_get(id, nk, where=where)

Counts dynamicDatas of DataSourceSoap.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts dynamicDatas of DataSourceSoap.
    api_response = api_instance.teams_id_data_source_soaps_nk_dynamic_datas_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_dynamic_datas_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_dynamic_datas_delete**
> teams_id_data_source_soaps_nk_dynamic_datas_delete(id, nk)

Deletes all dynamicDatas of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.

try: 
    # Deletes all dynamicDatas of this model.
    api_instance.teams_id_data_source_soaps_nk_dynamic_datas_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_dynamic_datas_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_dynamic_datas_fk_delete**
> teams_id_data_source_soaps_nk_dynamic_datas_fk_delete(id, nk, fk)

Delete a related item by id for dynamicDatas.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Delete a related item by id for dynamicDatas.
    api_instance.teams_id_data_source_soaps_nk_dynamic_datas_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_dynamic_datas_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_dynamic_datas_fk_get**
> DynamicData teams_id_data_source_soaps_nk_dynamic_datas_fk_get(id, nk, fk)

Find a related item by id for dynamicDatas.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Find a related item by id for dynamicDatas.
    api_response = api_instance.teams_id_data_source_soaps_nk_dynamic_datas_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_dynamic_datas_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_dynamic_datas_fk_put**
> DynamicData teams_id_data_source_soaps_nk_dynamic_datas_fk_put(id, nk, fk, data=data)

Update a related item by id for dynamicDatas.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.
fk = 'fk_example' # str | Foreign key for dynamicDatas
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Update a related item by id for dynamicDatas.
    api_response = api_instance.teams_id_data_source_soaps_nk_dynamic_datas_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_dynamic_datas_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 
 **fk** | **str**| Foreign key for dynamicDatas | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_dynamic_datas_get**
> list[DynamicData] teams_id_data_source_soaps_nk_dynamic_datas_get(id, nk, filter=filter)

Queries dynamicDatas of DataSourceSoap.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries dynamicDatas of DataSourceSoap.
    api_response = api_instance.teams_id_data_source_soaps_nk_dynamic_datas_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_dynamic_datas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DynamicData]**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_dynamic_datas_post**
> DynamicData teams_id_data_source_soaps_nk_dynamic_datas_post(id, nk, data=data)

Creates a new instance in dynamicDatas of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Creates a new instance in dynamicDatas of this model.
    api_response = api_instance.teams_id_data_source_soaps_nk_dynamic_datas_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_dynamic_datas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_nk_team_get**
> Team teams_id_data_source_soaps_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dataSourceSoaps.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_data_source_soaps_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dataSourceSoaps. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_data_source_soaps_post**
> DataSourceSoap teams_id_data_source_soaps_post(id, data=data)

Creates a new instance in dataSourceSoaps of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.DataSourceSoap() # DataSourceSoap |  (optional)

try: 
    # Creates a new instance in dataSourceSoaps of this model.
    api_response = api_instance.teams_id_data_source_soaps_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_data_source_soaps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**DataSourceSoap**](DataSourceSoap.md)|  | [optional] 

### Return type

[**DataSourceSoap**](DataSourceSoap.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_delete**
> object teams_id_delete(id)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.teams_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_delete: %s\n" % e)
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

# **teams_id_dynamic_datas_count_get**
> InlineResponse2001 teams_id_dynamic_datas_count_get(id, where=where)

Counts dynamicDatas of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts dynamicDatas of Team.
    api_response = api_instance.teams_id_dynamic_datas_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_fk_delete**
> teams_id_dynamic_datas_fk_delete(id, fk)

Delete a related item by id for dynamicDatas.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Delete a related item by id for dynamicDatas.
    api_instance.teams_id_dynamic_datas_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_fk_get**
> DynamicData teams_id_dynamic_datas_fk_get(id, fk)

Find a related item by id for dynamicDatas.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Find a related item by id for dynamicDatas.
    api_response = api_instance.teams_id_dynamic_datas_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_fk_put**
> DynamicData teams_id_dynamic_datas_fk_put(id, fk, data=data)

Update a related item by id for dynamicDatas.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for dynamicDatas
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Update a related item by id for dynamicDatas.
    api_response = api_instance.teams_id_dynamic_datas_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for dynamicDatas | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_get**
> list[DynamicData] teams_id_dynamic_datas_get(id, filter=filter)

Queries dynamicDatas of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries dynamicDatas of Team.
    api_response = api_instance.teams_id_dynamic_datas_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DynamicData]**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_data_source_mongo_get**
> DataSourceMongo teams_id_dynamic_datas_nk_data_source_mongo_get(id, nk, refresh=refresh)

Fetches belongsTo relation dataSourceMongo.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceMongo.
    api_response = api_instance.teams_id_dynamic_datas_nk_data_source_mongo_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_data_source_mongo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMongo**](DataSourceMongo.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_data_source_ms_sql_get**
> DataSourceMsSql teams_id_dynamic_datas_nk_data_source_ms_sql_get(id, nk, refresh=refresh)

Fetches belongsTo relation dataSourceMsSql.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceMsSql.
    api_response = api_instance.teams_id_dynamic_datas_nk_data_source_ms_sql_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_data_source_ms_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_data_source_my_sql_get**
> DataSourceMySql teams_id_dynamic_datas_nk_data_source_my_sql_get(id, nk, refresh=refresh)

Fetches belongsTo relation dataSourceMySql.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceMySql.
    api_response = api_instance.teams_id_dynamic_datas_nk_data_source_my_sql_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_data_source_my_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMySql**](DataSourceMySql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_data_source_oracle_get**
> DataSourceOracle teams_id_dynamic_datas_nk_data_source_oracle_get(id, nk, refresh=refresh)

Fetches belongsTo relation dataSourceOracle.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceOracle.
    api_response = api_instance.teams_id_dynamic_datas_nk_data_source_oracle_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_data_source_oracle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceOracle**](DataSourceOracle.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_data_source_postgre_sql_get**
> DataSourcePostgreSql teams_id_dynamic_datas_nk_data_source_postgre_sql_get(id, nk, refresh=refresh)

Fetches belongsTo relation dataSourcePostgreSql.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourcePostgreSql.
    api_response = api_instance.teams_id_dynamic_datas_nk_data_source_postgre_sql_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_data_source_postgre_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourcePostgreSql**](DataSourcePostgreSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_data_source_rest_get**
> DataSourceRest teams_id_dynamic_datas_nk_data_source_rest_get(id, nk, refresh=refresh)

Fetches belongsTo relation dataSourceRest.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceRest.
    api_response = api_instance.teams_id_dynamic_datas_nk_data_source_rest_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_data_source_rest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceRest**](DataSourceRest.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_data_source_soap_get**
> DataSourceSoap teams_id_dynamic_datas_nk_data_source_soap_get(id, nk, refresh=refresh)

Fetches belongsTo relation dataSourceSoap.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceSoap.
    api_response = api_instance.teams_id_dynamic_datas_nk_data_source_soap_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_data_source_soap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceSoap**](DataSourceSoap.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_designs_count_get**
> InlineResponse2001 teams_id_dynamic_datas_nk_designs_count_get(id, nk, where=where)

Counts designs of DynamicData.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of DynamicData.
    api_response = api_instance.teams_id_dynamic_datas_nk_designs_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_designs_fk_delete**
> teams_id_dynamic_datas_nk_designs_fk_delete(id, nk, fk)

Delete a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.teams_id_dynamic_datas_nk_designs_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_designs_fk_get**
> Design teams_id_dynamic_datas_nk_designs_fk_get(id, nk, fk)

Find a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.teams_id_dynamic_datas_nk_designs_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_designs_fk_put**
> Design teams_id_dynamic_datas_nk_designs_fk_put(id, nk, fk, data=data)

Update a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.teams_id_dynamic_datas_nk_designs_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_designs_get**
> list[Design] teams_id_dynamic_datas_nk_designs_get(id, nk, filter=filter)

Queries designs of DynamicData.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of DynamicData.
    api_response = api_instance.teams_id_dynamic_datas_nk_designs_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_designs_post**
> Design teams_id_dynamic_datas_nk_designs_post(id, nk, data=data)

Creates a new instance in designs of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.teams_id_dynamic_datas_nk_designs_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_count_get**
> InlineResponse2001 teams_id_dynamic_datas_nk_records_count_get(id, nk, where=where)

Count Dynamic Data records

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count Dynamic Data records
    api_response = api_instance.teams_id_dynamic_datas_nk_records_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_delete**
> object teams_id_dynamic_datas_nk_records_delete(id, nk, where=where)

Delete all matching records.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
where = 'where_example' # str | filter.where object (optional)

try: 
    # Delete all matching records.
    api_response = api_instance.teams_id_dynamic_datas_nk_records_delete(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **where** | **str**| filter.where object | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_fk_delete**
> object teams_id_dynamic_datas_nk_records_fk_delete(id, nk, fk)

Delete a model instance by {{fk}} from the data source.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
fk = 'fk_example' # str | Model id

try: 
    # Delete a model instance by {{fk}} from the data source.
    api_response = api_instance.teams_id_dynamic_datas_nk_records_fk_delete(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **fk** | **str**| Model id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_fk_get**
> object teams_id_dynamic_datas_nk_records_fk_get(id, nk, fk, filter=filter)

Find a model instance by {{fk}} from the data source.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
fk = 'fk_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{fk}} from the data source.
    api_response = api_instance.teams_id_dynamic_datas_nk_records_fk_get(id, nk, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **fk** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_fk_property_name_upload_put**
> object teams_id_dynamic_datas_nk_records_fk_property_name_upload_put(id, nk, fk, property_name, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
fk = 'fk_example' # str | Model id
property_name = 'property_name_example' # str | Model property name
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.teams_id_dynamic_datas_nk_records_fk_property_name_upload_put(id, nk, fk, property_name, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_fk_property_name_upload_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **fk** | **str**| Model id | 
 **property_name** | **str**| Model property name | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_fk_put**
> object teams_id_dynamic_datas_nk_records_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
fk = 'fk_example' # str | Model id
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.teams_id_dynamic_datas_nk_records_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **fk** | **str**| Model id | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_get**
> list[object] teams_id_dynamic_datas_nk_records_get(id, nk, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.teams_id_dynamic_datas_nk_records_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

**list[object]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_migrate_post**
> object teams_id_dynamic_datas_nk_records_migrate_post(id, nk, data=data)

Request migration for Dynamic Data records

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
data = TweakApi.Team() # Team |  (optional)

try: 
    # Request migration for Dynamic Data records
    api_response = api_instance.teams_id_dynamic_datas_nk_records_migrate_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_migrate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **data** | [**Team**](Team.md)|  | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_post**
> object teams_id_dynamic_datas_nk_records_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.teams_id_dynamic_datas_nk_records_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_records_upload_csv_post**
> object teams_id_dynamic_datas_nk_records_upload_csv_post(id, nk)

Upload CSV for this Dynamic Data

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.

try: 
    # Upload CSV for this Dynamic Data
    api_response = api_instance.teams_id_dynamic_datas_nk_records_upload_csv_post(id, nk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_records_upload_csv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_nk_team_get**
> Team teams_id_dynamic_datas_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for dynamicDatas.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_dynamic_datas_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for dynamicDatas. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_dynamic_datas_post**
> DynamicData teams_id_dynamic_datas_post(id, data=data)

Creates a new instance in dynamicDatas of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Creates a new instance in dynamicDatas of this model.
    api_response = api_instance.teams_id_dynamic_datas_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_dynamic_datas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_exists_get**
> InlineResponse2002 teams_id_exists_get(id)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.teams_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_exists_get: %s\n" % e)
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

# **teams_id_get**
> Team teams_id_get(id, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.teams_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_head**
> InlineResponse2002 teams_id_head(id)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.teams_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_head: %s\n" % e)
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

# **teams_id_image_folders_count_get**
> InlineResponse2001 teams_id_image_folders_count_get(id, where=where)

Counts imageFolders of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts imageFolders of Team.
    api_response = api_instance.teams_id_image_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_delete**
> teams_id_image_folders_delete(id)

Deletes all imageFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all imageFolders of this model.
    api_instance.teams_id_image_folders_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_fk_delete**
> teams_id_image_folders_fk_delete(id, fk)

Delete a related item by id for imageFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Delete a related item by id for imageFolders.
    api_instance.teams_id_image_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_fk_get**
> ImageFolder teams_id_image_folders_fk_get(id, fk)

Find a related item by id for imageFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Find a related item by id for imageFolders.
    api_response = api_instance.teams_id_image_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_fk_put**
> ImageFolder teams_id_image_folders_fk_put(id, fk, data=data)

Update a related item by id for imageFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for imageFolders.
    api_response = api_instance.teams_id_image_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for imageFolders | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_get**
> list[ImageFolder] teams_id_image_folders_get(id, filter=filter)

Queries imageFolders of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries imageFolders of Team.
    api_response = api_instance.teams_id_image_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_count_get**
> InlineResponse2001 teams_id_image_folders_nk_children_count_get(id, nk, where=where)

Counts children of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts children of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_children_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_children_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_fk_delete**
> teams_id_image_folders_nk_children_fk_delete(id, nk, fk)

Delete a related item by id for children.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for children

try: 
    # Delete a related item by id for children.
    api_instance.teams_id_image_folders_nk_children_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_children_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for children | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_fk_get**
> ImageFolder teams_id_image_folders_nk_children_fk_get(id, nk, fk)

Find a related item by id for children.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for children

try: 
    # Find a related item by id for children.
    api_response = api_instance.teams_id_image_folders_nk_children_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_children_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for children | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_fk_put**
> ImageFolder teams_id_image_folders_nk_children_fk_put(id, nk, fk, data=data)

Update a related item by id for children.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for children
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for children.
    api_response = api_instance.teams_id_image_folders_nk_children_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_children_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for children | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_get**
> list[ImageFolder] teams_id_image_folders_nk_children_get(id, nk, filter=filter)

Queries children of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries children of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_children_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_post**
> ImageFolder teams_id_image_folders_nk_children_post(id, nk, data=data)

Creates a new instance in children of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in children of this model.
    api_response = api_instance.teams_id_image_folders_nk_children_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_children_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_count_get**
> InlineResponse2001 teams_id_image_folders_nk_folder_members_count_get(id, nk, where=where)

Counts folderMembers of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts folderMembers of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_folder_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_folder_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_delete**
> teams_id_image_folders_nk_folder_members_delete(id, nk)

Deletes all folderMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.

try: 
    # Deletes all folderMembers of this model.
    api_instance.teams_id_image_folders_nk_folder_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_folder_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_fk_delete**
> teams_id_image_folders_nk_folder_members_fk_delete(id, nk, fk)

Delete a related item by id for folderMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for folderMembers

try: 
    # Delete a related item by id for folderMembers.
    api_instance.teams_id_image_folders_nk_folder_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_folder_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for folderMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_fk_get**
> ImageFolderMember teams_id_image_folders_nk_folder_members_fk_get(id, nk, fk)

Find a related item by id for folderMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for folderMembers

try: 
    # Find a related item by id for folderMembers.
    api_response = api_instance.teams_id_image_folders_nk_folder_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_folder_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for folderMembers | 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_fk_put**
> ImageFolderMember teams_id_image_folders_nk_folder_members_fk_put(id, nk, fk, data=data)

Update a related item by id for folderMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for folderMembers
data = TweakApi.ImageFolderMember() # ImageFolderMember |  (optional)

try: 
    # Update a related item by id for folderMembers.
    api_response = api_instance.teams_id_image_folders_nk_folder_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_folder_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for folderMembers | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_get**
> list[ImageFolderMember] teams_id_image_folders_nk_folder_members_get(id, nk, filter=filter)

Queries folderMembers of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries folderMembers of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_folder_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_folder_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolderMember]**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_post**
> ImageFolderMember teams_id_image_folders_nk_folder_members_post(id, nk, data=data)

Creates a new instance in folderMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
data = TweakApi.ImageFolderMember() # ImageFolderMember |  (optional)

try: 
    # Creates a new instance in folderMembers of this model.
    api_response = api_instance.teams_id_image_folders_nk_folder_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_folder_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_count_get**
> InlineResponse2001 teams_id_image_folders_nk_images_count_get(id, nk, where=where)

Counts images of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts images of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_images_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_images_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_fk_delete**
> teams_id_image_folders_nk_images_fk_delete(id, nk, fk)

Delete a related item by id for images.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for images

try: 
    # Delete a related item by id for images.
    api_instance.teams_id_image_folders_nk_images_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_images_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for images | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_fk_get**
> Image teams_id_image_folders_nk_images_fk_get(id, nk, fk)

Find a related item by id for images.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for images

try: 
    # Find a related item by id for images.
    api_response = api_instance.teams_id_image_folders_nk_images_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_images_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for images | 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_fk_put**
> Image teams_id_image_folders_nk_images_fk_put(id, nk, fk, data=data)

Update a related item by id for images.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for images
data = TweakApi.Image() # Image |  (optional)

try: 
    # Update a related item by id for images.
    api_response = api_instance.teams_id_image_folders_nk_images_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_images_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for images | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_get**
> list[Image] teams_id_image_folders_nk_images_get(id, nk, filter=filter)

Queries images of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries images of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_images_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_post**
> Image teams_id_image_folders_nk_images_post(id, nk, data=data)

Creates a new instance in images of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
data = TweakApi.Image() # Image |  (optional)

try: 
    # Creates a new instance in images of this model.
    api_response = api_instance.teams_id_image_folders_nk_images_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_count_get**
> InlineResponse2001 teams_id_image_folders_nk_members_count_get(id, nk, where=where)

Counts members of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_delete**
> teams_id_image_folders_nk_members_delete(id, nk)

Deletes all members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.

try: 
    # Deletes all members of this model.
    api_instance.teams_id_image_folders_nk_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_fk_delete**
> teams_id_image_folders_nk_members_fk_delete(id, nk, fk)

Delete a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.teams_id_image_folders_nk_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_fk_get**
> TeamMember teams_id_image_folders_nk_members_fk_get(id, nk, fk)

Find a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.teams_id_image_folders_nk_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_fk_put**
> TeamMember teams_id_image_folders_nk_members_fk_put(id, nk, fk, data=data)

Update a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.teams_id_image_folders_nk_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_get**
> list[TeamMember] teams_id_image_folders_nk_members_get(id, nk, filter=filter)

Queries members of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_post**
> TeamMember teams_id_image_folders_nk_members_post(id, nk, data=data)

Creates a new instance in members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.teams_id_image_folders_nk_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_rel_fk_delete**
> teams_id_image_folders_nk_members_rel_fk_delete(id, nk, fk)

Remove the members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.teams_id_image_folders_nk_members_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_rel_fk_head**
> bool teams_id_image_folders_nk_members_rel_fk_head(id, nk, fk)

Check the existence of members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.teams_id_image_folders_nk_members_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_rel_fk_put**
> ImageFolderMember teams_id_image_folders_nk_members_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.ImageFolderMember() # ImageFolderMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.teams_id_image_folders_nk_members_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_parent_get**
> ImageFolder teams_id_image_folders_nk_parent_get(id, nk, refresh=refresh)

Fetches belongsTo relation parent.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation parent.
    api_response = api_instance.teams_id_image_folders_nk_parent_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_parent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_count_get**
> InlineResponse2001 teams_id_image_folders_nk_portals_count_get(id, nk, where=where)

Counts portals of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_portals_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_delete**
> teams_id_image_folders_nk_portals_delete(id, nk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.

try: 
    # Deletes all portals of this model.
    api_instance.teams_id_image_folders_nk_portals_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_fk_delete**
> teams_id_image_folders_nk_portals_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.teams_id_image_folders_nk_portals_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_fk_get**
> Portal teams_id_image_folders_nk_portals_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.teams_id_image_folders_nk_portals_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_fk_put**
> Portal teams_id_image_folders_nk_portals_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.teams_id_image_folders_nk_portals_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
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

# **teams_id_image_folders_nk_portals_get**
> list[Portal] teams_id_image_folders_nk_portals_get(id, nk, filter=filter)

Queries portals of ImageFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of ImageFolder.
    api_response = api_instance.teams_id_image_folders_nk_portals_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_post**
> Portal teams_id_image_folders_nk_portals_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.teams_id_image_folders_nk_portals_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_rel_fk_delete**
> teams_id_image_folders_nk_portals_rel_fk_delete(id, nk, fk)

Remove the portals relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Remove the portals relation to an item by id.
    api_instance.teams_id_image_folders_nk_portals_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_rel_fk_head**
> bool teams_id_image_folders_nk_portals_rel_fk_head(id, nk, fk)

Check the existence of portals relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Check the existence of portals relation to an item by id.
    api_response = api_instance.teams_id_image_folders_nk_portals_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_rel_fk_put**
> PortalImageFolder teams_id_image_folders_nk_portals_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for portals.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.PortalImageFolder() # PortalImageFolder |  (optional)

try: 
    # Add a related item by id for portals.
    api_response = api_instance.teams_id_image_folders_nk_portals_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_portals_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)|  | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_team_get**
> Team teams_id_image_folders_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_image_folders_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_post**
> ImageFolder teams_id_image_folders_post(id, data=data)

Creates a new instance in imageFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in imageFolders of this model.
    api_response = api_instance.teams_id_image_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_count_get**
> InlineResponse2001 teams_id_images_count_get(id, where=where)

Counts images of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts images of Team.
    api_response = api_instance.teams_id_images_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_delete**
> teams_id_images_delete(id)

Deletes all images of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all images of this model.
    api_instance.teams_id_images_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_fk_delete**
> teams_id_images_fk_delete(id, fk)

Delete a related item by id for images.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for images

try: 
    # Delete a related item by id for images.
    api_instance.teams_id_images_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for images | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_fk_get**
> Image teams_id_images_fk_get(id, fk)

Find a related item by id for images.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for images

try: 
    # Find a related item by id for images.
    api_response = api_instance.teams_id_images_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for images | 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_fk_put**
> Image teams_id_images_fk_put(id, fk, data=data)

Update a related item by id for images.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for images
data = TweakApi.Image() # Image |  (optional)

try: 
    # Update a related item by id for images.
    api_response = api_instance.teams_id_images_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for images | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_get**
> list[Image] teams_id_images_get(id, filter=filter)

Queries images of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries images of Team.
    api_response = api_instance.teams_id_images_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_nk_folder_get**
> ImageFolder teams_id_images_nk_folder_get(id, nk, refresh=refresh)

Fetches belongsTo relation folder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for images.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation folder.
    api_response = api_instance.teams_id_images_nk_folder_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_nk_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for images. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_nk_team_get**
> Team teams_id_images_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for images.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_images_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for images. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_post**
> Image teams_id_images_post(id, data=data)

Creates a new instance in images of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Image() # Image |  (optional)

try: 
    # Creates a new instance in images of this model.
    api_response = api_instance.teams_id_images_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_invitation_tickets_fk_delete**
> object teams_id_invitation_tickets_fk_delete(id, id2, fk)

Delete InvitationTickets for this Team

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
id2 = 'id_example' # str | Team id
fk = 'fk_example' # str | InvitationTicket id

try: 
    # Delete InvitationTickets for this Team
    api_response = api_instance.teams_id_invitation_tickets_fk_delete(id, id2, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_invitation_tickets_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **id2** | **str**| Team id | 
 **fk** | **str**| InvitationTicket id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_invitation_tickets_fk_get**
> InvitationTicket teams_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)

Get InvitationTicket by Id for this Team

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
id2 = 'id_example' # str | Team id
fk = 'fk_example' # str | InvitationTicket id
filter = 'filter_example' # str | Only include changes that match this filter (optional)

try: 
    # Get InvitationTicket by Id for this Team
    api_response = api_instance.teams_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_invitation_tickets_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **id2** | **str**| Team id | 
 **fk** | **str**| InvitationTicket id | 
 **filter** | **str**| Only include changes that match this filter | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_invitation_tickets_get**
> list[InvitationTicket] teams_id_invitation_tickets_get(id, id2, filter=filter)

List InvitationTickets for this Team

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
id2 = 'id_example' # str | Team id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List InvitationTickets for this Team
    api_response = api_instance.teams_id_invitation_tickets_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_invitation_tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **id2** | **str**| Team id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_logo_put**
> Team teams_id_logo_put(id, id2, data)

Change logo

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
id2 = 'id_example' # str | Team id
data = TweakApi.Team() # Team | Logo

try: 
    # Change logo
    api_response = api_instance.teams_id_logo_put(id, id2, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_logo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **id2** | **str**| Team id | 
 **data** | [**Team**](Team.md)| Logo | 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_count_get**
> InlineResponse2001 teams_id_members_count_get(id, where=where)

Counts members of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Team.
    api_response = api_instance.teams_id_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_delete**
> teams_id_members_delete(id)

Deletes all members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all members of this model.
    api_instance.teams_id_members_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_fk_delete**
> teams_id_members_fk_delete(id, fk)

Delete a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.teams_id_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_fk_get**
> Customer teams_id_members_fk_get(id, fk)

Find a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.teams_id_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_fk_put**
> Customer teams_id_members_fk_put(id, fk, data=data)

Update a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.Customer() # Customer |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.teams_id_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**Customer**](Customer.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_get**
> list[Customer] teams_id_members_get(id, filter=filter)

Queries members of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Team.
    api_response = api_instance.teams_id_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_post**
> Customer teams_id_members_post(id, data=data)

Creates a new instance in members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Customer() # Customer |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.teams_id_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Customer**](Customer.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_rel_fk_delete**
> teams_id_members_rel_fk_delete(id, fk)

Remove the members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.teams_id_members_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_rel_fk_head**
> bool teams_id_members_rel_fk_head(id, fk)

Check the existence of members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.teams_id_members_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_rel_fk_put**
> TeamMember teams_id_members_rel_fk_put(id, fk, data=data)

Add a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.teams_id_members_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_patch**
> Team teams_id_patch(id, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Team() # Team | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.teams_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Team**](Team.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_permission_delete**
> teams_id_permission_delete(id)

Deletes permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes permission of this model.
    api_instance.teams_id_permission_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_permission_get**
> TeamPermissionSet teams_id_permission_get(id, refresh=refresh)

Fetches hasOne relation permission.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.teams_id_permission_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamPermissionSet**](TeamPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_permission_post**
> TeamPermissionSet teams_id_permission_post(id, data=data)

Creates a new instance in permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.TeamPermissionSet() # TeamPermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.teams_id_permission_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**TeamPermissionSet**](TeamPermissionSet.md)|  | [optional] 

### Return type

[**TeamPermissionSet**](TeamPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_permission_put**
> TeamPermissionSet teams_id_permission_put(id, data=data)

Update permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.TeamPermissionSet() # TeamPermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.teams_id_permission_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**TeamPermissionSet**](TeamPermissionSet.md)|  | [optional] 

### Return type

[**TeamPermissionSet**](TeamPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_count_get**
> InlineResponse2001 teams_id_portals_count_get(id, where=where)

Counts portals of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of Team.
    api_response = api_instance.teams_id_portals_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_delete**
> teams_id_portals_delete(id)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all portals of this model.
    api_instance.teams_id_portals_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_fk_delete**
> teams_id_portals_fk_delete(id, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.teams_id_portals_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_fk_get**
> Portal teams_id_portals_fk_get(id, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.teams_id_portals_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_fk_put**
> Portal teams_id_portals_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.teams_id_portals_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
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

# **teams_id_portals_get**
> list[Portal] teams_id_portals_get(id, filter=filter)

Queries portals of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of Team.
    api_response = api_instance.teams_id_portals_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_default_builder_config_get**
> TeamBuilderConfig teams_id_portals_nk_default_builder_config_get(id, nk, refresh=refresh)

Fetches belongsTo relation defaultBuilderConfig.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation defaultBuilderConfig.
    api_response = api_instance.teams_id_portals_nk_default_builder_config_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_default_builder_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_count_get**
> InlineResponse2001 teams_id_portals_nk_design_folders_count_get(id, nk, where=where)

Counts designFolders of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designFolders of Portal.
    api_response = api_instance.teams_id_portals_nk_design_folders_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_design_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_delete**
> teams_id_portals_nk_design_folders_delete(id, nk)

Deletes all designFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all designFolders of this model.
    api_instance.teams_id_portals_nk_design_folders_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_design_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_fk_delete**
> teams_id_portals_nk_design_folders_fk_delete(id, nk, fk)

Delete a related item by id for designFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for designFolders

try: 
    # Delete a related item by id for designFolders.
    api_instance.teams_id_portals_nk_design_folders_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_design_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for designFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_fk_get**
> DesignFolder teams_id_portals_nk_design_folders_fk_get(id, nk, fk)

Find a related item by id for designFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for designFolders

try: 
    # Find a related item by id for designFolders.
    api_response = api_instance.teams_id_portals_nk_design_folders_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_design_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for designFolders | 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_fk_put**
> DesignFolder teams_id_portals_nk_design_folders_fk_put(id, nk, fk, data=data)

Update a related item by id for designFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for designFolders
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Update a related item by id for designFolders.
    api_response = api_instance.teams_id_portals_nk_design_folders_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_design_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for designFolders | 
 **data** | [**DesignFolder**](DesignFolder.md)|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_get**
> list[DesignFolder] teams_id_portals_nk_design_folders_get(id, nk, filter=filter)

Queries designFolders of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designFolders of Portal.
    api_response = api_instance.teams_id_portals_nk_design_folders_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_design_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignFolder]**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_post**
> DesignFolder teams_id_portals_nk_design_folders_post(id, nk, data=data)

Creates a new instance in designFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Creates a new instance in designFolders of this model.
    api_response = api_instance.teams_id_portals_nk_design_folders_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_design_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**DesignFolder**](DesignFolder.md)|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_count_get**
> InlineResponse2001 teams_id_portals_nk_designs_count_get(id, nk, where=where)

Counts designs of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of Portal.
    api_response = api_instance.teams_id_portals_nk_designs_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_fk_delete**
> teams_id_portals_nk_designs_fk_delete(id, nk, fk)

Delete a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.teams_id_portals_nk_designs_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_fk_get**
> Design teams_id_portals_nk_designs_fk_get(id, nk, fk)

Find a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.teams_id_portals_nk_designs_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_fk_put**
> Design teams_id_portals_nk_designs_fk_put(id, nk, fk, data=data)

Update a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.teams_id_portals_nk_designs_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_get**
> list[Design] teams_id_portals_nk_designs_get(id, nk, filter=filter)

Queries designs of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of Portal.
    api_response = api_instance.teams_id_portals_nk_designs_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_post**
> Design teams_id_portals_nk_designs_post(id, nk, data=data)

Creates a new instance in designs of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.teams_id_portals_nk_designs_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_count_get**
> InlineResponse2001 teams_id_portals_nk_image_folders_count_get(id, nk, where=where)

Counts imageFolders of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts imageFolders of Portal.
    api_response = api_instance.teams_id_portals_nk_image_folders_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_delete**
> teams_id_portals_nk_image_folders_delete(id, nk)

Deletes all imageFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all imageFolders of this model.
    api_instance.teams_id_portals_nk_image_folders_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_fk_delete**
> teams_id_portals_nk_image_folders_fk_delete(id, nk, fk)

Delete a related item by id for imageFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Delete a related item by id for imageFolders.
    api_instance.teams_id_portals_nk_image_folders_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_fk_get**
> ImageFolder teams_id_portals_nk_image_folders_fk_get(id, nk, fk)

Find a related item by id for imageFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Find a related item by id for imageFolders.
    api_response = api_instance.teams_id_portals_nk_image_folders_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_fk_put**
> ImageFolder teams_id_portals_nk_image_folders_fk_put(id, nk, fk, data=data)

Update a related item by id for imageFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for imageFolders.
    api_response = api_instance.teams_id_portals_nk_image_folders_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for imageFolders | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_get**
> list[ImageFolder] teams_id_portals_nk_image_folders_get(id, nk, filter=filter)

Queries imageFolders of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries imageFolders of Portal.
    api_response = api_instance.teams_id_portals_nk_image_folders_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_post**
> ImageFolder teams_id_portals_nk_image_folders_post(id, nk, data=data)

Creates a new instance in imageFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in imageFolders of this model.
    api_response = api_instance.teams_id_portals_nk_image_folders_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_rel_fk_delete**
> teams_id_portals_nk_image_folders_rel_fk_delete(id, nk, fk)

Remove the imageFolders relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Remove the imageFolders relation to an item by id.
    api_instance.teams_id_portals_nk_image_folders_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_rel_fk_head**
> bool teams_id_portals_nk_image_folders_rel_fk_head(id, nk, fk)

Check the existence of imageFolders relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Check the existence of imageFolders relation to an item by id.
    api_response = api_instance.teams_id_portals_nk_image_folders_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_rel_fk_put**
> PortalImageFolder teams_id_portals_nk_image_folders_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for imageFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.PortalImageFolder() # PortalImageFolder |  (optional)

try: 
    # Add a related item by id for imageFolders.
    api_response = api_instance.teams_id_portals_nk_image_folders_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_image_folders_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for imageFolders | 
 **data** | [**PortalImageFolder**](PortalImageFolder.md)|  | [optional] 

### Return type

[**PortalImageFolder**](PortalImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_count_get**
> InlineResponse2001 teams_id_portals_nk_members_count_get(id, nk, where=where)

Counts members of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Portal.
    api_response = api_instance.teams_id_portals_nk_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_delete**
> teams_id_portals_nk_members_delete(id, nk)

Deletes all members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all members of this model.
    api_instance.teams_id_portals_nk_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_fk_delete**
> teams_id_portals_nk_members_fk_delete(id, nk, fk)

Delete a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.teams_id_portals_nk_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_fk_get**
> TeamMember teams_id_portals_nk_members_fk_get(id, nk, fk)

Find a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.teams_id_portals_nk_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_fk_put**
> TeamMember teams_id_portals_nk_members_fk_put(id, nk, fk, data=data)

Update a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.teams_id_portals_nk_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_get**
> list[TeamMember] teams_id_portals_nk_members_get(id, nk, filter=filter)

Queries members of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Portal.
    api_response = api_instance.teams_id_portals_nk_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_post**
> TeamMember teams_id_portals_nk_members_post(id, nk, data=data)

Creates a new instance in members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.teams_id_portals_nk_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_rel_fk_delete**
> teams_id_portals_nk_members_rel_fk_delete(id, nk, fk)

Remove the members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.teams_id_portals_nk_members_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_rel_fk_head**
> bool teams_id_portals_nk_members_rel_fk_head(id, nk, fk)

Check the existence of members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.teams_id_portals_nk_members_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_rel_fk_put**
> PortalMember teams_id_portals_nk_members_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.PortalMember() # PortalMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.teams_id_portals_nk_members_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**PortalMember**](PortalMember.md)|  | [optional] 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_permission_delete**
> teams_id_portals_nk_permission_delete(id, nk)

Deletes permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes permission of this model.
    api_instance.teams_id_portals_nk_permission_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_permission_get**
> PortalPermissionSet teams_id_portals_nk_permission_get(id, nk, refresh=refresh)

Fetches hasOne relation permission.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.teams_id_portals_nk_permission_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**PortalPermissionSet**](PortalPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_permission_post**
> PortalPermissionSet teams_id_portals_nk_permission_post(id, nk, data=data)

Creates a new instance in permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.PortalPermissionSet() # PortalPermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.teams_id_portals_nk_permission_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**PortalPermissionSet**](PortalPermissionSet.md)|  | [optional] 

### Return type

[**PortalPermissionSet**](PortalPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_permission_put**
> PortalPermissionSet teams_id_portals_nk_permission_put(id, nk, data=data)

Update permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.PortalPermissionSet() # PortalPermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.teams_id_portals_nk_permission_put(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**PortalPermissionSet**](PortalPermissionSet.md)|  | [optional] 

### Return type

[**PortalPermissionSet**](PortalPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_count_get**
> InlineResponse2001 teams_id_portals_nk_portal_members_count_get(id, nk, where=where)

Counts portalMembers of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portalMembers of Portal.
    api_response = api_instance.teams_id_portals_nk_portal_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_portal_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_delete**
> teams_id_portals_nk_portal_members_delete(id, nk)

Deletes all portalMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all portalMembers of this model.
    api_instance.teams_id_portals_nk_portal_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_portal_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_fk_delete**
> teams_id_portals_nk_portal_members_fk_delete(id, nk, fk)

Delete a related item by id for portalMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for portalMembers

try: 
    # Delete a related item by id for portalMembers.
    api_instance.teams_id_portals_nk_portal_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_portal_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for portalMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_fk_get**
> PortalMember teams_id_portals_nk_portal_members_fk_get(id, nk, fk)

Find a related item by id for portalMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for portalMembers

try: 
    # Find a related item by id for portalMembers.
    api_response = api_instance.teams_id_portals_nk_portal_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_portal_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for portalMembers | 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_fk_put**
> PortalMember teams_id_portals_nk_portal_members_fk_put(id, nk, fk, data=data)

Update a related item by id for portalMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for portalMembers
data = TweakApi.PortalMember() # PortalMember |  (optional)

try: 
    # Update a related item by id for portalMembers.
    api_response = api_instance.teams_id_portals_nk_portal_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_portal_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for portalMembers | 
 **data** | [**PortalMember**](PortalMember.md)|  | [optional] 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_get**
> list[PortalMember] teams_id_portals_nk_portal_members_get(id, nk, filter=filter)

Queries portalMembers of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portalMembers of Portal.
    api_response = api_instance.teams_id_portals_nk_portal_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_portal_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalMember]**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_post**
> PortalMember teams_id_portals_nk_portal_members_post(id, nk, data=data)

Creates a new instance in portalMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.PortalMember() # PortalMember |  (optional)

try: 
    # Creates a new instance in portalMembers of this model.
    api_response = api_instance.teams_id_portals_nk_portal_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_portal_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**PortalMember**](PortalMember.md)|  | [optional] 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_team_get**
> Team teams_id_portals_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_portals_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_count_get**
> InlineResponse2001 teams_id_portals_nk_template_folders_count_get(id, nk, where=where)

Counts templateFolders of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateFolders of Portal.
    api_response = api_instance.teams_id_portals_nk_template_folders_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_delete**
> teams_id_portals_nk_template_folders_delete(id, nk)

Deletes all templateFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all templateFolders of this model.
    api_instance.teams_id_portals_nk_template_folders_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_fk_delete**
> teams_id_portals_nk_template_folders_fk_delete(id, nk, fk)

Delete a related item by id for templateFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Delete a related item by id for templateFolders.
    api_instance.teams_id_portals_nk_template_folders_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_fk_get**
> PortalTemplateFolder teams_id_portals_nk_template_folders_fk_get(id, nk, fk)

Find a related item by id for templateFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Find a related item by id for templateFolders.
    api_response = api_instance.teams_id_portals_nk_template_folders_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_fk_put**
> PortalTemplateFolder teams_id_portals_nk_template_folders_fk_put(id, nk, fk, data=data)

Update a related item by id for templateFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templateFolders
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Update a related item by id for templateFolders.
    api_response = api_instance.teams_id_portals_nk_template_folders_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templateFolders | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_get**
> list[PortalTemplateFolder] teams_id_portals_nk_template_folders_get(id, nk, filter=filter)

Queries templateFolders of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateFolders of Portal.
    api_response = api_instance.teams_id_portals_nk_template_folders_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalTemplateFolder]**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_post**
> PortalTemplateFolder teams_id_portals_nk_template_folders_post(id, nk, data=data)

Creates a new instance in templateFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Creates a new instance in templateFolders of this model.
    api_response = api_instance.teams_id_portals_nk_template_folders_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_count_get**
> InlineResponse2001 teams_id_portals_nk_template_rels_count_get(id, nk, where=where)

Counts templateRels of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateRels of Portal.
    api_response = api_instance.teams_id_portals_nk_template_rels_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_rels_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_delete**
> teams_id_portals_nk_template_rels_delete(id, nk)

Deletes all templateRels of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all templateRels of this model.
    api_instance.teams_id_portals_nk_template_rels_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_rels_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_fk_delete**
> teams_id_portals_nk_template_rels_fk_delete(id, nk, fk)

Delete a related item by id for templateRels.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templateRels

try: 
    # Delete a related item by id for templateRels.
    api_instance.teams_id_portals_nk_template_rels_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_rels_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templateRels | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_fk_get**
> PortalTemplate teams_id_portals_nk_template_rels_fk_get(id, nk, fk)

Find a related item by id for templateRels.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templateRels

try: 
    # Find a related item by id for templateRels.
    api_response = api_instance.teams_id_portals_nk_template_rels_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_rels_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templateRels | 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_fk_put**
> PortalTemplate teams_id_portals_nk_template_rels_fk_put(id, nk, fk, data=data)

Update a related item by id for templateRels.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templateRels
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Update a related item by id for templateRels.
    api_response = api_instance.teams_id_portals_nk_template_rels_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_rels_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templateRels | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_get**
> list[PortalTemplate] teams_id_portals_nk_template_rels_get(id, nk, filter=filter)

Queries templateRels of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateRels of Portal.
    api_response = api_instance.teams_id_portals_nk_template_rels_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_rels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalTemplate]**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_post**
> PortalTemplate teams_id_portals_nk_template_rels_post(id, nk, data=data)

Creates a new instance in templateRels of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Creates a new instance in templateRels of this model.
    api_response = api_instance.teams_id_portals_nk_template_rels_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_template_rels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_count_get**
> InlineResponse2001 teams_id_portals_nk_templates_count_get(id, nk, where=where)

Counts templates of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of Portal.
    api_response = api_instance.teams_id_portals_nk_templates_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_delete**
> teams_id_portals_nk_templates_delete(id, nk)

Deletes all templates of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all templates of this model.
    api_instance.teams_id_portals_nk_templates_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_fk_delete**
> teams_id_portals_nk_templates_fk_delete(id, nk, fk)

Delete a related item by id for templates.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.teams_id_portals_nk_templates_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_fk_get**
> Template teams_id_portals_nk_templates_fk_get(id, nk, fk)

Find a related item by id for templates.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.teams_id_portals_nk_templates_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_fk_put**
> Template teams_id_portals_nk_templates_fk_put(id, nk, fk, data=data)

Update a related item by id for templates.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.teams_id_portals_nk_templates_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_get**
> list[Template] teams_id_portals_nk_templates_get(id, nk, filter=filter)

Queries templates of Portal.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of Portal.
    api_response = api_instance.teams_id_portals_nk_templates_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_post**
> Template teams_id_portals_nk_templates_post(id, nk, data=data)

Creates a new instance in templates of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.teams_id_portals_nk_templates_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_rel_fk_delete**
> teams_id_portals_nk_templates_rel_fk_delete(id, nk, fk)

Remove the templates relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Remove the templates relation to an item by id.
    api_instance.teams_id_portals_nk_templates_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_rel_fk_head**
> bool teams_id_portals_nk_templates_rel_fk_head(id, nk, fk)

Check the existence of templates relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Check the existence of templates relation to an item by id.
    api_response = api_instance.teams_id_portals_nk_templates_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templates | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_rel_fk_put**
> PortalTemplate teams_id_portals_nk_templates_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for templates.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Add a related item by id for templates.
    api_response = api_instance.teams_id_portals_nk_templates_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_templates_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_post**
> Portal teams_id_portals_post(id, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.teams_id_portals_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_count_get**
> InlineResponse2001 teams_id_product_materials_count_get(id, where=where)

Counts productMaterials of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productMaterials of Team.
    api_response = api_instance.teams_id_product_materials_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_delete**
> teams_id_product_materials_delete(id)

Deletes all productMaterials of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all productMaterials of this model.
    api_instance.teams_id_product_materials_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_fk_delete**
> teams_id_product_materials_fk_delete(id, fk)

Delete a related item by id for productMaterials.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productMaterials

try: 
    # Delete a related item by id for productMaterials.
    api_instance.teams_id_product_materials_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_fk_get**
> ProductMaterial teams_id_product_materials_fk_get(id, fk)

Find a related item by id for productMaterials.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productMaterials

try: 
    # Find a related item by id for productMaterials.
    api_response = api_instance.teams_id_product_materials_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productMaterials | 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_fk_put**
> ProductMaterial teams_id_product_materials_fk_put(id, fk, data=data)

Update a related item by id for productMaterials.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productMaterials
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Update a related item by id for productMaterials.
    api_response = api_instance.teams_id_product_materials_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productMaterials | 
 **data** | [**ProductMaterial**](ProductMaterial.md)|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_get**
> list[ProductMaterial] teams_id_product_materials_get(id, filter=filter)

Queries productMaterials of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productMaterials of Team.
    api_response = api_instance.teams_id_product_materials_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductMaterial]**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_nk_team_get**
> Team teams_id_product_materials_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for productMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_product_materials_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for productMaterials. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_materials_post**
> ProductMaterial teams_id_product_materials_post(id, data=data)

Creates a new instance in productMaterials of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Creates a new instance in productMaterials of this model.
    api_response = api_instance.teams_id_product_materials_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**ProductMaterial**](ProductMaterial.md)|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_available_get**
> list[ProductPdfColorProfile] teams_id_product_pdf_color_profiles_available_get(id, filter=filter)

Find all available PdfColorProfile

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all available PdfColorProfile
    api_response = api_instance.teams_id_product_pdf_color_profiles_available_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ProductPdfColorProfile]**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_count_get**
> InlineResponse2001 teams_id_product_pdf_color_profiles_count_get(id, where=where)

Counts productPdfColorProfiles of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productPdfColorProfiles of Team.
    api_response = api_instance.teams_id_product_pdf_color_profiles_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_delete**
> teams_id_product_pdf_color_profiles_delete(id)

Deletes all productPdfColorProfiles of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all productPdfColorProfiles of this model.
    api_instance.teams_id_product_pdf_color_profiles_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_fk_delete**
> teams_id_product_pdf_color_profiles_fk_delete(id, fk)

Delete a related item by id for productPdfColorProfiles.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productPdfColorProfiles

try: 
    # Delete a related item by id for productPdfColorProfiles.
    api_instance.teams_id_product_pdf_color_profiles_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productPdfColorProfiles | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_fk_get**
> ProductPdfColorProfile teams_id_product_pdf_color_profiles_fk_get(id, fk)

Find a related item by id for productPdfColorProfiles.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productPdfColorProfiles

try: 
    # Find a related item by id for productPdfColorProfiles.
    api_response = api_instance.teams_id_product_pdf_color_profiles_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productPdfColorProfiles | 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_fk_put**
> ProductPdfColorProfile teams_id_product_pdf_color_profiles_fk_put(id, fk, data=data)

Update a related item by id for productPdfColorProfiles.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productPdfColorProfiles
data = TweakApi.ProductPdfColorProfile() # ProductPdfColorProfile |  (optional)

try: 
    # Update a related item by id for productPdfColorProfiles.
    api_response = api_instance.teams_id_product_pdf_color_profiles_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productPdfColorProfiles | 
 **data** | [**ProductPdfColorProfile**](ProductPdfColorProfile.md)|  | [optional] 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_get**
> list[ProductPdfColorProfile] teams_id_product_pdf_color_profiles_get(id, filter=filter)

Queries productPdfColorProfiles of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productPdfColorProfiles of Team.
    api_response = api_instance.teams_id_product_pdf_color_profiles_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductPdfColorProfile]**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_pdf_color_profiles_upload_post**
> ProductPdfColorProfile teams_id_product_pdf_color_profiles_upload_post(id)

Upload ICC PDF Color Profile for this Team

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Upload ICC PDF Color Profile for this Team
    api_response = api_instance.teams_id_product_pdf_color_profiles_upload_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_pdf_color_profiles_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_size_materials_count_get**
> InlineResponse2001 teams_id_product_size_materials_count_get(id, where=where)

Counts productSizeMaterials of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizeMaterials of Team.
    api_response = api_instance.teams_id_product_size_materials_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_size_materials_delete**
> teams_id_product_size_materials_delete(id)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all productSizeMaterials of this model.
    api_instance.teams_id_product_size_materials_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_size_materials_fk_delete**
> teams_id_product_size_materials_fk_delete(id, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Delete a related item by id for productSizeMaterials.
    api_instance.teams_id_product_size_materials_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_size_materials_fk_get**
> ProductSizeMaterial teams_id_product_size_materials_fk_get(id, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Find a related item by id for productSizeMaterials.
    api_response = api_instance.teams_id_product_size_materials_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_size_materials_fk_put**
> ProductSizeMaterial teams_id_product_size_materials_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for productSizeMaterials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for productSizeMaterials.
    api_response = api_instance.teams_id_product_size_materials_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
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

# **teams_id_product_size_materials_get**
> list[ProductSizeMaterial] teams_id_product_size_materials_get(id, filter=filter)

Queries productSizeMaterials of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizeMaterials of Team.
    api_response = api_instance.teams_id_product_size_materials_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_product_size_materials_nk_material_get**
> ProductMaterial teams_id_product_size_materials_nk_material_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation material.
    api_response = api_instance.teams_id_product_size_materials_nk_material_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_nk_material_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
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

# **teams_id_product_size_materials_nk_pdf_color_profile_get**
> ProductPdfColorProfile teams_id_product_size_materials_nk_pdf_color_profile_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation pdfColorProfile.
    api_response = api_instance.teams_id_product_size_materials_nk_pdf_color_profile_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_nk_pdf_color_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
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

# **teams_id_product_size_materials_nk_size_get**
> ProductSize teams_id_product_size_materials_nk_size_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation size.
    api_response = api_instance.teams_id_product_size_materials_nk_size_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_nk_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
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

# **teams_id_product_size_materials_nk_team_get**
> Team teams_id_product_size_materials_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for productSizeMaterials.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_product_size_materials_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
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

# **teams_id_product_size_materials_post**
> ProductSizeMaterial teams_id_product_size_materials_post(id, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in productSizeMaterials of this model.
    api_response = api_instance.teams_id_product_size_materials_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_product_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_put**
> Team teams_id_put(id, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Model id
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.teams_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_replace_post**
> Team teams_id_replace_post(id, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Model id
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.teams_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_data_source_mongo_get**
> DataSourceMongo teams_id_team_data_data_source_mongo_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceMongo.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceMongo.
    api_response = api_instance.teams_id_team_data_data_source_mongo_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_data_source_mongo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMongo**](DataSourceMongo.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_data_source_ms_sql_get**
> DataSourceMsSql teams_id_team_data_data_source_ms_sql_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceMsSql.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceMsSql.
    api_response = api_instance.teams_id_team_data_data_source_ms_sql_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_data_source_ms_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMsSql**](DataSourceMsSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_data_source_my_sql_get**
> DataSourceMySql teams_id_team_data_data_source_my_sql_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceMySql.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceMySql.
    api_response = api_instance.teams_id_team_data_data_source_my_sql_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_data_source_my_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceMySql**](DataSourceMySql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_data_source_oracle_get**
> DataSourceOracle teams_id_team_data_data_source_oracle_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceOracle.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceOracle.
    api_response = api_instance.teams_id_team_data_data_source_oracle_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_data_source_oracle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceOracle**](DataSourceOracle.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_data_source_postgre_sql_get**
> DataSourcePostgreSql teams_id_team_data_data_source_postgre_sql_get(id, refresh=refresh)

Fetches belongsTo relation dataSourcePostgreSql.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourcePostgreSql.
    api_response = api_instance.teams_id_team_data_data_source_postgre_sql_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_data_source_postgre_sql_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourcePostgreSql**](DataSourcePostgreSql.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_data_source_rest_get**
> DataSourceRest teams_id_team_data_data_source_rest_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceRest.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceRest.
    api_response = api_instance.teams_id_team_data_data_source_rest_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_data_source_rest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceRest**](DataSourceRest.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_data_source_soap_get**
> DataSourceSoap teams_id_team_data_data_source_soap_get(id, refresh=refresh)

Fetches belongsTo relation dataSourceSoap.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation dataSourceSoap.
    api_response = api_instance.teams_id_team_data_data_source_soap_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_data_source_soap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DataSourceSoap**](DataSourceSoap.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_designs_count_get**
> InlineResponse2001 teams_id_team_data_designs_count_get(id, where=where)

Counts designs of DynamicData.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of DynamicData.
    api_response = api_instance.teams_id_team_data_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_designs_fk_delete**
> teams_id_team_data_designs_fk_delete(id, fk)

Delete a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.teams_id_team_data_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_designs_fk_get**
> Design teams_id_team_data_designs_fk_get(id, fk)

Find a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.teams_id_team_data_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_designs_fk_put**
> Design teams_id_team_data_designs_fk_put(id, fk, data=data)

Update a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.teams_id_team_data_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_designs_get**
> list[Design] teams_id_team_data_designs_get(id, filter=filter)

Queries designs of DynamicData.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of DynamicData.
    api_response = api_instance.teams_id_team_data_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_designs_post**
> Design teams_id_team_data_designs_post(id, data=data)

Creates a new instance in designs of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.teams_id_team_data_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_get**
> DynamicData teams_id_team_data_get(id, refresh=refresh)

Fetches belongsTo relation teamData.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation teamData.
    api_response = api_instance.teams_id_team_data_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_count_get**
> InlineResponse2001 teams_id_team_data_records_count_get(id, where=where)

Count Dynamic Data records

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count Dynamic Data records
    api_response = api_instance.teams_id_team_data_records_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_delete**
> object teams_id_team_data_records_delete(id, where=where)

Delete all matching records.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | filter.where object (optional)

try: 
    # Delete all matching records.
    api_response = api_instance.teams_id_team_data_records_delete(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| filter.where object | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_fk_delete**
> object teams_id_team_data_records_fk_delete(id, fk)

Delete a model instance by {{fk}} from the data source.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Model id

try: 
    # Delete a model instance by {{fk}} from the data source.
    api_response = api_instance.teams_id_team_data_records_fk_delete(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Model id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_fk_get**
> object teams_id_team_data_records_fk_get(id, fk, filter=filter)

Find a model instance by {{fk}} from the data source.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{fk}} from the data source.
    api_response = api_instance.teams_id_team_data_records_fk_get(id, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_fk_property_name_upload_put**
> object teams_id_team_data_records_fk_property_name_upload_put(id, fk, property_name, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Model id
property_name = 'property_name_example' # str | Model property name
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.teams_id_team_data_records_fk_property_name_upload_put(id, fk, property_name, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_fk_property_name_upload_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Model id | 
 **property_name** | **str**| Model property name | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_fk_put**
> object teams_id_team_data_records_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Model id
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.teams_id_team_data_records_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Model id | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_get**
> list[object] teams_id_team_data_records_get(id, filter=filter)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.teams_id_team_data_records_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

**list[object]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_migrate_post**
> object teams_id_team_data_records_migrate_post(id, data=data)

Request migration for Dynamic Data records

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Team() # Team |  (optional)

try: 
    # Request migration for Dynamic Data records
    api_response = api_instance.teams_id_team_data_records_migrate_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_migrate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Team**](Team.md)|  | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_post**
> object teams_id_team_data_records_post(id, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.teams_id_team_data_records_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_records_upload_csv_post**
> object teams_id_team_data_records_upload_csv_post(id)

Upload CSV for this Dynamic Data

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Upload CSV for this Dynamic Data
    api_response = api_instance.teams_id_team_data_records_upload_csv_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_records_upload_csv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_data_team_get**
> Team teams_id_team_data_team_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_team_data_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_data_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_count_get**
> InlineResponse2001 teams_id_team_members_count_get(id, where=where)

Counts teamMembers of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts teamMembers of Team.
    api_response = api_instance.teams_id_team_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_delete**
> teams_id_team_members_delete(id)

Deletes all teamMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all teamMembers of this model.
    api_instance.teams_id_team_members_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_fk_delete**
> teams_id_team_members_fk_delete(id, fk)

Delete a related item by id for teamMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for teamMembers

try: 
    # Delete a related item by id for teamMembers.
    api_instance.teams_id_team_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for teamMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_fk_get**
> TeamMember teams_id_team_members_fk_get(id, fk)

Find a related item by id for teamMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for teamMembers

try: 
    # Find a related item by id for teamMembers.
    api_response = api_instance.teams_id_team_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for teamMembers | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_fk_put**
> TeamMember teams_id_team_members_fk_put(id, fk, data=data)

Update a related item by id for teamMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for teamMembers
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for teamMembers.
    api_response = api_instance.teams_id_team_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for teamMembers | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_get**
> list[TeamMember] teams_id_team_members_get(id, filter=filter)

Queries teamMembers of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries teamMembers of Team.
    api_response = api_instance.teams_id_team_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_map_keys_get**
> list[object] teams_id_team_members_map_keys_get(id, data)

Map teamMembers emails to teamMembers keys

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Team() # Team | TeamMember(s) email

try: 
    # Map teamMembers emails to teamMembers keys
    api_response = api_instance.teams_id_team_members_map_keys_get(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_map_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Team**](Team.md)| TeamMember(s) email | 

### Return type

**list[object]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_post**
> TeamMember teams_id_team_members_post(id, data=data)

Creates a new instance in teamMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in teamMembers of this model.
    api_response = api_instance.teams_id_team_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_count_get**
> InlineResponse2001 teams_id_template_folders_count_get(id, where=where)

Counts templateFolders of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateFolders of Team.
    api_response = api_instance.teams_id_template_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_template_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_delete**
> teams_id_template_folders_delete(id)

Deletes all templateFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all templateFolders of this model.
    api_instance.teams_id_template_folders_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_template_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_fk_delete**
> teams_id_template_folders_fk_delete(id, fk)

Delete a related item by id for templateFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Delete a related item by id for templateFolders.
    api_instance.teams_id_template_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_template_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_fk_get**
> TeamTemplateFolder teams_id_template_folders_fk_get(id, fk)

Find a related item by id for templateFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Find a related item by id for templateFolders.
    api_response = api_instance.teams_id_template_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_template_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_fk_put**
> TeamTemplateFolder teams_id_template_folders_fk_put(id, fk, data=data)

Update a related item by id for templateFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for templateFolders
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Update a related item by id for templateFolders.
    api_response = api_instance.teams_id_template_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_template_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for templateFolders | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_get**
> list[TeamTemplateFolder] teams_id_template_folders_get(id, filter=filter)

Queries templateFolders of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateFolders of Team.
    api_response = api_instance.teams_id_template_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamTemplateFolder]**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_post**
> TeamTemplateFolder teams_id_template_folders_post(id, data=data)

Creates a new instance in templateFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Creates a new instance in templateFolders of this model.
    api_response = api_instance.teams_id_template_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_template_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_count_get**
> InlineResponse2001 teams_id_templates_count_get(id, where=where)

Counts templates of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of Team.
    api_response = api_instance.teams_id_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_delete**
> teams_id_templates_delete(id)

Deletes all templates of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all templates of this model.
    api_instance.teams_id_templates_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_fk_delete**
> teams_id_templates_fk_delete(id, fk)

Delete a related item by id for templates.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.teams_id_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_fk_get**
> Template teams_id_templates_fk_get(id, fk)

Find a related item by id for templates.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.teams_id_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_fk_put**
> Template teams_id_templates_fk_put(id, fk, data=data)

Update a related item by id for templates.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.teams_id_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_get**
> list[Template] teams_id_templates_get(id, filter=filter)

Queries templates of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of Team.
    api_response = api_instance.teams_id_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_count_get**
> InlineResponse2001 teams_id_templates_nk_designs_count_get(id, nk, where=where)

Counts designs of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of Template.
    api_response = api_instance.teams_id_templates_nk_designs_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_fk_delete**
> teams_id_templates_nk_designs_fk_delete(id, nk, fk)

Delete a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.teams_id_templates_nk_designs_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_fk_get**
> Design teams_id_templates_nk_designs_fk_get(id, nk, fk)

Find a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.teams_id_templates_nk_designs_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_fk_put**
> Design teams_id_templates_nk_designs_fk_put(id, nk, fk, data=data)

Update a related item by id for designs.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.teams_id_templates_nk_designs_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for designs | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_get**
> list[Design] teams_id_templates_nk_designs_get(id, nk, filter=filter)

Queries designs of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of Template.
    api_response = api_instance.teams_id_templates_nk_designs_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_post**
> Design teams_id_templates_nk_designs_post(id, nk, data=data)

Creates a new instance in designs of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.teams_id_templates_nk_designs_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_count_get**
> InlineResponse2001 teams_id_templates_nk_members_count_get(id, nk, where=where)

Counts members of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Template.
    api_response = api_instance.teams_id_templates_nk_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_delete**
> teams_id_templates_nk_members_delete(id, nk)

Deletes all members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.

try: 
    # Deletes all members of this model.
    api_instance.teams_id_templates_nk_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_fk_delete**
> teams_id_templates_nk_members_fk_delete(id, nk, fk)

Delete a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.teams_id_templates_nk_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_fk_get**
> TeamMember teams_id_templates_nk_members_fk_get(id, nk, fk)

Find a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.teams_id_templates_nk_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_fk_put**
> TeamMember teams_id_templates_nk_members_fk_put(id, nk, fk, data=data)

Update a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.teams_id_templates_nk_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_get**
> list[TeamMember] teams_id_templates_nk_members_get(id, nk, filter=filter)

Queries members of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Template.
    api_response = api_instance.teams_id_templates_nk_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_post**
> TeamMember teams_id_templates_nk_members_post(id, nk, data=data)

Creates a new instance in members of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.teams_id_templates_nk_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_rel_fk_delete**
> teams_id_templates_nk_members_rel_fk_delete(id, nk, fk)

Remove the members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.teams_id_templates_nk_members_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_rel_fk_head**
> bool teams_id_templates_nk_members_rel_fk_head(id, nk, fk)

Check the existence of members relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.teams_id_templates_nk_members_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_rel_fk_put**
> TemplateMember teams_id_templates_nk_members_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for members.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TemplateMember() # TemplateMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.teams_id_templates_nk_members_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for members | 
 **data** | [**TemplateMember**](TemplateMember.md)|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_permission_delete**
> teams_id_templates_nk_permission_delete(id, nk)

Deletes permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.

try: 
    # Deletes permission of this model.
    api_instance.teams_id_templates_nk_permission_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_permission_get**
> TemplatePermissionSet teams_id_templates_nk_permission_get(id, nk, refresh=refresh)

Fetches hasOne relation permission.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.teams_id_templates_nk_permission_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TemplatePermissionSet**](TemplatePermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_permission_post**
> TemplatePermissionSet teams_id_templates_nk_permission_post(id, nk, data=data)

Creates a new instance in permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.TemplatePermissionSet() # TemplatePermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.teams_id_templates_nk_permission_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**TemplatePermissionSet**](TemplatePermissionSet.md)|  | [optional] 

### Return type

[**TemplatePermissionSet**](TemplatePermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_permission_put**
> TemplatePermissionSet teams_id_templates_nk_permission_put(id, nk, data=data)

Update permission of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.TemplatePermissionSet() # TemplatePermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.teams_id_templates_nk_permission_put(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**TemplatePermissionSet**](TemplatePermissionSet.md)|  | [optional] 

### Return type

[**TemplatePermissionSet**](TemplatePermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_count_get**
> InlineResponse2001 teams_id_templates_nk_portal_folders_count_get(id, nk, where=where)

Counts portalFolders of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portalFolders of Template.
    api_response = api_instance.teams_id_templates_nk_portal_folders_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_delete**
> teams_id_templates_nk_portal_folders_delete(id, nk)

Deletes all portalFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.

try: 
    # Deletes all portalFolders of this model.
    api_instance.teams_id_templates_nk_portal_folders_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_fk_delete**
> teams_id_templates_nk_portal_folders_fk_delete(id, nk, fk)

Delete a related item by id for portalFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Delete a related item by id for portalFolders.
    api_instance.teams_id_templates_nk_portal_folders_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_fk_get**
> PortalTemplateFolder teams_id_templates_nk_portal_folders_fk_get(id, nk, fk)

Find a related item by id for portalFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Find a related item by id for portalFolders.
    api_response = api_instance.teams_id_templates_nk_portal_folders_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_fk_put**
> PortalTemplateFolder teams_id_templates_nk_portal_folders_fk_put(id, nk, fk, data=data)

Update a related item by id for portalFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portalFolders
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Update a related item by id for portalFolders.
    api_response = api_instance.teams_id_templates_nk_portal_folders_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portalFolders | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_get**
> list[PortalTemplateFolder] teams_id_templates_nk_portal_folders_get(id, nk, filter=filter)

Queries portalFolders of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portalFolders of Template.
    api_response = api_instance.teams_id_templates_nk_portal_folders_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalTemplateFolder]**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_post**
> PortalTemplateFolder teams_id_templates_nk_portal_folders_post(id, nk, data=data)

Creates a new instance in portalFolders of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Creates a new instance in portalFolders of this model.
    api_response = api_instance.teams_id_templates_nk_portal_folders_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_rel_fk_delete**
> teams_id_templates_nk_portal_folders_rel_fk_delete(id, nk, fk)

Remove the portalFolders relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Remove the portalFolders relation to an item by id.
    api_instance.teams_id_templates_nk_portal_folders_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_rel_fk_head**
> bool teams_id_templates_nk_portal_folders_rel_fk_head(id, nk, fk)

Check the existence of portalFolders relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portalFolders

try: 
    # Check the existence of portalFolders relation to an item by id.
    api_response = api_instance.teams_id_templates_nk_portal_folders_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portalFolders | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_rel_fk_put**
> PortalTemplate teams_id_templates_nk_portal_folders_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for portalFolders.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portalFolders
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Add a related item by id for portalFolders.
    api_response = api_instance.teams_id_templates_nk_portal_folders_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portal_folders_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portalFolders | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_count_get**
> InlineResponse2001 teams_id_templates_nk_portals_count_get(id, nk, where=where)

Counts portals of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of Template.
    api_response = api_instance.teams_id_templates_nk_portals_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_delete**
> teams_id_templates_nk_portals_delete(id, nk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.

try: 
    # Deletes all portals of this model.
    api_instance.teams_id_templates_nk_portals_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_fk_delete**
> teams_id_templates_nk_portals_fk_delete(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.teams_id_templates_nk_portals_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_fk_get**
> Portal teams_id_templates_nk_portals_fk_get(id, nk, fk)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.teams_id_templates_nk_portals_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_fk_put**
> Portal teams_id_templates_nk_portals_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.teams_id_templates_nk_portals_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
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

# **teams_id_templates_nk_portals_get**
> list[Portal] teams_id_templates_nk_portals_get(id, nk, filter=filter)

Queries portals of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of Template.
    api_response = api_instance.teams_id_templates_nk_portals_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_post**
> Portal teams_id_templates_nk_portals_post(id, nk, data=data)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.teams_id_templates_nk_portals_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_rel_fk_delete**
> teams_id_templates_nk_portals_rel_fk_delete(id, nk, fk)

Remove the portals relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Remove the portals relation to an item by id.
    api_instance.teams_id_templates_nk_portals_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_rel_fk_head**
> bool teams_id_templates_nk_portals_rel_fk_head(id, nk, fk)

Check the existence of portals relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Check the existence of portals relation to an item by id.
    api_response = api_instance.teams_id_templates_nk_portals_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_rel_fk_put**
> PortalTemplate teams_id_templates_nk_portals_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for portals.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Add a related item by id for portals.
    api_response = api_instance.teams_id_templates_nk_portals_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_portals_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_count_get**
> InlineResponse2001 teams_id_templates_nk_tags_count_get(id, nk, where=where)

Counts tags of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts tags of Template.
    api_response = api_instance.teams_id_templates_nk_tags_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_delete**
> teams_id_templates_nk_tags_delete(id, nk)

Deletes all tags of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.

try: 
    # Deletes all tags of this model.
    api_instance.teams_id_templates_nk_tags_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_fk_delete**
> teams_id_templates_nk_tags_fk_delete(id, nk, fk)

Delete a related item by id for tags.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Delete a related item by id for tags.
    api_instance.teams_id_templates_nk_tags_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_fk_get**
> Tag teams_id_templates_nk_tags_fk_get(id, nk, fk)

Find a related item by id for tags.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Find a related item by id for tags.
    api_response = api_instance.teams_id_templates_nk_tags_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_fk_put**
> Tag teams_id_templates_nk_tags_fk_put(id, nk, fk, data=data)

Update a related item by id for tags.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Update a related item by id for tags.
    api_response = api_instance.teams_id_templates_nk_tags_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for tags | 
 **data** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_get**
> list[Tag] teams_id_templates_nk_tags_get(id, nk, filter=filter)

Queries tags of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries tags of Template.
    api_response = api_instance.teams_id_templates_nk_tags_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_post**
> Tag teams_id_templates_nk_tags_post(id, nk, data=data)

Creates a new instance in tags of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Creates a new instance in tags of this model.
    api_response = api_instance.teams_id_templates_nk_tags_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_rel_fk_delete**
> teams_id_templates_nk_tags_rel_fk_delete(id, nk, fk)

Remove the tags relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Remove the tags relation to an item by id.
    api_instance.teams_id_templates_nk_tags_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_rel_fk_head**
> bool teams_id_templates_nk_tags_rel_fk_head(id, nk, fk)

Check the existence of tags relation to an item by id.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Check the existence of tags relation to an item by id.
    api_response = api_instance.teams_id_templates_nk_tags_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_rel_fk_put**
> TemplateTag teams_id_templates_nk_tags_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for tags.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.TemplateTag() # TemplateTag |  (optional)

try: 
    # Add a related item by id for tags.
    api_response = api_instance.teams_id_templates_nk_tags_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_tags_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for tags | 
 **data** | [**TemplateTag**](TemplateTag.md)|  | [optional] 

### Return type

[**TemplateTag**](TemplateTag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_team_folder_get**
> TeamTemplateFolder teams_id_templates_nk_team_folder_get(id, nk, refresh=refresh)

Fetches belongsTo relation teamFolder.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation teamFolder.
    api_response = api_instance.teams_id_templates_nk_team_folder_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_team_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_team_get**
> Team teams_id_templates_nk_team_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.teams_id_templates_nk_team_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_count_get**
> InlineResponse2001 teams_id_templates_nk_template_members_count_get(id, nk, where=where)

Counts templateMembers of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateMembers of Template.
    api_response = api_instance.teams_id_templates_nk_template_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_template_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_delete**
> teams_id_templates_nk_template_members_delete(id, nk)

Deletes all templateMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.

try: 
    # Deletes all templateMembers of this model.
    api_instance.teams_id_templates_nk_template_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_template_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_fk_delete**
> teams_id_templates_nk_template_members_fk_delete(id, nk, fk)

Delete a related item by id for templateMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for templateMembers

try: 
    # Delete a related item by id for templateMembers.
    api_instance.teams_id_templates_nk_template_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_template_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for templateMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_fk_get**
> TemplateMember teams_id_templates_nk_template_members_fk_get(id, nk, fk)

Find a related item by id for templateMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for templateMembers

try: 
    # Find a related item by id for templateMembers.
    api_response = api_instance.teams_id_templates_nk_template_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_template_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for templateMembers | 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_fk_put**
> TemplateMember teams_id_templates_nk_template_members_fk_put(id, nk, fk, data=data)

Update a related item by id for templateMembers.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
fk = 'fk_example' # str | Foreign key for templateMembers
data = TweakApi.TemplateMember() # TemplateMember |  (optional)

try: 
    # Update a related item by id for templateMembers.
    api_response = api_instance.teams_id_templates_nk_template_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_template_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **fk** | **str**| Foreign key for templateMembers | 
 **data** | [**TemplateMember**](TemplateMember.md)|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_get**
> list[TemplateMember] teams_id_templates_nk_template_members_get(id, nk, filter=filter)

Queries templateMembers of Template.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateMembers of Template.
    api_response = api_instance.teams_id_templates_nk_template_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_template_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TemplateMember]**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_post**
> TemplateMember teams_id_templates_nk_template_members_post(id, nk, data=data)

Creates a new instance in templateMembers of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
data = TweakApi.TemplateMember() # TemplateMember |  (optional)

try: 
    # Creates a new instance in templateMembers of this model.
    api_response = api_instance.teams_id_templates_nk_template_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_template_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **data** | [**TemplateMember**](TemplateMember.md)|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_uploader_get**
> TeamMember teams_id_templates_nk_uploader_get(id, nk, refresh=refresh)

Fetches belongsTo relation uploader.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation uploader.
    api_response = api_instance.teams_id_templates_nk_uploader_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_uploader_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_workflow_get**
> Workflow teams_id_templates_nk_workflow_get(id, nk, refresh=refresh)

Fetches belongsTo relation workflow.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation workflow.
    api_response = api_instance.teams_id_templates_nk_workflow_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_workflow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_post**
> Template teams_id_templates_post(id, data=data)

Creates a new instance in templates of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.teams_id_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_with_designs_get**
> list[Template] teams_id_templates_with_designs_get(id, id2, filter=filter)

List Templates with Designs for this Team

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
id2 = 'id_example' # str | Team id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List Templates with Designs for this Team
    api_response = api_instance.teams_id_templates_with_designs_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_with_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **id2** | **str**| Team id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_count_get**
> InlineResponse2001 teams_id_workflows_count_get(id, where=where)

Counts workflows of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts workflows of Team.
    api_response = api_instance.teams_id_workflows_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_workflows_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_delete**
> teams_id_workflows_delete(id)

Deletes all workflows of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id

try: 
    # Deletes all workflows of this model.
    api_instance.teams_id_workflows_delete(id)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_workflows_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_fk_delete**
> teams_id_workflows_fk_delete(id, fk)

Delete a related item by id for workflows.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Delete a related item by id for workflows.
    api_instance.teams_id_workflows_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_workflows_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_fk_get**
> Workflow teams_id_workflows_fk_get(id, fk)

Find a related item by id for workflows.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Find a related item by id for workflows.
    api_response = api_instance.teams_id_workflows_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_workflows_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_fk_put**
> Workflow teams_id_workflows_fk_put(id, fk, data=data)

Update a related item by id for workflows.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
fk = 'fk_example' # str | Foreign key for workflows
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Update a related item by id for workflows.
    api_response = api_instance.teams_id_workflows_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_workflows_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **fk** | **str**| Foreign key for workflows | 
 **data** | [**Workflow**](Workflow.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_get**
> list[Workflow] teams_id_workflows_get(id, filter=filter)

Queries workflows of Team.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries workflows of Team.
    api_response = api_instance.teams_id_workflows_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_workflows_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Workflow]**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_post**
> Workflow teams_id_workflows_post(id, data=data)

Creates a new instance in workflows of this model.

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
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Creates a new instance in workflows of this model.
    api_response = api_instance.teams_id_workflows_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_workflows_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **data** | [**Workflow**](Workflow.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_name_name_exists_get**
> InlineResponse2002 teams_name_name_exists_get(name)

Define whether team exists or not

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
api_instance = TweakApi.TeamApi()
name = 'name_example' # str | Team name

try: 
    # Define whether team exists or not
    api_response = api_instance.teams_name_name_exists_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_name_name_exists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Team name | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_post**
> Team teams_post(data=data)

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
api_instance = TweakApi.TeamApi()
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.teams_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_subdomain_subdomain_exists_get**
> InlineResponse2002 teams_subdomain_subdomain_exists_get(subdomain)

Define whether team exists or not

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
api_instance = TweakApi.TeamApi()
subdomain = 'subdomain_example' # str | Team subdomain

try: 
    # Define whether team exists or not
    api_response = api_instance.teams_subdomain_subdomain_exists_get(subdomain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_subdomain_subdomain_exists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**| Team subdomain | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

