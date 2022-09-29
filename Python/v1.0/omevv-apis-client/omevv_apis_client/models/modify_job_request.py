from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.modify_job_request_modify_job import ModifyJobRequestModifyJob
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyJobRequest")


@attr.s(auto_attribs=True)
class ModifyJobRequest:
    """
    Attributes:
        modify_job (Union[Unset, ModifyJobRequestModifyJob]):
    """

    modify_job: Union[Unset, ModifyJobRequestModifyJob] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modify_job: Union[Unset, str] = UNSET
        if not isinstance(self.modify_job, Unset):
            modify_job = self.modify_job.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modify_job is not UNSET:
            field_dict["modifyJob"] = modify_job

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _modify_job = d.pop("modifyJob", UNSET)
        modify_job: Union[Unset, ModifyJobRequestModifyJob]
        if isinstance(_modify_job, Unset):
            modify_job = UNSET
        else:
            modify_job = ModifyJobRequestModifyJob(_modify_job)

        modify_job_request = cls(
            modify_job=modify_job,
        )

        modify_job_request.additional_properties = d
        return modify_job_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
