# coding: utf-8

"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets version 2 API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated zip archive](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/large-download/), and retrieve the individual data files at a later time. 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from ncbi.datasets.openapi.models.v2_element_flank_config import V2ElementFlankConfig
from ncbi.datasets.openapi.models.v2_ref_gene_catalog_dataset_request_file_type import V2RefGeneCatalogDatasetRequestFileType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2RefGeneCatalogDatasetRequest(BaseModel):
    """
    V2RefGeneCatalogDatasetRequest
    """ # noqa: E501
    opaque_solr_query: Optional[StrictStr] = None
    files: Optional[List[V2RefGeneCatalogDatasetRequestFileType]] = None
    element_flank_config: Optional[V2ElementFlankConfig] = None
    __properties: ClassVar[List[str]] = ["opaque_solr_query", "files", "element_flank_config"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V2RefGeneCatalogDatasetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of element_flank_config
        if self.element_flank_config:
            _dict['element_flank_config'] = self.element_flank_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V2RefGeneCatalogDatasetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "opaque_solr_query": obj.get("opaque_solr_query"),
            "files": obj.get("files"),
            "element_flank_config": V2ElementFlankConfig.from_dict(obj.get("element_flank_config")) if obj.get("element_flank_config") is not None else None
        })
        return _obj


