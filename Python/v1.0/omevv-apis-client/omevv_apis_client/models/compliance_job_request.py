from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceJobRequest")


@attr.s(auto_attribs=True)
class ComplianceJobRequest:
    """
    Attributes:
        job_name (str): Name of the job
        host_ids (List[int]): List of vCenter host entity IDs for which compliance has to be refreshed
        job_description (Union[Unset, str]): Description of the compliance job
    """

    job_name: str
    host_ids: List[int]
    job_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        host_ids = self.host_ids

        job_description = self.job_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobName": job_name,
                "hostIds": host_ids,
            }
        )
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_name = d.pop("jobName")

        host_ids = cast(List[int], d.pop("hostIds"))

        job_description = d.pop("jobDescription", UNSET)

        compliance_job_request = cls(
            job_name=job_name,
            host_ids=host_ids,
            job_description=job_description,
        )

        compliance_job_request.additional_properties = d
        return compliance_job_request

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
