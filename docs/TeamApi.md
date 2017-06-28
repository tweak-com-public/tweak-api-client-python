# TweakApi.TeamApi

All URIs are relative to *https://apistagecdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_change_stream_get**](TeamApi.md#teams_change_stream_get) | **GET** /Teams/change-stream | Create a change stream.
[**teams_change_stream_post**](TeamApi.md#teams_change_stream_post) | **POST** /Teams/change-stream | Create a change stream.
[**teams_count_get**](TeamApi.md#teams_count_get) | **GET** /Teams/count | Count instances of the model matched by where from the data source.
[**teams_find_one_get**](TeamApi.md#teams_find_one_get) | **GET** /Teams/findOne | Find first instance of the model matched by filter from the data source.
[**teams_get**](TeamApi.md#teams_get) | **GET** /Teams | Find all instances of the model matched by filter from the data source.
[**teams_id_brand_delete**](TeamApi.md#teams_id_brand_delete) | **DELETE** /Teams/{id}/brand | Deletes brand of this model.
[**teams_id_brand_get**](TeamApi.md#teams_id_brand_get) | **GET** /Teams/{id}/brand | Fetches hasOne relation brand.
[**teams_id_brand_post**](TeamApi.md#teams_id_brand_post) | **POST** /Teams/{id}/brand | Creates a new instance in brand of this model.
[**teams_id_brand_put**](TeamApi.md#teams_id_brand_put) | **PUT** /Teams/{id}/brand | Update brand of this model.
[**teams_id_delete**](TeamApi.md#teams_id_delete) | **DELETE** /Teams/{id} | Delete a model instance by {{id}} from the data source.
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
[**teams_id_image_folders_nk_children_delete**](TeamApi.md#teams_id_image_folders_nk_children_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/children | Deletes all children of this model.
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
[**teams_id_image_folders_nk_images_delete**](TeamApi.md#teams_id_image_folders_nk_images_delete) | **DELETE** /Teams/{id}/imageFolders/{nk}/images | Deletes all images of this model.
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
[**teams_id_portals_count_get**](TeamApi.md#teams_id_portals_count_get) | **GET** /Teams/{id}/portals/count | Counts portals of Team.
[**teams_id_portals_delete**](TeamApi.md#teams_id_portals_delete) | **DELETE** /Teams/{id}/portals | Deletes all portals of this model.
[**teams_id_portals_fk_delete**](TeamApi.md#teams_id_portals_fk_delete) | **DELETE** /Teams/{id}/portals/{fk} | Delete a related item by id for portals.
[**teams_id_portals_fk_get**](TeamApi.md#teams_id_portals_fk_get) | **GET** /Teams/{id}/portals/{fk} | Find a related item by id for portals.
[**teams_id_portals_fk_put**](TeamApi.md#teams_id_portals_fk_put) | **PUT** /Teams/{id}/portals/{fk} | Update a related item by id for portals.
[**teams_id_portals_get**](TeamApi.md#teams_id_portals_get) | **GET** /Teams/{id}/portals | Queries portals of Team.
[**teams_id_portals_nk_design_folders_count_get**](TeamApi.md#teams_id_portals_nk_design_folders_count_get) | **GET** /Teams/{id}/portals/{nk}/designFolders/count | Counts designFolders of Portal.
[**teams_id_portals_nk_design_folders_delete**](TeamApi.md#teams_id_portals_nk_design_folders_delete) | **DELETE** /Teams/{id}/portals/{nk}/designFolders | Deletes all designFolders of this model.
[**teams_id_portals_nk_design_folders_fk_delete**](TeamApi.md#teams_id_portals_nk_design_folders_fk_delete) | **DELETE** /Teams/{id}/portals/{nk}/designFolders/{fk} | Delete a related item by id for designFolders.
[**teams_id_portals_nk_design_folders_fk_get**](TeamApi.md#teams_id_portals_nk_design_folders_fk_get) | **GET** /Teams/{id}/portals/{nk}/designFolders/{fk} | Find a related item by id for designFolders.
[**teams_id_portals_nk_design_folders_fk_put**](TeamApi.md#teams_id_portals_nk_design_folders_fk_put) | **PUT** /Teams/{id}/portals/{nk}/designFolders/{fk} | Update a related item by id for designFolders.
[**teams_id_portals_nk_design_folders_get**](TeamApi.md#teams_id_portals_nk_design_folders_get) | **GET** /Teams/{id}/portals/{nk}/designFolders | Queries designFolders of Portal.
[**teams_id_portals_nk_design_folders_post**](TeamApi.md#teams_id_portals_nk_design_folders_post) | **POST** /Teams/{id}/portals/{nk}/designFolders | Creates a new instance in designFolders of this model.
[**teams_id_portals_nk_designs_count_get**](TeamApi.md#teams_id_portals_nk_designs_count_get) | **GET** /Teams/{id}/portals/{nk}/designs/count | Counts designs of Portal.
[**teams_id_portals_nk_designs_delete**](TeamApi.md#teams_id_portals_nk_designs_delete) | **DELETE** /Teams/{id}/portals/{nk}/designs | Deletes all designs of this model.
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
[**teams_id_put**](TeamApi.md#teams_id_put) | **PUT** /Teams/{id} | Replace attributes for a model instance and persist it into the data source.
[**teams_id_replace_post**](TeamApi.md#teams_id_replace_post) | **POST** /Teams/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**teams_id_team_members_count_get**](TeamApi.md#teams_id_team_members_count_get) | **GET** /Teams/{id}/teamMembers/count | Counts teamMembers of Team.
[**teams_id_team_members_delete**](TeamApi.md#teams_id_team_members_delete) | **DELETE** /Teams/{id}/teamMembers | Deletes all teamMembers of this model.
[**teams_id_team_members_fk_delete**](TeamApi.md#teams_id_team_members_fk_delete) | **DELETE** /Teams/{id}/teamMembers/{fk} | Delete a related item by id for teamMembers.
[**teams_id_team_members_fk_get**](TeamApi.md#teams_id_team_members_fk_get) | **GET** /Teams/{id}/teamMembers/{fk} | Find a related item by id for teamMembers.
[**teams_id_team_members_fk_put**](TeamApi.md#teams_id_team_members_fk_put) | **PUT** /Teams/{id}/teamMembers/{fk} | Update a related item by id for teamMembers.
[**teams_id_team_members_get**](TeamApi.md#teams_id_team_members_get) | **GET** /Teams/{id}/teamMembers | Queries teamMembers of Team.
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
[**teams_id_templates_nk_designs_delete**](TeamApi.md#teams_id_templates_nk_designs_delete) | **DELETE** /Teams/{id}/templates/{nk}/designs | Deletes all designs of this model.
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
[**teams_patch**](TeamApi.md#teams_patch) | **PATCH** /Teams | Patch an existing model instance or insert a new one into the data source.
[**teams_post**](TeamApi.md#teams_post) | **POST** /Teams | Create a new instance of the model and persist it into the data source.
[**teams_put**](TeamApi.md#teams_put) | **PUT** /Teams | Replace an existing model instance or insert a new one into the data source.
[**teams_replace_or_create_post**](TeamApi.md#teams_replace_or_create_post) | **POST** /Teams/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**teams_update_post**](TeamApi.md#teams_update_post) | **POST** /Teams/update | Update instances of the model matched by {{where}} from the data source.
[**teams_upsert_with_where_post**](TeamApi.md#teams_upsert_with_where_post) | **POST** /Teams/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_count_get**
> InlineResponse200 teams_count_get(where=where)

Count instances of the model matched by where from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_count_get**
> InlineResponse200 teams_id_image_folders_count_get(id, where=where)

Counts imageFolders of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_count_get**
> InlineResponse200 teams_id_image_folders_nk_children_count_get(id, nk, where=where)

Counts children of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_children_delete**
> teams_id_image_folders_nk_children_delete(id, nk)

Deletes all children of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.

try: 
    # Deletes all children of this model.
    api_instance.teams_id_image_folders_nk_children_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_children_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_folder_members_count_get**
> InlineResponse200 teams_id_image_folders_nk_folder_members_count_get(id, nk, where=where)

Counts folderMembers of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_count_get**
> InlineResponse200 teams_id_image_folders_nk_images_count_get(id, nk, where=where)

Counts images of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_images_delete**
> teams_id_image_folders_nk_images_delete(id, nk)

Deletes all images of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for imageFolders.

try: 
    # Deletes all images of this model.
    api_instance.teams_id_image_folders_nk_images_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_image_folders_nk_images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for imageFolders. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_members_count_get**
> InlineResponse200 teams_id_image_folders_nk_members_count_get(id, nk, where=where)

Counts members of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_image_folders_nk_portals_count_get**
> InlineResponse200 teams_id_image_folders_nk_portals_count_get(id, nk, where=where)

Counts portals of ImageFolder.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_images_count_get**
> InlineResponse200 teams_id_images_count_get(id, where=where)

Counts images of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_members_count_get**
> InlineResponse200 teams_id_members_count_get(id, where=where)

Counts members of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_count_get**
> InlineResponse200 teams_id_portals_count_get(id, where=where)

Counts portals of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_design_folders_count_get**
> InlineResponse200 teams_id_portals_nk_design_folders_count_get(id, nk, where=where)

Counts designFolders of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_count_get**
> InlineResponse200 teams_id_portals_nk_designs_count_get(id, nk, where=where)

Counts designs of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_designs_delete**
> teams_id_portals_nk_designs_delete(id, nk)

Deletes all designs of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for portals.

try: 
    # Deletes all designs of this model.
    api_instance.teams_id_portals_nk_designs_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_portals_nk_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for portals. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_image_folders_count_get**
> InlineResponse200 teams_id_portals_nk_image_folders_count_get(id, nk, where=where)

Counts imageFolders of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_members_count_get**
> InlineResponse200 teams_id_portals_nk_members_count_get(id, nk, where=where)

Counts members of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_portal_members_count_get**
> InlineResponse200 teams_id_portals_nk_portal_members_count_get(id, nk, where=where)

Counts portalMembers of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_folders_count_get**
> InlineResponse200 teams_id_portals_nk_template_folders_count_get(id, nk, where=where)

Counts templateFolders of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_template_rels_count_get**
> InlineResponse200 teams_id_portals_nk_template_rels_count_get(id, nk, where=where)

Counts templateRels of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_portals_nk_templates_count_get**
> InlineResponse200 teams_id_portals_nk_templates_count_get(id, nk, where=where)

Counts templates of Portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_team_members_count_get**
> InlineResponse200 teams_id_team_members_count_get(id, where=where)

Counts teamMembers of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_template_folders_count_get**
> InlineResponse200 teams_id_template_folders_count_get(id, where=where)

Counts templateFolders of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_count_get**
> InlineResponse200 teams_id_templates_count_get(id, where=where)

Counts templates of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_count_get**
> InlineResponse200 teams_id_templates_nk_designs_count_get(id, nk, where=where)

Counts designs of Template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_designs_delete**
> teams_id_templates_nk_designs_delete(id, nk)

Deletes all designs of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
id = 'id_example' # str | Team id
nk = 'nk_example' # str | Foreign key for templates.

try: 
    # Deletes all designs of this model.
    api_instance.teams_id_templates_nk_designs_delete(id, nk)
except ApiException as e:
    print("Exception when calling TeamApi->teams_id_templates_nk_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Team id | 
 **nk** | **str**| Foreign key for templates. | 

### Return type

void (empty response body)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_members_count_get**
> InlineResponse200 teams_id_templates_nk_members_count_get(id, nk, where=where)

Counts members of Template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portal_folders_count_get**
> InlineResponse200 teams_id_templates_nk_portal_folders_count_get(id, nk, where=where)

Counts portalFolders of Template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_portals_count_get**
> InlineResponse200 teams_id_templates_nk_portals_count_get(id, nk, where=where)

Counts portals of Template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_tags_count_get**
> InlineResponse200 teams_id_templates_nk_tags_count_get(id, nk, where=where)

Counts tags of Template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_templates_nk_template_members_count_get**
> InlineResponse200 teams_id_templates_nk_template_members_count_get(id, nk, where=where)

Counts templateMembers of Template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_id_workflows_count_get**
> InlineResponse200 teams_id_workflows_count_get(id, where=where)

Counts workflows of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_patch**
> Team teams_patch(data=data)

Patch an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.teams_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_put**
> Team teams_put(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.teams_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_replace_or_create_post**
> Team teams_replace_or_create_post(data=data)

Replace an existing model instance or insert a new one into the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
data = TweakApi.Team() # Team | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.teams_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Team**](Team.md)| Model instance data | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_update_post**
> InlineResponse2001 teams_update_post(where=where, data=data)

Update instances of the model matched by {{where}} from the data source.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Team() # Team | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.teams_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Team**](Team.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_upsert_with_where_post**
> Team teams_upsert_with_where_post(where=where, data=data)

Update an existing model instance or insert a new one into the data source based on the where criteria.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TweakApi.TeamApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Team() # Team | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.teams_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->teams_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Team**](Team.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

