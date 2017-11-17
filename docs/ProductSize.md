# ProductSize

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | 
**thumbnail** | **str** |  | [optional] 
**folding_type** | **str** |  | [optional] 
**folding_method** | **str** |  | [optional] 
**binding_type** | **str** |  | [optional] 
**double_sided** | **bool** |  | [optional] [default to False]
**die_cut** | **bool** |  | [optional] [default to False]
**unfolded_size** | [**Dimensions**](Dimensions.md) |  | [optional] 
**folded_size** | [**Dimensions**](Dimensions.md) |  | [optional] 
**pdf_size** | [**Dimensions**](Dimensions.md) |  | [optional] 
**pdf_page_count** | **float** |  | [optional] [default to 1.0]
**pdf_dpi** | **float** |  | [optional] [default to 300.0]
**print_profile** | **str** |  | [optional] 
**customer_size** | [**Dimensions**](Dimensions.md) |  | [optional] 
**customer_page_count** | **float** |  | [optional] [default to 1.0]
**max_bleed** | [**Bounds**](Bounds.md) |  | [optional] 
**default_bleed** | [**Bounds**](Bounds.md) |  | [optional] 
**safe_area** | [**Bounds**](Bounds.md) |  | [optional] 
**unit** | **str** |  | [optional] 
**frame** | **float** |  | [optional] [default to 0.0]
**shape** | **str** |  | [optional] 
**orientation** | **str** |  | [optional] 
**format** | **str** |  | 
**envelope_window** | **str** |  | [optional] 
**canvas_image_count** | **float** |  | [optional] [default to 0.0]
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**pdf_color_profile_id** | **str** |  | [optional] 
**type_id** | **str** |  | [optional] 
**type** | [**ProductType**](ProductType.md) |  | [optional] 
**materials** | [**list[ProductMaterial]**](ProductMaterial.md) |  | [optional] 
**size_materials** | [**list[ProductSizeMaterial]**](ProductSizeMaterial.md) |  | [optional] 
**products** | [**list[Product]**](Product.md) |  | [optional] 
**pdf_color_profile** | [**ProductPdfColorProfile**](ProductPdfColorProfile.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


