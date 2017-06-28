# TeamMemberAccessToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ttl** | **float** | time to live in seconds (2 weeks by default) | [optional] [default to 1209600.0]
**scopes** | **list[str]** | Array of scopes granted to this access token. | [optional] 
**created** | **datetime** |  | [optional] 
**user_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_member_id** | **str** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**portal_member_id** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**team_member** | [**TeamMember**](TeamMember.md) |  | [optional] 
**portal** | [**Portal**](Portal.md) |  | [optional] 
**portal_member** | [**PortalMember**](PortalMember.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


