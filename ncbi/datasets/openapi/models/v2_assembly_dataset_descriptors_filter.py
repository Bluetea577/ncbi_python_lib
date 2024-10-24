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
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2AssemblyDatasetDescriptorsFilter(BaseModel):
    """
    V2AssemblyDatasetDescriptorsFilter
    """ # noqa: E501
    reference_only: Optional[StrictBool] = None
    assembly_source: Optional[V2AssemblyDatasetDescriptorsFilterAssemblySource] = None
    has_annotation: Optional[StrictBool] = None
    exclude_paired_reports: Optional[StrictBool] = None
    exclude_atypical: Optional[StrictBool] = None
    assembly_version: Optional[V2AssemblyDatasetDescriptorsFilterAssemblyVersion] = None
    assembly_level: Optional[List[V2reportsAssemblyLevel]] = None
    first_release_date: Optional[datetime] = None
    last_release_date: Optional[datetime] = None
    search_text: Optional[List[StrictStr]] = None
    is_metagenome_derived: Optional[V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter] = None
    is_type_material: Optional[StrictBool] = None
    is_ictv_exemplar: Optional[StrictBool] = None
    exclude_multi_isolate: Optional[StrictBool] = None
    type_material_category: Optional[V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory] = None
    __properties: ClassVar[List[str]] = ["reference_only", "assembly_source", "has_annotation", "exclude_paired_reports", "exclude_atypical", "assembly_version", "assembly_level", "first_release_date", "last_release_date", "search_text", "is_metagenome_derived", "is_type_material", "is_ictv_exemplar", "exclude_multi_isolate", "type_material_category"]

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
        """Create an instance of V2AssemblyDatasetDescriptorsFilter from a JSON string"""
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
        """Create an instance of V2AssemblyDatasetDescriptorsFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reference_only": obj.get("reference_only"),
            "assembly_source": obj.get("assembly_source"),
            "has_annotation": obj.get("has_annotation"),
            "exclude_paired_reports": obj.get("exclude_paired_reports"),
            "exclude_atypical": obj.get("exclude_atypical"),
            "assembly_version": obj.get("assembly_version"),
            "assembly_level": obj.get("assembly_level"),
            "first_release_date": obj.get("first_release_date"),
            "last_release_date": obj.get("last_release_date"),
            "search_text": obj.get("search_text"),
            "is_metagenome_derived": obj.get("is_metagenome_derived"),
            "is_type_material": obj.get("is_type_material"),
            "is_ictv_exemplar": obj.get("is_ictv_exemplar"),
            "exclude_multi_isolate": obj.get("exclude_multi_isolate"),
            "type_material_category": obj.get("type_material_category")
        })
        return _obj

