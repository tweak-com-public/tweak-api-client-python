# TweakApi.TeamMemberApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_members_change_stream_get**](TeamMemberApi.md#team_members_change_stream_get) | **GET** /TeamMembers/change-stream | Create a change stream.
[**team_members_change_stream_post**](TeamMemberApi.md#team_members_change_stream_post) | **POST** /TeamMembers/change-stream | Create a change stream.
[**team_members_count_get**](TeamMemberApi.md#team_members_count_get) | **GET** /TeamMembers/count | Count instances of the model matched by where from the data source.
[**team_members_find_one_get**](TeamMemberApi.md#team_members_find_one_get) | **GET** /TeamMembers/findOne | Find first instance of the model matched by filter from the data source.
[**team_members_get**](TeamMemberApi.md#team_members_get) | **GET** /TeamMembers | Find all instances of the model matched by filter from the data source.
[**team_members_id_assigned_designs_count_get**](TeamMemberApi.md#team_members_id_assigned_designs_count_get) | **GET** /TeamMembers/{id}/assignedDesigns/count | Counts assignedDesigns of TeamMember.
[**team_members_id_assigned_designs_delete**](TeamMemberApi.md#team_members_id_assigned_designs_delete) | **DELETE** /TeamMembers/{id}/assignedDesigns | Deletes all assignedDesigns of this model.
[**team_members_id_assigned_designs_fk_delete**](TeamMemberApi.md#team_members_id_assigned_designs_fk_delete) | **DELETE** /TeamMembers/{id}/assignedDesigns/{fk} | Delete a related item by id for assignedDesigns.
[**team_members_id_assigned_designs_fk_get**](TeamMemberApi.md#team_members_id_assigned_designs_fk_get) | **GET** /TeamMembers/{id}/assignedDesigns/{fk} | Find a related item by id for assignedDesigns.
[**team_members_id_assigned_designs_fk_put**](TeamMemberApi.md#team_members_id_assigned_designs_fk_put) | **PUT** /TeamMembers/{id}/assignedDesigns/{fk} | Update a related item by id for assignedDesigns.
[**team_members_id_assigned_designs_get**](TeamMemberApi.md#team_members_id_assigned_designs_get) | **GET** /TeamMembers/{id}/assignedDesigns | Queries assignedDesigns of TeamMember.
[**team_members_id_assigned_designs_post**](TeamMemberApi.md#team_members_id_assigned_designs_post) | **POST** /TeamMembers/{id}/assignedDesigns | Creates a new instance in assignedDesigns of this model.
[**team_members_id_commented_designs_count_get**](TeamMemberApi.md#team_members_id_commented_designs_count_get) | **GET** /TeamMembers/{id}/commentedDesigns/count | Counts commentedDesigns of TeamMember.
[**team_members_id_commented_designs_delete**](TeamMemberApi.md#team_members_id_commented_designs_delete) | **DELETE** /TeamMembers/{id}/commentedDesigns | Deletes all commentedDesigns of this model.
[**team_members_id_commented_designs_fk_delete**](TeamMemberApi.md#team_members_id_commented_designs_fk_delete) | **DELETE** /TeamMembers/{id}/commentedDesigns/{fk} | Delete a related item by id for commentedDesigns.
[**team_members_id_commented_designs_fk_get**](TeamMemberApi.md#team_members_id_commented_designs_fk_get) | **GET** /TeamMembers/{id}/commentedDesigns/{fk} | Find a related item by id for commentedDesigns.
[**team_members_id_commented_designs_fk_put**](TeamMemberApi.md#team_members_id_commented_designs_fk_put) | **PUT** /TeamMembers/{id}/commentedDesigns/{fk} | Update a related item by id for commentedDesigns.
[**team_members_id_commented_designs_get**](TeamMemberApi.md#team_members_id_commented_designs_get) | **GET** /TeamMembers/{id}/commentedDesigns | Queries commentedDesigns of TeamMember.
[**team_members_id_commented_designs_post**](TeamMemberApi.md#team_members_id_commented_designs_post) | **POST** /TeamMembers/{id}/commentedDesigns | Creates a new instance in commentedDesigns of this model.
[**team_members_id_commented_designs_rel_fk_delete**](TeamMemberApi.md#team_members_id_commented_designs_rel_fk_delete) | **DELETE** /TeamMembers/{id}/commentedDesigns/rel/{fk} | Remove the commentedDesigns relation to an item by id.
[**team_members_id_commented_designs_rel_fk_head**](TeamMemberApi.md#team_members_id_commented_designs_rel_fk_head) | **HEAD** /TeamMembers/{id}/commentedDesigns/rel/{fk} | Check the existence of commentedDesigns relation to an item by id.
[**team_members_id_commented_designs_rel_fk_put**](TeamMemberApi.md#team_members_id_commented_designs_rel_fk_put) | **PUT** /TeamMembers/{id}/commentedDesigns/rel/{fk} | Add a related item by id for commentedDesigns.
[**team_members_id_customer_get**](TeamMemberApi.md#team_members_id_customer_get) | **GET** /TeamMembers/{id}/customer | Fetches belongsTo relation customer.
[**team_members_id_delete**](TeamMemberApi.md#team_members_id_delete) | **DELETE** /TeamMembers/{id} | Delete a model instance by {{id}} from the data source.
[**team_members_id_design_comments_count_get**](TeamMemberApi.md#team_members_id_design_comments_count_get) | **GET** /TeamMembers/{id}/designComments/count | Counts designComments of TeamMember.
[**team_members_id_design_comments_delete**](TeamMemberApi.md#team_members_id_design_comments_delete) | **DELETE** /TeamMembers/{id}/designComments | Deletes all designComments of this model.
[**team_members_id_design_comments_fk_delete**](TeamMemberApi.md#team_members_id_design_comments_fk_delete) | **DELETE** /TeamMembers/{id}/designComments/{fk} | Delete a related item by id for designComments.
[**team_members_id_design_comments_fk_get**](TeamMemberApi.md#team_members_id_design_comments_fk_get) | **GET** /TeamMembers/{id}/designComments/{fk} | Find a related item by id for designComments.
[**team_members_id_design_comments_fk_put**](TeamMemberApi.md#team_members_id_design_comments_fk_put) | **PUT** /TeamMembers/{id}/designComments/{fk} | Update a related item by id for designComments.
[**team_members_id_design_comments_get**](TeamMemberApi.md#team_members_id_design_comments_get) | **GET** /TeamMembers/{id}/designComments | Queries designComments of TeamMember.
[**team_members_id_design_comments_post**](TeamMemberApi.md#team_members_id_design_comments_post) | **POST** /TeamMembers/{id}/designComments | Creates a new instance in designComments of this model.
[**team_members_id_design_folders_count_get**](TeamMemberApi.md#team_members_id_design_folders_count_get) | **GET** /TeamMembers/{id}/designFolders/count | Counts designFolders of TeamMember.
[**team_members_id_design_folders_delete**](TeamMemberApi.md#team_members_id_design_folders_delete) | **DELETE** /TeamMembers/{id}/designFolders | Deletes all designFolders of this model.
[**team_members_id_design_folders_fk_delete**](TeamMemberApi.md#team_members_id_design_folders_fk_delete) | **DELETE** /TeamMembers/{id}/designFolders/{fk} | Delete a related item by id for designFolders.
[**team_members_id_design_folders_fk_get**](TeamMemberApi.md#team_members_id_design_folders_fk_get) | **GET** /TeamMembers/{id}/designFolders/{fk} | Find a related item by id for designFolders.
[**team_members_id_design_folders_fk_put**](TeamMemberApi.md#team_members_id_design_folders_fk_put) | **PUT** /TeamMembers/{id}/designFolders/{fk} | Update a related item by id for designFolders.
[**team_members_id_design_folders_get**](TeamMemberApi.md#team_members_id_design_folders_get) | **GET** /TeamMembers/{id}/designFolders | Queries designFolders of TeamMember.
[**team_members_id_design_folders_post**](TeamMemberApi.md#team_members_id_design_folders_post) | **POST** /TeamMembers/{id}/designFolders | Creates a new instance in designFolders of this model.
[**team_members_id_design_shares_count_get**](TeamMemberApi.md#team_members_id_design_shares_count_get) | **GET** /TeamMembers/{id}/designShares/count | Counts designShares of TeamMember.
[**team_members_id_design_shares_delete**](TeamMemberApi.md#team_members_id_design_shares_delete) | **DELETE** /TeamMembers/{id}/designShares | Deletes all designShares of this model.
[**team_members_id_design_shares_fk_delete**](TeamMemberApi.md#team_members_id_design_shares_fk_delete) | **DELETE** /TeamMembers/{id}/designShares/{fk} | Delete a related item by id for designShares.
[**team_members_id_design_shares_fk_get**](TeamMemberApi.md#team_members_id_design_shares_fk_get) | **GET** /TeamMembers/{id}/designShares/{fk} | Find a related item by id for designShares.
[**team_members_id_design_shares_fk_put**](TeamMemberApi.md#team_members_id_design_shares_fk_put) | **PUT** /TeamMembers/{id}/designShares/{fk} | Update a related item by id for designShares.
[**team_members_id_design_shares_get**](TeamMemberApi.md#team_members_id_design_shares_get) | **GET** /TeamMembers/{id}/designShares | Queries designShares of TeamMember.
[**team_members_id_design_shares_post**](TeamMemberApi.md#team_members_id_design_shares_post) | **POST** /TeamMembers/{id}/designShares | Creates a new instance in designShares of this model.
[**team_members_id_exists_get**](TeamMemberApi.md#team_members_id_exists_get) | **GET** /TeamMembers/{id}/exists | Check whether a model instance exists in the data source.
[**team_members_id_get**](TeamMemberApi.md#team_members_id_get) | **GET** /TeamMembers/{id} | Find a model instance by {{id}} from the data source.
[**team_members_id_head**](TeamMemberApi.md#team_members_id_head) | **HEAD** /TeamMembers/{id} | Check whether a model instance exists in the data source.
[**team_members_id_image_folders_count_get**](TeamMemberApi.md#team_members_id_image_folders_count_get) | **GET** /TeamMembers/{id}/imageFolders/count | Counts imageFolders of TeamMember.
[**team_members_id_image_folders_delete**](TeamMemberApi.md#team_members_id_image_folders_delete) | **DELETE** /TeamMembers/{id}/imageFolders | Deletes all imageFolders of this model.
[**team_members_id_image_folders_fk_delete**](TeamMemberApi.md#team_members_id_image_folders_fk_delete) | **DELETE** /TeamMembers/{id}/imageFolders/{fk} | Delete a related item by id for imageFolders.
[**team_members_id_image_folders_fk_get**](TeamMemberApi.md#team_members_id_image_folders_fk_get) | **GET** /TeamMembers/{id}/imageFolders/{fk} | Find a related item by id for imageFolders.
[**team_members_id_image_folders_fk_put**](TeamMemberApi.md#team_members_id_image_folders_fk_put) | **PUT** /TeamMembers/{id}/imageFolders/{fk} | Update a related item by id for imageFolders.
[**team_members_id_image_folders_get**](TeamMemberApi.md#team_members_id_image_folders_get) | **GET** /TeamMembers/{id}/imageFolders | Queries imageFolders of TeamMember.
[**team_members_id_image_folders_post**](TeamMemberApi.md#team_members_id_image_folders_post) | **POST** /TeamMembers/{id}/imageFolders | Creates a new instance in imageFolders of this model.
[**team_members_id_image_folders_rel_fk_delete**](TeamMemberApi.md#team_members_id_image_folders_rel_fk_delete) | **DELETE** /TeamMembers/{id}/imageFolders/rel/{fk} | Remove the imageFolders relation to an item by id.
[**team_members_id_image_folders_rel_fk_head**](TeamMemberApi.md#team_members_id_image_folders_rel_fk_head) | **HEAD** /TeamMembers/{id}/imageFolders/rel/{fk} | Check the existence of imageFolders relation to an item by id.
[**team_members_id_image_folders_rel_fk_put**](TeamMemberApi.md#team_members_id_image_folders_rel_fk_put) | **PUT** /TeamMembers/{id}/imageFolders/rel/{fk} | Add a related item by id for imageFolders.
[**team_members_id_invitation_tickets_count_get**](TeamMemberApi.md#team_members_id_invitation_tickets_count_get) | **GET** /TeamMembers/{id}/invitationTickets/count | Counts invitationTickets of TeamMember.
[**team_members_id_invitation_tickets_delete**](TeamMemberApi.md#team_members_id_invitation_tickets_delete) | **DELETE** /TeamMembers/{id}/invitationTickets | Deletes all invitationTickets of this model.
[**team_members_id_invitation_tickets_fk_delete**](TeamMemberApi.md#team_members_id_invitation_tickets_fk_delete) | **DELETE** /TeamMembers/{id}/invitationTickets/{fk} | Delete a related item by id for invitationTickets.
[**team_members_id_invitation_tickets_fk_get**](TeamMemberApi.md#team_members_id_invitation_tickets_fk_get) | **GET** /TeamMembers/{id}/invitationTickets/{fk} | Find a related item by id for invitationTickets.
[**team_members_id_invitation_tickets_fk_put**](TeamMemberApi.md#team_members_id_invitation_tickets_fk_put) | **PUT** /TeamMembers/{id}/invitationTickets/{fk} | Update a related item by id for invitationTickets.
[**team_members_id_invitation_tickets_get**](TeamMemberApi.md#team_members_id_invitation_tickets_get) | **GET** /TeamMembers/{id}/invitationTickets | Queries invitationTickets of TeamMember.
[**team_members_id_invitation_tickets_post**](TeamMemberApi.md#team_members_id_invitation_tickets_post) | **POST** /TeamMembers/{id}/invitationTickets | Creates a new instance in invitationTickets of this model.
[**team_members_id_invite_invitee_post**](TeamMemberApi.md#team_members_id_invite_invitee_post) | **POST** /TeamMembers/{id}/invite/{invitee} | Invite somebody to join the team
[**team_members_id_notifications_count_get**](TeamMemberApi.md#team_members_id_notifications_count_get) | **GET** /TeamMembers/{id}/notifications/count | Counts notifications of TeamMember.
[**team_members_id_notifications_delete**](TeamMemberApi.md#team_members_id_notifications_delete) | **DELETE** /TeamMembers/{id}/notifications | Deletes all notifications of this model.
[**team_members_id_notifications_fk_delete**](TeamMemberApi.md#team_members_id_notifications_fk_delete) | **DELETE** /TeamMembers/{id}/notifications/{fk} | Delete a related item by id for notifications.
[**team_members_id_notifications_fk_get**](TeamMemberApi.md#team_members_id_notifications_fk_get) | **GET** /TeamMembers/{id}/notifications/{fk} | Find a related item by id for notifications.
[**team_members_id_notifications_fk_put**](TeamMemberApi.md#team_members_id_notifications_fk_put) | **PUT** /TeamMembers/{id}/notifications/{fk} | Update a related item by id for notifications.
[**team_members_id_notifications_get**](TeamMemberApi.md#team_members_id_notifications_get) | **GET** /TeamMembers/{id}/notifications | Queries notifications of TeamMember.
[**team_members_id_notifications_post**](TeamMemberApi.md#team_members_id_notifications_post) | **POST** /TeamMembers/{id}/notifications | Creates a new instance in notifications of this model.
[**team_members_id_patch**](TeamMemberApi.md#team_members_id_patch) | **PATCH** /TeamMembers/{id} | Patch attributes for a model instance and persist it into the data source.
[**team_members_id_portals_available_get**](TeamMemberApi.md#team_members_id_portals_available_get) | **GET** /TeamMembers/{id}/portals/available | Find all available Portals
[**team_members_id_portals_count_get**](TeamMemberApi.md#team_members_id_portals_count_get) | **GET** /TeamMembers/{id}/portals/count | Counts portals of TeamMember.
[**team_members_id_portals_delete**](TeamMemberApi.md#team_members_id_portals_delete) | **DELETE** /TeamMembers/{id}/portals | Deletes all portals of this model.
[**team_members_id_portals_fk_available_get**](TeamMemberApi.md#team_members_id_portals_fk_available_get) | **GET** /TeamMembers/{id}/portals/{fk}/available | Find available Portal by id
[**team_members_id_portals_fk_delete**](TeamMemberApi.md#team_members_id_portals_fk_delete) | **DELETE** /TeamMembers/{id}/portals/{fk} | Delete a related item by id for portals.
[**team_members_id_portals_fk_get**](TeamMemberApi.md#team_members_id_portals_fk_get) | **GET** /TeamMembers/{id}/portals/{fk} | Find a related item by id for portals.
[**team_members_id_portals_fk_logo_put**](TeamMemberApi.md#team_members_id_portals_fk_logo_put) | **PUT** /TeamMembers/{id}/portals/{fk}/logo | Change Portal logo
[**team_members_id_portals_fk_put**](TeamMemberApi.md#team_members_id_portals_fk_put) | **PUT** /TeamMembers/{id}/portals/{fk} | Update a related item by id for portals.
[**team_members_id_portals_get**](TeamMemberApi.md#team_members_id_portals_get) | **GET** /TeamMembers/{id}/portals | Queries portals of TeamMember.
[**team_members_id_portals_nk_designs_fk_flashvars_get**](TeamMemberApi.md#team_members_id_portals_nk_designs_fk_flashvars_get) | **GET** /TeamMembers/{id}/portals/{nk}/designs/{fk}/flashvars | Find Design FlashVars within available Portal by id
[**team_members_id_portals_nk_templates_fk_flashvars_get**](TeamMemberApi.md#team_members_id_portals_nk_templates_fk_flashvars_get) | **GET** /TeamMembers/{id}/portals/{nk}/templates/{fk}/flashvars | Find Template FlashVars within available Portal by id
[**team_members_id_portals_post**](TeamMemberApi.md#team_members_id_portals_post) | **POST** /TeamMembers/{id}/portals | Creates a new instance in portals of this model.
[**team_members_id_portals_rel_fk_delete**](TeamMemberApi.md#team_members_id_portals_rel_fk_delete) | **DELETE** /TeamMembers/{id}/portals/rel/{fk} | Remove the portals relation to an item by id.
[**team_members_id_portals_rel_fk_head**](TeamMemberApi.md#team_members_id_portals_rel_fk_head) | **HEAD** /TeamMembers/{id}/portals/rel/{fk} | Check the existence of portals relation to an item by id.
[**team_members_id_portals_rel_fk_put**](TeamMemberApi.md#team_members_id_portals_rel_fk_put) | **PUT** /TeamMembers/{id}/portals/rel/{fk} | Add a related item by id for portals.
[**team_members_id_put**](TeamMemberApi.md#team_members_id_put) | **PUT** /TeamMembers/{id} | Replace attributes for a model instance and persist it into the data source.
[**team_members_id_replace_post**](TeamMemberApi.md#team_members_id_replace_post) | **POST** /TeamMembers/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**team_members_id_requested_design_exports_count_get**](TeamMemberApi.md#team_members_id_requested_design_exports_count_get) | **GET** /TeamMembers/{id}/requestedDesignExports/count | Counts requestedDesignExports of TeamMember.
[**team_members_id_requested_design_exports_delete**](TeamMemberApi.md#team_members_id_requested_design_exports_delete) | **DELETE** /TeamMembers/{id}/requestedDesignExports | Deletes all requestedDesignExports of this model.
[**team_members_id_requested_design_exports_fk_delete**](TeamMemberApi.md#team_members_id_requested_design_exports_fk_delete) | **DELETE** /TeamMembers/{id}/requestedDesignExports/{fk} | Delete a related item by id for requestedDesignExports.
[**team_members_id_requested_design_exports_fk_get**](TeamMemberApi.md#team_members_id_requested_design_exports_fk_get) | **GET** /TeamMembers/{id}/requestedDesignExports/{fk} | Find a related item by id for requestedDesignExports.
[**team_members_id_requested_design_exports_fk_put**](TeamMemberApi.md#team_members_id_requested_design_exports_fk_put) | **PUT** /TeamMembers/{id}/requestedDesignExports/{fk} | Update a related item by id for requestedDesignExports.
[**team_members_id_requested_design_exports_get**](TeamMemberApi.md#team_members_id_requested_design_exports_get) | **GET** /TeamMembers/{id}/requestedDesignExports | Queries requestedDesignExports of TeamMember.
[**team_members_id_requested_design_exports_post**](TeamMemberApi.md#team_members_id_requested_design_exports_post) | **POST** /TeamMembers/{id}/requestedDesignExports | Creates a new instance in requestedDesignExports of this model.
[**team_members_id_requested_designs_count_get**](TeamMemberApi.md#team_members_id_requested_designs_count_get) | **GET** /TeamMembers/{id}/requestedDesigns/count | Counts requestedDesigns of TeamMember.
[**team_members_id_requested_designs_delete**](TeamMemberApi.md#team_members_id_requested_designs_delete) | **DELETE** /TeamMembers/{id}/requestedDesigns | Deletes all requestedDesigns of this model.
[**team_members_id_requested_designs_fk_delete**](TeamMemberApi.md#team_members_id_requested_designs_fk_delete) | **DELETE** /TeamMembers/{id}/requestedDesigns/{fk} | Delete a related item by id for requestedDesigns.
[**team_members_id_requested_designs_fk_get**](TeamMemberApi.md#team_members_id_requested_designs_fk_get) | **GET** /TeamMembers/{id}/requestedDesigns/{fk} | Find a related item by id for requestedDesigns.
[**team_members_id_requested_designs_fk_put**](TeamMemberApi.md#team_members_id_requested_designs_fk_put) | **PUT** /TeamMembers/{id}/requestedDesigns/{fk} | Update a related item by id for requestedDesigns.
[**team_members_id_requested_designs_get**](TeamMemberApi.md#team_members_id_requested_designs_get) | **GET** /TeamMembers/{id}/requestedDesigns | Queries requestedDesigns of TeamMember.
[**team_members_id_requested_designs_post**](TeamMemberApi.md#team_members_id_requested_designs_post) | **POST** /TeamMembers/{id}/requestedDesigns | Creates a new instance in requestedDesigns of this model.
[**team_members_id_reviewed_designs_count_get**](TeamMemberApi.md#team_members_id_reviewed_designs_count_get) | **GET** /TeamMembers/{id}/reviewedDesigns/count | Counts reviewedDesigns of TeamMember.
[**team_members_id_reviewed_designs_delete**](TeamMemberApi.md#team_members_id_reviewed_designs_delete) | **DELETE** /TeamMembers/{id}/reviewedDesigns | Deletes all reviewedDesigns of this model.
[**team_members_id_reviewed_designs_fk_delete**](TeamMemberApi.md#team_members_id_reviewed_designs_fk_delete) | **DELETE** /TeamMembers/{id}/reviewedDesigns/{fk} | Delete a related item by id for reviewedDesigns.
[**team_members_id_reviewed_designs_fk_get**](TeamMemberApi.md#team_members_id_reviewed_designs_fk_get) | **GET** /TeamMembers/{id}/reviewedDesigns/{fk} | Find a related item by id for reviewedDesigns.
[**team_members_id_reviewed_designs_fk_put**](TeamMemberApi.md#team_members_id_reviewed_designs_fk_put) | **PUT** /TeamMembers/{id}/reviewedDesigns/{fk} | Update a related item by id for reviewedDesigns.
[**team_members_id_reviewed_designs_get**](TeamMemberApi.md#team_members_id_reviewed_designs_get) | **GET** /TeamMembers/{id}/reviewedDesigns | Queries reviewedDesigns of TeamMember.
[**team_members_id_reviewed_designs_post**](TeamMemberApi.md#team_members_id_reviewed_designs_post) | **POST** /TeamMembers/{id}/reviewedDesigns | Creates a new instance in reviewedDesigns of this model.
[**team_members_id_shared_designs_count_get**](TeamMemberApi.md#team_members_id_shared_designs_count_get) | **GET** /TeamMembers/{id}/sharedDesigns/count | Counts sharedDesigns of TeamMember.
[**team_members_id_shared_designs_delete**](TeamMemberApi.md#team_members_id_shared_designs_delete) | **DELETE** /TeamMembers/{id}/sharedDesigns | Deletes all sharedDesigns of this model.
[**team_members_id_shared_designs_fk_delete**](TeamMemberApi.md#team_members_id_shared_designs_fk_delete) | **DELETE** /TeamMembers/{id}/sharedDesigns/{fk} | Delete a related item by id for sharedDesigns.
[**team_members_id_shared_designs_fk_get**](TeamMemberApi.md#team_members_id_shared_designs_fk_get) | **GET** /TeamMembers/{id}/sharedDesigns/{fk} | Find a related item by id for sharedDesigns.
[**team_members_id_shared_designs_fk_put**](TeamMemberApi.md#team_members_id_shared_designs_fk_put) | **PUT** /TeamMembers/{id}/sharedDesigns/{fk} | Update a related item by id for sharedDesigns.
[**team_members_id_shared_designs_get**](TeamMemberApi.md#team_members_id_shared_designs_get) | **GET** /TeamMembers/{id}/sharedDesigns | Queries sharedDesigns of TeamMember.
[**team_members_id_shared_designs_post**](TeamMemberApi.md#team_members_id_shared_designs_post) | **POST** /TeamMembers/{id}/sharedDesigns | Creates a new instance in sharedDesigns of this model.
[**team_members_id_shared_designs_rel_fk_delete**](TeamMemberApi.md#team_members_id_shared_designs_rel_fk_delete) | **DELETE** /TeamMembers/{id}/sharedDesigns/rel/{fk} | Remove the sharedDesigns relation to an item by id.
[**team_members_id_shared_designs_rel_fk_head**](TeamMemberApi.md#team_members_id_shared_designs_rel_fk_head) | **HEAD** /TeamMembers/{id}/sharedDesigns/rel/{fk} | Check the existence of sharedDesigns relation to an item by id.
[**team_members_id_shared_designs_rel_fk_put**](TeamMemberApi.md#team_members_id_shared_designs_rel_fk_put) | **PUT** /TeamMembers/{id}/sharedDesigns/rel/{fk} | Add a related item by id for sharedDesigns.
[**team_members_id_target_model_target_id_invite_invitee_post**](TeamMemberApi.md#team_members_id_target_model_target_id_invite_invitee_post) | **POST** /TeamMembers/{id}/{targetModel}/{targetId}/invite/{invitee} | Invite somebody to join a team, portal or other targets
[**team_members_id_target_model_target_id_invite_post**](TeamMemberApi.md#team_members_id_target_model_target_id_invite_post) | **POST** /TeamMembers/{id}/{targetModel}/{targetId}/invite | Invite a group of people to join a team, portal or other targets
[**team_members_id_team_billing_available_plans_get**](TeamMemberApi.md#team_members_id_team_billing_available_plans_get) | **GET** /TeamMembers/{id}/team/billing/availablePlans | Get Available Plans
[**team_members_id_team_billing_cached_get**](TeamMemberApi.md#team_members_id_team_billing_cached_get) | **GET** /TeamMembers/{id}/team/billing/cached | Get Cached version of Team Billing
[**team_members_id_team_billing_card_delete**](TeamMemberApi.md#team_members_id_team_billing_card_delete) | **DELETE** /TeamMembers/{id}/team/billing/card | Delete Team Billing Card
[**team_members_id_team_billing_card_post**](TeamMemberApi.md#team_members_id_team_billing_card_post) | **POST** /TeamMembers/{id}/team/billing/card | Create Team Billing Card
[**team_members_id_team_billing_card_put**](TeamMemberApi.md#team_members_id_team_billing_card_put) | **PUT** /TeamMembers/{id}/team/billing/card | Update Team Billing Card
[**team_members_id_team_billing_invoices_fk_post**](TeamMemberApi.md#team_members_id_team_billing_invoices_fk_post) | **POST** /TeamMembers/{id}/team/billing/invoices/{fk} | Pay Team Billing Invoice
[**team_members_id_team_billing_invoices_get**](TeamMemberApi.md#team_members_id_team_billing_invoices_get) | **GET** /TeamMembers/{id}/team/billing/invoices | List Team Billing Invoices
[**team_members_id_team_billing_invoices_upcoming_get**](TeamMemberApi.md#team_members_id_team_billing_invoices_upcoming_get) | **GET** /TeamMembers/{id}/team/billing/invoices/upcoming | List Upcoming Team Billing Invoices
[**team_members_id_team_billing_put**](TeamMemberApi.md#team_members_id_team_billing_put) | **PUT** /TeamMembers/{id}/team/billing | Update Team Billing
[**team_members_id_team_billing_subscription_plan_put**](TeamMemberApi.md#team_members_id_team_billing_subscription_plan_put) | **PUT** /TeamMembers/{id}/team/billing/subscription/plan | Update Team Billing Subscription Plan
[**team_members_id_team_billing_tax_evidence_get**](TeamMemberApi.md#team_members_id_team_billing_tax_evidence_get) | **GET** /TeamMembers/{id}/team/billing/taxEvidence | Get Team Billing Tax Evidence
[**team_members_id_team_billing_uncached_get**](TeamMemberApi.md#team_members_id_team_billing_uncached_get) | **GET** /TeamMembers/{id}/team/billing/uncached | Get Team Billing
[**team_members_id_team_brand_delete**](TeamMemberApi.md#team_members_id_team_brand_delete) | **DELETE** /TeamMembers/{id}/team/brand | Deletes brand of this model.
[**team_members_id_team_brand_get**](TeamMemberApi.md#team_members_id_team_brand_get) | **GET** /TeamMembers/{id}/team/brand | Fetches hasOne relation brand.
[**team_members_id_team_brand_post**](TeamMemberApi.md#team_members_id_team_brand_post) | **POST** /TeamMembers/{id}/team/brand | Creates a new instance in brand of this model.
[**team_members_id_team_brand_put**](TeamMemberApi.md#team_members_id_team_brand_put) | **PUT** /TeamMembers/{id}/team/brand | Update brand of this model.
[**team_members_id_team_builder_configs_count_get**](TeamMemberApi.md#team_members_id_team_builder_configs_count_get) | **GET** /TeamMembers/{id}/team/builderConfigs/count | Counts builderConfigs of Team.
[**team_members_id_team_builder_configs_default_get**](TeamMemberApi.md#team_members_id_team_builder_configs_default_get) | **GET** /TeamMembers/{id}/team/builderConfigs/default | Get default Team Builder Config
[**team_members_id_team_builder_configs_delete**](TeamMemberApi.md#team_members_id_team_builder_configs_delete) | **DELETE** /TeamMembers/{id}/team/builderConfigs | Deletes all builderConfigs of this model.
[**team_members_id_team_builder_configs_fk_delete**](TeamMemberApi.md#team_members_id_team_builder_configs_fk_delete) | **DELETE** /TeamMembers/{id}/team/builderConfigs/{fk} | Delete a related item by id for builderConfigs.
[**team_members_id_team_builder_configs_fk_get**](TeamMemberApi.md#team_members_id_team_builder_configs_fk_get) | **GET** /TeamMembers/{id}/team/builderConfigs/{fk} | Find a related item by id for builderConfigs.
[**team_members_id_team_builder_configs_fk_logo_put**](TeamMemberApi.md#team_members_id_team_builder_configs_fk_logo_put) | **PUT** /TeamMembers/{id}/team/builderConfigs/{fk}/logo | Change Builder Config logo
[**team_members_id_team_builder_configs_fk_put**](TeamMemberApi.md#team_members_id_team_builder_configs_fk_put) | **PUT** /TeamMembers/{id}/team/builderConfigs/{fk} | Update a related item by id for builderConfigs.
[**team_members_id_team_builder_configs_fk_watermark_put**](TeamMemberApi.md#team_members_id_team_builder_configs_fk_watermark_put) | **PUT** /TeamMembers/{id}/team/builderConfigs/{fk}/watermark | Change Builder Config watermark
[**team_members_id_team_builder_configs_get**](TeamMemberApi.md#team_members_id_team_builder_configs_get) | **GET** /TeamMembers/{id}/team/builderConfigs | Queries builderConfigs of Team.
[**team_members_id_team_builder_configs_post**](TeamMemberApi.md#team_members_id_team_builder_configs_post) | **POST** /TeamMembers/{id}/team/builderConfigs | Creates a new instance in builderConfigs of this model.
[**team_members_id_team_data_record_get**](TeamMemberApi.md#team_members_id_team_data_record_get) | **GET** /TeamMembers/{id}/teamData/record | Get TeamData Record
[**team_members_id_team_data_record_post**](TeamMemberApi.md#team_members_id_team_data_record_post) | **POST** /TeamMembers/{id}/teamData/record | Create TeamData Record
[**team_members_id_team_data_record_put**](TeamMemberApi.md#team_members_id_team_data_record_put) | **PUT** /TeamMembers/{id}/teamData/record | Update TeamData Record
[**team_members_id_team_data_sources_count_get**](TeamMemberApi.md#team_members_id_team_data_sources_count_get) | **GET** /TeamMembers/{id}/team/dataSources/count | Counts dataSources of Team.
[**team_members_id_team_data_sources_delete**](TeamMemberApi.md#team_members_id_team_data_sources_delete) | **DELETE** /TeamMembers/{id}/team/dataSources | Deletes all dataSources of this model.
[**team_members_id_team_data_sources_fk_delete**](TeamMemberApi.md#team_members_id_team_data_sources_fk_delete) | **DELETE** /TeamMembers/{id}/team/dataSources/{fk} | Delete a related item by id for dataSources.
[**team_members_id_team_data_sources_fk_get**](TeamMemberApi.md#team_members_id_team_data_sources_fk_get) | **GET** /TeamMembers/{id}/team/dataSources/{fk} | Find a related item by id for dataSources.
[**team_members_id_team_data_sources_fk_put**](TeamMemberApi.md#team_members_id_team_data_sources_fk_put) | **PUT** /TeamMembers/{id}/team/dataSources/{fk} | Update a related item by id for dataSources.
[**team_members_id_team_data_sources_get**](TeamMemberApi.md#team_members_id_team_data_sources_get) | **GET** /TeamMembers/{id}/team/dataSources | Queries dataSources of Team.
[**team_members_id_team_data_sources_post**](TeamMemberApi.md#team_members_id_team_data_sources_post) | **POST** /TeamMembers/{id}/team/dataSources | Creates a new instance in dataSources of this model.
[**team_members_id_team_dynamic_datas_count_get**](TeamMemberApi.md#team_members_id_team_dynamic_datas_count_get) | **GET** /TeamMembers/{id}/team/dynamicDatas/count | Counts dynamicDatas of Team.
[**team_members_id_team_dynamic_datas_delete**](TeamMemberApi.md#team_members_id_team_dynamic_datas_delete) | **DELETE** /TeamMembers/{id}/team/dynamicDatas | Deletes all dynamicDatas of this model.
[**team_members_id_team_dynamic_datas_fk_delete**](TeamMemberApi.md#team_members_id_team_dynamic_datas_fk_delete) | **DELETE** /TeamMembers/{id}/team/dynamicDatas/{fk} | Delete a related item by id for dynamicDatas.
[**team_members_id_team_dynamic_datas_fk_get**](TeamMemberApi.md#team_members_id_team_dynamic_datas_fk_get) | **GET** /TeamMembers/{id}/team/dynamicDatas/{fk} | Find a related item by id for dynamicDatas.
[**team_members_id_team_dynamic_datas_fk_put**](TeamMemberApi.md#team_members_id_team_dynamic_datas_fk_put) | **PUT** /TeamMembers/{id}/team/dynamicDatas/{fk} | Update a related item by id for dynamicDatas.
[**team_members_id_team_dynamic_datas_get**](TeamMemberApi.md#team_members_id_team_dynamic_datas_get) | **GET** /TeamMembers/{id}/team/dynamicDatas | Queries dynamicDatas of Team.
[**team_members_id_team_dynamic_datas_post**](TeamMemberApi.md#team_members_id_team_dynamic_datas_post) | **POST** /TeamMembers/{id}/team/dynamicDatas | Creates a new instance in dynamicDatas of this model.
[**team_members_id_team_get**](TeamMemberApi.md#team_members_id_team_get) | **GET** /TeamMembers/{id}/team | Fetches belongsTo relation team.
[**team_members_id_team_image_folders_count_get**](TeamMemberApi.md#team_members_id_team_image_folders_count_get) | **GET** /TeamMembers/{id}/team/imageFolders/count | Counts imageFolders of Team.
[**team_members_id_team_image_folders_delete**](TeamMemberApi.md#team_members_id_team_image_folders_delete) | **DELETE** /TeamMembers/{id}/team/imageFolders | Deletes all imageFolders of this model.
[**team_members_id_team_image_folders_fk_delete**](TeamMemberApi.md#team_members_id_team_image_folders_fk_delete) | **DELETE** /TeamMembers/{id}/team/imageFolders/{fk} | Delete a related item by id for imageFolders.
[**team_members_id_team_image_folders_fk_get**](TeamMemberApi.md#team_members_id_team_image_folders_fk_get) | **GET** /TeamMembers/{id}/team/imageFolders/{fk} | Find a related item by id for imageFolders.
[**team_members_id_team_image_folders_fk_put**](TeamMemberApi.md#team_members_id_team_image_folders_fk_put) | **PUT** /TeamMembers/{id}/team/imageFolders/{fk} | Update a related item by id for imageFolders.
[**team_members_id_team_image_folders_get**](TeamMemberApi.md#team_members_id_team_image_folders_get) | **GET** /TeamMembers/{id}/team/imageFolders | Queries imageFolders of Team.
[**team_members_id_team_image_folders_post**](TeamMemberApi.md#team_members_id_team_image_folders_post) | **POST** /TeamMembers/{id}/team/imageFolders | Creates a new instance in imageFolders of this model.
[**team_members_id_team_images_count_get**](TeamMemberApi.md#team_members_id_team_images_count_get) | **GET** /TeamMembers/{id}/team/images/count | Counts images of Team.
[**team_members_id_team_images_delete**](TeamMemberApi.md#team_members_id_team_images_delete) | **DELETE** /TeamMembers/{id}/team/images | Deletes all images of this model.
[**team_members_id_team_images_fk_delete**](TeamMemberApi.md#team_members_id_team_images_fk_delete) | **DELETE** /TeamMembers/{id}/team/images/{fk} | Delete a related item by id for images.
[**team_members_id_team_images_fk_get**](TeamMemberApi.md#team_members_id_team_images_fk_get) | **GET** /TeamMembers/{id}/team/images/{fk} | Find a related item by id for images.
[**team_members_id_team_images_fk_put**](TeamMemberApi.md#team_members_id_team_images_fk_put) | **PUT** /TeamMembers/{id}/team/images/{fk} | Update a related item by id for images.
[**team_members_id_team_images_get**](TeamMemberApi.md#team_members_id_team_images_get) | **GET** /TeamMembers/{id}/team/images | Queries images of Team.
[**team_members_id_team_images_post**](TeamMemberApi.md#team_members_id_team_images_post) | **POST** /TeamMembers/{id}/team/images | Creates a new instance in images of this model.
[**team_members_id_team_logo_put**](TeamMemberApi.md#team_members_id_team_logo_put) | **PUT** /TeamMembers/{id}/team/logo | Change Team logo
[**team_members_id_team_members_count_get**](TeamMemberApi.md#team_members_id_team_members_count_get) | **GET** /TeamMembers/{id}/team/members/count | Counts members of Team.
[**team_members_id_team_members_delete**](TeamMemberApi.md#team_members_id_team_members_delete) | **DELETE** /TeamMembers/{id}/team/members | Deletes all members of this model.
[**team_members_id_team_members_fk_delete**](TeamMemberApi.md#team_members_id_team_members_fk_delete) | **DELETE** /TeamMembers/{id}/team/members/{fk} | Delete a related item by id for members.
[**team_members_id_team_members_fk_get**](TeamMemberApi.md#team_members_id_team_members_fk_get) | **GET** /TeamMembers/{id}/team/members/{fk} | Find a related item by id for members.
[**team_members_id_team_members_fk_put**](TeamMemberApi.md#team_members_id_team_members_fk_put) | **PUT** /TeamMembers/{id}/team/members/{fk} | Update a related item by id for members.
[**team_members_id_team_members_get**](TeamMemberApi.md#team_members_id_team_members_get) | **GET** /TeamMembers/{id}/team/members | Queries members of Team.
[**team_members_id_team_members_post**](TeamMemberApi.md#team_members_id_team_members_post) | **POST** /TeamMembers/{id}/team/members | Creates a new instance in members of this model.
[**team_members_id_team_members_rel_fk_delete**](TeamMemberApi.md#team_members_id_team_members_rel_fk_delete) | **DELETE** /TeamMembers/{id}/team/members/rel/{fk} | Remove the members relation to an item by id.
[**team_members_id_team_members_rel_fk_head**](TeamMemberApi.md#team_members_id_team_members_rel_fk_head) | **HEAD** /TeamMembers/{id}/team/members/rel/{fk} | Check the existence of members relation to an item by id.
[**team_members_id_team_members_rel_fk_put**](TeamMemberApi.md#team_members_id_team_members_rel_fk_put) | **PUT** /TeamMembers/{id}/team/members/rel/{fk} | Add a related item by id for members.
[**team_members_id_team_permission_delete**](TeamMemberApi.md#team_members_id_team_permission_delete) | **DELETE** /TeamMembers/{id}/team/permission | Deletes permission of this model.
[**team_members_id_team_permission_get**](TeamMemberApi.md#team_members_id_team_permission_get) | **GET** /TeamMembers/{id}/team/permission | Fetches hasOne relation permission.
[**team_members_id_team_permission_post**](TeamMemberApi.md#team_members_id_team_permission_post) | **POST** /TeamMembers/{id}/team/permission | Creates a new instance in permission of this model.
[**team_members_id_team_permission_put**](TeamMemberApi.md#team_members_id_team_permission_put) | **PUT** /TeamMembers/{id}/team/permission | Update permission of this model.
[**team_members_id_team_portals_count_get**](TeamMemberApi.md#team_members_id_team_portals_count_get) | **GET** /TeamMembers/{id}/team/portals/count | Counts portals of Team.
[**team_members_id_team_portals_delete**](TeamMemberApi.md#team_members_id_team_portals_delete) | **DELETE** /TeamMembers/{id}/team/portals | Deletes all portals of this model.
[**team_members_id_team_portals_fk_delete**](TeamMemberApi.md#team_members_id_team_portals_fk_delete) | **DELETE** /TeamMembers/{id}/team/portals/{fk} | Delete a related item by id for portals.
[**team_members_id_team_portals_fk_get**](TeamMemberApi.md#team_members_id_team_portals_fk_get) | **GET** /TeamMembers/{id}/team/portals/{fk} | Find a related item by id for portals.
[**team_members_id_team_portals_fk_put**](TeamMemberApi.md#team_members_id_team_portals_fk_put) | **PUT** /TeamMembers/{id}/team/portals/{fk} | Update a related item by id for portals.
[**team_members_id_team_portals_get**](TeamMemberApi.md#team_members_id_team_portals_get) | **GET** /TeamMembers/{id}/team/portals | Queries portals of Team.
[**team_members_id_team_portals_post**](TeamMemberApi.md#team_members_id_team_portals_post) | **POST** /TeamMembers/{id}/team/portals | Creates a new instance in portals of this model.
[**team_members_id_team_product_materials_count_get**](TeamMemberApi.md#team_members_id_team_product_materials_count_get) | **GET** /TeamMembers/{id}/team/productMaterials/count | Counts productMaterials of Team.
[**team_members_id_team_product_materials_delete**](TeamMemberApi.md#team_members_id_team_product_materials_delete) | **DELETE** /TeamMembers/{id}/team/productMaterials | Deletes all productMaterials of this model.
[**team_members_id_team_product_materials_fk_delete**](TeamMemberApi.md#team_members_id_team_product_materials_fk_delete) | **DELETE** /TeamMembers/{id}/team/productMaterials/{fk} | Delete a related item by id for productMaterials.
[**team_members_id_team_product_materials_fk_get**](TeamMemberApi.md#team_members_id_team_product_materials_fk_get) | **GET** /TeamMembers/{id}/team/productMaterials/{fk} | Find a related item by id for productMaterials.
[**team_members_id_team_product_materials_fk_put**](TeamMemberApi.md#team_members_id_team_product_materials_fk_put) | **PUT** /TeamMembers/{id}/team/productMaterials/{fk} | Update a related item by id for productMaterials.
[**team_members_id_team_product_materials_get**](TeamMemberApi.md#team_members_id_team_product_materials_get) | **GET** /TeamMembers/{id}/team/productMaterials | Queries productMaterials of Team.
[**team_members_id_team_product_materials_post**](TeamMemberApi.md#team_members_id_team_product_materials_post) | **POST** /TeamMembers/{id}/team/productMaterials | Creates a new instance in productMaterials of this model.
[**team_members_id_team_product_pdf_color_profiles_available_get**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_available_get) | **GET** /TeamMembers/{id}/team/productPdfColorProfiles/available | Find all available PdfColorProfile
[**team_members_id_team_product_pdf_color_profiles_count_get**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_count_get) | **GET** /TeamMembers/{id}/team/productPdfColorProfiles/count | Counts productPdfColorProfiles of Team.
[**team_members_id_team_product_pdf_color_profiles_delete**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_delete) | **DELETE** /TeamMembers/{id}/team/productPdfColorProfiles | Deletes all productPdfColorProfiles of this model.
[**team_members_id_team_product_pdf_color_profiles_fk_delete**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_fk_delete) | **DELETE** /TeamMembers/{id}/team/productPdfColorProfiles/{fk} | Delete a related item by id for productPdfColorProfiles.
[**team_members_id_team_product_pdf_color_profiles_fk_get**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_fk_get) | **GET** /TeamMembers/{id}/team/productPdfColorProfiles/{fk} | Find a related item by id for productPdfColorProfiles.
[**team_members_id_team_product_pdf_color_profiles_fk_put**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_fk_put) | **PUT** /TeamMembers/{id}/team/productPdfColorProfiles/{fk} | Update a related item by id for productPdfColorProfiles.
[**team_members_id_team_product_pdf_color_profiles_get**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_get) | **GET** /TeamMembers/{id}/team/productPdfColorProfiles | Queries productPdfColorProfiles of Team.
[**team_members_id_team_product_pdf_color_profiles_upload_post**](TeamMemberApi.md#team_members_id_team_product_pdf_color_profiles_upload_post) | **POST** /TeamMembers/{id}/team/productPdfColorProfiles/upload | Upload ICC PDF Color Profile for this Team
[**team_members_id_team_product_size_materials_count_get**](TeamMemberApi.md#team_members_id_team_product_size_materials_count_get) | **GET** /TeamMembers/{id}/team/productSizeMaterials/count | Counts productSizeMaterials of Team.
[**team_members_id_team_product_size_materials_delete**](TeamMemberApi.md#team_members_id_team_product_size_materials_delete) | **DELETE** /TeamMembers/{id}/team/productSizeMaterials | Deletes all productSizeMaterials of this model.
[**team_members_id_team_product_size_materials_fk_delete**](TeamMemberApi.md#team_members_id_team_product_size_materials_fk_delete) | **DELETE** /TeamMembers/{id}/team/productSizeMaterials/{fk} | Delete a related item by id for productSizeMaterials.
[**team_members_id_team_product_size_materials_fk_get**](TeamMemberApi.md#team_members_id_team_product_size_materials_fk_get) | **GET** /TeamMembers/{id}/team/productSizeMaterials/{fk} | Find a related item by id for productSizeMaterials.
[**team_members_id_team_product_size_materials_fk_put**](TeamMemberApi.md#team_members_id_team_product_size_materials_fk_put) | **PUT** /TeamMembers/{id}/team/productSizeMaterials/{fk} | Update a related item by id for productSizeMaterials.
[**team_members_id_team_product_size_materials_get**](TeamMemberApi.md#team_members_id_team_product_size_materials_get) | **GET** /TeamMembers/{id}/team/productSizeMaterials | Queries productSizeMaterials of Team.
[**team_members_id_team_product_size_materials_post**](TeamMemberApi.md#team_members_id_team_product_size_materials_post) | **POST** /TeamMembers/{id}/team/productSizeMaterials | Creates a new instance in productSizeMaterials of this model.
[**team_members_id_team_team_data_get**](TeamMemberApi.md#team_members_id_team_team_data_get) | **GET** /TeamMembers/{id}/team/teamData | Fetches belongsTo relation teamData.
[**team_members_id_team_team_members_count_get**](TeamMemberApi.md#team_members_id_team_team_members_count_get) | **GET** /TeamMembers/{id}/team/teamMembers/count | Counts teamMembers of Team.
[**team_members_id_team_team_members_delete**](TeamMemberApi.md#team_members_id_team_team_members_delete) | **DELETE** /TeamMembers/{id}/team/teamMembers | Deletes all teamMembers of this model.
[**team_members_id_team_team_members_fk_delete**](TeamMemberApi.md#team_members_id_team_team_members_fk_delete) | **DELETE** /TeamMembers/{id}/team/teamMembers/{fk} | Delete a related item by id for teamMembers.
[**team_members_id_team_team_members_fk_get**](TeamMemberApi.md#team_members_id_team_team_members_fk_get) | **GET** /TeamMembers/{id}/team/teamMembers/{fk} | Find a related item by id for teamMembers.
[**team_members_id_team_team_members_fk_put**](TeamMemberApi.md#team_members_id_team_team_members_fk_put) | **PUT** /TeamMembers/{id}/team/teamMembers/{fk} | Update a related item by id for teamMembers.
[**team_members_id_team_team_members_get**](TeamMemberApi.md#team_members_id_team_team_members_get) | **GET** /TeamMembers/{id}/team/teamMembers | Queries teamMembers of Team.
[**team_members_id_team_team_members_post**](TeamMemberApi.md#team_members_id_team_team_members_post) | **POST** /TeamMembers/{id}/team/teamMembers | Creates a new instance in teamMembers of this model.
[**team_members_id_team_template_folders_count_get**](TeamMemberApi.md#team_members_id_team_template_folders_count_get) | **GET** /TeamMembers/{id}/team/templateFolders/count | Counts templateFolders of Team.
[**team_members_id_team_template_folders_delete**](TeamMemberApi.md#team_members_id_team_template_folders_delete) | **DELETE** /TeamMembers/{id}/team/templateFolders | Deletes all templateFolders of this model.
[**team_members_id_team_template_folders_fk_delete**](TeamMemberApi.md#team_members_id_team_template_folders_fk_delete) | **DELETE** /TeamMembers/{id}/team/templateFolders/{fk} | Delete a related item by id for templateFolders.
[**team_members_id_team_template_folders_fk_get**](TeamMemberApi.md#team_members_id_team_template_folders_fk_get) | **GET** /TeamMembers/{id}/team/templateFolders/{fk} | Find a related item by id for templateFolders.
[**team_members_id_team_template_folders_fk_put**](TeamMemberApi.md#team_members_id_team_template_folders_fk_put) | **PUT** /TeamMembers/{id}/team/templateFolders/{fk} | Update a related item by id for templateFolders.
[**team_members_id_team_template_folders_get**](TeamMemberApi.md#team_members_id_team_template_folders_get) | **GET** /TeamMembers/{id}/team/templateFolders | Queries templateFolders of Team.
[**team_members_id_team_template_folders_post**](TeamMemberApi.md#team_members_id_team_template_folders_post) | **POST** /TeamMembers/{id}/team/templateFolders | Creates a new instance in templateFolders of this model.
[**team_members_id_team_templates_count_get**](TeamMemberApi.md#team_members_id_team_templates_count_get) | **GET** /TeamMembers/{id}/team/templates/count | Counts templates of Team.
[**team_members_id_team_templates_delete**](TeamMemberApi.md#team_members_id_team_templates_delete) | **DELETE** /TeamMembers/{id}/team/templates | Deletes all templates of this model.
[**team_members_id_team_templates_fk_delete**](TeamMemberApi.md#team_members_id_team_templates_fk_delete) | **DELETE** /TeamMembers/{id}/team/templates/{fk} | Delete a related item by id for templates.
[**team_members_id_team_templates_fk_get**](TeamMemberApi.md#team_members_id_team_templates_fk_get) | **GET** /TeamMembers/{id}/team/templates/{fk} | Find a related item by id for templates.
[**team_members_id_team_templates_fk_put**](TeamMemberApi.md#team_members_id_team_templates_fk_put) | **PUT** /TeamMembers/{id}/team/templates/{fk} | Update a related item by id for templates.
[**team_members_id_team_templates_fk_url_review_get**](TeamMemberApi.md#team_members_id_team_templates_fk_url_review_get) | **GET** /TeamMembers/{id}/team/templates/{fk}/url/review | Get URL to review a Team Template
[**team_members_id_team_templates_get**](TeamMemberApi.md#team_members_id_team_templates_get) | **GET** /TeamMembers/{id}/team/templates | Queries templates of Team.
[**team_members_id_team_templates_post**](TeamMemberApi.md#team_members_id_team_templates_post) | **POST** /TeamMembers/{id}/team/templates | Creates a new instance in templates of this model.
[**team_members_id_team_templates_with_designs_get**](TeamMemberApi.md#team_members_id_team_templates_with_designs_get) | **GET** /TeamMembers/{id}/team/templatesWithDesigns | List Templates with Designs for the Team of TeamMember
[**team_members_id_team_workflows_count_get**](TeamMemberApi.md#team_members_id_team_workflows_count_get) | **GET** /TeamMembers/{id}/team/workflows/count | Counts workflows of Team.
[**team_members_id_team_workflows_delete**](TeamMemberApi.md#team_members_id_team_workflows_delete) | **DELETE** /TeamMembers/{id}/team/workflows | Deletes all workflows of this model.
[**team_members_id_team_workflows_fk_delete**](TeamMemberApi.md#team_members_id_team_workflows_fk_delete) | **DELETE** /TeamMembers/{id}/team/workflows/{fk} | Delete a related item by id for workflows.
[**team_members_id_team_workflows_fk_get**](TeamMemberApi.md#team_members_id_team_workflows_fk_get) | **GET** /TeamMembers/{id}/team/workflows/{fk} | Find a related item by id for workflows.
[**team_members_id_team_workflows_fk_put**](TeamMemberApi.md#team_members_id_team_workflows_fk_put) | **PUT** /TeamMembers/{id}/team/workflows/{fk} | Update a related item by id for workflows.
[**team_members_id_team_workflows_get**](TeamMemberApi.md#team_members_id_team_workflows_get) | **GET** /TeamMembers/{id}/team/workflows | Queries workflows of Team.
[**team_members_id_team_workflows_post**](TeamMemberApi.md#team_members_id_team_workflows_post) | **POST** /TeamMembers/{id}/team/workflows | Creates a new instance in workflows of this model.
[**team_members_id_templates_count_get**](TeamMemberApi.md#team_members_id_templates_count_get) | **GET** /TeamMembers/{id}/templates/count | Counts templates of TeamMember.
[**team_members_id_templates_delete**](TeamMemberApi.md#team_members_id_templates_delete) | **DELETE** /TeamMembers/{id}/templates | Deletes all templates of this model.
[**team_members_id_templates_fk_delete**](TeamMemberApi.md#team_members_id_templates_fk_delete) | **DELETE** /TeamMembers/{id}/templates/{fk} | Delete a related item by id for templates.
[**team_members_id_templates_fk_flashvars_get**](TeamMemberApi.md#team_members_id_templates_fk_flashvars_get) | **GET** /TeamMembers/{id}/templates/{fk}/flashvars | Find Template FlashVars by id
[**team_members_id_templates_fk_get**](TeamMemberApi.md#team_members_id_templates_fk_get) | **GET** /TeamMembers/{id}/templates/{fk} | Find a related item by id for templates.
[**team_members_id_templates_fk_put**](TeamMemberApi.md#team_members_id_templates_fk_put) | **PUT** /TeamMembers/{id}/templates/{fk} | Update a related item by id for templates.
[**team_members_id_templates_get**](TeamMemberApi.md#team_members_id_templates_get) | **GET** /TeamMembers/{id}/templates | Queries templates of TeamMember.
[**team_members_id_templates_post**](TeamMemberApi.md#team_members_id_templates_post) | **POST** /TeamMembers/{id}/templates | Creates a new instance in templates of this model.
[**team_members_id_templates_rel_fk_delete**](TeamMemberApi.md#team_members_id_templates_rel_fk_delete) | **DELETE** /TeamMembers/{id}/templates/rel/{fk} | Remove the templates relation to an item by id.
[**team_members_id_templates_rel_fk_head**](TeamMemberApi.md#team_members_id_templates_rel_fk_head) | **HEAD** /TeamMembers/{id}/templates/rel/{fk} | Check the existence of templates relation to an item by id.
[**team_members_id_templates_rel_fk_put**](TeamMemberApi.md#team_members_id_templates_rel_fk_put) | **PUT** /TeamMembers/{id}/templates/rel/{fk} | Add a related item by id for templates.
[**team_members_id_tweak_template_folders_get**](TeamMemberApi.md#team_members_id_tweak_template_folders_get) | **GET** /TeamMembers/{id}/tweakTemplateFolders | List Tweak Templates Folders
[**team_members_id_tweak_template_folders_nk_get**](TeamMemberApi.md#team_members_id_tweak_template_folders_nk_get) | **GET** /TeamMembers/{id}/tweakTemplateFolders/{nk} | Get Tweak Templates Folders details
[**team_members_id_tweak_template_folders_nk_templates_fk_get**](TeamMemberApi.md#team_members_id_tweak_template_folders_nk_templates_fk_get) | **GET** /TeamMembers/{id}/tweakTemplateFolders/{nk}/templates/{fk} | Get Tweak Template details within a Tweak Template Folder
[**team_members_id_tweak_template_folders_nk_templates_get**](TeamMemberApi.md#team_members_id_tweak_template_folders_nk_templates_get) | **GET** /TeamMembers/{id}/tweakTemplateFolders/{nk}/templates | List Tweak Templates within a Tweak Template Folder
[**team_members_id_tweak_templates_fk_flashvars_get**](TeamMemberApi.md#team_members_id_tweak_templates_fk_flashvars_get) | **GET** /TeamMembers/{id}/tweakTemplates/{fk}/flashvars | Find Template FlashVars by id
[**team_members_id_tweak_templates_fk_get**](TeamMemberApi.md#team_members_id_tweak_templates_fk_get) | **GET** /TeamMembers/{id}/tweakTemplates/{fk} | Get Tweak Template details
[**team_members_id_tweak_templates_get**](TeamMemberApi.md#team_members_id_tweak_templates_get) | **GET** /TeamMembers/{id}/tweakTemplates | List Tweak Templates
[**team_members_id_uploaded_templates_count_get**](TeamMemberApi.md#team_members_id_uploaded_templates_count_get) | **GET** /TeamMembers/{id}/uploadedTemplates/count | Counts uploadedTemplates of TeamMember.
[**team_members_id_uploaded_templates_delete**](TeamMemberApi.md#team_members_id_uploaded_templates_delete) | **DELETE** /TeamMembers/{id}/uploadedTemplates | Deletes all uploadedTemplates of this model.
[**team_members_id_uploaded_templates_fk_delete**](TeamMemberApi.md#team_members_id_uploaded_templates_fk_delete) | **DELETE** /TeamMembers/{id}/uploadedTemplates/{fk} | Delete a related item by id for uploadedTemplates.
[**team_members_id_uploaded_templates_fk_get**](TeamMemberApi.md#team_members_id_uploaded_templates_fk_get) | **GET** /TeamMembers/{id}/uploadedTemplates/{fk} | Find a related item by id for uploadedTemplates.
[**team_members_id_uploaded_templates_fk_put**](TeamMemberApi.md#team_members_id_uploaded_templates_fk_put) | **PUT** /TeamMembers/{id}/uploadedTemplates/{fk} | Update a related item by id for uploadedTemplates.
[**team_members_id_uploaded_templates_get**](TeamMemberApi.md#team_members_id_uploaded_templates_get) | **GET** /TeamMembers/{id}/uploadedTemplates | Queries uploadedTemplates of TeamMember.
[**team_members_id_uploaded_templates_post**](TeamMemberApi.md#team_members_id_uploaded_templates_post) | **POST** /TeamMembers/{id}/uploadedTemplates | Creates a new instance in uploadedTemplates of this model.
[**team_members_id_workflows_count_get**](TeamMemberApi.md#team_members_id_workflows_count_get) | **GET** /TeamMembers/{id}/workflows/count | Counts workflows of TeamMember.
[**team_members_id_workflows_delete**](TeamMemberApi.md#team_members_id_workflows_delete) | **DELETE** /TeamMembers/{id}/workflows | Deletes all workflows of this model.
[**team_members_id_workflows_fk_delete**](TeamMemberApi.md#team_members_id_workflows_fk_delete) | **DELETE** /TeamMembers/{id}/workflows/{fk} | Delete a related item by id for workflows.
[**team_members_id_workflows_fk_get**](TeamMemberApi.md#team_members_id_workflows_fk_get) | **GET** /TeamMembers/{id}/workflows/{fk} | Find a related item by id for workflows.
[**team_members_id_workflows_fk_put**](TeamMemberApi.md#team_members_id_workflows_fk_put) | **PUT** /TeamMembers/{id}/workflows/{fk} | Update a related item by id for workflows.
[**team_members_id_workflows_get**](TeamMemberApi.md#team_members_id_workflows_get) | **GET** /TeamMembers/{id}/workflows | Queries workflows of TeamMember.
[**team_members_id_workflows_post**](TeamMemberApi.md#team_members_id_workflows_post) | **POST** /TeamMembers/{id}/workflows | Creates a new instance in workflows of this model.
[**team_members_patch**](TeamMemberApi.md#team_members_patch) | **PATCH** /TeamMembers | Patch an existing model instance or insert a new one into the data source.
[**team_members_post**](TeamMemberApi.md#team_members_post) | **POST** /TeamMembers | Create a new instance of the model and persist it into the data source.
[**team_members_put**](TeamMemberApi.md#team_members_put) | **PUT** /TeamMembers | Replace an existing model instance or insert a new one into the data source.
[**team_members_replace_or_create_post**](TeamMemberApi.md#team_members_replace_or_create_post) | **POST** /TeamMembers/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**team_members_update_post**](TeamMemberApi.md#team_members_update_post) | **POST** /TeamMembers/update | Update instances of the model matched by {{where}} from the data source.
[**team_members_upsert_with_where_post**](TeamMemberApi.md#team_members_upsert_with_where_post) | **POST** /TeamMembers/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **team_members_change_stream_get**
> file team_members_change_stream_get(options=options)

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
api_instance = TweakApi.TeamMemberApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_members_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_change_stream_get: %s\n" % e)
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

# **team_members_change_stream_post**
> file team_members_change_stream_post(options=options)

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
api_instance = TweakApi.TeamMemberApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.team_members_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_change_stream_post: %s\n" % e)
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

# **team_members_count_get**
> InlineResponse2001 team_members_count_get(where=where)

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
api_instance = TweakApi.TeamMemberApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.team_members_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_count_get: %s\n" % e)
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

# **team_members_find_one_get**
> TeamMember team_members_find_one_get(filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.team_members_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_get**
> list[TeamMember] team_members_get(filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.team_members_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_assigned_designs_count_get**
> InlineResponse2001 team_members_id_assigned_designs_count_get(id, where=where)

Counts assignedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts assignedDesigns of TeamMember.
    api_response = api_instance.team_members_id_assigned_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_assigned_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_assigned_designs_delete**
> team_members_id_assigned_designs_delete(id)

Deletes all assignedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all assignedDesigns of this model.
    api_instance.team_members_id_assigned_designs_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_assigned_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_assigned_designs_fk_delete**
> team_members_id_assigned_designs_fk_delete(id, fk)

Delete a related item by id for assignedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for assignedDesigns

try: 
    # Delete a related item by id for assignedDesigns.
    api_instance.team_members_id_assigned_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_assigned_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for assignedDesigns | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_assigned_designs_fk_get**
> Design team_members_id_assigned_designs_fk_get(id, fk)

Find a related item by id for assignedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for assignedDesigns

try: 
    # Find a related item by id for assignedDesigns.
    api_response = api_instance.team_members_id_assigned_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_assigned_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for assignedDesigns | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_assigned_designs_fk_put**
> Design team_members_id_assigned_designs_fk_put(id, fk, data=data)

Update a related item by id for assignedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for assignedDesigns
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for assignedDesigns.
    api_response = api_instance.team_members_id_assigned_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_assigned_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for assignedDesigns | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_assigned_designs_get**
> list[Design] team_members_id_assigned_designs_get(id, filter=filter)

Queries assignedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries assignedDesigns of TeamMember.
    api_response = api_instance.team_members_id_assigned_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_assigned_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_assigned_designs_post**
> Design team_members_id_assigned_designs_post(id, data=data)

Creates a new instance in assignedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in assignedDesigns of this model.
    api_response = api_instance.team_members_id_assigned_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_assigned_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_count_get**
> InlineResponse2001 team_members_id_commented_designs_count_get(id, where=where)

Counts commentedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts commentedDesigns of TeamMember.
    api_response = api_instance.team_members_id_commented_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_delete**
> team_members_id_commented_designs_delete(id)

Deletes all commentedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all commentedDesigns of this model.
    api_instance.team_members_id_commented_designs_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_fk_delete**
> team_members_id_commented_designs_fk_delete(id, fk)

Delete a related item by id for commentedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for commentedDesigns

try: 
    # Delete a related item by id for commentedDesigns.
    api_instance.team_members_id_commented_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for commentedDesigns | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_fk_get**
> Design team_members_id_commented_designs_fk_get(id, fk)

Find a related item by id for commentedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for commentedDesigns

try: 
    # Find a related item by id for commentedDesigns.
    api_response = api_instance.team_members_id_commented_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for commentedDesigns | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_fk_put**
> Design team_members_id_commented_designs_fk_put(id, fk, data=data)

Update a related item by id for commentedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for commentedDesigns
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for commentedDesigns.
    api_response = api_instance.team_members_id_commented_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for commentedDesigns | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_get**
> list[Design] team_members_id_commented_designs_get(id, filter=filter)

Queries commentedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries commentedDesigns of TeamMember.
    api_response = api_instance.team_members_id_commented_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_post**
> Design team_members_id_commented_designs_post(id, data=data)

Creates a new instance in commentedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in commentedDesigns of this model.
    api_response = api_instance.team_members_id_commented_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_rel_fk_delete**
> team_members_id_commented_designs_rel_fk_delete(id, fk)

Remove the commentedDesigns relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for commentedDesigns

try: 
    # Remove the commentedDesigns relation to an item by id.
    api_instance.team_members_id_commented_designs_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for commentedDesigns | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_rel_fk_head**
> bool team_members_id_commented_designs_rel_fk_head(id, fk)

Check the existence of commentedDesigns relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for commentedDesigns

try: 
    # Check the existence of commentedDesigns relation to an item by id.
    api_response = api_instance.team_members_id_commented_designs_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for commentedDesigns | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_commented_designs_rel_fk_put**
> DesignComment team_members_id_commented_designs_rel_fk_put(id, fk, data=data)

Add a related item by id for commentedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for commentedDesigns
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Add a related item by id for commentedDesigns.
    api_response = api_instance.team_members_id_commented_designs_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_commented_designs_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for commentedDesigns | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_customer_get**
> Customer team_members_id_customer_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation customer.
    api_response = api_instance.team_members_id_customer_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_customer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_delete**
> object team_members_id_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.team_members_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_delete: %s\n" % e)
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

# **team_members_id_design_comments_count_get**
> InlineResponse2001 team_members_id_design_comments_count_get(id, where=where)

Counts designComments of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designComments of TeamMember.
    api_response = api_instance.team_members_id_design_comments_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_comments_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_comments_delete**
> team_members_id_design_comments_delete(id)

Deletes all designComments of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all designComments of this model.
    api_instance.team_members_id_design_comments_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_comments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_comments_fk_delete**
> team_members_id_design_comments_fk_delete(id, fk)

Delete a related item by id for designComments.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designComments

try: 
    # Delete a related item by id for designComments.
    api_instance.team_members_id_design_comments_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_comments_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designComments | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_comments_fk_get**
> DesignComment team_members_id_design_comments_fk_get(id, fk)

Find a related item by id for designComments.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designComments

try: 
    # Find a related item by id for designComments.
    api_response = api_instance.team_members_id_design_comments_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_comments_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designComments | 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_comments_fk_put**
> DesignComment team_members_id_design_comments_fk_put(id, fk, data=data)

Update a related item by id for designComments.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designComments
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Update a related item by id for designComments.
    api_response = api_instance.team_members_id_design_comments_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_comments_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designComments | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_comments_get**
> list[DesignComment] team_members_id_design_comments_get(id, filter=filter)

Queries designComments of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designComments of TeamMember.
    api_response = api_instance.team_members_id_design_comments_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignComment]**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_comments_post**
> DesignComment team_members_id_design_comments_post(id, data=data)

Creates a new instance in designComments of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.DesignComment() # DesignComment |  (optional)

try: 
    # Creates a new instance in designComments of this model.
    api_response = api_instance.team_members_id_design_comments_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**DesignComment**](DesignComment.md)|  | [optional] 

### Return type

[**DesignComment**](DesignComment.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_folders_count_get**
> InlineResponse2001 team_members_id_design_folders_count_get(id, where=where)

Counts designFolders of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designFolders of TeamMember.
    api_response = api_instance.team_members_id_design_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_folders_delete**
> team_members_id_design_folders_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all designFolders of this model.
    api_instance.team_members_id_design_folders_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_folders_fk_delete**
> team_members_id_design_folders_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designFolders

try: 
    # Delete a related item by id for designFolders.
    api_instance.team_members_id_design_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_folders_fk_get**
> DesignFolder team_members_id_design_folders_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designFolders

try: 
    # Find a related item by id for designFolders.
    api_response = api_instance.team_members_id_design_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designFolders | 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_folders_fk_put**
> DesignFolder team_members_id_design_folders_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designFolders
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Update a related item by id for designFolders.
    api_response = api_instance.team_members_id_design_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_design_folders_get**
> list[DesignFolder] team_members_id_design_folders_get(id, filter=filter)

Queries designFolders of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designFolders of TeamMember.
    api_response = api_instance.team_members_id_design_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignFolder]**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_folders_post**
> DesignFolder team_members_id_design_folders_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.DesignFolder() # DesignFolder |  (optional)

try: 
    # Creates a new instance in designFolders of this model.
    api_response = api_instance.team_members_id_design_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**DesignFolder**](DesignFolder.md)|  | [optional] 

### Return type

[**DesignFolder**](DesignFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_shares_count_get**
> InlineResponse2001 team_members_id_design_shares_count_get(id, where=where)

Counts designShares of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designShares of TeamMember.
    api_response = api_instance.team_members_id_design_shares_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_shares_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_shares_delete**
> team_members_id_design_shares_delete(id)

Deletes all designShares of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all designShares of this model.
    api_instance.team_members_id_design_shares_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_shares_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_shares_fk_delete**
> team_members_id_design_shares_fk_delete(id, fk)

Delete a related item by id for designShares.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designShares

try: 
    # Delete a related item by id for designShares.
    api_instance.team_members_id_design_shares_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_shares_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designShares | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_shares_fk_get**
> DesignMember team_members_id_design_shares_fk_get(id, fk)

Find a related item by id for designShares.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designShares

try: 
    # Find a related item by id for designShares.
    api_response = api_instance.team_members_id_design_shares_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_shares_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designShares | 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_shares_fk_put**
> DesignMember team_members_id_design_shares_fk_put(id, fk, data=data)

Update a related item by id for designShares.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for designShares
data = TweakApi.DesignMember() # DesignMember |  (optional)

try: 
    # Update a related item by id for designShares.
    api_response = api_instance.team_members_id_design_shares_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_shares_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for designShares | 
 **data** | [**DesignMember**](DesignMember.md)|  | [optional] 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_shares_get**
> list[DesignMember] team_members_id_design_shares_get(id, filter=filter)

Queries designShares of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designShares of TeamMember.
    api_response = api_instance.team_members_id_design_shares_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_shares_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignMember]**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_design_shares_post**
> DesignMember team_members_id_design_shares_post(id, data=data)

Creates a new instance in designShares of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.DesignMember() # DesignMember |  (optional)

try: 
    # Creates a new instance in designShares of this model.
    api_response = api_instance.team_members_id_design_shares_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_design_shares_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**DesignMember**](DesignMember.md)|  | [optional] 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_exists_get**
> InlineResponse2002 team_members_id_exists_get(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_members_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_exists_get: %s\n" % e)
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

# **team_members_id_get**
> TeamMember team_members_id_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.team_members_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_head**
> InlineResponse2002 team_members_id_head(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.team_members_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_head: %s\n" % e)
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

# **team_members_id_image_folders_count_get**
> InlineResponse2001 team_members_id_image_folders_count_get(id, where=where)

Counts imageFolders of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts imageFolders of TeamMember.
    api_response = api_instance.team_members_id_image_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_delete**
> team_members_id_image_folders_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all imageFolders of this model.
    api_instance.team_members_id_image_folders_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_fk_delete**
> team_members_id_image_folders_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Delete a related item by id for imageFolders.
    api_instance.team_members_id_image_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_fk_get**
> ImageFolder team_members_id_image_folders_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Find a related item by id for imageFolders.
    api_response = api_instance.team_members_id_image_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_fk_put**
> ImageFolder team_members_id_image_folders_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for imageFolders.
    api_response = api_instance.team_members_id_image_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_image_folders_get**
> list[ImageFolder] team_members_id_image_folders_get(id, filter=filter)

Queries imageFolders of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries imageFolders of TeamMember.
    api_response = api_instance.team_members_id_image_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_post**
> ImageFolder team_members_id_image_folders_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in imageFolders of this model.
    api_response = api_instance.team_members_id_image_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_rel_fk_delete**
> team_members_id_image_folders_rel_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Remove the imageFolders relation to an item by id.
    api_instance.team_members_id_image_folders_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_rel_fk_head**
> bool team_members_id_image_folders_rel_fk_head(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Check the existence of imageFolders relation to an item by id.
    api_response = api_instance.team_members_id_image_folders_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_image_folders_rel_fk_put**
> ImageFolderMember team_members_id_image_folders_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.ImageFolderMember() # ImageFolderMember |  (optional)

try: 
    # Add a related item by id for imageFolders.
    api_response = api_instance.team_members_id_image_folders_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_image_folders_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for imageFolders | 
 **data** | [**ImageFolderMember**](ImageFolderMember.md)|  | [optional] 

### Return type

[**ImageFolderMember**](ImageFolderMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invitation_tickets_count_get**
> InlineResponse2001 team_members_id_invitation_tickets_count_get(id, where=where)

Counts invitationTickets of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts invitationTickets of TeamMember.
    api_response = api_instance.team_members_id_invitation_tickets_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invitation_tickets_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invitation_tickets_delete**
> team_members_id_invitation_tickets_delete(id)

Deletes all invitationTickets of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all invitationTickets of this model.
    api_instance.team_members_id_invitation_tickets_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invitation_tickets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invitation_tickets_fk_delete**
> team_members_id_invitation_tickets_fk_delete(id, fk)

Delete a related item by id for invitationTickets.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for invitationTickets

try: 
    # Delete a related item by id for invitationTickets.
    api_instance.team_members_id_invitation_tickets_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invitation_tickets_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for invitationTickets | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invitation_tickets_fk_get**
> InvitationTicket team_members_id_invitation_tickets_fk_get(id, fk)

Find a related item by id for invitationTickets.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for invitationTickets

try: 
    # Find a related item by id for invitationTickets.
    api_response = api_instance.team_members_id_invitation_tickets_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invitation_tickets_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for invitationTickets | 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invitation_tickets_fk_put**
> InvitationTicket team_members_id_invitation_tickets_fk_put(id, fk, data=data)

Update a related item by id for invitationTickets.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for invitationTickets
data = TweakApi.InvitationTicket() # InvitationTicket |  (optional)

try: 
    # Update a related item by id for invitationTickets.
    api_response = api_instance.team_members_id_invitation_tickets_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invitation_tickets_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for invitationTickets | 
 **data** | [**InvitationTicket**](InvitationTicket.md)|  | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invitation_tickets_get**
> list[InvitationTicket] team_members_id_invitation_tickets_get(id, filter=filter)

Queries invitationTickets of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries invitationTickets of TeamMember.
    api_response = api_instance.team_members_id_invitation_tickets_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invitation_tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invitation_tickets_post**
> InvitationTicket team_members_id_invitation_tickets_post(id, data=data)

Creates a new instance in invitationTickets of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.InvitationTicket() # InvitationTicket |  (optional)

try: 
    # Creates a new instance in invitationTickets of this model.
    api_response = api_instance.team_members_id_invitation_tickets_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invitation_tickets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**InvitationTicket**](InvitationTicket.md)|  | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_invite_invitee_post**
> InvitationTicket team_members_id_invite_invitee_post(id, id2, invitee, data=data)

Invite somebody to join the team

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
invitee = 'invitee_example' # str | 
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Invite somebody to join the team
    api_response = api_instance.team_members_id_invite_invitee_post(id, id2, invitee, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_invite_invitee_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **invitee** | **str**|  | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_notifications_count_get**
> InlineResponse2001 team_members_id_notifications_count_get(id, where=where)

Counts notifications of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts notifications of TeamMember.
    api_response = api_instance.team_members_id_notifications_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_notifications_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_notifications_delete**
> team_members_id_notifications_delete(id)

Deletes all notifications of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all notifications of this model.
    api_instance.team_members_id_notifications_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_notifications_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_notifications_fk_delete**
> team_members_id_notifications_fk_delete(id, fk)

Delete a related item by id for notifications.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for notifications

try: 
    # Delete a related item by id for notifications.
    api_instance.team_members_id_notifications_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_notifications_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for notifications | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_notifications_fk_get**
> Notification team_members_id_notifications_fk_get(id, fk)

Find a related item by id for notifications.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for notifications

try: 
    # Find a related item by id for notifications.
    api_response = api_instance.team_members_id_notifications_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_notifications_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for notifications | 

### Return type

[**Notification**](Notification.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_notifications_fk_put**
> Notification team_members_id_notifications_fk_put(id, fk, data=data)

Update a related item by id for notifications.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for notifications
data = TweakApi.Notification() # Notification |  (optional)

try: 
    # Update a related item by id for notifications.
    api_response = api_instance.team_members_id_notifications_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_notifications_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for notifications | 
 **data** | [**Notification**](Notification.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_notifications_get**
> list[Notification] team_members_id_notifications_get(id, filter=filter)

Queries notifications of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries notifications of TeamMember.
    api_response = api_instance.team_members_id_notifications_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_notifications_post**
> Notification team_members_id_notifications_post(id, data=data)

Creates a new instance in notifications of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Notification() # Notification |  (optional)

try: 
    # Creates a new instance in notifications of this model.
    api_response = api_instance.team_members_id_notifications_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_notifications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Notification**](Notification.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_patch**
> TeamMember team_members_id_patch(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_members_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_available_get**
> list[Portal] team_members_id_portals_available_get(id, id2, filter=filter)

Find all available Portals

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all available Portals
    api_response = api_instance.team_members_id_portals_available_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_count_get**
> InlineResponse2001 team_members_id_portals_count_get(id, where=where)

Counts portals of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of TeamMember.
    api_response = api_instance.team_members_id_portals_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_delete**
> team_members_id_portals_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all portals of this model.
    api_instance.team_members_id_portals_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_fk_available_get**
> Portal team_members_id_portals_fk_available_get(id, id2, fk, include=include)

Find available Portal by id

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
fk = 'fk_example' # str | 
include = 'include_example' # str | Only include changes that match this filter (optional)

try: 
    # Find available Portal by id
    api_response = api_instance.team_members_id_portals_fk_available_get(id, id2, fk, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_fk_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **fk** | **str**|  | 
 **include** | **str**| Only include changes that match this filter | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_fk_delete**
> team_members_id_portals_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.team_members_id_portals_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_fk_get**
> Portal team_members_id_portals_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.team_members_id_portals_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_fk_logo_put**
> Portal team_members_id_portals_fk_logo_put(id, id2, fk, data)

Change Portal logo

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Portal id
data = TweakApi.TeamMember() # TeamMember | Logo

try: 
    # Change Portal logo
    api_response = api_instance.team_members_id_portals_fk_logo_put(id, id2, fk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_fk_logo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **fk** | **str**| Portal id | 
 **data** | [**TeamMember**](TeamMember.md)| Logo | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_fk_put**
> Portal team_members_id_portals_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.team_members_id_portals_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_portals_get**
> list[Portal] team_members_id_portals_get(id, filter=filter)

Queries portals of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of TeamMember.
    api_response = api_instance.team_members_id_portals_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_nk_designs_fk_flashvars_get**
> FlashVar team_members_id_portals_nk_designs_fk_flashvars_get(id, id2, nk, fk)

Find Design FlashVars within available Portal by id

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
nk = 'nk_example' # str | 
fk = 'fk_example' # str | 

try: 
    # Find Design FlashVars within available Portal by id
    api_response = api_instance.team_members_id_portals_nk_designs_fk_flashvars_get(id, id2, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_nk_designs_fk_flashvars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **nk** | **str**|  | 
 **fk** | **str**|  | 

### Return type

[**FlashVar**](FlashVar.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_nk_templates_fk_flashvars_get**
> FlashVar team_members_id_portals_nk_templates_fk_flashvars_get(id, id2, nk, fk)

Find Template FlashVars within available Portal by id

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
nk = 'nk_example' # str | 
fk = 'fk_example' # str | 

try: 
    # Find Template FlashVars within available Portal by id
    api_response = api_instance.team_members_id_portals_nk_templates_fk_flashvars_get(id, id2, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_nk_templates_fk_flashvars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **nk** | **str**|  | 
 **fk** | **str**|  | 

### Return type

[**FlashVar**](FlashVar.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_post**
> Portal team_members_id_portals_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.team_members_id_portals_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_rel_fk_delete**
> team_members_id_portals_rel_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Remove the portals relation to an item by id.
    api_instance.team_members_id_portals_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_rel_fk_head**
> bool team_members_id_portals_rel_fk_head(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Check the existence of portals relation to an item by id.
    api_response = api_instance.team_members_id_portals_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_portals_rel_fk_put**
> PortalMember team_members_id_portals_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.PortalMember() # PortalMember |  (optional)

try: 
    # Add a related item by id for portals.
    api_response = api_instance.team_members_id_portals_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_portals_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for portals | 
 **data** | [**PortalMember**](PortalMember.md)|  | [optional] 

### Return type

[**PortalMember**](PortalMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_put**
> TeamMember team_members_id_put(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_members_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_replace_post**
> TeamMember team_members_id_replace_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | Model id
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.team_members_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_design_exports_count_get**
> InlineResponse2001 team_members_id_requested_design_exports_count_get(id, where=where)

Counts requestedDesignExports of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts requestedDesignExports of TeamMember.
    api_response = api_instance.team_members_id_requested_design_exports_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_design_exports_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_design_exports_delete**
> team_members_id_requested_design_exports_delete(id)

Deletes all requestedDesignExports of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all requestedDesignExports of this model.
    api_instance.team_members_id_requested_design_exports_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_design_exports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_design_exports_fk_delete**
> team_members_id_requested_design_exports_fk_delete(id, fk)

Delete a related item by id for requestedDesignExports.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for requestedDesignExports

try: 
    # Delete a related item by id for requestedDesignExports.
    api_instance.team_members_id_requested_design_exports_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_design_exports_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for requestedDesignExports | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_design_exports_fk_get**
> DesignExport team_members_id_requested_design_exports_fk_get(id, fk)

Find a related item by id for requestedDesignExports.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for requestedDesignExports

try: 
    # Find a related item by id for requestedDesignExports.
    api_response = api_instance.team_members_id_requested_design_exports_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_design_exports_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for requestedDesignExports | 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_design_exports_fk_put**
> DesignExport team_members_id_requested_design_exports_fk_put(id, fk, data=data)

Update a related item by id for requestedDesignExports.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for requestedDesignExports
data = TweakApi.DesignExport() # DesignExport |  (optional)

try: 
    # Update a related item by id for requestedDesignExports.
    api_response = api_instance.team_members_id_requested_design_exports_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_design_exports_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for requestedDesignExports | 
 **data** | [**DesignExport**](DesignExport.md)|  | [optional] 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_design_exports_get**
> list[DesignExport] team_members_id_requested_design_exports_get(id, filter=filter)

Queries requestedDesignExports of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries requestedDesignExports of TeamMember.
    api_response = api_instance.team_members_id_requested_design_exports_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_design_exports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DesignExport]**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_design_exports_post**
> DesignExport team_members_id_requested_design_exports_post(id, data=data)

Creates a new instance in requestedDesignExports of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.DesignExport() # DesignExport |  (optional)

try: 
    # Creates a new instance in requestedDesignExports of this model.
    api_response = api_instance.team_members_id_requested_design_exports_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_design_exports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**DesignExport**](DesignExport.md)|  | [optional] 

### Return type

[**DesignExport**](DesignExport.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_designs_count_get**
> InlineResponse2001 team_members_id_requested_designs_count_get(id, where=where)

Counts requestedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts requestedDesigns of TeamMember.
    api_response = api_instance.team_members_id_requested_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_designs_delete**
> team_members_id_requested_designs_delete(id)

Deletes all requestedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all requestedDesigns of this model.
    api_instance.team_members_id_requested_designs_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_designs_fk_delete**
> team_members_id_requested_designs_fk_delete(id, fk)

Delete a related item by id for requestedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for requestedDesigns

try: 
    # Delete a related item by id for requestedDesigns.
    api_instance.team_members_id_requested_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for requestedDesigns | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_designs_fk_get**
> Design team_members_id_requested_designs_fk_get(id, fk)

Find a related item by id for requestedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for requestedDesigns

try: 
    # Find a related item by id for requestedDesigns.
    api_response = api_instance.team_members_id_requested_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for requestedDesigns | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_designs_fk_put**
> Design team_members_id_requested_designs_fk_put(id, fk, data=data)

Update a related item by id for requestedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for requestedDesigns
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for requestedDesigns.
    api_response = api_instance.team_members_id_requested_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for requestedDesigns | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_designs_get**
> list[Design] team_members_id_requested_designs_get(id, filter=filter)

Queries requestedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries requestedDesigns of TeamMember.
    api_response = api_instance.team_members_id_requested_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_requested_designs_post**
> Design team_members_id_requested_designs_post(id, data=data)

Creates a new instance in requestedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in requestedDesigns of this model.
    api_response = api_instance.team_members_id_requested_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_requested_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_reviewed_designs_count_get**
> InlineResponse2001 team_members_id_reviewed_designs_count_get(id, where=where)

Counts reviewedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts reviewedDesigns of TeamMember.
    api_response = api_instance.team_members_id_reviewed_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_reviewed_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_reviewed_designs_delete**
> team_members_id_reviewed_designs_delete(id)

Deletes all reviewedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all reviewedDesigns of this model.
    api_instance.team_members_id_reviewed_designs_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_reviewed_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_reviewed_designs_fk_delete**
> team_members_id_reviewed_designs_fk_delete(id, fk)

Delete a related item by id for reviewedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for reviewedDesigns

try: 
    # Delete a related item by id for reviewedDesigns.
    api_instance.team_members_id_reviewed_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_reviewed_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for reviewedDesigns | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_reviewed_designs_fk_get**
> Design team_members_id_reviewed_designs_fk_get(id, fk)

Find a related item by id for reviewedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for reviewedDesigns

try: 
    # Find a related item by id for reviewedDesigns.
    api_response = api_instance.team_members_id_reviewed_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_reviewed_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for reviewedDesigns | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_reviewed_designs_fk_put**
> Design team_members_id_reviewed_designs_fk_put(id, fk, data=data)

Update a related item by id for reviewedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for reviewedDesigns
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for reviewedDesigns.
    api_response = api_instance.team_members_id_reviewed_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_reviewed_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for reviewedDesigns | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_reviewed_designs_get**
> list[Design] team_members_id_reviewed_designs_get(id, filter=filter)

Queries reviewedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries reviewedDesigns of TeamMember.
    api_response = api_instance.team_members_id_reviewed_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_reviewed_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_reviewed_designs_post**
> Design team_members_id_reviewed_designs_post(id, data=data)

Creates a new instance in reviewedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in reviewedDesigns of this model.
    api_response = api_instance.team_members_id_reviewed_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_reviewed_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_count_get**
> InlineResponse2001 team_members_id_shared_designs_count_get(id, where=where)

Counts sharedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts sharedDesigns of TeamMember.
    api_response = api_instance.team_members_id_shared_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_delete**
> team_members_id_shared_designs_delete(id)

Deletes all sharedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all sharedDesigns of this model.
    api_instance.team_members_id_shared_designs_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_fk_delete**
> team_members_id_shared_designs_fk_delete(id, fk)

Delete a related item by id for sharedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for sharedDesigns

try: 
    # Delete a related item by id for sharedDesigns.
    api_instance.team_members_id_shared_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for sharedDesigns | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_fk_get**
> Design team_members_id_shared_designs_fk_get(id, fk)

Find a related item by id for sharedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for sharedDesigns

try: 
    # Find a related item by id for sharedDesigns.
    api_response = api_instance.team_members_id_shared_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for sharedDesigns | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_fk_put**
> Design team_members_id_shared_designs_fk_put(id, fk, data=data)

Update a related item by id for sharedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for sharedDesigns
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for sharedDesigns.
    api_response = api_instance.team_members_id_shared_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for sharedDesigns | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_get**
> list[Design] team_members_id_shared_designs_get(id, filter=filter)

Queries sharedDesigns of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries sharedDesigns of TeamMember.
    api_response = api_instance.team_members_id_shared_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_post**
> Design team_members_id_shared_designs_post(id, data=data)

Creates a new instance in sharedDesigns of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in sharedDesigns of this model.
    api_response = api_instance.team_members_id_shared_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_rel_fk_delete**
> team_members_id_shared_designs_rel_fk_delete(id, fk)

Remove the sharedDesigns relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for sharedDesigns

try: 
    # Remove the sharedDesigns relation to an item by id.
    api_instance.team_members_id_shared_designs_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for sharedDesigns | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_rel_fk_head**
> bool team_members_id_shared_designs_rel_fk_head(id, fk)

Check the existence of sharedDesigns relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for sharedDesigns

try: 
    # Check the existence of sharedDesigns relation to an item by id.
    api_response = api_instance.team_members_id_shared_designs_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for sharedDesigns | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_shared_designs_rel_fk_put**
> DesignMember team_members_id_shared_designs_rel_fk_put(id, fk, data=data)

Add a related item by id for sharedDesigns.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for sharedDesigns
data = TweakApi.DesignMember() # DesignMember |  (optional)

try: 
    # Add a related item by id for sharedDesigns.
    api_response = api_instance.team_members_id_shared_designs_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_shared_designs_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for sharedDesigns | 
 **data** | [**DesignMember**](DesignMember.md)|  | [optional] 

### Return type

[**DesignMember**](DesignMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_target_model_target_id_invite_invitee_post**
> InvitationTicket team_members_id_target_model_target_id_invite_invitee_post(id, id2, target_model, target_id, invitee, data=data)

Invite somebody to join a team, portal or other targets

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
target_model = 'target_model_example' # str | 
target_id = 'target_id_example' # str | 
invitee = 'invitee_example' # str | 
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Invite somebody to join a team, portal or other targets
    api_response = api_instance.team_members_id_target_model_target_id_invite_invitee_post(id, id2, target_model, target_id, invitee, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_target_model_target_id_invite_invitee_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **target_model** | **str**|  | 
 **target_id** | **str**|  | 
 **invitee** | **str**|  | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_target_model_target_id_invite_post**
> list[InvitationTicket] team_members_id_target_model_target_id_invite_post(id, id2, target_model, target_id, data=data)

Invite a group of people to join a team, portal or other targets

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
target_model = 'target_model_example' # str | 
target_id = 'target_id_example' # str | 
data = [TweakApi.list[object]()] # list[object] |  (optional)

try: 
    # Invite a group of people to join a team, portal or other targets
    api_response = api_instance.team_members_id_target_model_target_id_invite_post(id, id2, target_model, target_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_target_model_target_id_invite_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **target_model** | **str**|  | 
 **target_id** | **str**|  | 
 **data** | **list[object]**|  | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_available_plans_get**
> list[BillingPlan] team_members_id_team_billing_available_plans_get(id, filter=filter)

Get Available Plans

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Get Available Plans
    api_response = api_instance.team_members_id_team_billing_available_plans_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_available_plans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[BillingPlan]**](BillingPlan.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_cached_get**
> Billing team_members_id_team_billing_cached_get(id)

Get Cached version of Team Billing

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Get Cached version of Team Billing
    api_response = api_instance.team_members_id_team_billing_cached_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_cached_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

[**Billing**](Billing.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_card_delete**
> Billing team_members_id_team_billing_card_delete(id)

Delete Team Billing Card

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Delete Team Billing Card
    api_response = api_instance.team_members_id_team_billing_card_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_card_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

[**Billing**](Billing.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_card_post**
> Billing team_members_id_team_billing_card_post(id, data=data)

Create Team Billing Card

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Create Team Billing Card
    api_response = api_instance.team_members_id_team_billing_card_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_card_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**Billing**](Billing.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_card_put**
> Billing team_members_id_team_billing_card_put(id, data=data)

Update Team Billing Card

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update Team Billing Card
    api_response = api_instance.team_members_id_team_billing_card_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_card_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**Billing**](Billing.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_invoices_fk_post**
> BillingInvoice team_members_id_team_billing_invoices_fk_post(id, fk)

Pay Team Billing Invoice

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Billing Invoice id

try: 
    # Pay Team Billing Invoice
    api_response = api_instance.team_members_id_team_billing_invoices_fk_post(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_invoices_fk_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Billing Invoice id | 

### Return type

[**BillingInvoice**](BillingInvoice.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_invoices_get**
> list[BillingInvoice] team_members_id_team_billing_invoices_get(id, filter=filter)

List Team Billing Invoices

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List Team Billing Invoices
    api_response = api_instance.team_members_id_team_billing_invoices_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_invoices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[BillingInvoice]**](BillingInvoice.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_invoices_upcoming_get**
> BillingInvoice team_members_id_team_billing_invoices_upcoming_get(id)

List Upcoming Team Billing Invoices

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # List Upcoming Team Billing Invoices
    api_response = api_instance.team_members_id_team_billing_invoices_upcoming_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_invoices_upcoming_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

[**BillingInvoice**](BillingInvoice.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_put**
> Billing team_members_id_team_billing_put(id, data=data)

Update Team Billing

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update Team Billing
    api_response = api_instance.team_members_id_team_billing_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**Billing**](Billing.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_subscription_plan_put**
> Billing team_members_id_team_billing_subscription_plan_put(id, data=data)

Update Team Billing Subscription Plan

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update Team Billing Subscription Plan
    api_response = api_instance.team_members_id_team_billing_subscription_plan_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_subscription_plan_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**Billing**](Billing.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_tax_evidence_get**
> object team_members_id_team_billing_tax_evidence_get(id)

Get Team Billing Tax Evidence

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Get Team Billing Tax Evidence
    api_response = api_instance.team_members_id_team_billing_tax_evidence_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_tax_evidence_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_billing_uncached_get**
> Billing team_members_id_team_billing_uncached_get(id)

Get Team Billing

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Get Team Billing
    api_response = api_instance.team_members_id_team_billing_uncached_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_billing_uncached_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

[**Billing**](Billing.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_brand_delete**
> team_members_id_team_brand_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes brand of this model.
    api_instance.team_members_id_team_brand_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_brand_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_brand_get**
> TeamBrand team_members_id_team_brand_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation brand.
    api_response = api_instance.team_members_id_team_brand_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_brand_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_brand_post**
> TeamBrand team_members_id_team_brand_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamBrand() # TeamBrand |  (optional)

try: 
    # Creates a new instance in brand of this model.
    api_response = api_instance.team_members_id_team_brand_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_brand_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamBrand**](TeamBrand.md)|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_brand_put**
> TeamBrand team_members_id_team_brand_put(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamBrand() # TeamBrand |  (optional)

try: 
    # Update brand of this model.
    api_response = api_instance.team_members_id_team_brand_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_brand_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamBrand**](TeamBrand.md)|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_count_get**
> InlineResponse2001 team_members_id_team_builder_configs_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts builderConfigs of Team.
    api_response = api_instance.team_members_id_team_builder_configs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_default_get**
> TeamBuilderConfig team_members_id_team_builder_configs_default_get(id)

Get default Team Builder Config

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Get default Team Builder Config
    api_response = api_instance.team_members_id_team_builder_configs_default_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_default_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_delete**
> team_members_id_team_builder_configs_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all builderConfigs of this model.
    api_instance.team_members_id_team_builder_configs_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_fk_delete**
> team_members_id_team_builder_configs_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for builderConfigs

try: 
    # Delete a related item by id for builderConfigs.
    api_instance.team_members_id_team_builder_configs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for builderConfigs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_fk_get**
> TeamBuilderConfig team_members_id_team_builder_configs_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for builderConfigs

try: 
    # Find a related item by id for builderConfigs.
    api_response = api_instance.team_members_id_team_builder_configs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for builderConfigs | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_fk_logo_put**
> TeamBuilderConfig team_members_id_team_builder_configs_fk_logo_put(id, fk, data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | BuilderConfig id
data = TweakApi.TeamMember() # TeamMember | Logo

try: 
    # Change Builder Config logo
    api_response = api_instance.team_members_id_team_builder_configs_fk_logo_put(id, fk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_fk_logo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| BuilderConfig id | 
 **data** | [**TeamMember**](TeamMember.md)| Logo | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_fk_put**
> TeamBuilderConfig team_members_id_team_builder_configs_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for builderConfigs
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig |  (optional)

try: 
    # Update a related item by id for builderConfigs.
    api_response = api_instance.team_members_id_team_builder_configs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_builder_configs_fk_watermark_put**
> TeamBuilderConfig team_members_id_team_builder_configs_fk_watermark_put(id, fk, data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | BuilderConfig id
data = TweakApi.TeamMember() # TeamMember | Watermark

try: 
    # Change Builder Config watermark
    api_response = api_instance.team_members_id_team_builder_configs_fk_watermark_put(id, fk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_fk_watermark_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| BuilderConfig id | 
 **data** | [**TeamMember**](TeamMember.md)| Watermark | 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_get**
> list[TeamBuilderConfig] team_members_id_team_builder_configs_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries builderConfigs of Team.
    api_response = api_instance.team_members_id_team_builder_configs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamBuilderConfig]**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_builder_configs_post**
> TeamBuilderConfig team_members_id_team_builder_configs_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamBuilderConfig() # TeamBuilderConfig |  (optional)

try: 
    # Creates a new instance in builderConfigs of this model.
    api_response = api_instance.team_members_id_team_builder_configs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_builder_configs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamBuilderConfig**](TeamBuilderConfig.md)|  | [optional] 

### Return type

[**TeamBuilderConfig**](TeamBuilderConfig.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_record_get**
> object team_members_id_team_data_record_get(id)

Get TeamData Record

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Get TeamData Record
    api_response = api_instance.team_members_id_team_data_record_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_record_post**
> object team_members_id_team_data_record_post(id, data=data)

Create TeamData Record

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Create TeamData Record
    api_response = api_instance.team_members_id_team_data_record_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_record_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_record_put**
> object team_members_id_team_data_record_put(id, data=data)

Update TeamData Record

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Update TeamData Record
    api_response = api_instance.team_members_id_team_data_record_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_record_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_sources_count_get**
> InlineResponse2001 team_members_id_team_data_sources_count_get(id, where=where)

Counts dataSources of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts dataSources of Team.
    api_response = api_instance.team_members_id_team_data_sources_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_sources_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_sources_delete**
> team_members_id_team_data_sources_delete(id)

Deletes all dataSources of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all dataSources of this model.
    api_instance.team_members_id_team_data_sources_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_sources_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_sources_fk_delete**
> team_members_id_team_data_sources_fk_delete(id, fk)

Delete a related item by id for dataSources.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for dataSources

try: 
    # Delete a related item by id for dataSources.
    api_instance.team_members_id_team_data_sources_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_sources_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for dataSources | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_sources_fk_get**
> DataSource team_members_id_team_data_sources_fk_get(id, fk)

Find a related item by id for dataSources.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for dataSources

try: 
    # Find a related item by id for dataSources.
    api_response = api_instance.team_members_id_team_data_sources_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_sources_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for dataSources | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_sources_fk_put**
> DataSource team_members_id_team_data_sources_fk_put(id, fk, data=data)

Update a related item by id for dataSources.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for dataSources
data = TweakApi.DataSource() # DataSource |  (optional)

try: 
    # Update a related item by id for dataSources.
    api_response = api_instance.team_members_id_team_data_sources_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_sources_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for dataSources | 
 **data** | [**DataSource**](DataSource.md)|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_sources_get**
> list[DataSource] team_members_id_team_data_sources_get(id, filter=filter)

Queries dataSources of Team.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries dataSources of Team.
    api_response = api_instance.team_members_id_team_data_sources_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_sources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DataSource]**](DataSource.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_data_sources_post**
> DataSource team_members_id_team_data_sources_post(id, data=data)

Creates a new instance in dataSources of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.DataSource() # DataSource |  (optional)

try: 
    # Creates a new instance in dataSources of this model.
    api_response = api_instance.team_members_id_team_data_sources_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_data_sources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**DataSource**](DataSource.md)|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_dynamic_datas_count_get**
> InlineResponse2001 team_members_id_team_dynamic_datas_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts dynamicDatas of Team.
    api_response = api_instance.team_members_id_team_dynamic_datas_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_dynamic_datas_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_dynamic_datas_delete**
> team_members_id_team_dynamic_datas_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all dynamicDatas of this model.
    api_instance.team_members_id_team_dynamic_datas_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_dynamic_datas_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_dynamic_datas_fk_delete**
> team_members_id_team_dynamic_datas_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Delete a related item by id for dynamicDatas.
    api_instance.team_members_id_team_dynamic_datas_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_dynamic_datas_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_dynamic_datas_fk_get**
> DynamicData team_members_id_team_dynamic_datas_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for dynamicDatas

try: 
    # Find a related item by id for dynamicDatas.
    api_response = api_instance.team_members_id_team_dynamic_datas_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_dynamic_datas_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for dynamicDatas | 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_dynamic_datas_fk_put**
> DynamicData team_members_id_team_dynamic_datas_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for dynamicDatas
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Update a related item by id for dynamicDatas.
    api_response = api_instance.team_members_id_team_dynamic_datas_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_dynamic_datas_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_dynamic_datas_get**
> list[DynamicData] team_members_id_team_dynamic_datas_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries dynamicDatas of Team.
    api_response = api_instance.team_members_id_team_dynamic_datas_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_dynamic_datas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[DynamicData]**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_dynamic_datas_post**
> DynamicData team_members_id_team_dynamic_datas_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.DynamicData() # DynamicData |  (optional)

try: 
    # Creates a new instance in dynamicDatas of this model.
    api_response = api_instance.team_members_id_team_dynamic_datas_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_dynamic_datas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**DynamicData**](DynamicData.md)|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_get**
> Team team_members_id_team_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation team.
    api_response = api_instance.team_members_id_team_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_image_folders_count_get**
> InlineResponse2001 team_members_id_team_image_folders_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts imageFolders of Team.
    api_response = api_instance.team_members_id_team_image_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_image_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_image_folders_delete**
> team_members_id_team_image_folders_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all imageFolders of this model.
    api_instance.team_members_id_team_image_folders_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_image_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_image_folders_fk_delete**
> team_members_id_team_image_folders_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Delete a related item by id for imageFolders.
    api_instance.team_members_id_team_image_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_image_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_image_folders_fk_get**
> ImageFolder team_members_id_team_image_folders_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Find a related item by id for imageFolders.
    api_response = api_instance.team_members_id_team_image_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_image_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_image_folders_fk_put**
> ImageFolder team_members_id_team_image_folders_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for imageFolders.
    api_response = api_instance.team_members_id_team_image_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_image_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_image_folders_get**
> list[ImageFolder] team_members_id_team_image_folders_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries imageFolders of Team.
    api_response = api_instance.team_members_id_team_image_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_image_folders_post**
> ImageFolder team_members_id_team_image_folders_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in imageFolders of this model.
    api_response = api_instance.team_members_id_team_image_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_images_count_get**
> InlineResponse2001 team_members_id_team_images_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts images of Team.
    api_response = api_instance.team_members_id_team_images_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_images_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_images_delete**
> team_members_id_team_images_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all images of this model.
    api_instance.team_members_id_team_images_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_images_fk_delete**
> team_members_id_team_images_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for images

try: 
    # Delete a related item by id for images.
    api_instance.team_members_id_team_images_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_images_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for images | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_images_fk_get**
> Image team_members_id_team_images_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for images

try: 
    # Find a related item by id for images.
    api_response = api_instance.team_members_id_team_images_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_images_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for images | 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_images_fk_put**
> Image team_members_id_team_images_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for images
data = TweakApi.Image() # Image |  (optional)

try: 
    # Update a related item by id for images.
    api_response = api_instance.team_members_id_team_images_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_images_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_images_get**
> list[Image] team_members_id_team_images_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries images of Team.
    api_response = api_instance.team_members_id_team_images_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_images_post**
> Image team_members_id_team_images_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Image() # Image |  (optional)

try: 
    # Creates a new instance in images of this model.
    api_response = api_instance.team_members_id_team_images_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_logo_put**
> Team team_members_id_team_logo_put(id, id2, data)

Change Team logo

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember | Logo

try: 
    # Change Team logo
    api_response = api_instance.team_members_id_team_logo_put(id, id2, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_logo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)| Logo | 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_count_get**
> InlineResponse2001 team_members_id_team_members_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Team.
    api_response = api_instance.team_members_id_team_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_delete**
> team_members_id_team_members_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all members of this model.
    api_instance.team_members_id_team_members_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_fk_delete**
> team_members_id_team_members_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.team_members_id_team_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_fk_get**
> Customer team_members_id_team_members_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.team_members_id_team_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_fk_put**
> Customer team_members_id_team_members_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.Customer() # Customer |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.team_members_id_team_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_members_get**
> list[Customer] team_members_id_team_members_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Team.
    api_response = api_instance.team_members_id_team_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_post**
> Customer team_members_id_team_members_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Customer() # Customer |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.team_members_id_team_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Customer**](Customer.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_rel_fk_delete**
> team_members_id_team_members_rel_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.team_members_id_team_members_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_rel_fk_head**
> bool team_members_id_team_members_rel_fk_head(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.team_members_id_team_members_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_members_rel_fk_put**
> TeamMember team_members_id_team_members_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.team_members_id_team_members_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_permission_delete**
> team_members_id_team_permission_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes permission of this model.
    api_instance.team_members_id_team_permission_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_permission_get**
> TeamPermissionSet team_members_id_team_permission_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.team_members_id_team_permission_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamPermissionSet**](TeamPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_permission_post**
> TeamPermissionSet team_members_id_team_permission_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamPermissionSet() # TeamPermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.team_members_id_team_permission_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamPermissionSet**](TeamPermissionSet.md)|  | [optional] 

### Return type

[**TeamPermissionSet**](TeamPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_permission_put**
> TeamPermissionSet team_members_id_team_permission_put(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamPermissionSet() # TeamPermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.team_members_id_team_permission_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamPermissionSet**](TeamPermissionSet.md)|  | [optional] 

### Return type

[**TeamPermissionSet**](TeamPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_portals_count_get**
> InlineResponse2001 team_members_id_team_portals_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of Team.
    api_response = api_instance.team_members_id_team_portals_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_portals_delete**
> team_members_id_team_portals_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all portals of this model.
    api_instance.team_members_id_team_portals_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_portals_fk_delete**
> team_members_id_team_portals_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.team_members_id_team_portals_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_portals_fk_get**
> Portal team_members_id_team_portals_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.team_members_id_team_portals_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_portals_fk_put**
> Portal team_members_id_team_portals_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.team_members_id_team_portals_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_portals_get**
> list[Portal] team_members_id_team_portals_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of Team.
    api_response = api_instance.team_members_id_team_portals_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_portals_post**
> Portal team_members_id_team_portals_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.team_members_id_team_portals_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_materials_count_get**
> InlineResponse2001 team_members_id_team_product_materials_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productMaterials of Team.
    api_response = api_instance.team_members_id_team_product_materials_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_materials_delete**
> team_members_id_team_product_materials_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all productMaterials of this model.
    api_instance.team_members_id_team_product_materials_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_materials_fk_delete**
> team_members_id_team_product_materials_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productMaterials

try: 
    # Delete a related item by id for productMaterials.
    api_instance.team_members_id_team_product_materials_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for productMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_materials_fk_get**
> ProductMaterial team_members_id_team_product_materials_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productMaterials

try: 
    # Find a related item by id for productMaterials.
    api_response = api_instance.team_members_id_team_product_materials_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for productMaterials | 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_materials_fk_put**
> ProductMaterial team_members_id_team_product_materials_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productMaterials
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Update a related item by id for productMaterials.
    api_response = api_instance.team_members_id_team_product_materials_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_product_materials_get**
> list[ProductMaterial] team_members_id_team_product_materials_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productMaterials of Team.
    api_response = api_instance.team_members_id_team_product_materials_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductMaterial]**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_materials_post**
> ProductMaterial team_members_id_team_product_materials_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.ProductMaterial() # ProductMaterial |  (optional)

try: 
    # Creates a new instance in productMaterials of this model.
    api_response = api_instance.team_members_id_team_product_materials_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**ProductMaterial**](ProductMaterial.md)|  | [optional] 

### Return type

[**ProductMaterial**](ProductMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_pdf_color_profiles_available_get**
> list[ProductPdfColorProfile] team_members_id_team_product_pdf_color_profiles_available_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all available PdfColorProfile
    api_response = api_instance.team_members_id_team_product_pdf_color_profiles_available_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[ProductPdfColorProfile]**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_pdf_color_profiles_count_get**
> InlineResponse2001 team_members_id_team_product_pdf_color_profiles_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productPdfColorProfiles of Team.
    api_response = api_instance.team_members_id_team_product_pdf_color_profiles_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_pdf_color_profiles_delete**
> team_members_id_team_product_pdf_color_profiles_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all productPdfColorProfiles of this model.
    api_instance.team_members_id_team_product_pdf_color_profiles_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_pdf_color_profiles_fk_delete**
> team_members_id_team_product_pdf_color_profiles_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productPdfColorProfiles

try: 
    # Delete a related item by id for productPdfColorProfiles.
    api_instance.team_members_id_team_product_pdf_color_profiles_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for productPdfColorProfiles | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_pdf_color_profiles_fk_get**
> ProductPdfColorProfile team_members_id_team_product_pdf_color_profiles_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productPdfColorProfiles

try: 
    # Find a related item by id for productPdfColorProfiles.
    api_response = api_instance.team_members_id_team_product_pdf_color_profiles_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for productPdfColorProfiles | 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_pdf_color_profiles_fk_put**
> ProductPdfColorProfile team_members_id_team_product_pdf_color_profiles_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productPdfColorProfiles
data = TweakApi.ProductPdfColorProfile() # ProductPdfColorProfile |  (optional)

try: 
    # Update a related item by id for productPdfColorProfiles.
    api_response = api_instance.team_members_id_team_product_pdf_color_profiles_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_product_pdf_color_profiles_get**
> list[ProductPdfColorProfile] team_members_id_team_product_pdf_color_profiles_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productPdfColorProfiles of Team.
    api_response = api_instance.team_members_id_team_product_pdf_color_profiles_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductPdfColorProfile]**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_pdf_color_profiles_upload_post**
> ProductPdfColorProfile team_members_id_team_product_pdf_color_profiles_upload_post(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Upload ICC PDF Color Profile for this Team
    api_response = api_instance.team_members_id_team_product_pdf_color_profiles_upload_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_pdf_color_profiles_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

[**ProductPdfColorProfile**](ProductPdfColorProfile.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_size_materials_count_get**
> InlineResponse2001 team_members_id_team_product_size_materials_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts productSizeMaterials of Team.
    api_response = api_instance.team_members_id_team_product_size_materials_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_size_materials_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_size_materials_delete**
> team_members_id_team_product_size_materials_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all productSizeMaterials of this model.
    api_instance.team_members_id_team_product_size_materials_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_size_materials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_size_materials_fk_delete**
> team_members_id_team_product_size_materials_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Delete a related item by id for productSizeMaterials.
    api_instance.team_members_id_team_product_size_materials_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_size_materials_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_size_materials_fk_get**
> ProductSizeMaterial team_members_id_team_product_size_materials_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productSizeMaterials

try: 
    # Find a related item by id for productSizeMaterials.
    api_response = api_instance.team_members_id_team_product_size_materials_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_size_materials_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for productSizeMaterials | 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_size_materials_fk_put**
> ProductSizeMaterial team_members_id_team_product_size_materials_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for productSizeMaterials
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Update a related item by id for productSizeMaterials.
    api_response = api_instance.team_members_id_team_product_size_materials_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_size_materials_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_product_size_materials_get**
> list[ProductSizeMaterial] team_members_id_team_product_size_materials_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries productSizeMaterials of Team.
    api_response = api_instance.team_members_id_team_product_size_materials_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_size_materials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ProductSizeMaterial]**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_product_size_materials_post**
> ProductSizeMaterial team_members_id_team_product_size_materials_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.ProductSizeMaterial() # ProductSizeMaterial |  (optional)

try: 
    # Creates a new instance in productSizeMaterials of this model.
    api_response = api_instance.team_members_id_team_product_size_materials_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_product_size_materials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**ProductSizeMaterial**](ProductSizeMaterial.md)|  | [optional] 

### Return type

[**ProductSizeMaterial**](ProductSizeMaterial.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_team_data_get**
> DynamicData team_members_id_team_team_data_get(id, refresh=refresh)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
refresh = true # bool |  (optional)

try: 
    # Fetches belongsTo relation teamData.
    api_response = api_instance.team_members_id_team_team_data_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**DynamicData**](DynamicData.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_team_members_count_get**
> InlineResponse2001 team_members_id_team_team_members_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts teamMembers of Team.
    api_response = api_instance.team_members_id_team_team_members_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_team_members_delete**
> team_members_id_team_team_members_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all teamMembers of this model.
    api_instance.team_members_id_team_team_members_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_team_members_fk_delete**
> team_members_id_team_team_members_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for teamMembers

try: 
    # Delete a related item by id for teamMembers.
    api_instance.team_members_id_team_team_members_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for teamMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_team_members_fk_get**
> TeamMember team_members_id_team_team_members_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for teamMembers

try: 
    # Find a related item by id for teamMembers.
    api_response = api_instance.team_members_id_team_team_members_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for teamMembers | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_team_members_fk_put**
> TeamMember team_members_id_team_team_members_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for teamMembers
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for teamMembers.
    api_response = api_instance.team_members_id_team_team_members_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_team_members_get**
> list[TeamMember] team_members_id_team_team_members_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries teamMembers of Team.
    api_response = api_instance.team_members_id_team_team_members_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_team_members_post**
> TeamMember team_members_id_team_team_members_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in teamMembers of this model.
    api_response = api_instance.team_members_id_team_team_members_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_template_folders_count_get**
> InlineResponse2001 team_members_id_team_template_folders_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateFolders of Team.
    api_response = api_instance.team_members_id_team_template_folders_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_template_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_template_folders_delete**
> team_members_id_team_template_folders_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all templateFolders of this model.
    api_instance.team_members_id_team_template_folders_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_template_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_template_folders_fk_delete**
> team_members_id_team_template_folders_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Delete a related item by id for templateFolders.
    api_instance.team_members_id_team_template_folders_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_template_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_template_folders_fk_get**
> TeamTemplateFolder team_members_id_team_template_folders_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Find a related item by id for templateFolders.
    api_response = api_instance.team_members_id_team_template_folders_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_template_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_template_folders_fk_put**
> TeamTemplateFolder team_members_id_team_template_folders_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templateFolders
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Update a related item by id for templateFolders.
    api_response = api_instance.team_members_id_team_template_folders_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_template_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_template_folders_get**
> list[TeamTemplateFolder] team_members_id_team_template_folders_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateFolders of Team.
    api_response = api_instance.team_members_id_team_template_folders_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamTemplateFolder]**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_template_folders_post**
> TeamTemplateFolder team_members_id_team_template_folders_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Creates a new instance in templateFolders of this model.
    api_response = api_instance.team_members_id_team_template_folders_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_template_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_count_get**
> InlineResponse2001 team_members_id_team_templates_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of Team.
    api_response = api_instance.team_members_id_team_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_delete**
> team_members_id_team_templates_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all templates of this model.
    api_instance.team_members_id_team_templates_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_fk_delete**
> team_members_id_team_templates_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.team_members_id_team_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_fk_get**
> Template team_members_id_team_templates_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.team_members_id_team_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_fk_put**
> Template team_members_id_team_templates_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.team_members_id_team_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_templates_fk_url_review_get**
> str team_members_id_team_templates_fk_url_review_get(id, fk)

Get URL to review a Team Template

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Template id

try: 
    # Get URL to review a Team Template
    api_response = api_instance.team_members_id_team_templates_fk_url_review_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_fk_url_review_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Template id | 

### Return type

**str**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_get**
> list[Template] team_members_id_team_templates_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of Team.
    api_response = api_instance.team_members_id_team_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_post**
> Template team_members_id_team_templates_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.team_members_id_team_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_templates_with_designs_get**
> list[Template] team_members_id_team_templates_with_designs_get(id, id2, filter=filter)

List Templates with Designs for the Team of TeamMember

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List Templates with Designs for the Team of TeamMember
    api_response = api_instance.team_members_id_team_templates_with_designs_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_templates_with_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_workflows_count_get**
> InlineResponse2001 team_members_id_team_workflows_count_get(id, where=where)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts workflows of Team.
    api_response = api_instance.team_members_id_team_workflows_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_workflows_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_workflows_delete**
> team_members_id_team_workflows_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all workflows of this model.
    api_instance.team_members_id_team_workflows_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_workflows_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_workflows_fk_delete**
> team_members_id_team_workflows_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Delete a related item by id for workflows.
    api_instance.team_members_id_team_workflows_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_workflows_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_workflows_fk_get**
> Workflow team_members_id_team_workflows_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Find a related item by id for workflows.
    api_response = api_instance.team_members_id_team_workflows_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_workflows_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_workflows_fk_put**
> Workflow team_members_id_team_workflows_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for workflows
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Update a related item by id for workflows.
    api_response = api_instance.team_members_id_team_workflows_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_workflows_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_team_workflows_get**
> list[Workflow] team_members_id_team_workflows_get(id, filter=filter)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries workflows of Team.
    api_response = api_instance.team_members_id_team_workflows_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_workflows_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Workflow]**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_team_workflows_post**
> Workflow team_members_id_team_workflows_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Creates a new instance in workflows of this model.
    api_response = api_instance.team_members_id_team_workflows_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_team_workflows_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Workflow**](Workflow.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_count_get**
> InlineResponse2001 team_members_id_templates_count_get(id, where=where)

Counts templates of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of TeamMember.
    api_response = api_instance.team_members_id_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_delete**
> team_members_id_templates_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all templates of this model.
    api_instance.team_members_id_templates_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_fk_delete**
> team_members_id_templates_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.team_members_id_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_fk_flashvars_get**
> FlashVar team_members_id_templates_fk_flashvars_get(id, id2, fk)

Find Template FlashVars by id

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
fk = 'fk_example' # str | 

try: 
    # Find Template FlashVars by id
    api_response = api_instance.team_members_id_templates_fk_flashvars_get(id, id2, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_fk_flashvars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **fk** | **str**|  | 

### Return type

[**FlashVar**](FlashVar.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_fk_get**
> Template team_members_id_templates_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.team_members_id_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_fk_put**
> Template team_members_id_templates_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.team_members_id_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_templates_get**
> list[Template] team_members_id_templates_get(id, filter=filter)

Queries templates of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of TeamMember.
    api_response = api_instance.team_members_id_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_post**
> Template team_members_id_templates_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.team_members_id_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_rel_fk_delete**
> team_members_id_templates_rel_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Remove the templates relation to an item by id.
    api_instance.team_members_id_templates_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_rel_fk_head**
> bool team_members_id_templates_rel_fk_head(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Check the existence of templates relation to an item by id.
    api_response = api_instance.team_members_id_templates_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templates | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_templates_rel_fk_put**
> TemplateMember team_members_id_templates_rel_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.TemplateMember() # TemplateMember |  (optional)

try: 
    # Add a related item by id for templates.
    api_response = api_instance.team_members_id_templates_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_templates_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for templates | 
 **data** | [**TemplateMember**](TemplateMember.md)|  | [optional] 

### Return type

[**TemplateMember**](TemplateMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_tweak_template_folders_get**
> list[TeamTemplateFolder] team_members_id_tweak_template_folders_get(id, id2, filter=filter)

List Tweak Templates Folders

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List Tweak Templates Folders
    api_response = api_instance.team_members_id_tweak_template_folders_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_tweak_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TeamTemplateFolder]**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_tweak_template_folders_nk_get**
> TeamTemplateFolder team_members_id_tweak_template_folders_nk_get(id, id2, nk, filter=filter)

Get Tweak Templates Folders details

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
nk = 'nk_example' # str | TemplateFolder id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Get Tweak Templates Folders details
    api_response = api_instance.team_members_id_tweak_template_folders_nk_get(id, id2, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_tweak_template_folders_nk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **nk** | **str**| TemplateFolder id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_tweak_template_folders_nk_templates_fk_get**
> Template team_members_id_tweak_template_folders_nk_templates_fk_get(id, id2, nk, fk, filter=filter)

Get Tweak Template details within a Tweak Template Folder

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
nk = 'nk_example' # str | TemplateFolder id
fk = 'fk_example' # str | Template id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Get Tweak Template details within a Tweak Template Folder
    api_response = api_instance.team_members_id_tweak_template_folders_nk_templates_fk_get(id, id2, nk, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_tweak_template_folders_nk_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **nk** | **str**| TemplateFolder id | 
 **fk** | **str**| Template id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_tweak_template_folders_nk_templates_get**
> list[Template] team_members_id_tweak_template_folders_nk_templates_get(id, id2, nk, filter=filter)

List Tweak Templates within a Tweak Template Folder

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
nk = 'nk_example' # str | TemplateFolder id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List Tweak Templates within a Tweak Template Folder
    api_response = api_instance.team_members_id_tweak_template_folders_nk_templates_get(id, id2, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_tweak_template_folders_nk_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **nk** | **str**| TemplateFolder id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_tweak_templates_fk_flashvars_get**
> FlashVar team_members_id_tweak_templates_fk_flashvars_get(id, id2, fk)

Find Template FlashVars by id

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | 
fk = 'fk_example' # str | 

try: 
    # Find Template FlashVars by id
    api_response = api_instance.team_members_id_tweak_templates_fk_flashvars_get(id, id2, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_tweak_templates_fk_flashvars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**|  | 
 **fk** | **str**|  | 

### Return type

[**FlashVar**](FlashVar.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_tweak_templates_fk_get**
> Template team_members_id_tweak_templates_fk_get(id, id2, fk, filter=filter)

Get Tweak Template details

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Template id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Get Tweak Template details
    api_response = api_instance.team_members_id_tweak_templates_fk_get(id, id2, fk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_tweak_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **fk** | **str**| Template id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_tweak_templates_get**
> list[Template] team_members_id_tweak_templates_get(id, id2, filter=filter)

List Tweak Templates

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
id2 = 'id_example' # str | TeamMember id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # List Tweak Templates
    api_response = api_instance.team_members_id_tweak_templates_get(id, id2, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_tweak_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **id2** | **str**| TeamMember id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_uploaded_templates_count_get**
> InlineResponse2001 team_members_id_uploaded_templates_count_get(id, where=where)

Counts uploadedTemplates of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts uploadedTemplates of TeamMember.
    api_response = api_instance.team_members_id_uploaded_templates_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_uploaded_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_uploaded_templates_delete**
> team_members_id_uploaded_templates_delete(id)

Deletes all uploadedTemplates of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all uploadedTemplates of this model.
    api_instance.team_members_id_uploaded_templates_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_uploaded_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_uploaded_templates_fk_delete**
> team_members_id_uploaded_templates_fk_delete(id, fk)

Delete a related item by id for uploadedTemplates.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for uploadedTemplates

try: 
    # Delete a related item by id for uploadedTemplates.
    api_instance.team_members_id_uploaded_templates_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_uploaded_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for uploadedTemplates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_uploaded_templates_fk_get**
> Template team_members_id_uploaded_templates_fk_get(id, fk)

Find a related item by id for uploadedTemplates.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for uploadedTemplates

try: 
    # Find a related item by id for uploadedTemplates.
    api_response = api_instance.team_members_id_uploaded_templates_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_uploaded_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for uploadedTemplates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_uploaded_templates_fk_put**
> Template team_members_id_uploaded_templates_fk_put(id, fk, data=data)

Update a related item by id for uploadedTemplates.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for uploadedTemplates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for uploadedTemplates.
    api_response = api_instance.team_members_id_uploaded_templates_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_uploaded_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for uploadedTemplates | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_uploaded_templates_get**
> list[Template] team_members_id_uploaded_templates_get(id, filter=filter)

Queries uploadedTemplates of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries uploadedTemplates of TeamMember.
    api_response = api_instance.team_members_id_uploaded_templates_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_uploaded_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_uploaded_templates_post**
> Template team_members_id_uploaded_templates_post(id, data=data)

Creates a new instance in uploadedTemplates of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in uploadedTemplates of this model.
    api_response = api_instance.team_members_id_uploaded_templates_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_uploaded_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_workflows_count_get**
> InlineResponse2001 team_members_id_workflows_count_get(id, where=where)

Counts workflows of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts workflows of TeamMember.
    api_response = api_instance.team_members_id_workflows_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_workflows_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_workflows_delete**
> team_members_id_workflows_delete(id)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id

try: 
    # Deletes all workflows of this model.
    api_instance.team_members_id_workflows_delete(id)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_workflows_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_workflows_fk_delete**
> team_members_id_workflows_fk_delete(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Delete a related item by id for workflows.
    api_instance.team_members_id_workflows_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_workflows_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_workflows_fk_get**
> Workflow team_members_id_workflows_fk_get(id, fk)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Find a related item by id for workflows.
    api_response = api_instance.team_members_id_workflows_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_workflows_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_workflows_fk_put**
> Workflow team_members_id_workflows_fk_put(id, fk, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
fk = 'fk_example' # str | Foreign key for workflows
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Update a related item by id for workflows.
    api_response = api_instance.team_members_id_workflows_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_workflows_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
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

# **team_members_id_workflows_get**
> list[Workflow] team_members_id_workflows_get(id, filter=filter)

Queries workflows of TeamMember.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries workflows of TeamMember.
    api_response = api_instance.team_members_id_workflows_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_workflows_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Workflow]**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_id_workflows_post**
> Workflow team_members_id_workflows_post(id, data=data)

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
api_instance = TweakApi.TeamMemberApi()
id = 'id_example' # str | TeamMember id
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Creates a new instance in workflows of this model.
    api_response = api_instance.team_members_id_workflows_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_id_workflows_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TeamMember id | 
 **data** | [**Workflow**](Workflow.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_patch**
> TeamMember team_members_patch(data=data)

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
api_instance = TweakApi.TeamMemberApi()
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_members_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_post**
> TeamMember team_members_post(data=data)

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
api_instance = TweakApi.TeamMemberApi()
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.team_members_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_put**
> TeamMember team_members_put(data=data)

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
api_instance = TweakApi.TeamMemberApi()
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_members_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_replace_or_create_post**
> TeamMember team_members_replace_or_create_post(data=data)

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
api_instance = TweakApi.TeamMemberApi()
data = TweakApi.TeamMember() # TeamMember | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.team_members_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TeamMember**](TeamMember.md)| Model instance data | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_update_post**
> InlineResponse2003 team_members_update_post(where=where, data=data)

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
api_instance = TweakApi.TeamMemberApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamMember() # TeamMember | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.team_members_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamMember**](TeamMember.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_upsert_with_where_post**
> TeamMember team_members_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.TeamMemberApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.TeamMember() # TeamMember | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.team_members_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMemberApi->team_members_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**TeamMember**](TeamMember.md)| An object of model property name/value pairs | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

