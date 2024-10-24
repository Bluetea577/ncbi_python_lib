# V2reportsExtraSequenceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genbank_accession** | **str** |  | [optional] 
**refseq_accession** | **str** |  | [optional] 
**chr_name** | **str** |  | [optional] 
**molecule_type** | **str** |  | [optional] 
**submitter** | **str** |  | [optional] 
**bioproject_accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_extra_sequence_info import V2reportsExtraSequenceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsExtraSequenceInfo from a JSON string
v2reports_extra_sequence_info_instance = V2reportsExtraSequenceInfo.from_json(json)
# print the JSON string representation of the object
print V2reportsExtraSequenceInfo.to_json()

# convert the object into a dict
v2reports_extra_sequence_info_dict = v2reports_extra_sequence_info_instance.to_dict()
# create an instance of V2reportsExtraSequenceInfo from a dict
v2reports_extra_sequence_info_form_dict = v2reports_extra_sequence_info.from_dict(v2reports_extra_sequence_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

