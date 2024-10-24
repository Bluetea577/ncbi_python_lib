# V2MethodPayloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**payload** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_method_payload_request import V2MethodPayloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MethodPayloadRequest from a JSON string
v2_method_payload_request_instance = V2MethodPayloadRequest.from_json(json)
# print the JSON string representation of the object
print V2MethodPayloadRequest.to_json()

# convert the object into a dict
v2_method_payload_request_dict = v2_method_payload_request_instance.to_dict()
# create an instance of V2MethodPayloadRequest from a dict
v2_method_payload_request_form_dict = v2_method_payload_request.from_dict(v2_method_payload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


