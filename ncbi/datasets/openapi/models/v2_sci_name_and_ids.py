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
from pydantic import BaseModel
from ncbi.datasets.openapi.models.v2_sci_name_and_ids_sci_name_and_id import V2SciNameAndIdsSciNameAndId
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2SciNameAndIds(BaseModel):
    """
    V2SciNameAndIds
    """ # noqa: E501
    sci_name_and_ids: Optional[List[V2SciNameAndIdsSciNameAndId]] = None
    __properties: ClassVar[List[str]] = ["sci_name_and_ids"]

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
        """Create an instance of V2SciNameAndIds from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sci_name_and_ids (list)
        _items = []
        if self.sci_name_and_ids:
            for _item in self.sci_name_and_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sci_name_and_ids'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V2SciNameAndIds from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sci_name_and_ids": [V2SciNameAndIdsSciNameAndId.from_dict(_item) for _item in obj.get("sci_name_and_ids")] if obj.get("sci_name_and_ids") is not None else None
        })
        return _obj

