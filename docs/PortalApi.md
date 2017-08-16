# TweakApi.PortalApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portals_change_stream_get**](PortalApi.md#portals_change_stream_get) | **GET** /Portals/change-stream | Create a change stream.
[**portals_change_stream_post**](PortalApi.md#portals_change_stream_post) | **POST** /Portals/change-stream | Create a change stream.
[**portals_count_get**](PortalApi.md#portals_count_get) | **GET** /Portals/count | Count instances of the model matched by where from the data source.
[**portals_find_one_get**](PortalApi.md#portals_find_one_get) | **GET** /Portals/findOne | Find first instance of the model matched by filter from the data source.
[**portals_get**](PortalApi.md#portals_get) | **GET** /Portals | Find all instances of the model matched by filter from the data source.
[**portals_id_delete**](PortalApi.md#portals_id_delete) | **DELETE** /Portals/{id} | Delete a model instance by {{id}} from the data source.
[**portals_id_design_folders_count_get**](PortalApi.md#portals_id_design_folders_count_get) | **GET** /Portals/{id}/designFolders/count | Counts designFolders of Portal.
[**portals_id_design_folders_delete**](PortalApi.md#portals_id_design_folders_delete) | **DELETE** /Portals/{id}/designFolders | Deletes all designFolders of this model.
[**portals_id_design_folders_fk_delete**](PortalApi.md#portals_id_design_folders_fk_delete) | **DELETE** /Portals/{id}/designFolders/{fk} | Delete a related item by id for designFolders.
[**portals_id_design_folders_fk_get**](PortalApi.md#portals_id_design_folders_fk_get) | **GET** /Portals/{id}/designFolders/{fk} | Find a related item by id for designFolders.
[**portals_id_design_folders_fk_put**](PortalApi.md#portals_id_design_folders_fk_put) | **PUT** /Portals/{id}/designFolders/{fk} | Update a related item by id for designFolders.
[**portals_id_design_folders_get**](PortalApi.md#portals_id_design_folders_get) | **GET** /Portals/{id}/designFolders | Queries designFolders of Portal.
[**portals_id_design_folders_post**](PortalApi.md#portals_id_design_folders_post) | **POST** /Portals/{id}/designFolders | Creates a new instance in designFolders of this model.
[**portals_id_designs_count_get**](PortalApi.md#portals_id_designs_count_get) | **GET** /Portals/{id}/designs/count | Counts designs of Portal.
[**portals_id_designs_delete**](PortalApi.md#portals_id_designs_delete) | **DELETE** /Portals/{id}/designs | Deletes all designs of this model.
[**portals_id_designs_fk_delete**](PortalApi.md#portals_id_designs_fk_delete) | **DELETE** /Portals/{id}/designs/{fk} | Delete a related item by id for designs.
[**portals_id_designs_fk_get**](PortalApi.md#portals_id_designs_fk_get) | **GET** /Portals/{id}/designs/{fk} | Find a related item by id for designs.
[**portals_id_designs_fk_put**](PortalApi.md#portals_id_designs_fk_put) | **PUT** /Portals/{id}/designs/{fk} | Update a related item by id for designs.
[**portals_id_designs_get**](PortalApi.md#portals_id_designs_get) | **GET** /Portals/{id}/designs | Queries designs of Portal.
[**portals_id_designs_nk_assignee_get**](PortalApi.md#portals_id_designs_nk_assignee_get) | **GET** /Portals/{id}/designs/{nk}/assignee | Fetches belongsTo relation assignee.
[**portals_id_designs_nk_commenters_count_get**](PortalApi.md#portals_id_designs_nk_commenters_count_get) | **GET** /Portals/{id}/designs/{nk}/commenters/count | Counts commenters of Design.
[**portals_id_designs_nk_commenters_delete**](PortalApi.md#portals_id_designs_nk_commenters_delete) | **DELETE** /Portals/{id}/designs/{nk}/commenters | Deletes all commenters of this model.
[**portals_id_designs_nk_commenters_fk_delete**](PortalApi.md#portals_id_designs_nk_commenters_fk_delete) | **DELETE** /Portals/{id}/designs/{nk}/commenters/{fk} | Delete a related item by id for commenters.
[**portals_id_designs_nk_commenters_fk_get**](PortalApi.md#portals_id_designs_nk_commenters_fk_get) | **GET** /Portals/{id}/designs/{nk}/commenters/{fk} | Find a related item by id for commenters.
[**portals_id_designs_nk_commenters_fk_put**](PortalApi.md#portals_id_designs_nk_commenters_fk_put) | **PUT** /Portals/{id}/designs/{nk}/commenters/{fk} | Update a related item by id for commenters.
[**portals_id_designs_nk_commenters_get**](PortalApi.md#portals_id_designs_nk_commenters_get) | **GET** /Portals/{id}/designs/{nk}/commenters | Queries commenters of Design.
[**portals_id_designs_nk_commenters_post**](PortalApi.md#portals_id_designs_nk_commenters_post) | **POST** /Portals/{id}/designs/{nk}/commenters | Creates a new instance in commenters of this model.
[**portals_id_designs_nk_commenters_rel_fk_delete**](PortalApi.md#portals_id_designs_nk_commenters_rel_fk_delete) | **DELETE** /Portals/{id}/designs/{nk}/commenters/rel/{fk} | Remove the commenters relation to an item by id.
[**portals_id_designs_nk_commenters_rel_fk_head**](PortalApi.md#portals_id_designs_nk_commenters_rel_fk_head) | **HEAD** /Portals/{id}/designs/{nk}/commenters/rel/{fk} | Check the existence of commenters relation to an item by id.
[**portals_id_designs_nk_commenters_rel_fk_put**](PortalApi.md#portals_id_designs_nk_commenters_rel_fk_put) | **PUT** /Portals/{id}/designs/{nk}/commenters/rel/{fk} | Add a related item by id for commenters.
[**portals_id_designs_nk_comments_count_get**](PortalApi.md#portals_id_designs_nk_comments_count_get) | **GET** /Portals/{id}/designs/{nk}/comments/count | Counts comments of Design.
[**portals_id_designs_nk_comments_delete**](PortalApi.md#portals_id_designs_nk_comments_delete) | **DELETE** /Portals/{id}/designs/{nk}/comments | Deletes all comments of this model.
[**portals_id_designs_nk_comments_fk_delete**](PortalApi.md#portals_id_designs_nk_comments_fk_delete) | **DELETE** /Portals/{id}/designs/{nk}/comments/{fk} | Delete a related item by id for comments.
[**portals_id_designs_nk_comments_fk_get**](PortalApi.md#portals_id_designs_nk_comments_fk_get) | **GET** /Portals/{id}/designs/{nk}/comments/{fk} | Find a related item by id for comments.
[**portals_id_designs_nk_comments_fk_put**](PortalApi.md#portals_id_designs_nk_comments_fk_put) | **PUT** /Portals/{id}/designs/{nk}/comments/{fk} | Update a related item by id for comments.
[**portals_id_designs_nk_comments_get**](PortalApi.md#portals_id_designs_nk_comments_get) | **GET** /Portals/{id}/designs/{nk}/comments | Queries comments of Design.
[**portals_id_designs_nk_comments_post**](PortalApi.md#portals_id_designs_nk_comments_post) | **POST** /Portals/{id}/designs/{nk}/comments | Creates a new instance in comments of this model.
[**portals_id_designs_nk_customer_get**](PortalApi.md#portals_id_designs_nk_customer_get) | **GET** /Portals/{id}/designs/{nk}/customer | Fetches belongsTo relation customer.
[**portals_id_designs_nk_exports_count_get**](PortalApi.md#portals_id_designs_nk_exports_count_get) | **GET** /Portals/{id}/designs/{nk}/exports/count | Counts exports of Design.
[**portals_id_designs_nk_exports_delete**](PortalApi.md#portals_id_designs_nk_exports_delete) | **DELETE** /Portals/{id}/designs/{nk}/exports | Deletes all exports of this model.
[**portals_id_designs_nk_exports_fk_delete**](PortalApi.md#portals_id_designs_nk_exports_fk_delete) | **DELETE** /Portals/{id}/designs/{nk}/exports/{fk} | Delete a related item by id for exports.
[**portals_id_designs_nk_exports_fk_get**](PortalApi.md#portals_id_designs_nk_exports_fk_get) | **GET** /Portals/{id}/designs/{nk}/exports/{fk} | Find a related item by id for exports.
[**portals_id_designs_nk_exports_fk_put**](PortalApi.md#portals_id_designs_nk_exports_fk_put) | **PUT** /Portals/{id}/designs/{nk}/exports/{fk} | Update a related item by id for exports.
[**portals_id_designs_nk_exports_get**](PortalApi.md#portals_id_designs_nk_exports_get) | **GET** /Portals/{id}/designs/{nk}/exports | Queries exports of Design.
[**portals_id_designs_nk_exports_post**](PortalApi.md#portals_id_designs_nk_exports_post) | **POST** /Portals/{id}/designs/{nk}/exports | Creates a new instance in exports of this model.
[**portals_id_designs_nk_folder_get**](PortalApi.md#portals_id_designs_nk_folder_get) | **GET** /Portals/{id}/designs/{nk}/folder | Fetches belongsTo relation folder.
[**portals_id_designs_nk_permission_delete**](PortalApi.md#portals_id_designs_nk_permission_delete) | **DELETE** /Portals/{id}/designs/{nk}/permission | Deletes permission of this model.
[**portals_id_designs_nk_permission_get**](PortalApi.md#portals_id_designs_nk_permission_get) | **GET** /Portals/{id}/designs/{nk}/permission | Fetches hasOne relation permission.
[**portals_id_designs_nk_permission_post**](PortalApi.md#portals_id_designs_nk_permission_post) | **POST** /Portals/{id}/designs/{nk}/permission | Creates a new instance in permission of this model.
[**portals_id_designs_nk_permission_put**](PortalApi.md#portals_id_designs_nk_permission_put) | **PUT** /Portals/{id}/designs/{nk}/permission | Update permission of this model.
[**portals_id_designs_nk_portal_get**](PortalApi.md#portals_id_designs_nk_portal_get) | **GET** /Portals/{id}/designs/{nk}/portal | Fetches belongsTo relation portal.
[**portals_id_designs_nk_rejection_comment_get**](PortalApi.md#portals_id_designs_nk_rejection_comment_get) | **GET** /Portals/{id}/designs/{nk}/rejectionComment | Fetches belongsTo relation rejectionComment.
[**portals_id_designs_nk_requester_get**](PortalApi.md#portals_id_designs_nk_requester_get) | **GET** /Portals/{id}/designs/{nk}/requester | Fetches belongsTo relation requester.
[**portals_id_designs_nk_reviewer_get**](PortalApi.md#portals_id_designs_nk_reviewer_get) | **GET** /Portals/{id}/designs/{nk}/reviewer | Fetches belongsTo relation reviewer.
[**portals_id_designs_nk_tags_count_get**](PortalApi.md#portals_id_designs_nk_tags_count_get) | **GET** /Portals/{id}/designs/{nk}/tags/count | Counts tags of Design.
[**portals_id_designs_nk_tags_delete**](PortalApi.md#portals_id_designs_nk_tags_delete) | **DELETE** /Portals/{id}/designs/{nk}/tags | Deletes all tags of this model.
[**portals_id_designs_nk_tags_fk_delete**](PortalApi.md#portals_id_designs_nk_tags_fk_delete) | **DELETE** /Portals/{id}/designs/{nk}/tags/{fk} | Delete a related item by id for tags.
[**portals_id_designs_nk_tags_fk_get**](PortalApi.md#portals_id_designs_nk_tags_fk_get) | **GET** /Portals/{id}/designs/{nk}/tags/{fk} | Find a related item by id for tags.
[**portals_id_designs_nk_tags_fk_put**](PortalApi.md#portals_id_designs_nk_tags_fk_put) | **PUT** /Portals/{id}/designs/{nk}/tags/{fk} | Update a related item by id for tags.
[**portals_id_designs_nk_tags_get**](PortalApi.md#portals_id_designs_nk_tags_get) | **GET** /Portals/{id}/designs/{nk}/tags | Queries tags of Design.
[**portals_id_designs_nk_tags_post**](PortalApi.md#portals_id_designs_nk_tags_post) | **POST** /Portals/{id}/designs/{nk}/tags | Creates a new instance in tags of this model.
[**portals_id_designs_nk_tags_rel_fk_delete**](PortalApi.md#portals_id_designs_nk_tags_rel_fk_delete) | **DELETE** /Portals/{id}/designs/{nk}/tags/rel/{fk} | Remove the tags relation to an item by id.
[**portals_id_designs_nk_tags_rel_fk_head**](PortalApi.md#portals_id_designs_nk_tags_rel_fk_head) | **HEAD** /Portals/{id}/designs/{nk}/tags/rel/{fk} | Check the existence of tags relation to an item by id.
[**portals_id_designs_nk_tags_rel_fk_put**](PortalApi.md#portals_id_designs_nk_tags_rel_fk_put) | **PUT** /Portals/{id}/designs/{nk}/tags/rel/{fk} | Add a related item by id for tags.
[**portals_id_designs_nk_template_get**](PortalApi.md#portals_id_designs_nk_template_get) | **GET** /Portals/{id}/designs/{nk}/template | Fetches belongsTo relation template.
[**portals_id_designs_post**](PortalApi.md#portals_id_designs_post) | **POST** /Portals/{id}/designs | Creates a new instance in designs of this model.
[**portals_id_exists_get**](PortalApi.md#portals_id_exists_get) | **GET** /Portals/{id}/exists | Check whether a model instance exists in the data source.
[**portals_id_get**](PortalApi.md#portals_id_get) | **GET** /Portals/{id} | Find a model instance by {{id}} from the data source.
[**portals_id_head**](PortalApi.md#portals_id_head) | **HEAD** /Portals/{id} | Check whether a model instance exists in the data source.
[**portals_id_image_folders_count_get**](PortalApi.md#portals_id_image_folders_count_get) | **GET** /Portals/{id}/imageFolders/count | Counts imageFolders of Portal.
[**portals_id_image_folders_delete**](PortalApi.md#portals_id_image_folders_delete) | **DELETE** /Portals/{id}/imageFolders | Deletes all imageFolders of this model.
[**portals_id_image_folders_fk_delete**](PortalApi.md#portals_id_image_folders_fk_delete) | **DELETE** /Portals/{id}/imageFolders/{fk} | Delete a related item by id for imageFolders.
[**portals_id_image_folders_fk_get**](PortalApi.md#portals_id_image_folders_fk_get) | **GET** /Portals/{id}/imageFolders/{fk} | Find a related item by id for imageFolders.
[**portals_id_image_folders_fk_put**](PortalApi.md#portals_id_image_folders_fk_put) | **PUT** /Portals/{id}/imageFolders/{fk} | Update a related item by id for imageFolders.
[**portals_id_image_folders_get**](PortalApi.md#portals_id_image_folders_get) | **GET** /Portals/{id}/imageFolders | Queries imageFolders of Portal.
[**portals_id_image_folders_post**](PortalApi.md#portals_id_image_folders_post) | **POST** /Portals/{id}/imageFolders | Creates a new instance in imageFolders of this model.
[**portals_id_image_folders_rel_fk_delete**](PortalApi.md#portals_id_image_folders_rel_fk_delete) | **DELETE** /Portals/{id}/imageFolders/rel/{fk} | Remove the imageFolders relation to an item by id.
[**portals_id_image_folders_rel_fk_head**](PortalApi.md#portals_id_image_folders_rel_fk_head) | **HEAD** /Portals/{id}/imageFolders/rel/{fk} | Check the existence of imageFolders relation to an item by id.
[**portals_id_image_folders_rel_fk_put**](PortalApi.md#portals_id_image_folders_rel_fk_put) | **PUT** /Portals/{id}/imageFolders/rel/{fk} | Add a related item by id for imageFolders.
[**portals_id_invitation_tickets_fk_delete**](PortalApi.md#portals_id_invitation_tickets_fk_delete) | **DELETE** /Portals/{id}/invitationTickets/{fk} | Delete InvitationTickets for this Portal
[**portals_id_invitation_tickets_fk_get**](PortalApi.md#portals_id_invitation_tickets_fk_get) | **GET** /Portals/{id}/invitationTickets/{fk} | Get InvitationTicket by Id for this Portal
[**portals_id_invitation_tickets_get**](PortalApi.md#portals_id_invitation_tickets_get) | **GET** /Portals/{id}/invitationTickets | List InvitationTickets for this Portal
[**portals_id_logo_put**](PortalApi.md#portals_id_logo_put) | **PUT** /Portals/{id}/logo | Change logo
[**portals_id_members_count_get**](PortalApi.md#portals_id_members_count_get) | **GET** /Portals/{id}/members/count | Counts members of Portal.
[**portals_id_members_delete**](PortalApi.md#portals_id_members_delete) | **DELETE** /Portals/{id}/members | Deletes all members of this model.
[**portals_id_members_fk_delete**](PortalApi.md#portals_id_members_fk_delete) | **DELETE** /Portals/{id}/members/{fk} | Delete a related item by id for members.
[**portals_id_members_fk_get**](PortalApi.md#portals_id_members_fk_get) | **GET** /Portals/{id}/members/{fk} | Find a related item by id for members.
[**portals_id_members_fk_put**](PortalApi.md#portals_id_members_fk_put) | **PUT** /Portals/{id}/members/{fk} | Update a related item by id for members.
[**portals_id_members_get**](PortalApi.md#portals_id_members_get) | **GET** /Portals/{id}/members | Queries members of Portal.
[**portals_id_members_post**](PortalApi.md#portals_id_members_post) | **POST** /Portals/{id}/members | Creates a new instance in members of this model.
[**portals_id_members_rel_fk_delete**](PortalApi.md#portals_id_members_rel_fk_delete) | **DELETE** /Portals/{id}/members/rel/{fk} | Remove the members relation to an item by id.
[**portals_id_members_rel_fk_head**](PortalApi.md#portals_id_members_rel_fk_head) | **HEAD** /Portals/{id}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**portals_id_members_rel_fk_put**](PortalApi.md#portals_id_members_rel_fk_put) | **PUT** /Portals/{id}/members/rel/{fk} | Add a related item by id for members.
[**portals_id_patch**](PortalApi.md#portals_id_patch) | **PATCH** /Portals/{id} | Patch attributes for a model instance and persist it into the data source.
[**portals_id_permission_delete**](PortalApi.md#portals_id_permission_delete) | **DELETE** /Portals/{id}/permission | Deletes permission of this model.
[**portals_id_permission_get**](PortalApi.md#portals_id_permission_get) | **GET** /Portals/{id}/permission | Fetches hasOne relation permission.
[**portals_id_permission_post**](PortalApi.md#portals_id_permission_post) | **POST** /Portals/{id}/permission | Creates a new instance in permission of this model.
[**portals_id_permission_put**](PortalApi.md#portals_id_permission_put) | **PUT** /Portals/{id}/permission | Update permission of this model.
[**portals_id_portal_members_count_get**](PortalApi.md#portals_id_portal_members_count_get) | **GET** /Portals/{id}/portalMembers/count | Counts portalMembers of Portal.
[**portals_id_portal_members_delete**](PortalApi.md#portals_id_portal_members_delete) | **DELETE** /Portals/{id}/portalMembers | Deletes all portalMembers of this model.
[**portals_id_portal_members_fk_delete**](PortalApi.md#portals_id_portal_members_fk_delete) | **DELETE** /Portals/{id}/portalMembers/{fk} | Delete a related item by id for portalMembers.
[**portals_id_portal_members_fk_get**](PortalApi.md#portals_id_portal_members_fk_get) | **GET** /Portals/{id}/portalMembers/{fk} | Find a related item by id for portalMembers.
[**portals_id_portal_members_fk_put**](PortalApi.md#portals_id_portal_members_fk_put) | **PUT** /Portals/{id}/portalMembers/{fk} | Update a related item by id for portalMembers.
[**portals_id_portal_members_get**](PortalApi.md#portals_id_portal_members_get) | **GET** /Portals/{id}/portalMembers | Queries portalMembers of Portal.
[**portals_id_portal_members_post**](PortalApi.md#portals_id_portal_members_post) | **POST** /Portals/{id}/portalMembers | Creates a new instance in portalMembers of this model.
[**portals_id_put**](PortalApi.md#portals_id_put) | **PUT** /Portals/{id} | Replace attributes for a model instance and persist it into the data source.
[**portals_id_replace_post**](PortalApi.md#portals_id_replace_post) | **POST** /Portals/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**portals_id_team_get**](PortalApi.md#portals_id_team_get) | **GET** /Portals/{id}/team | Fetches belongsTo relation team.
[**portals_id_template_folders_count_get**](PortalApi.md#portals_id_template_folders_count_get) | **GET** /Portals/{id}/templateFolders/count | Counts templateFolders of Portal.
[**portals_id_template_folders_delete**](PortalApi.md#portals_id_template_folders_delete) | **DELETE** /Portals/{id}/templateFolders | Deletes all templateFolders of this model.
[**portals_id_template_folders_fk_delete**](PortalApi.md#portals_id_template_folders_fk_delete) | **DELETE** /Portals/{id}/templateFolders/{fk} | Delete a related item by id for templateFolders.
[**portals_id_template_folders_fk_get**](PortalApi.md#portals_id_template_folders_fk_get) | **GET** /Portals/{id}/templateFolders/{fk} | Find a related item by id for templateFolders.
[**portals_id_template_folders_fk_put**](PortalApi.md#portals_id_template_folders_fk_put) | **PUT** /Portals/{id}/templateFolders/{fk} | Update a related item by id for templateFolders.
[**portals_id_template_folders_get**](PortalApi.md#portals_id_template_folders_get) | **GET** /Portals/{id}/templateFolders | Queries templateFolders of Portal.
[**portals_id_template_folders_nk_templates_fk_rel_delete**](PortalApi.md#portals_id_template_folders_nk_templates_fk_rel_delete) | **DELETE** /Portals/{id}/templateFolders/{nk}/templates/{fk}/rel | Unlink folder with Template and Portal
[**portals_id_template_folders_nk_templates_fk_rel_put**](PortalApi.md#portals_id_template_folders_nk_templates_fk_rel_put) | **PUT** /Portals/{id}/templateFolders/{nk}/templates/{fk}/rel | Link folder with Template and Portal
[**portals_id_template_folders_post**](PortalApi.md#portals_id_template_folders_post) | **POST** /Portals/{id}/templateFolders | Creates a new instance in templateFolders of this model.
[**portals_id_template_folders_root_templates_get**](PortalApi.md#portals_id_template_folders_root_templates_get) | **GET** /Portals/{id}/templateFolders/root/templates | List templates on root folder
[**portals_id_template_rels_count_get**](PortalApi.md#portals_id_template_rels_count_get) | **GET** /Portals/{id}/templateRels/count | Counts templateRels of Portal.
[**portals_id_template_rels_delete**](PortalApi.md#portals_id_template_rels_delete) | **DELETE** /Portals/{id}/templateRels | Deletes all templateRels of this model.
[**portals_id_template_rels_fk_delete**](PortalApi.md#portals_id_template_rels_fk_delete) | **DELETE** /Portals/{id}/templateRels/{fk} | Delete a related item by id for templateRels.
[**portals_id_template_rels_fk_get**](PortalApi.md#portals_id_template_rels_fk_get) | **GET** /Portals/{id}/templateRels/{fk} | Find a related item by id for templateRels.
[**portals_id_template_rels_fk_put**](PortalApi.md#portals_id_template_rels_fk_put) | **PUT** /Portals/{id}/templateRels/{fk} | Update a related item by id for templateRels.
[**portals_id_template_rels_get**](PortalApi.md#portals_id_template_rels_get) | **GET** /Portals/{id}/templateRels | Queries templateRels of Portal.
[**portals_id_template_rels_post**](PortalApi.md#portals_id_template_rels_post) | **POST** /Portals/{id}/templateRels | Creates a new instance in templateRels of this model.
[**portals_id_templates_count_get**](PortalApi.md#portals_id_templates_count_get) | **GET** /Portals/{id}/templates/count | Counts templates of Portal.
[**portals_id_templates_delete**](PortalApi.md#portals_id_templates_delete) | **DELETE** /Portals/{id}/templates | Deletes all templates of this model.
[**portals_id_templates_fk_delete**](PortalApi.md#portals_id_templates_fk_delete) | **DELETE** /Portals/{id}/templates/{fk} | Delete a related item by id for templates.
[**portals_id_templates_fk_designs_generate_bulk_post**](PortalApi.md#portals_id_templates_fk_designs_generate_bulk_post) | **POST** /Portals/{id}/templates/{fk}/designs/generate/bulk | Generate Design from Template
[**portals_id_templates_fk_designs_generate_post**](PortalApi.md#portals_id_templates_fk_designs_generate_post) | **POST** /Portals/{id}/templates/{fk}/designs/generate | Generate Design from Template
[**portals_id_templates_fk_get**](PortalApi.md#portals_id_templates_fk_get) | **GET** /Portals/{id}/templates/{fk} | Find a related item by id for templates.
[**portals_id_templates_fk_put**](PortalApi.md#portals_id_templates_fk_put) | **PUT** /Portals/{id}/templates/{fk} | Update a related item by id for templates.
[**portals_id_templates_get**](PortalApi.md#portals_id_templates_get) | **GET** /Portals/{id}/templates | Queries templates of Portal.
[**portals_id_templates_post**](PortalApi.md#portals_id_templates_post) | **POST** /Portals/{id}/templates | Creates a new instance in templates of this model.
[**portals_id_templates_rel_fk_delete**](PortalApi.md#portals_id_templates_rel_fk_delete) | **DELETE** /Portals/{id}/templates/rel/{fk} | Remove the templates relation to an item by id.
[**portals_id_templates_rel_fk_head**](PortalApi.md#portals_id_templates_rel_fk_head) | **HEAD** /Portals/{id}/templates/rel/{fk} | Check the existence of templates relation to an item by id.
[**portals_id_templates_rel_fk_put**](PortalApi.md#portals_id_templates_rel_fk_put) | **PUT** /Portals/{id}/templates/rel/{fk} | Add a related item by id for templates.
[**portals_patch**](PortalApi.md#portals_patch) | **PATCH** /Portals | Patch an existing model instance or insert a new one into the data source.
[**portals_post**](PortalApi.md#portals_post) | **POST** /Portals | Create a new instance of the model and persist it into the data source.
[**portals_put**](PortalApi.md#portals_put) | **PUT** /Portals | Replace an existing model instance or insert a new one into the data source.
[**portals_replace_or_create_post**](PortalApi.md#portals_replace_or_create_post) | **POST** /Portals/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**portals_update_post**](PortalApi.md#portals_update_post) | **POST** /Portals/update | Update instances of the model matched by {{where}} from the data source.
[**portals_upsert_with_where_post**](PortalApi.md#portals_upsert_with_where_post) | **POST** /Portals/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **portals_change_stream_get**
> file portals_change_stream_get(options=options)

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
api_instance = TweakApi.PortalApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portals_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_change_stream_get: %s\n" % e)
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

# **portals_change_stream_post**
> file portals_change_stream_post(options=options)

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
api_instance = TweakApi.PortalApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.portals_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_change_stream_post: %s\n" % e)
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

# **portals_count_get**
> InlineResponse200 portals_count_get(where=where)

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
api_instance = TweakApi.PortalApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.portals_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_find_one_get**
> Portal portals_find_one_get(filter=filter)

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
api_instance = TweakApi.PortalApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.portals_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_get**
> list[Portal] portals_get(filter=filter)

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
api_instance = TweakApi.PortalApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.portals_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_delete**
> object portals_id_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.portals_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_delete: %s\n" % e)
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

# **portals_id_design_folders_count_get**
> InlineResponse200 portals_id_design_folders_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designFolders of Portal.
    api_response = api_instance.portals_id_design_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_design_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_design_folders_delete**
> portals_id_design_folders_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all designFolders of this model.
    api_instance.portals_id_design_folders_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_design_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_design_folders_fk_delete**
> portals_id_design_folders_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for designFolders

try: 
    # Delete a related item by id for designFolders.
    api_instance.portals_id_design_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_design_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for designFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_design_folders_fk_get**
> DesignFolder portals_id_design_folders_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for designFolders

try: 
    # Find a related item by id for designFolders.
    api_response = api_instance.portals_id_design_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_design_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for designFolders | 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_design_folders_fk_put**
> DesignFolder portals_id_design_folders_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for designFolders
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Update a related item by id for designFolders.
    api_response = api_instance.portals_id_design_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_design_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_design_folders_get**
> list[DesignFolder] portals_id_design_folders_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designFolders of Portal.
    api_response = api_instance.portals_id_design_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_design_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignFolder]**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_design_folders_post**
> DesignFolder portals_id_design_folders_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Creates a new instance in designFolders of this model.
    api_response = api_instance.portals_id_design_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_design_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**DesignFolder**](DesignFolder.md)|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_count_get**
> InlineResponse200 portals_id_designs_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of Portal.
    api_response = api_instance.portals_id_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_delete**
> portals_id_designs_delete(id)

Deletes all designs of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all designs of this model.
    api_instance.portals_id_designs_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_fk_delete**
> portals_id_designs_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.portals_id_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_fk_get**
> Design portals_id_designs_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.portals_id_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_fk_put**
> Design portals_id_designs_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.portals_id_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_designs_get**
> list[Design] portals_id_designs_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of Portal.
    api_response = api_instance.portals_id_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_assignee_get**
> TeamMember portals_id_designs_nk_assignee_get(id, nk, refresh=refresh)

Fetches belongsTo relation assignee.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation assignee.
    api_response = api_instance.portals_id_designs_nk_assignee_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_assignee_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_count_get**
> InlineResponse200 portals_id_designs_nk_commenters_count_get(id, nk, where=where)

Counts commenters of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts commenters of Design.
    api_response = api_instance.portals_id_designs_nk_commenters_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_delete**
> portals_id_designs_nk_commenters_delete(id, nk)

Deletes all commenters of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.

try: 
    # Deletes all commenters of this model.
    api_instance.portals_id_designs_nk_commenters_delete(id, nk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_fk_delete**
> portals_id_designs_nk_commenters_fk_delete(id, nk, fk)

Delete a related item by id for commenters.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Delete a related item by id for commenters.
    api_instance.portals_id_designs_nk_commenters_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_fk_get**
> TeamMember portals_id_designs_nk_commenters_fk_get(id, nk, fk)

Find a related item by id for commenters.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Find a related item by id for commenters.
    api_response = api_instance.portals_id_designs_nk_commenters_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_fk_put**
> TeamMember portals_id_designs_nk_commenters_fk_put(id, nk, fk, data=data)

Update a related item by id for commenters.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for commenters
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for commenters.
    api_response = api_instance.portals_id_designs_nk_commenters_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for commenters | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_get**
> list[TeamMember] portals_id_designs_nk_commenters_get(id, nk, filter=filter)

Queries commenters of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries commenters of Design.
    api_response = api_instance.portals_id_designs_nk_commenters_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_post**
> TeamMember portals_id_designs_nk_commenters_post(id, nk, data=data)

Creates a new instance in commenters of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in commenters of this model.
    api_response = api_instance.portals_id_designs_nk_commenters_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_rel_fk_delete**
> portals_id_designs_nk_commenters_rel_fk_delete(id, nk, fk)

Remove the commenters relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Remove the commenters relation to an item by id.
    api_instance.portals_id_designs_nk_commenters_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_rel_fk_head**
> bool portals_id_designs_nk_commenters_rel_fk_head(id, nk, fk)

Check the existence of commenters relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for commenters

try: 
    # Check the existence of commenters relation to an item by id.
    api_response = api_instance.portals_id_designs_nk_commenters_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for commenters | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_commenters_rel_fk_put**
> DesignComment portals_id_designs_nk_commenters_rel_fk_put(id, nk, fk, data=data)

Add a related item by id for commenters.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for commenters
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Add a related item by id for commenters.
    api_response = api_instance.portals_id_designs_nk_commenters_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_commenters_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for commenters | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_comments_count_get**
> InlineResponse200 portals_id_designs_nk_comments_count_get(id, nk, where=where)

Counts comments of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts comments of Design.
    api_response = api_instance.portals_id_designs_nk_comments_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_comments_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_comments_delete**
> portals_id_designs_nk_comments_delete(id, nk)

Deletes all comments of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.

try: 
    # Deletes all comments of this model.
    api_instance.portals_id_designs_nk_comments_delete(id, nk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_comments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_comments_fk_delete**
> portals_id_designs_nk_comments_fk_delete(id, nk, fk)

Delete a related item by id for comments.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for comments

try: 
    # Delete a related item by id for comments.
    api_instance.portals_id_designs_nk_comments_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_comments_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for comments | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_comments_fk_get**
> DesignComment portals_id_designs_nk_comments_fk_get(id, nk, fk)

Find a related item by id for comments.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for comments

try: 
    # Find a related item by id for comments.
    api_response = api_instance.portals_id_designs_nk_comments_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_comments_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for comments | 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_comments_fk_put**
> DesignComment portals_id_designs_nk_comments_fk_put(id, nk, fk, data=data)

Update a related item by id for comments.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for comments
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Update a related item by id for comments.
    api_response = api_instance.portals_id_designs_nk_comments_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_comments_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for comments | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_comments_get**
> list[DesignComment] portals_id_designs_nk_comments_get(id, nk, filter=filter)

Queries comments of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries comments of Design.
    api_response = api_instance.portals_id_designs_nk_comments_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignComment]**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_comments_post**
> DesignComment portals_id_designs_nk_comments_post(id, nk, data=data)

Creates a new instance in comments of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Creates a new instance in comments of this model.
    api_response = api_instance.portals_id_designs_nk_comments_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_customer_get**
> Customer portals_id_designs_nk_customer_get(id, nk, refresh=refresh)

Fetches belongsTo relation customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation customer.
    api_response = api_instance.portals_id_designs_nk_customer_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_customer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_exports_count_get**
> InlineResponse200 portals_id_designs_nk_exports_count_get(id, nk, where=where)

Counts exports of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts exports of Design.
    api_response = api_instance.portals_id_designs_nk_exports_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_exports_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_exports_delete**
> portals_id_designs_nk_exports_delete(id, nk)

Deletes all exports of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.

try: 
    # Deletes all exports of this model.
    api_instance.portals_id_designs_nk_exports_delete(id, nk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_exports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_exports_fk_delete**
> portals_id_designs_nk_exports_fk_delete(id, nk, fk)

Delete a related item by id for exports.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for exports

try: 
    # Delete a related item by id for exports.
    api_instance.portals_id_designs_nk_exports_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_exports_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for exports | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_exports_fk_get**
> DesignExport portals_id_designs_nk_exports_fk_get(id, nk, fk)

Find a related item by id for exports.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for exports

try: 
    # Find a related item by id for exports.
    api_response = api_instance.portals_id_designs_nk_exports_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_exports_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for exports | 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_exports_fk_put**
> DesignExport portals_id_designs_nk_exports_fk_put(id, nk, fk, data=data)

Update a related item by id for exports.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for exports
data = TweakApi.DesignExport() # DesignExport |  (optional)

try: 
    # Update a related item by id for exports.
    api_response = api_instance.portals_id_designs_nk_exports_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_exports_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for exports | 
 **data** | [**DesignExport**](DesignExport.md)|  | [optional] 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_exports_get**
> list[DesignExport] portals_id_designs_nk_exports_get(id, nk, filter=filter)

Queries exports of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries exports of Design.
    api_response = api_instance.portals_id_designs_nk_exports_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_exports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignExport]**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_exports_post**
> DesignExport portals_id_designs_nk_exports_post(id, nk, data=data)

Creates a new instance in exports of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
data = TweakApi.DesignExport() # DesignExport |  (optional)

try: 
    # Creates a new instance in exports of this model.
    api_response = api_instance.portals_id_designs_nk_exports_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_exports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **data** | [**DesignExport**](DesignExport.md)|  | [optional] 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_folder_get**
> DesignFolder portals_id_designs_nk_folder_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation folder.
    api_response = api_instance.portals_id_designs_nk_folder_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_folder_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_permission_delete**
> portals_id_designs_nk_permission_delete(id, nk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.

try: 
    # Deletes permission of this model.
    api_instance.portals_id_designs_nk_permission_delete(id, nk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_permission_get**
> DesignPermissionSet portals_id_designs_nk_permission_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.portals_id_designs_nk_permission_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_permission_post**
> DesignPermissionSet portals_id_designs_nk_permission_post(id, nk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
data = TweakApi.DesignPermissionSet() # DesignPermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.portals_id_designs_nk_permission_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)|  | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_permission_put**
> DesignPermissionSet portals_id_designs_nk_permission_put(id, nk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
data = TweakApi.DesignPermissionSet() # DesignPermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.portals_id_designs_nk_permission_put(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **data** | [**DesignPermissionSet**](DesignPermissionSet.md)|  | [optional] 

### Return type

[**DesignPermissionSet**](DesignPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_portal_get**
> Portal portals_id_designs_nk_portal_get(id, nk, refresh=refresh)

Fetches belongsTo relation portal.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation portal.
    api_response = api_instance.portals_id_designs_nk_portal_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_portal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_rejection_comment_get**
> DesignComment portals_id_designs_nk_rejection_comment_get(id, nk, refresh=refresh)

Fetches belongsTo relation rejectionComment.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation rejectionComment.
    api_response = api_instance.portals_id_designs_nk_rejection_comment_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_rejection_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_requester_get**
> TeamMember portals_id_designs_nk_requester_get(id, nk, refresh=refresh)

Fetches belongsTo relation requester.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation requester.
    api_response = api_instance.portals_id_designs_nk_requester_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_requester_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_reviewer_get**
> TeamMember portals_id_designs_nk_reviewer_get(id, nk, refresh=refresh)

Fetches belongsTo relation reviewer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation reviewer.
    api_response = api_instance.portals_id_designs_nk_reviewer_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_reviewer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_count_get**
> InlineResponse200 portals_id_designs_nk_tags_count_get(id, nk, where=where)

Counts tags of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts tags of Design.
    api_response = api_instance.portals_id_designs_nk_tags_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_delete**
> portals_id_designs_nk_tags_delete(id, nk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.

try: 
    # Deletes all tags of this model.
    api_instance.portals_id_designs_nk_tags_delete(id, nk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_fk_delete**
> portals_id_designs_nk_tags_fk_delete(id, nk, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Delete a related item by id for tags.
    api_instance.portals_id_designs_nk_tags_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_fk_get**
> Tag portals_id_designs_nk_tags_fk_get(id, nk, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Find a related item by id for tags.
    api_response = api_instance.portals_id_designs_nk_tags_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_fk_put**
> Tag portals_id_designs_nk_tags_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Update a related item by id for tags.
    api_response = api_instance.portals_id_designs_nk_tags_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
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

# **portals_id_designs_nk_tags_get**
> list[Tag] portals_id_designs_nk_tags_get(id, nk, filter=filter)

Queries tags of Design.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries tags of Design.
    api_response = api_instance.portals_id_designs_nk_tags_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_post**
> Tag portals_id_designs_nk_tags_post(id, nk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
data = TweakApi.Tag() # Tag |  (optional)

try: 
    # Creates a new instance in tags of this model.
    api_response = api_instance.portals_id_designs_nk_tags_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **data** | [**Tag**](Tag.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_rel_fk_delete**
> portals_id_designs_nk_tags_rel_fk_delete(id, nk, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Remove the tags relation to an item by id.
    api_instance.portals_id_designs_nk_tags_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_rel_fk_head**
> bool portals_id_designs_nk_tags_rel_fk_head(id, nk, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for tags

try: 
    # Check the existence of tags relation to an item by id.
    api_response = api_instance.portals_id_designs_nk_tags_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for tags | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_tags_rel_fk_put**
> DesignTag portals_id_designs_nk_tags_rel_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
fk = 'fk_example' # str | Foreign key for tags
data = TweakApi.DesignTag() # DesignTag |  (optional)

try: 
    # Add a related item by id for tags.
    api_response = api_instance.portals_id_designs_nk_tags_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_tags_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **fk** | **str**| Foreign key for tags | 
 **data** | [**DesignTag**](DesignTag.md)|  | [optional] 

### Return type

[**DesignTag**](DesignTag.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_nk_template_get**
> Template portals_id_designs_nk_template_get(id, nk, refresh=refresh)

Fetches belongsTo relation template.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
nk = 'nk_example' # str | Foreign key for designs.
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation template.
    api_response = api_instance.portals_id_designs_nk_template_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_nk_template_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **nk** | **str**| Foreign key for designs. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_designs_post**
> Design portals_id_designs_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.portals_id_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_exists_get**
> InlineResponse2001 portals_id_exists_get(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portals_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_exists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_get**
> Portal portals_id_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.portals_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_head**
> InlineResponse2001 portals_id_head(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.portals_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_count_get**
> InlineResponse200 portals_id_image_folders_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts imageFolders of Portal.
    api_response = api_instance.portals_id_image_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_delete**
> portals_id_image_folders_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all imageFolders of this model.
    api_instance.portals_id_image_folders_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_fk_delete**
> portals_id_image_folders_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Delete a related item by id for imageFolders.
    api_instance.portals_id_image_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_fk_get**
> ImageFolder portals_id_image_folders_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Find a related item by id for imageFolders.
    api_response = api_instance.portals_id_image_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_fk_put**
> ImageFolder portals_id_image_folders_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for imageFolders.
    api_response = api_instance.portals_id_image_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_image_folders_get**
> list[ImageFolder] portals_id_image_folders_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries imageFolders of Portal.
    api_response = api_instance.portals_id_image_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_post**
> ImageFolder portals_id_image_folders_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in imageFolders of this model.
    api_response = api_instance.portals_id_image_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_rel_fk_delete**
> portals_id_image_folders_rel_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Remove the imageFolders relation to an item by id.
    api_instance.portals_id_image_folders_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_rel_fk_head**
> bool portals_id_image_folders_rel_fk_head(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Check the existence of imageFolders relation to an item by id.
    api_response = api_instance.portals_id_image_folders_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_image_folders_rel_fk_put**
> PortalImageFolder portals_id_image_folders_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.PortalImageFolder() # PortalImageFolder |  (optional)

try: 
    # Add a related item by id for imageFolders.
    api_response = api_instance.portals_id_image_folders_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_image_folders_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_invitation_tickets_fk_delete**
> object portals_id_invitation_tickets_fk_delete(id, id2, fk)

Delete InvitationTickets for this Portal

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | Portal id
fk = 'fk_example' # str | InvitationTicket id

try: 
    # Delete InvitationTickets for this Portal
    api_response = api_instance.portals_id_invitation_tickets_fk_delete(id, id2, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_invitation_tickets_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**| Portal id | 
 **fk** | **str**| InvitationTicket id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_invitation_tickets_fk_get**
> InvitationTicket portals_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)

Get InvitationTicket by Id for this Portal

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | Portal id
fk = 'fk_example' # str | InvitationTicket id
filter = 'filter_example' # str | Only include changes that match this filter (optional)

try: 
    # Get InvitationTicket by Id for this Portal
    api_response = api_instance.portals_id_invitation_tickets_fk_get(id, id2, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_invitation_tickets_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**| Portal id | 
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

# **portals_id_invitation_tickets_get**
> list[InvitationTicket] portals_id_invitation_tickets_get(id, id2, filter=filter)

List InvitationTickets for this Portal

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | Portal id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List InvitationTickets for this Portal
    api_response = api_instance.portals_id_invitation_tickets_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_invitation_tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**| Portal id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_logo_put**
> Portal portals_id_logo_put(id, id2, data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | Portal id
data = TweakApi.Portal() # Portal | Logo

try: 
    # Change logo
    api_response = api_instance.portals_id_logo_put(id, id2, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_logo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**| Portal id | 
 **data** | [**Portal**](Portal.md)| Logo | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_count_get**
> InlineResponse200 portals_id_members_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Portal.
    api_response = api_instance.portals_id_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_delete**
> portals_id_members_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all members of this model.
    api_instance.portals_id_members_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_fk_delete**
> portals_id_members_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.portals_id_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_fk_get**
> TeamMember portals_id_members_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.portals_id_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_fk_put**
> TeamMember portals_id_members_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.portals_id_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_members_get**
> list[TeamMember] portals_id_members_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Portal.
    api_response = api_instance.portals_id_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_post**
> TeamMember portals_id_members_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.portals_id_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_rel_fk_delete**
> portals_id_members_rel_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.portals_id_members_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_rel_fk_head**
> bool portals_id_members_rel_fk_head(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.portals_id_members_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_members_rel_fk_put**
> PortalMember portals_id_members_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.PortalMember() # PortalMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.portals_id_members_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_patch**
> Portal portals_id_patch(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.Portal() # Portal | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.portals_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**Portal**](Portal.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_permission_delete**
> portals_id_permission_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes permission of this model.
    api_instance.portals_id_permission_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_permission_get**
> PortalPermissionSet portals_id_permission_get(id, refresh=refresh)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.portals_id_permission_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**PortalPermissionSet**](PortalPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_permission_post**
> PortalPermissionSet portals_id_permission_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.PortalPermissionSet() # PortalPermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.portals_id_permission_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**PortalPermissionSet**](PortalPermissionSet.md)|  | [optional] 

### Return type

[**PortalPermissionSet**](PortalPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_permission_put**
> PortalPermissionSet portals_id_permission_put(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.PortalPermissionSet() # PortalPermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.portals_id_permission_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**PortalPermissionSet**](PortalPermissionSet.md)|  | [optional] 

### Return type

[**PortalPermissionSet**](PortalPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_portal_members_count_get**
> InlineResponse200 portals_id_portal_members_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portalMembers of Portal.
    api_response = api_instance.portals_id_portal_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_portal_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_portal_members_delete**
> portals_id_portal_members_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all portalMembers of this model.
    api_instance.portals_id_portal_members_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_portal_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_portal_members_fk_delete**
> portals_id_portal_members_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for portalMembers

try: 
    # Delete a related item by id for portalMembers.
    api_instance.portals_id_portal_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_portal_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for portalMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_portal_members_fk_get**
> PortalMember portals_id_portal_members_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for portalMembers

try: 
    # Find a related item by id for portalMembers.
    api_response = api_instance.portals_id_portal_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_portal_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for portalMembers | 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_portal_members_fk_put**
> PortalMember portals_id_portal_members_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for portalMembers
data = TweakApi.PortalMember() # PortalMember |  (optional)

try: 
    # Update a related item by id for portalMembers.
    api_response = api_instance.portals_id_portal_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_portal_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_portal_members_get**
> list[PortalMember] portals_id_portal_members_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portalMembers of Portal.
    api_response = api_instance.portals_id_portal_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_portal_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalMember]**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_portal_members_post**
> PortalMember portals_id_portal_members_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.PortalMember() # PortalMember |  (optional)

try: 
    # Creates a new instance in portalMembers of this model.
    api_response = api_instance.portals_id_portal_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_portal_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**PortalMember**](PortalMember.md)|  | [optional] 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_put**
> Portal portals_id_put(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Model id
data = TweakApi.Portal() # Portal | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portals_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Portal**](Portal.md)| Model instance data | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_replace_post**
> Portal portals_id_replace_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Model id
data = TweakApi.Portal() # Portal | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.portals_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Portal**](Portal.md)| Model instance data | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_team_get**
> Team portals_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.portals_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_count_get**
> InlineResponse200 portals_id_template_folders_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateFolders of Portal.
    api_response = api_instance.portals_id_template_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_delete**
> portals_id_template_folders_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all templateFolders of this model.
    api_instance.portals_id_template_folders_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_fk_delete**
> portals_id_template_folders_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Delete a related item by id for templateFolders.
    api_instance.portals_id_template_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_fk_get**
> PortalTemplateFolder portals_id_template_folders_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Find a related item by id for templateFolders.
    api_response = api_instance.portals_id_template_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_fk_put**
> PortalTemplateFolder portals_id_template_folders_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templateFolders
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Update a related item by id for templateFolders.
    api_response = api_instance.portals_id_template_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_template_folders_get**
> list[PortalTemplateFolder] portals_id_template_folders_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateFolders of Portal.
    api_response = api_instance.portals_id_template_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalTemplateFolder]**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_nk_templates_fk_rel_delete**
> PortalTemplate portals_id_template_folders_nk_templates_fk_rel_delete(id, id2, nk, fk)

Unlink folder with Template and Portal

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | Portal id
nk = 'nk_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Template id

try: 
    # Unlink folder with Template and Portal
    api_response = api_instance.portals_id_template_folders_nk_templates_fk_rel_delete(id, id2, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_nk_templates_fk_rel_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**| Portal id | 
 **nk** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Template id | 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_nk_templates_fk_rel_put**
> PortalTemplate portals_id_template_folders_nk_templates_fk_rel_put(id, id2, nk, fk)

Link folder with Template and Portal

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | Portal id
nk = 'nk_example' # str | PortalTemplateFolder id
fk = 'fk_example' # str | Template id

try: 
    # Link folder with Template and Portal
    api_response = api_instance.portals_id_template_folders_nk_templates_fk_rel_put(id, id2, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_nk_templates_fk_rel_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**| Portal id | 
 **nk** | **str**| PortalTemplateFolder id | 
 **fk** | **str**| Template id | 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_post**
> PortalTemplateFolder portals_id_template_folders_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.PortalTemplateFolder() # PortalTemplateFolder |  (optional)

try: 
    # Creates a new instance in templateFolders of this model.
    api_response = api_instance.portals_id_template_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**PortalTemplateFolder**](PortalTemplateFolder.md)|  | [optional] 

### Return type

[**PortalTemplateFolder**](PortalTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_folders_root_templates_get**
> list[PortalTemplate] portals_id_template_folders_root_templates_get(id, id2, filter=filter)

List templates on root folder

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | Portal id
filter = 'filter_example' # str | Only include changes that match this filter (optional)

try: 
    # List templates on root folder
    api_response = api_instance.portals_id_template_folders_root_templates_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_folders_root_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**| Portal id | 
 **filter** | **str**| Only include changes that match this filter | [optional] 

### Return type

[**list[PortalTemplate]**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_rels_count_get**
> InlineResponse200 portals_id_template_rels_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateRels of Portal.
    api_response = api_instance.portals_id_template_rels_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_rels_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_rels_delete**
> portals_id_template_rels_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all templateRels of this model.
    api_instance.portals_id_template_rels_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_rels_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_rels_fk_delete**
> portals_id_template_rels_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templateRels

try: 
    # Delete a related item by id for templateRels.
    api_instance.portals_id_template_rels_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_rels_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templateRels | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_rels_fk_get**
> PortalTemplate portals_id_template_rels_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templateRels

try: 
    # Find a related item by id for templateRels.
    api_response = api_instance.portals_id_template_rels_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_rels_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templateRels | 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_rels_fk_put**
> PortalTemplate portals_id_template_rels_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templateRels
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Update a related item by id for templateRels.
    api_response = api_instance.portals_id_template_rels_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_rels_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_template_rels_get**
> list[PortalTemplate] portals_id_template_rels_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateRels of Portal.
    api_response = api_instance.portals_id_template_rels_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_rels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[PortalTemplate]**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_template_rels_post**
> PortalTemplate portals_id_template_rels_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Creates a new instance in templateRels of this model.
    api_response = api_instance.portals_id_template_rels_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_template_rels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**PortalTemplate**](PortalTemplate.md)|  | [optional] 

### Return type

[**PortalTemplate**](PortalTemplate.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_count_get**
> InlineResponse200 portals_id_templates_count_get(id, where=where)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of Portal.
    api_response = api_instance.portals_id_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_delete**
> portals_id_templates_delete(id)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id

try: 
    # Deletes all templates of this model.
    api_instance.portals_id_templates_delete(id)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_fk_delete**
> portals_id_templates_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.portals_id_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_fk_designs_generate_bulk_post**
> list[Design] portals_id_templates_fk_designs_generate_bulk_post(id, id2, fk, data=data)

Generate Design from Template

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | 
fk = 'fk_example' # str | 
data = [TweakApi.list[object]()] # list[object] |  (optional)

try: 
    # Generate Design from Template
    api_response = api_instance.portals_id_templates_fk_designs_generate_bulk_post(id, id2, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_fk_designs_generate_bulk_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**|  | 
 **fk** | **str**|  | 
 **data** | **list[object]**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_fk_designs_generate_post**
> Design portals_id_templates_fk_designs_generate_post(id, id2, fk, data=data)

Generate Design from Template

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
id2 = 'id_example' # str | 
fk = 'fk_example' # str | 
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Generate Design from Template
    api_response = api_instance.portals_id_templates_fk_designs_generate_post(id, id2, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_fk_designs_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **id2** | **str**|  | 
 **fk** | **str**|  | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_fk_get**
> Template portals_id_templates_fk_get(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.portals_id_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_fk_put**
> Template portals_id_templates_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.portals_id_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_id_templates_get**
> list[Template] portals_id_templates_get(id, filter=filter)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of Portal.
    api_response = api_instance.portals_id_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_post**
> Template portals_id_templates_post(id, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.portals_id_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_rel_fk_delete**
> portals_id_templates_rel_fk_delete(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Remove the templates relation to an item by id.
    api_instance.portals_id_templates_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_rel_fk_head**
> bool portals_id_templates_rel_fk_head(id, fk)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Check the existence of templates relation to an item by id.
    api_response = api_instance.portals_id_templates_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_id_templates_rel_fk_put**
> PortalTemplate portals_id_templates_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.PortalApi()
id = 'id_example' # str | Portal id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.PortalTemplate() # PortalTemplate |  (optional)

try: 
    # Add a related item by id for templates.
    api_response = api_instance.portals_id_templates_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_id_templates_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Portal id | 
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

# **portals_patch**
> Portal portals_patch(data=data)

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
api_instance = TweakApi.PortalApi()
data = TweakApi.Portal() # Portal | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.portals_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Portal**](Portal.md)| Model instance data | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_post**
> Portal portals_post(data=data)

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
api_instance = TweakApi.PortalApi()
data = TweakApi.Portal() # Portal | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.portals_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Portal**](Portal.md)| Model instance data | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_put**
> Portal portals_put(data=data)

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
api_instance = TweakApi.PortalApi()
data = TweakApi.Portal() # Portal | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.portals_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Portal**](Portal.md)| Model instance data | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_replace_or_create_post**
> Portal portals_replace_or_create_post(data=data)

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
api_instance = TweakApi.PortalApi()
data = TweakApi.Portal() # Portal | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.portals_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Portal**](Portal.md)| Model instance data | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_update_post**
> InlineResponse2002 portals_update_post(where=where, data=data)

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
api_instance = TweakApi.PortalApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Portal() # Portal | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.portals_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Portal**](Portal.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portals_upsert_with_where_post**
> Portal portals_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.PortalApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Portal() # Portal | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.portals_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->portals_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Portal**](Portal.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

