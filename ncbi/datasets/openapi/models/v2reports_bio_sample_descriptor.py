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
from ncbi.datasets.openapi.models.v2reports_bio_project import V2reportsBioProject
from ncbi.datasets.openapi.models.v2reports_bio_sample_attribute import V2reportsBioSampleAttribute
from ncbi.datasets.openapi.models.v2reports_bio_sample_description import V2reportsBioSampleDescription
from ncbi.datasets.openapi.models.v2reports_bio_sample_id import V2reportsBioSampleId
from ncbi.datasets.openapi.models.v2reports_bio_sample_owner import V2reportsBioSampleOwner
from ncbi.datasets.openapi.models.v2reports_bio_sample_status import V2reportsBioSampleStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2reportsBioSampleDescriptor(BaseModel):
    """
    V2reportsBioSampleDescriptor
    """ # noqa: E501
    accession: Optional[StrictStr] = None
    last_updated: Optional[StrictStr] = None
    publication_date: Optional[StrictStr] = None
    submission_date: Optional[StrictStr] = None
    sample_ids: Optional[List[V2reportsBioSampleId]] = None
    description: Optional[V2reportsBioSampleDescription] = None
    owner: Optional[V2reportsBioSampleOwner] = None
    models: Optional[List[StrictStr]] = None
    bioprojects: Optional[List[V2reportsBioProject]] = None
    package: Optional[StrictStr] = None
    attributes: Optional[List[V2reportsBioSampleAttribute]] = None
    status: Optional[V2reportsBioSampleStatus] = None
    age: Optional[StrictStr] = None
    biomaterial_provider: Optional[StrictStr] = None
    breed: Optional[StrictStr] = None
    collected_by: Optional[StrictStr] = None
    collection_date: Optional[StrictStr] = None
    cultivar: Optional[StrictStr] = None
    dev_stage: Optional[StrictStr] = None
    ecotype: Optional[StrictStr] = None
    geo_loc_name: Optional[StrictStr] = None
    host: Optional[StrictStr] = None
    host_disease: Optional[StrictStr] = None
    identified_by: Optional[StrictStr] = None
    ifsac_category: Optional[StrictStr] = None
    isolate: Optional[StrictStr] = None
    isolate_name_alias: Optional[StrictStr] = None
    isolation_source: Optional[StrictStr] = None
    lat_lon: Optional[StrictStr] = None
    project_name: Optional[StrictStr] = None
    sample_name: Optional[StrictStr] = None
    serovar: Optional[StrictStr] = None
    sex: Optional[StrictStr] = None
    source_type: Optional[StrictStr] = None
    strain: Optional[StrictStr] = None
    sub_species: Optional[StrictStr] = None
    tissue: Optional[StrictStr] = None
    serotype: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["accession", "last_updated", "publication_date", "submission_date", "sample_ids", "description", "owner", "models", "bioprojects", "package", "attributes", "status", "age", "biomaterial_provider", "breed", "collected_by", "collection_date", "cultivar", "dev_stage", "ecotype", "geo_loc_name", "host", "host_disease", "identified_by", "ifsac_category", "isolate", "isolate_name_alias", "isolation_source", "lat_lon", "project_name", "sample_name", "serovar", "sex", "source_type", "strain", "sub_species", "tissue", "serotype"]

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
        """Create an instance of V2reportsBioSampleDescriptor from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sample_ids (list)
        _items = []
        if self.sample_ids:
            for _item in self.sample_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sample_ids'] = _items
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in bioprojects (list)
        _items = []
        if self.bioprojects:
            for _item in self.bioprojects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bioprojects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V2reportsBioSampleDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accession": obj.get("accession"),
            "last_updated": obj.get("last_updated"),
            "publication_date": obj.get("publication_date"),
            "submission_date": obj.get("submission_date"),
            "sample_ids": [V2reportsBioSampleId.from_dict(_item) for _item in obj.get("sample_ids")] if obj.get("sample_ids") is not None else None,
            "description": V2reportsBioSampleDescription.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "owner": V2reportsBioSampleOwner.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "models": obj.get("models"),
            "bioprojects": [V2reportsBioProject.from_dict(_item) for _item in obj.get("bioprojects")] if obj.get("bioprojects") is not None else None,
            "package": obj.get("package"),
            "attributes": [V2reportsBioSampleAttribute.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None,
            "status": V2reportsBioSampleStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "age": obj.get("age"),
            "biomaterial_provider": obj.get("biomaterial_provider"),
            "breed": obj.get("breed"),
            "collected_by": obj.get("collected_by"),
            "collection_date": obj.get("collection_date"),
            "cultivar": obj.get("cultivar"),
            "dev_stage": obj.get("dev_stage"),
            "ecotype": obj.get("ecotype"),
            "geo_loc_name": obj.get("geo_loc_name"),
            "host": obj.get("host"),
            "host_disease": obj.get("host_disease"),
            "identified_by": obj.get("identified_by"),
            "ifsac_category": obj.get("ifsac_category"),
            "isolate": obj.get("isolate"),
            "isolate_name_alias": obj.get("isolate_name_alias"),
            "isolation_source": obj.get("isolation_source"),
            "lat_lon": obj.get("lat_lon"),
            "project_name": obj.get("project_name"),
            "sample_name": obj.get("sample_name"),
            "serovar": obj.get("serovar"),
            "sex": obj.get("sex"),
            "source_type": obj.get("source_type"),
            "strain": obj.get("strain"),
            "sub_species": obj.get("sub_species"),
            "tissue": obj.get("tissue"),
            "serotype": obj.get("serotype")
        })
        return _obj


