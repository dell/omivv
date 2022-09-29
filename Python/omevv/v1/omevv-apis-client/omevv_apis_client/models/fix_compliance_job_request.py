from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FixComplianceJobRequest")


@attr.s(auto_attribs=True)
class FixComplianceJobRequest:
    """
    Attributes:
        job_name (Union[Unset, str]): Name of the job
        job_description (Union[Unset, str]):
        host_ids (Union[Unset, List[int]]): List of vCenter host entity IDs for which management compliance has to be
            fixed
    """

    job_name: Union[Unset, str] = UNSET
    job_description: Union[Unset, str] = UNSET
    host_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        job_description = self.job_description
        host_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.host_ids, Unset):
            host_ids = self.host_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description
        if host_ids is not UNSET:
            field_dict["hostIds"] = host_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_name = d.pop("jobName", UNSET)

        job_description = d.pop("jobDescription", UNSET)

        host_ids = cast(List[int], d.pop("hostIds", UNSET))

        fix_compliance_job_request = cls(
            job_name=job_name,
            job_description=job_description,
            host_ids=host_ids,
        )

        fix_compliance_job_request.additional_properties = d
        return fix_compliance_job_request

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
