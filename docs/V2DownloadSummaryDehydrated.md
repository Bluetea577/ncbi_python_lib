# V2DownloadSummaryDehydrated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_file_size_mb** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**cli_download_command_line** | **str** |  | [optional] 
**cli_rehydrate_command_line** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_download_summary_dehydrated import V2DownloadSummaryDehydrated

# TODO update the JSON string below
json = "{}"
# create an instance of V2DownloadSummaryDehydrated from a JSON string
v2_download_summary_dehydrated_instance = V2DownloadSummaryDehydrated.from_json(json)
# print the JSON string representation of the object
print V2DownloadSummaryDehydrated.to_json()

# convert the object into a dict
v2_download_summary_dehydrated_dict = v2_download_summary_dehydrated_instance.to_dict()
# create an instance of V2DownloadSummaryDehydrated from a dict
v2_download_summary_dehydrated_form_dict = v2_download_summary_dehydrated.from_dict(v2_download_summary_dehydrated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

