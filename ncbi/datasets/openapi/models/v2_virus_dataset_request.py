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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from ncbi.datasets.openapi.models.v2_table_format import V2TableFormat
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
from ncbi.datasets.openapi.models.v2_virus_table_field import V2VirusTableField
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2VirusDatasetRequest(BaseModel):
    """
    V2VirusDatasetRequest
    """ # noqa: E501
    accessions: Optional[List[StrictStr]] = None
    taxon: Optional[StrictStr] = None
    refseq_only: Optional[StrictBool] = None
    annotated_only: Optional[StrictBool] = None
    released_since: Optional[datetime] = None
    updated_since: Optional[datetime] = None
    host: Optional[StrictStr] = None
    pangolin_classification: Optional[StrictStr] = None
    geo_location: Optional[StrictStr] = None
    usa_state: Optional[StrictStr] = None
    complete_only: Optional[StrictBool] = None
    table_fields: Optional[List[V2VirusTableField]] = None
    include_sequence: Optional[List[V2ViralSequenceType]] = None
    aux_report: Optional[List[V2VirusDatasetReportType]] = None
    format: Optional[V2TableFormat] = None
    use_psg: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["accessions", "taxon", "refseq_only", "annotated_only", "released_since", "updated_since", "host", "pangolin_classification", "geo_location", "usa_state", "complete_only", "table_fields", "include_sequence", "aux_report", "format", "use_psg"]

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
        """Create an instance of V2VirusDatasetRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V2VirusDatasetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessions": obj.get("accessions"),
            "taxon": obj.get("taxon"),
            "refseq_only": obj.get("refseq_only"),
            "annotated_only": obj.get("annotated_only"),
            "released_since": obj.get("released_since"),
            "updated_since": obj.get("updated_since"),
            "host": obj.get("host"),
            "pangolin_classification": obj.get("pangolin_classification"),
            "geo_location": obj.get("geo_location"),
            "usa_state": obj.get("usa_state"),
            "complete_only": obj.get("complete_only"),
            "table_fields": obj.get("table_fields"),
            "include_sequence": obj.get("include_sequence"),
            "aux_report": obj.get("aux_report"),
            "format": obj.get("format"),
            "use_psg": obj.get("use_psg")
        })
        return _obj

