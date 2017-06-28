# TweakApi.CustomerApi

All URIs are relative to *https://apidevcdn.tweak.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_change_password_post**](CustomerApi.md#customers_change_password_post) | **POST** /Customers/change-password | Change a user&#39;s password.
[**customers_change_stream_get**](CustomerApi.md#customers_change_stream_get) | **GET** /Customers/change-stream | Create a change stream.
[**customers_change_stream_post**](CustomerApi.md#customers_change_stream_post) | **POST** /Customers/change-stream | Create a change stream.
[**customers_confirm_get**](CustomerApi.md#customers_confirm_get) | **GET** /Customers/confirm | Confirm a user registration with identity verification token.
[**customers_count_get**](CustomerApi.md#customers_count_get) | **GET** /Customers/count | Count instances of the model matched by where from the data source.
[**customers_find_one_get**](CustomerApi.md#customers_find_one_get) | **GET** /Customers/findOne | Find first instance of the model matched by filter from the data source.
[**customers_get**](CustomerApi.md#customers_get) | **GET** /Customers | Find all instances of the model matched by filter from the data source.
[**customers_id_access_tokens_count_get**](CustomerApi.md#customers_id_access_tokens_count_get) | **GET** /Customers/{id}/accessTokens/count | Counts accessTokens of Customer.
[**customers_id_access_tokens_delete**](CustomerApi.md#customers_id_access_tokens_delete) | **DELETE** /Customers/{id}/accessTokens | Deletes all accessTokens of this model.
[**customers_id_access_tokens_fk_delete**](CustomerApi.md#customers_id_access_tokens_fk_delete) | **DELETE** /Customers/{id}/accessTokens/{fk} | Delete a related item by id for accessTokens.
[**customers_id_access_tokens_fk_get**](CustomerApi.md#customers_id_access_tokens_fk_get) | **GET** /Customers/{id}/accessTokens/{fk} | Find a related item by id for accessTokens.
[**customers_id_access_tokens_fk_put**](CustomerApi.md#customers_id_access_tokens_fk_put) | **PUT** /Customers/{id}/accessTokens/{fk} | Update a related item by id for accessTokens.
[**customers_id_access_tokens_get**](CustomerApi.md#customers_id_access_tokens_get) | **GET** /Customers/{id}/accessTokens | Queries accessTokens of Customer.
[**customers_id_access_tokens_post**](CustomerApi.md#customers_id_access_tokens_post) | **POST** /Customers/{id}/accessTokens | Creates a new instance in accessTokens of this model.
[**customers_id_active_get**](CustomerApi.md#customers_id_active_get) | **GET** /Customers/{id}/active | Define whether customer is active or not
[**customers_id_delete**](CustomerApi.md#customers_id_delete) | **DELETE** /Customers/{id} | Delete a model instance by {{id}} from the data source.
[**customers_id_designs_count_get**](CustomerApi.md#customers_id_designs_count_get) | **GET** /Customers/{id}/designs/count | Counts designs of Customer.
[**customers_id_designs_delete**](CustomerApi.md#customers_id_designs_delete) | **DELETE** /Customers/{id}/designs | Deletes all designs of this model.
[**customers_id_designs_fk_delete**](CustomerApi.md#customers_id_designs_fk_delete) | **DELETE** /Customers/{id}/designs/{fk} | Delete a related item by id for designs.
[**customers_id_designs_fk_get**](CustomerApi.md#customers_id_designs_fk_get) | **GET** /Customers/{id}/designs/{fk} | Find a related item by id for designs.
[**customers_id_designs_fk_put**](CustomerApi.md#customers_id_designs_fk_put) | **PUT** /Customers/{id}/designs/{fk} | Update a related item by id for designs.
[**customers_id_designs_get**](CustomerApi.md#customers_id_designs_get) | **GET** /Customers/{id}/designs | Queries designs of Customer.
[**customers_id_designs_post**](CustomerApi.md#customers_id_designs_post) | **POST** /Customers/{id}/designs | Creates a new instance in designs of this model.
[**customers_id_exists_get**](CustomerApi.md#customers_id_exists_get) | **GET** /Customers/{id}/exists | Check whether a model instance exists in the data source.
[**customers_id_get**](CustomerApi.md#customers_id_get) | **GET** /Customers/{id} | Find a model instance by {{id}} from the data source.
[**customers_id_head**](CustomerApi.md#customers_id_head) | **HEAD** /Customers/{id} | Check whether a model instance exists in the data source.
[**customers_id_invitation_tickets_count_get**](CustomerApi.md#customers_id_invitation_tickets_count_get) | **GET** /Customers/{id}/invitationTickets/count | Counts invitationTickets of Customer.
[**customers_id_invitation_tickets_delete**](CustomerApi.md#customers_id_invitation_tickets_delete) | **DELETE** /Customers/{id}/invitationTickets | Deletes all invitationTickets of this model.
[**customers_id_invitation_tickets_fk_delete**](CustomerApi.md#customers_id_invitation_tickets_fk_delete) | **DELETE** /Customers/{id}/invitationTickets/{fk} | Delete a related item by id for invitationTickets.
[**customers_id_invitation_tickets_fk_get**](CustomerApi.md#customers_id_invitation_tickets_fk_get) | **GET** /Customers/{id}/invitationTickets/{fk} | Find a related item by id for invitationTickets.
[**customers_id_invitation_tickets_fk_put**](CustomerApi.md#customers_id_invitation_tickets_fk_put) | **PUT** /Customers/{id}/invitationTickets/{fk} | Update a related item by id for invitationTickets.
[**customers_id_invitation_tickets_get**](CustomerApi.md#customers_id_invitation_tickets_get) | **GET** /Customers/{id}/invitationTickets | Queries invitationTickets of Customer.
[**customers_id_invitation_tickets_post**](CustomerApi.md#customers_id_invitation_tickets_post) | **POST** /Customers/{id}/invitationTickets | Creates a new instance in invitationTickets of this model.
[**customers_id_patch**](CustomerApi.md#customers_id_patch) | **PATCH** /Customers/{id} | Patch attributes for a model instance and persist it into the data source.
[**customers_id_permission_delete**](CustomerApi.md#customers_id_permission_delete) | **DELETE** /Customers/{id}/permission | Deletes permission of this model.
[**customers_id_permission_get**](CustomerApi.md#customers_id_permission_get) | **GET** /Customers/{id}/permission | Fetches hasOne relation permission.
[**customers_id_permission_post**](CustomerApi.md#customers_id_permission_post) | **POST** /Customers/{id}/permission | Creates a new instance in permission of this model.
[**customers_id_permission_put**](CustomerApi.md#customers_id_permission_put) | **PUT** /Customers/{id}/permission | Update permission of this model.
[**customers_id_profile_picture_put**](CustomerApi.md#customers_id_profile_picture_put) | **PUT** /Customers/{id}/profilePicture | Change profile picture
[**customers_id_put**](CustomerApi.md#customers_id_put) | **PUT** /Customers/{id} | Replace attributes for a model instance and persist it into the data source.
[**customers_id_replace_post**](CustomerApi.md#customers_id_replace_post) | **POST** /Customers/{id}/replace | Replace attributes for a model instance and persist it into the data source.
[**customers_id_teams_count_get**](CustomerApi.md#customers_id_teams_count_get) | **GET** /Customers/{id}/teams/count | Counts teams of Customer.
[**customers_id_teams_delete**](CustomerApi.md#customers_id_teams_delete) | **DELETE** /Customers/{id}/teams | Deletes all teams of this model.
[**customers_id_teams_fk_delete**](CustomerApi.md#customers_id_teams_fk_delete) | **DELETE** /Customers/{id}/teams/{fk} | Delete a related item by id for teams.
[**customers_id_teams_fk_get**](CustomerApi.md#customers_id_teams_fk_get) | **GET** /Customers/{id}/teams/{fk} | Find a related item by id for teams.
[**customers_id_teams_fk_put**](CustomerApi.md#customers_id_teams_fk_put) | **PUT** /Customers/{id}/teams/{fk} | Update a related item by id for teams.
[**customers_id_teams_get**](CustomerApi.md#customers_id_teams_get) | **GET** /Customers/{id}/teams | Queries teams of Customer.
[**customers_id_teams_nk_brand_delete**](CustomerApi.md#customers_id_teams_nk_brand_delete) | **DELETE** /Customers/{id}/teams/{nk}/brand | Deletes brand of this model.
[**customers_id_teams_nk_brand_get**](CustomerApi.md#customers_id_teams_nk_brand_get) | **GET** /Customers/{id}/teams/{nk}/brand | Fetches hasOne relation brand.
[**customers_id_teams_nk_brand_post**](CustomerApi.md#customers_id_teams_nk_brand_post) | **POST** /Customers/{id}/teams/{nk}/brand | Creates a new instance in brand of this model.
[**customers_id_teams_nk_brand_put**](CustomerApi.md#customers_id_teams_nk_brand_put) | **PUT** /Customers/{id}/teams/{nk}/brand | Update brand of this model.
[**customers_id_teams_nk_image_folders_count_get**](CustomerApi.md#customers_id_teams_nk_image_folders_count_get) | **GET** /Customers/{id}/teams/{nk}/imageFolders/count | Counts imageFolders of Team.
[**customers_id_teams_nk_image_folders_delete**](CustomerApi.md#customers_id_teams_nk_image_folders_delete) | **DELETE** /Customers/{id}/teams/{nk}/imageFolders | Deletes all imageFolders of this model.
[**customers_id_teams_nk_image_folders_fk_delete**](CustomerApi.md#customers_id_teams_nk_image_folders_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/imageFolders/{fk} | Delete a related item by id for imageFolders.
[**customers_id_teams_nk_image_folders_fk_get**](CustomerApi.md#customers_id_teams_nk_image_folders_fk_get) | **GET** /Customers/{id}/teams/{nk}/imageFolders/{fk} | Find a related item by id for imageFolders.
[**customers_id_teams_nk_image_folders_fk_put**](CustomerApi.md#customers_id_teams_nk_image_folders_fk_put) | **PUT** /Customers/{id}/teams/{nk}/imageFolders/{fk} | Update a related item by id for imageFolders.
[**customers_id_teams_nk_image_folders_get**](CustomerApi.md#customers_id_teams_nk_image_folders_get) | **GET** /Customers/{id}/teams/{nk}/imageFolders | Queries imageFolders of Team.
[**customers_id_teams_nk_image_folders_post**](CustomerApi.md#customers_id_teams_nk_image_folders_post) | **POST** /Customers/{id}/teams/{nk}/imageFolders | Creates a new instance in imageFolders of this model.
[**customers_id_teams_nk_images_count_get**](CustomerApi.md#customers_id_teams_nk_images_count_get) | **GET** /Customers/{id}/teams/{nk}/images/count | Counts images of Team.
[**customers_id_teams_nk_images_delete**](CustomerApi.md#customers_id_teams_nk_images_delete) | **DELETE** /Customers/{id}/teams/{nk}/images | Deletes all images of this model.
[**customers_id_teams_nk_images_fk_delete**](CustomerApi.md#customers_id_teams_nk_images_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/images/{fk} | Delete a related item by id for images.
[**customers_id_teams_nk_images_fk_get**](CustomerApi.md#customers_id_teams_nk_images_fk_get) | **GET** /Customers/{id}/teams/{nk}/images/{fk} | Find a related item by id for images.
[**customers_id_teams_nk_images_fk_put**](CustomerApi.md#customers_id_teams_nk_images_fk_put) | **PUT** /Customers/{id}/teams/{nk}/images/{fk} | Update a related item by id for images.
[**customers_id_teams_nk_images_get**](CustomerApi.md#customers_id_teams_nk_images_get) | **GET** /Customers/{id}/teams/{nk}/images | Queries images of Team.
[**customers_id_teams_nk_images_post**](CustomerApi.md#customers_id_teams_nk_images_post) | **POST** /Customers/{id}/teams/{nk}/images | Creates a new instance in images of this model.
[**customers_id_teams_nk_members_count_get**](CustomerApi.md#customers_id_teams_nk_members_count_get) | **GET** /Customers/{id}/teams/{nk}/members/count | Counts members of Team.
[**customers_id_teams_nk_members_delete**](CustomerApi.md#customers_id_teams_nk_members_delete) | **DELETE** /Customers/{id}/teams/{nk}/members | Deletes all members of this model.
[**customers_id_teams_nk_members_fk_delete**](CustomerApi.md#customers_id_teams_nk_members_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/members/{fk} | Delete a related item by id for members.
[**customers_id_teams_nk_members_fk_get**](CustomerApi.md#customers_id_teams_nk_members_fk_get) | **GET** /Customers/{id}/teams/{nk}/members/{fk} | Find a related item by id for members.
[**customers_id_teams_nk_members_fk_put**](CustomerApi.md#customers_id_teams_nk_members_fk_put) | **PUT** /Customers/{id}/teams/{nk}/members/{fk} | Update a related item by id for members.
[**customers_id_teams_nk_members_get**](CustomerApi.md#customers_id_teams_nk_members_get) | **GET** /Customers/{id}/teams/{nk}/members | Queries members of Team.
[**customers_id_teams_nk_members_post**](CustomerApi.md#customers_id_teams_nk_members_post) | **POST** /Customers/{id}/teams/{nk}/members | Creates a new instance in members of this model.
[**customers_id_teams_nk_members_rel_fk_delete**](CustomerApi.md#customers_id_teams_nk_members_rel_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/members/rel/{fk} | Remove the members relation to an item by id.
[**customers_id_teams_nk_members_rel_fk_head**](CustomerApi.md#customers_id_teams_nk_members_rel_fk_head) | **HEAD** /Customers/{id}/teams/{nk}/members/rel/{fk} | Check the existence of members relation to an item by id.
[**customers_id_teams_nk_members_rel_fk_put**](CustomerApi.md#customers_id_teams_nk_members_rel_fk_put) | **PUT** /Customers/{id}/teams/{nk}/members/rel/{fk} | Add a related item by id for members.
[**customers_id_teams_nk_portals_count_get**](CustomerApi.md#customers_id_teams_nk_portals_count_get) | **GET** /Customers/{id}/teams/{nk}/portals/count | Counts portals of Team.
[**customers_id_teams_nk_portals_delete**](CustomerApi.md#customers_id_teams_nk_portals_delete) | **DELETE** /Customers/{id}/teams/{nk}/portals | Deletes all portals of this model.
[**customers_id_teams_nk_portals_fk_delete**](CustomerApi.md#customers_id_teams_nk_portals_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/portals/{fk} | Delete a related item by id for portals.
[**customers_id_teams_nk_portals_fk_get**](CustomerApi.md#customers_id_teams_nk_portals_fk_get) | **GET** /Customers/{id}/teams/{nk}/portals/{fk} | Find a related item by id for portals.
[**customers_id_teams_nk_portals_fk_put**](CustomerApi.md#customers_id_teams_nk_portals_fk_put) | **PUT** /Customers/{id}/teams/{nk}/portals/{fk} | Update a related item by id for portals.
[**customers_id_teams_nk_portals_get**](CustomerApi.md#customers_id_teams_nk_portals_get) | **GET** /Customers/{id}/teams/{nk}/portals | Queries portals of Team.
[**customers_id_teams_nk_portals_post**](CustomerApi.md#customers_id_teams_nk_portals_post) | **POST** /Customers/{id}/teams/{nk}/portals | Creates a new instance in portals of this model.
[**customers_id_teams_nk_team_members_count_get**](CustomerApi.md#customers_id_teams_nk_team_members_count_get) | **GET** /Customers/{id}/teams/{nk}/teamMembers/count | Counts teamMembers of Team.
[**customers_id_teams_nk_team_members_delete**](CustomerApi.md#customers_id_teams_nk_team_members_delete) | **DELETE** /Customers/{id}/teams/{nk}/teamMembers | Deletes all teamMembers of this model.
[**customers_id_teams_nk_team_members_fk_delete**](CustomerApi.md#customers_id_teams_nk_team_members_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/teamMembers/{fk} | Delete a related item by id for teamMembers.
[**customers_id_teams_nk_team_members_fk_get**](CustomerApi.md#customers_id_teams_nk_team_members_fk_get) | **GET** /Customers/{id}/teams/{nk}/teamMembers/{fk} | Find a related item by id for teamMembers.
[**customers_id_teams_nk_team_members_fk_put**](CustomerApi.md#customers_id_teams_nk_team_members_fk_put) | **PUT** /Customers/{id}/teams/{nk}/teamMembers/{fk} | Update a related item by id for teamMembers.
[**customers_id_teams_nk_team_members_get**](CustomerApi.md#customers_id_teams_nk_team_members_get) | **GET** /Customers/{id}/teams/{nk}/teamMembers | Queries teamMembers of Team.
[**customers_id_teams_nk_team_members_post**](CustomerApi.md#customers_id_teams_nk_team_members_post) | **POST** /Customers/{id}/teams/{nk}/teamMembers | Creates a new instance in teamMembers of this model.
[**customers_id_teams_nk_template_folders_count_get**](CustomerApi.md#customers_id_teams_nk_template_folders_count_get) | **GET** /Customers/{id}/teams/{nk}/templateFolders/count | Counts templateFolders of Team.
[**customers_id_teams_nk_template_folders_delete**](CustomerApi.md#customers_id_teams_nk_template_folders_delete) | **DELETE** /Customers/{id}/teams/{nk}/templateFolders | Deletes all templateFolders of this model.
[**customers_id_teams_nk_template_folders_fk_delete**](CustomerApi.md#customers_id_teams_nk_template_folders_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/templateFolders/{fk} | Delete a related item by id for templateFolders.
[**customers_id_teams_nk_template_folders_fk_get**](CustomerApi.md#customers_id_teams_nk_template_folders_fk_get) | **GET** /Customers/{id}/teams/{nk}/templateFolders/{fk} | Find a related item by id for templateFolders.
[**customers_id_teams_nk_template_folders_fk_put**](CustomerApi.md#customers_id_teams_nk_template_folders_fk_put) | **PUT** /Customers/{id}/teams/{nk}/templateFolders/{fk} | Update a related item by id for templateFolders.
[**customers_id_teams_nk_template_folders_get**](CustomerApi.md#customers_id_teams_nk_template_folders_get) | **GET** /Customers/{id}/teams/{nk}/templateFolders | Queries templateFolders of Team.
[**customers_id_teams_nk_template_folders_post**](CustomerApi.md#customers_id_teams_nk_template_folders_post) | **POST** /Customers/{id}/teams/{nk}/templateFolders | Creates a new instance in templateFolders of this model.
[**customers_id_teams_nk_templates_count_get**](CustomerApi.md#customers_id_teams_nk_templates_count_get) | **GET** /Customers/{id}/teams/{nk}/templates/count | Counts templates of Team.
[**customers_id_teams_nk_templates_delete**](CustomerApi.md#customers_id_teams_nk_templates_delete) | **DELETE** /Customers/{id}/teams/{nk}/templates | Deletes all templates of this model.
[**customers_id_teams_nk_templates_fk_delete**](CustomerApi.md#customers_id_teams_nk_templates_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/templates/{fk} | Delete a related item by id for templates.
[**customers_id_teams_nk_templates_fk_get**](CustomerApi.md#customers_id_teams_nk_templates_fk_get) | **GET** /Customers/{id}/teams/{nk}/templates/{fk} | Find a related item by id for templates.
[**customers_id_teams_nk_templates_fk_put**](CustomerApi.md#customers_id_teams_nk_templates_fk_put) | **PUT** /Customers/{id}/teams/{nk}/templates/{fk} | Update a related item by id for templates.
[**customers_id_teams_nk_templates_get**](CustomerApi.md#customers_id_teams_nk_templates_get) | **GET** /Customers/{id}/teams/{nk}/templates | Queries templates of Team.
[**customers_id_teams_nk_templates_post**](CustomerApi.md#customers_id_teams_nk_templates_post) | **POST** /Customers/{id}/teams/{nk}/templates | Creates a new instance in templates of this model.
[**customers_id_teams_nk_workflows_count_get**](CustomerApi.md#customers_id_teams_nk_workflows_count_get) | **GET** /Customers/{id}/teams/{nk}/workflows/count | Counts workflows of Team.
[**customers_id_teams_nk_workflows_delete**](CustomerApi.md#customers_id_teams_nk_workflows_delete) | **DELETE** /Customers/{id}/teams/{nk}/workflows | Deletes all workflows of this model.
[**customers_id_teams_nk_workflows_fk_delete**](CustomerApi.md#customers_id_teams_nk_workflows_fk_delete) | **DELETE** /Customers/{id}/teams/{nk}/workflows/{fk} | Delete a related item by id for workflows.
[**customers_id_teams_nk_workflows_fk_get**](CustomerApi.md#customers_id_teams_nk_workflows_fk_get) | **GET** /Customers/{id}/teams/{nk}/workflows/{fk} | Find a related item by id for workflows.
[**customers_id_teams_nk_workflows_fk_put**](CustomerApi.md#customers_id_teams_nk_workflows_fk_put) | **PUT** /Customers/{id}/teams/{nk}/workflows/{fk} | Update a related item by id for workflows.
[**customers_id_teams_nk_workflows_get**](CustomerApi.md#customers_id_teams_nk_workflows_get) | **GET** /Customers/{id}/teams/{nk}/workflows | Queries workflows of Team.
[**customers_id_teams_nk_workflows_post**](CustomerApi.md#customers_id_teams_nk_workflows_post) | **POST** /Customers/{id}/teams/{nk}/workflows | Creates a new instance in workflows of this model.
[**customers_id_teams_post**](CustomerApi.md#customers_id_teams_post) | **POST** /Customers/{id}/teams | Creates a new instance in teams of this model.
[**customers_id_teams_rel_fk_delete**](CustomerApi.md#customers_id_teams_rel_fk_delete) | **DELETE** /Customers/{id}/teams/rel/{fk} | Remove the teams relation to an item by id.
[**customers_id_teams_rel_fk_head**](CustomerApi.md#customers_id_teams_rel_fk_head) | **HEAD** /Customers/{id}/teams/rel/{fk} | Check the existence of teams relation to an item by id.
[**customers_id_teams_rel_fk_put**](CustomerApi.md#customers_id_teams_rel_fk_put) | **PUT** /Customers/{id}/teams/rel/{fk} | Add a related item by id for teams.
[**customers_id_teams_team_id_change_post**](CustomerApi.md#customers_id_teams_team_id_change_post) | **POST** /Customers/{id}/teams/{teamId}/change | Move authentication to a Team
[**customers_id_teams_team_id_portals_portal_id_change_post**](CustomerApi.md#customers_id_teams_team_id_portals_portal_id_change_post) | **POST** /Customers/{id}/teams/{teamId}/portals/{portalId}/change | Move authentication to a Portal
[**customers_id_token_get**](CustomerApi.md#customers_id_token_get) | **GET** /Customers/{id}/token | Get token info
[**customers_id_verify_post**](CustomerApi.md#customers_id_verify_post) | **POST** /Customers/{id}/verify | Trigger user&#39;s identity verification with configured verifyOptions
[**customers_invitation_tickets_token_accept_post**](CustomerApi.md#customers_invitation_tickets_token_accept_post) | **POST** /Customers/invitationTickets/{token}/accept | Accept invitation with token
[**customers_invitation_tickets_token_get**](CustomerApi.md#customers_invitation_tickets_token_get) | **GET** /Customers/invitationTickets/{token} | Get invitation details with token
[**customers_login_post**](CustomerApi.md#customers_login_post) | **POST** /Customers/login | Login a user with username/email and password.
[**customers_logout_post**](CustomerApi.md#customers_logout_post) | **POST** /Customers/logout | Logout a user with access token.
[**customers_patch**](CustomerApi.md#customers_patch) | **PATCH** /Customers | Patch an existing model instance or insert a new one into the data source.
[**customers_post**](CustomerApi.md#customers_post) | **POST** /Customers | Create a new instance of the model and persist it into the data source.
[**customers_put**](CustomerApi.md#customers_put) | **PUT** /Customers | Replace an existing model instance or insert a new one into the data source.
[**customers_register_post**](CustomerApi.md#customers_register_post) | **POST** /Customers/register | Create customer and assign it to a team
[**customers_replace_or_create_post**](CustomerApi.md#customers_replace_or_create_post) | **POST** /Customers/replaceOrCreate | Replace an existing model instance or insert a new one into the data source.
[**customers_reset_password_post**](CustomerApi.md#customers_reset_password_post) | **POST** /Customers/reset-password | Reset user&#39;s password via a password-reset token.
[**customers_reset_post**](CustomerApi.md#customers_reset_post) | **POST** /Customers/reset | Reset password for a user with email.
[**customers_update_post**](CustomerApi.md#customers_update_post) | **POST** /Customers/update | Update instances of the model matched by {{where}} from the data source.
[**customers_upsert_with_where_post**](CustomerApi.md#customers_upsert_with_where_post) | **POST** /Customers/upsertWithWhere | Update an existing model instance or insert a new one into the data source based on the where criteria.


# **customers_change_password_post**
> customers_change_password_post(old_password, new_password)

Change a user's password.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
old_password = 'old_password_example' # str | 
new_password = 'new_password_example' # str | 

try: 
    # Change a user's password.
    api_instance.customers_change_password_post(old_password, new_password)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_password** | **str**|  | 
 **new_password** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_change_stream_get**
> file customers_change_stream_get(options=options)

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
api_instance = TweakApi.CustomerApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.customers_change_stream_get(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_change_stream_get: %s\n" % e)
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

# **customers_change_stream_post**
> file customers_change_stream_post(options=options)

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
api_instance = TweakApi.CustomerApi()
options = 'options_example' # str |  (optional)

try: 
    # Create a change stream.
    api_response = api_instance.customers_change_stream_post(options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_change_stream_post: %s\n" % e)
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

# **customers_confirm_get**
> customers_confirm_get(uid, token, redirect=redirect)

Confirm a user registration with identity verification token.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
uid = 'uid_example' # str | 
token = 'token_example' # str | 
redirect = 'redirect_example' # str |  (optional)

try: 
    # Confirm a user registration with identity verification token.
    api_instance.customers_confirm_get(uid, token, redirect=redirect)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_confirm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **token** | **str**|  | 
 **redirect** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_count_get**
> InlineResponse200 customers_count_get(where=where)

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
api_instance = TweakApi.CustomerApi()
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Count instances of the model matched by where from the data source.
    api_response = api_instance.customers_count_get(where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_count_get: %s\n" % e)
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

# **customers_find_one_get**
> Customer customers_find_one_get(filter=filter)

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
api_instance = TweakApi.CustomerApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find first instance of the model matched by filter from the data source.
    api_response = api_instance.customers_find_one_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_find_one_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_get**
> list[Customer] customers_get(filter=filter)

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
api_instance = TweakApi.CustomerApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.customers_get(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_access_tokens_count_get**
> InlineResponse200 customers_id_access_tokens_count_get(id, where=where)

Counts accessTokens of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts accessTokens of Customer.
    api_response = api_instance.customers_id_access_tokens_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_access_tokens_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_access_tokens_delete**
> customers_id_access_tokens_delete(id)

Deletes all accessTokens of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id

try: 
    # Deletes all accessTokens of this model.
    api_instance.customers_id_access_tokens_delete(id)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_access_tokens_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_access_tokens_fk_delete**
> customers_id_access_tokens_fk_delete(id, fk)

Delete a related item by id for accessTokens.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for accessTokens

try: 
    # Delete a related item by id for accessTokens.
    api_instance.customers_id_access_tokens_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_access_tokens_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for accessTokens | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_access_tokens_fk_get**
> TeamMemberAccessToken customers_id_access_tokens_fk_get(id, fk)

Find a related item by id for accessTokens.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for accessTokens

try: 
    # Find a related item by id for accessTokens.
    api_response = api_instance.customers_id_access_tokens_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_access_tokens_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for accessTokens | 

### Return type

[**TeamMemberAccessToken**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_access_tokens_fk_put**
> TeamMemberAccessToken customers_id_access_tokens_fk_put(id, fk, data=data)

Update a related item by id for accessTokens.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for accessTokens
data = TweakApi.TeamMemberAccessToken() # TeamMemberAccessToken |  (optional)

try: 
    # Update a related item by id for accessTokens.
    api_response = api_instance.customers_id_access_tokens_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_access_tokens_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for accessTokens | 
 **data** | [**TeamMemberAccessToken**](TeamMemberAccessToken.md)|  | [optional] 

### Return type

[**TeamMemberAccessToken**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_access_tokens_get**
> list[TeamMemberAccessToken] customers_id_access_tokens_get(id, filter=filter)

Queries accessTokens of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries accessTokens of Customer.
    api_response = api_instance.customers_id_access_tokens_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_access_tokens_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMemberAccessToken]**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_access_tokens_post**
> TeamMemberAccessToken customers_id_access_tokens_post(id, data=data)

Creates a new instance in accessTokens of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
data = TweakApi.TeamMemberAccessToken() # TeamMemberAccessToken |  (optional)

try: 
    # Creates a new instance in accessTokens of this model.
    api_response = api_instance.customers_id_access_tokens_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_access_tokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **data** | [**TeamMemberAccessToken**](TeamMemberAccessToken.md)|  | [optional] 

### Return type

[**TeamMemberAccessToken**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_active_get**
> InlineResponse2003 customers_id_active_get(id)

Define whether customer is active or not

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id or email

try: 
    # Define whether customer is active or not
    api_response = api_instance.customers_id_active_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id or email | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_delete**
> object customers_id_delete(id)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Model id

try: 
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.customers_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_delete: %s\n" % e)
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

# **customers_id_designs_count_get**
> InlineResponse200 customers_id_designs_count_get(id, where=where)

Counts designs of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts designs of Customer.
    api_response = api_instance.customers_id_designs_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_designs_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_designs_delete**
> customers_id_designs_delete(id)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id

try: 
    # Deletes all designs of this model.
    api_instance.customers_id_designs_delete(id)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_designs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_designs_fk_delete**
> customers_id_designs_fk_delete(id, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Delete a related item by id for designs.
    api_instance.customers_id_designs_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_designs_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_designs_fk_get**
> Design customers_id_designs_fk_get(id, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for designs

try: 
    # Find a related item by id for designs.
    api_response = api_instance.customers_id_designs_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_designs_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for designs | 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_designs_fk_put**
> Design customers_id_designs_fk_put(id, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for designs
data = TweakApi.Design() # Design |  (optional)

try: 
    # Update a related item by id for designs.
    api_response = api_instance.customers_id_designs_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_designs_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
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

# **customers_id_designs_get**
> list[Design] customers_id_designs_get(id, filter=filter)

Queries designs of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries designs of Customer.
    api_response = api_instance.customers_id_designs_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_designs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Design]**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_designs_post**
> Design customers_id_designs_post(id, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
data = TweakApi.Design() # Design |  (optional)

try: 
    # Creates a new instance in designs of this model.
    api_response = api_instance.customers_id_designs_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_designs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **data** | [**Design**](Design.md)|  | [optional] 

### Return type

[**Design**](Design.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_exists_get**
> InlineResponse2002 customers_id_exists_get(id)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.customers_id_exists_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_exists_get: %s\n" % e)
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

# **customers_id_get**
> Customer customers_id_get(id, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try: 
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.customers_id_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_head**
> InlineResponse2002 customers_id_head(id)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Model id

try: 
    # Check whether a model instance exists in the data source.
    api_response = api_instance.customers_id_head(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_head: %s\n" % e)
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

# **customers_id_invitation_tickets_count_get**
> InlineResponse200 customers_id_invitation_tickets_count_get(id, where=where)

Counts invitationTickets of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts invitationTickets of Customer.
    api_response = api_instance.customers_id_invitation_tickets_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_invitation_tickets_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_invitation_tickets_delete**
> customers_id_invitation_tickets_delete(id)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id

try: 
    # Deletes all invitationTickets of this model.
    api_instance.customers_id_invitation_tickets_delete(id)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_invitation_tickets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_invitation_tickets_fk_delete**
> customers_id_invitation_tickets_fk_delete(id, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for invitationTickets

try: 
    # Delete a related item by id for invitationTickets.
    api_instance.customers_id_invitation_tickets_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_invitation_tickets_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for invitationTickets | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_invitation_tickets_fk_get**
> InvitationTicket customers_id_invitation_tickets_fk_get(id, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for invitationTickets

try: 
    # Find a related item by id for invitationTickets.
    api_response = api_instance.customers_id_invitation_tickets_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_invitation_tickets_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for invitationTickets | 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_invitation_tickets_fk_put**
> InvitationTicket customers_id_invitation_tickets_fk_put(id, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for invitationTickets
data = TweakApi.InvitationTicket() # InvitationTicket |  (optional)

try: 
    # Update a related item by id for invitationTickets.
    api_response = api_instance.customers_id_invitation_tickets_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_invitation_tickets_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
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

# **customers_id_invitation_tickets_get**
> list[InvitationTicket] customers_id_invitation_tickets_get(id, filter=filter)

Queries invitationTickets of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries invitationTickets of Customer.
    api_response = api_instance.customers_id_invitation_tickets_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_invitation_tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[InvitationTicket]**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_invitation_tickets_post**
> InvitationTicket customers_id_invitation_tickets_post(id, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
data = TweakApi.InvitationTicket() # InvitationTicket |  (optional)

try: 
    # Creates a new instance in invitationTickets of this model.
    api_response = api_instance.customers_id_invitation_tickets_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_invitation_tickets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **data** | [**InvitationTicket**](InvitationTicket.md)|  | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_patch**
> Customer customers_id_patch(id, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
data = TweakApi.Customer() # Customer | An object of model property name/value pairs (optional)

try: 
    # Patch attributes for a model instance and persist it into the data source.
    api_response = api_instance.customers_id_patch(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **data** | [**Customer**](Customer.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_permission_delete**
> customers_id_permission_delete(id)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id

try: 
    # Deletes permission of this model.
    api_instance.customers_id_permission_delete(id)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_permission_get**
> CustomerPermissionSet customers_id_permission_get(id, refresh=refresh)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation permission.
    api_response = api_instance.customers_id_permission_get(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_permission_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**CustomerPermissionSet**](CustomerPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_permission_post**
> CustomerPermissionSet customers_id_permission_post(id, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
data = TweakApi.CustomerPermissionSet() # CustomerPermissionSet |  (optional)

try: 
    # Creates a new instance in permission of this model.
    api_response = api_instance.customers_id_permission_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_permission_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **data** | [**CustomerPermissionSet**](CustomerPermissionSet.md)|  | [optional] 

### Return type

[**CustomerPermissionSet**](CustomerPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_permission_put**
> CustomerPermissionSet customers_id_permission_put(id, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
data = TweakApi.CustomerPermissionSet() # CustomerPermissionSet |  (optional)

try: 
    # Update permission of this model.
    api_response = api_instance.customers_id_permission_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **data** | [**CustomerPermissionSet**](CustomerPermissionSet.md)|  | [optional] 

### Return type

[**CustomerPermissionSet**](CustomerPermissionSet.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_profile_picture_put**
> Customer customers_id_profile_picture_put(id, id2, data)

Change profile picture

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
id2 = 'id_example' # str | Customer id
data = TweakApi.Customer() # Customer | Profile picture

try: 
    # Change profile picture
    api_response = api_instance.customers_id_profile_picture_put(id, id2, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_profile_picture_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **id2** | **str**| Customer id | 
 **data** | [**Customer**](Customer.md)| Profile picture | 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_put**
> Customer customers_id_put(id, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Model id
data = TweakApi.Customer() # Customer | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.customers_id_put(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Customer**](Customer.md)| Model instance data | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_replace_post**
> Customer customers_id_replace_post(id, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Model id
data = TweakApi.Customer() # Customer | Model instance data (optional)

try: 
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.customers_id_replace_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**Customer**](Customer.md)| Model instance data | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_count_get**
> InlineResponse200 customers_id_teams_count_get(id, where=where)

Counts teams of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts teams of Customer.
    api_response = api_instance.customers_id_teams_count_get(id, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_delete**
> customers_id_teams_delete(id)

Deletes all teams of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id

try: 
    # Deletes all teams of this model.
    api_instance.customers_id_teams_delete(id)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_fk_delete**
> customers_id_teams_fk_delete(id, fk)

Delete a related item by id for teams.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for teams

try: 
    # Delete a related item by id for teams.
    api_instance.customers_id_teams_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for teams | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_fk_get**
> Team customers_id_teams_fk_get(id, fk)

Find a related item by id for teams.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for teams

try: 
    # Find a related item by id for teams.
    api_response = api_instance.customers_id_teams_fk_get(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for teams | 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_fk_put**
> Team customers_id_teams_fk_put(id, fk, data=data)

Update a related item by id for teams.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for teams
data = TweakApi.Team() # Team |  (optional)

try: 
    # Update a related item by id for teams.
    api_response = api_instance.customers_id_teams_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for teams | 
 **data** | [**Team**](Team.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_get**
> list[Team] customers_id_teams_get(id, filter=filter)

Queries teams of Customer.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
filter = 'filter_example' # str |  (optional)

try: 
    # Queries teams of Customer.
    api_response = api_instance.customers_id_teams_get(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Team]**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_brand_delete**
> customers_id_teams_nk_brand_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes brand of this model.
    api_instance.customers_id_teams_nk_brand_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_brand_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_brand_get**
> TeamBrand customers_id_teams_nk_brand_get(id, nk, refresh=refresh)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
refresh = true # bool |  (optional)

try: 
    # Fetches hasOne relation brand.
    api_response = api_instance.customers_id_teams_nk_brand_get(id, nk, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_brand_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_brand_post**
> TeamBrand customers_id_teams_nk_brand_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.TeamBrand() # TeamBrand |  (optional)

try: 
    # Creates a new instance in brand of this model.
    api_response = api_instance.customers_id_teams_nk_brand_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_brand_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**TeamBrand**](TeamBrand.md)|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_brand_put**
> TeamBrand customers_id_teams_nk_brand_put(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.TeamBrand() # TeamBrand |  (optional)

try: 
    # Update brand of this model.
    api_response = api_instance.customers_id_teams_nk_brand_put(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_brand_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**TeamBrand**](TeamBrand.md)|  | [optional] 

### Return type

[**TeamBrand**](TeamBrand.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_image_folders_count_get**
> InlineResponse200 customers_id_teams_nk_image_folders_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts imageFolders of Team.
    api_response = api_instance.customers_id_teams_nk_image_folders_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_image_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_image_folders_delete**
> customers_id_teams_nk_image_folders_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all imageFolders of this model.
    api_instance.customers_id_teams_nk_image_folders_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_image_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_image_folders_fk_delete**
> customers_id_teams_nk_image_folders_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Delete a related item by id for imageFolders.
    api_instance.customers_id_teams_nk_image_folders_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_image_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_image_folders_fk_get**
> ImageFolder customers_id_teams_nk_image_folders_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for imageFolders

try: 
    # Find a related item by id for imageFolders.
    api_response = api_instance.customers_id_teams_nk_image_folders_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_image_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for imageFolders | 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_image_folders_fk_put**
> ImageFolder customers_id_teams_nk_image_folders_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for imageFolders
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Update a related item by id for imageFolders.
    api_response = api_instance.customers_id_teams_nk_image_folders_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_image_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_image_folders_get**
> list[ImageFolder] customers_id_teams_nk_image_folders_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries imageFolders of Team.
    api_response = api_instance.customers_id_teams_nk_image_folders_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_image_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[ImageFolder]**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_image_folders_post**
> ImageFolder customers_id_teams_nk_image_folders_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.ImageFolder() # ImageFolder |  (optional)

try: 
    # Creates a new instance in imageFolders of this model.
    api_response = api_instance.customers_id_teams_nk_image_folders_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_image_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**ImageFolder**](ImageFolder.md)|  | [optional] 

### Return type

[**ImageFolder**](ImageFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_images_count_get**
> InlineResponse200 customers_id_teams_nk_images_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts images of Team.
    api_response = api_instance.customers_id_teams_nk_images_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_images_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_images_delete**
> customers_id_teams_nk_images_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all images of this model.
    api_instance.customers_id_teams_nk_images_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_images_fk_delete**
> customers_id_teams_nk_images_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for images

try: 
    # Delete a related item by id for images.
    api_instance.customers_id_teams_nk_images_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_images_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for images | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_images_fk_get**
> Image customers_id_teams_nk_images_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for images

try: 
    # Find a related item by id for images.
    api_response = api_instance.customers_id_teams_nk_images_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_images_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for images | 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_images_fk_put**
> Image customers_id_teams_nk_images_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for images
data = TweakApi.Image() # Image |  (optional)

try: 
    # Update a related item by id for images.
    api_response = api_instance.customers_id_teams_nk_images_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_images_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_images_get**
> list[Image] customers_id_teams_nk_images_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries images of Team.
    api_response = api_instance.customers_id_teams_nk_images_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_images_post**
> Image customers_id_teams_nk_images_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.Image() # Image |  (optional)

try: 
    # Creates a new instance in images of this model.
    api_response = api_instance.customers_id_teams_nk_images_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**Image**](Image.md)|  | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_count_get**
> InlineResponse200 customers_id_teams_nk_members_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts members of Team.
    api_response = api_instance.customers_id_teams_nk_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_delete**
> customers_id_teams_nk_members_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all members of this model.
    api_instance.customers_id_teams_nk_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_fk_delete**
> customers_id_teams_nk_members_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Delete a related item by id for members.
    api_instance.customers_id_teams_nk_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_fk_get**
> Customer customers_id_teams_nk_members_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Find a related item by id for members.
    api_response = api_instance.customers_id_teams_nk_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for members | 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_fk_put**
> Customer customers_id_teams_nk_members_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.Customer() # Customer |  (optional)

try: 
    # Update a related item by id for members.
    api_response = api_instance.customers_id_teams_nk_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_members_get**
> list[Customer] customers_id_teams_nk_members_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries members of Team.
    api_response = api_instance.customers_id_teams_nk_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_post**
> Customer customers_id_teams_nk_members_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.Customer() # Customer |  (optional)

try: 
    # Creates a new instance in members of this model.
    api_response = api_instance.customers_id_teams_nk_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**Customer**](Customer.md)|  | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_rel_fk_delete**
> customers_id_teams_nk_members_rel_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Remove the members relation to an item by id.
    api_instance.customers_id_teams_nk_members_rel_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for members | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_rel_fk_head**
> bool customers_id_teams_nk_members_rel_fk_head(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for members

try: 
    # Check the existence of members relation to an item by id.
    api_response = api_instance.customers_id_teams_nk_members_rel_fk_head(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for members | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_members_rel_fk_put**
> TeamMember customers_id_teams_nk_members_rel_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for members
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Add a related item by id for members.
    api_response = api_instance.customers_id_teams_nk_members_rel_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_members_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_portals_count_get**
> InlineResponse200 customers_id_teams_nk_portals_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts portals of Team.
    api_response = api_instance.customers_id_teams_nk_portals_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_portals_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_portals_delete**
> customers_id_teams_nk_portals_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all portals of this model.
    api_instance.customers_id_teams_nk_portals_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_portals_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_portals_fk_delete**
> customers_id_teams_nk_portals_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Delete a related item by id for portals.
    api_instance.customers_id_teams_nk_portals_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_portals_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_portals_fk_get**
> Portal customers_id_teams_nk_portals_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for portals

try: 
    # Find a related item by id for portals.
    api_response = api_instance.customers_id_teams_nk_portals_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_portals_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for portals | 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_portals_fk_put**
> Portal customers_id_teams_nk_portals_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for portals
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Update a related item by id for portals.
    api_response = api_instance.customers_id_teams_nk_portals_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_portals_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_portals_get**
> list[Portal] customers_id_teams_nk_portals_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries portals of Team.
    api_response = api_instance.customers_id_teams_nk_portals_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_portals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_portals_post**
> Portal customers_id_teams_nk_portals_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.Portal() # Portal |  (optional)

try: 
    # Creates a new instance in portals of this model.
    api_response = api_instance.customers_id_teams_nk_portals_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_portals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**Portal**](Portal.md)|  | [optional] 

### Return type

[**Portal**](Portal.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_team_members_count_get**
> InlineResponse200 customers_id_teams_nk_team_members_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts teamMembers of Team.
    api_response = api_instance.customers_id_teams_nk_team_members_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_team_members_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_team_members_delete**
> customers_id_teams_nk_team_members_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all teamMembers of this model.
    api_instance.customers_id_teams_nk_team_members_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_team_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_team_members_fk_delete**
> customers_id_teams_nk_team_members_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for teamMembers

try: 
    # Delete a related item by id for teamMembers.
    api_instance.customers_id_teams_nk_team_members_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_team_members_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for teamMembers | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_team_members_fk_get**
> TeamMember customers_id_teams_nk_team_members_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for teamMembers

try: 
    # Find a related item by id for teamMembers.
    api_response = api_instance.customers_id_teams_nk_team_members_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_team_members_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for teamMembers | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_team_members_fk_put**
> TeamMember customers_id_teams_nk_team_members_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for teamMembers
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Update a related item by id for teamMembers.
    api_response = api_instance.customers_id_teams_nk_team_members_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_team_members_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_team_members_get**
> list[TeamMember] customers_id_teams_nk_team_members_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries teamMembers of Team.
    api_response = api_instance.customers_id_teams_nk_team_members_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_team_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamMember]**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_team_members_post**
> TeamMember customers_id_teams_nk_team_members_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Creates a new instance in teamMembers of this model.
    api_response = api_instance.customers_id_teams_nk_team_members_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_template_folders_count_get**
> InlineResponse200 customers_id_teams_nk_template_folders_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templateFolders of Team.
    api_response = api_instance.customers_id_teams_nk_template_folders_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_template_folders_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_template_folders_delete**
> customers_id_teams_nk_template_folders_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all templateFolders of this model.
    api_instance.customers_id_teams_nk_template_folders_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_template_folders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_template_folders_fk_delete**
> customers_id_teams_nk_template_folders_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Delete a related item by id for templateFolders.
    api_instance.customers_id_teams_nk_template_folders_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_template_folders_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_template_folders_fk_get**
> TeamTemplateFolder customers_id_teams_nk_template_folders_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for templateFolders

try: 
    # Find a related item by id for templateFolders.
    api_response = api_instance.customers_id_teams_nk_template_folders_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_template_folders_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for templateFolders | 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_template_folders_fk_put**
> TeamTemplateFolder customers_id_teams_nk_template_folders_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for templateFolders
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Update a related item by id for templateFolders.
    api_response = api_instance.customers_id_teams_nk_template_folders_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_template_folders_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_template_folders_get**
> list[TeamTemplateFolder] customers_id_teams_nk_template_folders_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templateFolders of Team.
    api_response = api_instance.customers_id_teams_nk_template_folders_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_template_folders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[TeamTemplateFolder]**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_template_folders_post**
> TeamTemplateFolder customers_id_teams_nk_template_folders_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.TeamTemplateFolder() # TeamTemplateFolder |  (optional)

try: 
    # Creates a new instance in templateFolders of this model.
    api_response = api_instance.customers_id_teams_nk_template_folders_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_template_folders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**TeamTemplateFolder**](TeamTemplateFolder.md)|  | [optional] 

### Return type

[**TeamTemplateFolder**](TeamTemplateFolder.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_templates_count_get**
> InlineResponse200 customers_id_teams_nk_templates_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts templates of Team.
    api_response = api_instance.customers_id_teams_nk_templates_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_templates_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_templates_delete**
> customers_id_teams_nk_templates_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all templates of this model.
    api_instance.customers_id_teams_nk_templates_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_templates_fk_delete**
> customers_id_teams_nk_templates_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Delete a related item by id for templates.
    api_instance.customers_id_teams_nk_templates_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_templates_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for templates | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_templates_fk_get**
> Template customers_id_teams_nk_templates_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for templates

try: 
    # Find a related item by id for templates.
    api_response = api_instance.customers_id_teams_nk_templates_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_templates_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for templates | 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_templates_fk_put**
> Template customers_id_teams_nk_templates_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for templates
data = TweakApi.Template() # Template |  (optional)

try: 
    # Update a related item by id for templates.
    api_response = api_instance.customers_id_teams_nk_templates_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_templates_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_templates_get**
> list[Template] customers_id_teams_nk_templates_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries templates of Team.
    api_response = api_instance.customers_id_teams_nk_templates_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_templates_post**
> Template customers_id_teams_nk_templates_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.Template() # Template |  (optional)

try: 
    # Creates a new instance in templates of this model.
    api_response = api_instance.customers_id_teams_nk_templates_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**Template**](Template.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_workflows_count_get**
> InlineResponse200 customers_id_teams_nk_workflows_count_get(id, nk, where=where)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
where = 'where_example' # str | Criteria to match model instances (optional)

try: 
    # Counts workflows of Team.
    api_response = api_instance.customers_id_teams_nk_workflows_count_get(id, nk, where=where)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_workflows_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **where** | **str**| Criteria to match model instances | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_workflows_delete**
> customers_id_teams_nk_workflows_delete(id, nk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.

try: 
    # Deletes all workflows of this model.
    api_instance.customers_id_teams_nk_workflows_delete(id, nk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_workflows_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_workflows_fk_delete**
> customers_id_teams_nk_workflows_fk_delete(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Delete a related item by id for workflows.
    api_instance.customers_id_teams_nk_workflows_fk_delete(id, nk, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_workflows_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_workflows_fk_get**
> Workflow customers_id_teams_nk_workflows_fk_get(id, nk, fk)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for workflows

try: 
    # Find a related item by id for workflows.
    api_response = api_instance.customers_id_teams_nk_workflows_fk_get(id, nk, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_workflows_fk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **fk** | **str**| Foreign key for workflows | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_workflows_fk_put**
> Workflow customers_id_teams_nk_workflows_fk_put(id, nk, fk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
fk = 'fk_example' # str | Foreign key for workflows
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Update a related item by id for workflows.
    api_response = api_instance.customers_id_teams_nk_workflows_fk_put(id, nk, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_workflows_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
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

# **customers_id_teams_nk_workflows_get**
> list[Workflow] customers_id_teams_nk_workflows_get(id, nk, filter=filter)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
filter = 'filter_example' # str |  (optional)

try: 
    # Queries workflows of Team.
    api_response = api_instance.customers_id_teams_nk_workflows_get(id, nk, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_workflows_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **filter** | **str**|  | [optional] 

### Return type

[**list[Workflow]**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_nk_workflows_post**
> Workflow customers_id_teams_nk_workflows_post(id, nk, data=data)

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
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
nk = 'nk_example' # str | Foreign key for teams.
data = TweakApi.Workflow() # Workflow |  (optional)

try: 
    # Creates a new instance in workflows of this model.
    api_response = api_instance.customers_id_teams_nk_workflows_post(id, nk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_nk_workflows_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **nk** | **str**| Foreign key for teams. | 
 **data** | [**Workflow**](Workflow.md)|  | [optional] 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_post**
> Team customers_id_teams_post(id, data=data)

Creates a new instance in teams of this model.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
data = TweakApi.Team() # Team |  (optional)

try: 
    # Creates a new instance in teams of this model.
    api_response = api_instance.customers_id_teams_post(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **data** | [**Team**](Team.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_rel_fk_delete**
> customers_id_teams_rel_fk_delete(id, fk)

Remove the teams relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for teams

try: 
    # Remove the teams relation to an item by id.
    api_instance.customers_id_teams_rel_fk_delete(id, fk)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_rel_fk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for teams | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_rel_fk_head**
> bool customers_id_teams_rel_fk_head(id, fk)

Check the existence of teams relation to an item by id.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for teams

try: 
    # Check the existence of teams relation to an item by id.
    api_response = api_instance.customers_id_teams_rel_fk_head(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_rel_fk_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for teams | 

### Return type

**bool**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_rel_fk_put**
> TeamMember customers_id_teams_rel_fk_put(id, fk, data=data)

Add a related item by id for teams.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
fk = 'fk_example' # str | Foreign key for teams
data = TweakApi.TeamMember() # TeamMember |  (optional)

try: 
    # Add a related item by id for teams.
    api_response = api_instance.customers_id_teams_rel_fk_put(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_rel_fk_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **fk** | **str**| Foreign key for teams | 
 **data** | [**TeamMember**](TeamMember.md)|  | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_team_id_change_post**
> TeamMemberAccessToken customers_id_teams_team_id_change_post(id, id2, team_id)

Move authentication to a Team

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
id2 = 'id_example' # str | Customer id
team_id = 'team_id_example' # str | Team id

try: 
    # Move authentication to a Team
    api_response = api_instance.customers_id_teams_team_id_change_post(id, id2, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_team_id_change_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **id2** | **str**| Customer id | 
 **team_id** | **str**| Team id | 

### Return type

[**TeamMemberAccessToken**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_teams_team_id_portals_portal_id_change_post**
> TeamMemberAccessToken customers_id_teams_team_id_portals_portal_id_change_post(id, id2, team_id, portal_id)

Move authentication to a Portal

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
id2 = 'id_example' # str | Customer id
team_id = 'team_id_example' # str | Team id
portal_id = 'portal_id_example' # str | Portal id

try: 
    # Move authentication to a Portal
    api_response = api_instance.customers_id_teams_team_id_portals_portal_id_change_post(id, id2, team_id, portal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_teams_team_id_portals_portal_id_change_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **id2** | **str**| Customer id | 
 **team_id** | **str**| Team id | 
 **portal_id** | **str**| Portal id | 

### Return type

[**TeamMemberAccessToken**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_token_get**
> TeamMemberAccessToken customers_id_token_get(id, id2)

Get token info

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id
id2 = 'id_example' # str | Customer id

try: 
    # Get token info
    api_response = api_instance.customers_id_token_get(id, id2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 
 **id2** | **str**| Customer id | 

### Return type

[**TeamMemberAccessToken**](TeamMemberAccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_verify_post**
> customers_id_verify_post(id)

Trigger user's identity verification with configured verifyOptions

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
id = 'id_example' # str | Customer id

try: 
    # Trigger user's identity verification with configured verifyOptions
    api_instance.customers_id_verify_post(id)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_id_verify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer id | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_invitation_tickets_token_accept_post**
> InvitationTicket customers_invitation_tickets_token_accept_post(token, data=data)

Accept invitation with token

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
token = 'token_example' # str | Token describing invitation ticket
data = TweakApi.Customer() # Customer | Customer data in case new customer (optional)

try: 
    # Accept invitation with token
    api_response = api_instance.customers_invitation_tickets_token_accept_post(token, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_invitation_tickets_token_accept_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token describing invitation ticket | 
 **data** | [**Customer**](Customer.md)| Customer data in case new customer | [optional] 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_invitation_tickets_token_get**
> InvitationTicket customers_invitation_tickets_token_get(token)

Get invitation details with token

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
token = 'token_example' # str | Token describing invitation ticket

try: 
    # Get invitation details with token
    api_response = api_instance.customers_invitation_tickets_token_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_invitation_tickets_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token describing invitation ticket | 

### Return type

[**InvitationTicket**](InvitationTicket.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_login_post**
> object customers_login_post(credentials, include=include)

Login a user with username/email and password.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
credentials = NULL # object | 
include = 'include_example' # str | Related objects to include in the response. See the description of return value for more details. (optional)

try: 
    # Login a user with username/email and password.
    api_response = api_instance.customers_login_post(credentials, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | **object**|  | 
 **include** | **str**| Related objects to include in the response. See the description of return value for more details. | [optional] 

### Return type

**object**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_logout_post**
> customers_logout_post()

Logout a user with access token.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()

try: 
    # Logout a user with access token.
    api_instance.customers_logout_post()
except ApiException as e:
    print("Exception when calling CustomerApi->customers_logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_patch**
> Customer customers_patch(data=data)

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
api_instance = TweakApi.CustomerApi()
data = TweakApi.Customer() # Customer | Model instance data (optional)

try: 
    # Patch an existing model instance or insert a new one into the data source.
    api_response = api_instance.customers_patch(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Customer**](Customer.md)| Model instance data | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_post**
> Customer customers_post(data=data)

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
api_instance = TweakApi.CustomerApi()
data = TweakApi.Customer() # Customer | Model instance data (optional)

try: 
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.customers_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Customer**](Customer.md)| Model instance data | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_put**
> Customer customers_put(data=data)

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
api_instance = TweakApi.CustomerApi()
data = TweakApi.Customer() # Customer | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.customers_put(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Customer**](Customer.md)| Model instance data | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_register_post**
> TeamMember customers_register_post(data=data)

Create customer and assign it to a team

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
data = TweakApi.Customer() # Customer | Model instance data (optional)

try: 
    # Create customer and assign it to a team
    api_response = api_instance.customers_register_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Customer**](Customer.md)| Model instance data | [optional] 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_replace_or_create_post**
> Customer customers_replace_or_create_post(data=data)

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
api_instance = TweakApi.CustomerApi()
data = TweakApi.Customer() # Customer | Model instance data (optional)

try: 
    # Replace an existing model instance or insert a new one into the data source.
    api_response = api_instance.customers_replace_or_create_post(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_replace_or_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Customer**](Customer.md)| Model instance data | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_reset_password_post**
> customers_reset_password_post(new_password)

Reset user's password via a password-reset token.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
new_password = 'new_password_example' # str | 

try: 
    # Reset user's password via a password-reset token.
    api_instance.customers_reset_password_post(new_password)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_reset_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_password** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_reset_post**
> customers_reset_post(options)

Reset password for a user with email.

### Example 
```python
from __future__ import print_statement
import time
import TweakApi
from TweakApi.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
TweakApi.configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# TweakApi.configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = TweakApi.CustomerApi()
options = NULL # object | 

try: 
    # Reset password for a user with email.
    api_instance.customers_reset_post(options)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_update_post**
> InlineResponse2001 customers_update_post(where=where, data=data)

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
api_instance = TweakApi.CustomerApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Customer() # Customer | An object of model property name/value pairs (optional)

try: 
    # Update instances of the model matched by {{where}} from the data source.
    api_response = api_instance.customers_update_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Customer**](Customer.md)| An object of model property name/value pairs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_upsert_with_where_post**
> Customer customers_upsert_with_where_post(where=where, data=data)

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
api_instance = TweakApi.CustomerApi()
where = 'where_example' # str | Criteria to match model instances (optional)
data = TweakApi.Customer() # Customer | An object of model property name/value pairs (optional)

try: 
    # Update an existing model instance or insert a new one into the data source based on the where criteria.
    api_response = api_instance.customers_upsert_with_where_post(where=where, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_upsert_with_where_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Criteria to match model instances | [optional] 
 **data** | [**Customer**](Customer.md)| An object of model property name/value pairs | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

